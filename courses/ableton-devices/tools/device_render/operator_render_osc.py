#!/usr/bin/env python3
"""
operator_render_osc.py — fully headless Operator (and generic MIDI-instrument)
demo renderer driven entirely over AbletonOSC. No clicking in Live, no M4L
RENDER button.

What it does, per demo in clip_manifest.yaml `operator_demos`:
  1. apply the demo's `params:` to the Operator on the render track (name→index
     via param_maps/operator.json, enum strings mapped through value_items)
  2. create a MIDI clip on the render track and add the note(s)
  3. arm the resampling capture track, start session record, fire both slots
  4. drive any `automation:` (param ramps / stepped values / multi-note vel)
     on a timer thread while recording
  5. stop, find the freshly recorded .aif in <project>/Samples/Recorded,
     trim + convert to clips/<episode>/<demo_id>.wav, measure loudness
  6. clean up the clips and move on
`mix_from` demos (e.g. op-rhythmic-layered) are synthesised with ffmpeg amix
from their already-rendered sources — no Live pass.

PREREQUISITES (see make_render_template.py):
  - Ableton Live 12 running with the render-template set loaded:
      track 0 = MIDI track with an Operator instrument (device index 0)
      track 1 = audio track, input = Resampling, Monitor = Off, armed
  - AbletonOSC enabled (Preferences → Link/Tempo/MIDI → Control Surfaces)
    and reachable on UDP send :11000 / reply :11001.

USAGE:
  python courses/ableton-devices/tools/device_render/operator_render_osc.py \
      --course-root courses/ableton-devices --episode e01-operator \
      --device Operator
  # single demo:           --demo op-poly-bell-step3
  # list status:           --list
  # plan without touching Live: --dry-run
  # re-render everything:  --clear  (then run again)
"""
from __future__ import annotations

import argparse
import json
import queue
import shutil
import subprocess
import sys
import threading
import time
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.stderr.write("pyyaml missing. uv pip install pyyaml\n")
    sys.exit(2)

try:
    from pythonosc.udp_client import SimpleUDPClient
    from pythonosc.dispatcher import Dispatcher
    from pythonosc.osc_server import BlockingOSCUDPServer
except ImportError:
    sys.stderr.write("python-osc missing. uv pip install python-osc\n")
    sys.exit(2)

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[3] / "shared" / "tools"))
sys.path.insert(0, str(HERE))
from _course_lib import load_course, episodes_dir, lessons_dir, build_audio  # noqa: E402
# reuse the proven helpers from the M4L driver
from device_render import expand_pattern, normalize_midi, mix_demos, find_rendered  # noqa: E402


# ── note names → MIDI, Ableton DISPLAY convention (middle C = C3 = 60) ───────
_SEMI = {"C": 0, "C#": 1, "DB": 1, "D": 2, "D#": 3, "EB": 3, "E": 4, "F": 5,
         "F#": 6, "GB": 6, "G": 7, "G#": 8, "AB": 8, "A": 9, "A#": 10, "BB": 10, "B": 11}


def note_to_midi(name: str) -> int:
    s = name.strip()
    i = 1
    if len(s) > 1 and s[1] in "#b":
        i = 2
    pitch, octave = s[:i], int(s[i:])
    return _SEMI[pitch.upper()] + 12 * (octave + 2)


# ── OSC client with ask/reply ────────────────────────────────────────────────
class Live:
    def __init__(self, send_port=11000, reply_port=11001, host="127.0.0.1", timeout=3.0):
        self.timeout = timeout
        self._q: queue.Queue = queue.Queue()
        disp = Dispatcher()
        disp.set_default_handler(lambda addr, *a: self._q.put((addr, a)))
        self._srv = BlockingOSCUDPServer((host, reply_port), disp)
        threading.Thread(target=self._srv.serve_forever, daemon=True).start()
        self._cli = SimpleUDPClient(host, send_port)

    def send(self, addr, *args):
        self._cli.send_message(addr, list(args))

    def ask(self, addr, *args):
        while not self._q.empty():
            self._q.get_nowait()
        self.send(addr, *args)
        try:
            return self._q.get(timeout=self.timeout)[1]
        except queue.Empty:
            return None

    def close(self):
        self._srv.shutdown()

    def assert_connected(self):
        r = self.ask("/live/test")
        if not r or "ok" not in [str(x) for x in r]:
            raise RuntimeError(
                "AbletonOSC did not answer /live/test. Is Live running with "
                "AbletonOSC enabled (Preferences → Link/Tempo/MIDI → Control Surfaces)?"
            )


# ── param-map translation ────────────────────────────────────────────────────
class ParamMap:
    def __init__(self, path: Path):
        data = json.loads(path.read_text())
        self.by_name = {p["name"]: p for p in data["parameters"]}

    def resolve(self, name: str, value):
        """Return (index, float_value) for an OSC set, or None if unknown name."""
        p = self.by_name.get(name)
        if p is None:
            return None
        idx = p["index"]
        if p["is_quantized"] and isinstance(value, str):
            items = p.get("value_items") or []
            if value in items:
                return idx, float(items.index(value))
            raise ValueError(f"{name!r}: {value!r} not in {items}")
        v = float(value)
        lo, hi = float(p["min"]), float(p["max"])
        return idx, max(lo, min(hi, v))


# ── render core ──────────────────────────────────────────────────────────────
class Renderer:
    def __init__(self, live: Live, pm: ParamMap, *, op_track: int, op_device: int,
                 cap_track: int, tempo: float, recorded_dir: Path, tail_s: float,
                 settle_s: float, output_dir: Path, verbose=True):
        self.live = live
        self.pm = pm
        self.op_track = op_track
        self.op_device = op_device
        self.cap_track = cap_track
        self.tempo = tempo
        self.recorded_dir = recorded_dir
        self.tail_s = tail_s
        self.settle_s = settle_s
        self.output_dir = output_dir
        self.verbose = verbose

    def log(self, *a):
        if self.verbose:
            print(*a, flush=True)

    def set_param(self, name: str, value):
        r = self.pm.resolve(name, value)
        if r is None:
            self.log(f"    [warn] unknown param {name!r}; skipping")
            return
        idx, v = r
        self.live.send("/live/device/set/parameter/value", self.op_track, self.op_device, idx, v)

    def apply_params(self, params: dict):
        # Operator is not reset between demos, so the manifest sets every relevant
        # param explicitly. Apply Algorithm first, then the rest.
        if "Algorithm" in params:
            self.set_param("Algorithm", params["Algorithm"])
        for k, v in params.items():
            if k == "Algorithm":
                continue
            self.set_param(k, v)

    def _beats(self, seconds: float) -> float:
        return seconds * self.tempo / 60.0

    def _clear_slot(self, track: int, slot: int):
        has = self.live.ask("/live/clip_slot/get/has_clip", track, slot)
        if has and len(has) >= 3 and bool(has[2]):
            self.live.send("/live/clip_slot/delete_clip", track, slot)
            time.sleep(0.1)

    def _make_midi_clip(self, midi: dict, slot: int = 0) -> float:
        """Create a MIDI clip on the Operator track and add notes. Returns the
        length in seconds the recording must cover."""
        length_s = float(midi.get("length_s") or 2.0)
        # collect notes
        notes = []
        if midi.get("notes"):
            for n in midi["notes"]:
                t = float(n.get("t", 0.0))
                dur = float(n.get("dur_s", length_s - t))
                notes.append((note_to_midi(n["note"]), t, dur, int(n.get("vel", 100))))
        else:
            note = midi.get("note", "C3")
            notes.append((note_to_midi(note), 0.0, length_s, int(midi.get("vel", 100))))

        clip_beats = max(self._beats(length_s) + 0.25, 1.0)
        self._clear_slot(self.op_track, slot)
        self.live.send("/live/clip_slot/create_clip", self.op_track, slot, clip_beats)
        time.sleep(0.15)
        # disable looping so the clip plays once
        self.live.send("/live/clip/set/looping", self.op_track, slot, 0)
        args = [self.op_track, slot]
        for pitch, t, dur, vel in notes:
            args += [pitch, self._beats(t), self._beats(dur), vel, 0]
        self.live.send("/live/clip/add/notes", *args)
        time.sleep(0.1)
        return length_s

    def _arm_capture(self):
        self.live.send("/live/track/set/arm", self.cap_track, 1)
        # belt-and-suspenders: input monitor Off so we capture the resampling bus
        self.live.send("/live/track/set/current_monitoring_state", self.cap_track, 2)

    def _clear_recorded(self):
        """Wipe the Recorded folder so only THIS demo's captures are present.
        Safe: the prior demo's file was already copied out."""
        if not self.recorded_dir.exists():
            return
        for p in self.recorded_dir.iterdir():
            if p.suffix.lower() in (".aif", ".aiff", ".wav", ".asd"):
                try:
                    p.unlink()
                except OSError:
                    pass

    def _best_recording(self, after_ts: float, min_bytes: int = 50_000) -> Path | None:
        """Pick the LARGEST recording (a stray short/0-byte capture is sometimes
        left alongside the real one; the full take is always the biggest)."""
        if not self.recorded_dir.exists():
            return None
        cands = []
        for ext in ("*.aif", "*.wav", "*.aiff"):
            for p in self.recorded_dir.glob(ext):
                st = p.stat()
                if st.st_mtime >= after_ts - 1 and st.st_size >= min_bytes:
                    cands.append(p)
        if not cands:
            return None
        return max(cands, key=lambda p: p.stat().st_size)

    def _automation_thread(self, automation: dict, length_s: float, stop: threading.Event):
        """Drive ramps / stepped param changes during recording."""
        def run():
            t0 = time.time()
            for name, spec in automation.items():
                pass  # handled below per-spec; we run a single combined loop
            # Build per-param schedules
            ramps = {}
            steps = {}
            for name, spec in automation.items():
                if "from" in spec and "to" in spec:
                    ramps[name] = spec
                elif "steps" in spec:
                    steps[name] = spec
            # fire step[0] immediately
            for name, spec in steps.items():
                self.set_param(name, spec["steps"][0])
            next_step_idx = {name: 1 for name in steps}
            while not stop.is_set():
                t = time.time() - t0
                for name, spec in ramps.items():
                    dur = float(spec.get("ramp_s", length_s))
                    frac = min(1.0, t / dur) if dur > 0 else 1.0
                    val = spec["from"] + (spec["to"] - spec["from"]) * frac
                    self.set_param(name, val)
                for name, spec in steps.items():
                    step_s = float(spec.get("step_s", 1.0))
                    i = next_step_idx[name]
                    if i < len(spec["steps"]) and t >= i * step_s:
                        self.set_param(name, spec["steps"][i])
                        next_step_idx[name] = i + 1
                time.sleep(1.0 / 30.0)
        threading.Thread(target=run, daemon=True).start()

    def _concat(self, segs: list[Path], dst: Path, gap_s: float = 0.45):
        """Concatenate segments with a short silence between (for A/B demos)."""
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            sil = Path(td) / "sil.wav"
            subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-f", "lavfi",
                            "-i", "anullsrc=r=48000:cl=stereo", "-t", str(gap_s),
                            "-c:a", "pcm_s24le", str(sil)], check=True)
            lst = Path(td) / "l.txt"
            parts = []
            for i, s in enumerate(segs):
                if i: parts.append(f"file {sil}")
                parts.append(f"file {s.resolve()}")
            lst.write_text("\n".join(parts))
            subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-f", "concat",
                            "-safe", "0", "-i", str(lst), "-c:a", "pcm_s24le", str(dst)], check=True)

    def _render_ab(self, demo: dict) -> dict:
        """A/B demo: render segment A and B (one param differs), concat A | B."""
        did = demo["id"]
        ab_param = demo["ab_param"]; ab_values = demo["ab_values"]
        self.log(f"    A/B on {ab_param!r}: {ab_values[0]} | {ab_values[1]}")
        segs = []
        for i, val in enumerate(ab_values[:2]):
            sub = dict(demo)
            sub.pop("ab_param", None); sub.pop("ab_values", None)
            sub["params"] = {**(demo.get("params") or {}), ab_param: val}
            sub["id"] = f"{did}__seg{i}"
            self.render_one(sub)
            p = self.output_dir / f"{did}__seg{i}.wav"
            if p.exists(): segs.append(p)
        out = self.output_dir / f"{did}.wav"
        if len(segs) == 2:
            self._concat(segs, out)
            for s in segs: s.unlink()
            db = measure_db(out)
            self.log(f"    → {out.name} (A/B)  mean={db['mean']:.1f}dB peak={db['peak']:.1f}dB")
            return {"id": did, "status": "ok" if db["mean"] > -45 else "quiet", "out": str(out)}
        return {"id": did, "status": "ab-incomplete"}

    def render_one(self, demo: dict) -> dict:
        did = demo["id"]
        self.log(f"  ▶ {did}")
        if demo.get("ab_param") and demo.get("ab_values") and len(demo["ab_values"]) >= 2:
            return self._render_ab(demo)
        params = demo.get("params") or {}
        if params:
            self.apply_params(params)
            time.sleep(self.settle_s)

        midi = normalize_midi(demo.get("midi"), demo.get("duration_s")) or {"note": "C3", "length_s": 2.0}
        length_s = self._make_midi_clip(midi, slot=0)
        record_s = max(length_s, float(demo.get("duration_s") or length_s))

        self._arm_capture()
        out = self.output_dir / f"{did}.wav"

        # The FIRST capture after a fresh arm can truncate; retry if the take
        # comes back much shorter than expected.
        for attempt in range(3):
            self._clear_slot(self.cap_track, 0)
            time.sleep(0.1)
            ts = time.time()
            # start session record, then fire both slots (Operator MIDI + capture audio)
            self.live.send("/live/song/set/session_record", 1)
            self.live.send("/live/clip_slot/fire", self.op_track, 0)
            self.live.send("/live/clip_slot/fire", self.cap_track, 0)

            stop = threading.Event()
            if demo.get("automation"):
                self._automation_thread(demo["automation"], length_s, stop)

            time.sleep(record_s + self.tail_s)
            stop.set()
            self.live.send("/live/song/set/session_record", 0)
            self.live.send("/live/song/stop_playing")
            time.sleep(0.4)

            rec = self._best_recording(ts)
            if rec:
                last = -1
                for _ in range(20):
                    sz = rec.stat().st_size
                    if sz == last and sz > 1024:
                        break
                    last = sz
                    time.sleep(0.2)
                self._finalize(rec, out, record_s)
                got = _audio_dur(out)
                if got >= 0.6 * record_s or record_s < 1.5:
                    break
                self.log(f"    [retry {attempt+1}] short take ({got:.1f}s < {record_s:.1f}s), re-firing")
            else:
                self.log(f"    [retry {attempt+1}] no recording yet")
            self._clear_slot(self.cap_track, 0)
        else:
            if not out.exists():
                self.log(f"    [fail] no usable recording for {did}")
                return {"id": did, "status": "no-recording"}

        # cleanup clips
        self._clear_slot(self.op_track, 0)
        self._clear_slot(self.cap_track, 0)

        db = measure_db(out)
        status = "ok" if db["mean"] > -45 else "quiet"
        self.log(f"    → {out.name}  mean={db['mean']:.1f}dB peak={db['peak']:.1f}dB [{status}]")
        return {"id": did, "status": status, "out": str(out), "mean_db": db["mean"], "peak_db": db["peak"]}

    def _finalize(self, src: Path, dst: Path, duration_s: float):
        dst.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
             "-i", str(src), "-t", f"{duration_s:.3f}",
             "-ar", "48000", "-ac", "2", "-c:a", "pcm_s24le", str(dst)],
            check=True,
        )
        trim_trailing_silence(dst)  # drop the dead air after a pluck decays


def trim_trailing_silence(path: Path, keep_tail_s: float = 0.4, thr_db: float = -50.0):
    """Drop trailing silence (e.g. the dead air after a pluck decays), keeping a
    short tail. No-op for sustained tones. In-place, 24-bit."""
    try:
        import soundfile as sf
        import numpy as np
    except ImportError:
        return
    x, sr = sf.read(str(path))
    mono = x.mean(1) if x.ndim > 1 else x
    peak = float(np.abs(mono).max())
    if peak <= 0:
        return
    thr = peak * (10 ** (thr_db / 20))
    nz = np.where(np.abs(mono) > thr)[0]
    if len(nz) == 0:
        return
    end = min(len(mono), int(nz[-1]) + int(keep_tail_s * sr))
    if end < len(mono) - int(0.05 * sr):
        sf.write(str(path), x[:end], sr, subtype="PCM_24")


def _audio_dur(path: Path) -> float:
    try:
        r = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", str(path)], capture_output=True, text=True)
        return float(r.stdout.strip())
    except (ValueError, subprocess.SubprocessError):
        return 0.0


def measure_db(path: Path) -> dict:
    r = subprocess.run(
        ["ffmpeg", "-hide_banner", "-nostats", "-i", str(path),
         "-af", "volumedetect", "-f", "null", "-"],
        capture_output=True, text=True,
    )
    mean = peak = -99.0
    for line in r.stderr.splitlines():
        if "mean_volume:" in line:
            mean = float(line.split("mean_volume:")[1].split("dB")[0])
        elif "max_volume:" in line:
            peak = float(line.split("max_volume:")[1].split("dB")[0])
    return {"mean": mean, "peak": peak}


def load_demos(manifest: dict, demos_key: str) -> list[dict]:
    return manifest.get(demos_key) or []


def find_operator_track(live: Live, device_class: str = "Operator") -> int | None:
    n = live.ask("/live/song/get/num_tracks")
    n = int(n[0]) if n else 0
    for t in range(n):
        cls = live.ask("/live/track/get/devices/class_name", t)
        names = [str(x) for x in (cls[1:] if cls and len(cls) > 1 else [])]
        if any(device_class in x for x in names):
            return t
    return None


def _is_resampling_capable(live: Live, t: int) -> list[str]:
    types = live.ask("/live/track/get/available_input_routing_types", t)
    return [str(x) for x in (types[1:] if types and len(types) > 1 else [])]


def ensure_capture_track(live: Live, op_track: int) -> tuple[int, str | None, list[str]]:
    """Create a FRESH audio capture track (this is what reliably records; reusing
    an existing track can capture 0 bytes), route it to Resampling, arm +
    monitor-off, and DISARM every other track so exactly one track records.
    (Old disarmed capture tracks from prior runs are harmless.)"""
    # disarm all existing tracks so only the new capture track records
    n = int(live.ask("/live/song/get/num_tracks")[0])
    for t in range(n):
        live.send("/live/track/set/arm", t, 0)
    live.send("/live/song/create_audio_track", -1)
    time.sleep(0.5)
    n = int(live.ask("/live/song/get/num_tracks")[0])
    cap = n - 1
    avail = _is_resampling_capable(live, cap)
    target = "Resampling" if "Resampling" in avail else next(
        (a for a in avail if "resampl" in a.lower()), None)
    if target:
        live.send("/live/track/set/input_routing_type", cap, target)
    live.send("/live/track/set/arm", cap, 1)
    live.send("/live/track/set/current_monitoring_state", cap, 2)  # 2 = Off
    time.sleep(0.3)
    return cap, target, avail


def selftest(live: Live) -> int:
    live.assert_connected()
    n = live.ask("/live/song/get/num_tracks")
    n = int(n[0]) if n else 0
    print(f"Connected. tracks={n}")
    for t in range(n):
        nm = live.ask("/live/track/get/name", t)
        cls = live.ask("/live/track/get/devices/class_name", t)
        nm = nm[1] if nm and len(nm) > 1 else "?"
        classes = [str(x) for x in (cls[1:] if cls and len(cls) > 1 else [])]
        print(f"  T{t}: {nm!r}  devices={classes}")
    op = find_operator_track(live)
    if op is None:
        print("\n✗ No Operator found. Drag an Operator instrument onto a MIDI track.")
        return 1
    print(f"\n✓ Operator on track {op}. Ready to render.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--course-root", required=True)
    ap.add_argument("--episode", "--lesson", dest="episode", required=True)
    ap.add_argument("--device", default="Operator")
    ap.add_argument("--demos-key", default="operator_demos")
    ap.add_argument("--demo", help="filter to a single demo id")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--clear", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--op-track", type=int, default=None, help="Operator track index (default: auto-detect)")
    ap.add_argument("--op-device", type=int, default=0)
    ap.add_argument("--cap-track", type=int, default=None, help="capture track index (default: create one)")
    ap.add_argument("--selftest", action="store_true", help="probe Live + confirm Operator, then exit")
    ap.add_argument("--tempo", type=float, default=120.0)
    ap.add_argument("--tail-s", type=float, default=0.6)
    ap.add_argument("--settle-s", type=float, default=0.25)
    ap.add_argument("--recorded-dir", help="<project>/Samples/Recorded (default: derive from --project)")
    ap.add_argument("--project", help="render project folder (has Samples/Recorded)")
    args = ap.parse_args()

    cfg = load_course(args.course_root)
    content_kind = cfg.get("content_kind", "lesson")
    base = episodes_dir(cfg) if content_kind == "episode" else lessons_dir(cfg)
    episode_dir = base / args.episode
    manifest = yaml.safe_load((episode_dir / "clip_manifest.yaml").read_text()) or {}
    demos = load_demos(manifest, args.demos_key)
    if args.demo:
        demos = [d for d in demos if d["id"] == args.demo]
        if not demos:
            sys.stderr.write(f"demo {args.demo!r} not found\n")
            return 2

    output_dir = build_audio(cfg) / "clips" / args.episode
    output_dir.mkdir(parents=True, exist_ok=True)

    if args.clear:
        n = 0
        for d in demos:
            for ext in (".wav", ".aif", ".aiff"):
                p = output_dir / f"{d['id']}{ext}"
                if p.exists():
                    p.unlink(); n += 1
        print(f"Cleared {n} file(s)")
        return 0

    if args.list:
        for d in demos:
            f = find_rendered(d["id"], output_dir)
            mark = "✓" if f else " "
            extra = ""
            if f:
                db = measure_db(f)
                extra = f"  mean={db['mean']:.1f}dB"
                if db["mean"] <= -45:
                    extra += "  ⚠ QUIET"
            print(f"  [{mark}] {d['id']}{extra}")
        return 0

    if args.dry_run:
        for d in demos:
            print(f"{d['id']}: midi={normalize_midi(d.get('midi'), d.get('duration_s'))} "
                  f"params={len(d.get('params') or {})} automation={list((d.get('automation') or {}).keys())} "
                  f"mix_from={d.get('mix_from')}")
        return 0

    if args.selftest:
        live = Live()
        try:
            return selftest(live)
        finally:
            live.close()

    # resolve recorded dir
    if args.recorded_dir:
        recorded_dir = Path(args.recorded_dir).expanduser()
    elif args.project:
        recorded_dir = Path(args.project).expanduser() / "Samples" / "Recorded"
    else:
        sys.stderr.write("need --recorded-dir or --project (where Live writes resampled .aif)\n")
        return 2

    pm = ParamMap(HERE / "param_maps" / f"{args.device.lower()}.json")
    live = Live()
    try:
        live.assert_connected()
        op_track = args.op_track
        if op_track is None:
            op_track = find_operator_track(live)
            if op_track is None:
                sys.stderr.write("No Operator track found. Drag an Operator onto a MIDI track.\n")
                return 2
        cap_track = args.cap_track
        if cap_track is None:
            cap_track, rt, avail = ensure_capture_track(live, op_track)
            if not rt:
                sys.stderr.write(f"Could not route Resampling on the capture track. "
                                 f"Available inputs: {avail}\n")
                return 2
            print(f"Capture track {cap_track} (reused), routed to {rt!r}, armed, others disarmed.")
        print(f"Connected. op_track={op_track} cap_track={cap_track} "
              f"tempo={args.tempo} recorded={recorded_dir}")
        live.send("/live/song/set/tempo", args.tempo)
        r = Renderer(live, pm, op_track=op_track, op_device=args.op_device,
                     cap_track=cap_track, tempo=args.tempo, recorded_dir=recorded_dir,
                     tail_s=args.tail_s, settle_s=args.settle_s, output_dir=output_dir)
        results = []
        def _composed(x):
            return x.get("mix_from") or x.get("concat_from")
        # render real demos first, then composed (mix/concat) demos
        for d in [x for x in demos if not _composed(x)]:
            if find_rendered(d["id"], output_dir):
                print(f"  [skip] {d['id']} already rendered")
                continue
            results.append(r.render_one(d))
            time.sleep(0.3)
        for d in [x for x in demos if _composed(x)]:
            if find_rendered(d["id"], output_dir):
                continue
            if d.get("concat_from"):
                segs = [p for s in d["concat_from"] if (p := find_rendered(s, output_dir))]
                if len(segs) == len(d["concat_from"]):
                    r._concat(segs, output_dir / f"{d['id']}.wav")
                    results.append({"id": d["id"], "status": "ok"})
                    print(f"  [concat] {d['id']} ← {d['concat_from']} → ok")
                else:
                    results.append({"id": d["id"], "status": "concat-missing-src"})
            else:
                dest = mix_demos(d["mix_from"], d["id"], output_dir)
                results.append({"id": d["id"], "status": "ok" if dest else "mix-failed"})
                print(f"  [mix] {d['id']} ← {d['mix_from']} → {'ok' if dest else 'FAILED'}")
    finally:
        live.close()

    (output_dir / "_osc_render_status.json").write_text(json.dumps(results, indent=2))
    ok = sum(1 for x in results if x.get("status") == "ok")
    print(f"\nRendered {ok}/{len(results)} ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())

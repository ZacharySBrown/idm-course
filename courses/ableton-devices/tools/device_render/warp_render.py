#!/usr/bin/env python3
"""
warp_render.py — render the ep05 WARP demos by driving Ableton's REAL warp engine
over AbletonOSC + the resampling capture (same trick the synth renderer uses).

The user loads the source breaks/clips into Live (the API can't load samples into
clips). This tool, per demo: sets the source clip's warp_mode (+ pitch for transpose),
sets the song tempo to a stretch ratio that exposes the mode's character, fires the
clip while a resampling track records, then trims the capture to clips/e05/<id>.wav.

Only mode+pitch+tempo are settable over the LOM — Grain Size / Flux / Complex-Pro
Formants are NOT exposed, so those demos stay as recipe cards (headless:false).

Usage:
  python warp_render.py --project "operator-template Project" --breaks-track 26
  # --demo <id>   one demo
"""
from __future__ import annotations
import argparse, subprocess, sys, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from operator_render_osc import (Live, ensure_capture_track, measure_db,  # noqa: E402
                                 trim_trailing_silence, _audio_dur)

WARP = {"Beats": 0, "Tones": 1, "Texture": 2, "Re-Pitch": 3, "Complex": 4, "Complex Pro": 6}
OUT = HERE.parents[3] / "build" / "ableton-devices" / "audio" / "clips" / "e05-warp-modes"

# id, break-slot, [mode(s)], tempo (stretch ratio vs ~120 native), record_s, pitch_semitones
# A/B demos list two modes → rendered as two segments, concatenated.
DEMOS = [
    ("texture-cloud",        0, ["Texture"],            58, 3.8,  0),   # amen → granular cloud (2x stretch)
    ("tones-warble",         0, ["Tones"],              58, 3.8,  0),   # amen → Tones can't pitch-track a drum loop → warble
    ("repitch-halfspeed",    0, ["Re-Pitch"],           60, 3.8,  0),   # amen → varispeed octave-down (half tempo)
    ("beats-stutter-freeze", 0, ["Beats"],              75, 3.8,  0),   # amen → Beats keeps transients while stretched
    ("transient-survival-ab",0, ["Beats", "Complex"],   72, 3.5,  0),   # A=transients survive, B=smear
    ("aliasing-on-speedup",  0, ["Re-Pitch"],          120, 3.5, 12),   # amen +12st → bright HF aliasing (Re-Pitch)
]


def finalize(src: Path, dst: Path, dur: float):
    dst.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", str(src),
                    "-t", f"{dur:.3f}", "-ar", "48000", "-ac", "2", "-c:a", "pcm_s24le", str(dst)],
                   check=True)
    trim_trailing_silence(dst)


def concat(segs, dst, gap=0.4):
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        sil = Path(td) / "s.wav"
        subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-f", "lavfi",
                        "-i", "anullsrc=r=48000:cl=stereo", "-t", str(gap), "-c:a", "pcm_s24le", str(sil)], check=True)
        lst = Path(td) / "l.txt"
        parts = []
        for i, s in enumerate(segs):
            if i: parts.append(f"file {sil}")
            parts.append(f"file {s.resolve()}")
        lst.write_text("\n".join(parts))
        subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-f", "concat",
                        "-safe", "0", "-i", str(lst), "-c:a", "pcm_s24le", str(dst)], check=True)


def render_one(live, cap, rec_dir, bt, slot, modes, tempo, rec_s, pitch, did):
    live.send("/live/song/set/tempo", float(tempo))
    live.send("/live/clip/set/pitch_coarse", bt, slot, int(pitch))
    segs = []
    for i, mode in enumerate(modes):
        live.send("/live/clip/set/warping", bt, slot, 1)
        live.send("/live/clip/set/warp_mode", bt, slot, WARP[mode])
        time.sleep(0.3)
        seg = OUT / (f"{did}__seg{i}.wav" if len(modes) > 1 else f"{did}.wav")
        # The FIRST resampling capture on a fresh armed track returns 0 bytes /
        # truncated; retry until we get a take of roughly the requested length.
        rec = None
        for attempt in range(4):
            live.send("/live/clip_slot/delete_clip", cap, 0); time.sleep(0.15)
            for p in rec_dir.glob("*.aif"):
                try: p.unlink()
                except OSError: pass
            ts = time.time()
            live.send("/live/song/set/session_record", 1)
            live.send("/live/clip_slot/fire", bt, slot)
            live.send("/live/clip_slot/fire", cap, 0)
            time.sleep(rec_s + 0.8)
            live.send("/live/song/set/session_record", 0)
            live.send("/live/clip/stop", bt, slot)
            live.send("/live/song/stop_playing")
            time.sleep(0.5)
            cands = [p for p in rec_dir.glob("*.aif") if p.stat().st_mtime >= ts - 1 and p.stat().st_size > 40_000]
            if cands:
                rec = max(cands, key=lambda p: p.stat().st_size)
                last = -1
                for _ in range(15):
                    sz = rec.stat().st_size
                    if sz == last: break
                    last = sz; time.sleep(0.2)
                finalize(rec, seg, rec_s)
                if _audio_dur(seg) >= 0.6 * rec_s:
                    break
            print(f"    [retry {attempt+1}] {did} seg{i} short/empty")
        if not rec or not seg.exists():
            print(f"    [fail] no capture for {did} seg{i}"); continue
        segs.append(seg)
        print(f"    seg{i} {mode}: {seg.name}  ({_audio_dur(seg):.1f}s)")
    out = OUT / f"{did}.wav"
    if len(segs) > 1:
        concat(segs, out)
        for s in segs: s.unlink()
    db = measure_db(out) if out.exists() else {"mean": -99, "peak": -99}
    print(f"  ▶ {did}: peak={db['peak']:.1f}dB [{'ok' if db['peak'] > -40 else 'LOW'}]")
    return out.exists()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", required=True)
    ap.add_argument("--breaks-track", type=int, required=True)
    ap.add_argument("--demo")
    args = ap.parse_args()
    rec_dir = Path(args.project).expanduser() / "Samples" / "Recorded"
    live = Live()
    live.assert_connected()
    cap, rt, _ = ensure_capture_track(live, args.breaks_track)
    print(f"capture track {cap} ({rt}); breaks track {args.breaks_track}")
    demos = [d for d in DEMOS if (not args.demo or d[0] == args.demo)]
    ok = 0
    for did, slot, modes, tempo, rec_s, pitch in demos:
        if render_one(live, cap, rec_dir, args.breaks_track, slot, modes, tempo, rec_s, pitch, did):
            ok += 1
        time.sleep(0.3)
    live.send("/live/song/set/tempo", 120.0)
    live.close()
    print(f"\nwarp-rendered {ok}/{len(demos)}")


if __name__ == "__main__":
    main()

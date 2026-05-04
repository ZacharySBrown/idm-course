#!/usr/bin/env python3
"""
device_render.py — generic driver for any Live-device render pipeline.

One tool for every Ableton device covered by the course. Pairs with one of two
M4L devices:

    --kind midi-instrument   →  MidiInstrumentRender.amxd  (e01 Operator,
                                e02 Analog, e03 Wavetable, e04 Meld,
                                e06 Drum Rack, e07 Granulator)
    --kind audio-fx          →  AudioFxRender.amxd         (e05 Warp Modes,
                                e08 Spectral, e10 Racks)

Splits responsibility:

    Python (this file)            M4L device
    ────────────────────          ──────────────────────────────────────
    read clip_manifest.yaml   →   spec.json
    write spec.json           ↓
    [user clicks RENDER]      ←   read spec.json
    watch output dir + NDJSON ↔   apply LOM params, drop MIDI clip OR fire
                                  audio clip, freeze track, copy WAV out,
                                  emit NDJSON event per demo

Usage:
    # ep01 Operator (default kind = midi-instrument, default demos-key = operator_demos)
    python courses/ableton-devices/tools/device_render/device_render.py \\
        --course-root courses/ableton-devices --episode e01-operator \\
        --device Operator

    # Future ep02 Analog
    python courses/ableton-devices/tools/device_render/device_render.py \\
        --course-root courses/ableton-devices --episode e02-analog \\
        --device Analog --demos-key analog_demos

    # Future ep05 Warp Modes (audio fx)
    python courses/ableton-devices/tools/device_render/device_render.py \\
        --course-root courses/ableton-devices --episode e05-warp-modes \\
        --kind audio-fx --device "Warp" --demos-key warp_demos

Convenience flags:
    --demo <id>   filter to a single demo
    --list        list demo render status, then exit
    --clear       wipe rendered WAVs (force re-render)
    --dry-run     print spec, don't write

Output paths:
    spec:       <build_root>/tmp/device-render/<episode>/spec.json
    events:     <build_root>/tmp/device-render/<episode>/events.ndjson
    rendered:   <build_root>/audio/clips/<episode>/<demo_id>.wav
                (same dir as extract_clips.py — build_episode reads either)
"""
from __future__ import annotations

import argparse
import json
import shutil
import signal
import sys
import time
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.stderr.write("pyyaml missing. uv pip install pyyaml\n")
    sys.exit(2)

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "shared" / "tools"))
from _course_lib import load_course, episodes_dir, lessons_dir, build_audio  # noqa: E402


SPEC_VERSION = 2
KIND_CHOICES = ("midi-instrument", "audio-fx")


def find_episode_dir(cfg: dict, episode_id: str) -> Path:
    content_kind = cfg.get("content_kind", "lesson")
    base = episodes_dir(cfg) if content_kind == "episode" else lessons_dir(cfg)
    return base / episode_id


def build_spec(
    manifest: dict,
    episode_id: str,
    device_class: str,
    kind: str,
    demos_key: str,
    output_dir: Path,
    events_path: Path,
) -> dict:
    demos = manifest.get(demos_key) or []
    return {
        "spec_version": SPEC_VERSION,
        "episode_id": episode_id,
        "device_class": device_class,
        "kind": kind,
        "output_dir": str(output_dir),
        "events_path": str(events_path),
        "demos": [
            {
                "id": d["id"],
                "description": d.get("description", ""),
                "duration_s": d.get("duration_s"),
                "midi": d.get("midi"),
                "automation": d.get("automation"),
                "params": d.get("params"),
                "notes": d.get("notes"),
            }
            for d in demos
        ],
    }


def find_rendered(demo_id: str, output_dir: Path) -> Path | None:
    for ext in (".wav", ".aif", ".aiff"):
        p = output_dir / f"{demo_id}{ext}"
        if p.exists():
            return p
    return None


def status_for_demo(demo_id: str, output_dir: Path) -> str:
    return "rendered" if find_rendered(demo_id, output_dir) else "pending"


def print_status(spec: dict, output_dir: Path) -> tuple[int, int]:
    rendered = 0
    for d in spec["demos"]:
        s = status_for_demo(d["id"], output_dir)
        marker = "✓" if s == "rendered" else " "
        size = ""
        if s == "rendered":
            wav = find_rendered(d["id"], output_dir)
            size = f" ({wav.stat().st_size // 1024}KB {wav.suffix})" if wav else ""
            rendered += 1
        print(f"  [{marker}] {d['id']}{size}")
    return rendered, len(spec["demos"])


def watch(spec: dict, output_dir: Path, events_path: Path) -> int:
    interrupted = {"flag": False}
    signal.signal(signal.SIGINT, lambda *_: interrupted.__setitem__("flag", True))

    pending = {d["id"] for d in spec["demos"]}
    pending -= {d["id"] for d in spec["demos"] if status_for_demo(d["id"], output_dir) == "rendered"}

    if not pending:
        print("\nAll demos already rendered.")
        return 0

    device_label = spec.get("device_class", "?")
    kind = spec.get("kind", "midi-instrument")
    amxd_name = "MidiInstrumentRender.amxd" if kind == "midi-instrument" else "AudioFxRender.amxd"
    print(f"\nWaiting on {len(pending)} demo(s). Click RENDER in {amxd_name} (device={device_label}). Ctrl-C to exit.")

    events_path.parent.mkdir(parents=True, exist_ok=True)
    if not events_path.exists():
        events_path.touch()

    last_offset = events_path.stat().st_size
    last_dump = time.time()

    while pending and not interrupted["flag"]:
        time.sleep(0.5)

        try:
            with events_path.open("r") as f:
                f.seek(last_offset)
                new = f.read()
                last_offset = f.tell()
        except FileNotFoundError:
            new = ""
        for line in new.splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                evt = json.loads(line)
            except json.JSONDecodeError:
                print(f"[event/non-json] {line}")
                continue
            kind_e = evt.get("event")
            did = evt.get("demo_id")
            if kind_e == "render_done" and did:
                src = evt.get("src_path")
                if src:
                    src_path = Path(src)
                    ext = src_path.suffix.lower() or ".wav"
                    dest = output_dir / f"{did}{ext}"
                    try:
                        shutil.copyfile(src_path, dest)
                        size_kb = dest.stat().st_size // 1024
                        print(f"[event] render_done {did} → {dest.name} ({size_kb}KB)")
                    except Exception as e:
                        print(f"[event] render_done {did} but copy failed: {e}")
                        continue
                else:
                    print(f"[event] render_done {did} (no src_path)")
                pending.discard(did)
            elif kind_e == "render_start" and did:
                print(f"[event] render_start {did}")
            elif kind_e == "error":
                print(f"[event] error: {evt.get('message', '?')}")
            else:
                print(f"[event] {evt}")

        for did in list(pending):
            if find_rendered(did, output_dir):
                print(f"[poll] {did} appeared in output dir")
                pending.discard(did)

        now = time.time()
        if now - last_dump > 30:
            done = len(spec['demos']) - len(pending)
            sample = sorted(pending)[:5]
            tail = "…" if len(pending) > 5 else ""
            print(f"[status] {done}/{len(spec['demos'])} done; pending: {sample}{tail}")
            last_dump = now

    if interrupted["flag"]:
        print("\nInterrupted.")
        return 1
    print(f"\nAll {len(spec['demos'])} demos rendered.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--course-root", required=True)
    ap.add_argument("--episode", "--lesson", dest="episode", required=True)
    ap.add_argument("--device", required=True,
                    help="device class (e.g. Operator, Analog, Wavetable). "
                         "Lowercased to find param_maps/<class>.json.")
    ap.add_argument("--kind", choices=KIND_CHOICES, default="midi-instrument",
                    help="which M4L render device to target")
    ap.add_argument("--demos-key", default="operator_demos",
                    help="key in clip_manifest.yaml that holds the demo list "
                         "(default: operator_demos)")
    ap.add_argument("--demo", help="filter to a single demo id")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--clear", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    cfg = load_course(args.course_root)
    repo_root = cfg["_repo_root"]
    episode_dir = find_episode_dir(cfg, args.episode)
    if not episode_dir.exists():
        sys.stderr.write(f"episode dir not found: {episode_dir}\n")
        return 2

    manifest_path = episode_dir / "clip_manifest.yaml"
    if not manifest_path.exists():
        sys.stderr.write(f"clip_manifest.yaml not found at {manifest_path}\n")
        return 2

    manifest = yaml.safe_load(manifest_path.read_text()) or {}
    if args.demos_key not in manifest:
        sys.stderr.write(
            f"manifest has no '{args.demos_key}' key. Available top-level keys: "
            f"{sorted(manifest.keys())}\n"
        )
        return 2

    output_dir = build_audio(cfg) / "clips" / args.episode
    events_dir = cfg["_build_root"] / "tmp" / "device-render" / args.episode
    spec_path = events_dir / "spec.json"
    events_path = events_dir / "events.ndjson"

    spec = build_spec(
        manifest,
        episode_id=args.episode,
        device_class=args.device,
        kind=args.kind,
        demos_key=args.demos_key,
        output_dir=output_dir,
        events_path=events_path,
    )
    if args.demo:
        spec["demos"] = [d for d in spec["demos"] if d["id"] == args.demo]
        if not spec["demos"]:
            sys.stderr.write(f"demo id {args.demo!r} not found in {args.demos_key}\n")
            return 2

    if args.clear:
        n = 0
        for d in spec["demos"]:
            for ext in (".wav", ".aif", ".aiff"):
                p = output_dir / f"{d['id']}{ext}"
                if p.exists():
                    p.unlink()
                    n += 1
        print(f"Cleared {n} rendered file(s) under {output_dir}")
        return 0

    if args.list:
        print(f"Episode: {args.episode}  Device: {args.device}  Kind: {args.kind}")
        print(f"Output dir: {output_dir}")
        rendered, total = print_status(spec, output_dir)
        print(f"\n{rendered}/{total} demos rendered")
        return 0

    if args.dry_run:
        print(json.dumps(spec, indent=2))
        return 0

    output_dir.mkdir(parents=True, exist_ok=True)
    events_dir.mkdir(parents=True, exist_ok=True)
    spec_path.write_text(json.dumps(spec, indent=2))
    print(f"Spec → {_rel(spec_path, repo_root)}")
    print(f"Events → {_rel(events_path, repo_root)}")
    print(f"Output → {_rel(output_dir, repo_root)}")

    print("\nCurrent status:")
    rendered, total = print_status(spec, output_dir)
    print(f"\n{rendered}/{total} already rendered")

    return watch(spec, output_dir, events_path)


def _rel(p: Path, root: Path) -> str:
    try:
        return str(p.resolve().relative_to(root.resolve()))
    except ValueError:
        return str(p)


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""
operator_render.py — driver for the Operator-patch render pipeline.

Splits responsibility with the Max for Live device `OperatorRender.amxd`
(see m4l/README.md):

    Python (this file)            M4L device (operator_render.js)
    ────────────────────          ───────────────────────────────
    read clip_manifest.yaml   →   spec.json
    write spec.json           ↓
    [user clicks RENDER]      ←   read spec.json
    watch output dir + NDJSON ↔   apply LOM params, freeze track,
                                  copy frozen WAV to output_dir,
                                  emit NDJSON event per demo

The CLI does no IPC beyond flat files. This works because the user runs
this script in a terminal alongside Live; the M4L device produces files;
the script tails them. Exit cleanly on Ctrl-C.

Usage:
    # Default — write spec, watch for renders, exit when all demos done
    python courses/ableton-devices/tools/operator_render/operator_render.py \\
        --course-root courses/ableton-devices --episode e01-operator

    # Filter to a single demo
    --demo op-ratio-1to1

    # Just list demos + their render status, then exit
    --list

    # Wipe rendered WAVs to force re-render (does NOT touch song_clips/)
    --clear

    # Dry-run: print spec, don't write
    --dry-run

Output paths:
    spec:       <build_root>/tmp/operator-render/<episode>/spec.json
    events:     <build_root>/tmp/operator-render/<episode>/events.ndjson
    rendered:   <build_root>/audio/clips/<episode>/<demo_id>.wav
                (same dir as extract_clips.py output — build_episode reads either)
"""
from __future__ import annotations

import argparse
import json
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


SPEC_VERSION = 1


def find_episode_dir(cfg: dict, episode_id: str) -> Path:
    content_kind = cfg.get("content_kind", "lesson")
    base = episodes_dir(cfg) if content_kind == "episode" else lessons_dir(cfg)
    return base / episode_id


def build_spec(manifest: dict, episode_id: str, output_dir: Path, events_path: Path) -> dict:
    demos = manifest.get("operator_demos") or []
    return {
        "spec_version": SPEC_VERSION,
        "episode_id": episode_id,
        "output_dir": str(output_dir),
        "events_path": str(events_path),
        "demos": [
            {
                "id": d["id"],
                "description": d.get("description", ""),
                "duration_s": d.get("duration_s"),
                "midi": d.get("midi"),
                "automation": d.get("automation"),
                "params": d.get("params"),  # may be None — JS treats as "needs manual setup"
                "notes": d.get("notes"),
            }
            for d in demos
        ],
    }


def status_for_demo(demo_id: str, output_dir: Path) -> str:
    return "rendered" if (output_dir / f"{demo_id}.wav").exists() else "pending"


def print_status(spec: dict, output_dir: Path) -> tuple[int, int]:
    rendered = 0
    for d in spec["demos"]:
        s = status_for_demo(d["id"], output_dir)
        marker = "✓" if s == "rendered" else " "
        size = ""
        if s == "rendered":
            wav = output_dir / f"{d['id']}.wav"
            size = f" ({wav.stat().st_size // 1024}KB)"
            rendered += 1
        print(f"  [{marker}] {d['id']}{size}")
    return rendered, len(spec["demos"])


def watch(spec: dict, output_dir: Path, events_path: Path) -> int:
    """Block until all demos rendered, or Ctrl-C. Returns 0 if all done, 1 if interrupted."""
    interrupted = {"flag": False}

    def on_sigint(_sig, _frame):
        interrupted["flag"] = True

    signal.signal(signal.SIGINT, on_sigint)

    pending = {d["id"] for d in spec["demos"]}
    pending -= {d["id"] for d in spec["demos"] if status_for_demo(d["id"], output_dir) == "rendered"}

    if not pending:
        print("\nAll demos already rendered.")
        return 0

    print(f"\nWaiting on {len(pending)} demo(s). Click RENDER in OperatorRender.amxd. Ctrl-C to exit.")
    events_path.parent.mkdir(parents=True, exist_ok=True)
    if not events_path.exists():
        events_path.touch()

    last_offset = events_path.stat().st_size
    last_dump = time.time()

    while pending and not interrupted["flag"]:
        time.sleep(0.5)

        # Tail events.ndjson for structured progress
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
            kind = evt.get("event")
            did = evt.get("demo_id")
            if kind == "render_done" and did:
                print(f"[event] render_done {did}")
                pending.discard(did)
            elif kind == "render_start" and did:
                print(f"[event] render_start {did}")
            elif kind == "error":
                print(f"[event] error: {evt.get('message', '?')}")
            else:
                print(f"[event] {evt}")

        # Polling fallback — if event file missing or M4L can't write events,
        # still detect new WAVs. Once a demo's WAV exists, it's done.
        for did in list(pending):
            if (output_dir / f"{did}.wav").exists():
                print(f"[poll] {did} appeared in output dir")
                pending.discard(did)

        # Periodic status dump every 30s
        now = time.time()
        if now - last_dump > 30:
            print(f"[status] {len(spec['demos']) - len(pending)}/{len(spec['demos'])} done; pending: {sorted(pending)[:5]}{'…' if len(pending) > 5 else ''}")
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
    ap.add_argument("--demo", help="filter to a single demo id")
    ap.add_argument("--list", action="store_true", help="list demos + status, then exit")
    ap.add_argument("--clear", action="store_true", help="delete rendered WAVs to force re-render")
    ap.add_argument("--dry-run", action="store_true", help="print spec, don't write")
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
    output_dir = build_audio(cfg) / "clips" / args.episode
    events_dir = cfg["_build_root"] / "tmp" / "operator-render" / args.episode
    spec_path = events_dir / "spec.json"
    events_path = events_dir / "events.ndjson"

    spec = build_spec(manifest, args.episode, output_dir, events_path)
    if args.demo:
        spec["demos"] = [d for d in spec["demos"] if d["id"] == args.demo]
        if not spec["demos"]:
            sys.stderr.write(f"demo id {args.demo!r} not found in operator_demos\n")
            return 2

    if args.clear:
        n = 0
        for d in spec["demos"]:
            p = output_dir / f"{d['id']}.wav"
            if p.exists():
                p.unlink()
                n += 1
        print(f"Cleared {n} rendered WAV(s) under {output_dir}")
        return 0

    if args.list:
        print(f"Episode: {args.episode}")
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

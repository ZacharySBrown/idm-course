#!/usr/bin/env python3
"""
extract_clips.py — cut song-clip WAVs declared in an episode's clip_manifest.

Reads:
    <course_root>/<episode_dir>/<episode>/clip_manifest.yaml
        song_source_dir: songs/ableton-ep01      # repo-relative; per-clip override allowed
        song_clips:
          - id: polynomial-c-cold-open
            source: "01_polynomial-c.wav"
            start: "0:00"
            end:   "0:08"
            fade_in_ms: 0
            fade_out_ms: 800
            normalize_lufs: -16

Writes:
    <build_root>/audio/clips/<episode>/<id>.wav    (PCM 16-bit stereo, 44.1kHz)

Usage:
    python shared/tools/extract_clips.py --course-root courses/ableton-devices --lesson e01-operator
    python shared/tools/extract_clips.py --course-root courses/ableton-devices --lesson e01-operator --clip stria-excerpt-1
    python shared/tools/extract_clips.py --course-root courses/ableton-devices --lesson e01-operator --dry-run

Requires:
    ffmpeg on PATH (uses native afade + loudnorm filters; no pyloudnorm dep).
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.stderr.write("pyyaml missing. uv pip install pyyaml\n")
    sys.exit(2)

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _course_lib import load_course, episodes_dir, lessons_dir, build_audio  # noqa: E402


TIME_RE = re.compile(r"^\s*(?:(\d+):)?(\d+):(\d{1,2}(?:\.\d+)?)\s*$")


def parse_time(s: str | int | float) -> float:
    """Accept '12.5', '0:08', '1:30', '1:23:45.5', or numeric seconds → seconds."""
    if isinstance(s, (int, float)):
        return float(s)
    if not isinstance(s, str):
        raise ValueError(f"unparseable time value: {s!r}")
    txt = s.strip()
    if ":" not in txt:
        return float(txt)
    m = TIME_RE.match(txt)
    if not m:
        raise ValueError(f"bad time format {s!r} — want HH:MM:SS or MM:SS")
    hours = int(m.group(1)) if m.group(1) else 0
    minutes = int(m.group(2))
    seconds = float(m.group(3))
    return hours * 3600 + minutes * 60 + seconds


def build_filter_chain(duration_s: float, entry: dict) -> str | None:
    parts: list[str] = []
    fade_in_ms = int(entry.get("fade_in_ms") or 0)
    fade_out_ms = int(entry.get("fade_out_ms") or 0)
    lufs = entry.get("normalize_lufs")

    if fade_in_ms > 0:
        parts.append(f"afade=t=in:st=0:d={fade_in_ms / 1000:.3f}")
    if fade_out_ms > 0:
        fade_out_s = fade_out_ms / 1000
        start = max(0.0, duration_s - fade_out_s)
        parts.append(f"afade=t=out:st={start:.3f}:d={fade_out_s:.3f}")
    if lufs is not None:
        parts.append(f"loudnorm=I={lufs}:TP=-1.5:LRA=11")

    return ",".join(parts) if parts else None


def cut_one(entry: dict, source_root: Path, out_dir: Path, dry_run: bool, repo_root: Path) -> dict:
    cid = entry["id"]
    src_rel = entry.get("source")
    if not src_rel:
        return {"id": cid, "status": "missing-source-field"}

    # Per-entry override of song_source_dir possible via absolute path or with leading directory.
    src = Path(src_rel)
    if not src.is_absolute():
        src = source_root / src
    if not src.exists():
        return {"id": cid, "status": "source-not-found", "source": str(src)}

    try:
        start_s = parse_time(entry["start"])
        end_s = parse_time(entry["end"])
    except (KeyError, ValueError) as e:
        return {"id": cid, "status": "bad-time", "error": str(e)}

    duration_s = end_s - start_s
    if duration_s <= 0:
        return {"id": cid, "status": "non-positive-duration", "duration_s": duration_s}

    out_path = out_dir / f"{cid}.wav"
    filter_chain = build_filter_chain(duration_s, entry)

    cmd = [
        "ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
        "-ss", f"{start_s:.3f}", "-to", f"{end_s:.3f}",
        "-i", str(src),
    ]
    if filter_chain:
        cmd += ["-af", filter_chain]
    cmd += [
        "-ac", "2", "-ar", "44100", "-c:a", "pcm_s16le",
        str(out_path),
    ]

    if dry_run:
        return {
            "id": cid,
            "status": "dry-run",
            "source": _rel(src, repo_root),
            "out": _rel(out_path, repo_root),
            "duration_s": round(duration_s, 3),
            "filters": filter_chain or "",
        }

    out_path.parent.mkdir(parents=True, exist_ok=True)
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        return {
            "id": cid,
            "status": "ffmpeg-failed",
            "error": proc.stderr.strip()[:1000],
            "cmd": " ".join(cmd),
        }

    return {
        "id": cid,
        "status": "ok",
        "out": _rel(out_path, repo_root),
        "duration_s": round(duration_s, 3),
        "filters": filter_chain or "",
    }


def _rel(p: Path, root: Path) -> str:
    try:
        return str(p.resolve().relative_to(root.resolve()))
    except ValueError:
        return str(p)


def find_episode_dir(cfg: dict, episode_id: str) -> Path:
    content_kind = cfg.get("content_kind", "lesson")
    base = episodes_dir(cfg) if content_kind == "episode" else lessons_dir(cfg)
    return base / episode_id


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--course-root", required=True)
    ap.add_argument("--lesson", "--episode", dest="lesson", required=True,
                    help="lesson|episode id, e.g. e01-operator")
    ap.add_argument("--clip", help="filter to a single clip id")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--manifest", help="override manifest path (default: <episode>/clip_manifest.yaml)")
    args = ap.parse_args()

    cfg = load_course(args.course_root)
    repo_root = cfg["_repo_root"]

    episode_dir = find_episode_dir(cfg, args.lesson)
    if not episode_dir.exists():
        sys.stderr.write(f"episode dir not found: {episode_dir}\n")
        return 2

    manifest_path = Path(args.manifest) if args.manifest else episode_dir / "clip_manifest.yaml"
    if not manifest_path.exists():
        sys.stderr.write(f"clip_manifest.yaml not found at {manifest_path}\n")
        return 2

    manifest = yaml.safe_load(manifest_path.read_text()) or {}
    song_clips = manifest.get("song_clips") or []
    if args.clip:
        song_clips = [c for c in song_clips if c.get("id") == args.clip]
        if not song_clips:
            sys.stderr.write(f"clip id {args.clip!r} not found in manifest\n")
            return 2

    source_root_rel = manifest.get("song_source_dir", "")
    source_root = (
        Path(source_root_rel)
        if Path(source_root_rel).is_absolute()
        else repo_root / source_root_rel
    )
    out_dir = build_audio(cfg) / "clips" / args.lesson

    results = [cut_one(c, source_root, out_dir, args.dry_run, repo_root) for c in song_clips]
    for r in results:
        line = f"[clip] {r['id']}: {r['status']}"
        if r["status"] in ("ok", "dry-run"):
            line += f" — {r['out']} ({r['duration_s']}s)"
            if r.get("filters"):
                line += f" [{r['filters']}]"
        elif r["status"] == "source-not-found":
            line += f" — {r.get('source')}"
        elif "error" in r:
            line += f" — {r['error'][:200]}"
        print(line)

    status_path = out_dir / "_extract_status.json"
    if not args.dry_run:
        out_dir.mkdir(parents=True, exist_ok=True)
        status_path.write_text(json.dumps(results, indent=2))

    ok = sum(1 for r in results if r["status"] in ("ok", "dry-run"))
    print(f"\nextract_clips: {ok}/{len(results)} ok")
    return 0 if ok == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())

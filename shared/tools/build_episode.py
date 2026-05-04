#!/usr/bin/env python3
"""
build_episode.py — assemble a walking-podcast MP3 per lesson.

Reads:
    lessons/<lesson>/lesson.yaml
    build/audio/narration/<lesson>/*.wav          (from render_voiceover.py)
    build/audio/stemforge-renders/<week>/*.wav    (inlined as musical interludes)

Writes:
    build/audio/episodes/<lesson>.mp3
    build/audio/episodes/<lesson>.chapters.json   (sidecar)

Chapter markers: embeds ID3 CTOC/CHAP frames via mutagen so podcast players
jump between slides.

Usage:
    python tools/build_episode.py                        # all lessons
    python tools/build_episode.py --lesson w05-aphex-tuning
    python tools/build_episode.py --include-stemforge    # inline per-slide AB renders as interludes

Requires:
    ffmpeg on PATH
    uv pip install mutagen pyyaml
"""
from __future__ import annotations

import argparse
import json
import shlex
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.stderr.write("pyyaml missing. uv pip install pyyaml\n")
    sys.exit(2)

try:
    from mutagen.id3 import ID3, CHAP, CTOC, CTOCFlags, TIT2, TALB, TPE1, TRCK
    from mutagen.mp3 import MP3
except ImportError:
    sys.stderr.write("mutagen missing. uv pip install mutagen\n")
    sys.exit(2)

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _course_lib import (  # noqa: E402
    load_course,
    lessons_dir,
    episodes_dir,
    narration_out,
    stemforge_out,
    episodes_out,
    build_audio,
)


def ffprobe_duration_ms(path: Path) -> int:
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "a:0",
         "-show_entries", "stream=duration", "-of", "csv=p=0", str(path)],
        capture_output=True, text=True, check=True,
    )
    return int(float(r.stdout.strip()) * 1000)


def concat_wavs(pieces: list[Path], out_mp3: Path, title: str, artist: str, album: str) -> None:
    """Concatenate WAVs, inserting 400ms silences between pieces, transcode to MP3 @192k."""
    with tempfile.TemporaryDirectory() as td:
        concat_list = Path(td) / "concat.txt"
        silence = Path(td) / "silence_400ms.wav"
        subprocess.run(
            ["ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo",
             "-t", "0.4", "-c:a", "pcm_s16le", str(silence)],
            check=True, capture_output=True,
        )
        lines: list[str] = []
        for i, p in enumerate(pieces):
            if i > 0:
                lines.append(f"file {shlex.quote(str(silence))}")
            lines.append(f"file {shlex.quote(str(p.resolve()))}")
        concat_list.write_text("\n".join(lines))

        out_mp3.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_list),
             "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
             "-c:a", "libmp3lame", "-b:a", "192k",
             "-metadata", f"title={title}",
             "-metadata", f"artist={artist}",
             "-metadata", f"album={album}",
             str(out_mp3)],
            check=True, capture_output=True,
        )


def write_chapters(mp3_path: Path, chapters: list[dict], sidecar: Path) -> None:
    sidecar.write_text(json.dumps(chapters, indent=2))

    audio = MP3(str(mp3_path), ID3=ID3)
    if audio.tags is None:
        audio.add_tags()
    tags = audio.tags
    for ch in chapters:
        tags.add(CHAP(
            element_id=ch["id"],
            start_time=ch["start_ms"],
            end_time=ch["end_ms"],
            start_offset=0, end_offset=0,
            sub_frames=[TIT2(encoding=3, text=ch["title"])],
        ))
    tags.add(CTOC(
        element_id="toc",
        flags=CTOCFlags.TOP_LEVEL | CTOCFlags.ORDERED,
        child_element_ids=[c["id"] for c in chapters],
        sub_frames=[TIT2(encoding=3, text="Chapters")],
    ))
    audio.save()


def build_one(
    lesson_dir: Path,
    include_stemforge: bool,
    narr_root: Path,
    out_dir: Path,
    repo_root: Path,
    show_artist: str,
    show_album: str,
    clips_root: Path | None = None,
) -> dict:
    # Support both content_kind=lesson (lesson.yaml) and content_kind=episode (episode.yaml).
    if (lesson_dir / "lesson.yaml").exists():
        item_yaml = lesson_dir / "lesson.yaml"
    elif (lesson_dir / "episode.yaml").exists():
        item_yaml = lesson_dir / "episode.yaml"
    else:
        return {"lesson": lesson_dir.name, "status": "missing-lesson-or-episode-yaml"}

    lesson = yaml.safe_load(item_yaml.read_text())
    lesson_id = lesson["id"]
    episode_cfg = lesson.get("episode", {})

    narr_dir = narr_root / lesson_id
    if not narr_dir.exists():
        return {"lesson": lesson_id, "status": "no-narration — run render_voiceover.py first"}

    clips_dir = clips_root / lesson_id if clips_root else None

    # Assemble pieces in slide order, grouping each slide+its demos into one chapter block.
    intro = narr_dir / "intro.wav"
    outro = narr_dir / "outro.wav"
    blocks: list[tuple[str, list[Path]]] = []  # (chapter title, pieces in chapter)
    missing_demos: list[str] = []

    if intro.exists():
        blocks.append(("Intro", [intro]))

    for slide in lesson.get("slides", []):
        script_rel = slide.get("script_md")
        if not script_rel:
            continue
        wav_name = Path(script_rel).stem + ".wav"
        wav_path = narr_dir / wav_name
        if not wav_path.exists():
            continue
        block_pieces: list[Path] = [wav_path]
        for demo_id in slide.get("demos", []) or []:
            if clips_dir is None:
                missing_demos.append(f"{slide['id']}:{demo_id} (no clips_root)")
                continue
            demo_path = None
            for ext in (".wav", ".aif", ".aiff"):
                cand = clips_dir / f"{demo_id}{ext}"
                if cand.exists():
                    demo_path = cand
                    break
            if demo_path:
                block_pieces.append(demo_path)
            else:
                missing_demos.append(f"{slide['id']}:{demo_id}")
        blocks.append((slide.get("heading", slide["id"]), block_pieces))

    if outro.exists():
        blocks.append(("Outro", [outro]))

    pieces: list[Path] = [p for _, parts in blocks for p in parts]
    if not pieces:
        return {"lesson": lesson_id, "status": "no-narration-wavs"}

    # Per-piece durations + start cursors, accounting for 400ms inter-piece silence.
    durations = [ffprobe_duration_ms(p) for p in pieces]
    piece_starts: list[int] = []
    cursor = 0
    for i, dur in enumerate(durations):
        piece_starts.append(cursor)
        cursor += dur
        if i < len(durations) - 1:
            cursor += 400
    total_ms = cursor

    # Chapter spans first piece's start → last piece's end within each block.
    chapters = []
    piece_idx = 0
    for bidx, (title, parts) in enumerate(blocks):
        n = len(parts)
        start_ms = piece_starts[piece_idx]
        last_idx = piece_idx + n - 1
        end_ms = piece_starts[last_idx] + durations[last_idx]
        chapters.append({
            "id": f"ch{bidx:03d}",
            "title": title,
            "start_ms": start_ms,
            "end_ms": end_ms,
        })
        piece_idx += n

    out_mp3 = out_dir / f"{lesson_id}.mp3"
    sidecar = out_dir / f"{lesson_id}.chapters.json"

    concat_wavs(
        pieces, out_mp3,
        title=episode_cfg.get("title", lesson.get("title", lesson_id)),
        artist=show_artist,
        album=show_album,
    )
    write_chapters(out_mp3, chapters, sidecar)

    try:
        rel = str(out_mp3.relative_to(repo_root))
    except ValueError:
        rel = str(out_mp3)
    result = {
        "lesson": lesson_id,
        "status": "ok",
        "mp3": rel,
        "chapters": len(chapters),
        "pieces": len(pieces),
        "duration_ms": total_ms,
    }
    if missing_demos:
        result["missing_demos"] = missing_demos
    return result


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--course-root", required=True)
    ap.add_argument("--lesson", "--episode", dest="lesson",
                    help="lesson|episode id, e.g. e01-operator")
    ap.add_argument("--include-stemforge", action="store_true",
                    help="(reserved) inline AB renders as musical interludes")
    args = ap.parse_args()

    cfg = load_course(args.course_root)
    content_kind = cfg.get("content_kind", "lesson")
    items_root = episodes_dir(cfg) if content_kind == "episode" else lessons_dir(cfg)
    narr_root = narration_out(cfg)
    out_dir = episodes_out(cfg)
    clips_root = build_audio(cfg) / "clips"
    show_artist = cfg.get("episode_artist", f"{cfg.get('title', 'Course')} (narrator)")
    show_album = cfg.get("title", "Course")

    targets = (
        [items_root / args.lesson]
        if args.lesson
        else sorted(items_root.iterdir())
    )
    targets = [t for t in targets if t.is_dir()]

    results = [
        build_one(
            t,
            args.include_stemforge,
            narr_root=narr_root,
            out_dir=out_dir,
            repo_root=cfg["_repo_root"],
            show_artist=show_artist,
            show_album=show_album,
            clips_root=clips_root,
        )
        for t in targets
    ]
    for r in results:
        line = f"[episode] {r['lesson']}: {r['status']}"
        if r["status"] == "ok":
            line += f" — {r['mp3']} ({r['chapters']} chapters, {r.get('pieces', '?')} pieces)"
            if r.get("missing_demos"):
                line += f" [missing demos: {len(r['missing_demos'])}]"
        print(line)

    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "_build_status.json").write_text(json.dumps(results, indent=2))

    ok = sum(1 for r in results if r["status"] == "ok")
    print(f"\nbuild_episode: {ok}/{len(results)} ok")
    return 0 if ok == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())

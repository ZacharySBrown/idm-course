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

ROOT = Path(__file__).resolve().parent.parent
LESSONS = ROOT / "lessons"
NARR = ROOT / "build" / "audio" / "narration"
SF_RENDERS = ROOT / "build" / "audio" / "stemforge-renders"
OUT = ROOT / "build" / "audio" / "episodes"


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


def build_one(lesson_dir: Path, include_stemforge: bool) -> dict:
    lesson_yaml = lesson_dir / "lesson.yaml"
    if not lesson_yaml.exists():
        return {"lesson": lesson_dir.name, "status": "missing-lesson-yaml"}

    lesson = yaml.safe_load(lesson_yaml.read_text())
    lesson_id = lesson["id"]
    episode_cfg = lesson.get("episode", {})

    narr_dir = NARR / lesson_id
    if not narr_dir.exists():
        return {"lesson": lesson_id, "status": "no-narration — run render_voiceover.py first"}

    # Assemble pieces in slide order
    intro = narr_dir / "intro.wav"
    outro = narr_dir / "outro.wav"
    pieces: list[Path] = []
    chapter_plan: list[tuple[str, str]] = []  # (title, wav_path_absolute_str)

    if intro.exists():
        pieces.append(intro)
        chapter_plan.append(("Intro", str(intro)))

    for slide in lesson.get("slides", []):
        script_rel = slide.get("script_md")
        if not script_rel:
            continue
        wav_name = Path(script_rel).stem + ".wav"
        wav_path = narr_dir / wav_name
        if wav_path.exists():
            pieces.append(wav_path)
            chapter_plan.append((slide.get("heading", slide["id"]), str(wav_path)))

    if outro.exists():
        pieces.append(outro)
        chapter_plan.append(("Outro", str(outro)))

    if not pieces:
        return {"lesson": lesson_id, "status": "no-narration-wavs"}

    # Compute chapter start/end
    durations = [ffprobe_duration_ms(p) for p in pieces]
    chapters = []
    cursor = 0
    for (title, _), dur in zip(chapter_plan, durations):
        chapters.append({
            "id": f"ch{len(chapters):03d}",
            "title": title,
            "start_ms": cursor,
            "end_ms": cursor + dur,
        })
        cursor += dur + 400  # matches 400ms inter-piece silence

    out_mp3 = OUT / f"{lesson_id}.mp3"
    sidecar = OUT / f"{lesson_id}.chapters.json"

    concat_wavs(
        pieces, out_mp3,
        title=episode_cfg.get("title", lesson.get("title", lesson_id)),
        artist="IDM Course (Bernd)",
        album="IDM Production — 12 Weeks, 12 Tracks",
    )
    write_chapters(out_mp3, chapters, sidecar)

    return {
        "lesson": lesson_id,
        "status": "ok",
        "mp3": str(out_mp3.relative_to(ROOT)),
        "chapters": len(chapters),
        "duration_ms": cursor,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lesson")
    ap.add_argument("--include-stemforge", action="store_true",
                    help="(reserved) inline AB renders as musical interludes")
    args = ap.parse_args()

    targets = [LESSONS / args.lesson] if args.lesson else sorted(LESSONS.iterdir())
    targets = [t for t in targets if t.is_dir()]

    results = [build_one(t, args.include_stemforge) for t in targets]
    for r in results:
        print(f"[episode] {r['lesson']}: {r['status']}"
              + (f" — {r['mp3']} ({r['chapters']} chapters)" if r['status'] == 'ok' else ''))

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "_build_status.json").write_text(json.dumps(results, indent=2))

    ok = sum(1 for r in results if r["status"] == "ok")
    print(f"\nbuild_episode: {ok}/{len(results)} ok")
    return 0 if ok == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())

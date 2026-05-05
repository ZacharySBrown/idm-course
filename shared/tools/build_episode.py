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


# ── Default mastering config ─────────────────────────────────────────────────
# Per-piece loudness normalization targets (LUFS). Narration sits a few dB
# above music so voice always cuts through.
DEFAULT_MASTERING = {
    "enabled": True,
    "per_piece_normalize": {
        "enabled": True,
        "targets": {
            "narration":  -18,
            "music":      -22,   # operator demos + song clips
            "transition": -26,   # background-music transitions, ducked under
        },
        "true_peak_db": -1.5,
        "lra": 11,
    },
    "master_chain": {
        "target_lufs": -16,
        "true_peak_db": -1.5,
        "lra": 11,
        "compressor": {
            "enabled": True,
            "threshold_db": -20,
            "ratio": 2.0,
            "attack_ms": 20,
            "release_ms": 250,
            "knee_db": 4,
        },
        "limiter": {
            "enabled": True,
            "limit": 0.97,        # peak ceiling, linear (≈ -0.26 dBFS)
            "attack": 7,
            "release": 100,
        },
    },
}


def merge_mastering(user_cfg: dict | None) -> dict:
    """Shallow-deep merge of user mastering config over defaults."""
    cfg = json.loads(json.dumps(DEFAULT_MASTERING))  # deep copy
    if not user_cfg:
        return cfg
    for k, v in user_cfg.items():
        if isinstance(v, dict) and isinstance(cfg.get(k), dict):
            for kk, vv in v.items():
                if isinstance(vv, dict) and isinstance(cfg[k].get(kk), dict):
                    cfg[k][kk].update(vv)
                else:
                    cfg[k][kk] = vv
        else:
            cfg[k] = v
    return cfg


def normalize_piece(src: Path, dst: Path, target_lufs: float, tp_db: float, lra: int) -> None:
    """Single-pass loudnorm. Output stays as 44.1kHz/16-bit stereo WAV."""
    subprocess.run(
        ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
         "-i", str(src),
         "-af", f"loudnorm=I={target_lufs}:TP={tp_db}:LRA={lra}",
         "-ar", "44100", "-ac", "2", "-c:a", "pcm_s16le",
         str(dst)],
        check=True,
    )


def build_master_filter(mastering: dict) -> str:
    """Build the post-concat ffmpeg filter chain: compressor → loudnorm → limiter."""
    parts: list[str] = []
    mc = mastering["master_chain"]
    comp = mc.get("compressor", {})
    if comp.get("enabled"):
        parts.append(
            f"acompressor=threshold={comp['threshold_db']}dB"
            f":ratio={comp['ratio']}"
            f":attack={comp['attack_ms']}"
            f":release={comp['release_ms']}"
            f":knee={comp['knee_db']}"
        )
    parts.append(f"loudnorm=I={mc['target_lufs']}:TP={mc['true_peak_db']}:LRA={mc['lra']}")
    lim = mc.get("limiter", {})
    if lim.get("enabled"):
        parts.append(
            f"alimiter=limit={lim['limit']}"
            f":attack={lim['attack']}"
            f":release={lim['release']}"
        )
    return ",".join(parts)


def concat_wavs(
    pieces: list[tuple[Path, str]],   # (path, role) tuples
    out_mp3: Path,
    title: str,
    artist: str,
    album: str,
    mastering: dict,
) -> None:
    """Concat pieces with 400ms silences, applying optional per-piece normalization
    and a final mastering chain. `pieces` is a list of (path, role) where role
    keys into mastering.per_piece_normalize.targets."""
    with tempfile.TemporaryDirectory() as td:
        td_p = Path(td)
        silence = td_p / "silence_400ms.wav"
        subprocess.run(
            ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
             "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo",
             "-t", "0.4", "-c:a", "pcm_s16le", str(silence)],
            check=True,
        )

        ppn = mastering["per_piece_normalize"]
        targets = ppn["targets"]

        # Either copy pieces as-is or normalize them into the temp dir.
        normalized: list[Path] = []
        for i, (p, role) in enumerate(pieces):
            if ppn.get("enabled"):
                target = targets.get(role, targets.get("music", -22))
                norm_p = td_p / f"{i:03d}_{role}_{p.stem}.wav"
                normalize_piece(p, norm_p, target, ppn["true_peak_db"], ppn["lra"])
                normalized.append(norm_p)
            else:
                normalized.append(p)

        concat_list = td_p / "concat.txt"
        lines: list[str] = []
        for i, p in enumerate(normalized):
            if i > 0:
                lines.append(f"file {shlex.quote(str(silence))}")
            lines.append(f"file {shlex.quote(str(p.resolve()))}")
        concat_list.write_text("\n".join(lines))

        out_mp3.parent.mkdir(parents=True, exist_ok=True)
        master_filter = build_master_filter(mastering)
        subprocess.run(
            ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
             "-f", "concat", "-safe", "0", "-i", str(concat_list),
             "-af", master_filter,
             "-c:a", "libmp3lame", "-b:a", "192k",
             "-metadata", f"title={title}",
             "-metadata", f"artist={artist}",
             "-metadata", f"album={album}",
             str(out_mp3)],
            check=True,
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
    mastering: dict | None = None,
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

    # Per-episode mastering override merged over course-level config.
    mastering = merge_mastering({**(mastering or {}), **(lesson.get("mastering") or {})})

    # Build a slide-id → transition-clip-id map from episode.yaml's transitions block.
    # Schema (episode.yaml):
    #   transitions:
    #     enabled: true
    #     insertions:
    #       - after_slide: 02g-tx81z-underground
    #         clip_id: trans-stria-mid
    transitions_cfg = lesson.get("transitions") or {}
    transitions_after: dict[str, str] = {}
    if transitions_cfg.get("enabled"):
        for ins in transitions_cfg.get("insertions") or []:
            sid = ins.get("after_slide")
            cid = ins.get("clip_id")
            if sid and cid:
                transitions_after[sid] = cid

    narr_dir = narr_root / lesson_id
    if not narr_dir.exists():
        return {"lesson": lesson_id, "status": "no-narration — run render_voiceover.py first"}

    clips_dir = clips_root / lesson_id if clips_root else None

    # Assemble pieces in slide order, grouping each slide+its demos into one chapter block.
    # Each piece is (path, role) where role is "narration" or "music" so the
    # mastering pipeline can apply the right per-piece loudness target.
    intro = narr_dir / "intro.wav"
    outro = narr_dir / "outro.wav"
    blocks: list[tuple[str, list[tuple[Path, str]]]] = []
    missing_demos: list[str] = []

    if intro.exists():
        blocks.append(("Intro", [(intro, "narration")]))

    for slide in lesson.get("slides", []):
        script_rel = slide.get("script_md")
        if not script_rel:
            continue
        wav_name = Path(script_rel).stem + ".wav"
        wav_path = narr_dir / wav_name
        if not wav_path.exists():
            continue
        block_pieces: list[tuple[Path, str]] = [(wav_path, "narration")]
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
                block_pieces.append((demo_path, "music"))
            else:
                missing_demos.append(f"{slide['id']}:{demo_id}")
        # Transition clip after this slide (in the same chapter, so listeners
        # don't get a chapter marker for the transition).
        trans_cid = transitions_after.get(slide["id"])
        if trans_cid and clips_dir is not None:
            trans_path = None
            for ext in (".wav", ".aif", ".aiff"):
                cand = clips_dir / f"{trans_cid}{ext}"
                if cand.exists():
                    trans_path = cand
                    break
            if trans_path:
                block_pieces.append((trans_path, "transition"))
            else:
                missing_demos.append(f"{slide['id']}:transition:{trans_cid}")
        blocks.append((slide.get("heading", slide["id"]), block_pieces))

    if outro.exists():
        blocks.append(("Outro", [(outro, "narration")]))

    pieces: list[tuple[Path, str]] = [p for _, parts in blocks for p in parts]
    if not pieces:
        return {"lesson": lesson_id, "status": "no-narration-wavs"}

    # Per-piece durations + start cursors, accounting for 400ms inter-piece silence.
    durations = [ffprobe_duration_ms(p) for p, _ in pieces]
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
        mastering=mastering,
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
    course_mastering = cfg.get("mastering")

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
            mastering=course_mastering,
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

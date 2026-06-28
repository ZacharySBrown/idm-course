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
            "demo":       -22,   # rendered operator demos (controlled tones)
            "song":       -16,   # extracted song clips — keep their natural punch
            "music":      -22,   # legacy/fallback
            "transition": -26,   # background-music transitions, ducked under
            "bed":        -28,   # ambient bed under narration (sidechain-ducked)
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


def build_bed_track(
    bed_insertions: list[dict],
    block_starts: list[int],
    block_ends: list[int],
    block_slides: list[str],
    total_ms: int,
    clips_dir: Path | None,
    out_path: Path,
    mute_spans: list[tuple[int, int]] | None = None,
) -> None:
    """Generate a single 44.1kHz/16-bit stereo WAV of length total_ms with each
    bed clip placed at the right time offset and faded in/out. Returns nothing
    on disk if no insertions resolve."""
    if not bed_insertions or clips_dir is None:
        return

    slide_to_block = {sid: i for i, sid in enumerate(block_slides)}

    inputs: list[Path] = []
    delays: list[int] = []   # ms offset into the final track
    fade_ins: list[float] = []
    fade_outs: list[float] = []
    durations_s: list[float] = []
    gains_db: list[float] = []

    for ins in bed_insertions:
        cid = ins.get("clip_id")
        if not cid:
            continue
        # Resolve clip
        src = None
        for ext in (".wav", ".aif", ".aiff"):
            cand = clips_dir / f"{cid}{ext}"
            if cand.exists():
                src = cand
                break
        if not src:
            continue
        sb = slide_to_block.get(ins.get("start_at_slide"))
        eb = slide_to_block.get(ins.get("end_at_slide", ins.get("start_at_slide")))
        if sb is None or eb is None:
            continue
        delay_ms = block_starts[sb]
        end_ms = block_ends[eb]
        dur_ms = max(0, end_ms - delay_ms)
        if dur_ms < 500:
            continue
        inputs.append(src)
        delays.append(delay_ms)
        fade_ins.append(ins.get("fade_in_ms", 2500) / 1000)
        fade_outs.append(ins.get("fade_out_ms", 2500) / 1000)
        durations_s.append(dur_ms / 1000)
        gains_db.append(ins.get("gain_db", 0))

    if not inputs:
        return

    # ffmpeg filter graph: each input gets adelay + afade(in/out) + atrim, then amix.
    args = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error"]
    for src in inputs:
        args += ["-stream_loop", "-1", "-i", str(src)]
    parts = []
    for i in range(len(inputs)):
        d = delays[i]
        dur = durations_s[i]
        fin = fade_ins[i]
        fout = fade_outs[i]
        gdb = gains_db[i]
        # Loop the bed via -stream_loop, then trim to dur, then fade in/out, then delay, then volume.
        parts.append(
            f"[{i}:a]atrim=duration={dur},asetpts=PTS-STARTPTS,"
            f"afade=t=in:st=0:d={fin},"
            f"afade=t=out:st={max(0, dur - fout)}:d={fout},"
            f"adelay={d}|{d},volume={gdb}dB[b{i}]"
        )
    if len(inputs) == 1:
        parts.append(f"[b0]apad=whole_dur={total_ms / 1000}[bedout]")
    else:
        labels = "".join(f"[b{i}]" for i in range(len(inputs)))
        parts.append(f"{labels}amix=inputs={len(inputs)}:normalize=0:dropout_transition=2,apad=whole_dur={total_ms / 1000}[bedout]")
    # Hard-MUTE the bed under every foreground demo/song cue (not just duck):
    # a demo is itself music, so the bed must vanish so the example stands alone.
    # Pad each span by 200ms so the bed is already silent as the demo begins.
    out_label = "bedout"
    if mute_spans:
        conds = "+".join(
            f"between(t,{max(0, s - 200) / 1000:.3f},{(e + 200) / 1000:.3f})"
            for s, e in mute_spans
        )
        parts.append(f"[bedout]volume=0:enable='{conds}'[bedmuted]")
        out_label = "bedmuted"
    filter_complex = ";".join(parts)
    args += [
        "-filter_complex", filter_complex,
        "-map", f"[{out_label}]",
        "-ar", "44100", "-ac", "2", "-c:a", "pcm_s16le",
        "-t", f"{total_ms / 1000}",
        str(out_path),
    ]
    subprocess.run(args, check=True)


def concat_wavs(
    pieces: list[tuple[Path, str]],   # (path, role) tuples
    out_mp3: Path,
    title: str,
    artist: str,
    album: str,
    mastering: dict,
    bed_track: Path | None = None,
    bed_duck_db: float = -14,
) -> None:
    """Concat pieces with 400ms silences, applying optional per-piece normalization
    and a final mastering chain. `pieces` is a list of (path, role) where role
    keys into mastering.per_piece_normalize.targets. If `bed_track` is given,
    the bed is sidechain-ducked under the narration concat by `bed_duck_db`."""
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

        if bed_track and bed_track.exists():
            # Concat narration first, then mix with sidechain-ducked bed.
            narr_concat = td_p / "narration_concat.wav"
            subprocess.run(
                ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
                 "-f", "concat", "-safe", "0", "-i", str(concat_list),
                 "-c:a", "pcm_s16le", str(narr_concat)],
                check=True,
            )
            # Filter graph:
            #   [bed][narr]sidechaincompress  → bed ducked when narration is loud
            #   [narr][bed_ducked]amix         → mixed two-stream output
            #   then master chain
            duck_filter = (
                f"[1:a]volume=0dB[bed_pre];"
                f"[bed_pre][0:a]sidechaincompress="
                f"threshold=0.04:ratio=8:attack=20:release=300:makeup=1:level_sc=1[bed_ducked];"
                f"[0:a][bed_ducked]amix=inputs=2:normalize=0:weights=1 0.55[mixed];"
                f"[mixed]{master_filter}[out]"
            )
            subprocess.run(
                ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
                 "-i", str(narr_concat),
                 "-i", str(bed_track),
                 "-filter_complex", duck_filter,
                 "-map", "[out]",
                 "-c:a", "libmp3lame", "-b:a", "192k",
                 "-metadata", f"title={title}",
                 "-metadata", f"artist={artist}",
                 "-metadata", f"album={album}",
                 str(out_mp3)],
                check=True,
            )
        else:
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

    def _resolve_clip(demo_id: str) -> Path | None:
        if clips_dir is None:
            return None
        for ext in (".wav", ".aif", ".aiff"):
            cand = clips_dir / f"{demo_id}{ext}"
            if cand.exists():
                return cand
        return None

    def _clip_role(demo_id: str) -> str:
        # "op-..." = generated operator demo (tighter -22 LUFS target);
        # everything else = extracted song clip (looser -16 LUFS target)
        return "demo" if demo_id.startswith("op-") else "song"

    for slide in lesson.get("slides", []):
        script_rel = slide.get("script_md")
        if not script_rel:
            continue
        stem = Path(script_rel).stem

        # Cue-aware path: if render_voiceover produced a <stem>.cues.json sidecar,
        # the script had [cue: id] markers. Interleave chunk WAVs with demos.
        sidecar_path = narr_dir / f"{stem}.cues.json"
        block_pieces: list[tuple[Path, str]] = []
        used_cues: set[str] = set()

        if sidecar_path.exists():
            try:
                sidecar = json.loads(sidecar_path.read_text())
            except json.JSONDecodeError:
                sidecar = None
            if sidecar:
                for chunk in sidecar.get("chunks", []):
                    chunk_wav = narr_dir / chunk["wav"]
                    if not chunk_wav.exists():
                        continue
                    block_pieces.append((chunk_wav, "narration"))
                    cue_id = chunk.get("cue_after")
                    if not cue_id:
                        continue
                    cue_path = _resolve_clip(cue_id)
                    if cue_path:
                        block_pieces.append((cue_path, _clip_role(cue_id)))
                        used_cues.add(cue_id)
                    else:
                        missing_demos.append(f"{slide['id']}:cue:{cue_id}")

        # Fallback / no-cue path: single full-script WAV.
        if not block_pieces:
            wav_path = narr_dir / f"{stem}.wav"
            if not wav_path.exists():
                continue
            block_pieces.append((wav_path, "narration"))

        # Any demo IDs declared on the slide but NOT consumed as cues are
        # appended at the end of the block (legacy behavior).
        for demo_id in slide.get("demos", []) or []:
            if demo_id in used_cues:
                continue
            demo_path = _resolve_clip(demo_id)
            if demo_path:
                block_pieces.append((demo_path, _clip_role(demo_id)))
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

    # Track slide_id parallel to blocks for bed-layer time anchoring
    block_slides: list[str] = []
    if intro.exists():
        block_slides.append("_intro_")
    for slide in lesson.get("slides", []):
        script_rel = slide.get("script_md")
        if not script_rel:
            continue
        stem = Path(script_rel).stem
        # Only count slides that produced a block
        if (narr_dir / f"{stem}.cues.json").exists() or (narr_dir / f"{stem}.wav").exists():
            block_slides.append(slide["id"])
    if outro.exists():
        block_slides.append("_outro_")

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
    # Also emit a cuemap: the EXACT ms span of every spliced demo/song/transition
    # piece in the final mp3 (role != narration). Clip files are named <id>.wav,
    # so the piece path stem is the cue id. This lets the alignment tool measure
    # and play demos precisely instead of guessing from chapter timings.
    chapters = []
    cuemap = []
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
        for k, (ppath, prole) in enumerate(parts):
            if prole == "narration":
                continue
            gi = piece_idx + k
            cuemap.append({
                "heading": title,
                "cue_id": Path(ppath).stem,
                "role": prole,
                "demo_start_ms": piece_starts[gi],
                "demo_end_ms": piece_starts[gi] + durations[gi],
            })
        piece_idx += n

    out_mp3 = out_dir / f"{lesson_id}.mp3"
    sidecar = out_dir / f"{lesson_id}.chapters.json"

    # Compute block start/end times for bed anchoring (block N spans
    # piece_starts[first_piece] → piece_starts[last_piece] + durations[last_piece])
    block_starts: list[int] = []
    block_ends: list[int] = []
    pi = 0
    for _, parts in blocks:
        n = len(parts)
        block_starts.append(piece_starts[pi])
        last = pi + n - 1
        block_ends.append(piece_starts[last] + durations[last])
        pi += n

    # Optional bed layer: schema in episode.yaml
    #   beds:
    #     enabled: true
    #     duck_db: -14
    #     insertions:
    #       - clip_id: bed-warm-pad
    #         start_at_slide: 02a-vibrato-accident
    #         end_at_slide: 02d-yamaha-license
    #         gain_db: -2
    #         fade_in_ms: 3000
    #         fade_out_ms: 3000
    bed_track_path: Path | None = None
    beds_cfg = lesson.get("beds") or {}
    if beds_cfg.get("enabled") and clips_dir is not None:
        bed_track_path = out_dir / f"{lesson_id}.bed.wav"
        # mute the bed under every foreground demo/song cue (from the cuemap)
        mute_spans = [(c["demo_start_ms"], c["demo_end_ms"]) for c in cuemap
                      if c.get("role") in ("demo", "song")]
        try:
            build_bed_track(
                bed_insertions=beds_cfg.get("insertions") or [],
                block_starts=block_starts,
                block_ends=block_ends,
                block_slides=block_slides,
                total_ms=total_ms,
                clips_dir=clips_dir,
                out_path=bed_track_path,
                mute_spans=mute_spans,
            )
            if not bed_track_path.exists():
                bed_track_path = None
        except Exception as e:
            print(f"[bed] track generation failed: {e}; assembling without bed")
            bed_track_path = None

    concat_wavs(
        pieces, out_mp3,
        title=episode_cfg.get("title", lesson.get("title", lesson_id)),
        artist=show_artist,
        album=show_album,
        mastering=mastering,
        bed_track=bed_track_path,
        bed_duck_db=beds_cfg.get("duck_db", -14),
    )
    write_chapters(out_mp3, chapters, sidecar)
    (out_dir / f"{lesson_id}.cuemap.json").write_text(json.dumps(cuemap, indent=2))

    # Clean up the multi-hundred-MB intermediate bed track.
    if bed_track_path and bed_track_path.exists():
        try: bed_track_path.unlink()
        except OSError: pass

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

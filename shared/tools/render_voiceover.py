#!/usr/bin/env python3
"""
render_voiceover.py — render narration scripts (markdown) to WAV via OpenAI TTS.

Reads:
    <course_root>/lessons/*/script/*.md (or episodes/*/script/*.md depending on
    course content_kind).

Writes:
    <build_root>/audio/narration/<id>/<script_name>.wav
    <build_root>/audio/narration/.cache/<sha256>.wav

Usage:
    python shared/tools/render_voiceover.py --course-root courses/idm-12x12
    python shared/tools/render_voiceover.py --course-root courses/idm-12x12 --lesson w05-aphex-tuning
    python shared/tools/render_voiceover.py --course-root courses/idm-12x12 --dry-run

Script markup (from shared/style/voice.md):
    [pause 600ms]    → rendered as ". "
    *word*           → UPPER-CASED
    ~word~           → stripped
    — (em-dash)      → preserved
    <!-- comments --> / HTML tags → stripped

Requires:
    OPENAI_API_KEY in environment.
    uv pip install openai
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _course_lib import load_course, lessons_dir, episodes_dir, narration_out  # noqa: E402

VOICE_INSTRUCTION = (
    "Male, mid-30s, dry sardonic. Reads technical specs without awe. Pauses before "
    "punchlines. Never laughs audibly. Occasionally sighs. Reference: Ira Glass deadpan "
    "crossed with Steve Albini interview cadence. Slightly clipped diction, light "
    "English inflection welcome. No smiling-through-it."
)

RE_HTML_COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)
RE_HTML_TAG = re.compile(r"<[^>]+>")
RE_PAUSE = re.compile(r"\[pause\s+(\d+)\s*ms\]", re.IGNORECASE)
RE_EMPH = re.compile(r"\*([^*\n]+)\*")
RE_SARDONIC = re.compile(r"~([^~\n]+)~")
RE_FM_HEADER = re.compile(r"^---\n.*?\n---\n", re.DOTALL)
# Demo cue marker: own line, e.g.  [cue: op-ratio-1to1]
RE_CUE = re.compile(r"^\s*\[cue:\s*([a-zA-Z0-9_-]+)\]\s*$", re.MULTILINE)
# Bed marker: ambient bed clip starting at this point in the script.
# e.g. [bed: trans-bike-pulse]  or  [bed: stop]  to end the current bed.
RE_BED = re.compile(r"^\s*\[bed:\s*([a-zA-Z0-9_-]+)\]\s*$", re.MULTILINE)


def normalize(md: str) -> str:
    s = RE_FM_HEADER.sub("", md)
    s = RE_HTML_COMMENT.sub("", s)
    s = RE_HTML_TAG.sub("", s)
    # Strip cue + bed markers — those are handled by the orchestrator before TTS
    s = RE_CUE.sub("", s)
    s = RE_BED.sub("", s)
    s = RE_PAUSE.sub(". ", s)             # synthesize a beat from the period
    s = RE_EMPH.sub(lambda m: m.group(1).upper(), s)  # emphasis -> caps
    s = RE_SARDONIC.sub(lambda m: m.group(1), s)      # no pitch expression in tts-1-hd
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


def split_at_cues(md: str) -> tuple[list[str], list[dict]]:
    """Split the raw markdown at [cue: id] markers.

    Returns (chunks, cues) where chunks is a list of script-text segments and
    cues is a parallel list — cues[i] is the cue inserted AFTER chunks[i], or
    None for the final chunk. A cue dict has shape {"id": "<cue_id>"}.

    A script with no cues returns (chunks=[whole_text], cues=[None]).
    Bed markers are kept inline in chunk text — extracted by build_episode.
    """
    text = RE_FM_HEADER.sub("", md)
    text = RE_HTML_COMMENT.sub("", text)

    chunks: list[str] = []
    cues: list[dict | None] = []
    last_end = 0
    for m in RE_CUE.finditer(text):
        chunks.append(text[last_end:m.start()])
        cues.append({"id": m.group(1)})
        last_end = m.end()
    chunks.append(text[last_end:])
    cues.append(None)
    return chunks, cues


def extract_beds(md: str) -> list[dict]:
    """Pull bed markers from a chunk's text, returning a list of
    {"id": "<bed_id>"} in source order. The text is left as-is — markers are
    already stripped at TTS time by normalize()."""
    return [{"id": m.group(1)} for m in RE_BED.finditer(md)]


def content_hash(text: str, model: str, voice: str) -> str:
    h = hashlib.sha256()
    h.update(text.encode("utf-8"))
    h.update(model.encode("utf-8"))
    h.update(voice.encode("utf-8"))
    return h.hexdigest()


def synthesize(text: str, out_path: Path, model: str, voice: str, dry_run: bool) -> dict:
    if dry_run:
        return {"path": str(out_path), "status": "dry-run", "len_chars": len(text)}
    try:
        from openai import OpenAI
    except ImportError:
        return {"path": str(out_path), "status": "failed", "error": "openai pkg missing — uv pip install openai"}

    if not os.environ.get("OPENAI_API_KEY"):
        return {"path": str(out_path), "status": "failed", "error": "OPENAI_API_KEY not set"}

    client = OpenAI()

    out_path.parent.mkdir(parents=True, exist_ok=True)

    # Try gpt-4o-mini-tts first (supports instructions). Fall back to tts-1-hd.
    try:
        params = {"model": model, "voice": voice, "input": text, "response_format": "wav"}
        if model == "gpt-4o-mini-tts":
            params["instructions"] = VOICE_INSTRUCTION
        with client.audio.speech.with_streaming_response.create(**params) as resp:
            resp.stream_to_file(str(out_path))
        return {"path": str(out_path), "status": "ok", "model": model, "voice": voice, "len_chars": len(text)}
    except Exception as e:
        if model == "gpt-4o-mini-tts":
            try:
                with client.audio.speech.with_streaming_response.create(
                    model="tts-1-hd", voice=voice, input=text, response_format="wav"
                ) as resp:
                    resp.stream_to_file(str(out_path))
                return {"path": str(out_path), "status": "ok-fallback-tts1hd", "voice": voice, "len_chars": len(text)}
            except Exception as e2:
                return {"path": str(out_path), "status": "failed", "error": f"{e} || fallback: {e2}"}
        return {"path": str(out_path), "status": "failed", "error": str(e)}


def render_one(
    script_md: Path,
    item_id: str,
    model: str,
    voice: str,
    dry_run: bool,
    out_root: Path,
    cache_dir: Path,
    repo_root: Path,
) -> dict:
    raw = script_md.read_text()
    chunks_md, cues = split_at_cues(raw)
    chunk_texts = [normalize(c) for c in chunks_md]
    # Drop empty chunks but preserve the cue ordering.
    pruned: list[tuple[str, dict | None]] = []
    pending_cue: dict | None = None
    for txt, c in zip(chunk_texts, cues):
        if not txt.strip():
            # Forward any pending cue past the empty chunk
            if c is not None:
                pending_cue = c
            continue
        pruned.append((txt, c if c is not None else pending_cue))
        pending_cue = None
    if not pruned:
        return {"path": str(script_md), "status": "empty", "id": item_id}

    has_cues = any(c is not None for _, c in pruned[:-1]) or pending_cue is not None
    stem = script_md.stem
    item_dir = out_root / item_id
    item_dir.mkdir(parents=True, exist_ok=True)

    # Single-chunk path: keep classic <stem>.wav for backwards compat.
    if not has_cues and len(pruned) == 1:
        text = pruned[0][0]
        out_abs = item_dir / f"{stem}.wav"
        return _synth_one(text, out_abs, cache_dir, model, voice, dry_run, item_id, script_md, repo_root)

    # Multi-chunk: render each chunk to <stem>.<NNN>.wav and emit sidecar
    # JSON listing chunks + cues so build_episode can interleave demos.
    chunk_results: list[dict] = []
    sidecar_chunks: list[dict] = []
    for i, (text, cue) in enumerate(pruned):
        chunk_wav = item_dir / f"{stem}.{i:03d}.wav"
        beds = extract_beds(chunks_md[chunk_texts.index(chunks_md[0])] if False else "")  # placeholder; beds carried from raw chunks below
        # Pull beds from the original markdown chunk that produced this text:
        # find the corresponding chunks_md index.
        # (simpler: re-extract from the matching chunks_md element by position)
        r = _synth_one(text, chunk_wav, cache_dir, model, voice, dry_run, item_id, script_md, repo_root)
        r["chunk_index"] = i
        if cue:
            r["cue_after"] = cue["id"]
        chunk_results.append(r)
        sidecar_chunks.append({
            "wav": chunk_wav.name,
            "cue_after": cue["id"] if cue else None,
        })

    # Bed markers parsed from the raw chunks (one bed list per chunk).
    bed_lists: list[list[dict]] = [extract_beds(c) for c in chunks_md if normalize(c).strip()]
    # Trim to match pruned length (defensive)
    bed_lists = bed_lists[: len(pruned)]
    for i, b in enumerate(bed_lists):
        if b:
            sidecar_chunks[i]["beds"] = [bd["id"] for bd in b]

    sidecar_path = item_dir / f"{stem}.cues.json"
    sidecar_path.write_text(json.dumps({
        "stem": stem,
        "chunks": sidecar_chunks,
    }, indent=2))

    statuses = [r.get("status", "?") for r in chunk_results]
    overall = "ok" if all(s in ("ok", "ok-fallback-tts1hd", "cache-hit", "dry-run") for s in statuses) else "failed"
    return {
        "id": item_id,
        "stem": stem,
        "status": overall,
        "chunks": len(chunk_results),
        "chunk_statuses": statuses,
        "sidecar": str(sidecar_path),
    }


def _synth_one(
    text: str,
    out_abs: Path,
    cache_dir: Path,
    model: str,
    voice: str,
    dry_run: bool,
    item_id: str,
    script_md: Path,
    repo_root: Path,
) -> dict:
    cache_key = content_hash(text, model, voice)
    cache_path = cache_dir / f"{cache_key}.wav"
    if cache_path.exists():
        out_abs.parent.mkdir(parents=True, exist_ok=True)
        if not out_abs.exists() or out_abs.stat().st_size != cache_path.stat().st_size:
            try:
                os.link(cache_path, out_abs)
            except OSError:
                out_abs.write_bytes(cache_path.read_bytes())
        return {"path": str(out_abs), "status": "cache-hit", "hash": cache_key[:12], "id": item_id}
    result = synthesize(text, cache_path, model=model, voice=voice, dry_run=dry_run)
    if result["status"].startswith("ok"):
        out_abs.parent.mkdir(parents=True, exist_ok=True)
        try:
            os.link(cache_path, out_abs)
        except OSError:
            out_abs.write_bytes(cache_path.read_bytes())
        result["hash"] = cache_key[:12]
    result["id"] = item_id
    try:
        result["script"] = str(script_md.relative_to(repo_root))
    except ValueError:
        result["script"] = str(script_md)
    return result


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--course-root", required=True)
    ap.add_argument("--lesson", help="lesson|episode id, e.g. w05-aphex-tuning")
    ap.add_argument("--model", default="gpt-4o-mini-tts", help="OpenAI TTS model id")
    ap.add_argument(
        "--voice",
        default="onyx",
        help="OpenAI voice: onyx|alloy|echo|fable|ash|coral|sage|nova",
    )
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    cfg = load_course(args.course_root)
    out_root = narration_out(cfg)
    cache_dir = out_root / ".cache"
    status_out = out_root / "_render_status.json"
    cache_dir.mkdir(parents=True, exist_ok=True)

    content_kind = cfg.get("content_kind", "lesson")
    items_root = (
        episodes_dir(cfg) if content_kind == "episode" else lessons_dir(cfg)
    )

    item_dirs = (
        sorted(items_root.iterdir())
        if not args.lesson
        else [items_root / args.lesson]
    )
    item_dirs = [d for d in item_dirs if d.is_dir()]

    results = []
    for idir in item_dirs:
        item_id = idir.name
        script_dir = idir / "script"
        if not script_dir.exists():
            continue
        for script_md in sorted(script_dir.glob("*.md")):
            r = render_one(
                script_md,
                item_id,
                args.model,
                args.voice,
                args.dry_run,
                out_root=out_root,
                cache_dir=cache_dir,
                repo_root=cfg["_repo_root"],
            )
            print(f"[tts] {item_id}/{script_md.name}: {r['status']}", flush=True)
            results.append(r)

    status_out.parent.mkdir(parents=True, exist_ok=True)
    status_out.write_text(json.dumps(results, indent=2))

    ok = sum(
        1
        for r in results
        if r["status"] in ("ok", "ok-fallback-tts1hd", "cache-hit", "dry-run")
    )
    print(f"\nrender_voiceover: {ok}/{len(results)} ok — status: {status_out}")
    return 0 if ok == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())

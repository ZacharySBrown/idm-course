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


def normalize(md: str) -> str:
    s = RE_FM_HEADER.sub("", md)
    s = RE_HTML_COMMENT.sub("", s)
    s = RE_HTML_TAG.sub("", s)
    s = RE_PAUSE.sub(". ", s)             # synthesize a beat from the period
    s = RE_EMPH.sub(lambda m: m.group(1).upper(), s)  # emphasis -> caps
    s = RE_SARDONIC.sub(lambda m: m.group(1), s)      # no pitch expression in tts-1-hd
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


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
    text = normalize(script_md.read_text())
    if not text.strip():
        return {"path": str(script_md), "status": "empty", "id": item_id}

    out_rel = Path(item_id) / (script_md.stem + ".wav")
    out_abs = out_root / out_rel
    cache_key = content_hash(text, model, voice)
    cache_path = cache_dir / f"{cache_key}.wav"

    if cache_path.exists():
        out_abs.parent.mkdir(parents=True, exist_ok=True)
        if not out_abs.exists() or out_abs.stat().st_size != cache_path.stat().st_size:
            try:
                os.link(cache_path, out_abs)
            except OSError:
                out_abs.write_bytes(cache_path.read_bytes())
        return {"path": str(out_abs), "status": "cache-hit", "hash": cache_key[:12]}

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

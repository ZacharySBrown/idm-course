#!/usr/bin/env python3
"""
render_voiceover.py — render narration scripts (markdown) to WAV via OpenAI TTS.

Reads:
    lessons/*/script/*.md

Writes:
    build/audio/narration/<lesson>/<script_name>.wav
    build/audio/narration/.cache/<sha256>.wav     (content-addressed cache)

Usage:
    python tools/render_voiceover.py                  # all lessons
    python tools/render_voiceover.py --lesson w05-aphex-tuning
    python tools/render_voiceover.py --dry-run        # parse only, no API call

Script markup (from style/voice.md):
    [pause 600ms]    → rendered as ". " (tts-1-hd has no SSML; punctuation approximates)
    *word*           → UPPER-CASED (tts-1-hd responds to caps as emphasis)
    ~word~           → stripped (pitch-down not expressible)
    — (em-dash)      → preserved
    <!-- comments --> → stripped
    HTML tags         → stripped

Provider defaults:
    OpenAI gpt-4o-mini-tts (if key present; supports voice 'onyx', instructions via 'instructions' field)
    Falls back to openai tts-1-hd if gpt-4o-mini-tts unavailable.

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

ROOT = Path(__file__).resolve().parent.parent
LESSONS = ROOT / "lessons"
OUT = ROOT / "build" / "audio" / "narration"
CACHE = OUT / ".cache"
STATUS_OUT = OUT / "_render_status.json"

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


def render_one(script_md: Path, lesson_id: str, model: str, voice: str, dry_run: bool) -> dict:
    text = normalize(script_md.read_text())
    if not text.strip():
        return {"path": str(script_md), "status": "empty", "lesson": lesson_id}

    out_rel = Path(lesson_id) / (script_md.stem + ".wav")
    out_abs = OUT / out_rel
    cache_key = content_hash(text, model, voice)
    cache_path = CACHE / f"{cache_key}.wav"

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
    result["lesson"] = lesson_id
    result["script"] = str(script_md.relative_to(ROOT))
    return result


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lesson", help="e.g. w05-aphex-tuning")
    ap.add_argument("--model", default="gpt-4o-mini-tts", help="OpenAI TTS model id")
    ap.add_argument("--voice", default="onyx", help="OpenAI voice: onyx|alloy|echo|fable|ash|coral|sage|nova")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    CACHE.mkdir(parents=True, exist_ok=True)

    lesson_dirs = sorted(LESSONS.iterdir()) if not args.lesson else [LESSONS / args.lesson]
    lesson_dirs = [d for d in lesson_dirs if d.is_dir()]

    results = []
    for ldir in lesson_dirs:
        lesson_id = ldir.name
        script_dir = ldir / "script"
        if not script_dir.exists():
            continue
        for script_md in sorted(script_dir.glob("*.md")):
            r = render_one(script_md, lesson_id, args.model, args.voice, args.dry_run)
            print(f"[tts] {lesson_id}/{script_md.name}: {r['status']}", flush=True)
            results.append(r)

    STATUS_OUT.parent.mkdir(parents=True, exist_ok=True)
    STATUS_OUT.write_text(json.dumps(results, indent=2))

    ok = sum(1 for r in results if r["status"] in ("ok", "ok-fallback-tts1hd", "cache-hit", "dry-run"))
    print(f"\nrender_voiceover: {ok}/{len(results)} ok — status: {STATUS_OUT}")
    return 0 if ok == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())

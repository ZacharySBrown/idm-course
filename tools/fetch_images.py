#!/usr/bin/env python3
"""
fetch_images.py — download + optimize images declared in references/images.json.

For each entry:
  - If source_url is a direct image URL → curl, then Pillow resize/encode
  - If source_url is a Wikipedia article / Commons page → try to resolve the
    primary image via MediaWiki API
  - Target max width 1600px, JPEG quality 85 for photos, PNG as-is for UI shots
  - Writes to entry.local_path (relative to repo root)
  - Skips if local file already exists

Status → build/images_fetch_status.json

Usage:
    python3 tools/fetch_images.py
    python3 tools/fetch_images.py --redo       # refetch even if local exists
    python3 tools/fetch_images.py --only gear_qy700_hero
"""
from __future__ import annotations

import argparse
import json
import mimetypes
import re
import ssl
import sys
import urllib.parse
import urllib.request
from io import BytesIO
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    sys.exit("pip install Pillow")

ROOT = Path(__file__).resolve().parent.parent
IMAGES_JSON = ROOT / "references" / "images.json"
STATUS = ROOT / "build" / "images_fetch_status.json"
MAX_WIDTH = 1600
JPEG_QUALITY = 85

UA = {"User-Agent": "IDM-Course-Builder/0.1 (educational non-commercial use)"}
CTX = ssl.create_default_context()


def fetch_bytes(url: str, timeout: int = 30) -> tuple[bytes, str] | None:
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
            ctype = r.headers.get("Content-Type", "")
            return r.read(), ctype
    except Exception as e:
        return None


def resolve_wikipedia_article_to_image(url: str) -> str | None:
    """For Wikipedia article URLs, fetch the page and find og:image."""
    data = fetch_bytes(url)
    if not data:
        return None
    html = data[0].decode("utf-8", errors="ignore")
    m = re.search(r'<meta[^>]+property="og:image"[^>]+content="([^"]+)"', html)
    if m:
        return m.group(1)
    m = re.search(r'<link[^>]+rel="image_src"[^>]+href="([^"]+)"', html)
    if m:
        return m.group(1)
    return None


def resolve_commons_file_page(url: str) -> str | None:
    """For commons.wikimedia.org/wiki/File:... pages, fetch the actual image."""
    data = fetch_bytes(url)
    if not data:
        return None
    html = data[0].decode("utf-8", errors="ignore")
    m = re.search(r'<meta[^>]+property="og:image"[^>]+content="([^"]+)"', html)
    if m:
        return m.group(1)
    m = re.search(r'<div class="fullImageLink"[^>]*>\s*<a href="([^"]+)"', html)
    if m:
        src = m.group(1)
        if src.startswith("//"):
            src = "https:" + src
        return src
    return None


def derive_image_url(url: str) -> str | None:
    if not url:
        return None
    ulc = url.lower()
    # Direct image URL
    if re.search(r"\.(jpg|jpeg|png|gif|webp)(\?.*)?$", ulc):
        return url
    # Wikipedia article
    if "wikipedia.org/wiki/" in url and "/wiki/File:" not in url:
        return resolve_wikipedia_article_to_image(url)
    # Commons file page
    if "commons.wikimedia.org/wiki/File:" in url or "wikipedia.org/wiki/File:" in url:
        return resolve_commons_file_page(url)
    # Ableton features page — look for og:image
    if "ableton.com" in ulc:
        return resolve_wikipedia_article_to_image(url)  # same og:image logic
    # Unknown — try as-is; worst case curl returns HTML and we catch below
    return url


def save_image(data: bytes, out_path: Path, ctype: str) -> str:
    try:
        img = Image.open(BytesIO(data))
    except Exception as e:
        raise ValueError(f"not a valid image: {e}")
    w, h = img.size
    if w > MAX_WIDTH:
        scale = MAX_WIDTH / w
        img = img.resize((MAX_WIDTH, int(h * scale)), Image.LANCZOS)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    is_png = out_path.suffix.lower() == ".png" or ctype.endswith("png")
    if is_png and "png" in ctype.lower():
        img.save(out_path, "PNG", optimize=True)
    else:
        if img.mode not in ("RGB", "L"):
            img = img.convert("RGB")
        # Force .jpg extension if saving JPEG
        if not out_path.suffix.lower() in (".jpg", ".jpeg"):
            out_path = out_path.with_suffix(".jpg")
        img.save(out_path, "JPEG", quality=JPEG_QUALITY, optimize=True, progressive=True)
    return str(out_path)


def fetch_one(slug: str, entry: dict, redo: bool) -> dict:
    source_url = entry.get("source_url")
    local_rel = entry.get("local_path")
    if not source_url:
        return {"slug": slug, "status": "no-source-url"}
    if not local_rel:
        return {"slug": slug, "status": "no-local-path"}

    out_path = ROOT / local_rel
    if out_path.exists() and not redo:
        return {"slug": slug, "status": "skipped-exists", "path": local_rel}

    img_url = derive_image_url(source_url)
    if not img_url:
        return {"slug": slug, "status": "resolve-failed", "source": source_url}

    result = fetch_bytes(img_url)
    if result is None:
        return {"slug": slug, "status": "fetch-failed", "url": img_url}

    data, ctype = result
    if "html" in ctype.lower():
        return {"slug": slug, "status": "got-html-not-image", "url": img_url, "ctype": ctype}

    try:
        saved = save_image(data, out_path, ctype)
    except Exception as e:
        return {"slug": slug, "status": "save-failed", "error": str(e)}

    return {
        "slug": slug,
        "status": "ok",
        "path": str(Path(saved).relative_to(ROOT)),
        "source_bytes": len(data),
        "derived_url": img_url if img_url != source_url else None,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--redo", action="store_true")
    ap.add_argument("--only")
    args = ap.parse_args()

    data = json.loads(IMAGES_JSON.read_text())
    entries = {k: v for k, v in data.items() if k.startswith("img:")}

    results = []
    n_ok = n_skip = n_fail = 0
    for slug, entry in entries.items():
        if args.only and args.only not in slug:
            continue
        r = fetch_one(slug, entry, args.redo)
        results.append(r)
        if r["status"] == "ok":
            n_ok += 1
        elif r["status"].startswith("skip"):
            n_skip += 1
        else:
            n_fail += 1
        print(f"[img] {slug}: {r['status']}")

    STATUS.parent.mkdir(parents=True, exist_ok=True)
    STATUS.write_text(json.dumps({"ok": n_ok, "skip": n_skip, "fail": n_fail, "results": results}, indent=2))
    print(f"\nfetch_images: {n_ok} ok / {n_skip} skipped / {n_fail} failed — status: {STATUS}")
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

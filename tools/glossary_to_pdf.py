#!/usr/bin/env python3
"""
glossary_to_pdf.py — convert build/glossary.md to build/pdf/idm_glossary.pdf
for reMarkable sync.

Prefers pandoc + xelatex. Falls back to pandoc's default PDF engine. If pandoc
is missing, renders via weasyprint from the HTML version.

Usage:
    python3 tools/render_glossary.py      # generates the md first
    python3 tools/glossary_to_pdf.py
"""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC_MD = ROOT / "build" / "glossary.md"
SRC_HTML = ROOT / "build" / "html" / "glossary.html"
OUT_PDF = ROOT / "build" / "pdf" / "idm_glossary.pdf"


def try_pandoc() -> bool:
    if not shutil.which("pandoc"):
        return False
    OUT_PDF.parent.mkdir(parents=True, exist_ok=True)
    engines = ["xelatex", "pdflatex", "lualatex", "wkhtmltopdf", "weasyprint"]
    for eng in engines:
        if not shutil.which(eng) and eng not in ("wkhtmltopdf", "weasyprint"):
            continue
        try:
            r = subprocess.run(
                ["pandoc", str(SRC_MD), "-o", str(OUT_PDF), f"--pdf-engine={eng}"],
                capture_output=True, text=True,
            )
            if r.returncode == 0 and OUT_PDF.exists() and OUT_PDF.stat().st_size > 1000:
                print(f"[pdf] pandoc + {eng} → {OUT_PDF}")
                return True
            else:
                print(f"[pdf] pandoc with {eng} failed: {r.stderr[-300:]}", file=sys.stderr)
        except FileNotFoundError:
            continue
    return False


def try_weasyprint_from_html() -> bool:
    try:
        from weasyprint import HTML  # type: ignore
    except ImportError:
        return False
    if not SRC_HTML.exists():
        return False
    OUT_PDF.parent.mkdir(parents=True, exist_ok=True)
    HTML(filename=str(SRC_HTML)).write_pdf(str(OUT_PDF))
    print(f"[pdf] weasyprint → {OUT_PDF}")
    return True


def try_chrome_headless() -> bool:
    chrome_paths = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
        shutil.which("google-chrome") or "",
        shutil.which("chromium") or "",
    ]
    chrome = next((p for p in chrome_paths if p and Path(p).exists()), None)
    if not chrome or not SRC_HTML.exists():
        return False
    OUT_PDF.parent.mkdir(parents=True, exist_ok=True)
    html_abs = SRC_HTML.resolve()
    r = subprocess.run(
        [chrome, "--headless=new", "--disable-gpu", "--no-margins",
         "--no-pdf-header-footer",
         f"--print-to-pdf={OUT_PDF}",
         f"file://{html_abs}"],
        capture_output=True, text=True, timeout=60,
    )
    if OUT_PDF.exists() and OUT_PDF.stat().st_size > 5000:
        print(f"[pdf] Chrome headless → {OUT_PDF} ({OUT_PDF.stat().st_size // 1024} kB)")
        return True
    print(f"[pdf] Chrome headless failed: rc={r.returncode} stderr={r.stderr[-300:]}", file=sys.stderr)
    return False


def try_wkhtmltopdf() -> bool:
    if not shutil.which("wkhtmltopdf"):
        return False
    if not SRC_HTML.exists():
        return False
    OUT_PDF.parent.mkdir(parents=True, exist_ok=True)
    r = subprocess.run(
        ["wkhtmltopdf", "--print-media-type", "--enable-local-file-access",
         str(SRC_HTML), str(OUT_PDF)],
        capture_output=True, text=True,
    )
    if r.returncode == 0 and OUT_PDF.exists() and OUT_PDF.stat().st_size > 1000:
        print(f"[pdf] wkhtmltopdf → {OUT_PDF}")
        return True
    return False


def main() -> int:
    if not SRC_MD.exists() and not SRC_HTML.exists():
        sys.exit("run tools/render_glossary.py first to generate source")

    if try_pandoc():
        return 0
    print("[pdf] pandoc path failed or unavailable, trying Chrome headless...", file=sys.stderr)
    if try_chrome_headless():
        return 0
    print("[pdf] Chrome headless failed, trying weasyprint...", file=sys.stderr)
    if try_weasyprint_from_html():
        return 0
    print("[pdf] weasyprint unavailable, trying wkhtmltopdf...", file=sys.stderr)
    if try_wkhtmltopdf():
        return 0

    print(
        "[pdf] NO PDF ENGINE AVAILABLE.\n"
        "Install one of:\n"
        "  brew install pandoc basictex      (MacTeX Basic)\n"
        "  pip install weasyprint\n"
        "  brew install --cask wkhtmltopdf",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())

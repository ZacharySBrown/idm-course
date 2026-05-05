#!/usr/bin/env python3
"""
Generate podcast cover art (1500×1500, JPG, Tape Op-coded) at the path
declared in course.yaml's podcast.artwork_path. Swap in custom art later
by replacing the JPG and re-committing.
"""
import argparse
import sys
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "shared" / "tools"))
from _course_lib import load_course  # noqa: E402

_ap = argparse.ArgumentParser()
_ap.add_argument("--course-root", required=True)
_args, _rest = _ap.parse_known_args()
sys.argv = [sys.argv[0]] + _rest
_cfg = load_course(_args.course_root)
ROOT = _cfg["_repo_root"]
_artwork_rel = ((_cfg.get("podcast") or {}).get("artwork_path", "artwork-ableton.jpg"))
OUT = ROOT / _artwork_rel

SIZE = 1500
BG = (244, 240, 232)     # cream — matches deck CSS
INK = (17, 17, 17)
DIM = (90, 80, 71)
ACCENT = (139, 26, 26)

FONT_SERIF = "/System/Library/Fonts/Supplemental/Georgia.ttf"
FONT_SERIF_BOLD = "/System/Library/Fonts/Supplemental/Georgia Bold.ttf"
FONT_MONO = "/System/Library/Fonts/Menlo.ttc"
FONT_ITALIC = "/System/Library/Fonts/Supplemental/Georgia Italic.ttf"


def font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.load_default()


def main():
    img = Image.new("RGB", (SIZE, SIZE), BG)
    d = ImageDraw.Draw(img)

    # Header thin rule
    d.line([(120, 180), (SIZE - 120, 180)], fill=INK, width=3)

    # Top caption (mono, uppercase, letter-spaced)
    caption = "DEVICES, HISTORY, AND TECHNIQUE"
    f_cap = font(FONT_MONO, 34)
    w = d.textlength(caption, font=f_cap)
    d.text(((SIZE - w) / 2, 128), caption, font=f_cap, fill=DIM)

    # Main title — two lines of giant serif
    f_title = font(FONT_SERIF_BOLD, 220)
    line1 = "Ableton"
    line2 = "Mastery"
    w1 = d.textlength(line1, font=f_title)
    w2 = d.textlength(line2, font=f_title)
    d.text(((SIZE - w1) / 2, 320), line1, font=f_title, fill=INK)
    d.text(((SIZE - w2) / 2, 560), line2, font=f_title, fill=INK)

    # Italic subtitle
    f_sub = font(FONT_ITALIC, 64)
    sub = "ten devices, ten episodes"
    ws = d.textlength(sub, font=f_sub)
    d.text(((SIZE - ws) / 2, 870), sub, font=f_sub, fill=DIM)

    # Middle divider with accent tick
    y = 1020
    d.line([(300, y), (SIZE - 300, y)], fill=INK, width=2)
    cx = SIZE // 2
    d.rectangle([(cx - 6, y - 10), (cx + 6, y + 10)], fill=ACCENT)

    # Device list — mono, spaced (matches the 10 episode arc)
    f_pill = font(FONT_MONO, 32)
    devices = [
        "OPERATOR   ·   ANALOG   ·   WAVETABLE",
        "MELD   ·   WARP MODES   ·   DRUM RACK",
        "GRANULATOR III   ·   SPECTRAL   ·   M4L",
    ]
    y0 = 1100
    for i, line in enumerate(devices):
        wl = d.textlength(line, font=f_pill)
        d.text(((SIZE - wl) / 2, y0 + i * 56), line, font=f_pill, fill=INK)

    # Footer — thin rule + mono motto
    d.line([(120, SIZE - 180), (SIZE - 120, SIZE - 180)], fill=INK, width=3)
    f_foot = font(FONT_MONO, 28)
    motto = "PATCH  ·  HISTORY  ·  PRODUCTION"
    wf = d.textlength(motto, font=f_foot)
    d.text(((SIZE - wf) / 2, SIZE - 140), motto, font=f_foot, fill=DIM)

    # Corner annotation (like Tape Op spine number)
    f_corner = font(FONT_MONO, 22)
    d.text((120, 60), "ABLETON / 01 / 10", font=f_corner, fill=DIM)
    zak_tag = "ZAK — RAINDOG.AI"
    wc = d.textlength(zak_tag, font=f_corner)
    d.text((SIZE - wc - 120, 60), zak_tag, font=f_corner, fill=DIM)

    img.save(OUT, "JPEG", quality=92, optimize=True, progressive=True)
    print(f"art → {OUT}  ({OUT.stat().st_size // 1024} kB, {SIZE}×{SIZE})")


if __name__ == "__main__":
    main()

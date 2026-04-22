#!/usr/bin/env python3
"""
Generate podcast cover art (1500×1500, JPG, Tape Op-coded) at repo root.
Swap in custom art later by replacing /artwork.jpg and re-committing.
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "artwork.jpg"

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
    caption = "A COURSE ON ELECTRONIC MUSIC PRODUCTION"
    f_cap = font(FONT_MONO, 34)
    w = d.textlength(caption, font=f_cap)
    d.text(((SIZE - w) / 2, 128), caption, font=f_cap, fill=DIM)

    # Main title — two lines of giant serif
    f_title = font(FONT_SERIF_BOLD, 220)
    line1 = "IDM"
    line2 = "Production"
    w1 = d.textlength(line1, font=f_title)
    w2 = d.textlength(line2, font=f_title)
    d.text(((SIZE - w1) / 2, 320), line1, font=f_title, fill=INK)
    d.text(((SIZE - w2) / 2, 560), line2, font=f_title, fill=INK)

    # Italic subtitle
    f_sub = font(FONT_ITALIC, 72)
    sub = "twelve weeks, twelve tracks"
    ws = d.textlength(sub, font=f_sub)
    d.text(((SIZE - ws) / 2, 860), sub, font=f_sub, fill=DIM)

    # Middle divider with accent tick
    y = 1020
    d.line([(300, y), (SIZE - 300, y)], fill=INK, width=2)
    # Accent bar in center
    cx = SIZE // 2
    d.rectangle([(cx - 6, y - 10), (cx + 6, y + 10)], fill=ACCENT)

    # Pillar list — mono, spaced
    f_pill = font(FONT_MONO, 36)
    pillars = [
        "APHEX TWIN   ·   AUTECHRE   ·   FOUR TET",
        "SQUAREPUSHER   ·   J DILLA   ·   DJ SHADOW",
        "PREMIER   ·   KANYE   ·   MADLIB   ·   BURIAL",
    ]
    y0 = 1100
    for i, line in enumerate(pillars):
        wl = d.textlength(line, font=f_pill)
        d.text(((SIZE - wl) / 2, y0 + i * 60), line, font=f_pill, fill=INK)

    # Footer — thin rule + mono motto
    d.line([(120, SIZE - 180), (SIZE - 120, SIZE - 180)], fill=INK, width=3)
    f_foot = font(FONT_MONO, 28)
    motto = "CONSTRAINT  ·  RECOMBINATION  ·  COMPLETION"
    wf = d.textlength(motto, font=f_foot)
    d.text(((SIZE - wf) / 2, SIZE - 140), motto, font=f_foot, fill=DIM)

    # Corner annotation (like Tape Op spine number)
    f_corner = font(FONT_MONO, 22)
    d.text((120, 60), "IDM / 01 / 12", font=f_corner, fill=DIM)
    zak_tag = "ZAK — RAINDOG.AI"
    wc = d.textlength(zak_tag, font=f_corner)
    d.text((SIZE - wc - 120, 60), zak_tag, font=f_corner, fill=DIM)

    img.save(OUT, "JPEG", quality=92, optimize=True, progressive=True)
    print(f"art → {OUT}  ({OUT.stat().st_size // 1024} kB, {SIZE}×{SIZE})")


if __name__ == "__main__":
    main()

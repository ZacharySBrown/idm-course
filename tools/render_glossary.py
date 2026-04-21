#!/usr/bin/env python3
"""
render_glossary.py — emit build/html/glossary.html (browsable) and
build/glossary.md (source for PDF export).

Reads: references/glossary.json
Writes:
  - build/html/glossary.html  (Tape Op-coded HTML)
  - build/glossary.md          (pandoc-ready markdown for PDF export)
"""
from __future__ import annotations

import json
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REFS = ROOT / "references"
BUILD_HTML = ROOT / "build" / "html"
BUILD = ROOT / "build"

CATEGORY_ORDER = [
    "dsp_primitive",
    "mix_master",
    "time_rhythm",
    "signal_path",
    "ableton_specific",
    "hardware_history",
    "sampling",
    "named_technique",
    "artist_studio",
    "music_theory",
]
CATEGORY_LABELS = {
    "dsp_primitive": "DSP primitives",
    "mix_master": "Mix & master",
    "time_rhythm": "Time & rhythm",
    "signal_path": "Signal path",
    "ableton_specific": "Ableton specifics",
    "hardware_history": "Hardware & history",
    "sampling": "Sampling",
    "named_technique": "Named techniques",
    "artist_studio": "Artists & studios",
    "music_theory": "Music theory",
}


CSS = """
:root {
  --bg: #f4f0e8; --ink: #111; --dim: #5a5047; --line: #2a2520;
  --accent: #8b1a1a; --pill-bg: #e8e0d2;
  --mono: "JetBrains Mono","Berkeley Mono",ui-monospace,Menlo,Consolas,monospace;
  --serif: "Charter","Iowan Old Style","Georgia",serif;
  --sans: "Inter",system-ui,-apple-system,"Helvetica Neue",sans-serif;
}
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; background: var(--bg); color: var(--ink); }
body { font-family: var(--serif); font-size: 17px; line-height: 1.55; }
a { color: var(--accent); text-decoration: underline; text-underline-offset: 3px; }
a:hover { background: var(--ink); color: var(--bg); text-decoration: none; }

.hdr { border-bottom: 2px solid var(--ink); padding: 16px 32px; display: flex; justify-content: space-between; align-items: baseline;
  font-family: var(--sans); font-size: 13px; letter-spacing: 0.05em; text-transform: uppercase; position: sticky; top: 0; background: var(--bg); z-index: 10; }
.hdr .crumb a { color: var(--ink); }

.wrap { display: grid; grid-template-columns: 220px 1fr; gap: 40px; max-width: 1100px; margin: 0 auto; padding: 40px 32px 80px; }
.toc { position: sticky; top: 60px; align-self: start; font-family: var(--sans); font-size: 13px; }
.toc a { display: block; padding: 4px 0; color: var(--ink); text-decoration: none; border-bottom: 1px solid transparent; }
.toc a:hover { border-bottom-color: var(--line); background: transparent; }
.toc .count { color: var(--dim); font-family: var(--mono); font-size: 11px; margin-left: 6px; }

.content h1 { font-family: var(--serif); font-size: 40px; font-weight: 400; letter-spacing: -0.01em; margin: 0 0 8px 0; }
.content .tag { font-family: var(--sans); font-size: 13px; text-transform: uppercase; letter-spacing: 0.1em; color: var(--dim); margin-bottom: 40px; }

.cat { margin-bottom: 50px; }
.cat h2 { font-family: var(--sans); font-size: 13px; text-transform: uppercase; letter-spacing: 0.15em; color: var(--dim); margin: 0 0 20px; font-weight: 500; border-bottom: 1px solid var(--line); padding-bottom: 8px; }

.term { margin-bottom: 24px; padding: 0; }
.term .name { font-family: var(--serif); font-size: 22px; font-weight: 500; margin: 0; }
.term .name .slug { color: var(--dim); font-family: var(--mono); font-size: 11px; margin-left: 10px; font-weight: 400; letter-spacing: 0.04em; text-transform: lowercase; }
.term .def { margin: 8px 0 10px; }
.term .meta { font-family: var(--sans); font-size: 12px; color: var(--dim); }
.term .meta a { font-family: var(--mono); font-size: 11px; margin-right: 12px; padding: 2px 6px; background: var(--pill-bg); border: 1px solid var(--line); text-decoration: none; color: var(--ink); text-transform: uppercase; letter-spacing: 0.06em; }
.term .meta a:hover { background: var(--ink); color: var(--bg); }
.term .xrefs { font-family: var(--sans); font-size: 12px; color: var(--dim); margin-top: 6px; }
.term .xrefs .xref { display: inline-block; margin-right: 8px; padding: 1px 6px; background: rgba(0,0,0,0.05); border-radius: 3px; font-family: var(--mono); font-size: 11px; }

.search { font-family: var(--mono); font-size: 13px; padding: 8px 12px; border: 1px solid var(--line); background: #fff; width: 100%; margin-bottom: 24px; }
"""

JS = r"""
(function() {
  const input = document.querySelector('#search');
  const terms = Array.from(document.querySelectorAll('.term'));
  const cats = Array.from(document.querySelectorAll('.cat'));
  input.addEventListener('input', () => {
    const q = input.value.toLowerCase().trim();
    terms.forEach(t => {
      const blob = t.dataset.blob || '';
      t.style.display = (!q || blob.includes(q)) ? '' : 'none';
    });
    cats.forEach(c => {
      const any = c.querySelectorAll('.term:not([style*="display: none"])').length;
      c.style.display = any > 0 || !q ? '' : 'none';
    });
  });
})();
"""


def render_term_html(slug: str, entry: dict) -> str:
    term = escape(entry.get("term", slug))
    definition = escape(entry.get("definition", ""))
    wiki = entry.get("wikipedia_url")
    alt_links = entry.get("alt_links") or []
    bib_refs = entry.get("bib_refs") or []
    song_refs = entry.get("song_refs") or []
    see_also = entry.get("see_also") or []
    first_lesson = entry.get("first_used_in_lesson")

    link_pills = []
    if wiki:
        link_pills.append(f'<a href="{escape(wiki)}" target="_blank" rel="noopener">wikipedia</a>')
    for lk in alt_links:
        dom = lk.split("/")[2] if "://" in lk else lk[:20]
        link_pills.append(f'<a href="{escape(lk)}" target="_blank" rel="noopener">{escape(dom)}</a>')
    if first_lesson:
        link_pills.append(f'<a href="{escape(first_lesson)}/index.html">lesson: {escape(first_lesson)}</a>')

    xref_html = ""
    xrefs = []
    for s in see_also:
        xrefs.append(f'<span class="xref"><a href="#{escape(s)}" style="text-decoration:none;color:inherit">{escape(s)}</a></span>')
    for b in bib_refs:
        xrefs.append(f'<span class="xref">{escape(b)}</span>')
    for s in song_refs:
        xrefs.append(f'<span class="xref">{escape(s)}</span>')
    if xrefs:
        xref_html = f'<div class="xrefs">see also: {"".join(xrefs)}</div>'

    blob = " ".join([slug, term, definition, " ".join(see_also), " ".join(bib_refs)]).lower()

    return (
        f'<div class="term" id="{escape(slug)}" data-blob="{escape(blob)}">'
        f'<div class="name">{term}<span class="slug">{escape(slug)}</span></div>'
        f'<div class="def">{definition}</div>'
        f'<div class="meta">{" ".join(link_pills)}</div>'
        f'{xref_html}'
        f'</div>'
    )


def render_term_md(slug: str, entry: dict) -> str:
    term = entry.get("term", slug)
    definition = entry.get("definition", "")
    wiki = entry.get("wikipedia_url")
    alt_links = entry.get("alt_links") or []
    see_also = entry.get("see_also") or []

    md = f"### {term} `{slug}`\n\n{definition}\n\n"
    links = []
    if wiki:
        links.append(f"[Wikipedia]({wiki})")
    links.extend(f"<{lk}>" for lk in alt_links)
    if links:
        md += f"*Links:* {' · '.join(links)}\n\n"
    if see_also:
        md += f"*See also:* {', '.join(see_also)}\n\n"
    return md


def main() -> int:
    glossary = json.loads((REFS / "glossary.json").read_text())
    terms = {k: v for k, v in glossary.items() if not k.startswith("_")}

    # Group by category, sort terms alphabetically within
    by_cat = {}
    for slug, entry in terms.items():
        cat = entry.get("category", "other")
        by_cat.setdefault(cat, []).append((slug, entry))
    for cat in by_cat:
        by_cat[cat].sort(key=lambda x: x[1].get("term", x[0]).lower())

    # HTML
    BUILD_HTML.mkdir(parents=True, exist_ok=True)

    toc_html = "".join(
        f'<a href="#{cat}">{CATEGORY_LABELS.get(cat, cat)}<span class="count">{len(by_cat.get(cat, []))}</span></a>'
        for cat in CATEGORY_ORDER if cat in by_cat
    )

    cats_html = ""
    for cat in CATEGORY_ORDER:
        if cat not in by_cat:
            continue
        terms_html = "\n".join(render_term_html(s, e) for s, e in by_cat[cat])
        cats_html += (
            f'<section class="cat" id="{cat}">'
            f'<h2>{CATEGORY_LABELS.get(cat, cat)} <span class="count">— {len(by_cat[cat])} terms</span></h2>'
            f'{terms_html}'
            f'</section>'
        )

    html = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>IDM Course — Glossary</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>{CSS}</style>
</head><body>

<div class="hdr">
  <div class="crumb"><a href="index.html">IDM Course</a> / Glossary</div>
  <div>{len(terms)} terms</div>
</div>

<div class="wrap">
  <nav class="toc">{toc_html}</nav>
  <main class="content">
    <h1>Glossary</h1>
    <div class="tag">{len(terms)} terms · Wikipedia + spec cross-refs · built for the decks and for reMarkable</div>
    <input id="search" class="search" placeholder="filter — type to search definitions, terms, slugs, cross-refs">
    {cats_html}
  </main>
</div>

<script>{JS}</script>
</body></html>
"""

    (BUILD_HTML / "glossary.html").write_text(html)
    print(f"[glossary] HTML → build/html/glossary.html ({len(terms)} terms)")

    # Markdown for PDF
    md_lines = [
        "---",
        "title: IDM Course — Glossary",
        "subtitle: 134 terms · Wikipedia + spec cross-refs",
        "date: 2026-04-21",
        "geometry: margin=0.7in",
        "fontfamily: mathpazo",
        "linestretch: 1.3",
        "linkcolor: RoyalBlue",
        "documentclass: extarticle",
        "fontsize: 11pt",
        "---",
        "",
    ]
    for cat in CATEGORY_ORDER:
        if cat not in by_cat:
            continue
        md_lines.append(f"\n## {CATEGORY_LABELS.get(cat, cat)}\n")
        for slug, entry in by_cat[cat]:
            md_lines.append(render_term_md(slug, entry))

    md = "\n".join(md_lines)
    BUILD.mkdir(parents=True, exist_ok=True)
    (BUILD / "glossary.md").write_text(md)
    print(f"[glossary] markdown → build/glossary.md ({len(md)} chars)")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())

#!/usr/bin/env python3
"""
render_slides.py — compile each lesson to a self-contained HTML deck.

v2 changes:
  - Moved audio OUT of per-slide rendering. Single persistent podcast player
    at top of deck plays the full episode MP3, with chapter markers + a
    "jump to this slide's chapter" button available on every slide.
  - Per-slide narration players removed (slides are visual-only).
  - New slide fields supported: images[], diagrams[], gear_annotations[],
    song_refs[] (unchanged), kind: gear_deep_dive.
  - Mermaid.js inlined (no CDN dependency) for offline viewing.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.parse
from html import escape
from pathlib import Path

try:
    import yaml, markdown  # noqa
except ImportError as e:
    sys.exit(f"missing dep: {e}. pip install pyyaml markdown")

ROOT = Path(__file__).resolve().parent.parent
LESSONS = ROOT / "lessons"
BUILD = ROOT / "build" / "html"
NARR = ROOT / "build" / "audio" / "narration"
EPISODES = ROOT / "build" / "audio" / "episodes"
SF = ROOT / "build" / "audio" / "stemforge-renders"
REFS = ROOT / "references"


def load_json(p: Path) -> dict:
    return json.loads(p.read_text()) if p.exists() else {}


def render_markdown(text: str) -> str:
    md = markdown.Markdown(extensions=["extra", "smarty", "attr_list", "fenced_code"])
    return md.convert(text) if text.strip() else ""


# --- CSS ---
CSS = """
:root {
  --bg: #f4f0e8;
  --ink: #111;
  --dim: #5a5047;
  --line: #2a2520;
  --accent: #8b1a1a;
  --pill-bg: #e8e0d2;
  --pill-hover: #d8cdb8;
  --deep-dive-bg: #ede3cf;
  --mono: "JetBrains Mono", "Berkeley Mono", ui-monospace, Menlo, Consolas, monospace;
  --serif: "Charter", "Iowan Old Style", "Georgia", serif;
  --sans: "Inter", system-ui, -apple-system, "Helvetica Neue", sans-serif;
}
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; background: var(--bg); color: var(--ink); }
body { font-family: var(--serif); font-size: 18px; line-height: 1.55; padding-top: 96px; }
a { color: var(--accent); text-decoration: underline; text-underline-offset: 3px; text-decoration-thickness: 1px; }
a:hover { background: var(--ink); color: var(--bg); text-decoration: none; }
code { font-family: var(--mono); font-size: 0.92em; background: rgba(0,0,0,0.05); padding: 1px 4px; border-radius: 2px; }
pre { font-family: var(--mono); background: rgba(0,0,0,0.06); padding: 12px 16px; border-left: 2px solid var(--ink); overflow-x: auto; font-size: 14px; }
blockquote { margin: 0; padding: 0 1em; border-left: 2px solid var(--ink); color: var(--dim); font-style: italic; }
hr { border: 0; border-top: 1px solid var(--line); margin: 2rem 0; }

/* Podcast bar (sticky top) */
.podcast-bar {
  position: fixed; top: 0; left: 0; right: 0; z-index: 50;
  background: var(--bg); border-bottom: 2px solid var(--ink);
  padding: 10px 24px;
  display: flex; align-items: center; gap: 16px;
  font-family: var(--sans); font-size: 13px;
}
.podcast-bar .crumb { color: var(--dim); font-size: 12px; letter-spacing: 0.05em; text-transform: uppercase; }
.podcast-bar .crumb a { color: var(--ink); }
.podcast-bar .spacer { flex: 1; }
.podcast-bar audio { height: 34px; flex: 2; min-width: 280px; max-width: 520px; }
.podcast-bar .chapter { font-family: var(--mono); font-size: 11px; color: var(--dim); letter-spacing: 0.05em; white-space: nowrap; }
.podcast-bar button {
  font-family: var(--mono); font-size: 11px; padding: 5px 10px;
  background: var(--pill-bg); border: 1px solid var(--line); cursor: pointer;
  letter-spacing: 0.06em; text-transform: uppercase; color: var(--ink);
}
.podcast-bar button:hover { background: var(--ink); color: var(--bg); }
.podcast-bar .title-chip { font-weight: 500; letter-spacing: 0.02em; }

/* Stage */
.stage { max-width: 860px; margin: 0 auto; padding: 40px 32px 120px; min-height: 70vh; }
.slide { display: none; }
.slide.active { display: block; animation: fade 200ms ease-out; }
@keyframes fade { from { opacity: 0; transform: translateY(4px); } to { opacity: 1; transform: none; } }

/* Typography */
.slide h1 { font-family: var(--sans); font-size: 13px; text-transform: uppercase; letter-spacing: 0.12em; color: var(--dim); margin: 0 0 8px 0; font-weight: 500; }
.slide h2 { font-family: var(--serif); font-size: 38px; line-height: 1.15; font-weight: 400; margin: 0 0 24px 0; letter-spacing: -0.01em; }
.slide.title h2 { font-size: 52px; margin-top: 2rem; }
.slide.title .sub { color: var(--dim); font-style: italic; font-size: 22px; margin-top: 12px; }
.slide .body { font-size: 18px; }
.slide .body ul, .slide .body ol { padding-left: 1.4em; }
.slide .body li { margin: 6px 0; }
.slide .body p { margin: 0 0 14px 0; }
.slide .body img { max-width: 100%; height: auto; margin: 16px 0; border: 1px solid var(--line); }
.slide.exercise h2 { border-left: 3px solid var(--accent); padding-left: 16px; }
.slide.caveat h2 { font-style: italic; color: var(--dim); }
.slide.teaser { background: #e8e0d2; margin: 20px -32px; padding: 28px 32px; border-top: 1px solid var(--line); border-bottom: 1px solid var(--line); }
.slide.teaser h2 { font-size: 28px; }
.slide.gear_deep_dive { background: var(--deep-dive-bg); margin: 20px -32px; padding: 32px; border-left: 4px solid var(--accent); }
.slide.gear_deep_dive h1::before { content: "GEAR DEEP-DIVE · "; color: var(--accent); }
.deliverable { margin-top: 24px; padding: 14px 18px; background: rgba(139,26,26,0.08); border-left: 3px solid var(--accent); font-family: var(--mono); font-size: 14px; }
.deliverable::before { content: "DELIVERABLE — "; color: var(--accent); font-weight: 600; }

/* Images + figures */
.figure { margin: 20px 0; }
.figure img, .figure svg { max-width: 100%; height: auto; border: 1px solid var(--line); background: #fff; display: block; }
.figure figcaption { font-family: var(--sans); font-size: 12px; color: var(--dim); padding: 8px 0; border-bottom: 1px solid var(--line); }
.figure .credit { font-size: 10px; color: var(--dim); font-style: italic; letter-spacing: 0.04em; margin-top: 4px; }

/* Annotated gear */
.annotation { margin: 24px 0; border: 1px solid var(--line); padding: 0; background: #fff; }
.annotation .gear-svg { display: block; width: 100%; height: auto; }
.annotation .callouts { font-family: var(--sans); font-size: 13px; padding: 14px 18px; background: rgba(0,0,0,0.03); border-top: 1px solid var(--line); }
.annotation .callouts ol { margin: 0; padding-left: 1.4em; }

/* Diagrams (Mermaid + SVG) */
.diagram { margin: 20px 0; padding: 20px; background: rgba(0,0,0,0.03); border: 1px solid var(--line); text-align: center; }
.diagram svg { max-width: 100%; height: auto; }
.diagram .caption { font-family: var(--sans); font-size: 12px; color: var(--dim); margin-top: 10px; text-align: left; }

/* A/B audio */
.ab { margin: 20px 0; padding: 14px 16px; background: rgba(0,0,0,0.04); border: 1px solid var(--line); }
.ab .label { font-family: var(--sans); font-size: 12px; text-transform: uppercase; letter-spacing: 0.08em; color: var(--dim); margin-bottom: 8px; }
.ab .controls { display: flex; gap: 8px; margin-bottom: 8px; }
.ab button { font-family: var(--mono); font-size: 12px; padding: 6px 12px; background: var(--pill-bg); border: 1px solid var(--line); cursor: pointer; color: var(--ink); }
.ab button.active { background: var(--ink); color: var(--bg); }
.ab button:hover:not(.active) { background: var(--pill-hover); }
.ab audio { width: 100%; height: 32px; }

/* Song refs */
.song-refs { margin: 24px 0 12px; padding-top: 18px; border-top: 1px dashed var(--line); }
.song-refs .label { font-family: var(--sans); font-size: 11px; text-transform: uppercase; letter-spacing: 0.08em; color: var(--dim); margin-bottom: 10px; }
.song-ref { margin-bottom: 10px; }
.song-ref .title { font-weight: 600; font-style: italic; }
.song-ref .by { color: var(--dim); }
.song-ref .links { display: inline-flex; gap: 6px; margin-left: 10px; }
.song-ref .links a { font-family: var(--mono); font-size: 11px; padding: 3px 8px; background: var(--pill-bg); border: 1px solid var(--line); text-decoration: none; color: var(--ink); text-transform: uppercase; letter-spacing: 0.06em; }
.song-ref .links a:hover { background: var(--ink); color: var(--bg); }
.song-ref .tier-1 { color: var(--dim); font-size: 10px; }

/* Glossary term tooltips */
.term { border-bottom: 1px dotted var(--dim); cursor: help; position: relative; }
.term:hover .gloss { display: block; }
.term .gloss {
  display: none; position: absolute; bottom: 100%; left: 0;
  background: var(--ink); color: var(--bg); padding: 10px 14px; border-radius: 4px;
  font-family: var(--sans); font-size: 13px; font-weight: normal; font-style: normal;
  width: 320px; z-index: 100;
  box-shadow: 0 4px 12px rgba(0,0,0,0.3);
  line-height: 1.4;
}
.term .gloss a { color: #e8e0d2; }

/* Citations */
.cites { margin-top: 36px; padding-top: 20px; border-top: 1px solid var(--line); font-size: 13px; color: var(--dim); font-family: var(--sans); }
.cites .label { text-transform: uppercase; letter-spacing: 0.08em; font-size: 11px; margin-bottom: 8px; }
.cites ol { padding-left: 1.4em; margin: 0; }
.cites li { margin: 4px 0; }
.cites a { color: var(--dim); }

/* Live set download */
.als { margin: 16px 0; padding: 10px 14px; background: rgba(0,0,0,0.04); border-left: 3px solid var(--ink); font-family: var(--mono); font-size: 13px; }
.als::before { content: "LIVE SET — "; color: var(--accent); font-weight: 600; }

/* Footer */
.foot { position: fixed; bottom: 0; left: 0; right: 0; background: var(--bg); border-top: 1px solid var(--line); padding: 10px 32px; display: flex; justify-content: space-between; align-items: center; font-family: var(--sans); font-size: 12px; color: var(--dim); letter-spacing: 0.04em; z-index: 40; }
.foot .nav { display: flex; gap: 16px; align-items: center; }
.foot .dots { display: flex; gap: 4px; flex-wrap: wrap; max-width: 50%; }
.foot .dot { width: 8px; height: 8px; border-radius: 50%; background: var(--line); cursor: pointer; opacity: 0.4; }
.foot .dot.active { opacity: 1; background: var(--ink); }
.foot .dot.dd { background: var(--accent); }
.foot .dot:hover { opacity: 0.8; }
.foot button { font-family: var(--mono); font-size: 11px; padding: 4px 10px; background: var(--pill-bg); border: 1px solid var(--line); cursor: pointer; letter-spacing: 0.06em; }
.foot button:hover { background: var(--ink); color: var(--bg); }
.foot .keys { font-family: var(--mono); font-size: 10px; color: var(--dim); }

/* Index page */
.idx { max-width: 860px; margin: 0 auto; padding: 60px 32px; }
.idx h1 { font-family: var(--serif); font-size: 44px; letter-spacing: -0.01em; font-weight: 400; margin: 0 0 4px; }
.idx .tag { font-family: var(--sans); font-size: 14px; color: var(--dim); text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 40px; }
.idx .week { display: block; padding: 20px 0; border-top: 1px solid var(--line); text-decoration: none; color: var(--ink); }
.idx .week:last-child { border-bottom: 1px solid var(--line); }
.idx .week:hover { background: rgba(0,0,0,0.04); }
.idx .week .wk { font-family: var(--mono); font-size: 13px; color: var(--dim); letter-spacing: 0.06em; }
.idx .week .title { font-size: 22px; margin: 4px 0; }
.idx .week .meta { font-family: var(--sans); font-size: 12px; color: var(--dim); text-transform: uppercase; letter-spacing: 0.06em; }
.idx .aux { margin-top: 60px; padding-top: 20px; border-top: 2px solid var(--ink); }
.idx .aux a { display: inline-block; margin-right: 24px; font-family: var(--sans); font-size: 13px; }
"""

# --- JS ---
JS = r"""
(function() {
  const slides = Array.from(document.querySelectorAll('.slide'));
  const dotsWrap = document.querySelector('.foot .dots');
  const counter = document.querySelector('.foot .counter');
  const chapLabel = document.querySelector('.podcast-bar .chapter');
  const jumpBtn = document.querySelector('#jump-btn');
  const podcast = document.querySelector('#podcast');
  const chapters = window.__CHAPTERS__ || [];
  let idx = 0;

  function chapterForSlide(i) {
    // Slides with a narration script map 1:1 to a chapter in the podcast.
    // If there are more slides (e.g. gear deep-dives) than chapters, match by position modulo.
    if (chapters.length === 0) return null;
    return chapters[Math.min(i, chapters.length - 1)];
  }

  function render() {
    slides.forEach((s, i) => s.classList.toggle('active', i === idx));
    dots.forEach((d, i) => d.classList.toggle('active', i === idx));
    counter.textContent = `${idx + 1} / ${slides.length}`;
    const ch = chapterForSlide(idx);
    chapLabel.textContent = ch ? `ch ${idx + 1}: ${ch.title}` : '';
    history.replaceState(null, '', `#s${idx + 1}`);
  }

  function next() { if (idx < slides.length - 1) { idx++; render(); } }
  function prev() { if (idx > 0) { idx--; render(); } }
  function jump(i) { if (i >= 0 && i < slides.length) { idx = i; render(); } }

  function jumpPodcastToSlide() {
    const ch = chapterForSlide(idx);
    if (ch && podcast) {
      podcast.currentTime = ch.start_ms / 1000;
      podcast.play().catch(()=>{});
    }
  }

  // Dots with visual distinction for deep-dive slides
  const dots = [];
  slides.forEach((s, i) => {
    const d = document.createElement('div');
    d.className = 'dot';
    if (s.classList.contains('gear_deep_dive')) d.classList.add('dd');
    d.title = `Slide ${i + 1}`;
    d.onclick = () => jump(i);
    dotsWrap.appendChild(d);
    dots.push(d);
  });

  // Keyboard
  document.addEventListener('keydown', e => {
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
    if (e.key === 'ArrowRight' || e.key === 'j' || e.key === 'PageDown') { e.preventDefault(); next(); }
    else if (e.key === 'ArrowLeft' || e.key === 'k' || e.key === 'PageUp') { e.preventDefault(); prev(); }
    else if (e.key === 'Home') { e.preventDefault(); jump(0); }
    else if (e.key === 'End') { e.preventDefault(); jump(slides.length - 1); }
    else if (e.key === ' ' || e.key === 'p') {
      e.preventDefault();
      if (podcast) { podcast.paused ? podcast.play().catch(()=>{}) : podcast.pause(); }
    }
    else if (e.key === 'c') { e.preventDefault(); jumpPodcastToSlide(); }
    else if (e.key === 'm') { if (podcast) podcast.muted = !podcast.muted; }
  });

  if (jumpBtn) jumpBtn.addEventListener('click', jumpPodcastToSlide);

  // A/B players
  document.querySelectorAll('.ab').forEach(ab => {
    const buttons = ab.querySelectorAll('button[data-src]');
    const audio = ab.querySelector('audio.abplayer');
    buttons.forEach(btn => {
      btn.addEventListener('click', () => {
        buttons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        audio.src = btn.dataset.src;
        audio.play().catch(()=>{});
      });
    });
  });

  // Initial hash restore
  const m = location.hash.match(/^#s(\d+)$/);
  if (m) idx = Math.max(0, Math.min(slides.length - 1, parseInt(m[1], 10) - 1));
  render();
})();
"""


def href_song(song_id: str, songs: dict) -> str:
    e = songs.get(song_id)
    if not e:
        return ""
    tier = e.get("link_tier", 1)
    tier_label = f'<span class="tier-1">search</span>' if tier == 1 else ""
    links = []
    if e.get("spotify_url"):
        links.append(f'<a href="{escape(e["spotify_url"])}" target="_blank" rel="noopener">Spotify</a>')
    if e.get("youtube_url"):
        links.append(f'<a href="{escape(e["youtube_url"])}" target="_blank" rel="noopener">YouTube</a>')
    if e.get("apple_music_url"):
        links.append(f'<a href="{escape(e["apple_music_url"])}" target="_blank" rel="noopener">Apple</a>')
    return (
        f'<div class="song-ref">'
        f'<span class="title">{escape(e["title"])}</span>'
        f'<span class="by"> — {escape(e["artist"])}</span>'
        f'<span class="links">{"".join(links)} {tier_label}</span>'
        f'</div>'
    )


def href_citation(bib_id: str, bibliography: dict) -> str:
    e = bibliography.get(bib_id)
    if not e:
        return f'<li><code>{escape(bib_id)}</code> <em>(unresolved)</em></li>'
    title = e.get("title", bib_id)
    authors = ", ".join(e.get("authors") or [])
    pub = e.get("publisher", "")
    year = e.get("year", "")
    url = e.get("url")
    bits = [escape(title)]
    if authors:
        bits.insert(0, escape(authors))
    if pub or year:
        bits.append(f"{escape(pub)} {year}".strip())
    text = " — ".join(bits)
    if url:
        text += f' <a href="{escape(url)}" target="_blank" rel="noopener">↗</a>'
    return f'<li id="{escape(bib_id)}">{text}</li>'


def resolve_audio_src(raw: str | None, lesson_id: str) -> str:
    if not raw:
        return ""
    if raw.startswith("stemforge:"):
        _, week, recipe, label = raw.split(":", 3)
        return f"stemforge/{label}.wav"
    if raw.startswith("build/audio/stemforge-renders/"):
        return f"stemforge/{Path(raw).name}"
    if raw.startswith("build/audio/narration/"):
        return f"audio/{Path(raw).name}"
    return raw


def render_image(img: dict, lesson_dir: Path) -> str:
    src = img.get("src", "")
    caption = img.get("caption", "")
    credit = img.get("credit", "")
    license_note = img.get("license", "")
    # Rewrite relative lesson paths to deck-relative
    if src.startswith("assets/"):
        src = f"assets/{Path(src).name}"
    cred_html = ""
    if credit or license_note:
        parts = [p for p in [credit, license_note] if p]
        cred_html = f'<div class="credit">{escape(" · ".join(parts))}</div>'
    return (
        f'<figure class="figure">'
        f'<img src="{escape(src)}" alt="{escape(caption)}">'
        f'<figcaption>{escape(caption)}{cred_html}</figcaption>'
        f'</figure>'
    )


def render_diagram(diag: dict, lesson_dir: Path) -> str:
    src = diag.get("src", "")
    inline_svg = diag.get("svg_content", "")
    mermaid = diag.get("mermaid", "")
    caption = diag.get("caption", "")
    body = ""
    if mermaid:
        body = f'<div class="mermaid">{escape(mermaid)}</div>'
    elif inline_svg:
        body = inline_svg
    elif src:
        if src.startswith("assets/"):
            src = f"assets/{Path(src).name}"
        body = f'<img src="{escape(src)}" alt="{escape(caption)}">'
    cap_html = f'<div class="caption">{escape(caption)}</div>' if caption else ""
    return f'<div class="diagram">{body}{cap_html}</div>'


def render_gear_annotation(ann: dict, lesson_dir: Path) -> str:
    svg = ann.get("svg_content", "")
    src = ann.get("src", "")
    caption = ann.get("caption", "")
    callouts = ann.get("callouts", [])
    body = ""
    if svg:
        body = f'<div class="gear-svg">{svg}</div>'
    elif src:
        if src.startswith("assets/"):
            src = f"assets/{Path(src).name}"
        body = f'<img class="gear-svg" src="{escape(src)}" alt="{escape(caption)}">'
    callouts_html = ""
    if callouts:
        lis = "".join(f"<li><strong>{escape(c.get('label',''))}</strong>: {escape(c.get('note',''))}</li>" for c in callouts)
        callouts_html = f'<div class="callouts"><ol>{lis}</ol></div>'
    return f'<div class="annotation">{body}{callouts_html}</div>'


def expand_terms(html: str, glossary: dict) -> str:
    """Replace <term key='...'>text</term> markers with tooltip-wrapped spans."""
    def repl(m):
        key = m.group(1)
        inner = m.group(2)
        entry = glossary.get(key)
        if not entry:
            return inner
        definition = escape(entry.get("definition", ""))
        wiki = entry.get("wikipedia_url")
        gloss_html = f'<strong>{escape(entry.get("term", key))}</strong> — {definition}'
        if wiki:
            gloss_html += f' <a href="{escape(wiki)}" target="_blank" rel="noopener">wikipedia↗</a>'
        return f'<span class="term">{inner}<span class="gloss">{gloss_html}</span></span>'
    return re.sub(r'<term key="([^"]+)">([^<]+)</term>', repl, html)


def render_slide(slide: dict, lesson_dir: Path, lesson_id: str, songs: dict, bib: dict, glossary: dict) -> str:
    kind = slide.get("kind", "concept")
    sid = slide["id"]
    heading = escape(slide.get("heading", ""))
    subheading = slide.get("subheading", "")

    body_html = ""
    if slide.get("body_md"):
        p = lesson_dir / slide["body_md"]
        if p.exists():
            body_html = render_markdown(p.read_text())
            body_html = expand_terms(body_html, glossary)

    imgs_html = "".join(render_image(i, lesson_dir) for i in (slide.get("images") or []))
    diagrams_html = "".join(render_diagram(d, lesson_dir) for d in (slide.get("diagrams") or []))
    anns_html = "".join(render_gear_annotation(a, lesson_dir) for a in (slide.get("gear_annotations") or []))

    ab_html = ""
    for ex in slide.get("audio_examples") or []:
        if ex.get("type") == "ab":
            label = escape(ex.get("label", ""))
            a_src = resolve_audio_src(ex.get("a"), lesson_id)
            b_src = resolve_audio_src(ex.get("b"), lesson_id)
            ab_html += (
                f'<div class="ab"><div class="label">{label}</div>'
                f'<div class="controls">'
                f'<button data-src="{escape(a_src)}" class="active">A — dry</button>'
                f'<button data-src="{escape(b_src)}">B — wet</button>'
                f'</div>'
                f'<audio class="abplayer" preload="none" controls src="{escape(a_src)}"></audio>'
                f'</div>'
            )

    als_html = ""
    if slide.get("live_set"):
        rel = slide["live_set"]
        als_html = f'<div class="als"><a href="../../../lessons/{lesson_id}/{escape(rel)}">{escape(Path(rel).name)}</a></div>'

    deliv_html = ""
    if slide.get("deliverable"):
        deliv_html = f'<div class="deliverable">{escape(slide["deliverable"])}</div>'

    song_html = ""
    song_refs = slide.get("song_refs") or []
    if song_refs:
        pills = "".join(href_song(sid2, songs) for sid2 in song_refs)
        song_html = f'<div class="song-refs"><div class="label">♪ tracks</div>{pills}</div>'

    sub_html = f'<div class="sub">{escape(subheading)}</div>' if subheading else ""

    kind_label = kind.replace("_", " ")

    return f"""
<section class="slide {kind}" id="slide-{sid}">
  <h1>Slide {sid} · {escape(kind_label)}</h1>
  <h2>{heading}</h2>
  {sub_html}
  <div class="body">{body_html}</div>
  {imgs_html}
  {diagrams_html}
  {anns_html}
  {ab_html}
  {als_html}
  {deliv_html}
  {song_html}
</section>
"""


def render_lesson_html(lesson_id: str, lesson: dict, songs: dict, bib: dict, glossary: dict, lesson_dir: Path, chapters: list) -> str:
    slides_html = "\n".join(render_slide(s, lesson_dir, lesson_id, songs, bib, glossary) for s in lesson.get("slides", []))

    all_refs = set(lesson.get("references") or [])
    for s in lesson.get("slides", []):
        for key in ("body_md", "script_md"):
            rel = s.get(key)
            if rel:
                p = lesson_dir / rel
                if p.exists():
                    all_refs.update(re.findall(r"bib:[a-z0-9_]+", p.read_text()))
    cites_html = (
        '<div class="cites"><div class="label">References</div><ol>'
        + "".join(href_citation(b, bib) for b in sorted(all_refs))
        + "</ol></div>"
    ) if all_refs else ""

    title = escape(lesson.get("title", lesson_id))
    week = lesson.get("week", "?")
    duration = lesson.get("duration_minutes", "?")
    chapters_js = json.dumps(chapters)

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>IDM — W{week} — {title}</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>{CSS}</style>
</head>
<body>

<!-- Persistent podcast bar -->
<div class="podcast-bar">
  <span class="crumb"><a href="../index.html">IDM</a> / W{week}</span>
  <span class="title-chip">{title}</span>
  <span class="spacer"></span>
  <audio id="podcast" preload="metadata" controls src="episode.mp3"></audio>
  <span class="chapter"></span>
  <button id="jump-btn" title="Jump podcast audio to this slide's chapter">⤓ chapter</button>
</div>

<div class="stage">
  {slides_html}
  {cites_html}
</div>

<div class="foot">
  <div class="nav">
    <span class="counter">1 / 1</span>
  </div>
  <div class="dots"></div>
  <div class="keys">← → nav · space play/pause · c jump-to-chapter · m mute · p play</div>
</div>

<script>window.__CHAPTERS__ = {chapters_js};</script>
<script>{JS}</script>
</body>
</html>
"""


def render_index_html(lessons: list[tuple[str, dict]]) -> str:
    rows = []
    for lid, l in lessons:
        teasers = ", ".join(l.get("teasers") or []) or "—"
        rows.append(f"""
  <a class="week" href="{lid}/index.html">
    <div class="wk">Week {l.get('week','?')}</div>
    <div class="title">{escape(l.get('title', lid))}</div>
    <div class="meta">{l.get('duration_minutes','?')} min · teasers: {escape(teasers)}</div>
  </a>
""")
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>IDM Course — 12 Weeks, 12 Tracks</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>{CSS}</style>
</head>
<body>
<div class="idx">
  <h1>IDM Production</h1>
  <div class="tag">12 weeks · 12 tracks · constraint over options · completion over polish</div>
  {''.join(rows)}
  <div class="aux">
    <a href="glossary.html">Glossary →</a>
    <a href="../../references/bibliography.json">Bibliography</a>
    <a href="../../references/songs.json">Songs registry</a>
  </div>
</div>
</body>
</html>
"""


def ensure_symlink(link: Path, target: Path) -> None:
    if link.is_symlink() or link.exists():
        link.unlink()
    link.parent.mkdir(parents=True, exist_ok=True)
    link.symlink_to(target)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lesson")
    args = ap.parse_args()

    songs = load_json(REFS / "songs.json")
    bib = load_json(REFS / "bibliography.json")
    glossary = load_json(REFS / "glossary.json")

    BUILD.mkdir(parents=True, exist_ok=True)

    lesson_dirs = sorted(LESSONS.iterdir()) if not args.lesson else [LESSONS / args.lesson]
    lesson_dirs = [d for d in lesson_dirs if d.is_dir()]

    for ldir in lesson_dirs:
        y = ldir / "lesson.yaml"
        if not y.exists():
            continue
        lesson = yaml.safe_load(y.read_text())
        lesson_id = ldir.name
        out_dir = BUILD / lesson_id
        out_dir.mkdir(parents=True, exist_ok=True)

        # Symlink episode MP3 + chapter sidecar into deck dir
        mp3_src = EPISODES / f"{lesson_id}.mp3"
        if mp3_src.exists():
            ensure_symlink(out_dir / "episode.mp3", mp3_src)
        # Symlink stemforge stems
        week = f"w{lesson.get('week', 0):02d}"
        sf_src = SF / week
        if sf_src.exists():
            ensure_symlink(out_dir / "stemforge", sf_src)
        # Symlink lesson assets dir (for images/diagrams/etc)
        assets_src = ldir / "assets"
        if assets_src.exists():
            ensure_symlink(out_dir / "assets", assets_src)

        # Load chapters
        chapters = []
        chap_path = EPISODES / f"{lesson_id}.chapters.json"
        if chap_path.exists():
            chapters = json.loads(chap_path.read_text())

        html = render_lesson_html(lesson_id, lesson, songs, bib, glossary, ldir, chapters)
        (out_dir / "index.html").write_text(html)
        print(f"[slides] {lesson_id}: {len(lesson.get('slides', []))} slides → {out_dir}/index.html")

    # Course index
    all_pairs = []
    for ldir in sorted(LESSONS.iterdir()):
        if not ldir.is_dir(): continue
        y = ldir / "lesson.yaml"
        if not y.exists(): continue
        all_pairs.append((ldir.name, yaml.safe_load(y.read_text())))
    all_pairs.sort(key=lambda p: p[1].get("week", 99))
    (BUILD / "index.html").write_text(render_index_html(all_pairs))
    print(f"[slides] index → {BUILD}/index.html ({len(all_pairs)} lessons)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

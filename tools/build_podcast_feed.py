#!/usr/bin/env python3
"""
build_podcast_feed.py — emit podcast.xml (RSS 2.0 + iTunes namespace) for
the 12 course episodes.

Reads:
  - course.yaml (order, titles)
  - lessons/*/lesson.yaml (per-episode metadata)
  - build/audio/episodes/*.chapters.json (for durations)
  - build/audio/episodes/*.mp3 (for file sizes)

Writes:
  - podcast.xml (at repo root — served via GitHub raw URL)

Subscribe from Apple Podcasts iOS:
  Library → "..." top-right → Add a Show by URL → paste:
    https://raw.githubusercontent.com/ZacharySBrown/idm-course/main/podcast.xml
"""
from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from html import escape
from pathlib import Path

try:
    import yaml
except ImportError:
    import sys; sys.exit("pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
LESSONS = ROOT / "lessons"
EPISODES = ROOT / "build" / "audio" / "episodes"
OUT = ROOT / "podcast.xml"

REPO_RAW_BASE = "https://raw.githubusercontent.com/ZacharySBrown/idm-course/main"
REPO_WEB = "https://github.com/ZacharySBrown/idm-course"
ARTWORK_URL = f"{REPO_RAW_BASE}/artwork.jpg"

SHOW_TITLE = "IDM Production — 12 Weeks, 12 Tracks"
SHOW_AUTHOR = "Zak (raindog.ai)"
SHOW_EMAIL = "zak@raindog.ai"
SHOW_DESC = (
    "A twelve-week course reverse-engineering electronic music production "
    "from Aphex Twin, Autechre, Four Tet, Squarepusher, J Dilla, DJ Shadow, "
    "DJ Premier, Kanye, Madlib, Death Grips, and Burial. Narrated by Bernd. "
    "Constraint over options. Completion over polish. Ship twelve tracks in "
    "twelve weeks."
)
SHOW_CATEGORIES = [("Music", None), ("Education", "Courses")]


def rfc822(dt: datetime) -> str:
    return dt.strftime("%a, %d %b %Y %H:%M:%S %z")


def fmt_duration_hms(ms: int) -> str:
    total_sec = ms // 1000
    h = total_sec // 3600
    m = (total_sec % 3600) // 60
    s = total_sec % 60
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


def main() -> int:
    course = yaml.safe_load((ROOT / "course.yaml").read_text())
    weeks = course.get("weeks", [])

    items_xml = []
    # All pub-dates in the past so every episode is visible immediately.
    # W1 was "published" 12 days ago; each subsequent week +1 day. W12 = yesterday.
    now = datetime.now(timezone.utc)
    base_pub = now - timedelta(days=12)

    for w in weeks:
        lesson_id = w["id"]
        week_num = w["week"]
        title = w["title"]

        lesson_yaml = LESSONS / lesson_id / "lesson.yaml"
        lesson = yaml.safe_load(lesson_yaml.read_text()) if lesson_yaml.exists() else {}

        mp3_path = EPISODES / f"{lesson_id}.mp3"
        chap_path = EPISODES / f"{lesson_id}.chapters.json"

        if not mp3_path.exists():
            print(f"[feed] skip {lesson_id} — no mp3", flush=True)
            continue

        size_bytes = mp3_path.stat().st_size
        duration_ms = 0
        if chap_path.exists():
            chapters = json.loads(chap_path.read_text())
            if chapters:
                duration_ms = chapters[-1]["end_ms"]

        # Episode description
        desc_lines = [
            f"Week {week_num} of 12. {title}.",
            "",
            f"Pillars: {', '.join(lesson.get('pillars', []))}.",
        ]
        concepts = lesson.get("concepts", [])
        if concepts:
            desc_lines += ["", "Concepts covered: " + ", ".join(concepts[:8]) + ("..." if len(concepts) > 8 else "")]
        teasers = lesson.get("teasers", [])
        if teasers:
            desc_lines += ["", f"Teasers: {', '.join(teasers)}"]
        desc_lines += ["", f"Deck + references: {REPO_WEB}/blob/main/build/html/{lesson_id}/index.html"]
        description = "\n".join(desc_lines)

        # Stagger pubDates so episodes show in order (one per day from base)
        pub = base_pub + timedelta(days=week_num - 1)

        enclosure_url = f"{REPO_RAW_BASE}/build/audio/episodes/{lesson_id}.mp3"

        item = f"""    <item>
      <title>{escape(f"W{week_num} — {title}")}</title>
      <description>{escape(description)}</description>
      <pubDate>{rfc822(pub)}</pubDate>
      <guid isPermaLink="false">idm-course-{lesson_id}</guid>
      <enclosure url="{escape(enclosure_url)}" length="{size_bytes}" type="audio/mpeg" />
      <itunes:author>{escape(SHOW_AUTHOR)}</itunes:author>
      <itunes:duration>{fmt_duration_hms(duration_ms)}</itunes:duration>
      <itunes:episode>{week_num}</itunes:episode>
      <itunes:season>1</itunes:season>
      <itunes:episodeType>full</itunes:episodeType>
      <itunes:explicit>false</itunes:explicit>
      <itunes:summary>{escape(title)}</itunes:summary>
    </item>"""
        items_xml.append(item)

    cat_xml_parts = []
    for cat, sub in SHOW_CATEGORIES:
        if sub:
            cat_xml_parts.append(f'    <itunes:category text="{escape(cat)}"><itunes:category text="{escape(sub)}" /></itunes:category>')
        else:
            cat_xml_parts.append(f'    <itunes:category text="{escape(cat)}" />')
    cat_xml = "\n".join(cat_xml_parts)

    now = datetime.now(timezone.utc)

    feed = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"
     xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd"
     xmlns:content="http://purl.org/rss/1.0/modules/content/"
     xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <atom:link href="{REPO_RAW_BASE}/podcast.xml" rel="self" type="application/rss+xml" />
    <title>{escape(SHOW_TITLE)}</title>
    <link>{REPO_WEB}</link>
    <description>{escape(SHOW_DESC)}</description>
    <language>en-us</language>
    <copyright>© 2026 Zak. Course content CC-BY-NC 4.0.</copyright>
    <lastBuildDate>{rfc822(now)}</lastBuildDate>
    <pubDate>{rfc822(base_pub)}</pubDate>
    <image>
      <url>{ARTWORK_URL}</url>
      <title>{escape(SHOW_TITLE)}</title>
      <link>{REPO_WEB}</link>
    </image>
    <itunes:image href="{ARTWORK_URL}" />
    <itunes:author>{escape(SHOW_AUTHOR)}</itunes:author>
    <itunes:summary>{escape(SHOW_DESC)}</itunes:summary>
    <itunes:owner>
      <itunes:name>{escape(SHOW_AUTHOR)}</itunes:name>
      <itunes:email>{escape(SHOW_EMAIL)}</itunes:email>
    </itunes:owner>
{cat_xml}
    <itunes:explicit>false</itunes:explicit>
    <itunes:type>serial</itunes:type>
{chr(10).join(items_xml)}
  </channel>
</rss>
"""

    OUT.write_text(feed)
    print(f"[feed] {len(items_xml)} episodes → {OUT}")
    print(f"[feed] subscribe at: {REPO_RAW_BASE}/podcast.xml")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())

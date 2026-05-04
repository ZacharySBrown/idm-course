#!/usr/bin/env python3
"""
build_podcast_feed.py — emit a podcast RSS feed for a course.

Reads (relative to course_root):
  - course.yaml (order, titles, podcast metadata block)
  - lessons/*/lesson.yaml (per-episode metadata)
  - <repo_root>/<enclosure_path>/*.chapters.json (for durations)
  - <repo_root>/<enclosure_path>/*.mp3 (for file sizes)

Writes:
  - <repo_root>/<podcast.feed_path> (load-bearing — published URL)

Usage:
  python shared/tools/build_podcast_feed.py --course-root courses/idm-12x12

Subscribe (IDM):
  https://raw.githubusercontent.com/ZacharySBrown/idm-course/main/podcast.xml
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timedelta, timezone
from html import escape
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("pip install pyyaml")

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _course_lib import load_course, lessons_dir  # noqa: E402


def rfc822(dt: datetime) -> str:
    return dt.strftime("%a, %d %b %Y %H:%M:%S %z")


def fmt_duration_hms(ms: int) -> str:
    total_sec = ms // 1000
    h = total_sec // 3600
    m = (total_sec % 3600) // 60
    s = total_sec % 60
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--course-root", required=True)
    args = ap.parse_args()

    cfg = load_course(args.course_root)
    podcast = cfg.get("podcast") or {}
    if not podcast:
        sys.exit("course.yaml has no `podcast:` block — cannot build feed")

    repo_root = cfg["_repo_root"]
    repo_raw_base = podcast["repo_raw_base"].rstrip("/")
    repo_web = podcast["repo_web"].rstrip("/")
    artwork_url = f"{repo_raw_base}/{podcast.get('artwork_path', 'artwork.jpg')}"
    show_title = cfg.get("title", "Course")
    show_author = podcast["show_author"]
    show_email = podcast["show_email"]
    show_desc = podcast["show_description"].strip()
    show_categories = [tuple(c) for c in podcast.get("itunes_categories", [])]
    copyright_str = podcast.get("copyright", "")
    itunes_type = podcast.get("itunes_type", "serial")
    enclosure_tpl = podcast.get(
        "enclosure_path_template", "build/audio/episodes/{lesson_id}.mp3"
    )
    deck_tpl = podcast.get(
        "deck_url_template", "{repo_web}/blob/main/build/html/{lesson_id}/index.html"
    )
    feed_out = repo_root / podcast.get("feed_path", "podcast.xml")

    weeks = cfg.get("weeks") or cfg.get("episodes") or []
    items_xml = []
    now = datetime.now(timezone.utc)
    base_pub = now - timedelta(days=12)

    for w in weeks:
        lesson_id = w["id"]
        week_num = w.get("week", w.get("episode_number", 1))
        title = w["title"]

        item_yaml = lessons_dir(cfg) / lesson_id / "lesson.yaml"
        item_meta = (
            yaml.safe_load(item_yaml.read_text()) if item_yaml.exists() else {}
        )

        enclosure_rel = enclosure_tpl.format(lesson_id=lesson_id)
        mp3_path = repo_root / enclosure_rel
        chap_path = mp3_path.with_suffix(".chapters.json")

        if not mp3_path.exists():
            print(f"[feed] skip {lesson_id} — no mp3", flush=True)
            continue

        size_bytes = mp3_path.stat().st_size
        duration_ms = 0
        if chap_path.exists():
            chapters = json.loads(chap_path.read_text())
            if chapters:
                duration_ms = chapters[-1]["end_ms"]

        desc_lines = [
            f"Week {week_num} of 12. {title}.",
            "",
            f"Pillars: {', '.join(item_meta.get('pillars', []))}.",
        ]
        concepts = item_meta.get("concepts", [])
        if concepts:
            desc_lines += [
                "",
                "Concepts covered: "
                + ", ".join(concepts[:8])
                + ("..." if len(concepts) > 8 else ""),
            ]
        teasers = item_meta.get("teasers", [])
        if teasers:
            desc_lines += ["", f"Teasers: {', '.join(teasers)}"]
        deck_url = deck_tpl.format(repo_web=repo_web, lesson_id=lesson_id)
        desc_lines += ["", f"Deck + references: {deck_url}"]
        description = "\n".join(desc_lines)

        pub = base_pub + timedelta(days=week_num - 1)
        enclosure_url = f"{repo_raw_base}/{enclosure_rel}"

        item = f"""    <item>
      <title>{escape(f"W{week_num} — {title}")}</title>
      <description>{escape(description)}</description>
      <pubDate>{rfc822(pub)}</pubDate>
      <guid isPermaLink="false">idm-course-{lesson_id}</guid>
      <enclosure url="{escape(enclosure_url)}" length="{size_bytes}" type="audio/mpeg" />
      <itunes:author>{escape(show_author)}</itunes:author>
      <itunes:duration>{fmt_duration_hms(duration_ms)}</itunes:duration>
      <itunes:episode>{week_num}</itunes:episode>
      <itunes:season>1</itunes:season>
      <itunes:episodeType>full</itunes:episodeType>
      <itunes:explicit>false</itunes:explicit>
      <itunes:summary>{escape(title)}</itunes:summary>
    </item>"""
        items_xml.append(item)

    cat_xml_parts = []
    for cat, sub in show_categories:
        if sub:
            cat_xml_parts.append(
                f'    <itunes:category text="{escape(cat)}"><itunes:category text="{escape(sub)}" /></itunes:category>'
            )
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
    <atom:link href="{repo_raw_base}/{podcast.get('feed_path', 'podcast.xml')}" rel="self" type="application/rss+xml" />
    <title>{escape(show_title)}</title>
    <link>{repo_web}</link>
    <description>{escape(show_desc)}</description>
    <language>en-us</language>
    <copyright>{escape(copyright_str)}</copyright>
    <lastBuildDate>{rfc822(now)}</lastBuildDate>
    <pubDate>{rfc822(base_pub)}</pubDate>
    <image>
      <url>{artwork_url}</url>
      <title>{escape(show_title)}</title>
      <link>{repo_web}</link>
    </image>
    <itunes:image href="{artwork_url}" />
    <itunes:author>{escape(show_author)}</itunes:author>
    <itunes:summary>{escape(show_desc)}</itunes:summary>
    <itunes:owner>
      <itunes:name>{escape(show_author)}</itunes:name>
      <itunes:email>{escape(show_email)}</itunes:email>
    </itunes:owner>
{cat_xml}
    <itunes:explicit>false</itunes:explicit>
    <itunes:type>{itunes_type}</itunes:type>
{chr(10).join(items_xml)}
  </channel>
</rss>
"""

    feed_out.write_text(feed)
    print(f"[feed] {len(items_xml)} episodes → {feed_out}")
    print(
        f"[feed] subscribe at: {repo_raw_base}/{podcast.get('feed_path', 'podcast.xml')}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""
songs_upgrade.py — upgrade a song entry in references/songs.json from
Tier 1 (search URL) to Tier 2 (direct track/video ID) or Tier 3 (timestamped
YouTube). Atomic write — safe to run mid-build.

Usage:
    # Upgrade Spotify to direct track link (paste any open.spotify.com/track/... URL):
    python3 tools/songs_upgrade.py song:aphex_xtal \
        --spotify https://open.spotify.com/track/6tHqLXIQ...

    # Upgrade YouTube (any watch / youtu.be / Music URL — script extracts the ID):
    python3 tools/songs_upgrade.py song:aphex_xtal \
        --youtube https://www.youtube.com/watch?v=lLd0iJelm_Y

    # Add a timestamped moment (seconds):
    python3 tools/songs_upgrade.py song:aphex_xtal \
        --youtube https://www.youtube.com/watch?v=lLd0iJelm_Y \
        --moment-sec 12 --moment-note "Repitched 808 kick carries root + fifth"

    # Set ISRC directly:
    python3 tools/songs_upgrade.py song:aphex_xtal --isrc GBFFS9200121

    # Show current entry:
    python3 tools/songs_upgrade.py song:aphex_xtal --show

    # Upgrade link_tier explicitly (auto-set by Spotify or YouTube direct upgrade):
    python3 tools/songs_upgrade.py song:aphex_xtal --tier 2

Flags:
    --spotify URL       any open.spotify.com/track/<id> link
    --youtube URL       any youtube/youtu.be/music URL
    --apple URL         any music.apple.com track URL
    --isrc CODE         12-char ISRC
    --moment-sec N      seconds; pairs with --moment-note
    --moment-note TEXT  one-line description; must be paired with --moment-sec
    --tier {1,2,3}      override link_tier
    --notes TEXT        overwrite the notes field
    --show              print the entry and exit
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SONGS = ROOT / "references" / "songs.json"


def extract_spotify_track_id(url: str) -> str | None:
    m = re.search(r"open\.spotify\.com/(?:intl-\w+/)?track/([A-Za-z0-9]{22})", url)
    return m.group(1) if m else None


def extract_youtube_video_id(url: str) -> str | None:
    patterns = [
        r"youtu\.be/([A-Za-z0-9_-]{11})",
        r"youtube\.com/watch\?v=([A-Za-z0-9_-]{11})",
        r"youtube\.com/embed/([A-Za-z0-9_-]{11})",
        r"youtube\.com/shorts/([A-Za-z0-9_-]{11})",
        r"music\.youtube\.com/watch\?v=([A-Za-z0-9_-]{11})",
    ]
    for p in patterns:
        m = re.search(p, url)
        if m:
            return m.group(1)
    return None


def atomic_write_json(path: Path, data: dict) -> None:
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", dir=str(path.parent),
        prefix=path.name + ".", suffix=".tmp", delete=False,
    ) as tf:
        json.dump(data, tf, indent=2, ensure_ascii=False)
        tmp_name = tf.name
    os.replace(tmp_name, path)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("song_id", help="e.g. song:aphex_xtal")
    ap.add_argument("--spotify")
    ap.add_argument("--youtube")
    ap.add_argument("--apple")
    ap.add_argument("--isrc")
    ap.add_argument("--moment-sec", type=int, dest="moment_sec")
    ap.add_argument("--moment-note", dest="moment_note")
    ap.add_argument("--tier", type=int, choices=[1, 2, 3])
    ap.add_argument("--notes")
    ap.add_argument("--show", action="store_true")
    args = ap.parse_args()

    data = json.loads(SONGS.read_text())
    if args.song_id not in data:
        print(f"unknown song id: {args.song_id}", file=sys.stderr)
        print(f"available: {[k for k in data if k.startswith('song:')][:5]}...", file=sys.stderr)
        return 2
    entry = data[args.song_id]

    if args.show:
        print(json.dumps(entry, indent=2, ensure_ascii=False))
        return 0

    current_tier = entry.get("link_tier", 1)

    if args.spotify:
        sid = extract_spotify_track_id(args.spotify)
        if not sid:
            print(f"could not extract Spotify track id from URL: {args.spotify}", file=sys.stderr)
            return 2
        entry["spotify_track_id"] = sid
        entry["spotify_url"] = f"https://open.spotify.com/track/{sid}"
        current_tier = max(current_tier, 2)
        print(f"spotify: {sid}")

    if args.youtube:
        vid = extract_youtube_video_id(args.youtube)
        if not vid:
            print(f"could not extract YouTube video id from URL: {args.youtube}", file=sys.stderr)
            return 2
        entry["youtube_video_id"] = vid
        entry["youtube_url"] = f"https://youtu.be/{vid}"
        current_tier = max(current_tier, 2)
        print(f"youtube: {vid}")

    if args.moment_sec is not None:
        if not args.moment_note:
            print("--moment-sec requires --moment-note", file=sys.stderr)
            return 2
        vid = entry.get("youtube_video_id")
        if not vid:
            print("cannot set timestamped URL without a youtube_video_id — run with --youtube first", file=sys.stderr)
            return 2
        ts_url = f"https://youtu.be/{vid}?t={args.moment_sec}"
        entry["youtube_timestamped_url"] = ts_url
        moments = entry.get("key_moments") or []
        moments.append({"at_sec": args.moment_sec, "note": args.moment_note, "url": ts_url})
        entry["key_moments"] = moments
        current_tier = max(current_tier, 3)
        print(f"moment @ {args.moment_sec}s: {args.moment_note}")

    if args.apple:
        entry["apple_music_url"] = args.apple
        print("apple: set")

    if args.isrc:
        if not re.fullmatch(r"[A-Z]{2}[A-Z0-9]{3}[0-9]{7}", args.isrc):
            print(f"ISRC format suspicious: {args.isrc} (expected CCXXX0000000)", file=sys.stderr)
        entry["isrc"] = args.isrc
        print(f"isrc: {args.isrc}")

    if args.tier:
        current_tier = args.tier

    if args.notes is not None:
        entry["notes"] = args.notes

    entry["link_tier"] = current_tier
    data[args.song_id] = entry
    atomic_write_json(SONGS, data)
    print(f"\n{args.song_id} now at tier {current_tier}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

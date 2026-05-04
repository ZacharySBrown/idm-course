# raindog-courses

A monorepo of music-production courses sharing a common build pipeline (TTS narration, stemforge stems, podcast feed assembly) and a single voice bible.

## Layout

```
.
├── podcast.xml                 ← load-bearing — IDM podcast feed (Apple Podcasts)
├── artwork.jpg                 ← load-bearing — IDM cover art
├── build/                      ← generated; subscribers read from here
│   ├── audio/episodes/*.mp3    ← IDM episode MP3s (URLs published in podcast.xml)
│   ├── html/<lesson>/          ← IDM rendered decks
│   └── ableton-devices/...     ← Ableton course outputs (separate subtree)
├── courses/
│   ├── idm-12x12/              ← IDM Production — 12 Weeks, 12 Tracks
│   │   ├── course.yaml
│   │   ├── lessons/            ← 12 lessons (source of truth)
│   │   ├── references/         ← bibliography, glossary, songs, images
│   │   ├── specs/              ← source briefs that seeded the course
│   │   ├── stemforge-demo-material/recipes.yaml
│   │   ├── style/              ← per-course extension overlays + teaser-calendar.yaml
│   │   └── tools/              ← IDM-only tools (slides, glossary, art)
│   └── ableton-devices/        ← Ableton Live Mastery (walking podcast)
│       ├── course.yaml
│       ├── episodes/
│       ├── presets/
│       ├── style/              ← per-course extension overlays
│       └── tools/              ← Ableton-only tools (LOM/audio rendering)
└── shared/
    ├── style/                  ← base voice.md + lexicon.md (govern both courses)
    └── tools/                  ← cross-course build pipeline
        ├── _course_lib.py      ← path resolution helper
        ├── render_voiceover.py
        ├── stemforge_runner.py
        ├── build_episode.py
        ├── build_podcast_feed.py
        └── validate.ts
```

Every shared tool takes `--course-root <path>`. Per-course tools live under `courses/<id>/tools/` and also take `--course-root` for consistency.

## Courses

- **[IDM Production — 12 Weeks, 12 Tracks](courses/idm-12x12/)** — reverse-engineering electronic-music production from Aphex Twin, Autechre, Four Tet, Squarepusher, J Dilla, DJ Shadow, DJ Premier, Kanye, Madlib, Death Grips, and Burial. **Status:** shipping (12 episodes published).
- **[Ableton Live Mastery](courses/ableton-devices/)** — device-by-device walking-podcast deep-dives (Operator, Analog, Wavetable, Meld, etc.). **Status:** scaffold only (e01-operator in progress).

## Build pipeline (IDM, full)

```bash
# Wave 4 — Stem renders
python shared/tools/stemforge_runner.py --course-root courses/idm-12x12

# Wave 6 — Voiceover (requires OPENAI_API_KEY)
python shared/tools/render_voiceover.py --course-root courses/idm-12x12

# Wave 7 — Compile
python shared/tools/build_episode.py --course-root courses/idm-12x12
python courses/idm-12x12/tools/render_slides.py --course-root courses/idm-12x12
python courses/idm-12x12/tools/render_glossary.py --course-root courses/idm-12x12

# Wave 8 — Feed
python shared/tools/build_podcast_feed.py --course-root courses/idm-12x12
```

## Validation

```bash
bun run shared/tools/validate.ts --course-root courses/idm-12x12 --all
bun run shared/tools/validate.ts --course-root courses/ableton-devices --all
```

Loads banned phrases from [shared/style/lexicon.md](shared/style/lexicon.md) plus per-course extensions, checks bibliography citations, teaser calendar, exclamation/emoji policy, and script length.

## Voice + lexicon

The base voice bible is at [shared/style/voice.md](shared/style/voice.md). Each course can add overrides in `courses/<id>/style/voice-extension.md` (and `lexicon-extension.md`). The validator unions base + extension at lint time.

## Subscribe to IDM podcast

```
https://raw.githubusercontent.com/ZacharySBrown/idm-course/main/podcast.xml
```

(The repo name stays `idm-course` so this URL keeps resolving.)

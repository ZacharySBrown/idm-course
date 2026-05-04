# courses/idm-12x12/tools/

Build pipeline for the IDM course. Cross-course tools live at [`shared/tools/`](../../../shared/tools/).
All tools take `--course-root courses/idm-12x12`.

## Wave 4 — Stemforge renders

```bash
python shared/tools/stemforge_runner.py --course-root courses/idm-12x12
python shared/tools/stemforge_runner.py --course-root courses/idm-12x12 --week 5
python shared/tools/stemforge_runner.py --course-root courses/idm-12x12 --dry-run
```

Reads `courses/idm-12x12/stemforge-demo-material/recipes.yaml`.
Writes to `build/audio/stemforge-renders/<week>/`.
Requires: `stemforge` CLI on PATH.

## Wave 6 — Voiceover

```bash
python shared/tools/render_voiceover.py --course-root courses/idm-12x12
python shared/tools/render_voiceover.py --course-root courses/idm-12x12 --lesson w05-aphex-tuning
python shared/tools/render_voiceover.py --course-root courses/idm-12x12 --dry-run
```

Reads every `lessons/*/script/*.md`. Writes `build/audio/narration/<lesson>/<slide>.wav`.
Cached by SHA256(content + model + voice). Requires `OPENAI_API_KEY`.

## Wave 7 — Compile

```bash
python shared/tools/build_episode.py --course-root courses/idm-12x12
python shared/tools/build_episode.py --course-root courses/idm-12x12 --lesson w05-aphex-tuning
```

```bash
python courses/idm-12x12/tools/render_slides.py --course-root courses/idm-12x12
python courses/idm-12x12/tools/render_slides.py --course-root courses/idm-12x12 --lesson w05-aphex-tuning
```

```bash
python courses/idm-12x12/tools/render_glossary.py --course-root courses/idm-12x12
python courses/idm-12x12/tools/glossary_to_pdf.py --course-root courses/idm-12x12
```

## Wave 8 — Feed

```bash
python shared/tools/build_podcast_feed.py --course-root courses/idm-12x12
```

Writes `podcast.xml` at the repo root (the load-bearing published feed).

## Linting

```bash
bun run shared/tools/validate.ts --course-root courses/idm-12x12 --all
bun run shared/tools/validate.ts --course-root courses/idm-12x12 --week 5
bun run shared/tools/validate.ts --course-root courses/idm-12x12 --style
```

## PDF acquisition

```bash
bash courses/idm-12x12/tools/fetch_pdfs.sh   # COURSE_ROOT auto-resolves; override via env
```

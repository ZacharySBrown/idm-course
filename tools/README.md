# tools/

Build pipeline for the IDM course. Run order (Waves 4–8 from the plan):

## Wave 4 — Stemforge renders

```bash
python tools/stemforge_runner.py            # all recipes
python tools/stemforge_runner.py --week 5   # just W5
python tools/stemforge_runner.py --dry-run  # preview commands
```

Reads `stemforge-demo-material/recipes.yaml`.
Writes to `build/audio/stemforge-renders/<week>/`.
Requires: `stemforge` CLI on PATH.

## Wave 5 — Assets

TODO: `tools/spectrogram_gen.py`, `tools/waveform_peaks.py`. Straightforward librosa-based scripts; will land after W5 audition confirms visual styling.

## Wave 6 — Voiceover

```bash
python tools/render_voiceover.py                         # all lessons
python tools/render_voiceover.py --lesson w05-aphex-tuning
python tools/render_voiceover.py --model gpt-4o-mini-tts --voice onyx
python tools/render_voiceover.py --dry-run
```

Reads every `lessons/*/script/*.md`.
Writes `build/audio/narration/<lesson>/<slide>.wav`.
Cached by SHA256(content + model + voice) at `build/audio/narration/.cache/`.
Requires: `OPENAI_API_KEY`, `uv pip install openai`.

Default stack: `gpt-4o-mini-tts` with voice `onyx` + character instructions. Falls back to `tts-1-hd` on provider error. Swap to ElevenLabs later with minor edit (the character brief moves from `instructions=` to voice-preset selection).

## Wave 7 — Compile

TODO: `tools/render_slides.ts` (Slidev wrapper), `tools/build_episode.py` (ffmpeg + mutagen CTOC/CHAP).

## Wave 8 — Index + QA

TODO: `tools/build_index.ts` (regenerates course-wide `build/html/index.html`), plus headless-Chrome smoke test.

## Linting

```bash
bun run tools/validate_lesson.ts --week 5
bun run tools/validate_lesson.ts --all
bun run tools/validate_lesson.ts --allow-empty   # Wave 0 scaffold check
```

Fails on: unresolved citations, banned phrases from `style/lexicon.md`, exclamation points, emojis. Warns on: adjective-dense paragraphs, too-short/too-long scripts, missing scheduled teasers.

## PDF acquisition

```bash
bash tools/fetch_pdfs.sh   # Bucket A downloadable sources
```

Writes status to `references/pdfs/_status.json`.
Prints Bucket B purchase TODO to `references/pdfs/_purchase_todo.md`.

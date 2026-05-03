# tools/

Build pipeline for the Ableton Live Mastery podcast course.

## Order of Operations (per episode)

### Phase 1: Research
python tools/fetch_ableton_docs.py --device operator --output episodes/e01-operator/research/ableton-docs.md
python tools/clip_curator.py --scan-library --output episodes/e01-operator/research/library-scan.json
# Then: deep research pass (manual or research agent)

### Phase 2: Audio Demo Rendering
python tools/ableton_render.py --test              # validate LOM first
python tools/ableton_render.py --episode e01-operator

### Phase 3: Voiceover
python tools/render_voiceover.py --episode e01-operator
# --model gpt-4o-mini-tts --voice onyx (defaults)

### Phase 4: Assemble
python tools/build_episode.py --episode e01-operator
python tools/build_episode.py --episode e01-operator --dry-run  # preview first

## Validation
bun run tools/validate_episode.ts --episode e01-operator
bun run tools/validate_episode.ts --all

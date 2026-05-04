# courses/ableton-devices/tools/

Course-specific tools for Ableton Live Mastery. Cross-course tools at [`shared/tools/`](../../../shared/tools/).
All tools take `--course-root courses/ableton-devices`.

## Audio demo rendering

### Song clips (shared, ffmpeg-only — no Live required)

```bash
python shared/tools/extract_clips.py --course-root courses/ableton-devices --lesson e01-operator
python shared/tools/extract_clips.py --course-root courses/ableton-devices --lesson e01-operator --clip stria-excerpt-1
python shared/tools/extract_clips.py --course-root courses/ableton-devices --lesson e01-operator --dry-run
```

### Operator patch demos (Live + Max for Live required)

See [`operator_render/README.md`](operator_render/README.md) for the full
pipeline. Quick form:

```bash
python courses/ableton-devices/tools/operator_render/operator_render.py \
    --course-root courses/ableton-devices --episode e01-operator
# → click RENDER in the OperatorRender.amxd M4L device
```

### Legacy (deprecated)

`ableton_render.py` predates the operator_render split — kept temporarily as a
reference for the older IPC pattern. New work goes in `operator_render/`.

## Voiceover (shared tool)

```bash
python shared/tools/render_voiceover.py --course-root courses/ableton-devices
python shared/tools/render_voiceover.py --course-root courses/ableton-devices --lesson e01-operator
python shared/tools/render_voiceover.py --course-root courses/ableton-devices --dry-run
```

## Episode assembly (shared tool)

```bash
python shared/tools/build_episode.py --course-root courses/ableton-devices
python shared/tools/build_episode.py --course-root courses/ableton-devices --lesson e01-operator
```

## Validation (shared tool)

```bash
bun run shared/tools/validate.ts --course-root courses/ableton-devices --all
```

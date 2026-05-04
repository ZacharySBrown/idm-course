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

### Live device demos (Live + Max for Live required)

Generic for every device the course visits. See
[`device_render/README.md`](device_render/README.md). Quick form for ep01:

```bash
python courses/ableton-devices/tools/device_render/device_render.py \
    --course-root courses/ableton-devices --episode e01-operator --device Operator
# → click RENDER in MidiInstrumentRender.amxd
```

Other episodes pass `--device <Class> [--kind audio-fx] [--demos-key <key>]`.

### Legacy (deprecated)

`ableton_render.py` predates the device_render split — kept temporarily as a
reference for the older IPC pattern. New work goes in `device_render/`.

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

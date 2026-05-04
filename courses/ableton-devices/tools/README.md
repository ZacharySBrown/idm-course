# courses/ableton-devices/tools/

Course-specific tools for Ableton Live Mastery. Cross-course tools at [`shared/tools/`](../../../shared/tools/).
All tools take `--course-root courses/ableton-devices`.

## Audio demo rendering (Ableton-specific)

```bash
python courses/ableton-devices/tools/ableton_render.py --test
python courses/ableton-devices/tools/ableton_render.py --episode e01-operator
```

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

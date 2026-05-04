# The three modes side-by-side

A compact decision table. Pin this to the wall.

| Question | Classic | One-Shot | Slicing |
|---|---|---|---|
| Note transposes pitch? | yes | no | no — picks a slice |
| Release obeys note-off? | yes | no (Trigger) | depends on mode |
| Has amp envelope? | yes | no — fade in/out only | no |
| Has filter + LFO? | yes | no | no |
| Warp engine runs? | yes | optional, usually off | N/A (warp is baked in slice marker positions) |
| Typical job | <term key="chromatic_chopping">chromatic vocal chop</term>, pitched sources | kicks, snares, hats, FX | drum break reorder, glitch construction |

Two failure modes worth naming:

- Loading a kick in Classic and playing from C3 — kick is pitched up an octave, sounds wrong, you blame the sample.
- Loading a melodic vocal in One-Shot — no keyboard tracking, no envelope shaping, you can't play it chromatically.

Mode is a choice, not a default. Read the tab before you load.

[ref: bib:ableton_live_12_manual]

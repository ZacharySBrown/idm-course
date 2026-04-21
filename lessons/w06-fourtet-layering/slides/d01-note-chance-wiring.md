## Diagram — Note Chance + Pitch Transformer wiring

The "Looking At Your Pager" 15% / 15% randomization, laid out as a signal diagram.

```
MIDI clip ──► [Velocity Range ±15%] ──► note-on velocity randomized on each trigger
         │
         └──► duplicate notes +12 semitones, stacked at same beat position
                     │
                     └──► [Chance 15%] ──► 15% probability the duplicate plays
                                     │
                                     └──► if duplicate fires, original is masked via Chance 85%
```

- <term key="note_chance">Note Chance</term> is a per-note probability field in Live 12's clip editor. 0–100%.
- **Velocity Range** is the secondary handle on each note. Scales the triggered velocity randomly within the band.
- The **Pitch Transformer** is an alternative path — use *Clip → Transform → Pitch* with a probability setting, then **Bake** to lock the result into actual notes.

Prefer the duplicated-layer route. It survives bounces. `Ableton Live 12 Reference Manual`.

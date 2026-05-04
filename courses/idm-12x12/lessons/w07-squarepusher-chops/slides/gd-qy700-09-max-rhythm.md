# Parallel Max for Live — Rhythm and Seed

Ableton ships two native MIDI generators that approximate the QY700's deterministic-but-hand-drawn character when chained:

- **Rhythm.** Pattern-generating MIDI device. Seed-based, probability per step, density control. Swap the seed — swap the pattern. Deterministic given a seed, which is the replacement for blind-numeric entry. <Citation bib="ableton_live_12_manual" />
- **Seed.** Companion device for randomizing pitch/velocity within a constrained palette. Drives Rhythm's seed input.
- **Velocity Shaper.** Per-step velocity curves drawn as a ramp or freehand — literally the QY700 velocity editor reimplemented as a MIDI effect.

The chain for a QY700-style track:

```
Rhythm (seed=N) → Velocity Shaper (hand-drawn curve) → MIDI track → Instrument
```

Swap `seed=N` to mutate the pattern while keeping the velocity contour. This is the Ableton analogue of Jenkinson editing one pattern on the QY700 chain and letting every reference update.

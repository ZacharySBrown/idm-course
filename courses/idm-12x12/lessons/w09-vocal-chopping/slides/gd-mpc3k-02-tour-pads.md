# Annotated tour, 1/2 — pads, swing, note repeat

The four controls that matter for <term key="dilla_time">Dilla time</term>:

1. **16 velocity-sensitive pads** — grouped in banks A–D. Each pad is one voice with its own sample, envelope, tuning, and — critical — its own timing parameters.
2. **Swing %** — 50% is straight, 62–66% is triplet-heavy. On the MPC3000 this is set **per pad**, not globally (`bib:akai_mpc3000_manual`). That is the whole game.
3. **Note Repeat** — hold a pad, tap Note Repeat, and the pad fires at the current subdivision. This is how hand-stepped hi-hat rolls happen without a piano roll.
4. **Timing Correct %** — quantize strength, 0 to 100. Dilla set this to 0 on most pads and nudged by ear. On *Fantastic Vol. 2* the snare is ~20 ms early, the hats are freehand, the kicks are ±20–30 ms off (`bib:charnas_dilla_time`).

The 96 PPQN grid is the resolution underneath everything. One 16th note = 24 ticks. One millisecond at 90 BPM ≈ 0.14 ticks. When you nudge by a "tick," you are nudging by ~7 ms.

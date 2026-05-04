# Underlying algorithm — per-pad timing on a 96 PPQN grid

The MPC3000 sequencer runs at **96 pulses per quarter note (PPQN)**. One 16th = 24 ticks. Timing shift per pad is expressed in ticks, stored as a signed offset in the pattern.

At 90 BPM:
- 1 beat = 666.67 ms
- 1 tick = ~6.94 ms
- 1 ms ≈ 0.14 ticks

So the "20 ms early snare" in practice is a **−3-tick offset** on the snare pad, stored in the pattern's per-pad timing-shift field (`bib:akai_mpc3000_manual`). It applies on playback, after any Timing Correct but before the voice is assigned a sample. Swing % applies on the off-subdivisions of the assigned rate — so "hats at 62% swing" shifts every even 16th by roughly 12% of a 16th, ~8 ticks, ~55 ms at 90 BPM.

Crucially: Swing and Timing Shift are **independent per pad**. Kicks at swing 50% + shift −3 ticks, hats at swing 64% + shift 0, snare at swing 50% + shift −3 ticks — all in the same pattern. The SP-1200 has one global swing parameter. That is the architectural delta.

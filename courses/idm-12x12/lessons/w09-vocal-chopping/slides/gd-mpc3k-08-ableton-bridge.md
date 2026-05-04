# Ableton bridge — Drum Rack + per-pad Groove Pool

The Ableton analogue is not one device. It is a discipline:

1. **Drum Rack** — 16-pad grid. Each pad is a chain. Each chain gets its own Simpler in **Classic** mode (pitch/time coupled) to preserve varispeed character (`bib:ableton_live_12_manual`).
2. **Groove Pool, per pad** — drag a different groove file onto each chain. Swing timing applies only to that chain's output. Ableton's Groove Pool is the closest native analogue to MPC3000 per-pad swing.
3. **Per-pad note nudge in the MIDI editor** — select a pad's notes, shift-arrow nudges by the project grid. For sub-grid nudges, turn off snap and drag.
4. **Warp mode = Re-Pitch** on audio triggers — if you're triggering samples from audio clips instead of Simpler, Re-Pitch preserves the varispeed coupling. Complex Pro breaks it.

Parameter table for the approximation:

| MPC3000 | Ableton equivalent |
| --- | --- |
| Per-pad swing % | Groove file dragged onto chain |
| Per-pad timing shift (ticks) | MIDI nudge, snap off |
| Varispeed pitch | Simpler Classic mode / Warp Re-Pitch |
| 2-pole LPF per voice | Simpler filter, LPF 12 dB |
| 18-bit DAC character | Leave headroom; light analog-summing emulation optional |

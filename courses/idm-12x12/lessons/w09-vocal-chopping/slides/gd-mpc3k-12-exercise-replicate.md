# Exercise A — replicate Dilla swing, snare-only

Goal: a 4-bar boom-bap pattern where the snare lags the grid by ~50 ms and the kicks stay straight. This is the signature *Fantastic Vol. 2* move, reduced to its smallest verifiable case.

Steps:

1. New Drum Rack. Load a kick sample on C1, a snare on D1, a closed hat on F#1.
2. Program a basic 4-bar pattern: kicks on 1 and 3, snares on 2 and 4, hats on every 16th.
3. Bounce this as the **quantized baseline**. Label `hp_baseline.wav`.
4. Create a new groove file: **Swing = 0%, Timing = +25%** (at 90 BPM, +25% of a 16th ≈ +50 ms). Drag only onto the snare chain.
5. Leave the kick and hat chains with no groove.
6. Bounce as `hp_dillaswing.wav`.
7. A/B the two bounces.

Deliverable: two mono bounces, plus one sentence explaining which one sounds "alive" and why. The 50-ms snare drag is the smallest deliberate-sloppiness move that still reads as Dilla (`bib:charnas_dilla_time`).

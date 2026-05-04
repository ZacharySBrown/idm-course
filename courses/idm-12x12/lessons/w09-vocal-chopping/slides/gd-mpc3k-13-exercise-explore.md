# Exercise B — per-pad drift everywhere

Goal: a pattern where *every* hit has a unique per-pad timing offset. Prove to yourself that random offsets sound like noise and deliberate ones sound like a record.

Steps:

1. Program a 1-bar pattern with 4 kicks, 2 snares, 8 hats on a Drum Rack.
2. On the kick chain, set MIDI offsets: kick 1 at 0 ms, kick 2 at +5 ms, kick 3 at −3 ms, kick 4 at +10 ms. These are pad-specific, not groove-based — nudge in the MIDI editor with snap off.
3. On the snare chain: snare 1 at −3 ms (Dilla drag-early), snare 2 at −3 ms.
4. On the hat chain: leave on the grid.
5. Bounce as `hp_drift.wav`.
6. Re-bounce the same pattern with all kicks at 0 ms. Label `hp_nodrift.wav`.
7. A/B.

Reflect (one paragraph): which kick feels most wrong? Which feels most right? The drift is not random — Dilla chose each offset. You are choosing too.

Stretch: try all offsets in the *same direction* (all +5 to +15). Then all random-signed. The same-direction version reads as "late"; the random version reads as "bad." That asymmetry is the hidden rule.

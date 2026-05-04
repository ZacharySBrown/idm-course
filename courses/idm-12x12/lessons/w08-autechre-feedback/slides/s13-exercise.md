# Exercise — 32 bars, four commits, one bounce

**Deliverable:** a 32-bar bounced audio file of evolving-but-rule-based drums.

Steps:

1. Import the `stemforge:w08-moanin-ambient-feedback` render (`moanin_ambient.wav`). Slice to Drum Rack at 1/16 by transient. This is your kit.
2. New MIDI clip, 8 bars, empty. Apply **Rhythm generator**: Steps 16, Density 55%, Division 1/16. Commit.
3. Apply **Recombine (Shuffle)**. Commit.
4. Apply **Time Warp**: breakpoint curve 1.5x at bar 1 → 0.5x at bar 4 → 1.0x at bar 8. Commit.
5. Apply **Velocity Shaper** (hand-drawn curve). Commit. Apply **Ornament** at Length 1/64, Density 20%. Commit.
6. Loop the 8-bar clip × 4 into a 32-bar arrangement. Unlink a filter clip envelope at 7-bar length.
7. Bus the Drum Rack through **Roar MultiBand** with the settings on slide 9.
8. **Freeze → Flatten.** Export 32 bars.

**Time-box: 45 minutes.** Ship one bounce. Delete the source MIDI. Save the set as `w08_v01.als`.

`bib:ableton_live_12_manual` · `bib:stemforge_repo`

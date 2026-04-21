# Annotated tour, 1/2 — sample rate, pitch, truncate

The controls that matter:

1. **Sample rate: fixed at 26.04 kHz.** Not user-adjustable. Nyquist is ~13 kHz. Everything above that folds back as aliasing. Modern recordings at 44.1/48 kHz sound tame by comparison — this is the source of the "dusty" character.
2. **Pitch — semitone + fine tune.** Per-pad <term key="varispeed">varispeed</term>. Raising pitch shortens the sample *and* raises aliasing artifacts; lowering pitch lengthens it and moves the aliasing down into the mids. Pitch-and-time-coupled just like the MPC3000, but at lower bandwidth.
3. **Truncate** — head/tail crop at sample-level resolution. Destructive. The 2.5-second pad limit is a RAM division, not a truncate setting — you *cannot* load a longer sample, period.
4. **The "aliasing switch"** — producers' slang, not an actual button. Refers to routing via the individual outputs rather than the stereo mix, which avoids the master bus DAC's slight low-pass and preserves more high-frequency aliasing. Pete Rock and RZA ran out of the individual outs for exactly this reason.

2.5 seconds per pad is a compositional constraint. You cannot loop a whole phrase. You chop or you don't sample it.

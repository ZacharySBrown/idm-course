# Tape hysteresis — the algorithm nobody codes on purpose

Magnetic tape's input/output function is a <term key="hysteresis_loop">hysteresis loop</term>. At low levels the response is nearly linear; as input rises, the magnetic domains in the tape oxide saturate and the output compresses; when input reverses, the output lags. The shape traces a loop, not a line — the output is a function of both the input *and* the recent history of the input.

Three consequences for audio:

1. **Harmonic addition.** The non-linear transfer function generates second- and third-order harmonics. On bass, this adds perceptible "weight" by doubling the fundamental an octave up.
2. **Soft-knee compression.** At high input levels, the loop flattens — the tape compresses without an explicit threshold.
3. **Low-frequency thickening.** At 15 IPS tape speed, the low-end saturation is heavier; the record label's thump on *The Soft Bulletin* is in part this.

Modern tape plugins (Kramer Tape, U-he Satin, Ableton's Saturator in Soft Sine mode) model this loop. None reproduces it perfectly, because the physical system has thermal noise, tape formulation variance, and head wear that any static model ignores. Close is close enough for the Ableton bridge.

Cite: `bib:roads_computer_music_tutorial`, chapter on non-linear processing.

We just heard the filter perform — the 303's squelch is a hand on the cutoff. Stop two — how it actually works. For a physicist, what is that filter doing to the harmonics? And to answer that, you first have to know what's going *into* the filter. The raw material.

[pause 500ms]

Three waveforms matter, and they're all just sums of sines. A sawtooth has every harmonic — first, second, third, all of them — with amplitude falling off as one-over-n. That's why it's the default subtractive source: it gives the filter the most to work with. A square wave has only the *odd* harmonics, also one-over-n — that missing even content is what makes it sound hollow, woody, clarinet-ish. And a pulse wave is the interesting one, because its harmonic content depends on a single control: the duty cycle.

[pause 500ms]

The pulse is governed by a sinc envelope, which means it has nulls — gaps in the spectrum — at integer multiples of one-over-the-duty-cycle. At fifty percent, those nulls land exactly on the even harmonics, and you're back to a square. Narrow the pulse, the nulls move, and even harmonics fade *in*. So pulse width is a harmonic control hiding as a shape control.

[pause 500ms]

One held note, one rectangular oscillator, filter wide open so it isn't coloring anything, and I'm going to sweep the pulse width from fifty percent down toward narrow. Same pitch, same loudness. Listen to the even harmonics arrive. Listen.

[cue: an-pwm-sweep]

That was pulse-width modulation, by hand. The pitch never moved and the volume never moved — only the spectrum, thinning and nasalizing as the duty cycle narrowed. No filter touched. One note about Analog's palette before we go on: it has four shapes — sine, saw, rectangular, noise. No triangle. If you want a triangle's darkness, you low-pass a square.

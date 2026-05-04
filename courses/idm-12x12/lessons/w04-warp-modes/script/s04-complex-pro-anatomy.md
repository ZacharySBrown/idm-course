Complex Pro. [pause 150ms] Two controls do the heavy lifting. The rest is presentation.

**Formants.** Range zero to one hundred. [pause 200ms] A formant is a resonant bump in the spectrum of a sound — for the human voice, the formants are what make the difference between an "ah" and an "ooh." Same pitch, different formants, different vowel. For an instrument, formants are the resonant body — a violin's box, a piano's soundboard, a kick drum's shell.

When you pitch-shift a sample with most algorithms, the formants shift with it. Pitch a vocal up an octave and the formants go up too, which is why it sounds like a chipmunk — the vowels have moved into frequency ranges no human vocal tract produces. [pause 150ms] Set Complex Pro's Formants control to one hundred and it holds the formants in place while pitch-shifting. Pitch a baritone up a fifth and it still *sounds like a person*, just higher. Set Formants to zero and you get the chipmunk back. Both are useful.

**Envelope.** Values sixteen, thirty-two, sixty-four, one-twenty-eight, two-fifty-six. [pause 150ms] This is the FFT window size, in samples. It is a tradeoff. Small windows give you good time resolution and poor frequency resolution — fast transients survive, but pitched content gets warbly. Large windows reverse that. Transients smear; pitch tracking cleans up.

Defaults that work. [pause 100ms] Envelope *sixty-four* for high-frequency sources — hi-hats, cymbals, shakers, anything with fast transients on the top end. Envelope *one-twenty-eight* is Ableton's default and it is fine for most full mixes. Envelope *two-fifty-six* for low-frequency content — sub bass, 808s, held pedal tones.

Symptoms. If your top end sounds smeary after warping, drop Envelope to sixty-four. If your bass is chattering or phasey, raise it to two-fifty-six. [pause 200ms]

That's Complex Pro. Formants for vowel preservation. Envelope for tradeoff management. Both defaults are knowable. Commit them.

Cite — Live 12 manual, same page.

# Algorithm continued — aliasing and the 13 kHz cliff

26.04 kHz sample rate → <term key="nyquist">Nyquist</term> = 13.02 kHz. Anything in the source above 13 kHz folds back into the audible band as **aliasing**:

- A 16 kHz cymbal component folds to 26.04 − 16 = **10.04 kHz**.
- A 20 kHz source harmonic folds to 26.04 − 20 = **6.04 kHz**. Now you have a mid-range tone that wasn't in the original.
- A properly designed ADC has a **steep brick-wall anti-alias filter** (~20 kHz for 44.1 kHz systems). The SP-1200's filter is **famously permissive** — per the service manual there's a gentle ~1-pole analog roll-off starting around 10 kHz, so it's not absent, just lazy. Plenty of high-frequency content that would have been blocked elsewhere folds back into the audible band and gets printed directly into sample RAM.

Combined with varispeed playback: pitch a pad up an octave and the aliased content shifts *with* the sample, creating non-harmonic content that intermodulates with the source. This is why SP-1200 records sound "musically wrong in a way that works" — they contain frequency content that is not mathematically related to the source spectrum.

The frequency-response cliff is not at 13 kHz — it's at 26.04 − source-highest. That is a moving target dependent on what you sampled. Which is why every SP-1200 record has its own particular grit.

# LUFS explained — what the meter is actually measuring

<term key="lufs">LUFS</term> is not a volume knob. It is a perceptual average computed by <term key="itu_bs1770">ITU-R BS.1770-4</term> — the spec every streaming platform normalizes against.

Three moving parts in the algorithm.

- **K-weighting filter** — a high-shelf and high-pass pre-filter that approximates equal-loudness at moderate listening levels. Low bass and sub-bass count less than the 2–4 kHz presence region. The meter hears the way an ear at 83 dB SPL hears.
- **Gating** — the measurement drops any 400 ms block below −70 LUFS absolute, then re-gates relative to the running mean at −10 LU. Silence and fade-ins do not pull the number down.
- **Integration** — the reading you ship is the **integrated** LUFS, measured across the whole track. Short-term LUFS (3-second window) and momentary LUFS (400 ms) are diagnostic readouts for the loudest section, not the delivery number.

The practical consequence: a track with a quiet intro and a loud drop reads closer to the *drop's* loudness than to the average, because the gate is throwing out the intro below −70 LUFS.

Master to the integrated number. Watch the short-term for chorus-level danger. Ignore the momentary unless you are chasing a limiter spike. <Citation bib="edmprod_intermediate" />

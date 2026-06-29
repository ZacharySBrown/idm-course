That is the grain breaking. The phase vocoder breaks in two completely different ways, and both of them are the math showing through.

[pause 400ms]

Recall the mechanism: STFT frames re-spaced on output, the phase in each band re-derived so partials stay continuous. When that re-derivation is even slightly off, you get one of two artifacts, and they are the signature of the Complex modes.

[pause 500ms]

First: transient smearing. The STFT basis is sines and cosines, and as Stephan Bernsee puts it in his time-and-pitch overview, those basis functions "have no localization in the Time Domain, which without further treatment contributes to the inherent signal smearing." A drum hit is a sharp event in time, but the transform spreads its energy across a whole frame. Stretch the frame and you stretch the hit — the click softens into a thwip. That is exactly why the manual sends drums to Beats and whole songs to Complex. The phase vocoder cannot keep a transient sharp; it was never built in time.

[pause 500ms]

Second: phasiness. The phase vocoder keeps each band continuous across frames, but does not force the bands belonging to one partial to stay coherent with each other. That leftover incoherence sounds, again Bernsee, like "smearing and reverberation, even at low expansion ratios." Watery, hollow, loose of punch — because "the temporal development of a sound is contained in its phase information," and you just scrambled it.

[pause 400ms]

Hear both at once. Same break loop, half tempo, switched between Beats and Complex.

[cue: transient-survival-ab]

Beats kept the kick punchy because it cut on the silence between hits. Complex blurred the kick because it smeared it across a frame. That haunted, watery sound in the second half is not a preset and not reverb. It is the algorithm failing to keep phase. élastique, inside Complex Pro, is a high-quality member of this family — which is why Complex Pro is cleaner than plain Complex. But the manual is blunt: even the best of them is never neutral.

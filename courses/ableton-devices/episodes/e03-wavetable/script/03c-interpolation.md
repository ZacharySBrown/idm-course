If a wavetable is a row of separate frames, the obvious question is what happens between them. Jump straight from frame *i* to frame *i+1* and you get audible stepping — zipper noise. That is exactly the harshness Palm described, by the way: very harsh, he said, because the eight-bit hardware had no real-time interpolation. The PPG zippered, and it zippered gloriously, because it had no choice.

[pause 500ms]

The modern fix is a linear cross-fade. For a continuous position between frame *i* and the next, with fraction alpha: the output is one-minus-alpha times frame *i*, plus alpha times frame *i+1*. A weighted blend. As Position slides, alpha slides, and the harmonics morph rather than snap.

[pause 600ms]

This only works cleanly if neighboring frames are spectrum- and phase-compatible — which is why Ableton's table-builders enforce no inharmonic content between adjacent waves. Blend two compatible spectra and you morph; blend two incompatible ones and you phase-cancel into mush. Serum runs a comparable scheme — roughly a fifty-millisecond fade from one waveform to the next.

[pause 500ms]

Here is the difference, in your ears. The same slow sweep, twice: first stepped, the way the hardware did it, then interpolated. Listen for the stairs in the first pass and the glide in the second.

[cue: wt-zipper-vs-smooth]

The first one stepped between frames. The second one glided through them. That cross-fade is the entire reason a Position sweep sounds like a continuous timbre and not a fast arpeggio of separate tones.

Now the part where, if you've done any physics, you already know this — you just didn't know it was called wavetable.

[pause 500ms]

Take one frame. It's a single period of a periodic waveform, some number of samples long. By the discrete Fourier transform, that frame is exactly equivalent to a fixed set of harmonic partials — amplitudes and phases at integer multiples of the frame's fundamental. Which means each frame is an additive snapshot. A frozen additive patch.

[pause 600ms]

So a wavetable is a sequence of additive snapshots. And scanning Position from one frame to the next is interpolating between two additive spectra. You are walking a path through Fourier space, one frame at a time. That's all it is.

[pause 500ms]

To make the snapshot idea concrete: take one table, put two oscillators on it, set Osc one to a low Position and Osc two to a high Position of that same table, equal gain. Same waveform set, two different points in it. Listen to the two timbres — first the low position, then the high.

[cue: wt-ab-two-positions]

Two distinct spectra out of one table. That's the proof a wavetable is a collection of spectra, not a single tone you're bending. And this is why Serum's FFT import works at all — it computes the harmonic content of any sample and stores it as a frame. Any sound you have becomes a coordinate in the table.

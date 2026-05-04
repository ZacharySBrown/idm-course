Each of Operator's four oscillators exposes the same controls. A few of them are non-obvious enough that you can use Operator for years and not realize what they actually do.

[pause 400ms]

*Coarse* is a frequency multiplier, not an octave selector. Steps go zero-point-two-five, zero-point-five, zero-point-seven-five, one, two, three, all the way up to thirty-two. The DX7 maxed out at thirty-one-point-nine-nine — Operator goes to thirty-two. The ratio between Coarse on a modulator and Coarse on its carrier — the C-over-M ratio — determines whether the spectrum is harmonic or inharmonic.

[pause 500ms]

*Fine* is a one-octave span in one thousand steps, *positive only*. To detune downward, you have to lower Coarse by one octave and push Fine to nine-eighty or higher. This asymmetry is rarely explained in the manual. It's the canonical Francis Preve supersaw trick.

[pause 500ms]

*Fixed* mode toggles the oscillator from ratio-based to absolute-Hertz mode. Coarse becomes Frequency in Hertz, down to zero-point-one. The use case for IDM is inharmonic percussion: tune all four operators to small primes — one-thirty-seven, three-eleven, five-twenty-three Hertz — at low Multi values, against a key-tracked carrier. Every key produces a different inharmonic ratio. The result is metallic, drum-like, but pitched.

[pause 500ms]

*Level* is the brightness control. When the oscillator is functioning as a modulator, Level is proportional to the modulation index I. Envelope it, and you envelope timbre directly.

[pause 400ms]

The waveform list extends past sine. The IDM tools are *Sine 4* — a four-bit-quantized sine with audible odd harmonics, chip-grit — *Sine 8*, *Saw D* the digital infinite-bandwidth saw that aliases harshly on purpose, and *NoiseLoop* — a one-thousand-twenty-four-sample cyclic random lookup table, tunable, no DX7 equivalent. Henke's words: *"bad noise as a feature."*

# Underlying algorithm — 12-bit companded ADC at 7.5–40 kHz

People mistake the S950 for a low-sample-rate sampler because they think of the SP-1200. The S950's grit is different and worth being precise about.

- **Sampling rate.** User-selectable **7.5–40 kHz**. Jenkinson typically ran at the 40 kHz ceiling for pitch headroom; the lo-fi signature lives at the lower settings. Lower rate means lower Nyquist, which is the aliasing knob.
- **Bit depth.** 12-bit linear quantization with a **µ-law-style (Akai/E-mu 12→8-bit proprietary)** companding curve applied before the ADC — not literal ITU G.711 µ-law, but the same shape. Roads 1996 covers the general principle: companding compresses dynamic range before quantization, decompresses on playback, effectively trading linear SNR for a perceptual SNR that is quieter on transients and noisier on low-level sustained content. <Citation bib="roads_computer_music_tutorial" />
- **Reconstruction filter.** Fixed anti-alias filter at roughly half the sampling rate, gentle slope.
- **Pitch shift.** Naive sample-rate conversion — repitching up an octave doubles playback rate. Aliasing appears on upward shifts past a threshold that's audible by roughly **+4 semitones**; downward shifts produce decimation artifacts (not aliasing) that thicken the tone rather than fold it.

The "classic sampler grit" is the companding curve plus the aliasing, not the bit depth in isolation.

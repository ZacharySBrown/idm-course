## Underlying algorithm — STEAM + wavetable hybrid

Omnisphere's engine is called **STEAM** (Spectrasonics' internal name). Two parallel synthesis paths per layer, chosen per patch.

- **Sample path** — multi-sampled instruments, granularized, reverse-playable, time-stretchable. Backed by a 64+ GB factory library on disk. `bib:spectrasonics_omnisphere_docs`.
- **Synth path** — classic subtractive + wavetable + FM-like operator modulation, all under one oscillator page.
- **Hybrid mode** — sample + synth summed per layer, with independent filters and envelopes each.

The "three layers per patch" in practice: one sample layer for body, one wavetable for harmonic sparkle, one noise/texture for grain. Spectrasonics' engineers pre-stack these combinations into every factory patch.

Roads would call this <term key="concatenative">concatenative and spectral hybrid synthesis</term>. Hebden calls it "the synth plugin." Both are correct. `Roads 1996`.

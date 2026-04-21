# Where the four stems live, frequency-wise

Rough occupancy, in Hz, for the four-stem Demucs split. Ranges overlap — that's the point; separation is a probabilistic classification, not a clean crossover network.

- **Drums (kick + snare + hats)** — kick body sits 40-120 Hz, snare fundamental 150-250 Hz, hat content 3 kHz and up.
- **Bass** — 40-250 Hz for the fundamental, harmonic content up to 800 Hz depending on synthesis.
- **Vocals** — 200 Hz to 4 kHz for the lead range, sibilance out to 8-10 kHz.
- **Other** — everything else: pads, leads, textures, typically 100 Hz to 8 kHz with the densest content in the 300 Hz-2 kHz band.

The <term key="demucs">Demucs U-Net</term> learns these masks from training data; it doesn't apply a fixed filterbank. <Citation bib="stemforge_repo" />

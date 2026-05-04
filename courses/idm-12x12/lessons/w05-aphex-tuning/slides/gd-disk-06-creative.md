# What else Collision-as-Disklavier does — past the piano stereotype

Stop using Collision for piano-like tones. It is a better **percussion engine** than most drum synths. Four moves:

- **Collision as tuned wood-block kit** — Mallet layer only, Resonator type: Beam, Material 100%, Decay 500ms. Play chromatically; it sounds like a Balinese gamelan sampled through a physical model. Pair with a trap-style MIDI pattern; the contrast is the point.
- **Collision as detuned marimba** — Resonator type: Membrane, Ratio set to 7:4 or another 7-limit JI interval. Now the model resonates at a non-tempered pitch. Layer with a Tuning-Systems-loaded Operator for coherent JI drums.
- **Collision as percussion-only shell** — mute the Mallet layer entirely, use external MIDI CC to modulate the impact. The resonator "rings" without being struck. This is the sound Autechre often chases in Max/MSP. <Citation bib="autechre_watmm_ama_2013" />
- **Collision as solenoid-click printer** — strip the resonator completely (Decay 20ms, Ratio 0.01). What's left is the mallet attack. Layer that over any drum bus and you get the Drukqs "mechanical noise bed" — cheap, per-note-triggered.

The Disklavier technique generalizes: **the attack mechanism and the resonator are separable**, and separating them is where the interesting percussion lives. Aphex figured this out with microphone placement. You figure it out with Collision's two-layer architecture.

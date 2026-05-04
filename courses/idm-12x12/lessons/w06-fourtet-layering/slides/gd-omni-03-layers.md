## Annotated tour 2/5 — patch layer architecture

Every Omnisphere patch is two **Parts** (A + B), each with two **Layers** (A+B inside each Part). Four <term key="sound_source">sound sources</term> stackable per patch, each independently filtered, enveloped, and routed.

- Each Layer picks either a **Soundsource** (sample, multisampled or one-shot) or a **Synth oscillator** (wavetable, analog-model, granular).
- Layers can be **detuned, panned, velocity-crossfaded**, or triggered as round-robin.
- Most factory patches already use 3–4 layers. "Plectra Sub" is a plucked-string layer plus a filtered sine sub plus a noise transient. Pre-stacked.

The implication for Hebden: many Omnisphere presets are already layered subliminal kick-stacks in miniature. He is not skipping the layering work — someone did it for him at Spectrasonics.

# Patch tutorial — `an-reese-morph`

**Preset:** `presets/an-reese-morph.adv`  ·  **Concept:** Morph the 303 into a Reese — add OSC2 saw, detune, sub, drop the filter env

> The same patch with OSC2 turned on and detuned +18 cents, Sub on, the filter envelope dropped and the cutoff lowered: the acid squelch becomes a fat, growling detuned bass. **The pivot the walkthrough exists for** — start from the `an-303-step6` patch and apply these deltas.
>
> **You should hear:** A sustained low growl with slow beating between two detuned saws; no per-note filter wow.

Build from a **freshly loaded default Analog** (or the `an-303-step6` preset). Filter Freq is NORMALIZED 0–1 (NOT Hz); Detune 0.5 = 0 cents (norm = 0.5 + cents/600). **Bold rows = the morph deltas vs the 303.**

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | Load | Default Analog | init | A saw on each note |
| 1 | Global / Voices | Voices | Mono |  |
| 2 | Global / Glide | Glide On/Off | On |  |
| 3 | Global / Glide | Glide Mode | Const |  |
| 4 | Global / Glide | Glide Time | 0.15 |  |
| 5 | Global / Glide | Glide Legato | On |  |
| 6 | OSC 1 | OSC1 On/Off | On |  |
| 7 | OSC 1 | OSC1 Shape | Saw |  |
| 8 | **OSC 1** | **OSC1 Mode** | **Sub (Sub/Sync slider = sub-osc level)** |  |
| 9 | **OSC 1** | **O1 Sub/Sync** | **0.5 (sub-osc weight on)** | **An octave-down weight under the note** |
| 10 | OSC 1 | OSC1 Detune | 0.5 (= 0 cents) |  |
| 11 | OSC 1 | OSC1 Balance | 1.0 |  |
| 12 | **OSC 2** | **OSC2 On/Off** | **On (the pivot — second saw)** | **A second saw enters** |
| 13 | **OSC 2** | **OSC2 Shape** | **Saw** |  |
| 14 | **OSC 2** | **OSC2 Detune** | **0.53 (= +18 cents — the Reese beating)** | **A slow "wub" between the saws** |
| 15 | **OSC 2** | **OSC2 Balance** | **1.0** |  |
| 16 | Noise | Noise On/Off | Off |  |
| 17 | Filter 1 | F1 On/Off | On |  |
| 18 | Filter 2 | F2 On/Off | Off |  |
| 19 | Filter 1 | F1 Type | Low-pass 24dB/oct |  |
| 20 | **Filter 1** | **F1 Freq** | **0.507 (≈ 870 Hz — raised so saw body + beat carry)** |  |
| 21 | **Filter 1** | **F1 Resonance** | **0.2 (back off the squelch)** |  |
| 22 | Filter 1 | F1 Drive | Sym1 |  |
| 23 | **Filter 1** | **F1 Freq < Env** | **0.0 (filter envelope DROPPED — the morph)** | **No more per-note wow** |
| 24 | Filter Env 1 | FEG1 Decay | 0.25 (inert now that amount = 0) |  |
| 25 | Filter Env 1 | FEG1 Sustain | 1.0 |  |
| 26 | Amp Env 1 | AEG1 Attack | 0.03 (≈ 5 ms) |  |
| 27 | Amp Env 1 | AEG1 Decay | 0.0 |  |
| 28 | **Amp 1** | **AMP1 Level** | **0.85 (held low note lands healthy)** |  |
| 29 | Amp Env 1 | AEG1 Sustain | 1.0 |  |
| 30 | Amp Env 1 | AEG1 Rel | 0.3 (≈ 200 ms) |  |
| 31 | Global | Key Error | 0.0 |  |

**Play:** hold a low note (C1) so the beating reads. The acid squelch is now a detuned-saw growl.

_To persist: right-click the Analog title bar → **Save Preset** → save as `an-reese-morph` into `presets/`._

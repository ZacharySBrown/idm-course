# Patch tutorial — `an-303-step1`

**Preset:** `presets/an-303-step1.adv`  ·  **Concept:** 303 build step 1 — mono saw, glide + legato (the raw source)

> A bare sawtooth, monophonic, notes gliding into each other — no filter shaping yet. The starting material. **This is step 1 of the 6-step 303 ladder** (`an-303-step1` … `an-303-step6`); each step is a saved preset.
>
> **You should hear:** A bright unfiltered saw line with audible glide between overlapping (legato) notes.

Build from a **freshly loaded default Analog**. One parameter per step. Filter Freq is NORMALIZED 0–1 (NOT Hz).

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | Load | Default Analog | init | A saw on each note |
| 1 | Global / Voices | Voices | Mono |  |
| 2 | Global / Glide | Glide On/Off | On |  |
| 3 | Global / Glide | Glide Mode | Const |  |
| 4 | Global / Glide | Glide Time | 0.15 (short) |  |
| 5 | Global / Glide | Glide Legato | On | Overlapping notes slide |
| 6 | OSC 1 | OSC1 On/Off | On |  |
| 7 | OSC 1 | OSC1 Shape | Saw | A bright buzzy saw |
| 8 | OSC 1 | O1 Sub/Sync | 0.0 (sub off) |  |
| 9 | OSC 1 | OSC1 Balance | 1.0 |  |
| 10 | OSC 2 | OSC2 On/Off | Off |  |
| 11 | Noise | Noise On/Off | Off |  |
| 12 | Filter 1 | F1 On/Off | On |  |
| 13 | Filter 2 | F2 On/Off | Off |  |
| 14 | Filter 1 | F1 Type | Low-pass 24dB/oct |  |
| 15 | Filter 1 | F1 Freq | 1.0 (wide open this step) | Unfiltered, full saw |
| 16 | Filter 1 | F1 Resonance | 0.0 |  |
| 17 | Filter 1 | F1 Drive | Off |  |
| 18 | Filter 1 | F1 Freq < Env | 0.0 |  |
| 19 | Amp Env 1 | AEG1 Attack | 0.01 (≈ 2 ms) |  |
| 20 | Amp Env 1 | AEG1 Decay | 0.0 |  |
| 21 | Amp Env 1 | AEG1 Sustain | 1.0 |  |
| 22 | Amp Env 1 | AEG1 Rel | 0.15 (≈ 80 ms) |  |
| 23 | Global | Key Error | 0.0 |  |

**Play:** a 16th-note line (e.g. C2-C2-Eb2-C2, 2 bars at 130 BPM) with some overlapping notes so the glide reads.

_To persist: right-click the Analog title bar → **Save Preset** → save as `an-303-step1` into `presets/`._

# Patch tutorial — `an-reese-final`

**Preset:** `presets/an-reese-final.adv`  ·  **Concept:** The finished Reese — hold a low note, hear the saws beat (and accelerate up the keyboard)

> Two detuned saws on a held low note: the "wub" of phase cancellation with no LFO, the beating speeding up as the pitch rises (constant-cents detune). **Canonical Reese (Kevin Saunderson, "Just Another Chance", 1988) = TWO detuned saws — NO sub osc** (sub put energy at ~33 Hz, inaudible on phones and a normalization-headroom drain).
>
> **You should hear:** Audible beating on both notes; the higher note beats roughly twice as fast (Δf scales with f).

Build from a **freshly loaded default Analog**. One parameter per step. Filter Freq is NORMALIZED 0–1 (NOT Hz); Detune 0.5 = 0 cents.

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
| 8 | OSC 1 | O1 Sub/Sync | 0.0 (sub OFF — un-canonical and quiet) |  |
| 9 | OSC 1 | OSC1 Detune | 0.5 (= 0 cents) |  |
| 10 | OSC 1 | OSC1 Balance | 1.0 |  |
| 11 | OSC 2 | OSC2 On/Off | On |  |
| 12 | OSC 2 | OSC2 Shape | Saw |  |
| 13 | OSC 2 | OSC2 Detune | 0.53 (= +18 cents — the Reese beat) | A slow "wub" |
| 14 | OSC 2 | OSC2 Balance | 1.0 |  |
| 15 | Noise | Noise On/Off | Off |  |
| 16 | Filter 1 | F1 On/Off | On |  |
| 17 | Filter 2 | F2 On/Off | Off |  |
| 18 | Filter 1 | F1 Type | Low-pass 24dB/oct |  |
| 19 | Filter 1 | F1 Freq | 0.507 (≈ 870 Hz — more saw body passes) |  |
| 20 | Filter 1 | F1 Resonance | 0.2 |  |
| 21 | Filter 1 | F1 Drive | Sym1 |  |
| 22 | Filter 1 | F1 Freq < Env | 0.0 (no filter env) |  |
| 23 | Amp Env 1 | AEG1 Attack | 0.03 (≈ 5 ms) |  |
| 24 | Amp Env 1 | AEG1 Decay | 0.0 |  |
| 25 | Amp 1 | AMP1 Level | 0.85 (patch must set this; default 0.474 ≈ -6.5 dB) | A healthy level |
| 26 | Amp Env 1 | AEG1 Sustain | 1.0 |  |
| 27 | Amp Env 1 | AEG1 Rel | 0.3 (≈ 200 ms) |  |
| 28 | Global | Key Error | 0.0 |  |

**Play:** hold C1 (slow beating), then C2 an octave up (faster beating — Δf doubles per octave at constant cents).

_To persist: right-click the Analog title bar → **Save Preset** → save as `an-reese-final` into `presets/`. This is the "Subtractive-303-Reese" Reese half._

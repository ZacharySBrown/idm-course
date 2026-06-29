# Patch: Two-Hands — Step 3: Cross-Engine LFO  (preset: presets/meld-twohands-step3.adv)

**Demo:** `meld-twohands-step3`  ·  **Slide:** `05c-cross-engine-lfo`  ·  **Structure:** single (build-step)
**Concept demonstrated:** Step 3 — cross-engine: A's LFO 1 drives B's Macro 1 (control-rate, NOT audio-rate cross-mod). The two layers now breathe together but differently.

> ## ⚠ THIS DEMO IS BUILT BY HAND — IT CANNOT BE RENDERED OVER OUR HEADLESS PATH.
> The cross-engine route `A LFO 1 → B Osc Shape` lives in the **modulation matrix**, which is **not
> in Meld's LOM param map**. The manifest's single-ramp `automation:` FALLBACK morphs B's Osc Shape
> directly (one sweep, not LFO-cyclic) and will NOT pass the oscillation assertion. **Hand-build the
> cross-engine route in the live device.** (Bi-timbral cross-mod is control-rate only — A's LFO can
> modulate B's parameter; the engines do NOT audio-rate FM each other.)

**⚠ PLACEHOLDER ENUM INDEX:** `B Filter Type` Plate Resonator = PLACEHOLDER **15** (confirm live, carried from Step 2).

Re-state Engine A + B as Step 2 (renderer does not carry forward), then add the LFO and the cross-engine route.

### Engine A (as Step 2) + LFO 1
| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 1 | Engine A | `A On` / `A Osc Type` | On / **19 = Swarm Saw** | The in-key saw body |
| 2 | Engine A | `A Osc Shape` / `A Osc Tone` | 0.30 / 0.40 | Gentle motion, medium spread |
| 3 | Engine A | `A Osc Scale Aware` | On (1) | In-key |
| 4 | Engine A | `A Filter On` / `A Filter Type` / `A Filter L-B-H-N` | On / **0 = Analog** / 0.0 | Warm low-pass |
| 5 | Engine A | `A Filter Freq` | 0.55 | Gentle low-pass |
| 6 | Engine A (LFO 1) | `A LFO 1 Type` | **0 = first waveform (sine-ish)** | (the modulation shape) |
| 7 | Engine A (LFO 1) | `A LFO 1 Rate` | 0.25 (NORMALIZED 0–1, slow — NOT Hz) | (slow breathe period; no audible motion until routed) |
| 8 | Engine A | `A Volume` | 0.65 | Chord-level body |

### Engine B (as Step 2)
| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 9 | Engine B | `B On` / `B Osc Type` | On / **9 = Harmonic FM** | The glassy FM layer |
| 10 | Engine B | `B Osc Shape` (FM Amount) | 0.50 (this is what A's LFO will modulate) | A bright FM amount — the modulation target |
| 11 | Engine B | `B Osc Tone` (FM Ratio) | 0.40 | A metallic ratio |
| 12 | Engine B | `B Octave` | **1** (octave up) | The layer an octave above |
| 13 | Engine B | `B Filter On` / `B Filter Type` | On / **Plate Resonator (idx 15 PLACEHOLDER — CONFIRM)** | A struck, resonant shimmer |
| 14 | Engine B | `B Filter Filter Scale Aware` | On (1) | Modes snap in key |
| 15 | Engine B | `B Volume` | 0.40 | A layer under the body |
| 16 | Global | `Scale Aware` | On (1) | Master scale-snap on |

### HAND-BUILD: the cross-engine matrix route (this is what makes Step 3 work)
In the live device's **Matrix** tab, add ONE route:

| Source | Destination | Amount |
|---|---|---|
| `A LFO 1` | `B Osc Shape` (Engine B macro 1 = FM Amount) | **+0.6 (cross-engine, control-rate)** |

A's slow LFO now morphs B's FM timbre while A holds steady.

**Play:** hold `C3 + G3` for ~4.6 s.

**Final check:** same two layers as Step 2, but B's timbre now slowly morphs at the LFO rate while A holds steady.
**Analyzer:** B's centroid oscillates at A's LFO rate; A unchanged.

**Save:** with the cross-engine route built, right-click Meld → **Save Preset** → `presets/meld-twohands-step3.adv`.

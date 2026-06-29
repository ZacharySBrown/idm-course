# Patch: Zipper-vs-Smooth  (preset: presets/wt-zipper-vs-smooth.adv)

Concept demonstrated: **frame interpolation → a stepped scan becomes a continuous glide.**

> ⚠ **HAND-BUILD REQUIRED — the demonstrative variable is NOT settable over our headless path.**
> The A/B contrast hinges on the **Hi-Q / interpolation** state, which is **not LOM-exposed**. There is no settable proxy (Ableton always frame-interpolates), so the "stepped" segment cannot be produced from any param. **Set Hi-Q in Live by hand** for segment A (off → stepped) vs segment B (on → smooth), or render the two segments by hand and concatenate. The patch below renders only the **smooth reference (B)** half.

Build from a **freshly loaded default Wavetable.** Position on the **0–1 LOM scale**.

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | — | Load default Wavetable | init | Neutral saw per note |
| 1 | Osc 1 | Table / Category | **Basic Shapes** (default) | ⚠ Table not settable headless — confirm by hand. |
| 2 | Osc 1 | Osc 1 On | On (1) | Osc 1 sounding |
| 3 | Osc 1 | Osc 1 Pos | 0.0 | First frame — near-sine |
| 4 | Osc 1 | Osc 1 Detune | 0.5 (0 cents) | Single clean voice |
| 5 | Osc 1 | Osc 1 Gain | 1.0 (unity) | Full level |
| 6 | Osc 2 | Osc 2 On | Off (0) | Osc 1 only |
| 7 | Sub | Sub On | Off (0) | No sub |
| 8 | Filter 1 | Flt 1 On | On (1) | Filter in path |
| 9 | Filter 1 | Flt 1 Type | 0 (Clean) | Transparent circuit |
| 10 | Filter 1 | Flt 1 LP/HP | 0 (Lowpass) | Lowpass mode |
| 11 | Filter 1 | Flt 1 Freq | 1.0 (open) | Full brightness |
| 12 | Filter 1 | Flt 1 Res | 0.0 | No resonance |
| 13 | Filter 2 | Flt 2 On | Off (0) | Single filter |
| 14 | Amp Env | Amp Attack | 0.05 | Fast attack |
| 15 | Amp Env | Amp Sustain | 1.0 | Holds full level |
| 16 | Amp Env | Amp Release | 0.15 | Short tail |
| 17 | Global | **Hi-Q** | A = **Off**, B = **On** | ⚠ **Set in Live by hand (not settable over our headless path).** Off = stepped/zippered sweep; On = smooth glide. |

**The demonstrative move:**
Hold **C3** and sweep **Osc 1 Pos 0.0 → 1.0** over ~2.8 s — once with **Hi-Q OFF** (segment A, hear the stepping/zipper), once with **Hi-Q ON** (segment B, hear a continuous glide).

Final check: A stairsteps audibly during the sweep; B glides. A's spectral flux ≈ B's ⇒ reject.

**Save:** right-click Wavetable → **Save Preset** → `presets/wt-zipper-vs-smooth.adv`. **Set Hi-Q to the intended state in Live before saving** (save the B/Hi-Q-On reference; note the Hi-Q dependency in the preset comment).

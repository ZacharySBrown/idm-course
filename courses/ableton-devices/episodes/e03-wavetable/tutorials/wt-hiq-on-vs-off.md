# Patch: Hi-Q On-vs-Off (PPG vs Serum)  (preset: presets/wt-hiq-on-vs-off.adv)

Concept demonstrated: **Hi-Q (oversampling) → aliasing removed; the PPG-vs-Serum aesthetic in one switch.**

> ⚠ **HAND-BUILD REQUIRED — the demonstrative variable is NOT settable over our headless path.**
> The A/B hinges on the **Hi-Q toggle**, which is **not LOM-exposed**. **Set Hi-Q in Live by hand** and render the two segments separately (Hi-Q OFF = gritty/aliased PPG; Hi-Q ON = clean Serum), then concatenate. The patch below renders one fast high-register sweep (a single segment). A **bright/harmonic-rich table** (Distortion category) is also needed and is **not settable headless** — pre-load it by hand.

Build from a **freshly loaded default Wavetable.** Position on the **0–1 LOM scale**.

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | — | Load default Wavetable | init | Neutral saw per note |
| 1 | Osc 1 | Table / Category | **bright/Distortion table** | ⚠ **Set in Live by hand (not settable over our headless path)** — a harmonic-rich table exaggerates aliasing. |
| 2 | Osc 1 | Osc 1 On | On (1) | Osc 1 sounding |
| 3 | Osc 1 | Osc 1 Pos | 0.0 | First frame |
| 4 | Osc 1 | Osc 1 Detune | 0.5 (0 cents) | Single clean voice |
| 5 | Osc 1 | Osc 1 Gain | 1.0 (unity) | Full level |
| 6 | Osc 2 | Osc 2 On | Off (0) | Osc 1 only |
| 7 | Sub | Sub On | Off (0) | No sub |
| 8 | Filter 1 | Flt 1 On | On (1) | Filter in path |
| 9 | Filter 1 | Flt 1 Type | 0 (Clean) | Transparent circuit |
| 10 | Filter 1 | Flt 1 LP/HP | 0 (Lowpass) | Lowpass mode |
| 11 | Filter 1 | Flt 1 Freq | 1.0 (open) | Wide open so aliasing is NOT masked |
| 12 | Filter 1 | Flt 1 Res | 0.0 | No resonance |
| 13 | Filter 2 | Flt 2 On | Off (0) | Single filter |
| 14 | Amp Env | Amp Attack | 0.02 (very fast) | Note speaks instantly |
| 15 | Amp Env | Amp Sustain | 1.0 | Holds full level |
| 16 | Amp Env | Amp Release | 0.1 | Short tail |
| 17 | Global | **Hi-Q** | A = **Off**, B = **On** | ⚠ **Set in Live by hand (not settable over our headless path).** Off = gritty aliased PPG; On = clean Serum. |

**The demonstrative move:**
Hold a **high** note (**C5** — exaggerates aliasing) and sweep **Osc 1 Pos 0.0 → 1.0** fast (~2.0 s). Render once **Hi-Q OFF** (segment A — gritty buzz), once **Hi-Q ON** (segment B — clean glide).

Final check: A has inharmonic grit / raised inter-harmonic floor; B sits on the harmonic comb. A ≈ B ⇒ reject.

**Save:** right-click Wavetable → **Save Preset** → `presets/wt-hiq-on-vs-off.adv`. **Pre-load the bright table and set Hi-Q by hand before saving** (save the Hi-Q-On reference; note both dependencies in the preset comment).

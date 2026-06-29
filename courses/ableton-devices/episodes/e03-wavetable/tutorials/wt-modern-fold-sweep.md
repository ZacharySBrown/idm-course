# Patch: Modern-Fold-Sweep  (preset: presets/wt-modern-fold-sweep.adv)

Concept demonstrated: **Modern → Fold (wavefolding) → buzzy upper harmonics from one oscillator, no extra device.** Position fixed; sweep Fold and hear the wave driven into itself.

> ⚠ **PARTIAL HAND-BUILD — the Osc Effect MODE is NOT settable over our headless path.**
> Set **Osc 1's effect mode to Modern** in Live by hand. In Modern, **Effect 1 = Warp** and **Effect 2 = Fold** — both knobs ARE settable once the mode is set.

Build from a **freshly loaded default Wavetable.** Position on the **0–1 LOM scale**.

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | — | Load default Wavetable | init | Neutral saw per note |
| 1 | Osc 1 | Table / Category | default (Basic Shapes) | ⚠ Table not settable headless — confirm by hand. |
| 2 | Osc 1 | Osc 1 On | On (1) | Osc 1 sounding |
| 3 | Osc 1 | Osc 1 Pos | 0.25 (FIXED — not the variable) | A steady wavetable tone |
| 4 | Osc 1 | Osc 1 Detune | 0.5 (0 cents) | Single clean voice |
| 5 | Osc 1 | Osc 1 Gain | 1.0 (unity) | Full level |
| 6 | Osc 1 | **Osc 1 Effect Mode** | **Modern** | ⚠ **Set in Live by hand (not settable over our headless path).** Enables Warp + Fold. |
| 7 | Osc 1 | Osc 1 Effect 1 (Warp) | 0.0 | No warp |
| 8 | Osc 1 | Osc 1 Effect 2 (Fold) | 0.0 (start) | No fold yet — plain tone |
| 9 | Osc 2 | Osc 2 On | Off (0) | Osc 1 only |
| 10 | Sub | Sub On | Off (0) | No sub |
| 11 | Filter 1 | Flt 1 On | On (1) | Filter in path |
| 12 | Filter 1 | Flt 1 Type | 0 (Clean) | Transparent circuit |
| 13 | Filter 1 | Flt 1 LP/HP | 0 (Lowpass) | Lowpass mode |
| 14 | Filter 1 | Flt 1 Freq | 1.0 (open) | Full brightness — fold harmonics pass |
| 15 | Filter 1 | Flt 1 Res | 0.0 | No resonance |
| 16 | Filter 2 | Flt 2 On | Off (0) | Single filter |
| 17 | Amp Env | Amp Attack | 0.05 | Fast attack |
| 18 | Amp Env | Amp Sustain | 1.0 | Holds full level |
| 19 | Amp Env | Amp Release | 0.15 | Short tail |

**The demonstrative move (sweep):**
Hold **C3** for ~4.7 s and sweep **Osc 1 Effect 2 (Fold) 0.0 → 0.9** over ~4.3 s. Position stays fixed at 0.25. You should hear a plain tone grow into a buzzy, harmonically dense wavefold.

Final check: pitch constant; upper-harmonic energy / spectral spread rises monotonically. Flat ⇒ Fold didn't engage or the mode wasn't Modern ⇒ reject.

**Save:** right-click Wavetable → **Save Preset** → `presets/wt-modern-fold-sweep.adv`. **Set Effect Mode = Modern in Live before saving** (save with Effect 2 = 0.0, the sweep start).

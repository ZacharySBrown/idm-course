# Patch: Spectra-Morph — Step 2/7 (Slow LFO → Position bloom)  (preset: presets/wt-spectra-step2.adv)

Concept demonstrated: **walkthrough step 2 of 7 — slow LFO → Position with a fade-in: the PPG choir bloom.** The step-1 pad now blooms and morphs after it's held.

> ⚠ **PARTIAL HAND-BUILD — Formants table + LFO→Position matrix routing are NOT settable over our headless path.**
> Pre-load the **Formants table** (step 1) and build the **LFO 1 → Osc 1 Pos** matrix row by hand (step 19). `LFO 1 Attack Time` IS settable; its routing to Position is not. Headless render reproduces the bloom by automating `Osc 1 Pos` (flat ~2 s, then a slow drift).

Builds on **Step 1** (start from the step-1 patch, or rebuild from default below). Position on the **0–1 LOM scale**.

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | — | Load default Wavetable | init | Neutral saw per note |
| 1 | Osc 1 | Table / Category | **Formants (vocal/choir)** | ⚠ **Set in Live by hand.** Vowel timbre. |
| 2 | Osc 1 | Osc 1 On | On (1) | Osc 1 sounding |
| 3 | Osc 1 | Osc 1 Pos | 0.35 (center; will drift) | A vowel frame |
| 4 | Osc 1 | Osc 1 Detune | 0.5 (0 cents) | Single clean voice |
| 5 | Osc 1 | Osc 1 Gain | 1.0 (unity) | Full level |
| 6 | Osc 2 | Osc 2 On | Off (0) | Osc 1 only |
| 7 | Sub | Sub On | Off (0) | No sub |
| 8 | Filter 1 | Flt 1 On | On (1) | Filter in path |
| 9 | Filter 1 | Flt 1 Type | 0 (Clean) | Transparent circuit |
| 10 | Filter 1 | Flt 1 LP/HP | 0 (Lowpass) | Lowpass mode |
| 11 | Filter 1 | Flt 1 Freq | 0.9 | Gently shaded top |
| 12 | Filter 1 | Flt 1 Res | 0.1 | A touch of resonance |
| 13 | Filter 2 | Flt 2 On | Off (0) | Single filter |
| 14 | Amp Env | Amp Attack | 0.45 (~800 ms) | Soft swell |
| 15 | Amp Env | Amp Sustain | 1.0 | Holds full level |
| 16 | Amp Env | Amp Release | 0.55 (~1.5 s) | Long tail |
| 17 | LFO 1 | LFO 1 Shape | Triangle, slow rate | (sets the morph shape/rate) |
| 18 | LFO 1 | **LFO 1 Attack Time** | 0.6 (~2 s fade-in) | The LFO fades in over ~2 s |
| 19 | Matrix | **LFO 1 → Osc 1 Pos** | amount **30** | ⚠ **Set in Live by hand (not creatable over our headless path).** ADDED this step — the slow Position scan. |

**The sound (single):**
Hold the **C3 / Eb3 / G3** triad ~5.5 s. Static at first, then the chord morphs/breathes after ~2 s — the PPG choir scan. (Headless proxy: flat ~2 s, then slow `Osc 1 Pos` drift 0.35 → ~0.62 and back.)

Final check: centroid motion near zero early, growing later (the bloom). No motion ⇒ the Position drift didn't take ⇒ reject.

**Save:** right-click Wavetable → **Save Preset** → `presets/wt-spectra-step2.adv`. **Pre-load Formants + build the LFO 1 → Osc 1 Pos row in Live before saving.**

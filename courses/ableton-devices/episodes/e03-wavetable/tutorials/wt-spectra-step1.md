# Patch: Spectra-Morph — Step 1/7 (Static Vowel Pad)  (preset: presets/wt-spectra-step1.adv)

Concept demonstrated: **walkthrough step 1 of 7 — a static vowel pad (the starting point).** A held chord on a vocal/formant table with a slow amp attack and long release. No movement yet.

> ⚠ **PARTIAL HAND-BUILD — the Formants table is NOT settable over our headless path.**
> Pre-load a **Formants-category (vocal/choir) table** on Osc 1 in Live by hand (step 1). Position still selects the frame.

Build from a **freshly loaded default Wavetable.** Position on the **0–1 LOM scale**.

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | — | Load default Wavetable | init | Neutral saw per note |
| 1 | Osc 1 | Table / Category | **Formants (vocal/choir)** | ⚠ **Set in Live by hand (not settable over our headless path).** A vowel-like timbre. |
| 2 | Osc 1 | Osc 1 On | On (1) | Osc 1 sounding |
| 3 | Osc 1 | Osc 1 Pos | 0.35 | A specific vowel frame |
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
| 14 | Amp Env | Amp Attack | 0.45 (~800 ms) | A soft, slow swell |
| 15 | Amp Env | Amp Decay | 0.0 | No decay stage |
| 16 | Amp Env | Amp Sustain | 1.0 (full) | Holds at full level |
| 17 | Amp Env | Amp Release | 0.55 (~1.5 s) | Long tail on key-up |

**The sound (single):**
Hold a **C3 / Eb3 / G3** triad for ~4.5 s. A sustained vowel-like chord with a soft attack and no timbral motion — the static pad we add movement to in step 2.

Final check: formant-style fixed spectrum; centroid roughly flat across the sustain (no movement yet).

**Save:** right-click Wavetable → **Save Preset** → `presets/wt-spectra-step1.adv`. **Pre-load the Formants table in Live before saving.**

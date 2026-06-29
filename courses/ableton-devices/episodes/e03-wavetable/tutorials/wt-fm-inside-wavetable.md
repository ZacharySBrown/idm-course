# Patch: FM-Inside-Wavetable  (preset: presets/wt-fm-inside-wavetable.adv)

Concept demonstrated: **the hidden FM oscillator → harmonics generated INSIDE the wavetable osc** (the Episode 1 bridge). Position held fixed; sweep FM Amount and hear sidebands grow.

> ⚠ **PARTIAL HAND-BUILD — the Osc Effect MODE is NOT settable over our headless path.**
> Set **Osc 1's effect mode to FM** in Live by hand (the four-mode selector: None / FM / Classic / Modern). The two **Effect knobs** ARE settable, so once the device is in FM mode, `Osc 1 Effect 1` (Amount) and `Osc 1 Effect 2` (Tune) drive the sound.

Build from a **freshly loaded default Wavetable.** Position on the **0–1 LOM scale**.

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | — | Load default Wavetable | init | Neutral saw per note |
| 1 | Osc 1 | Table / Category | default (Basic Shapes) | ⚠ Table not settable headless — confirm by hand. |
| 2 | Osc 1 | Osc 1 On | On (1) | Osc 1 sounding |
| 3 | Osc 1 | Osc 1 Pos | 0.3 (FIXED — not the variable) | A steady wavetable tone |
| 4 | Osc 1 | Osc 1 Detune | 0.5 (0 cents) | Single clean voice |
| 5 | Osc 1 | Osc 1 Gain | 1.0 (unity) | Full level |
| 6 | Osc 1 | **Osc 1 Effect Mode** | **FM** | ⚠ **Set in Live by hand (not settable over our headless path).** Selects the hidden-sine FM modulator. |
| 7 | Osc 1 | Osc 1 Effect 1 (FM Amount) | 0.0 (start) | No FM yet — the bare wavetable tone |
| 8 | Osc 1 | Osc 1 Effect 2 (FM Tune) | 0.0 (modulator at osc pitch) | Modulator tuned to the oscillator |
| 9 | Osc 2 | Osc 2 On | Off (0) | Osc 1 only |
| 10 | Sub | Sub On | Off (0) | No sub |
| 11 | Filter 1 | Flt 1 On | On (1) | Filter in path |
| 12 | Filter 1 | Flt 1 Type | 0 (Clean) | Transparent circuit |
| 13 | Filter 1 | Flt 1 LP/HP | 0 (Lowpass) | Lowpass mode |
| 14 | Filter 1 | Flt 1 Freq | 1.0 (open) | Full brightness — FM sidebands pass |
| 15 | Filter 1 | Flt 1 Res | 0.0 | No resonance |
| 16 | Filter 2 | Flt 2 On | Off (0) | Single filter |
| 17 | Amp Env | Amp Attack | 0.05 | Fast attack |
| 18 | Amp Env | Amp Sustain | 1.0 | Holds full level |
| 19 | Amp Env | Amp Release | 0.15 | Short tail |

**The demonstrative move (sweep):**
Hold **C3** for ~4.7 s and sweep **Osc 1 Effect 1 (FM Amount) 0.0 → 0.85** over ~4.3 s. Position stays fixed at 0.3. You should hear the bare tone open into a metallic, sideband-rich buzz — harmonics **grown, not scanned**.

Final check: pitch/loudness roughly constant; centroid / inharmonic content rises monotonically. Flat centroid ⇒ FM Amount didn't engage or the mode wasn't FM ⇒ reject.

**Save:** right-click Wavetable → **Save Preset** → `presets/wt-fm-inside-wavetable.adv`. **Set Effect Mode = FM in Live before saving** (save with Effect 1 = 0.0, the sweep start).

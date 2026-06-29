# Patch: User-Table-Scan (Plaid Polymer method)  (preset: presets/wt-user-table-scan.adv)

Concept demonstrated: **user-imported wavetable + Env/LFO → Position → scanning your OWN source as texture.**

> ⚠ **DOUBLE HAND-BUILD — neither the import nor the Env→Position routing is settable over our headless path.**
> (1) **Import a user wavetable** by dragging an audio file onto Osc 1's sprite area in Live (step 1) — Live reads up to 256 frames. Use a neutral, non-copyrighted source (a sung vowel, a field recording, or a resampled Operator FM patch). (2) Build the **Env 2 → Osc 1 Pos** matrix row by hand (step 16). `Env 2` shape IS settable; its routing to Position is not. Headless renders the scan by automating `Osc 1 Pos` 0 → 1 directly (a long ramp ≈ the slow Env 2).

Build from a **freshly loaded default Wavetable.** Position on the **0–1 LOM scale**.

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | — | Load default Wavetable | init | Neutral saw per note |
| 1 | Osc 1 | **Table (user import)** | **drag your WAV onto the sprite** | ⚠ **Set in Live by hand (not settable over our headless path).** Your own source, framed. |
| 2 | Osc 1 | Osc 1 On | On (1) | Osc 1 sounding |
| 3 | Osc 1 | Osc 1 Pos | 0.0 (scanned by automation) | The first frame of your source |
| 4 | Osc 1 | Osc 1 Detune | 0.5 (0 cents) | Single clean voice |
| 5 | Osc 1 | Osc 1 Gain | 1.0 (unity) | Full level |
| 6 | Osc 2 | Osc 2 On | Off (0) | Osc 1 only |
| 7 | Sub | Sub On | Off (0) | No sub |
| 8 | Filter 1 | Flt 1 On | On (1) | Filter in path |
| 9 | Filter 1 | Flt 1 Type | 0 (Clean) | Transparent circuit |
| 10 | Filter 1 | Flt 1 LP/HP | 0 (Lowpass) | Lowpass mode |
| 11 | Filter 1 | Flt 1 Freq | 0.95 | Nearly open |
| 12 | Filter 1 | Flt 1 Res | 0.1 | A touch of resonance |
| 13 | Filter 2 | Flt 2 On | Off (0) | Single filter |
| 14 | Amp Env | Amp Attack / Sustain / Release | 0.05 / 1.0 / 0.2 | Fast attack, full hold |
| 15 | Env 2 | Env 2 Attack / Decay / Sustain / Release | 0.7 (slow) / 0.0 / 1.0 / 0.2 | A long slow rise (drives the scan) |
| 16 | Matrix | **Env 2 → Osc 1 Pos** | amount **90** | ⚠ **Set in Live by hand (not creatable over our headless path).** Env scans Position across the held note. |

**The demonstrative move (sweep):**
Hold **C3** for ~5.7 s. The tone morphs across the held note as Env 2 scans Position 0 → 1 — your own sound moving, not a factory table. (Headless proxy: `Osc 1 Pos` slow ramp 0 → 1 over ~5.3 s.)

Final check: spectral content evolves monotonically; the source spectrum is distinct from factory Basic Shapes.

**Save:** right-click Wavetable → **Save Preset** → `presets/wt-user-table-scan.adv`. **Import your source WAV onto Osc 1 and build the Env 2 → Osc 1 Pos row in Live before saving** (document the source file name in the preset comment — the imported sprite travels with the .adv).

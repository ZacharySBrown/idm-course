# Patch: MPE-Pressure-Position  (preset: presets/wt-mpe-pressure-position.adv)

Concept demonstrated: **MPE Pressure → Position → per-note timbre scanned by finger pressure.**

> ⚠ **PARTIAL HAND-BUILD — MPE enable, the Pressure source, and the matrix routing are NOT settable over our headless path.**
> In Live, **enable MPE** on the track and build the **Pressure → Osc 1 Pos** matrix row by hand (step 14). Per-note MPE pressure is also not emitted by our renderer. Headless renders the IDENTICAL audible *ladder* (three same pitches, rising brightness) by stepping `Osc 1 Pos` 0.1 / 0.45 / 0.8 at each note onset — it proves the brightness ladder, **not** MPE per-voice independence (that needs a hand demo on an MPE controller).

Build from a **freshly loaded default Wavetable.** Position on the **0–1 LOM scale**.

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | — | Load default Wavetable | init | Neutral saw per note |
| 1 | Osc 1 | Table / Category | default (Basic Shapes) | ⚠ Table not settable headless — confirm by hand. |
| 2 | Osc 1 | Osc 1 On | On (1) | Osc 1 sounding |
| 3 | Osc 1 | Osc 1 Pos | 0.1 (note-1 base; scanned by Pressure) | A dark, near-sine tone |
| 4 | Osc 1 | Osc 1 Detune | 0.5 (0 cents) | Single clean voice |
| 5 | Osc 1 | Osc 1 Gain | 1.0 (unity) | Full level |
| 6 | Osc 2 | Osc 2 On | Off (0) | Osc 1 only |
| 7 | Sub | Sub On | Off (0) | No sub |
| 8 | Filter 1 | Flt 1 On | On (1) | Filter in path |
| 9 | Filter 1 | Flt 1 Type | 0 (Clean) | Transparent circuit |
| 10 | Filter 1 | Flt 1 LP/HP | 0 (Lowpass) | Lowpass mode |
| 11 | Filter 1 | Flt 1 Freq | 0.95 | Nearly open |
| 12 | Filter 1 | Flt 1 Res | 0.05 | Barely any resonance |
| 13 | Filter 2 | Flt 2 On | Off (0) | Single filter |
| 14 | Amp Env | Amp Attack / Sustain / Release | 0.05 / 1.0 / 0.15 | Fast attack, full hold |
| 15 | Matrix | **Pressure → Osc 1 Pos** | amount **80** (MPE enabled) | ⚠ **Set in Live by hand (MPE + matrix not settable over our headless path).** Finger pressure now scans Position per note. |

**The demonstrative move (ladder):**
Play **C3** three times (~1.6 s each), increasing per-note Pressure each time. On an MPE controller, each note's brightness rises independently with finger pressure. (Headless proxy: `Osc 1 Pos` stepped 0.1 → 0.45 → 0.8 at the three note onsets — a per-note brightness ladder.)

Final check: three identical pitches at rising brightness; centroid increases monotonically (low < mid < high). Equal across notes ⇒ the Pos steps didn't take ⇒ reject. (Proves the ladder; note on-mic that true per-voice MPE independence needs a hand demo.)

**Save:** right-click Wavetable → **Save Preset** → `presets/wt-mpe-pressure-position.adv`. **Enable MPE and build the Pressure → Osc 1 Pos row in Live before saving.**

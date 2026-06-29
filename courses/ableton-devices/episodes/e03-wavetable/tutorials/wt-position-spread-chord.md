# Patch: Position-Spread-Chord  (preset: presets/wt-position-spread-chord.adv)

Concept demonstrated: **Position Spread unison → each voice at a different Position = a chord of timbres from ONE note.**

> ⚠ **PARTIAL HAND-BUILD — Unison MODE and Voices are NOT settable over our headless path.**
> Only **Unison Amount** is settable; the **Unison = Position Spread** mode and the voice count are not. In Live, **set Unison Mode = Position Spread (4 voices) by hand** (step 17) — without it, the A/B reads as detune width only, not a chord of timbres. Our headless render toggles `Unison Amount` 0 → 0.3 for the A/B.

Build from a **freshly loaded default Wavetable.** Position on the **0–1 LOM scale**.

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | — | Load default Wavetable | init | Neutral saw per note |
| 1 | Osc 1 | Table / Category | default (Basic Shapes) | ⚠ Table not settable headless — confirm by hand. |
| 2 | Osc 1 | Osc 1 On | On (1) | Osc 1 sounding |
| 3 | Osc 1 | Osc 1 Pos | 0.5 (mid table) | A steady mid-table tone |
| 4 | Osc 1 | Osc 1 Detune | 0.5 (0 cents) | Single clean voice |
| 5 | Osc 1 | Osc 1 Gain | 1.0 (unity) | Full level |
| 6 | Osc 2 | Osc 2 On | Off (0) | Osc 1 only |
| 7 | Sub | Sub On | Off (0) | No sub |
| 8 | Filter 1 | Flt 1 On | On (1) | Filter in path |
| 9 | Filter 1 | Flt 1 Type | 1 (OSR) | Characterful lowpass |
| 10 | Filter 1 | Flt 1 LP/HP | 0 (Lowpass) | Lowpass mode |
| 11 | Filter 1 | Flt 1 Freq | 0.85 | Gently shaded top |
| 12 | Filter 1 | Flt 1 Res | 0.1 | A touch of resonance |
| 13 | Filter 2 | Flt 2 On | Off (0) | Single filter |
| 14 | Amp Env | Amp Attack | 0.1 | Soft attack |
| 15 | Amp Env | Amp Sustain | 1.0 | Holds full level |
| 16 | Amp Env | Amp Release | 0.3 | Soft tail |
| 17 | Unison | **Unison Mode / Voices** | **Position Spread, 4 voices** | ⚠ **Set in Live by hand (not settable over our headless path).** Each voice sits at a different table position. |
| 18 | Unison | Unison Amount | A = 0.0, B = 0.3 | A = one voice; B = voices spread across positions (a chord of timbres) |

**The demonstrative move (A/B):**
- **Segment A:** play **C3** (~2 s) with **Unison Amount = 0.0** — one voice, one timbre.
- Beat of silence.
- **Segment B:** play **C3** (~2 s) with **Unison Amount = 0.3** and **Unison = Position Spread** — a stack of distinct timbres ringing together.

Final check: same pitch both segments; B audibly wider and richer. A ≈ B ⇒ reject. (Headless A/B proves width; the true chord-of-timbres needs the hand-set Position Spread mode.)

**Save:** right-click Wavetable → **Save Preset** → `presets/wt-position-spread-chord.adv`. **Set Unison = Position Spread (4 voices) in Live before saving** (save with Unison Amount = 0.0, the segment-A value).

# Patch: Rain/Crackle + Sub (Environmental Oscillator as Source)  (preset: presets/meld-rain-crackle-sub.adv)

**Demo:** `meld-rain-crackle-sub`  ·  **Slide:** `06b-environmental-osc`  ·  **Structure:** single
**Concept demonstrated:** a synthesized environmental oscillator (Rain) is the SOURCE, not an effect — evolving weather from a held note, over a quiet Sub for body.
**Render status:** RENDERABLE headless with a WORKING fallback. The true tutorial evolution comes from a Loop Mod Env → Rain Rate (matrix, hand-build), but sweeping the Rate macro (`A Osc Tone`) DIRECTLY also genuinely evolves Rain's broadband content — so the rendered fallback DOES produce evolving weather. The matrix block below is the looping-tutorial version.

Build from a **freshly loaded default Meld**. One parameter per step. Engine A = Rain (the source), Engine B = Sub (the body).

### Engine A — Rain (the source)
| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | — | Load default Meld | init | A plain tone on each note |
| 1 | Engine A | `A On` | On (1) | Engine A present |
| 2 | Engine A | `A Osc Type` | **12 = Rain** | A synthesized rain/weather texture (drops + wind) — not a sample |
| 3 | Engine A | `A Osc Shape` (macro 1 = Tone) | 0.50 | A balanced weather tone |
| 4 | Engine A | `A Osc Tone` (macro 2 = Rate) | 0.40 (start of the evolution sweep) | A moderate density of drops at the start |
| 5 | Engine A | `A Filter On` | On (1) | (routing) |
| 6 | Engine A | `A Filter Type` | **0 = Analog** | Transparent filter |
| 7 | Engine A | `A Filter L-B-H-N` | 0.0 (lowpass) | Lowpass response |
| 8 | Engine A | `A Filter Freq` | 0.70 | A gently tamed top |
| 9 | Engine A (Mod Env) | `A Mod Loop Mode` | **1 = Loop (PLACEHOLDER — CONFIRM; hand-build only)** | (arms the loop env for the tutorial matrix version) |
| 10 | Engine A (Mod Env) | `A Mod Attack` | 0.50 | (slow rise per loop cycle) |
| 11 | Engine A (Mod Env) | `A Mod Decay` | 1.0 | (long, slow evolution period) |
| 12 | Engine A | `A Amp Attack` | 0.30 | A gentle fade-in |
| 13 | Engine A | `A Amp Sustain` | 1.0 | Holds at full level |
| 14 | Engine A | `A Amp Release` | 0.50 | A soft tail |
| 15 | Engine A | `A Volume` | 0.70 | Solid weather level |

### Engine B — Sub (quiet body)
| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 16 | Engine B | `B On` | On (1) | A low sub joins under the weather |
| 17 | Engine B | `B Osc Type` | **18 = Sub** | A clean low fundamental |
| 18 | Engine B | `B Osc Shape` (macro 1 = Tone) | 0.30 | A round sub tone |
| 19 | Engine B | `B Osc Tone` (macro 2 = Aux) | 0.20 | A minimal aux character |
| 20 | Engine B | `B Filter On` / `B Filter Type` / `B Filter L-B-H-N` | On / **0 = Analog** / 0.0 | Lowpass on the sub |
| 21 | Engine B | `B Filter Freq` | 0.40 | A dark, tight sub |
| 22 | Engine B | `B Volume` | 0.40 | A quiet body under the weather |

### Evolution — two ways
- **Rendered fallback (WORKS):** hold `C2`; sweep `A Osc Tone` (Rain Rate) 0.20 → 0.80 over ~7 s. Rain's broadband content genuinely evolves as Rate climbs.
- **Tutorial / .adv (looping) version — HAND-BUILD the matrix route:** in the **Matrix** tab, add `A Mod Env → A Osc Tone` (Rain Rate) at **+0.7**, with the Loop Mod Env (steps 9–11). This loops the evolution instead of a single sweep.

| Source | Destination | Amount |
|---|---|---|
| `A Mod Env` (Loop) | `A Osc Tone` (Rain Rate) | **+0.7** |

**Play:** one held note `C2` for ~7.6 s.

**Final check:** a clearly synthesized rain/weather texture (not a sample) that evolves over the hold, with a low sub body underneath.
**Analyzer:** broadband stochastic "rain" content evolving over time + a low sub fundamental from Engine B.

**Save:** with the Loop matrix route built (the tutorial version), right-click Meld → **Save Preset** → `presets/meld-rain-crackle-sub.adv`.

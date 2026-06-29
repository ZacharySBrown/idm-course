# Patch: Two-Hands — Step 4: Self-Morph (Mod Env AD-Loop)  (preset: presets/meld-twohands-step4.adv)

**Demo:** `meld-twohands-step4`  ·  **Slide:** `05d-self-morph-loop-env`  ·  **Structure:** single (build-step)
**Concept demonstrated:** Step 4 — self-morph: Engine A Mod Env in AD Loop → A's Macro 1. The saw body sequences itself on held notes — the seam to the IDM act.

> ## ⚠ THIS DEMO IS BUILT BY HAND — IT CANNOT BE RENDERED OVER OUR HEADLESS PATH.
> Both routes here (`A LFO 1 → B Osc Shape` carried from Step 3, and `A Mod Env → A Osc Shape` new
> this step) are **modulation-matrix** entries, **not in Meld's LOM param map**. The manifest's
> single-ramp `automation:` FALLBACK morphs A's Osc Shape once and will NOT pass the `self-sequence`
> recurrence assertion. **Hand-build both routes in the live device.**

**⚠ PLACEHOLDER ENUM INDICES — CONFIRM LIVE:** `B Filter Type` Plate Resonator = **15**; `A Mod Loop Mode` AD Loop = **2** (quantized 0–3, EMPTY value_items, order uncertain).

Re-state Engine A + B as Step 3, then add the Mod Env AD-Loop and the self-morph route.

### Engine A (as Step 3) + Mod Env
| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 1 | Engine A | `A On` / `A Osc Type` | On / **19 = Swarm Saw** | The in-key saw body |
| 2 | Engine A | `A Osc Shape` (Motion) | 0.40 (center the AD-Loop env modulates) | A mid-bright body — the loop's center |
| 3 | Engine A | `A Osc Tone` (Spacing) | 0.40 | Medium spread |
| 4 | Engine A | `A Osc Scale Aware` | On (1) | In-key |
| 5 | Engine A | `A Filter On` / `A Filter Type` / `A Filter L-B-H-N` | On / **0 = Analog** / 0.0 | Warm low-pass |
| 6 | Engine A | `A Filter Freq` | 0.55 | Gentle low-pass |
| 7 | Engine A (LFO 1) | `A LFO 1 Type` / `A LFO 1 Rate` | 0 / 0.25 (normalized, slow) | (LFO for the cross-engine route) |
| 8 | Engine A (Mod Env) | `A Mod Loop Mode` | **2 = AD Loop (PLACEHOLDER — CONFIRM)** | The Mod Env cycles (no audible change yet — needs the route) |
| 9 | Engine A (Mod Env) | `A Mod Attack` | 0.20 | (rise of each loop cycle) |
| 10 | Engine A (Mod Env) | `A Mod Decay` | 0.60 | (the self-morph period) |
| 11 | Engine A | `A Volume` | 0.65 | Chord-level body |

### Engine B (as Step 3)
| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 12 | Engine B | `B On` / `B Osc Type` | On / **9 = Harmonic FM** | The glassy FM layer |
| 13 | Engine B | `B Octave` | **1** | An octave up |
| 14 | Engine B | `B Filter On` / `B Filter Type` | On / **Plate Resonator (idx 15 PLACEHOLDER — CONFIRM)** | A struck resonant shimmer |
| 15 | Engine B | `B Filter Filter Scale Aware` | On (1) | Modes in key |
| 16 | Engine B | `B Volume` | 0.40 | A layer under the body |
| 17 | Global | `Scale Aware` | On (1) | Master scale-snap on |

### HAND-BUILD: the matrix routes (this is what makes Step 4 work)
In the live device's **Matrix** tab:

| Source | Destination | Amount | Note |
|---|---|---|---|
| `A LFO 1` | `B Osc Shape` | **+0.6** | carried from Step 3 (cross-engine) |
| `A Mod Env` | `A Osc Shape` | **+0.7** | NEW this step — the AD-Loop self-morph |

On a single held chord, A's body now cyclically morphs (the AD-Loop envelope), recurring on a steady period.

**Play:** hold `C3 + G3` for ~4.6 s — no new notes.

**Final check:** on a single held chord, A's body cyclically morphs (the AD-Loop envelope), recurring on a steady period.
**Analyzer:** A's centroid shows a repeating AD-Loop contour from one held note.

**Save:** with both routes built, right-click Meld → **Save Preset** → `presets/meld-twohands-step4.adv`.

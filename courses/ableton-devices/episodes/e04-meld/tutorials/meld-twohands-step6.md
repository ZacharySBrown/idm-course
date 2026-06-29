# Patch: Two-Hands — Step 6: Global Glue  (preset: presets/meld-twohands-step6.adv)

**Demo:** `meld-twohands-step6`  ·  **Slide:** `05f-drive-limiter-spread`  ·  **Structure:** single (build-step)
**Concept demonstrated:** Step 6 — global glue: Drive, Limiter, and Voice Spread for width. The finished patch widens and thickens; same notes.
**Render status:** the global Drive / Limiter / Voice Spread ARE renderable params, so the build-step contrast vs Step 5 (width + saturation) IS provable headless. The matrix/MPE routes below are carried as hand-build only.
**Myth-bust note:** there is **NO "Stacked Voices" param** in Meld's LOM map (the slide heading says "Stacked Voices" but the device has no such control). The width here comes from `Voice Spread`. Do not narrate "Stacked Voices."

**⚠ PLACEHOLDER ENUM INDICES — CONFIRM LIVE:** `B Filter Type` Plate Resonator = **15**; `A Mod Loop Mode` AD Loop = **2**.

Re-state the Step-5 patch, then add the global glue.

### Engine A + B (as Step 5)
| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 1 | Engine A | `A On` / `A Osc Type` | On / **19 = Swarm Saw** | The in-key saw body |
| 2 | Engine A | `A Osc Scale Aware` | On (1) | In-key |
| 3 | Engine A | `A Filter On` / `A Filter Type` / `A Filter L-B-H-N` | On / **0 = Analog** / 0.0 | Warm low-pass |
| 4 | Engine A | `A Filter Freq` | 0.55 | Gentle low-pass |
| 5 | Engine A (Mod Env) | `A Mod Loop Mode` | **2 = AD Loop (PLACEHOLDER — CONFIRM)** | The self-morph loop |
| 6 | Engine A | `A Volume` | 0.65 | Chord-level body |
| 7 | Engine B | `B On` / `B Osc Type` | On / **9 = Harmonic FM** | The glassy FM layer |
| 8 | Engine B | `B Octave` | **1** | An octave up |
| 9 | Engine B | `B Filter On` / `B Filter Type` | On / **Plate Resonator (idx 15 PLACEHOLDER — CONFIRM)** | A struck resonant shimmer |
| 10 | Engine B | `B Volume` | 0.40 | A layer under the body |

### Global glue — the added element (RENDERABLE)
| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 11 | Global | `Drive` | 0.25 | The whole patch thickens with a touch of saturation |
| 12 | Global | `Limiter On` | On (1) | Peaks caught — the patch holds together loud |
| 13 | Global | `Voice Spread` | 0.30 | A small unison/per-note width — the patch widens |
| 14 | Global | `Scale Aware` | On (1) | Master scale-snap on |

### HAND-BUILD: matrix routes carried from Step 5 (not renderable)
In the live device's **Matrix** tab (carried, for the `.adv`):

| Source | Destination | Amount |
|---|---|---|
| `A LFO 1` | `B Osc Shape` | +0.6 |
| `A Mod Env` | `A Osc Shape` | +0.7 |
| `MPE Press` | `B Osc Shape` | +0.7 |
| `MPE Slide` | `A Filter Freq` | +0.5 |

**Play:** hold `C3 + G3` for ~4.6 s.

**Final check:** same patch as Step 5, now wider (Spread) and thicker (Drive); differs from Step 5 only by the global glue.
**Analyzer:** increased stereo width + saturation harmonics vs Step 5; no narrowing.

**Save:** right-click Meld → **Save Preset** → `presets/meld-twohands-step6.adv`.

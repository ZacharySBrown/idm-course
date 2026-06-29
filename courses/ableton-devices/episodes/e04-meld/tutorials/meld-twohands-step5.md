# Patch: Two-Hands — Step 5: Wire the Fingers In (MPE)  (preset: presets/meld-twohands-step5.adv)

**Demo:** `meld-twohands-step5`  ·  **Slide:** `05e-mpe-routing`  ·  **Structure:** single (build-step)
**Concept demonstrated:** Step 5 — wire the fingers in: MPE Press → B's FM Amount, Slide → A's filter, Note Bend → A detune. The step the whole patch exists to reach.

> ## ⚠ THIS DEMO IS PLAYED BY HAND ON AN MPE CONTROLLER — IT CANNOT BE RENDERED OVER OUR HEADLESS PATH.
> Needs per-note MPE expression (not authorable over our clip path) AND modulation-matrix routes
> (not in Meld's LOM param map). A static render makes sound but proves no per-voice behavior.
> Perform on an **MPE controller** (Push 3 / Seaboard / LinnStrument).

**⚠ PLACEHOLDER ENUM INDICES — CONFIRM LIVE:** `B Filter Type` Plate Resonator = **15**; `A Mod Loop Mode` AD Loop = **2**.

Re-state Engine A + B as Step 4, then add the three MPE matrix routes.

### Engine A (as Step 4)
| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 1 | Engine A | `A On` / `A Osc Type` | On / **19 = Swarm Saw** | The in-key saw body |
| 2 | Engine A | `A Osc Shape` (Motion) | 0.40 | Mid-bright body |
| 3 | Engine A | `A Osc Scale Aware` | On (1) | In-key |
| 4 | Engine A | `A Filter On` / `A Filter Type` / `A Filter L-B-H-N` | On / **0 = Analog** / 0.0 | Warm low-pass |
| 5 | Engine A | `A Filter Freq` | 0.50 (base cutoff — raised per-note by Slide over MPE) | A half-open body at rest |
| 6 | Engine A (Mod Env) | `A Mod Loop Mode` | **2 = AD Loop (PLACEHOLDER — CONFIRM)** | The self-morph loop (from Step 4) |
| 7 | Engine A | `A Volume` | 0.65 | Chord-level body |

### Engine B (as Step 4)
| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 8 | Engine B | `B On` / `B Osc Type` | On / **9 = Harmonic FM** | The glassy FM layer |
| 9 | Engine B | `B Osc Shape` (FM Amount) | 0.30 (base — raised per-note by Press over MPE) | A modest FM brightness at rest |
| 10 | Engine B | `B Octave` | **1** | An octave up |
| 11 | Engine B | `B Filter On` / `B Filter Type` | On / **Plate Resonator (idx 15 PLACEHOLDER — CONFIRM)** | A struck resonant shimmer |
| 12 | Engine B | `B Volume` | 0.40 | A layer under the body |
| 13 | Global | `Scale Aware` | On (1) | Master scale-snap on |

### HAND-BUILD: the full matrix (carried routes + the three new MPE routes)
In the live device's **Matrix** tab:

| Source | Destination | Amount | Note |
|---|---|---|---|
| `A LFO 1` | `B Osc Shape` | **+0.6** | carried (Step 3) |
| `A Mod Env` | `A Osc Shape` | **+0.7** | carried (Step 4) |
| `MPE Press` | `B Osc Shape` (FM Amount) | **+0.7** | NEW — pressure brightens the FM layer |
| `MPE Slide` | `A Filter Freq` (cutoff) | **+0.5** | NEW — slide opens the body filter |
| `MPE Note Bend` | `A Detune` | **+0.3** | NEW — per-note bend detunes the body |

### THE MPE GESTURE TO PERFORM
Hold two notes (`C3` + `G3`). On `C3`, **press harder and slide up** over the hold (ramp Press 0→0.9, Slide 0.2→0.8); keep `G3` near steady (Press ~0.3, Slide ~0.4). The pressed/slid note morphs more than the held-steady note — per-voice expression is audible.

**Final check:** the pressed/slid note morphs more than the held-steady note — per-voice expression is audible.
**Analyzer:** the expressed voice's centroid moves with Press/Slide; the steady voice moves less.

**Save:** with all five matrix routes built, right-click Meld → **Save Preset** → `presets/meld-twohands-step5.adv`.

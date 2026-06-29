# Patch: Two-Hands — Final (Save the Patch)  (preset: presets/meld-twohands-final.adv)

**Demo:** `meld-twohands-final`  ·  **Slide:** `05g-save`  ·  **Structure:** single (capstone)
**Concept demonstrated:** the finished "Two-Hands" patch — two engines, ten fingers — played as a short MPE phrase. No new variable; the capstone playthrough.

> ## ⚠ THIS DEMO IS PLAYED BY HAND ON AN MPE CONTROLLER — IT CANNOT FULLY RENDER OVER OUR HEADLESS PATH.
> The capstone is an **MPE phrase** (per-note expression) over the **full modulation matrix**. Both
> are out of reach of our clip path. Perform it from the saved "Two-Hands" `.adv` on an MPE
> controller (Push 3 / Seaboard / LinnStrument). A static-phrase render proves layering/timbre but
> NOT the MPE/matrix motion.

**⚠ PLACEHOLDER ENUM INDICES — CONFIRM LIVE:** `B Filter Type` Plate Resonator = **15**; `A Mod Loop Mode` AD Loop = **2**.

This is Step 6 plus the full matrix — the complete patch. Re-state it once for the saved preset.

### The complete "Two-Hands" patch
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
| 11 | Global | `Drive` | 0.25 | Saturation glue |
| 12 | Global | `Limiter On` | On (1) | Peaks caught |
| 13 | Global | `Voice Spread` | 0.30 | Stereo width |
| 14 | Global | `Scale Aware` | On (1) | Master scale-snap on |

### HAND-BUILD: the full matrix (the complete routing)
In the live device's **Matrix** tab:

| Source | Destination | Amount |
|---|---|---|
| `A LFO 1` | `B Osc Shape` | +0.6 |
| `A Mod Env` | `A Osc Shape` | +0.7 |
| `MPE Press` | `B Osc Shape` | +0.7 |
| `MPE Slide` | `A Filter Freq` | +0.5 |
| `MPE Note Bend` | `A Detune` | +0.3 |

### THE MPE PHRASE TO PERFORM
Play a ~4-bar Cm texture-lead phrase at ~90 BPM, with per-note Press/Slide expression on each note — shape each note's timbre, brightness, and pitch with your fingers.

**Final check:** all elements present and balanced; reads as one coherent instrument, not a pile of layers.
**Analyzer:** saw-swarm body + octave-up modal-resonant FM layer + AD-Loop morph + per-note MPE motion all present.

**Save:** this is THE patch the episode names — right-click Meld → **Save Preset** → `presets/meld-twohands-final.adv` (also reachable in-app as the user-saved **"Two-Hands"** preset).

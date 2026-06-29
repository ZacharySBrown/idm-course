# Patch: Swarm Scale-Snap  (preset: presets/meld-swarm-scale-snap.adv)

**Demo:** `meld-swarm-scale-snap`  ·  **Slide:** `03d-scale-aware`  ·  **Structure:** ab
**Concept demonstrated:** scale-aware oscillators snap their inharmonic spread to the Live Scale — a wide swarm stays in key.
**Render status:** RENDERABLE headless (A/B split render on `A Osc Scale Aware` = 0 vs 1). No matrix, no MPE.
**Orchestrator note:** the scale the partials snap to is a **Live-set / clip property**, NOT a Meld param. Set the Set's Scale (e.g. C Minor) before render. The device-global `Scale Aware` (master enable) and per-osc `A Osc Scale Aware` are the two toggles below.

Build from a **freshly loaded default Meld**. One parameter per step.

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | — | Load default Meld | init | A plain tone on each note |
| 1 | Engine B | `B On` | Off (0) | Engine B silent |
| 2 | Engine A | `A On` | On (1) | Engine A only |
| 3 | Engine A | `A Osc Type` | **20 = Swarm Sine** (scale-aware type, marked ♭♯) | A detuned swarm of sines on each note |
| 4 | Engine A | `A Osc Shape` (macro 1 = Motion) | 0.30 | A gentle internal motion in the swarm |
| 5 | Engine A | `A Osc Tone` (macro 2 = Spacing) | 0.70 (wide) | A wide spread — so the snap is obvious |
| 6 | Engine A | `A Osc Scale Aware` | On (1) (segment B value; A = 0) | (the per-osc toggle the A/B switches) |
| 7 | Engine A | `A Transpose` | 0 | (no offset) |
| 8 | Engine A | `A Detune` | 0.50 (0 cents) | Centered tuning |
| 9 | Engine A | `A Filter On` | On (1) | (routing) |
| 10 | Engine A | `A Filter Type` | **0 = Analog** | Transparent filter |
| 11 | Engine A | `A Filter L-B-H-N` | 0.0 (lowpass) | Lowpass response |
| 12 | Engine A | `A Filter Freq` | 1.0 (open) | Uncolored |
| 13 | Engine A | `A Filter Q` | 0.0 | No resonance |
| 14 | Engine A | `A Amp Attack` | 0.05 | Fast note start |
| 15 | Engine A | `A Amp Sustain` | 1.0 | Holds at full level |
| 16 | Engine A | `A Amp Release` | 0.30 | Short tail |
| 17 | Engine A | `A Volume` | 0.65 | Chord level with headroom |
| 18 | Global | `Scale Aware` (device master enable) | On (1) | (master scale-snap enabled; per-osc toggle decides the audible A/B) |

**Set-level prep:** set the Live Set's Scale to **C Minor** (or your chosen scale) before rendering.

**A/B (hold the chord `C3 + E3 + G3` each, beat of silence between):**
- **A:** `A Osc Scale Aware` = **0 (OFF)** — the wide spread smears inharmonically at the edges.
- **B:** `A Osc Scale Aware` = **1 (ON)** — the same spread snaps into key.

**Final check:** same chord both segments; A sounds smeared/detuned at the edges, B sounds locked in key.
**Analyzer:** segment B's swarm partials cluster on scale-degree frequencies; segment A's spread is inharmonic/unquantized.

**Save:** save with `A Osc Scale Aware` = ON (the in-key state) → right-click Meld → **Save Preset** → `presets/meld-swarm-scale-snap.adv`.

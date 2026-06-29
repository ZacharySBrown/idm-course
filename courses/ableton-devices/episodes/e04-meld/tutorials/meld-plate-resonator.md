# Patch: Plate Resonator  (preset: presets/meld-plate-resonator.adv)

**Demo:** `meld-plate-resonator`  ·  **Slide:** `03c-modal-resonators`  ·  **Structure:** ab
**Concept demonstrated:** the only "physical modelling" in Meld is a FILTER — a modal Plate Resonator on the oscillator output, not the oscillator itself. ("It's a filter, not the oscillator.")
**Render status:** RENDERABLE headless (A/B split render on `A Filter Type` = 0 vs Plate Resonator). No matrix, no MPE.
**⚠ PLACEHOLDER ENUM INDEX — NEEDS LIVE CONFIRMATION:** `A Filter Type` returns EMPTY value_items over LOM and no public doc gives the 0–16 ordering. The **Plate Resonator index is a PLACEHOLDER = 15**. Read the live filter-type list and correct it before render/save.

Build from a **freshly loaded default Meld**. One parameter per step.

| # | Panel | Parameter | Value | You should now hear |
|---|---|---|---|---|
| 0 | — | Load default Meld | init | A plain tone on each note |
| 1 | Engine B | `B On` | Off (0) | Engine B silent |
| 2 | Engine A | `A On` | On (1) | Engine A only |
| 3 | Engine A | `A Osc Type` | **9 = Harmonic FM** | A bright FM source — rich enough to excite the modes |
| 4 | Engine A | `A Osc Shape` (macro 1 = FM Amount) | 0.55 | A bright, harmonically dense source |
| 5 | Engine A | `A Osc Tone` (macro 2 = FM Ratio) | 0.40 | A metallic ratio in the source |
| 6 | Engine A | `A Transpose` | 0 | (no offset) |
| 7 | Engine A | `A Detune` | 0.50 (0 cents) | Centered tuning |
| 8 | Engine A | `A Filter On` | On (1) | (routing) |
| 9 | Engine A | `A Filter Type` | **0 = Analog** (segment A — the dry source) | The raw bright oscillator, no modal character |
| 10 | Engine A | `A Filter Filter Scale Aware` | On (1) | (arms scale-snap of the modal frequencies for segment B) |
| 11 | Engine A | `A Filter Freq` | 0.50 (resonator structure/pitch macro) | (sets resonator pitch when engaged) |
| 12 | Engine A | `A Filter Q` | 0.50 (resonator decay/sharpness) | (sets ring time when engaged) |
| 13 | Engine A | `A Amp Attack` | 0.02 | A sharp, struck attack |
| 14 | Engine A | `A Amp Decay` | 0.50 | A decaying pluck shape |
| 15 | Engine A | `A Amp Sustain` | 0.30 | Drops to a low sustain — pluck-like |
| 16 | Engine A | `A Amp Release` | 0.40 | A short ring-out |
| 17 | Engine A | `A Volume` | 0.70 | Solid level |

**A/B (hold `C3` each, beat of silence between):**
- **A:** `A Filter Type` = **0 = Analog** (transparent — the dry source).
- **B:** `A Filter Type` = **Plate Resonator (PLACEHOLDER idx 15 — CONFIRM LIVE)** — a struck, body-resonant, pluck-like tone appears.

**Final check:** same pitch both segments; B gains a struck, ringing, body-resonant character absent in A.
**Analyzer:** segment B shows discrete modal resonance peaks (plate modes) NOT present in A's smoother spectrum.

**Save:** save with `A Filter Type` set to the **confirmed Plate Resonator index** (this is the demonstrative state) → right-click Meld → **Save Preset** → `presets/meld-plate-resonator.adv`.

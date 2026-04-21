# Using it for an in-track beat switch — the step-by-step

- Goal: switch the bass timbre at bar 33 without leaving Arrangement View. One MIDI track, one Rack, one automation lane.
- **Recipe:**
  1. Create an Instrument Rack on a MIDI track. Three chains: **A** — clean saw sub (Operator, Algorithm 1, 2 ops). **B** — FM growl (Operator, Algorithm 4, 4 ops with a −12 ratio). **C** — bit-crushed square (Analog Saw + Redux at 8-bit).
  2. Set zones: A at 0–42, B at 43–85, C at 86–127. Zero-width fades on all zones.
  3. Map Chain Selector to Macro 1 on the Rack.
  4. Store **Variation "Verse A"** — Macro 1 = 20 (chain A active), all other macros default.
  5. Store **Variation "Switch B"** — Macro 1 = 64 (chain B active), filter macro open 80%.
  6. In Arrangement, draw an automation envelope on Macro 1. At bar 33 boundary, step from 20 to 64. No ramp — a vertical edge.
- **Why this beats a scene launch:** no new track, no scene reorg, the switch lives inside the Rack so you can move the whole clip around and the switch moves with it.
- **Callback to W8 (Autechre):** W8 used this same rack to flip 8 patches across a long piece. Same engine; different use — W8 is timbral variation, W11 is pocket change.

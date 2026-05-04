# The Ableton bridge — Tuning Systems + Operator + Scale device

The Monologue feature set ports to Live 12 in three devices working together. <Citation bib="ableton_live_12_manual" />

- **Tuning Systems (top-right toolbar)** — load a `.scl` file. The six RDJ scales from the Monologue firmware are not publicly shipped as `.scl` files, but the Korg Sound Librarian exports them as SysEx; the Surge Synth Team's Scale Workbench converts. For the exercise: the Huygens-Fokker `7-limit-just.scl` is the closest publicly-available match to James' documented preferences.
- **Operator (4-op FM)** — the Ableton stand-in for the Monologue's VCO pair. Tuning Systems applies globally; Operator plays the loaded scale on every note.
- **Scale device (MIDI effect)** — MIDI-side filter; rides in front of Operator. Use it to constrain incoming notes to scale degrees when the Tuning Systems scale is non-12-EDO.

Parameter table — Monologue → Live:

| Monologue | Live 12 equivalent |
|---|---|
| Master Tune ±50¢ | Preferences → Tuning → Master Tune |
| Microtuning slot | Tuning Systems loaded `.scl` |
| Per-key offset | Cells in Tuning Systems' edit grid |
| Motion sequence on pitch | Live 12.2 Pitch MIDI transformation |
| 6 user scales per program | 6 instances of a Rack macro-swapping Tuning |

Crucial caveat: Tuning Systems is **global to the set**, not per-track. For per-track tunings you either split into multiple sets or use MTS-ESP with a router plugin like ODDSound's MTS-ESP Mini.

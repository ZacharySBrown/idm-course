# Macro Variations — the snapshot primitive

- Live 12.2 (released 2025) introduced <term key="macro_variation">Macro Variations</term>: named snapshots of every macro's current position, stored on the Rack itself, recallable from the macros bar or via MIDI/automation.
- **What gets captured:** macro values, including the Chain Selector macro. Not the underlying chain devices' parameters (those are always live).
- **What that means operationally:** you can store "Verse A" (Chain Selector = 20, Filter macro = 40%, Drive macro = 0%) and "Switch B" (Chain Selector = 80, Filter = 80%, Drive = 30%) as two variations. One click recalls the entire snapshot across all 8 macros.
- **Recall is not interpolation by default.** A variation recall is an instantaneous jump — unless you assign a morph time in the variation settings (12.2+ supports per-variation morph ms), in which case it interpolates linearly.
- `bib:ableton_live_12_manual` *Macro Variations* section for the full semantics. This is the closest Live gets to a modular-synth snapshot recall; Autechre's patch-flipping workflow (W8) maps cleanly onto it.

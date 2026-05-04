# The Follow Actions panel — annotated

Five fields matter. Ignore the rest on first pass.

1. **Trigger** — how often FA fires. Bars, Beats, or Sixteenths. 1 Bar for drums and sections. 1/16 for stutter-fills.
2. **Action A / Action B** — the two edges out of this clip's state.
3. **Chance A / Chance B** — the weights. Live normalizes, so 20/80 and 1/4 are equivalent.
4. **Legato** — phase preserve vs reset, per fa-03.
5. **Linked** (scene-level) — when on, all clips in the scene transition together. Off, each clip's FA fires independently. <Citation bib="ableton_live_12_manual" />

**The scene-level FA** is the per-scene sibling added in 12. Set it once at the scene header, and every clip in the scene inherits unless the clip overrides. That is where you control *section advance* (scene 1 → scene 2) separately from *within-section variation* (clip rotation inside scene 1). Spec B §4. <Citation bib="sos_autechre_april_2004" />

Two-axis control — scene FA drives structure, clip FA drives texture.

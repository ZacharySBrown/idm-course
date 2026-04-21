# Parameter table — what to set for a hard switch

- **Chain Selector macro (Macro 1):**
  - Min: 0. Max: 127. Step: 1.
  - Automation mode: **Step** (right-click envelope → Step). Prevents diagonal ramps that would crossfade chains.
- **Zone A (pre-switch chain):**
  - Range: 0–42. Left fade: 0. Right fade: 0.
- **Zone B (post-switch chain):**
  - Range: 43–85. Left fade: 0. Right fade: 0.
- **Automation envelope on Macro 1 (Arrangement View):**
  - Break point 1: bar 1, value 20. Break point 2: bar 33, value 64. Step segment between.
- **Macro Variation settings:**
  - Variation A: morph time 0 ms. Variation B: morph time 0 ms.
- **CPU safety:** all chains are live all the time in Ableton's current implementation — inactive chains still use CPU. If the Rack stutters, **Freeze** or **Bounce** the Rack after committing the switch (see s08, commit before you flip).
- `bib:ableton_live_12_manual` table of defaults matches this. Values above are the hard-switch preset — narrow both ranges and zero both fades.

# Follow Actions — the state machine, drawn

Each clip is a node. Each Action is a weighted edge. The trigger fires every N bars. Two edges out; Live rolls Chance A vs Chance B and takes one.

Above — a simplified view of a three-clip pool with the Pattern 1 recipe (20% self, 80% other). Pool size N=3 gives roughly equal draw among the other clips.

**Reading it:**

- The **self-loop** on each node is Play Again at Chance 20.
- The **cross-edges** are Other at Chance 80 / (N−1) = ~40 each.
- **Any** (not drawn) would add a cross-edge back to the node itself.

**Why this matters for variation generation** — the five mutations produce five distinct 16-bar variants. Drop them into one Session column. Set each to Action A Play Again 10 / Action B Other 90. Now you have a variation pool *inside* the arrangement. Capture MIDI on the row-output gives you a committed Arrangement that never repeats. <Citation bib="ableton_live_12_manual" />

The state machine is how Autechre-style non-repetition lives in a DAW without a single patch cord. <Citation bib="sos_autechre_april_2004" />

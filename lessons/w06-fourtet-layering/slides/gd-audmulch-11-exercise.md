## Exercise — three-stage Effect Rack with chain-swap morph

**Deliverable.** A single audio track with a three-chain Effect Rack. Each chain is a filter → saturator → reverb sequence, but each slot can be swapped to a different plugin via Chain Selector position.

**Steps.**

1. Load `moanin_glitch.wav` (from Stemforge w06) on an audio track.
2. Insert an **Audio Effect Rack** on the track. Create three chains, name them *clean / crushed / wet-wide*.
3. In **chain 1**: Auto Filter (LP 4 kHz) → Saturator (soft drive) → Reverb (room, small).
4. In **chain 2**: EQ Eight (notch 200 Hz) → Overdrive → Echo (ping-pong dotted).
5. In **chain 3**: Auto Pan → Roar (heavy) → Hybrid Reverb (shimmer, 4 sec tail).
6. Map **Chain Selector** to Macro 1. Record automation on Macro 1 over a 16-bar loop, sweeping through all three chains.
7. Render. Reimport the render as a new clip. Arrange with it.

**Constraint.** Do not A/B the render against the source. Once rendered, treat it as a new sample. This simulates the 2003 "print and archive the source" discipline.

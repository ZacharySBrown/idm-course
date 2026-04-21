# Exercise — ship a Chain Selector switch Rack

- **Deliverable:** one `.adg` (Ableton Device Group / Rack preset) + one 60-second `.wav` demonstrating the switch.
- **Rack spec:**
  - Instrument Rack, 3 chains.
  - Chain A: any clean bass patch you already have. Chain B: same patch with added FM or distortion. Chain C: a deliberately wrong patch (bit-crushed, detuned, whatever).
  - Chain Selector mapped to Macro 1. Three Macro Variations stored: **A**, **B**, **C**.
  - Zones hard — 0 fades on all zones.
- **Arrangement spec:**
  - 64 bars. Switch from A to B at bar 33. Switch from B to C at bar 49. Return to A at bar 57 for outro.
  - Use step-curve automation on Macro 1; no diagonal ramps.
- **Bounce spec:**
  - Render bars 1–60 at the session tempo, 44.1 kHz 16-bit. Filename: `w11_<trackname>_cs-switch.wav`.
- **What "good" looks like:** the three switches are audible without a riser, without a crash, without a filter sweep. The switch is the switch.
- **What will trip you up:** envelopes on the destination chain re-trigger from zero on the switch bar. Either accept the attack, or commit the chain's sound to an audio clip and play the audio instead of the synth. `bib:ableton_live_12_manual` on Freeze + Flatten.

# The pitfall — Complex Pro softens kicks

Drop the Hallogallo drums stem on a track, set warp mode to Complex Pro, and listen to the kick. Something is off. The leading edge is rounded. The click is gone. It reads more like a floor tom than a kick.

This is a known cost of Complex Pro, and it is not a bug. Phase-vocoder reconstruction averages spectral frames across the Envelope window; transients get spread across adjacent frames and lose their attack. Per the compass notes: *"Complex Pro softens kick transients."*

Two fixes:

1. **Nudge warp markers.** For every kick, drag the warp marker a few milliseconds *before* the transient. This gives the algorithm a head-start so the attack sits on the grid cleanly.
2. **Layer Beats underneath.** Duplicate the track, set the duplicate to Beats mode, high-pass it around 80 Hz or so, low-volume underneath. The original carries the body; the Beats copy carries the punch.

Pick per source. Do not default.

Cite: `bib:ableton_live_12_manual`. Stem: `stemforge:w04-hallogallo-warp-ab`.

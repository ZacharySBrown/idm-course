# Slicing algorithms — how to pick the knife

Four Slice by options. They are not ranked; they solve different problems. The decision tree above the text dispatches by source type.

- **Transient** runs an onset detector over the waveform. Works well on dry, well-recorded drum loops. On anything with reverb tail, bleed, or soft onsets, it misfires — you get slices on tail peaks instead of hits.
- **Beat** ignores audio entirely and places markers at fixed note divisions (1/32 through 1 bar). Requires a warped clip. Safe for any <term key="warped_clip">warped clip</term> where the grid is honest — 1/16 is the default for drum loops.
- **Region** divides the sample into N equal pieces, tempo-blind. Useful for pads, drones, field recordings where rhythm is irrelevant and you want consistent fragment length.
- **Manual** — no algorithm. Cmd+I on a selection. The escape hatch when the detector is wrong and you're certain where the markers should go.

Practical rule: try **Beat 1/16** first. Fall back to **Transient** if the grid is loose. Use **Manual** to fix mistakes. **Region** is for non-rhythmic sources.

[ref: bib:ableton_live_12_manual]

# Slice to New MIDI Track

The hidden move that most tutorials botch.

Workflow, exact clicks:

1. Drop an audio clip onto an audio track.
2. Warp it. Warp mode matters — Beats for drums, Complex Pro for messy breaks. If the transients fall on the grid, Re:warp From Here is fine.
3. Right-click the clip header → **Slice to New MIDI Track**.
4. Dialog appears. Pick **Slicing Preset** — the default preset is a Drum Rack with Simpler in Slicing mode, one slice per pad, chromatic from C1.
5. Pick **Create one slice per** — Warp Marker, Transient, or Beat Division.
6. Click Create.

Live generates a new MIDI track, loads the Drum Rack, maps every slice to a pad, and writes a MIDI clip that re-plays the original sample one-for-one.

That last clip is your chopping source. Re-sequence it. Do not replay the original pattern.

[ref: bib:ableton_live_12_manual, bib:charnas_dilla_time]

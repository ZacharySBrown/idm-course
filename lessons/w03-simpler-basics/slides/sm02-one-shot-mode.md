# One-Shot mode — no envelope, just the sample

One-Shot is Simpler's drum mode. The amp envelope and filter disappear from the GUI. You get start/end markers, fade in, fade out, and a Trigger/Gate switch.

What actually happens under the hood:

- The note-on event triggers the sample from its start marker. Pitch is fixed — notes do **not** transpose the sample. That is the whole point. Load a kick, hit any key, get the same kick.
- **Trigger** mode: the sample plays start-to-end regardless of note length. Release is ignored.
- **Gate** mode: note-off cuts the sample. Rarely what you want for drums.
- **Fade In** and **Fade Out** are linear ramps — typically 0–2 ms in, 5–15 ms out — applied independently of the sample's envelope.
- **Snap** forces start/end markers to the nearest <term key="zero_crossing">zero crossing</term>, which suppresses the click you'd otherwise hear when truncating mid-cycle.

If you want pitched drum layers, <term key="transpose">transpose</term> in semitones at the device level. Don't play them from the keyboard.

[ref: bib:ableton_live_12_manual]

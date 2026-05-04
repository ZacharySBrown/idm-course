# What a warp mode actually is

A <term key="warp_mode">warp mode</term> is a dispatch table. Live looks at the clip, looks at the playhead, and routes the audio through one of five algorithms — <term key="beats_warp">Beats</term>, <term key="tones_warp">Tones</term>, <term key="texture_warp">Texture</term>, <term key="repitch_warp">Re-Pitch</term>, or <term key="complex_pro_warp">Complex Pro</term> — before sending samples to the output bus. Complex (legacy) is the same algorithm as Complex Pro with fewer controls; treat them as one.

Each algorithm solves a different problem. Beats solves "keep transients sharp." Complex Pro solves "pitch and time independently on polyphonic material." Texture solves "make this into a cloud." Re-Pitch does no solving at all — it changes the playback rate and hands you the coupled pitch-time result that tape always gave you.

Pick wrong and the algorithm costs more than it gives. The rest of this mini-module is the cost ledger.

Cite: `bib:ableton_live_12_manual`, Warp Modes section.

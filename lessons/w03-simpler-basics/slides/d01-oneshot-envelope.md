# One-Shot envelope — what the fade sliders actually do

One-Shot has no amp envelope. What it has are two linear ramps at the ends of the sample — Fade In and Fade Out. They are not ADSR stages; they are micro-ramps to suppress transients at the truncation points.

Read the waveform above:

- The **Fade In** ramp climbs from zero to full gain over its millisecond window. At 0 ms you hear the raw sample front — fine for a kick that starts on a zero crossing, bad for a sample snipped mid-cycle.
- The **Fade Out** ramp drops from full gain to zero over its window before the End marker. This is the pop-suppressor for long hits that get cut short by the next note.
- **Snap** pins Start and End to the nearest zero crossing. With Snap on, the fades are often unnecessary. With Snap off on a sample edited to arbitrary length, the fades do the work.

The numbers from the Reference Manual: Fade In range 0 s–4 s, Fade Out range 0 s–4 s. You will live in the 0–20 ms end of both sliders for drum work.

[ref: bib:ableton_live_12_manual]

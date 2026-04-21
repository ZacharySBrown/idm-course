# Algorithm continued — the scheduler's cost

Max's scheduler is a cooperative single-threaded event queue. A long-running object blocks everything downstream.

Practical constraints for Autechre-style patches:

- **Overdrive on** — scheduler runs at higher priority than the UI thread. Turn this on always for music use.
- **Scheduler-in-Audio-Interrupt (SIAI)** — scheduler runs inside the audio thread. Tighter MIDI/audio sync at the cost of lower allowed DSP headroom.
- **Signal Vector Size 64** — 1.45 ms DSP latency. Any lower and CPU goes up. For live-performance patches with dozens of voices, many Autechre-adjacent patches run at SVS 128 or 256.
- **`poly~` for polyphony** — spawn N voices of a subpatch on demand. The voice-allocation pattern.
- **`thispoly~` for voice management** — lets each voice know when to free itself.

Limits that bit Autechre in the `Confield` era and still bite you: **CPU cost scales with active voices**, and a Max patch that was fine at 4 voices will crackle at 16. Freeze sub-patches to audio when you can; use `poly~` with a modest voice cap; run DSP at a larger vector when performance matters more than latency.

`bib:cycling74_max_msp_docs`

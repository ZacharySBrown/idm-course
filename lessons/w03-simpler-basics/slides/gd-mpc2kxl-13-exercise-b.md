# Exercise B — go beyond: Buffer Shuffler + Drum Rack

**Deliverable.** One `.wav` file. 16 bars. A break that evolves — same source material, Buffer Shuffler re-ordering on a per-bar basis, plus a programmed Drum Rack layer underneath.

Steps:

1. Pick one drum loop from stemforge output — not a one-shot, a full bar of percussion. Drop it onto an audio track. Warp it to project tempo with Beats mode.
2. Add **Buffer Shuffler 2.0** (Ableton's native M4L device) to that track. Set the buffer to 1 bar. Set re-order density to moderate — about 40% shuffle. Let it run; now the break reshuffles itself every bar.
3. On a second MIDI track, load a Drum Rack from the StemForgeLoader's `w03-express-oneshots` output. Keep only kick, snare, hat. Program a simple 4-bar pattern.
4. Record 16 bars of both tracks together to a new audio track. The Buffer Shuffler layer will produce a different reshuffle on each bar — 16 distinct bars from one source clip.
5. On the bounced audio, **Slice to New MIDI Track** with Transient slicing. You now have a MIDI clip that re-plays the 16 reshuffled bars. Edit it — remove half the notes, double-time a section, whatever.
6. Bounce the edited version. File: `w03_<yourname>_shuffler_remix.wav`.

Time-box: ninety minutes. If the Buffer Shuffler feels random, it is random — that is the device. Audition until a bar lands.

[ref: bib:ableton_live_12_manual]

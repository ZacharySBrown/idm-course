# Exercise A — a four-note step sequencer, M4L

Build the simplest possible Max-for-Live step sequencer and drop it on a drum track.

Steps:

1. In Live, create a new MIDI track. Add a Drum Rack with four slots (kick, snare, closed hat, open hat).
2. Add a **Max MIDI Effect** device on the track. Hit the Edit button (pencil icon) — Max opens.
3. Build this graph:
   - `metro 125` (fires every 125 ms = 16th at 120 BPM) → `counter 0 3` (counts 0,1,2,3 repeating).
   - `counter` output → `route 0 1 2 3` (fans into four outlets by value).
   - Each of the four outlets → `makenote 127 100` (velocity 127, duration 100ms) → `noteout`.
   - Each `makenote` has a different note value: 36 (C1), 38 (D1), 42 (F#1), 46 (A#1) — standard GM drum map.
4. Freeze the patch. Save.
5. Hit play in Live. You hear kick, snare, closed hat, open hat in a 4-step loop.

**Deliverable.** One M4L MIDI device that plays a 4-step pattern into a drum track, checked in. 20 minutes.

Extension: replace `counter` with `random 4` — note the pattern now changes every bar. Then *remove* the random. That is the Autechre choice, made in one gesture.

`bib:cycling74_max_msp_docs` · `bib:ableton_live_12_manual`

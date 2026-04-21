# Exercise A — load a Scala file, tune a kick to root, play four bars

Replicate the Monologue's microtuning feature in Ableton, from scratch, on drums. <Citation bib="ableton_live_12_manual" />

**Setup (10 min):**
1. Download `7-limit-just-intonation.scl` from the Huygens-Fokker archive.
2. Open a new Live 12 set. Top-right → Tuning Systems → Load → pick the `.scl`. Set root note to E.
3. New MIDI track → Drum Rack → Simpler on pad C1 with a kick one-shot. Switch Simpler to **Melodic** mode (not Classic) so Tuning Systems applies.
4. Program a four-bar MIDI clip — kick on every downbeat.
5. Transpose Simpler so the kick lands at E1 (~41 Hz fundamental).

**The move (10 min):**
6. On bar 2, MIDI-nudge a kick onto scale degree 3 (G in E-min JI). On bar 3, degree 5 (B). On bar 4, degree 7 (D natural, 7-limit so ~31¢ flat of tempered D).
7. Render. Listen for the fundamental tracking the melody.

**Deliverable.** A 15-second WAV showing the kick-as-JI-arpeggio. One sentence: *what did the 7-limit seventh sound like against a normal 12-TET bass?* (Hint: it sounds like the bass is wrong. The bass is not wrong.)

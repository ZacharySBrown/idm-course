[pause 200ms]

Brief aside on two Live 12 features that are genuinely useful for this material, and one that is not. [pause 200ms]

Live 12 shipped a feature the Ableton marketing page under-sold at launch — **Tuning Systems**. Top-right of the toolbar, next to the metronome. You can load a Scala file — the .scl format, open spec, used by microtonal software since 1990 — as the active tuning for your entire set. <Citation bib="ableton_live_12_manual" /> Every stock Ableton synth that supports tuning messages — Operator, Wavetable, Meld, Drift, Simpler when triggered by MIDI — now plays the loaded scale instead of 12-TET.

The Huygens-Fokker archive in the Netherlands has thousands of historical and experimental tunings as free .scl downloads. Just intonation, meantone temperaments, Indian ragas, Indonesian gamelan, Partch's 43-tone divisions. Load one, play a C major chord, hear a different C major chord.

Second tool, don't confuse it with the first — the **Scale device**. MIDI effect, drop it on any MIDI track or rack. It constrains incoming MIDI to a chosen scale *before* the instrument sees the note. If a wrong note comes in, the device snaps it to the nearest scale tone. This is the sequencer-side fix — Tuning Systems is the instrument-side fix.

For tuned drums this week, you need neither. [pause 200ms] Simpler is the drum engine. It reads the MIDI note number and transposes the sample. You move Transpose with the mouse. No Scala file required.

For melodic content in *future* weeks — when you load a lead into Operator and want the track to be in Bohlen-Pierce — Tuning Systems is where you start. The Scale device is where you go when your MIDI sequencer is generating notes you don't want. <Citation bib="sos_autechre_april_2004" /> — Autechre's entire Max-for-Live rig does a version of this with conditional scale logic in patches, which we'll get to in Week 8.

Third, quickly — the Pitch MIDI transformation, Live 12.2 and up, applies per-note cent offsets to a committed MIDI clip. Useful later, not today.

# Live 12 Tuning Systems and the Scale device

Live 12 shipped a feature Ableton under-sold: a global tuning system. Load a **Scala (.scl)** file as the active tuning. Operator, Wavetable, Meld, and Drift all play the loaded scale. <Citation bib="ableton_live_12_manual" />

The Huygens-Fokker archive has thousands of free historical tunings.

Two different tools, don't confuse them.

- **Tuning Systems** (top-right toolbar) — the instrument-side fix. Changes what the synth plays.
- **Scale device** (MIDI effect, rack-droppable) — the sequencer-side fix. Constrains incoming MIDI before the instrument sees it.

For tuned drums you need neither. Simpler transposes the sample from the MIDI note number. For melodic content later, load the track's key as a Scala file and stop hitting wrong notes.

Second-order: the Pitch MIDI transformation (Live 12.2+) applies per-note cent offsets to committed clips.

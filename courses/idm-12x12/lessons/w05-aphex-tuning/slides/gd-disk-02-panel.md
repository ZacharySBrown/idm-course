# What's under the lid — the annotated mechanism

Three systems stacked into one piano: <Citation bib="wikipedia_disklavier" />

- **MIDI input jack** — DIN-5 on early models, USB on Mark IV and later. Takes any standard MIDI stream: 16 channels, note-on/off, velocity, CC1, CC64 (sustain pedal), CC66 (sostenuto), CC67 (soft pedal). The piano accepts SMF and XG-extended files. Velocity range: 1–127, mapped to solenoid drive current.
- **Solenoid bank under the keys** — 88 solenoids, one per key. Each solenoid is an electromagnet that pulls a plunger upward, which presses the key from below. The key's downward travel pushes the hammer action — the physical linkage is unchanged from a normal grand. Key-strike latency is ~30ms on Mark IV, <10ms on Enspire Pro. The click is the plunger seating.
- **Pedal solenoids** — three, mounted behind the pedal lyre. Sustain, sostenuto, soft. These click the loudest. When Aphex mics inside the body, the pedal solenoids become a percussion voice distinct from the string hits.

What's *not* instrumented: microtuning. The Disklavier is 12-TET to the bone; the keyboard layout is fixed, one hammer per string, no per-key detune. You layer microtuning on top in the DAW after recording.

The Drukqs technique is not about pitch. It is about the mechanical noise the piano makes when played by a machine.

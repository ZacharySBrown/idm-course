# Exercise A — layer Collision clicks under a piano VST

Replicate Drukqs-style solenoid-click-as-rhythm without a Disklavier.

**Setup (10 min):**
1. New Live 12 set. Track 1: MIDI → NI Noire or Ableton's built-in Grand Piano. Track 2: MIDI → Collision. <Citation bib="ni_noire_docs" />
2. Collision settings: Mallet ON, Stiffness 95%, Noise 40%. Resonator: Plate, Decay 200ms, Material 80%. Mallet layer level: +0dB. Resonator level: −12dB.
3. Route Track 2 to a new return (Return B). Return B insert: HPF at 600 Hz, Glue Compressor 4:1, makeup +3dB.

**The move (15 min):**
4. Import a MIDI piano file — any Chopin prelude, any Satie piece, or write a 16-bar melody in Piano Roll. Drop it on both tracks simultaneously.
5. Play. You now hear piano tone from Track 1 and solenoid clicks from Return B, synchronous.
6. Modulate Collision's Mallet velocity response via a Velocity Shaper M4L device — send MIDI velocities <60 to Collision only (fake soft-pedal click without hammer).
7. Add a subtle Drum Rack on Track 2 with a ~70 Hz kick sample triggered at low velocity — the body cavity "woof."

**Deliverable.** 20-second WAV. One sentence per layer: *what did removing Collision sound like? What did removing the piano sound like?* <Citation bib="ableton_live_12_manual" />

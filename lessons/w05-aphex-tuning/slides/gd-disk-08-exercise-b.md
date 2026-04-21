# Exercise B — Collision as a drum synth, not a piano surrogate

Past replication. Use Collision as the percussion source for a full drum pattern. No piano. No Disklavier reference. Just the physical model doing what physical models do. <Citation bib="ableton_live_12_manual" />

**Setup (15 min):**
1. New MIDI track with a Drum Rack. Drop one Collision instance onto pad C1, another on D1, a third on F#1 (kick, snare, hat).
2. For each Collision: different Resonator type. C1 = Membrane (kick-ish), D1 = Plate (snare-ish), F#1 = String (hat-ish). Tune the Ratio parameter per-pad to taste.
3. On each pad, set Mallet Stiffness 70%, Noise 50%, Decay 40ms. You want short, wood-tone attacks — not pretty piano hits.

**The move (30 min):**
4. Program a four-bar break pattern — any grid, any tempo. The Drum Rack fires Collision on each pad.
5. Tune each pad to a scale degree via Ratio parameter or via the Pitch MIDI transformation. Match the exercise: kick to root, snare to fifth.
6. Listen to the timbre. Collision's attack is harder than a 808 sample and softer than a drum synth. It has a characteristic "wooden" tone that is unmistakably physical-modeled.
7. Bounce 30 seconds.

**Deliverable.** 30-second WAV + one paragraph on the timbral difference between Collision drums and your normal sample-based drum rack. *What did the physical model give you that a sample didn't? What did it fail to give you that a sample did?*

Aphex made drums from a piano. You can make drums from a beam, a plate, and a membrane. The physical modeling is the point. <Citation bib="wikipedia_disklavier" />

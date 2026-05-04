# The 4-step resampling ladder — sample, chop, pitch, resample

Herren's workflow, reconstructed from XLR8R and the MPC2000XL manual. The ladder is the move.

**Rung 1 — Sample.** Record a 2–4 second vocal phrase from a turntable into a single pad. 44.1 kHz, 16-bit, mono. The phrase is too long to be a hit and too short to be a loop.

**Rung 2 — Chop.** Enter Chop Shop (Trim → F4). Slice by Regions (16 equal divisions) or by Threshold (transient-based). Assign each slice to a pad in Bank A. The vocal phrase is now 16 independent fragments addressable as MIDI notes.

**Rung 3 — Pitch.** Use the Note Variation slider to re-pitch selected pads ±3 to ±7 semitones. Some up, some down. Finger-drum a new rhythm across the pitched fragments. Record the performance into a MIDI track.

**Rung 4 — Resample.** Press Resample during playback of the MIDI track. The MPC captures its own output into a fresh sample slot. Now that resampled take is a new 2–4 second phrase — loop back to rung 1.

Two ladder cycles and the source is unrecognizable. Three, and it is no longer yours.

[ref: bib:prefuse_73_xlr8r, bib:akai_mpc2000xl_manual]

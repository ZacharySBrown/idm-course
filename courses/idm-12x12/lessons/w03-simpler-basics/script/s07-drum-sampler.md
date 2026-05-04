Drum Sampler. The Live 12 addition most producers missed.

[pause 400ms]

Drum Sampler is a pad device — a single-pad instrument that ships inside a Drum Rack. Functionally it is a Simpler plus three pattern-shaping MIDI tools built into the pad itself. The marketing calls it an enhancement. It is, as far as drum programming is concerned, the device.

The three tools are **Velocity Shaper**, **Ornament**, and **Time Warp**. They run on incoming MIDI, not on audio. The sample on the pad is untouched. You are reshaping the pattern, not the timbre.

[pause 500ms]

**Velocity Shaper.** You draw a curve. The horizontal axis is incoming velocity, zero to one-twenty-seven. The vertical axis is outgoing velocity, also zero to one-twenty-seven. A straight diagonal line is identity — what comes in is what goes out. Bend the curve and you rewrite the dynamics. On a kick pad, you want a steep curve — low velocities get suppressed to ghost-note territory, high velocities get boosted to hit the sample hard. On a ghost snare pad, you want the opposite — a gentle curve that keeps everything in the low dynamic range so the ghosts stay ghosts.

[pause 300ms]

This replaces the Velocity MIDI effect you would otherwise chain in front of a pad, and it is per pad, which is the whole point.

[pause 500ms]

**Ornament.** Adds flams and mordents at a chosen note length. The length setting is the distance between the grace note and the main note. Length 1/64 is the Aphex setting — almost-touching flams on snares. Length 1/32 is a looser flam. Longer lengths turn into rolls. Ornament runs per pad, so you can flam your snare without flamming your kick.

[pause 400ms]

**Time Warp.** Bends the timing of incoming MIDI notes within a bar. You draw a curve; Live pulls notes earlier or later depending on where they fall. Per pad. This is how you bake in Dilla time — the un-quantized per-pad swing signature we cover in Week 9. On a hat pad, pull the off-beats three milliseconds late. On a snare pad, push the backbeat two milliseconds early. The kick stays straight. The groove shifts without you touching a single MIDI note.

[pause 500ms]

~Three tools.~ Per pad. Running on MIDI before the sample fires. This is a bigger deal than the shipping announcement made it sound.

If you are coming from a pre-12 workflow where you built the same behaviors with MIDI Effect Racks and the Groove Pool, the short version is — you do not need those anymore for drum tracks. Drum Sampler does it in one device, per pad, recallable.

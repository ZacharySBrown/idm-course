## Ableton wiring — Note Chance + Pitch Transformer

Both pieces native to Live 12. `Ableton Live 12 Reference Manual`.

**Velocity variance (±15%)**
- Clip view → note editor → **Velocity Range** handle per note.
- Select all notes, drag any Range handle — Live scales proportionally.
- Every trigger, Live rolls a uniform random velocity inside the band.

**Octave shift at 15% probability**
- Duplicate the clip's notes in place. Shift duplicates +12 semitones. With duplicates selected, set **Chance** field to 15%. Delete originals at those beat positions.
- For ±12 symmetry, split 15% across two duplicate layers (one +12, one −12, ~7–8% each).
- Alternate: **Clip → Transform → Pitch** with probabilistic shift, then bake.

Prefer the duplicated-layer route. It survives bounces, it is inspectable in the clip.

Check: re-trigger five times. If every playback is identical, the Chance did not commit.

# Bass seed — the Ableton walk-through

Seed is a MIDI **Generator**, not a Transform. It draws notes from scratch into the clip's grid under rule constraints. <Citation bib="ableton_live_12_manual" />

**Click-by-click:**

1. Duplicate the bass MIDI track. Mute the original. Rename the duplicate `bass seed`.
2. Draw an empty 2-bar MIDI clip. Set **Scale** on the clip to match the track's key.
3. Open the clip. MIDI editor footer → **Generators → Seed**.
4. Parameters: **Pitch Range** ±7 semitones. **Density** 60%. **Note Length** 1/16 or 1/8.
5. Hit **Roll**. Live fills the clip.
6. Audition. If bad, Roll again. Budget ten rolls.
7. When one lands, close the Generator popover. The notes are now editable MIDI. Capture MIDI (Cmd+Shift+C) is a separate path if you Roll while the clip plays and want to keep what you heard. <Citation bib="ableton_live_12_manual" />

**Receipts.** Spec B 12.3 — "Seed generator produces acid-style basslines within key constraints; combine with Chance 60–75% on hats for non-repeating patterns." <Citation bib="sos_autechre_april_2004" />

**Caveat.** Seed obeys the Scale setting on the *clip*. If the clip's scale is C-major but your track is D-minor, the result will clash. Check the clip scale before rolling.

# Consolidate, Bounce in Place, and Freeze — which one, when

Three Ableton commands that all look like "commit the audio," all different.

| Command           | What it does                                             | Reversible?       | Use when                                                     |
|-------------------|----------------------------------------------------------|-------------------|--------------------------------------------------------------|
| **Consolidate** (`Cmd+J`) | Merges a selection of clips on one track into a single audio clip | No — destructive  | You have ten overlapping MIDI clips in a lane; you want one audio region. |
| **Bounce in Place**        | Renders a track's MIDI + effects to audio, muting the source | Reversible (source preserved, just muted) | You want to free up CPU from a plugin chain but keep the option to un-freeze. |
| **Freeze Track**          | Renders to a hidden cache; track becomes non-editable     | Fully reversible — unfreeze restores | CPU pressure during writing; you're not committing yet.       |
| **Bounce Group** (12.3)   | Renders a group track to a new audio track; source group muted | Reversible | Subtraction's checkpoint — commit the Peak before muting.     |

**For Subtraction.** Bounce Group the Peak. Don't Consolidate it — Consolidate is destructive and Subtraction needs the option to un-bounce if the Peak was wrong. `bib:ableton_live_12_manual`.

# One-Shot mode — drum hits without pitch drift

The parameter list, in the order you actually touch them:

- **Snap** — on. Start and end markers jump to zero crossings. Kills the click you would otherwise add.
- **Fade In** — 0 to 2 ms on a raw hit. Higher if the sample front-end is brittle.
- **Fade Out** — 5 to 15 ms. Prevents the tail pop when a long kick is cut by the next note.
- **Trigger** vs **Gate** — Trigger plays the full sample regardless of note length; Gate stops on note-off. One-shots are Trigger.
- **Transpose** — in semitones. The pitch-tune-to-root move from Week 5 lives here.
- **Detune** — cents. Use for layering the same hit against itself at ±5 cents.

Warp is available in all three modes. Leave it off for one-shots unless you are deliberately time-locking a hit to tempo.

[ref: bib:ableton_live_12_manual]

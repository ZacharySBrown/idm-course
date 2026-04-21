# Beats mode — slice, play, truncate

<term key="beats_warp">Beats mode</term> does three things in order.

1. **Detect transients.** Live runs an onset detector across the clip and drops a slice marker at every significant attack.
2. **Play each slice at source rate.** When the transport hits a slice, the slice plays back at the speed it was recorded. Transient intact.
3. **Fill to the next grid point.** If the slice ends before the next grid position, the remainder is either silenced (Loop Off), repeated (Loop), or played forward and stopped (Loop Forward).

This is why Beats is cheap and fast: no FFT, no re-synthesis. The trade is that anything tonal — a held chord, a vowel, a sustained synth — gets chopped at arbitrary points and relooped, which produces an audible zipper or chatter.

Use on <term key="drums">drums</term>, percussion, one-shots. Not on pads.

Cite: `bib:ableton_live_12_manual`.

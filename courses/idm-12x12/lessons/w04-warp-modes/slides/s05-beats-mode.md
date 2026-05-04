# Beats mode — transients intact, grid hostile

Beats mode is a slicer wearing a warp costume. Under the hood: detect transients, cut the audio at every marker, play each slice at its original speed, and truncate or loop the tail to hit the next grid position.

Three controls matter:

- **Preserve** (1/2, 1/4, 1/8, 1/16, 1/32, Transients). Sets the slice grid. Preserve 1/16 = a slice every sixteenth. Transients = slice at every detected hit.
- **Transient Loop Mode** (Loop / Loop Off / Loop Forward). Off = clean tails, occasional gaps. Loop = fills gaps by looping the slice tail — can artifact on held notes.
- **Transient Envelope** (0–100). Short decay on each slice. 100 = no envelope, clicks at every edge. 0 = fast fade, zipper noise on sustained content.

Beats mode preserves kick punch. It also mangles anything tonal — sustained synths, vocals, chord stabs. Use it on drums and you are safe. Use it on a pad and you will notice.

Cite: `bib:ableton_live_12_manual`.

Slice to New MIDI Track. The move every breakbeat tutorial either rushes or botches.

[pause 400ms]

The exact clicks. In order.

[pause 300ms]

Step one. Drop an audio clip on an audio track. For the exercise later today, this will be a stemforge render. For right now, use any drum loop — an Amen break, a Madlib drum loop, anything with eight or sixteen clear hits per bar.

Step two. Warp it. Warp mode matters. **Beats** is the correct warp mode for a drum loop — it preserves transients by holding each hit still and only stretching the tail between hits. **Complex Pro** softens drum transients in a way that is musical for some sources and wrong for others; the Reference Manual notes this on the Complex Pro page. For dirty or long breaks where Beats chatters, Complex Pro is the compromise. If the downbeats fall cleanly on the grid, the Re:warp-From-Here command is a one-click fix.

[pause 400ms]

Step three. Right-click the clip header — the gray strip at the top of the clip, not the waveform itself. A context menu opens. Scroll down to **Slice to New MIDI Track**.

Step four. A dialog appears. Two fields matter.

*Slicing Preset* — the factory default is a Drum Rack containing sixteen Simplers set to Slicing mode. This is fine for most cases. You can save your own preset — a Drum Rack pre-loaded with your preferred EQ, saturator, and output routing per pad — and pick it here. The preset decides what plays each slice.

*Create one slice per* — three options. **Warp Marker** makes a slice at every warp marker currently in the clip. **Transient** uses the same transient detector as Simpler's Slicing mode. **Beat Division** gives you 1/32 through 1 bar. 1/16 is almost always what you want for a drum loop.

[pause 500ms]

Step five. Click Create.

Live generates a new MIDI track. The Drum Rack sits on it. Every slice is mapped to its own pad chromatically, starting at C1 and walking up. On the same track, Live writes a MIDI clip that re-plays the original sample slice-by-slice — so if you press play, the loop sounds identical to the source.

[pause 400ms]

That MIDI clip is the starting material. It is not the finished pattern.

The compositional move — and this is the point Dan Charnas makes in *Dilla Time* about J Dilla's chopping philosophy, page one-twenty and following — is to **re-sequence the slices into a pattern the source never was**. Most producers slice a break, play back the automatic MIDI, and call that a remix. It is not a remix. It is a re-description of the original.

Rearrange. Reverse some slices. Mute half. *Then* bounce.

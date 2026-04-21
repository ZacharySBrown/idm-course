Slicing mode. The knife-placement problem.

[pause 300ms]

When you switch Simpler to Slicing, the waveform gets vertical lines drawn through it — the slice markers. Each marker is the start of a new playable slice. The sample is now, functionally, a kit — one sample with internal cut points, each cut point mapped to its own MIDI note chromatically from C1.

The question is where the markers go. That is the **Slice by** dropdown.

[pause 400ms]

**Transient.** Simpler's transient detector scans the sample and places a marker at every detected attack. A Sensitivity slider controls how aggressive. Higher sensitivity means more markers, shorter slices. This is the right choice for dry, gated drum loops with clear, separated hits. It is the wrong choice for a wet break where the reverb tail of one hit blurs into the next — the detector gets confused, you end up with markers three milliseconds off, and the resliced pattern sounds like a skipping CD.

[pause 300ms]

**Beat.** Markers on a fixed grid. The division choices are 1/32, 1/16, 1/8, 1/4, 1/2, and 1 bar. For a warped drum loop at a normal tempo, 1/16 is the default — sixteen slices per bar, one for each sixteenth-note grid position. If the loop is half-time — a slow hip-hop break — 1/8 gives you sixteen slices per two bars, same spacing. Beat mode is the safe choice when you have warped the clip correctly. Transients may fall a few milliseconds off the grid; Beat mode does not care, it cuts on the grid regardless.

[pause 400ms]

**Region.** Equal divisions of the sample, ignoring tempo completely. One through sixty-four divisions. This is for pad textures, ambient sources, non-rhythmic material — anything where the underlying audio has no beat. Slice a Four Tet pad into thirty-two regions and you can re-trigger sections of it melodically.

[pause 300ms]

**Manual.** You place markers yourself. Select a region of the waveform; press Cmd-I — Command, letter I — and Simpler inserts a marker at that point. Use Manual when the detector is wrong and you know better. Which is often.

[pause 500ms]

The other setting that matters is the playback mode — the three-way selector underneath the slice list. **Mono.** **Poly.** **Thru.**

Mono chokes the previous slice when a new one fires. Use this for kicks and snares — you almost never want two kick slices ringing together. Poly lets slices overlap; use it for melodic material. Thru means the current slice plays until a new one is triggered — interesting for drone textures and generally confusing for drums.

Mono is the default you want ninety percent of the time.

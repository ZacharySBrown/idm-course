# A populated Drum Rack — what you're building toward

The screenshot above shows a Drum Rack with 16 pads populated — the first three rows loaded from a Stemforge render: three kicks, three snares, three hats, three toms, a clap, a rim, a shaker, a crash.

Each pad is its own <term key="drum_rack_chain">chain</term>. The pad is not the sample — the pad is a route to a chain that contains a Simpler that contains the sample. Three layers of indirection that buy you per-pad effects, per-pad choke groups, per-pad Velocity Shaper, and per-pad audio-out routing.

Notice the pad numbers: C1, C#1, D1, D#1, E1, F1... the chromatic mapping starting at C1 that Slice to New MIDI Track uses by default, and that the StemForgeLoader follows for drum kits.

[ref: bib:ableton_live_12_manual]

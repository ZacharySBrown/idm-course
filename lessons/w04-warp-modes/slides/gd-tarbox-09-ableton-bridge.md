# Ableton bridge — approximating the Fridmann bass in the box

This is the load-bearing slide. You will not have a Dorrough 610 and a Studer A80. You will have Ableton.

The approximation stacks three Ableton primitives against Fridmann's three stages:

| Fridmann stage | Ableton primitive | Role |
|---|---|---|
| Neve 88RS mic pre (hot) | <term key="saturator">Saturator</term> Analog Clip, Drive +3 to +6 dB, Dry/Wet 80% | Input-stage non-linearity |
| Dorrough 610 multiband | Audio Effect Rack with 3 chains (EQ-8 band-split + <term key="glue_compressor">Glue Compressor</term> per chain) | Multiband compression with per-band distortion via hard settings |
| Studer A80 tape | Saturator Soft Sine mode, Drive +6 dB, Dry/Wet 60%, plus subtle EQ-8 shelf boost around 80 Hz | Tape saturation / low-end thickening |

Macros: Drive (Saturator #1), Low-band threshold (chain 1 Glue), Mid-band threshold (chain 2 Glue), Tape drive (Saturator #2). Four knobs, one Rack.

The next slide shows the Rack structure.

Cite: `bib:ableton_live_12_manual` (Glue Compressor, Saturator); `bib:soundtoys_decapitator_manual` for the plugin alternative.

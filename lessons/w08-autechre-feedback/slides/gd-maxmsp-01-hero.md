# Max/MSP — the studio as patched graph

Cycling '74's Max started life as Max (1986, control-rate only), grew MSP in 1997 (signal-rate audio), added Jitter in 2002 (video/matrix), and shipped **gen~** in 2012 (sample-accurate codebox DSP). Booth acquired a copy in 1997 per SOS April 2004: *"Most of Confield came out of experiments with Max that weren't really applicable in a club environment."*

The paradigm: **every audio or MIDI signal is a wire between objects.** No timeline. No clip. No session. A patch is a graph; the graph *is* the instrument.

This deep-dive treats Max as a composition environment — the thing that generated Confield, LP5, Untilted, Oversteps, Exai, and the NTS Sessions patch family — then maps it onto Max for Live, which is the same engine embedded inside Ableton 12.

`bib:sos_autechre_april_2004` · `bib:cycling74_max_msp_docs`

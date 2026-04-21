Drum Rack. Let us correct one vocabulary problem up front.

[pause 300ms]

A Drum Rack is *not* a sampler. It is a grid of independent device chains, with MIDI notes routed to each chain. Saying "the Drum Rack played the sample" is like saying "the recording studio recorded the vocal." The studio contained the microphone that recorded the vocal. The Drum Rack contains the sixteen Simplers that played the sample. The distinction matters because it tells you where to put things.

[pause 500ms]

The architecture, from the outside in.

**Pads.** 128 of them. One per MIDI note, zero through 127. The visible grid is sixteen at a time. Page Up and Page Down scroll by octave. Most producers live in the three octaves from C1 to C4 and never look at the rest.

[pause 300ms]

**Per pad, a chain.** A chain is a device list. It can be a single Simpler. It can be a Simpler followed by an EQ Eight, a Saturator, a Glue Compressor, and an Auto Filter with a macro assigned. It can be an entire nested Instrument Rack — the classic transient-body-sub kick Rack, three chains with different EQ windows, all triggered by the same MIDI note on C1. No rule says a drum pad has to start with a sampler. A pad can hold Operator. A pad can hold Wavetable. A pad can hold nothing but a MIDI Effect Rack that re-triggers other pads.

[pause 400ms]

**Send-return chains.** Down the right side of the Drum Rack, there is a column labeled S. Those are the send-return chains — normally a reverb, a delay, and a parallel compressor. Each pad has per-pad S knobs that send its output to those shared effects. This is how you get seven pads going to the same reverb without putting seven reverb instances on seven pads.

[pause 400ms]

**Choke groups.** Numbered one through sixteen. Set two pads to Choke 1 and hitting one silences the other. The classic use is closed-hat and open-hat sharing Choke 1, so the closed hat cuts off the open hat the way it would on a real kit. You can also use it to choke a kick against its own sub-body layer if you want — one trigger, two pads, clean chain.

[pause 400ms]

**Output routing.** Each pad has its own output selector. You can route kick to audio-out-2, snare to audio-out-3, hats to audio-out-4 — each landing on its own audio track for mixing. For this week we stay on the default; mixing discipline is Week 12.

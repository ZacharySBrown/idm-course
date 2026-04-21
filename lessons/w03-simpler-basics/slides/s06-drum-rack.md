# Drum Rack — chains are the point

A Drum Rack is not a sampler. It is a grid of independent device chains with MIDI notes routed to each chain.

The architecture, from the outside in:

- **128 pads** — one per MIDI note. The visible grid is 16 at a time; Page Up / Page Down scrolls octaves.
- **Per pad**: a chain. A device list — Simpler, or Simpler plus EQ Eight plus Saturator, or a nested Instrument Rack. No rule says the chain must start with a sampler.
- **Send-Return chains** (right column) — shared reverb, delay, parallel comp. Routed per-pad via the S knobs.
- **Choke groups** — 1 through 16. Pads in a group silence each other. Closed hat chokes open hat.
- **Output routing** — each pad can route to its own audio output.

[ref: bib:ableton_live_12_manual]

# Chain Selector — what actually routes through the Rack

- `bib:ableton_live_12_manual`, *Instrument Rack → Chain Selector*. A Rack hosts N parallel instrument chains. The <term key="chain_selector">Chain Selector</term> value (0–127) selects which chain receives incoming MIDI and passes audio out.
- Zones on the Chain Selector strip define which chain responds to which selector value. Overlap zones crossfade two chains; hard zones hard-switch.
- Macros expose parameters from any chain to the Rack's top-level 8-macro bar. The same macro can address a filter cutoff on Chain 1 and a feedback send on Chain 3 — one knob, different destinations per chain.
- **This is the mechanism that makes an in-track beat switch work without leaving Arrangement View.** Automate the Chain Selector macro from zone 1 (clean bass) to zone 2 (FM growl) at bar 33; audio path flips on the downbeat.
- See diagram — MIDI enters left, hits the Selector decision, audio exits right. The selector itself is just a MIDI-range gate with a UI.

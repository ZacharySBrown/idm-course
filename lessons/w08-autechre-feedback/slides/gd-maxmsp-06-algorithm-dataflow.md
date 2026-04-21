# Algorithm — dataflow model

Max is a **dataflow** language. Execution is not "top to bottom line by line" — it is "right-inlet-first, then left, then the next message."

Three rules that catch every beginner:

1. **Right-to-left, top-to-bottom order.** When an object has multiple outlets, Max fires the *rightmost* outlet first, then middle, then leftmost. Same for inlets. Mis-wiring here gives you the "my patch is one tick late" bug.
2. **Hot vs cold inlets.** A left (hot) inlet triggers output. Right (cold) inlets just store values. The classic `[+]` object: right inlet sets the addend, left inlet triggers output. `[trigger b b]` ("t b b") is how you enforce explicit fire order.
3. **Messages vs signals.** Messages are discrete events with a timestamp. Signals are continuous sample streams. Connecting a message outlet to a signal inlet is legal (converted via `sig~`) but the other direction requires `snapshot~` or `change` to sample the signal into a message.

The dataflow model is why Max patches look like schematics. They *are* schematics. Read them like analog synth patch cables, not like a script.

`bib:cycling74_max_msp_docs`

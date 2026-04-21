# Slicing mode — the sample becomes a drum rack

Slicing mode chops a sample into numbered segments. Each segment gets a MIDI note — by default chromatic from C1 upward. The device turns a single sample into a mini Drum Rack without the Drum Rack.

What actually happens under the hood:

- On load, Simpler runs the **Slice by** detector across the sample and writes marker positions.
- Each marker becomes a <term key="slice">slice</term>; notes C1, C#1, D1... trigger slices 1, 2, 3...
- **Playback**: Mono (new slice chokes previous), Poly (overlap allowed), Thru (current slice plays until next trigger, ignoring note length).
- Each slice has its own <term key="gain">gain</term> and can be reordered, deleted, or manually repositioned.

**When to use it vs. Slice to New MIDI Track** — Slicing mode keeps everything inside one Simpler; Slice to MIDI explodes the sample into a full Drum Rack with a Simpler per pad. Use Slicing mode for fast chopping where you won't add per-slice effects. Use Slice to MIDI when you want per-slice processing chains.

[ref: bib:ableton_live_12_manual]

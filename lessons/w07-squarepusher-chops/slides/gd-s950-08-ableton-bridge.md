# Ableton bridge — Drum Rack + Follow Actions + bitcrush

Modern chain. <Citation bib="ableton_live_12_manual" />

| S950/DR-660 feature | Ableton equivalent | Setting |
|---|---|---|
| Chop per keygroup | Drum Rack with Simpler per pad | Slice to New MIDI Track, 1/16 |
| DR-660 pad-to-keygroup trigger | MIDI clip on Drum Rack | Native — each pad is a C1+n note |
| 12-bit companding | TAL-Bitcrusher or Ableton Redux | Bit depth 12, downsampling off, drive 3 dB |
| Alias-on-repitch | Simpler Classic mode + Transpose | Classic mode does sample-rate conversion, aliases like S950 |
| Single-pass discipline | Follow Actions on a clip pool + one-shot record | No undo — Capture MIDI into a locked clip |

**Bitcrush note.** The 12-bit setting alone does not match the S950 grit. Add a 16 kHz LPF (Auto Filter, Type: LP, 12 dB/oct) *before* the bitcrusher to emulate the anti-alias filter, and ~1 dB of input drive *into* the bitcrusher to engage the companding-like behaviour.

Decimort 2 is the closer match for period-authentic companding behaviour if you own it.

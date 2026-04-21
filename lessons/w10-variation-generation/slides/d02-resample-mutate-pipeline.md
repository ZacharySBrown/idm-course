# Resample-and-Mutate — the pipeline, drawn

The Mr. Bill engine, rendered as a data flow. One-way arrows only; you cannot go back. <Citation bib="mr_bill_resample_tutorial" />

**Reading the diagram:**

- **Source tracks** on the left. MIDI drum + bass + pad.
- **Resample bus** captures their sum.
- **Print** — the bus is bounced to a new audio track. At this moment the MIDI is deletable.
- **Chop** splits the printed audio to Simpler Slicing.
- **Mutate** — pitch, reverse, bit-crush, Sample Offset envelope.
- **B/C section material** — the chopped mutants are dropped back into the Arrangement as variation source.

The dashed red line is the **commitment boundary**. Left of the line, MIDI is editable and the rabbit hole is open. Right of the line, audio is printed and the only moves are mutate or delete. <Citation bib="rick_rubin_creative_act" />

**In Live 12.3**, the whole pipeline collapses to Bounce Groups + Paste Bounced Audio. Before 12.3 you ran it manually with resample tracks. <Citation bib="ableton_live_12_manual" />

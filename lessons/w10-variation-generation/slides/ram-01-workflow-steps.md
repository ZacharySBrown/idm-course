# Resample-and-Mutate — the core loop, step-by-step

Mr. Bill's engine, written as a recipe. <Citation bib="mr_bill_resample_tutorial" />

**The loop (every 8–16 bars):**

1. **Route.** Create a new audio track. Set **Audio From → Resampling** (or pick the drum bus directly).
2. **Arm and record** 4–8 bars while the source plays.
3. **Mute or delete the source.** Mute first if nervous. Delete after one play-through confirms the print.
4. **Consolidate** the printed clip (Cmd+J) so it becomes a single warped audio file.
5. **Chop.** Right-click → Slice to New MIDI Track → Simpler (Slicing mode, transient markers).
6. **Mutate.** Pitch ±12st on two slices, reverse one, bit-crush one, leave the rest.
7. **Drop into B and C sections.** <Citation bib="ableton_live_12_manual" />

That is the whole engine. Repeat every 8–16 bars of finished material. The mutated output is the B and C sections you would otherwise have to compose.

**The commitment** is what makes this a workflow and not a toy. The printed audio survives undo stacks. The deleted MIDI does not.

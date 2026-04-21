# Filter sweep — the Ableton walk-through

One Auto Filter, one macro, one envelope. The whole trick is the unlinked envelope loop.

**Setup:**

1. Shift-select all tracks involved in the duplicate. Cmd+G to **Group**. Rename the group `var3 group`.
2. Insert **Auto Filter** on the group's insert chain. Filter type **LP24** (Clean). Frequency 20 kHz, Resonance 15%.
3. Cmd-right-click the Frequency knob → **Map to Macro 1**. The macro is now your sweep control.
4. Right-click the group clip → **Show Envelope**. Envelope selector → **Macro 1**.
5. Draw a ramp: bar 1 at macro 0 (closed), bar 16 at macro 100 (open). <Citation bib="ableton_live_12_manual" />

**Unlinked envelope:**

6. Click the Envelope pane's **Linked/Unlinked** toggle. Set envelope loop to **7 bars**. Audio loops 16.
7. The sweep now never lands at the same position across repeats. Autechre polymeter trick. <Citation bib="sos_autechre_april_2004" />

**Limitation.** A 24 dB LP sweep eats low end before it reaches the bass register. If the kick disappears, switch to **BP** with Resonance 40% for a body-preserving sweep, or keep LP but side-chain-bypass the kick channel from the group.

One parameter. Not two.

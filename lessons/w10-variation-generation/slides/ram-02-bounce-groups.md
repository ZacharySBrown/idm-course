# Bounce Groups (Live 12.3) — the engine, natively

Before 12.3, Resample-and-Mutate meant routing tracks, arming Resampling, and watching a meter. Live 12.3 shipped **Bounce Groups** and **Paste Bounced Audio** — the loop as a right-click menu. <Citation bib="ableton_live_12_manual" />

**The 12.3 path:**

1. Select a group track in Arrangement.
2. Right-click → **Bounce Group**. Dialog opens.
3. Pick range, sample rate, bit depth, whether to include returns.
4. **Delete source** toggle — check it. This is the Mr. Bill move, native.
5. Click Bounce. Live renders, inserts the printed audio, optionally clears the source MIDI.

Spec B receipts — "Bounce to New Track (12.2), Bounce Groups and Paste Bounced Audio (12.3) enable the bounce-and-arrange workflow as a native loop." <Citation bib="sos_autechre_april_2004" />

**Caveat** — Bounce Groups does not capture the state of *Follow Actions-driven* Session clips. For FA output you still need Capture MIDI → Arrangement first, *then* Bounce Groups on the Arrangement tracks.

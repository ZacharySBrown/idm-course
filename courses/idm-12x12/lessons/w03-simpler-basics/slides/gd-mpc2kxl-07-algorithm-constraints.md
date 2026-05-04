# Algorithm constraints — why the MPC sounds like the MPC

The machine has three constraints that became aesthetic signatures. Every modern re-creation has to choose which of them to preserve and which to skip.

**1. The TC swing curve.** TC 1/16 with swing values 50% (straight) to 75% (maximum shuffle). Swing is applied to every *other* 1/16 note — the "and" counts are pushed later. The curve is not Dilla's. It is a fixed exponential mapping; Dilla (MPC3000) had a different chip revision with a subtly different curve. Herren (MPC2000XL) usually worked at 54–58% swing.

**2. Sample memory as a ceiling.** The base machine ships with 2 MB of RAM — 12 seconds of mono 16-bit. Expanded to the full 32 MB via EXM-E3 SIMMs, you get about 6 minutes mono or 3 minutes stereo. This forced short samples — a 2-second vocal phrase, not a 20-second loop. The short-phrase-into-chop method is not a choice; it is what fit in RAM.

**3. No time-stretch, no warp.** The MPC2000XL cannot time-stretch a sample while preserving pitch. If you record a 95 BPM break and your track is at 90 BPM, you either pitch the whole sample down (which slows it), or you chop it and re-trigger at the new tempo. The "chop and re-trigger" workflow is forced by the absence of warp.

Ableton's Simpler breaks constraint 3 via Beats warp. Students who want the Prefuse sound should deliberately turn warp off.

[ref: bib:akai_mpc2000xl_manual]

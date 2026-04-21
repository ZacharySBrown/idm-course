# Scala, TUN, MTS — the three file formats that carry tunings

Before the deep-dives: know the file extensions.

- **`.scl` (Scala)** — plain-text scale definition. Lists the pitches as either cent offsets or integer ratios from the root. Does **not** specify what the root is; pair with a `.kbm` keyboard-mapping file to pin scale degree 1 to a MIDI note. Origin: Manuel Op de Coul's Scala program, 1990s. Live 12 reads `.scl` natively in **Tuning Systems**. <Citation bib="ableton_live_12_manual" />
- **`.tun` (AnaMark TUN)** — binary-style 128-entry table, one cent offset per MIDI note. Absolute — each MIDI note gets its own frequency. Used by older VSTs (Zebra 2, some Synth1 builds). Live 12 does not read `.tun` directly; convert via Scala software.
- **`.mts` / MTS-ESP** — MIDI Tuning Standard, runtime MTS-ESP protocol from ODDSound. Sends tuning as SysEx/MIDI messages to any compatible plugin in real time. Lets one master clock retune every synth in the session simultaneously. Live 12's Tuning Systems is MTS-ESP-compatible per the 12.2 manual.

The practical default: free `.scl` from Huygens-Fokker, drag into Tuning Systems, done. The practical upgrade: MTS-ESP for live tuning modulation — you can automate the *scale itself*, not just the pitch played in it.

Every format is public and documented. Ignorance is a skill issue, not a gatekeeper.

# Slice to New MIDI Track — the full flowchart

The flowchart above traces what Ableton actually does when you click **Slice to New MIDI Track**. Nothing is hidden. Everything is reversible.

Under the hood:

1. Live reads the source clip's warp markers, transient markers, or beat grid — whichever you selected in the dialog.
2. Live creates a new MIDI track below the source.
3. On that track, Live instantiates the **Slicing Preset** — by default a Drum Rack whose pads each contain a Simpler configured in Slicing mode, one slice per pad, chromatic from C1.
4. Live writes a MIDI clip on the new track. Each note corresponds to one slice. The notes are placed at the **original slice timings**, so the new MIDI clip replays the source audio position-for-position.
5. The source clip is unmuted and unchanged. You now have two tracks making the same sound. Mute the source.

The whole point of the command: you now have a MIDI pattern you can edit. Re-sequence it. That step — *not* the slicing — is the compositional move.

[ref: bib:ableton_live_12_manual, bib:charnas_dilla_time]

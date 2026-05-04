# CPU, Freeze, Bounce in Place — the unglamorous part

Generative chains get heavy. Three Max for Live devices plus Roar plus a Drum Rack full of sample chains and your session will start glitching.

Per the Live 12 manual, three tools, used in this order:

- **Freeze Track.** Right-click a track header → Freeze. Ableton renders the track to a temporary audio file and suspends device processing. CPU recovers. Frozen tracks can still be moved, but device parameters are locked until you Unfreeze.
- **Flatten.** After Freeze, right-click → Flatten. The frozen audio becomes a new audio clip; the MIDI and devices are removed. **This is the commit.**
- **Bounce in Place** (Live 12.3 Bounce Groups). For subgroups of tracks. Commit a generative drum bus to one audio track. Delete the source group.

Rule: once a generative chain sounds right, **Flatten within the same session.** Do not come back to unfreeze. You are buying decision closure.

`bib:ableton_live_12_manual`

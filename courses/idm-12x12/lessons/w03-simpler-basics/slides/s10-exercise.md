# Exercise — four bars, three drums, one bounce

**Deliverable.** One `.wav` file. Four bars. Project tempo. Drums only, from the kit you just built.

Steps:

1. Run the stemforge recipe `w03-express-oneshots` against `grooves/Express Yourself.wav`. Output lands in `build/audio/stemforge-renders/w03/express_oneshots/`. LarsNet classifies hits as kick / snare / hat / tom / cymbal.
2. Drop the **StemForgeLoader.amxd** on a fresh MIDI track. Point its manifest at the `w03-express-oneshots` output. Let it build the seven templates and the song-specific Drums Rack.
3. Keep only **kick, snare, hat** on C1, D1, F#1. Delete or mute the rest.
4. Program **4 bars** of MIDI. Any pattern. Your pattern, not Charles Wright's.
5. On each of the three pads, open the Drum Sampler and **draw a Velocity Shaper curve** — kick steep, snare medium, hat gentle.
6. Bounce the track. File: `w03_<yourname>_4bar.wav`. Mute the source chain. Ship.

Time-box: forty-five minutes.

[ref: bib:stemforge_repo, bib:ableton_live_12_manual]

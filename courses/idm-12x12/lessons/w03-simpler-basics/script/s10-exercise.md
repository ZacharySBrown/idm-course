The exercise. Forty-five minutes. Timer on.

[pause 400ms]

**Deliverable.** One wav file. Four bars. Project tempo. Drums only, from the kit you built this session. File name: w03-underscore-your-name-underscore-4bar-dot-wav. Muted source chain. Committed.

[pause 400ms]

Step one. Run the stemforge recipe. The recipe ID is *w03-express-oneshots*. It points at `grooves/Express Yourself dot wav` and runs *stemforge forge* with the max-diversity strategy across four bars. The output is a folder at `build/audio/stemforge-renders/w03/express oneshots/`. Inside that folder, LarsNet has classified every detected hit as kick, snare, hat, tom, or cymbal, and written each one to a separate wav. You did not do this classification by ear. Stemforge did it for you. That is the point of the wave-four rendering pipeline.

[pause 500ms]

Step two. New Live set. Open at project tempo. The stemforge demo material is at ninety-six BPM, which is a sensible default — slow enough to program sixteenth hats, fast enough to not put everyone to sleep.

Drop the StemForgeLoader dot amxd on a fresh MIDI track. Point its manifest at the w03-express-oneshots output folder. Press the build button. It creates the seven template tracks — source, drums rack, bass rack, vocals rack, other rack, chromatic simpler, beat chop simpler. It duplicates the drums rack template, renames it, and walks the kick, snare, and hat one-shots into the first three pads at C1, D1, F-sharp-1.

[pause 500ms]

Step three. Delete or mute every pad that is not kick, snare, or hat. You are building a three-element pattern. Toms and cymbals come back in later weeks. For this week — three pads, three drums.

[pause 400ms]

Step four. Program four bars of MIDI. Any pattern. Your pattern. Not Charles Wright's. The loop the stems came from has its own pattern; you are making a different one.

Rules. Kick on at least two positions per bar. Snare on the backbeat or on any ~wrong~ beat. Hats running sixteenths or eighths, your call. Thirty-two to sixty-four total hits across the four bars.

[pause 500ms]

Step five. On each of the three pads — kick, snare, hat — open the Drum Sampler. Go to the Velocity Shaper tab. Draw a curve.

Kick — steep. Low input velocities get pushed lower; high input velocities hit the sample at full. The kick either hits or it does not.

Snare — medium. Some dynamic range. Ghost snares at low velocity should stay ghost; backbeats should hit hard.

Hat — gentle. You want the full dynamic range of the sixteenths to read. A steep curve would flatten the hat into a machine.

[pause 500ms]

Step six. Bounce. Cmd-B or drag the track output to a new audio track, whichever you prefer. File name exactly as specified. Mute the source chain. Delete the intermediate MIDI if you are feeling brave; keep it if you are not.

Ship. Post the bounce in the course thread. Move on.

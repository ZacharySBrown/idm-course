# Sample Offset envelope — new patterns from one audio file

Once the drum bus is printed as audio, you have a new parameter you did not have as MIDI — **Sample Offset**. Clip Envelope → Clip → Sample Offset. Grid set to 16ths. <Citation bib="ableton_live_12_manual" />

Draw ±8 sixteenth-notes of offset over the 2-bar loop. At playback, Live jumps the playhead around inside the audio file at each 16th boundary. Same audio, new pattern.

**Four shapes to try:**

1. **Stutter every 4th 16th.** Offset drops to −1/16, then snaps back. MPC beat-repeat.
2. **Slow climb.** Linear ramp +0 to +4 over 2 bars. The loop slides forward inside itself.
3. **Random staircase.** Steps at random values ±4. A whole new rhythm from the same file.
4. **Unlinked loop length.** Set the envelope's loop to 3 bars, audio loops 2 bars. Pattern never repeats inside eight bars.

Stack this under Follow Actions — Sample Offset envelope on each clip in the pool, different shape per clip, FA rotating them. Three levels of indirection from one printed loop.

Mutation 6, if we allowed a sixth. We do not. Save it for your own records.

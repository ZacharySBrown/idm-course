# Exercise A — replicate the Big Loada single-pass

Chop the Funky Fanfare drums via stemforge, load into Drum Rack, bitcrush to emulate the S950, play 32 bars single-pass. <Citation bib="stemforge_repo" />

1. Open `build/audio/stemforge-renders/w07/ff_drums.wav` in Ableton.
2. Right-click → **Slice to New MIDI Track** → Slice to: **1/16**, Slicing Preset: **Built-In**. <Citation bib="ableton_live_12_manual" />
3. On the Drum Rack return or the rack itself, insert:
   - Auto Filter → LPF, 16 kHz, 12 dB/oct (S950 reconstruction filter)
   - Redux → Bit Depth 12, Downsampling off, Bit Dither off
   - Glue Compressor → Ratio 3:1, Attack 1 ms, Release Auto, 2 dB of grab
4. Arm a new MIDI clip on the Drum Rack track, 32 bars long.
5. Press record. Perform the pattern finger-drumming on a MIDI controller or the QWERTY keys. **No stopping.** If you flub, keep going.
6. At bar 32, stop. Do **not** open the clip to edit. Bounce-in-place.

Name the bounce `w07_bigloada_<yourname>.wav`. One pass. The mistakes are the record.

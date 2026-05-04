# Multiband Rack build — the Dorrough approximation

Build order.

1. New Audio Effect Rack on the bass track.
2. Inside the Rack, create three chains labelled **low**, **mid**, **high**.
3. On each chain, first device is <term key="eq_eight">EQ-8</term> in bandpass mode:
   - low: lowpass, 200 Hz, 48 dB/oct
   - mid: bandpass, 200–1200 Hz
   - high: highpass, 1200 Hz, 48 dB/oct
4. After each EQ-8, a <term key="glue_compressor">Glue Compressor</term>:
   - low chain: threshold −30 dB, ratio 10:1, attack 1 ms, release 100 ms — this is the crunch band
   - mid chain: threshold −24 dB, ratio 6:1, attack 3 ms, release 60 ms — growl
   - high chain: threshold −18 dB, ratio 4:1, attack 10 ms, release 100 ms — gentle control
5. After the Rack, insert <term key="saturator">Saturator</term>: Analog Clip, +6 dB, Dry/Wet 60%.

The low-chain Glue at 10:1 with a fast attack is where the broadcast-style crunch comes from. The Saturator afterwards is the tape role.

Caveat: Live's Glue is emulating an SSL bus compressor, not a broadcast limiter. The character is not identical to a Dorrough — it is the same *class* of tool. If you need more aggression, swap the Saturator for Decapitator Style N (next slide).

Cite: `bib:ableton_live_12_manual`.

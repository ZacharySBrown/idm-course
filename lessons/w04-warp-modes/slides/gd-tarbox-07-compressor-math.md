# Compressor math — threshold, ratio, attack, release, knee

The <term key="compressor_transfer_curve">compressor transfer curve</term> is the function from input level to output level. Below <term key="threshold">threshold</term>, it is a straight line at unity gain (1:1). Above threshold, the slope flattens to 1/<term key="ratio">ratio</term>. A 4:1 ratio means: for every 4 dB of input above threshold, only 1 dB appears at the output.

Four parameters to hold in your head:

- **Threshold** — where compression starts.
- **Ratio** — how hard it squashes above threshold.
- **Attack** — how fast it gets to the ratio slope after threshold is exceeded.
- **Release** — how fast it lets go when input drops below threshold.

The diagram compares two settings on the same axis. The blue line is a gentle bus compression — threshold −18 dB, ratio 4:1. The red line is a Fridmann-style setting — threshold −30 dB, ratio 10:1, fast attack. At those parameters, the compressor is in gain reduction nearly all the time, and the <term key="knee">knee</term> region (the curved corner) is where audible harmonic distortion starts to appear. This is the mechanism behind the crunch.

Cite: compressor theory covered in `bib:roads_computer_music_tutorial`.

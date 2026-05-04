Take a sine wave. Use a second sine wave to modulate the first one's frequency. Crank the second wave into the audio range. The result is — mathematically — a comb of new frequencies above and below the carrier, spaced by the modulator frequency, with amplitudes set by Bessel functions of the modulation index.

[pause 1000ms]

If you didn't follow that, the next eight minutes are for you.

[pause 600ms]

The equation Chowning wrote in nineteen-sixty-seven looks like this. Y of t equals A times sine of two-pi-f-c-t plus I times sine of two-pi-f-m-t.

[pause 400ms]

A is amplitude. F-c is the carrier frequency. F-m is the modulator frequency. I is the modulation index — the depth. That's it. One amplitude, two frequencies, one depth. Four numbers. From those four numbers you can synthesize a marimba, a bell, a clarinet, a chainsaw, the metallic clang on a Squarepusher record, and the swelling pad behind every nineteen-eighties NASA documentary.

[pause 500ms]

Pedantically, this is *phase* modulation, not frequency modulation. The DX7 and Operator both implement phase modulation internally because it avoids an integrator and stays DC-stable. PM and FM by a sinusoid are equivalent up to a ninety-degree phase offset. Robert Henke, who built Operator, will say this directly on his website: phase modulation, not frequency modulation, very similar sonic results, significantly easier to calculate. If you read FM marketing copy, what is doing the work is PM.

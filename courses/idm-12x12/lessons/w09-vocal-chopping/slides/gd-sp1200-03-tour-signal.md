# Annotated tour, 2/2 — signal path and output routing

Signal path, input side: **line in → sample-and-hold at 26.04 kHz → 12-bit companded ADC → sample RAM**. No anti-alias filter at the input. Any frequency in the source above 13 kHz folds back as aliasing *and is printed into the sample*. Resampling a hot 16 kHz cymbal returns a ~10 kHz ghost. That ghost is permanent.

Output side: **pad trigger → sample RAM → varispeed playback → 12-bit DAC → individual output OR stereo mix bus → line out**. The stereo mix bus has gentle summing coloration; the individual outputs skip it. Producers used the individuals for bass, mix bus for drums, or vice versa — personal taste.

**No filters, no envelopes per voice.** The MPC3000 has a 2-pole LPF per voice; the SP-1200 has nothing. Every shape comes from the sample itself — truncate, pitch, or re-sample.

That radical simplicity is why SP-1200 records sound the way they do. There is no character knob. The character is baked into the ADC curve and the sample rate.

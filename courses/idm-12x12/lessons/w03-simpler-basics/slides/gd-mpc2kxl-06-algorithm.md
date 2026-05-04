# Underlying algorithm — 44.1kHz, 16-bit, the velocity curve

The MPC2000XL is a 44.1 kHz, 16-bit sampler with 16 voices of polyphony. It is not a lo-fi machine in the SP-1200 sense — the specs are CD-quality. What shapes the sound is the **velocity curve** and the sample-playback algorithm, not the bit depth.

From the manual and from Akai's service documentation:

- **Bit depth**: 16-bit linear PCM, 44.1 kHz sample rate, no companding. Contrast with the SP-1200 at 12-bit 26.04 kHz companded — the MPC2000XL is already "clean" by hip-hop-sampler standards.
- **Playback engine**: sample-and-hold interpolation by default; optional linear interpolation when pitched. Extreme re-pitch (+12 or more semitones) introduces aliasing you can hear — which is why 16-Levels chops at ±6 semitones stay musical while wider spreads get metallic.
- **Velocity curve**: each pad has its own <term key="velocity_curve">velocity-to-amp curve</term> and velocity-to-filter curve. Default is linear; Herren and most MPC users bent the curve so that light touches produced ghost hits and hard touches produced accent hits — a three-tier dynamic map inside a single pad.
- **Timing correction**: the global TC (timing correct) value quantizes incoming pad hits to the nearest 1/8, 1/16, 1/32, 1/16T, 1/32T, or Off. "Off" is the Prefuse setting. Every other setting grid-locks the performance.

[ref: bib:akai_mpc2000xl_manual, bib:roads_computer_music_tutorial]

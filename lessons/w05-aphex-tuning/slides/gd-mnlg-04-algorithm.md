# The algorithm — cent math inside the Monologue's MCU

Under the panel: a microcontroller that converts MIDI note numbers to pitch control voltages for two VCOs. The microtuning layer is a lookup table inserted between MIDI-in and CV-out. <Citation bib="korg_monologue_afx_manual" />

For MIDI note N arriving at the synth:
1. Compute base CV = `(N − 69) × (1 V / octave) / 12` — the default 12-TET mapping.
2. Look up the scale's offset for `N mod 12` — a signed integer in ±75 cents.
3. Scale-adjust the CV: `cv += offset_cents × (1 V / 1200)`.
4. If a motion sequence is active on this step, add its cent offset to the running total.

All math is done in the microcontroller before the CV reaches the DAC feeding the VCOs. Korg's spec sheet lists **16-bit pitch resolution** internally; the microtuning edit page exposes **1-cent user offsets** — well below perceptual threshold. The Monologue's limitation is not precision but *scope* — six user scales per program, 12 cent offsets per scale. 7-limit JI fits comfortably. 19-EDO does not (needs 19 steps per octave; the Monologue only offers 12). <Citation bib="korg_monologue_afx_manual" />

The same lookup-table pattern lives inside Ableton Live 12's Tuning Systems engine, just in 32-bit float and polyphonic. <Citation bib="ableton_live_12_manual" />

The hardware is not magical. The file format is the technology.

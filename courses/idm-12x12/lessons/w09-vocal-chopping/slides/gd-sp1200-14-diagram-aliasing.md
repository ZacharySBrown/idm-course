# Diagram — the aliasing cliff and the companding curve

Two diagrams, one slide, both load-bearing:

**Top: frequency-response cliff at 13 kHz.** A 26.04 kHz sample rate means content above 13.02 kHz folds back into the audible band. The diagram shows a source spectrum (0–20 kHz flat) and the SP-1200 output: flat to ~13 kHz, with a mirror-image aliased ghost from 13 to 0 kHz. Folded content is *added* to the original — there is no filter to remove it.

**Bottom: companded ADC curve (µ-law-style).** Horizontal axis = input amplitude (linear). Vertical axis = quantization levels used. A linear 12-bit ADC uses evenly spaced levels; a companded ADC uses dense levels near zero and sparse levels near full-scale. The asymmetry is the "crunchy transient, clean tail" signature.

Rule: **aliasing is permanent, companding is permanent.** Neither can be removed after sampling. That is why they define the sound. Source: Roads 1996, Ch. 1 on quantization and Ch. 3 on sampling theory (`bib:roads_computer_music_tutorial`).

The two artifacts together are a fingerprint. Together with varispeed pitch and a 2.5-second RAM division, they are the SP-1200.

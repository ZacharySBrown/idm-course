Loudest single point of this section. In subtractive synthesis, two envelopes do orthogonal jobs — the amplitude envelope shapes loudness, the filter envelope shapes brightness. The two are independent. You can have a quiet bright sound or a loud dull one.

[pause 500ms]

In FM synthesis, those two envelopes are not orthogonal. The modulator's level envelope *is* the brightness envelope. Because modulator level is proportional to the modulation index I, and I controls how much spectral energy migrates into the sidebands, enveloping the modulator level directly envelopes the timbre. The carrier's level envelope is the amplitude envelope, separately.

[pause 400ms]

This is why an FM pluck has that liquid attack — the bright initial *dwah* that decays to a near-sine tail. It is not a filter sweep. It is a modulator envelope. They sound similar because they are doing the same job to your ears.

[pause 600ms]

A useful conservation law: the total signal power, summed over all sidebands, equals one. Cranking up the modulation index doesn't change the loudness — it redistributes the spectral energy outward. Brighter, not louder. A subtractive filter envelope mostly cuts loudness as it cuts brightness. An FM modulator envelope only changes color.

[pause 500ms]

Practical translation, in Operator: the *Level* parameter on a modulator operator is functionally proportional to I. Operator's Level is logarithmic, calibrated so the maximum corresponds to an I on the order of ten to fifteen. Envelope the modulator's Level, and you envelope the brightness directly. Every classic FM gesture — the wah, the vocal-formant, the pluck — is a modulator-level envelope.

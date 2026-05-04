# True peak vs sample peak — the four-times oversampling argument

The sample-peak meter lies by omission.

A digital file is a sequence of samples at 44.1 or 48 kHz. The analog waveform the DAC reconstructs between those samples can — and often does — rise *above* the highest sample value. That is an **intersample peak**. On a lossless playback chain it is mostly benign. On an AAC, Ogg Vorbis, or MP3 re-encode, the lossy decoder rebuilds the analog wave and clips against the codec's internal ceiling. The file that measured 0.0 dBFS in Live now shows audible distortion on Spotify.

True-peak metering oversamples the signal by 4× (BS.1770-4 minimum) and reports the *interpolated* peak — the peak the DAC would actually produce. That is the number to clamp.

- −1.0 dBTP — the industry-standard safety ceiling for streaming delivery
- −2.0 dBTP — cautious when the source is already hot; Apple's own delivery spec recommends −1.0 but some mastering houses use −2 for headroom
- 0.0 dBFS — ceiling that *will* clip on at least one major platform

FabFilter Pro-L 2 enables true-peak oversampling at 4× by default; it can be pushed to 16× for paranoid masters at a small CPU cost. <Citation bib="fabfilter_prol2_docs" /> Youlean's true-peak readout is the sanity check after bounce. If it reads worse than −1.0, lower the limiter ceiling and re-bounce. No exceptions.

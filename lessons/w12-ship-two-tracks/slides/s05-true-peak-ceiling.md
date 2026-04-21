# True peak ceiling — −1.0 dBTP, not zero

The one number that will bite you at upload: true peak, measured in dBTP.

Sample-peak metering shows you the loudest *sample* in your file. True peak metering shows you the loudest *inter-sample* reconstruction — the peak the DAC will produce when the file is played back through lossy codecs (AAC, Ogg Vorbis, MP3). Streaming platforms re-encode. Re-encoding raises intersample peaks. A file that hits 0 dBFS in Live can clip on Spotify's AAC.

Fix: **limit to −1.0 dBTP**, not 0 dBFS.

- FabFilter Pro-L 2 — ceiling set to −1.0 dBTP, true-peak oversampling enabled (default). <Citation bib="fabfilter_prol2_docs" />
- Brainworx bx_XL V2 — one option, not the only option. Useful if you want M/S limiting per band. <Citation bib="brainworx_bx_xl_docs" />
- iZotope Ozone Maximizer — fine if you already own Ozone. <Citation bib="izotope_ozone_maximizer_docs" />
- Live's stock Limiter — also fine. Set ceiling to −1.0.

Youlean's true peak readout is the check. If it reads anything above −1.0, lower your ceiling or lower your input. Re-bounce. Re-check.

This is the one place where "near enough" is actually not.

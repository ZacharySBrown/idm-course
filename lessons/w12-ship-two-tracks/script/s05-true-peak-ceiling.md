The one number that will bite you at upload is *true peak*, measured in dBTP. [pause 400ms]

Here is the mechanism, because it is worth understanding once. Sample-peak metering shows you the loudest discrete sample value in your audio file. Zero dBFS is the ceiling — the maximum digital value the file can hold. Everyone knows that. [pause 300ms]

But when your DAC reconstructs the analog signal between samples, or when a lossy codec like AAC or Ogg Vorbis re-encodes your file, the *reconstructed* waveform can overshoot the individual sample peaks. This overshoot is called inter-sample peaking. It is not theoretical. Spotify, Apple Music, YouTube — they all re-encode your uploaded WAV to AAC or similar. A file that peaks at zero dBFS in Live can clip on the re-encode.

[pause 400ms]

The fix is to limit to minus one dBTP. Not zero. Minus one.

[pause 300ms]

FabFilter Pro-L 2 exposes a ceiling parameter with a true-peak option — enable oversampling, set the ceiling to minus one point zero dBTP, and Pro-L 2 holds you there. Brainworx bx_XL version two is another option if you want mid-side limiting per band. [pause 200ms] bx_XL is *one* option. It is not, despite what marketing copy sometimes implies, the only mastering limiter worth owning. iZotope Ozone's Maximizer works too. Live's stock Limiter works too — set its ceiling to minus one.

[pause 400ms]

After you bounce, load Youlean on a blank track and play the exported WAV back through it. Read the true-peak number. If it says anything above minus one, your limiter leaked or your ceiling was set wrong. Lower the ceiling, lower the input gain, re-bounce, re-check.

[pause 300ms]

~This is the one place where near enough is not actually near enough.~ Minus zero point one dBTP will still occasionally clip on Spotify's AAC. Minus one is the safety margin that stops the phone call.

[pause 400ms]

The number is on the export. If Youlean reads minus one point two, you are clean. Ship.

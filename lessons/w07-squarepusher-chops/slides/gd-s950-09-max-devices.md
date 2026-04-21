# Parallel Max for Live / third-party devices

For closer period-correct processing:

- **Unfiltered Audio Sandman Pro.** Matches the S950's pitch-shift-as-sample-rate-conversion behaviour when set to Classic mode and bit-reduce on.
- **D16 Decimort 2.** Emulates specific vintage samplers — the E-mu SP-1200 preset is famous; the Akai S-series preset applies a gentle LPF + µ-law-shaped companding closer to the S950.
- **Ableton Redux (native, Live 12).** Bit-depth + downsample. Simpler than Decimort but needs a pre-filter to match the S950's reconstruction curve. <Citation bib="ableton_live_12_manual" />
- **M4L Buffer Shuffler 2.0.** Not a sampler emulator — a pattern tool. Pair it with a Drum Rack of Amen chops to get Squarepusher's *50 Cycles*-style re-sequenced bar-by-bar drum reshuffles. See W9 for deeper Dilla-era Shuffler work.

The combo that gets closest to the Big Loada sound: Drum Rack → Classic-mode Simplers → Decimort 2 (S-series preset) → a slow Glue Compressor on the drum bus at 3:1.

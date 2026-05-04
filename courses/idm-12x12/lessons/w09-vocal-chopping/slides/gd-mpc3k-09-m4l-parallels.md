# Max for Live parallels — Pad Swing, MPC Groove, Humanize

Third-party M4L devices that close the gap:

- **Pad Swing** (various authors on maxforlive.com) — puts a swing-% knob on every chain of a Drum Rack. The closest one-to-one MPC3000 per-pad swing clone.
- **MPC Groove** — a Max device that loads classic MPC groove templates (swing 54, 58, 62, 66%) as groove files. Hand-tuned against MPC hardware by the author. Verify the specific version on maxforlive.com; bib slot flagged in `needs_bib:`.
- **Humanize** (native Live MIDI effect) — randomizes timing within ±N ms. Not ideal — Dilla's drift is *deliberate*, not random. Useful for hats only, never for kicks or snares.
- **K-Devices TTAP** or **alkman Euclidean Pro** (`bib:alkman_euclidean_pro`) — handle polyrhythmic accents if you want to replicate the MPC3000's quintuplet/septuplet tricks.

The critical move: use these devices to set **different** values per chain. If every pad has the same swing %, you've built a TR-909 feel, not a Dilla feel.

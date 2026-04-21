# Metadata hygiene — composer credits, BPM, key, ISRC

The metadata fields are boring. Shipping without them is boring-and-expensive.

- **Composer credits** — your legal name or a single consistent pseudonym, spelled the same way on every release. This is what the PROs (ASCAP, BMI, SOCAN, PRS) register and what pays out performance royalties. "Zak Brown" on one release and "Zak R. Brown" on another registers as two rights-holders and collects half the royalties each. Pick one form. Commit.
- **Performer credits** — typically same as composer for solo-producer releases. If someone else played on a track, name them in the performer field, not in the track title.
- **BPM** — integer, honest. The DAW-reported tempo if the track is a single tempo. If the track has a tempo change, pick the dominant tempo or the final tempo; do not invent an average.
- **Key** — use Camelot notation (1A, 2B, etc.) if you are releasing to DJ-focused platforms; use musical notation (A minor, F# major) for Bandcamp and general catalogs. If the track is not in a single key, leave it blank.
- **ISRC** — 12 characters, agency-allocated. For Bandcamp-only, you can skip it initially and add it at DSP-distributor time. DistroKid auto-allocates; TuneCore does the same. Self-allocation via the RIAA US ISRC agency is available but only worth it if you release a lot. Flagged in `needs_bib:`.
- **Genre** — "IDM" plus "Electronic" plus one sub-tag is enough. Over-tagging does not help discovery. Under-tagging does hurt it.

The fifteen minutes you spend filling these fields accurately before release saves the three months of royalty chasing later. <Citation bib="edmprod_intermediate" />

# Bandcamp upload — the fields that actually matter

The upload form has twenty fields. Six of them matter for the private-EP exercise.

- **Album title** — lowercase or Title Case, consistent with your artist page. No trailing punctuation; some feeds strip it.
- **Release date** — set to today or a near date. "Private" does not require a public date, but Bandcamp records it for later re-publish.
- **Privacy: Private** — this is the setting for the exercise. Share-link only, not on your public artist page, not searchable.
- **Artwork** — 3000 × 3000 px, JPEG or PNG, sRGB, under 10 MB. Anything smaller and it degrades on every platform it ever touches later.
- **Track titles** — lowercase recommended. Do not use exclamation marks; some downstream DSP feeds silently strip them. No emoji. No brackets with credits — those go in the metadata, not the title.
- **Track file** — 24-bit / 44.1 kHz WAV, your `artist_trackname_v01_master.wav` from slide s12.

Bandcamp's own upload spec is the canonical receipt and was flagged in `needs_bib:` for a first-party URL. The dimensions and bit-depth numbers come from the upload form itself as of this lesson's authoring. <Citation bib="jack_conte_ship_it" />

Ignore the "About this track" and "Lyrics" fields for the private exercise. Fill them before you make it public. Not now.

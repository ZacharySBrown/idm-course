# Heather — the source pool for Follow Actions 2.0

stemforge recipe `w10-heather-variation-source` runs *Heather* (Billy Cobham) through section-stratified curation at 2-bar length. <Citation bib="stemforge_repo" />

```
stemforge forge grooves/Heather.wav \
  --strategy section-stratified \
  --n-bars 2
```

Output: `heather_loops/` tagged by region — `intro_*.wav`, `a_*.wav`, `b_*.wav`, `peak_*.wav`, `outro_*.wav`. Each 2-bar chunk is pre-curated for a structural role.

**Why this material.** Cobham's *Spectrum* era has long phrased sections that survive chopping. His drumming sits wide of the grid — the 2-bar chunks preserve swing without locking you into his kit.

**How to use.** Drop `a_*.wav` into Simpler Slicing mode, or onto an audio clip slot with **Follow Actions 2.0**. Next slide.

**Caveat.** The classifier guesses role from energy and spectral features. Re-audition. The tag is a hint, not a contract.

# File versioning — why `v01_mixprint` saves you in eighteen months

Future-you is a different person with worse memory than you think. Name files for that stranger.

The convention that survives.

```
artist_trackname_v01_mixprint.wav       # first full mix bounce
artist_trackname_v02_mixprint.wav       # revision
artist_trackname_v07_mixprint.wav       # final mix, committed
artist_trackname_v07_master.wav         # mastered from v07 mix
artist_trackname_v07_master_club.wav    # louder club variant
artist_trackname_v07_stems.zip          # stems bounced at same point
```

Rules that read paranoid and are not.

- **Never overwrite.** Bump the version. Disk is cheap.
- **Never rename the project file.** Duplicate it, bump the version, keep the old. Live's undo history dies on close.
- **The master is tied to a mix version.** If you re-bounce the mix, you re-master. Do not apply the old master chain to a new mix bounce and call it the same track.
- **Stems and masters share a version number.** `v07_master` was made from `v07_mixprint` from `v07.als`. Breaking that chain is how tracks lose their own lineage.
- **Final is not a word.** The file called `trackname_final.wav` is always wrong. So is `final_FINAL`, `really_final`, and `final_v2`. Numbers do not lie.

In eighteen months, when a label asks for the stems for a remix, you will find the session by version number and bounce from a known-good state. Without the convention you will open three projects that all look like the track and none of them are. <Citation bib="edmprod_intermediate" />

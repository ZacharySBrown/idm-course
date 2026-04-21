# Versioning discipline — the gap both specs missed

Neither Spec A nor Spec B names this. Filling the gap.

**Rule.** Before every bounce, save a timestamped copy of the Live set:

```
~/IDM_COURSE_versions/YYYY-MM-DD_wNN_track_N.als
```

Example: `~/IDM_COURSE_versions/2026-04-20_w10_track_01.als`. Re-edit, re-save as `_02`, `_03`. Never overwrite. Disk is cheap.

**Why here specifically.** The five-mutations method and the Resample-and-Mutate engine both *delete the source*. That is the point — commitment forcing. But if you delete the source and later want Mutation 3 back with inverted sweep, you are stuck. The versioned `.als` is your one-way-back.

**Autechre do this forever.** Booth in *Sound on Sound* April 2004 describes persistent Max patches across albums. <Citation bib="sos_autechre_april_2004" /> The NTS Sessions reportedly used patches from 2011 — forum consensus, not confirmed. <Citation bib="nts_autechre_sessions" /> The archive is the instrument.

**Pattern, one line.** Save timestamped `.als`. Consolidate. Delete. Bounce. Move on.

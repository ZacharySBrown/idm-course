# e03-wavetable — Preset Save Checklist

Save one `.adv` per demo from Live: **right-click the Wavetable title bar → Save Preset →**
`courses/ableton-devices/episodes/e03-wavetable/presets/<id>.adv`. Each preset is the single
source of truth's saved form — it must round-trip with `tutorials/<id>.md`.

**Before saving a flagged preset, set the hand-only device state** (the renderer cannot set these
over our headless LOM path — see `DEMO_VERIFICATION.md`). The flags below tell you exactly what to
set first. Save flagged presets in their **A / sweep-start / pad-end** state as noted, so the .adv
matches step 0 of the tutorial.

Legend for hand-set flags:
`TABLE` = pre-load a specific wavetable/category · `FM`/`MODERN` = set Osc Effect Mode ·
`HI-Q` = set/confirm the Hi-Q toggle · `SPREAD` = Unison Mode = Position Spread (+voices) ·
`MATRIX` = build mod-matrix row(s) by hand · `MACRO` = build Macro mappings · `MPE` = enable MPE ·
`IMPORT` = drag a user WAV onto Osc 1 · `SUB?` = confirm Sub Transpose octave by ear.

---

## Section 3 — Synthesis Deep-Dive (03a–03e)

- [ ] `wt-position-by-hand.adv` — **TABLE** (confirm default Basic Shapes). Save at Osc 1 Pos = 0.0.
- [ ] `wt-ab-two-positions.adv` — **TABLE** (Basic Shapes). Save at Osc 1 Pos = 0.1 (segment A).
- [ ] `wt-zipper-vs-smooth.adv` — **HI-Q** (hand-set; A=Off/B=On), **TABLE** (Basic Shapes).
      ⚠ Demonstrative variable not settable headless — save the Hi-Q-On reference; note Hi-Q dependency.
- [ ] `wt-hiq-on-vs-off.adv` — **HI-Q** (hand-set), **TABLE** (bright/Distortion).
      ⚠ Demonstrative variable not settable headless — save the Hi-Q-On reference; note both dependencies.
- [ ] `wt-fm-inside-wavetable.adv` — **FM** (Osc 1 Effect Mode = FM), **TABLE** (Basic Shapes).
      Save at Osc 1 Effect 1 = 0.0 (sweep start).

## Section 4 — Device Deep-Dive (04b–04e)

- [ ] `wt-modern-fold-sweep.adv` — **MODERN** (Osc 1 Effect Mode = Modern), **TABLE** (Basic Shapes).
      Save at Osc 1 Effect 2 = 0.0 (sweep start).
- [ ] `wt-lfo-to-position.adv` — **MATRIX** (LFO 1 → Osc 1 Pos, amount 40; LFO 1 sync 1/8), **TABLE**.
- [ ] `wt-lfo-attack-bloom.adv` — **MATRIX** (LFO 1 → Osc 1 Pos, amount 35; LFO 1 Attack ~2 s), **TABLE**.
- [ ] `wt-position-spread-chord.adv` — **SPREAD** (Unison = Position Spread, 4 voices), **TABLE**.
      Save at Unison Amount = 0.0 (segment A).

## Section 5 — Patch Walkthrough (05a–05g) — cumulative; save each step

- [ ] `wt-spectra-step1.adv` — **TABLE** (Osc 1 Formants/vocal-choir).
- [ ] `wt-spectra-step2.adv` — **TABLE** (Formants), **MATRIX** (LFO 1 → Osc 1 Pos, 30; LFO 1 Attack ~2 s).
- [ ] `wt-spectra-step3.adv` — **TABLE** (Formants), **MATRIX** (LFO 1 → Pos, 30), **SPREAD** (4 voices).
- [ ] `wt-spectra-step4.adv` — **TABLE** (Osc 1 Formants + Osc 2 Harmonics/bell), **MATRIX** (LFO 1 → Pos, 30),
      **SPREAD** (4 voices), **SUB?** (Sub Transpose idx 0 = octave-down, verify by ear).
- [ ] `wt-spectra-step5.adv` — **TABLE** (Formants + bell), **FM** (Osc 1 Effect Mode = FM),
      **MATRIX** (LFO 1 → Pos 30; LFO 2 → Pos 0 bypassed; Env 2 → Flt 1 Freq 35), **SPREAD**, **SUB?**.
- [ ] `wt-spectra-macro-sweep.adv` — **TABLE** (Formants + bell), **FM**, **SPREAD**, **SUB?**,
      **MATRIX** (LFO 1 → Pos; LFO 2 → Pos), **MACRO** (Macro 1 "Pad ↔ Growl": LFO1→Pos 30→0, LFO2→Pos 0→50,
      Flt 1 Freq 0.8→0.5, Mono Off→On, Glide 0.0→0.1). Save at Macro 1 = 0 (pad end).
- [ ] `wt-spectra-morph-final.adv` — **THE SAVED "Spectra-Morph" PATCH.** Same hand-set state as step 6
      (TABLE + FM + SPREAD + SUB? + MATRIX + MACRO). This is the canonical episode preset.

## Section 6 — IDM Application (06a–06d)

- [ ] `wt-user-table-scan.adv` — **IMPORT** (drag a neutral non-copyrighted WAV onto Osc 1),
      **MATRIX** (Env 2 → Osc 1 Pos, amount 90). Document the source WAV name in the preset comment.
- [ ] `wt-loop-env-sequence.adv` — **FM** (Osc 1 Effect Mode = FM), **MATRIX** (Env 2 → Osc 1 Pos, 90;
      optional LFO 1 → Osc 1 Effect 1, 30 @ 1/16), Env 2 Loop Mode = Loop, **TABLE** (Basic Shapes).
- [ ] `wt-hiq-off-grit.adv` — **MODERN** (Osc 1 Effect Mode = Modern), **HI-Q** (confirm OFF — default,
      do NOT enable), **TABLE** (Distortion/bright).
- [ ] `wt-mpe-pressure-position.adv` — **MPE** (enable on track), **MATRIX** (Pressure → Osc 1 Pos, 80),
      **TABLE** (Basic Shapes).

---

## Summary of hand-set demos (set device state BEFORE Save Preset)

| Hand-set need | Demos |
|---|---|
| **Hi-Q toggle** | `wt-zipper-vs-smooth` (A/B), `wt-hiq-on-vs-off` (A/B), `wt-hiq-off-grit` (confirm OFF) |
| **Effect Mode = FM** | `wt-fm-inside-wavetable`, `wt-spectra-step5`, `wt-spectra-macro-sweep`, `wt-spectra-morph-final`, `wt-loop-env-sequence` |
| **Effect Mode = Modern** | `wt-modern-fold-sweep`, `wt-hiq-off-grit` |
| **Specific table / category** | all 20 need the loaded table confirmed; **specific pre-loads:** `wt-hiq-on-vs-off` & `wt-hiq-off-grit` (Distortion), `wt-spectra-step1–5`/`-macro-sweep`/`-morph-final` (Formants + Osc 2 bell), `wt-user-table-scan` (user import) |
| **Unison = Position Spread** | `wt-position-spread-chord`, `wt-spectra-step3`, `-step4`, `-step5`, `-macro-sweep`, `-morph-final` |
| **Mod-matrix row(s)** | `wt-lfo-to-position`, `wt-lfo-attack-bloom`, `wt-spectra-step2`–`step5`, `-macro-sweep`, `-morph-final`, `wt-user-table-scan`, `wt-loop-env-sequence`, `wt-mpe-pressure-position` |
| **Macro mappings** | `wt-spectra-macro-sweep`, `wt-spectra-morph-final` |
| **MPE enable** | `wt-mpe-pressure-position` |
| **User WAV import** | `wt-user-table-scan` |
| **Sub Transpose by ear** | `wt-spectra-step4`, `-step5`, `-macro-sweep`, `-morph-final` |

**Cannot fully demonstrate headless (note on-mic / supplement with a hand demo):**
`wt-zipper-vs-smooth` and `wt-hiq-on-vs-off` (Hi-Q has no settable proxy);
`wt-position-spread-chord` (proves width, not the spread mode) and
`wt-mpe-pressure-position` (proves a brightness ladder, not MPE per-voice independence).

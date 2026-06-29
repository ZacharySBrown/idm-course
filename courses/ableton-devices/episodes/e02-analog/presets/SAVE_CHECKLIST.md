# e02-analog — Preset Save Checklist

Save every Analog patch as a committed `.adv` so each demo is recallable with one
drag. Procedure for each: build the patch from its tutorial (`tutorials/<id>.md`,
one parameter per row), then **right-click the Analog device title bar → Save
Preset →** save into this folder as `<id>.adv`. Commit the `.adv` files.

> All filter-frequency values in the tutorials are NORMALIZED 0–1 (NOT Hz); set
> them by the normalized value, not by reading a Hz display.

The single source of truth is each demo's `params` step-table in
`clip_manifest.yaml`; the tutorial and the `.adv` are both derived from it and
must round-trip (`gzip -cd` the `.adv`, diff the XML clean against a re-save).

---

## Section 3 — Synthesis deep-dive (6 presets)

- [ ] `an-pwm-sweep.adv` — rect osc, filter open, PW swept 50% → narrow (even harmonics)
- [ ] `an-slope-12-vs-24.adv` — saw at fixed cutoff; A/B `F1 Type` 12 vs 24 dB *(save segment A = 12 dB)*
- [ ] `an-reso-to-self-osc.adv` — saw, LP24, `F1 Resonance` swept 0 → 1 (self-oscillation)
- [ ] `an-reese-detune-sweep.adv` — two saws, `OSC2 Detune` swept 0 → +20 c (beating)
- [ ] `an-pwm-strings.adv` — one rect osc, `O1 PW < LFO` (PWM string ensemble)
- [ ] `an-filter-env-vs-amp-env.adv` — same decay, filter-env vs amp-env; A/B `ab_params` *(save segment A)*
- [ ] `an-drive-sym-vs-asym.adv` — resonant saw; A/B `F1 Drive` Sym2 vs Asym2 *(save segment A = Sym2)*

## Section 4 — Ableton Analog deep-dive (3 presets)

- [ ] `an-error-drift.adv` — 4-voice saw chord; A/B `Key Error` 0 vs 0.35 *(save segment A = 0)*
- [ ] `an-sync-ratio-sweep.adv` — `OSC1 Mode = Sync`, `O1 Sub/Sync` swept 0 → 1 (screaming sync)
- [ ] `an-ms20-series-filter.adv` — resonant HP → resonant LP in series; `F1 Freq` swept
- [ ] `an-unison-supersaw.adv` — saw chord; A/B `Unison On/Off` Off vs On (4 voices + detune) *(save segment A = Off)*

## Section 5 — Patch walkthrough: 303 → Reese (9 presets)

The 303 ladder is built incrementally — each step is the previous patch plus one
move — but **save each step as its own `.adv`** so any step is recallable.

- [ ] `an-303-step1.adv` — mono saw + glide/legato, filter open (the raw source)
- [ ] `an-303-step2.adv` — + resonant LP24 at a mid cutoff (the carve begins)
- [ ] `an-303-step3.adv` — + `F1 Freq < Env` and short `FEG1 Decay` (the per-note wow)
- [ ] `an-303-step4.adv` — `F1 Resonance` up to 0.8 (the squelch)
- [ ] `an-303-step5.adv` — + `F1 Drive = Asym2` and `FEG1 < Vel` (dirt + accent)
- [ ] `an-303-step6.adv` — + `AMP1 Level = 0.85` and automated `F1 Freq` (the full acid line)
- [ ] `an-reese-morph.adv` — OSC2 on + detune +18 c, Sub on, filter env dropped (the pivot)
- [ ] `an-reese-final.adv` — finished Reese (two detuned saws, no sub); the saved Reese half
- [ ] `an-303-reese-final.adv` — **the umbrella "Subtractive-303-Reese" patch.** Not a fresh
      build: it is the A/B `concat_from` of `an-303-step6` (acid) + `an-reese-final` (Reese).
      Save the final morphed device as this name — it is the single patch that yields both basses.

## Section 6 — IDM application (3 presets)

- [ ] `an-digeridoo-drone.adv` — oscillators off, noise-excited high-Q key-tracked LP + LFO (filter-as-oscillator)
- [ ] `an-ms20-scream.adv` — HP→LP series, both reso pushed, cutoffs swept in opposition
- [ ] `an-loop-env-pulse.adv` — one held note, `FEG1 Loop = AD-R` (rhythm from an envelope)

---

**Total: 23 presets** (22 built from `params` step-tables + the `an-303-reese-final`
umbrella patch). For the four A/B demos (`an-slope-12-vs-24`, `an-drive-sym-vs-asym`,
`an-error-drift`, `an-unison-supersaw`, `an-filter-env-vs-amp-env`) save the
**segment-A** configuration; segment B is a hand/split render of the single A/B
variable noted in the tutorial.

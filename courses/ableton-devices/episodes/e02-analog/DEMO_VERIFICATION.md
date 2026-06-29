# e02-analog — Device Demo Verification (pre-render, reference-checked)

Scope: all 23 `device_demos` in `clip_manifest.yaml`, audited against
`tools/device_render/param_maps/analog.json` (172 real LOM params) and against
authoritative subtractive-synthesis references. Live was NOT touched; this is
reference/theory verification + surgical manifest edits only.

## Machine audit (automated, all 23)

- **Param-name audit:** all 50 distinct `params`/`automation`/`ab_*` keys exist
  verbatim in `analog.json`. **0 missing names.** (A wrong name renders silently —
  none found.)
- **Value audit:** every quantized value matches its `value_items` exactly; every
  continuous value is within `[min,max]`. **0 violations** after edits.
- **Renderer wiring confirmed** in `operator_render_osc.py`: `ab_param`/`ab_values`
  (singular) AND `ab_params` (plural, multi-param A/B) both render seg A + seg B and
  concat; `automation` runs in a sweep thread; `concat_from` concatenates already-
  rendered sub-demos in a post-pass. Note: `_render_ab` pops `automation`, so an A/B
  demo cannot also sweep — none of the A/B demos here rely on automation, so OK.
- The renderer's own loudness gate flags `mean < -45 dB` as `quiet`. `an-reese-final`
  measured -47 mean = that gate firing; the fixes below target exactly that.

## Per-demo table

| id | concept | names OK? | isolates 1 var? | reference for the canonical demo | changes made | confidence |
|---|---|---|---|---|---|---|
| an-pwm-sweep | PW → harmonic content (even harmonics appear) | yes | yes (OSC1 PW swept, filter wide open) | SOS subtractive primer: 50% pulse = odd-only; off-50% introduces even harmonics. Correct. | none | high |
| an-slope-12-vs-24 | filter slope → darkness above cutoff | yes | yes (only F1 Type A↔B) | Standard LP pole/slope theory (12 vs 24 dB/oct). C3=262 over ~1 kHz cutoff shows it. | none (silence was the fixed duration bug) | high |
| an-reso-to-self-osc | resonance → self-oscillation | yes | yes (F1 Resonance 0→1 swept) | Barkhausen unity-gain self-osc; canonical Moog/MS-20 resonance sweep. | none | high |
| an-reese-detune-sweep | detune two saws → beating | yes | yes (OSC2 Detune swept; Key Error=0) | Reese bass = detuned-saw interference (Kevin Saunderson, "Just Another Chance", 1988). | none | med-high (held C1 at default AMP1 0.474, but 2 full saws = louder than single-saw cases; left as-is) |
| an-pwm-strings | LFO→PW = one osc like many (PWM strings) | yes | yes (O1 PW < LFO is the routing) | Solina/Juno PWM string-ensemble trick; SOS on PWM. | none | high |
| an-filter-env-vs-amp-env | same env, two destinations | yes (uses `ab_params` plural — renderer supports it) | yes (decay shape held; only destination moves A↔B) | Core subtractive teaching: VCF-env = timbre, VCA-env = loudness. | none (silence was duration bug; `ab_params` confirmed renderable) | high |
| an-drive-sym-vs-asym | sym (odd) vs asym (even) saturation | yes | yes (only F1 Drive Sym2↔Asym2) | Waveshaping theory: symmetric clip = odd harmonics, asymmetric adds even (2nd). Ableton Analog drive modes. | none (silence was duration bug) | high |
| an-error-drift | Error → per-voice tuning drift | yes | yes (only Key Error 0↔0.35; Detune=0 so Error is sole drift) | Analog manual "Error" = random per-voice detune to model analog instability. | none (silence was duration bug) | high |
| an-sync-ratio-sweep | hard-sync ratio → screaming lead | yes | yes (O1 Sub/Sync swept w/ OSC1 Mode=Sync) | Classic hard-sync lead (Prophet/JP); sync ratio sweeps formant. Analog: Sub/Sync slider = sync depth when Mode=Sync. | none | high |
| an-ms20-series-filter | resonant HP → resonant LP series (MS-20 band) | yes | yes (F1 HP swept, F2 LP held; F1 To F2=1, F2 Slave=Off) | Korg MS-20 architecture: HP→LP filters in series. | none | med-high (relies on F1→F2 series routing rendering correctly — a render check, not a param-name issue) |
| an-unison-supersaw | unison + detune → supersaw | yes | yes (only Unison On/Off A↔B) | Roland JP-8000 "Super Saw" (1996) = 7 detuned saws; Analog max is 4 — manifest honestly notes the approximation. | none | high (concept), med (4 ≠ 7 voices — acknowledged) |
| an-303-step1 | 303 src: mono saw + glide/legato | yes | yes (source only) | TB-303 signal path: saw → glide → filter. | none | high |
| an-303-step2 | add resonant 24 dB LP | yes | yes (F1 engaged vs step1 open) | TB-303 24 dB LP. | none | high |
| an-303-step3 | filter env → Freq (per-note "wow") | yes | yes (F1 Freq<Env + short FEG decay) | TB-303 envelope-mod "wow". | none | high |
| an-303-step4 | resonance → squelch | yes | yes (only F1 Resonance 0.4→0.8) | TB-303 high-resonance squelch. | none | high |
| an-303-step5 | asym drive + accent via Env<Vel | yes | yes (Drive=Asym + FEG1<Vel; alt velocities) | TB-303 accent = velocity → filter-env depth; overdrive grit. | none | high |
| an-303-step6 | full acid line, cutoff automated | yes | yes (F1 Freq automation across loop) | Performed 303 cutoff sweep. | **AMP1 Level=0.85** added — level-match the now-louder Reese for the A/B concat | high |
| an-reese-morph | morph 303→Reese (OSC2+detune+sub, drop filter-env) | yes | yes (the morph deltas) | Reese morph; "Sub on" is the narrated move so Sub kept. | **O1 Sub/Sync 0.6→0.5**, **F1 Freq 0.453→0.507**, **AMP1 Level=0.85 added** — held C1 was destined to render quiet (default AMP1 + ~33 Hz sub) | high |
| an-reese-final | finished Reese; beating scales with pitch | yes | yes (pitch C1→C2; constant-cents detune) | Reese = TWO detuned saws (Saunderson 1988); a sub osc is NOT canonical. | **Sub OFF** (was Mode=Sub @0.6 — un-canonical AND the main cause of -47 dB: energy at ~33 Hz, inaudible on phone, ate normalization), **F1 Freq 0.453→0.507**, **AMP1 Level=0.85 added** (patch never set AMP1; default 0.474 ≈ -6.5 dB) | high |
| an-303-reese-final | one saved patch → both basses (A/B concat) | yes | yes (concat of step6 + reese-final) | Inherits the two fixed sub-demos; now level-balanced. | inherits step6 + reese-final edits | high |
| an-digeridoo-drone | play the self-oscillating filter as an instrument | yes | yes (filter-as-osc: osc off, noise-excited, key-tracked, LFO) | Aphex "Digeridoo" (1992) = self-oscillating/resonant analog filter, not a real didgeridoo. Filter-as-oscillator technique = high-Q key-tracked filter excited by NOISE (SOS/MS-20). | **Reworked excitation: Sine→Noise.** A sine at the played pitch was ambiguous (can't tell filter from osc). Now: OSC off, Noise On @0.35 excites the high-Q (0.95) key-tracked LP so the pitched ring is provably the FILTER. **AMP1 Level=0.9 added**; verification text updated to "reedy ring over faint noise floor" (honest vs "near-sine"). | med-high (defensible "filter-as-oscillator" demo; the only one I substantively redesigned — flag for a listen on first render) |
| an-ms20-scream | MS-20 dual filter abused (HP→LP opposed sweeps) | yes | yes (both cutoffs swept in opposition) | MS-20 HP→LP series pushed extreme (Autechre/Tri Repetae move). | none | med-high (same F1→F2 series-render dependency as an-ms20-series-filter) |
| an-loop-env-pulse | looping filter env (AD-R) = rhythm from one note | yes | yes (only FEG1 Loop=AD-R; one held note) | The ep1 rhythmic-demo lesson — looping envelope generates rhythm with no LFO/sequencer. | none | high |

## Summary of manifest edits

1. **an-reese-final** — dropped the un-canonical Sub osc (root cause of the measured
   -47 dB: sub energy at ~33 Hz is inaudible on phones and stole normalization
   headroom), raised cutoff ~610→~870 Hz, and set `AMP1 Level=0.85` (the patch never
   set AMP1, leaving it at the default 0.474 ≈ -6.5 dB — the biggest single cause of
   the quiet render). Concept (pitch-scaled detuned-saw beating) is **preserved and
   strengthened** — Reese is canonically two saws, not saw+sub.
2. **an-reese-morph** — kept Sub (it's the narrated move) but trimmed it to 0.5,
   raised cutoff, and added `AMP1 Level=0.85` so the held C1 lands healthy.
3. **an-303-step6** — added `AMP1 Level=0.85` to level-match the Reese for the
   `an-303-reese-final` A/B concat (otherwise A would be ~6 dB louder than B).
4. **an-digeridoo-drone** — redesigned the excitation from a pitched Sine to low-level
   Noise into a very-high-Q key-tracked LP, so the pitched drone is provably the
   *filter ringing* (the actual "filter-as-oscillator" claim) rather than just a
   filtered sine; added `AMP1 Level=0.9`; updated the verification block to match the
   real timbre (reedy ring over a faint noise floor).

## Items to watch on first render (not blocking)

- **an-reese-detune-sweep** — held C1 at default AMP1 0.474; left as-is because two
  full-level saws are louder than the single-saw cases, but verify it clears -45 dB
  mean; if quiet, add `AMP1 Level` ~0.85 (same fix).
- **an-ms20-series-filter / an-ms20-scream** — depend on F1→F2 *series* routing
  (`F1 To F2`, `F2 Slave=Off`) actually rendering as series in the pipeline. Param
  names are correct; confirm the band-pass/two-peak spectrum appears, else the series
  route isn't engaging.
- **an-digeridoo-drone** — the one substantive redesign; confirm by ear that the
  noise floor stays faint and the key-tracked ring is the dominant, pitched element.
- **an-unison-supersaw** — Analog's 4 unison voices is a genuine but partial stand-in
  for the JP-8000's 7-saw Super Saw; the demo proves the principle, not the exact
  device.

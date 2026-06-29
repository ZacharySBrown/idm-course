# Preset Save Checklist — e01-operator

Save every Operator patch below as a reusable `.adv` so each demo is recallable with one drag
and round-trips against its tutorial. **Procedure for each:** build the patch from its
`tutorials/<id>.md` (or load the rendered set), then in Live **right-click the Operator title
bar → Save Preset → save as `<id>.adv` into this `presets/` folder**. Commit the `.adv`.

Round-trip gate (Gate 7): a fresh build from the tutorial table must produce an identical
sound + analyzer image; `gzip -cd <id>.adv` should show `<Manual Value>` entries matching the
tutorial. Any drift = a changed `<Manual Value>` → fix the patch or the table.

Status legend: ☐ = to save · ⚠ = needs a setting the headless renderer could not set (build/
verify by ear in Live before saving).

---

## Section 3 — Synthesis Deep Dive (concept demos)

- ☐ `op-mod-index-sweep.adv` — index→brightness sweep (Be Attack long fade-in). *(slide 03b)*
- ☐ `op-ratio-1to1.adv` — 1:1 integer, reedy. *(slide 03c)*
- ☐ `op-ratio-1to2.adv` — 1:2 integer, hollow/clarinet. *(slide 03c)*
- ☐ `op-ratio-1to3.adv` — 1:3 integer, sparse hollow. *(slide 03c)*
- ☐ `op-ratio-1-sqrt2.adv` — 1:√2 irrational (Fine 414), bell/gong. *(slide 03c)*
- ☐ `op-ratio-1-phi.adv` — 1:φ irrational (Fine 618), Stria cloud. *(slide 03c)*
- ⚠ `op-feedback-bifurcation.adv` — feedback→complexity ladder. **HEADLESS RENDERER CANNOT SET
  FEEDBACK AUDIBLY** (see `FEEDBACK_FIX.md`). Build the 4-rung feedback ladder (Osc-A Feedb
  0/40/60/70, or a modulator-feedback variant) **by hand in Live, ear-verify the sine→saw→broadband
  progression, then save.** Do not save a headless render of this — it will be a flat sine. *(slide 03e)*

## Section 5 — Patch Walkthrough: Polynomial-Bell (cumulative build, 8 steps)

Each step is a superset of the previous; save all eight so every build slide has its own recall.

- ☐ `op-poly-bell-step1.adv` — Alg. 1, all sines (pure sine). *(slide 05a)*
- ☐ `op-poly-bell-step2.adv` — + carrier A pluck envelope (1/400/−inf/200 ms). *(slide 05b)*
- ☐ `op-poly-bell-step3.adv` — + modulator B at √2 (Fine 414). *(slide 05c)*
- ☐ `op-poly-bell-step4.adv` — + modulator C (Coarse 7) feeding B. *(slide 05d)*
- ⚠ `op-poly-bell-step5.adv` — + **Feedback 30% on C**. Headless renderer under-reads feedback
  (see `FEEDBACK_FIX.md`); **confirm the attack grit by ear in Live before saving.** *(slide 05e)*
- ☐ `op-poly-bell-step6.adv` — + Spread 12% + Filter LP24 OSR ~8 kHz, Drive +3. *(slide 05f)*
- ☐ `op-poly-bell-step7.adv` — + **Osc-B Lev < Vel +50** (velocity→brightness). *(slide 05g)*
- ☐ `op-poly-bell-final.adv` — the saved **Polynomial-Bell** (display name *Polynomial-Bell*);
  same params as step7, auditioned as the C3–Eb3–G3–C4 arpeggio. *(slide 05h — this is THE
  preset the "Save Preset" step in the script produces.)* *(slide 05h)*

  > 📝 Gate 4: step7/final carry **only** `Osc-B Lev < Vel +50`. The `05g` script also names a
  > **Time < Vel +30** routing on B that is not in the rendered patch — reconcile (add it to the
  > patch or trim the line) before SCRIPT LOCK, then re-save if the patch changes.

## Section 6 — IDM Application (rhythmic FM)

- ⚠ `op-rhythmic-single.adv` — Beat-mode carrier @ ≈1/16, B Coarse 11. **Ae Retrig (≈1/16)
  is calibrated by ear** — verify the onset rate in Live and adjust Retrig before saving. *(slide 06a)*
- ⚠ `op-rhythmic-instance2.adv` — Beat-mode carrier @ ≈1/8 dotted, B Coarse 13. **Ae Retrig must
  render at a rate DISTINCT from `op-rhythmic-single`** (the ep1 `single == instance2` failure).
  Ear-verify both rates before saving. *(slide 06b)*
- — `op-rhythmic-layered` — **no preset.** This is an ffmpeg `amix` of the two instances above
  (`mix_from`), not a saved Operator patch. Nothing to save.

  > 📝 Gate 4: `06a` script narrates the **Beat** envelope on **B** (with **A = Trigger**); the
  > rendered patches put **Beat on carrier A** with **B = None**. Reconcile narration ↔ patch
  > before SCRIPT LOCK; re-save if the patch changes.

---

## Summary

| Group | Presets to save | Flagged ⚠ (set/verify by ear in Live) |
|---|---|---|
| Section 3 concept demos | 7 | `op-feedback-bifurcation` |
| Section 5 Polynomial-Bell | 8 | `op-poly-bell-step5` (feedback grit) |
| Section 6 rhythmic FM | 2 (+1 mix, no preset) | `op-rhythmic-single`, `op-rhythmic-instance2` (Retrig rate) |
| **Total** | **17 `.adv` to save** | **4 need ear-verification before save** |

After saving, run the Gate-7 round-trip: rebuild each from its tutorial, render, and diff the
gzip-decompressed XML against the saved `.adv`.

# Probability weights — Any vs specific jumps

Three patterns cover 90% of generative use.

**Pattern 1 — Non-repeating pool.**
- Action A: Play Again · Chance 20
- Action B: Other · Chance 80

Result — mostly variation, occasional self-repeat so the ear does not catch the rotation. Spec A §5.7 baseline. <Citation bib="ableton_live_12_manual" />

**Pattern 2 — Card shuffle.**
- Action A: Any · Chance 100

Pure uniform draw. Any includes the current clip, so ~1-in-N chance of self-repeat in a pool of N.

**Pattern 3 — Directed fills.**
- Main clip: Action A Next · Chance 10 · Action B Play Again · Chance 90
- Fill clip: Action A First · Chance 100

Main plays mostly itself with occasional advance to the next (a fill), which snaps back to First. That is a classic 4-bar-main-plus-every-Nth-fill pattern without writing the sequence. Spec B receipts. <Citation bib="sos_autechre_april_2004" />

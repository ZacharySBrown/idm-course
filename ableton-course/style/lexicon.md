# Lexicon

The `validate_lesson.ts --style` linter greps against the banned list below. Build fails on hit.

---

## BANNED — hard fail on build

Any case-insensitive occurrence in slides, scripts, or episode intros/outros fails the build.

- `sonic journey`
- `unleash`
- `take it to the next level` / `level up your production`
- `game-changing`
- `game-changer`
- `mind-blowing`
- `magic happens`
- `crafting sonic landscapes`
- `sonic landscape`
- `secret sauce`
- `pro tips`
- `synergy`
- `AI-powered`
- `AI-enhanced`
- `unlock the power of`
- `deep dive` (as a noun — "deep dive into" is ok as a verb phrase occasionally)
- `next-level`
- `truly unique`
- `really really` / `very very`

## BANNED — exclamation policy

Zero exclamation points in any student-facing copy. Linter counts them; >0 = fail.

## BANNED — emoji policy

Zero emojis. Unicode range check in linter.

---

## APPROVED — use liberally

- **Gear verbs**: "patched," "routed," "bussed," "summed," "nuked," "crushed," "bounced," "comped," "gated," "chopped"
- **Signal path nouns**: "pre," "send," "return," "bus," "insert," "group," "rack," "chain"
- **Era nouns**: "ADAT era," "SP-1200 era," "MPC3000 era," "tracker era" — when a piece of gear anchors a whole approach
- **Honest adjectives**: "rubbery," "dusty," "clipped," "muddy," "brittle," "anemic," "hot," "lopsided" — descriptive, not laudatory
- **Studio-rat in-jokes**: "committed to tape," "bounced and deleted the source," "printed," "recall-hostile," "recall-friendly"

## APPROVED — gear-specific slang (use when accurate)

- **Fridmann bass** — the overdriven sub-tracked-distorted low-end signature. Must have been defined in W4 before reused.
- **Dilla time** — the un-quantized per-pad swing signature. Defined in W9.
- **Amen break** — the drum break from "Amen, Brother" by The Winstons (1969). Name it explicitly the first time it appears.
- **boomsauce** — Madlib's SP-303 bass processing.
- **chipmunk soul** — Kanye/Just Blaze Re-Pitch-up sample chopping.

## APPROVED — citation shorthand

Use standardized citation shorthand in running text:
- `Tape Op #89` (for the Squarepusher interview)
- `SOS April 2004` (for the Autechre piece)
- `Tape Notes #140` (for the Four Tet episode)
- `Charnas 2022` (for *Dilla Time*)
- `Roads 1996` (for *The Computer Music Tutorial*)
- `Pitchfork 2014` (for Aphex Syro press)

The `<Citation bib="...">` component expands them in HTML.

---

## Tone anti-patterns — style warnings (not hard fail)

Linter warns (doesn't fail) on:
- Paragraphs averaging >2 adjectives per sentence
- Any slide where the first three sentences have no `bib:` citation (top-of-lesson slide exempt only if it's the cold-open contradiction)
- Scripts under 60 seconds of read time for a 45-minute lesson
- Scripts over 180 seconds for a single slide (split the slide instead)

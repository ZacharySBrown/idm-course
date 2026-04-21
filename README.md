# IDM Course — 12 Weeks, 12 Tracks

*Intelligent Dance Music production reverse-engineered from Aphex, Autechre, Four Tet, Squarepusher, Prefuse, Dilla, Premier, Kanye, and Death Grips. Built on Ableton Live 12 + stemforge.*

**Status:** work in progress — multi-agent build underway.

---

## Philosophy

Constraint + recombination beats sound-design rabbit holes. Completion > perfection. Ship 12 tracks in 12 weeks. Reverse-engineer artist methods rather than feature-tour the DAW.

## Repo structure

| Path | What's there |
|---|---|
| [specs/](specs/) | Two source briefs that seeded the course (read-only canon) |
| [style/voice.md](style/voice.md) | Tone bible — every authoring agent reads this |
| [style/lexicon.md](style/lexicon.md) | Banned phrases + approved slang (linter enforces) |
| [style/teaser-calendar.yaml](style/teaser-calendar.yaml) | Six teasers scheduled across 12 weeks |
| [course.yaml](course.yaml) | Master manifest — weeks, pillars, stemforge pipelines, teasers |
| [lessons/](lessons/) | Single source of truth — one directory per lesson |
| [references/bibliography.json](references/bibliography.json) | Canonical citation DB — cite only via `bib:*` IDs |
| [stemforge-demo-material/recipes.yaml](stemforge-demo-material/recipes.yaml) | Per-lesson stemforge CLI invocations |
| [tools/](tools/) | Build pipeline — see [tools/README.md](tools/README.md) |
| [build/](build/) | Generated artifacts (git-ignored; reproducible from sources) |

## The 12 weeks

1. **W1** — [Listen like an engineer, subtract like a producer](lessons/w01-listen-subtract/)
2. **W2** — [The Subtraction method — finish by removing](lessons/w02-subtraction/)
3. **W3** — [Simpler, Drum Rack, one-shots](lessons/w03-simpler-basics/)
4. **W4** — [Warp modes as sound design](lessons/w04-warp-modes/) *· tarbox_road teaser*
5. **W5** — [Aphex Pt.1 — Tuning drums to the track](lessons/w05-aphex-tuning/) *· fredonia_srt teaser · MVP exemplar*
6. **W6** — [Four Tet — subliminal layering & preset discipline](lessons/w06-fourtet-layering/)
7. **W7** — [Squarepusher — hardware hostility & Amen chopping](lessons/w07-squarepusher-chops/) *· tame_impala_boss teaser*
8. **W8** — [Autechre — generative, not random](lessons/w08-autechre-feedback/) *· mgmt_kids_distortion teaser*
9. **W9** — [Vocal chopping — Prefuse, Dilla, Kanye, Premier](lessons/w09-vocal-chopping/)
10. **W10** — [Variation generation — the five mutations](lessons/w10-variation-generation/) *· zaireeka_4cd teaser*
11. **W11** — [Beat switches, inverse drops, and the rub](lessons/w11-beat-switch/)
12. **W12** — [Ship two tracks — mastering, metadata, delivery](lessons/w12-ship-two-tracks/) *· gottinger_alumni teaser*

## How it builds

See [tools/README.md](tools/README.md) for the Wave 4–8 build pipeline. The plan lives at `~/.claude/plans/read-the-specs-in-hazy-galaxy.md`.

## References

PDFs mirrored to `references/pdfs/` for offline (and reMarkable) reading. Paywalled and UGC sources live in [references/links.yaml](references/links.yaml) — link-only, no mirroring.

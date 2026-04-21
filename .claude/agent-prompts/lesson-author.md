# Lesson Author — shared instructions

You are one of 12 parallel lesson-authoring agents. You own exactly one week of an IDM production course. Your job: produce a complete, lint-passing lesson for your assigned week.

## Your write scope (HARD LIMIT)

You may only write inside `lessons/wNN-<slug>/` for your assigned week. No other writes. No touches to `style/`, `references/`, `tools/`, other lessons, or `course.yaml`.

## What you read first (read ALL of these — they are your canon)

1. `/Users/zak/Desktop/IDM_COURSE/specs/compass_artifact_wf-c51f364d-ce3d-4091-afd0-4f796276ecb5_text_markdown.md` — "Zak Handbook" (personal playbook)
2. `/Users/zak/Desktop/IDM_COURSE/specs/compass_artifact_wf-efadee41-f0cf-4413-b6ce-b54c96118223_text_markdown.md` — "Deep Research Compendium" (scholarly reference)
3. `/Users/zak/Desktop/IDM_COURSE/style/voice.md` — tone bible, READ BEFORE WRITING ANY COPY
4. `/Users/zak/Desktop/IDM_COURSE/style/lexicon.md` — banned phrases + approved slang
5. `/Users/zak/Desktop/IDM_COURSE/style/teaser-calendar.yaml` — if your week is listed, you MUST inject the teaser paragraph verbatim-ish
6. `/Users/zak/Desktop/IDM_COURSE/references/bibliography.json` — resolve every citation via a `bib:*` ID; do not invent new ones (the bibliography-expander agent will add more later; if a source you need is missing, flag it in your lesson.yaml `needs_bib:` array rather than fabricating)
7. `/Users/zak/Desktop/IDM_COURSE/stemforge-demo-material/recipes.yaml` — the stemforge invocations pre-declared for your week
8. `/Users/zak/Desktop/IDM_COURSE/course.yaml` — read-only, to understand your lesson's position in the curriculum

## What you produce

Inside `lessons/wNN-<slug>/`:
- `lesson.yaml` — full schema (see below)
- `slides/s01-<name>.md`, `slides/s02-<name>.md`, … — one markdown fragment per slide body. Each is the on-screen content (bullets, images, code blocks, Ableton device notes). Keep each slide body ≤150 words. If it needs more, split the slide.
- `script/s01-<name>.md`, `script/s02-<name>.md`, … — one narration script per slide. Voiced by a dry sardonic male narrator (see voice.md). Markup rules: `[pause Nms]`, `*emphasis*`, `~sardonic pitch-down~`. Each script is 60–180 seconds at ~160 wpm (≈160–480 words). Total lesson script across all slides: target ~28 minutes ≈ 4500 words.
- `script/intro.md`, `script/outro.md` — episode intro + outro (for walking-podcast assembly)

## Target lesson shape

- 8–14 slides, mixing `kind: title | concept | exercise | reference | caveat | teaser`
- Every slide references ≥1 `bib:*` citation OR a `stemforge:*` render
- The first slide is a cold-open contradiction or confession (see voice.md examples)
- The last slide is an exercise with a concrete deliverable, not a motivational kicker
- If your week has a teaser in `teaser-calendar.yaml`, include exactly one slide of `kind: teaser` with the paragraph lifted from the calendar (verbatim-ish) and the citation preserved
- Include a mix of: song examples (specific tracks from your pillar artists), Ableton device instructions (concrete parameter values where possible), and one exercise the student can ship in 30–60 minutes

## lesson.yaml schema (authoritative)

```yaml
id: wNN-<slug>               # must match directory name
week: N
title: "Week N — <short title>"
duration_minutes: 45
pillars: [<pillar_ids>]
concepts: [<concept_tags>]
ableton_surface: [<device_tags>]
prereqs: [<lesson_ids>]

teasers: [<teaser_ids>]       # if any scheduled for this week, declare

stemforge:
  recipes: [<recipe_ids_from_recipes.yaml>]

references:
  - bib:<id>
  - bib:<id>

needs_bib:                    # optional — sources you needed but didn't find in bibliography
  - title: "..."
    reason: "..."

slides:
  - id: s01
    kind: title | concept | exercise | reference | caveat | teaser
    heading: "string"
    body_md: slides/s01-<name>.md       # omit for title/teaser-only slides
    script_md: script/s01-<name>.md
    visuals: []                          # array of {type: spectrogram|waveform|screenshot, src, caption}
    audio_examples: []                   # array of {type: ab|mono, label, a, b?}
    live_set: live-sets/<file>.als       # optional
    deliverable: "string"                # only for kind: exercise

episode:
  title: "IDM W<N> — <subtitle>"
  chapters_from_slides: true
  intro_script: script/intro.md
  outro_script: script/outro.md
  target_runtime_minutes: 28
```

## Style hard rules (lint will fail you on these)

1. **No banned phrases** from `lexicon.md`. Grep your own output before declaring done.
2. **Zero exclamation points.** Zero emojis.
3. **Cold-open contradiction required** — first slide must open with a confession/contradiction, not "welcome to week N."
4. **Receipt-first citations** — cite before claiming. "Tape Op #89, page 34 — Jenkinson says…" not "Jenkinson famously said…"
5. **Caveats inline** — flag uncertainty where it lives ("this is forum consensus, not a confirmed interview")
6. **Close with an exercise or a shrug** — no triumphant wrap-ups

## Style warnings (lint warns, doesn't fail)

- Paragraphs averaging >2 adjectives per sentence
- Scripts under 60 seconds per slide or over 180 seconds per slide
- Total lesson script under ~4000 words (too short for 28-minute episode)

## Artist + song reference material (summary you can trust)

Use the compass_artifact files for depth; this is the quick index:

- **Aphex Twin** — Xtal, Ageispolis (repitched 808 kicks as bass), Windowlicker (spectrogram drawing), Flim (148 BPM, 1/3 kicks 2/4 snares 8th hats), Alberto Balsalm (one loop + drum variations), Vordhosbn (PlayerPro tracker), minipops 67 (Korg Mini Pops 7 MIDI-modded), Avril 14th (Disklavier + solenoid clicks), Drukqs (prepared piano MIDI-driven). Microtuning philosophy: "right in tune is slightly off."
- **Squarepusher** — Hard Normal Daddy (half-speed tape bass), Go Plastic (no-computer: QY700/FS1R/TX81Z/Akai S6000/Eventide Orville), Big Loada (single-pass Boss DR-660 + Akai S950), My Red Hot Car (Amen break resequencing), Come On My Selector (Amen via S950), Iambic 9 Poetry (Orville + live fretless bass), The Metallurgist (sidechain bass to all dynamics).
- **Autechre** — Confield (Max/MSP procedural, Navier-Stokes modulators, nested sequencers), Draft 7.30 (deliberate pullback to straight sequencers), Tri Repetae (2+ bars of silence, minimalist), NTS Sessions (8 hours, persistent Max patches from 2011). Philosophy: "procedural, not random."
- **Four Tet** — Rounds (200–300 samples, AudioMulch + Cool Edit Pro), Three (Omnisphere presets, laptop-speaker mixing, released near-unmastered), Unspoken (40 tracks, pre-written arrangement), Daydream Repeat (4-layer kick stack: main + inaudible sub sine + transient click + sub body), Skater (Omnisphere bass doubled by bell), "Looking At Your Pager" (15% velocity random + 15% probability octave shift). Source: Tape Notes #140.
- **Prefuse 73** — MPC2000XL + Pro Tools, chopped vocal 4-step resample ladder, rejection of computer-IDM.
- **J Dilla** — Get Dis Money (Herbie Hancock vocal + counterpoint bass), Don't Cry (1/32 micro-chopping), Runnin' (Pharcyde — Stan Getz sax chopped + low-passed as bassline), Donuts (Pro Tools + MPC3000, per Charnas — NOT SP-303). Per-pad swing is the signature.
- **DJ Shadow** — Entroducing (MPC60 II + Technics 1200 + ADAT, nothing else). "Building Steam with a Grain of Salt" (Jeremy Storch loop, hand-stepped kick triplets).
- **Hip-hop integration** — Pete Rock "T.R.O.Y.", RZA SP-1200→EPS-16→ASR-10 evolution, Kanye chipmunk soul (Re-Pitch up 4-7 semitones), Kanye/Mike Dean MBDTF (6-12 vocal stack, MicroShift + Auto-Tune 0 retune), DJ Premier "Mass Appeal" (2-sec loop) / "Ten Crack Commandments" (self-scratched loop), Madlib (SP-303 boomsauce, Brazilian hotel recordings).
- **Death Grips** — Takyon (distorted 4-on-floor pitched up, clap/handclap/noise snare layering), System Blower (Williams Sisters tennis grunts stretched into snares).

## Ableton surface reference

- **Generative MIDI**: Rhythm (Steps/Density/Division/Split/Shift/Offset), Seed (±7 semitone acid), Shape, Stacks, Euclidean → Recombine (Rotate/Mirror/Shuffle), Time Warp, Velocity Shaper, Pitch, Ornament (flams/mordents at 1/64), Connect (passing tones Density 70%), Arpeggiate
- **Roar** (Live 12.2+) — Serial/Parallel/MultiBand/Mid-Side/Feedback shapers. IDM drum bus: MultiBand (Low Tube 40% LP 120Hz, Mid Diode 60% BP 800–3kHz, High Shards 25%), Feedback 1/16 at 15%.
- **Meld** — bi-timbral macro oscillators, scale-aware Plate/Membrane resonators, MPE.
- **Granulator III** — Classic/Loop/Cloud, Position/Scan/Grain/Spread, MPE Slide → Position.
- **SoundToys** — Decapitator styles A/E/N/T/P, EchoBoy BoC recipe (Cheap Tape, 1/4 triplet, Feedback 40%, Wobble MAX, Sat 60%), Crystallizer shimmer/glitch/vocal-chop recipes, Devil-Loc snare parallel, MicroShift Style I/II/III, Little AlterBoy.
- **Warp modes** — Complex Pro softens kick transients → layer Beats underneath; Texture Flux 0→100%.
- **Clip envelopes unlinked** — 4-bar audio + 7-bar filter LFO = non-repeating Autechre polymeter.
- **Follow Actions 2.0** — per-scene probability/legato; Any (20%/60%/20%) = non-repeating generative.
- **Bounce Groups** (12.3) — commit generative chains; **Stem Separation** (12.3 Suite Apple Silicon).

## Arrangement methods (5, from the specs)

1. **Subtraction** — densest case first, mute backward
2. **Variation generation** — 5 prescribed mutations (drum swap, bass seed, filter sweep, reverse, new layer)
3. **Skeleton** — line-by-line across sections (kick across all, then snare, then bass…)
4. **Resample-and-mutate** — Mr. Bill method; every 8–16 bars print audio, chop, pitch/reverse/bitcrush, delete source
5. **Bounce-and-Arrange** — Burial method; print stems from Session, rearrange in Arrangement

## Teaching philosophy (don't write it as a slide, embody it)

- Constraint + recombination beats sound-design rabbit holes
- Completion > perfection
- Separate the mentalities: R&D / Writing / Arrangement / Mixing are different sessions
- 45-minute time-box per rabbit hole
- Commit + bounce + delete source
- Rough arrangement first, then detailing
- If you enjoyed a loop for 8 bars, break it (Rick Rubin via both specs)

## Validation (self-check before declaring done)

Run in your head:
1. Did I use any banned phrases from lexicon.md? (grep)
2. Did every slide cite a `bib:*` or a `stemforge:*`? (grep)
3. Did the cold-open slide open with a contradiction? (read it)
4. If a teaser was scheduled for my week, did I include it with citation preserved? (check teaser-calendar.yaml)
5. Is total script content roughly 4000–5000 words for ~28 min runtime?
6. Are there any exclamation points or emojis in my output?

If all pass, write a one-line completion note to stdout summarizing the lesson and return.

## Don't

- Don't render audio (that's Wave 6's job)
- Don't run stemforge (that's Wave 4's job)
- Don't generate screenshots (that's Wave 5 with Zak's whitelisted inbox)
- Don't touch `.als` files (Zak records those)
- Don't edit bibliography.json or other shared files — only your lesson directory
- Don't invent citations. If a source is missing, add to `needs_bib:` array in lesson.yaml
- Don't clean up caveats. If the specs flag something as uncertain, preserve that flag
- Don't write "AI-powered" or any AI marketing language anywhere

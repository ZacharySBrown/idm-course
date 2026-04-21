# Lesson Expander — shared instructions (Wave 9.2)

You are one of 12 parallel lesson-expander agents. You own exactly one week's lesson directory. Your job: take the existing lint-passing lesson and **expand it** into a richer visual reference — 25-35 slides — while preserving the narrated content that powers the walking-podcast.

## Your write scope (HARD LIMIT)

You may only write inside `lessons/wNN-<slug>/` for your assigned week.

**What you MAY modify:**
- `lesson.yaml` (append new slides, add `images_needed`, add new fields to existing slides)
- `slides/*.md` (new body files for new slides)
- **Existing** `slides/*.md` files (minor expansion only — don't rewrite what's there)

**What you MUST NOT touch:**
- `script/*.md` (narration scripts — they drive the existing podcast and are frozen)
- Existing slides' `id` field, `script_md` field, `kind` field (preserves chapter-to-slide mapping)
- Any file outside your lesson directory

## Context to read

1. `/Users/zak/Desktop/IDM_COURSE/.claude/agent-prompts/lesson-author.md` — original shared brief
2. `/Users/zak/Desktop/IDM_COURSE/lessons/wNN-<slug>/lesson.yaml` — existing lesson (read-only canonical reference)
3. `/Users/zak/Desktop/IDM_COURSE/lessons/wNN-<slug>/slides/*.md` — existing slide bodies
4. `/Users/zak/Desktop/IDM_COURSE/specs/compass_artifact_*.md` — both specs, for gear/technique depth
5. `/Users/zak/Desktop/IDM_COURSE/style/voice.md` + `style/lexicon.md`
6. `/Users/zak/Desktop/IDM_COURSE/references/bibliography.json` + `references/songs.json`

## What you produce

Target: **25-35 total slides per lesson**. You're adding approximately 15-25 new slides.

### Four kinds of new slides to add

1. **Image-anchored slides** — break dense concept slides into 2-3 shorter visually-anchored slides. Each new slide: short body (~50 words), one reference image (photo/album art/studio shot), diagram if relevant.

2. **Technical diagram slides** — 2-4 per lesson — dedicated slides that teach a DSP or signal-flow concept with Mermaid or inline SVG. Examples:
   - Warp modes: side-by-side spectrogram of Beats vs Complex Pro
   - Microtuning: cents/Hz/ratio number line
   - Sidechain: compressor curve + gain-reduction envelope
   - Follow Actions: state-machine diagram
   - FM synthesis: operator algorithm tree
   - Kick-stack: frequency-domain bands
   
3. **Gear deep-dive modules (1-2 per week where applicable)** — 12-14 new slides each, all with `kind: gear_deep_dive`. Structure:
   ```
   gd-<gear-slug>-01   title + hero photo of the hardware
   gd-<gear-slug>-02   annotated tour (1/2) — key controls for the technique
   gd-<gear-slug>-03   annotated tour (2/2) — signal path
   gd-<gear-slug>-04   how the technique was executed on this machine (step-by-step)
   gd-<gear-slug>-05   ditto continued + interview receipts
   gd-<gear-slug>-06   underlying algorithm — diagram + explanation
   gd-<gear-slug>-07   algorithm continued + constraints/limits
   gd-<gear-slug>-08   Ableton bridge — screenshot + parameter table
   gd-<gear-slug>-09   parallel Max for Live device(s) that approximate it
   gd-<gear-slug>-10   what else can you do with this hardware — creative uses
   gd-<gear-slug>-11   parallel use cases in modern workflows
   gd-<gear-slug>-12   exercise A — replicate the specific technique
   gd-<gear-slug>-13   exercise B — explore beyond (use the Max device or Ableton equivalent in a novel way)
   ```

4. **Reference/context slides** — artist portraits, studio shots, album art with 1-2 sentences of context. Cheap, high-value.

### New slide field shapes

```yaml
slides:
  # ... existing slides untouched ...

  - id: i05       # image-anchored slide
    kind: concept
    heading: "Tarbox Road Studios, Cassadaga, NY"
    body_md: slides/i05-tarbox-shot.md
    images:
      - src: assets/tarbox-exterior.jpg
        caption: "Tarbox Road Studios in 2012. The building is a converted dairy."
        credit: "Photo: Sound on Sound / Paul White"
        license: "fair-use commentary"

  - id: d03       # diagram-centric slide
    kind: concept
    heading: "Complex Pro vs Beats — what the algorithm actually does"
    body_md: slides/d03-warp-diagram.md
    diagrams:
      - mermaid: |
          graph LR
            A[Audio] --> B{Warp mode}
            B -->|Beats| C[Transient-preserving slice+stretch]
            B -->|Complex Pro| D[Phase vocoder FFT resynth]
        caption: "Simplified dispatch — Beats fails on sustained content; Complex Pro softens transients."

  - id: gd-qy700-01   # gear deep-dive
    kind: gear_deep_dive
    heading: "Yamaha QY700 — the no-computer sequencer"
    body_md: slides/gd-qy700-01-title.md
    images:
      - src: assets/gear-qy700-hero.jpg
        caption: "Yamaha QY700, 1996. 32-track step sequencer + 16-part AWM tone generator."
        credit: "Wikimedia Commons / CC-BY-SA-3.0"
        license: "CC-BY-SA-3.0"

  - id: gd-qy700-04
    kind: gear_deep_dive
    heading: "How Jenkinson tracked Go Plastic on it"
    body_md: slides/gd-qy700-04-workflow.md
    gear_annotations:
      - src: assets/gear-qy700-panel.jpg
        caption: "Highlighting the step-grid + velocity editor workflow"
        callouts:
          - label: "step grid"
            note: "Jenkinson programmed patterns here, one line per track, no real-time play-in."
          - label: "velocity ed"
            note: "Per-step velocity curves applied here, then resampled externally."
          - label: "ch out"
            note: "Routed each track's MIDI out to a dedicated synth/sampler in the chain."

images_needed:       # Wave 10 photo-sourcer reads this from every lesson.yaml
  - slug: qy700-hero
    description: "Yamaha QY700 front panel, centered, on neutral background"
    preferred_angle: "front"
    lesson_context: "W7 gear deep-dive"
  - slug: tarbox-exterior
    description: "Tarbox Road Studios exterior, Cassadaga NY"
    lesson_context: "W4 teaser"
```

### Glossary term tagging (inline in body_md)

Wrap technical terms in `<term key="...">display text</term>` markers:

```md
The transient-preserving approach in <term key="beats_warp">Beats mode</term> slices at
<term key="transient">transient boundaries</term> and stretches each slice, which works well
on drums but falls apart on sustained content like the <term key="drone">drone</term>
washes in Hallogallo. Complex Pro instead does a <term key="phase_vocoder">phase-vocoder FFT
resynth</term> — preserves pitch under speed change but softens attack.
```

Glossary resolver runs at render time; unknown keys pass through as plain text.

## Diagram authoring guidance

- **Mermaid** for: flowcharts, state machines, signal dispatch, architecture trees. Keep them small (≤6 nodes). Use `graph LR` or `graph TD`.
- **Inline SVG** for: waveforms, spectra, DSP curves, annotated photos, anything custom. Write raw SVG in `svg_content` field. Keep viewBox 0 0 800 400 or similar; agents target ~800px wide, dark stroke on neutral fill.
- When in doubt, use Mermaid — the renderer auto-draws it.

## Gear deep-dive authoring — what "good" looks like

Each deep-dive MUST have all 5 sections:
1. **Annotated tour** — don't just show the machine, point to the 4-5 controls that matter for the technique
2. **Technique execution** — step-by-step citing interviews. "Jenkinson, Tape Op #89 page 34: he programmed in step mode, never in real-time. The velocity editor was where the humanization happened — per-step curves, not groove templates."
3. **Underlying algorithm** — the DSP or architecture behind the box. AWM sampling for QY700 tone gen. 6-operator FM for FS1R. 12-bit 26.04kHz companded ADC for SP-1200. Cite Roads or a manufacturer manual.
4. **Ableton/Max bridge** — the parallel modern device. For QY700 → Ableton Push step mode + native MIDI Generators. For FS1R → Ableton Operator (4-op) or external 6-op FM Max device. For SP-1200 → Redux + Decimort 2 + a HPF to simulate 26kHz sample rate.
5. **What else / exercise** — creative uses beyond the original technique + hands-on deliverable

## Irreverent tone enforcement (unchanged from lesson-author.md)

- No banned phrases from `style/lexicon.md`
- Zero exclamation points, zero emojis
- Cold-open contradiction on deep-dive title slides OK
- Receipt-first citations
- Close with exercise or a shrug

## Self-validation

Before declaring done:
1. Slide count: 25-35 total (existing + new)
2. Every new slide cites `bib:*` where claims are made
3. No existing slide's `id`/`kind`/`script_md` field is modified
4. At least one gear deep-dive module exists (if your week has named hardware)
5. `images_needed` array populated
6. `<term>` tags used liberally in new body_md files
7. No banned phrases in grep
8. Diagrams are pedagogically accurate (cite source for any numeric DSP claim)

## Final report

Print:
- Original slide count → new slide count
- Gear deep-dive(s) authored, by slug
- Number of diagrams added
- Number of image_needed entries added
- Anomalies / uncertain technical claims flagged

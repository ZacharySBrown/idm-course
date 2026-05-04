# Handoff — Ableton e01 (Operator), end of 2026-05-04 session

**Date:** 2026-05-04
**Branch:** `claude/bootstrap-ableton-course-0ROY6`
**Last commit (pre-handoff):** `ee4c710 ableton e01: keep audio track armed across the batch`
**Working tree at handoff:** `MidiInstrumentRender.amxd` modified (paste-in of v2 patcher with `[midiin]→[midiout]` passthrough); `build/ableton-devices/` untracked (gitignored).

---

## TL;DR

Phase 3a complete. Phase 3b largely complete. **End-to-end M4L→Live render pipeline works.** 10 of 11 simple Operator demos rendered to AIFF; 1 failed transiently and 4 came out too quiet (manifest tuning issue, not pipeline). 6 complex demos (automation/multi-note/polyrhythm) need manual rendering. Phase 4 ready to go after demo gaps are filled.

---

## What's done

### Pipeline architecture
- `device_render/` is generic — one Python CLI + three M4L devices (`LomProbe`, `MidiInstrumentRender`, `AudioFxRender`) that cover **every** Ableton device the course visits, not just Operator.
- `LomProbe.amxd` dumps any device's LOM parameter table into `param_maps/<class>.json`. Run once per device. **`operator.json` (195 params) is committed**.
- `MidiInstrumentRender.amxd` runs the full pipeline:
  1. apply LOM params to the target instrument (via the dumped param map)
  2. drop a MIDI clip on track 0, looping disabled
  3. arm + start global record + fire MIDI clip + fire empty audio clip slot simultaneously
  4. wait `(midi.length_s + 0.5)` seconds
  5. stop global record + clip slots (audio track stays armed for the next demo)
  6. poll until `clip.is_recording==0` AND file size stable AND >1KB
  7. emit `{event: render_done, src_path, bytes}` over events.ndjson
  8. Python CLI does the file copy with `shutil.copyfile` (Max's File API truncates binary copies on paths with spaces — moved out of JS)
  9. delete clip slots, schedule next demo

### Critical decisions / dead ends discovered
- **`track.freeze()` doesn't exist in LOM**, full stop. Live 11/12 expose `is_frozen` read-only but no callable to trigger freeze. Pivoted to Resampling-track recording, which IS fully LOM-driven. Documented in `device_render/README.md`.
- **Max's `File.readbytes/writebytes` corrupts binary copies** across paths/volumes/spaces. Moved file copy to Python.
- **Default M4L MIDI Effect template needs `[midiin]→[midiout]` passthrough**. Without it the device silently consumes all MIDI. Same with `[plugin~]→[plugout~ 1 2]` for audio effects. Both are in the v2 `.maxpat` files now.
- **Live's session clips loop by default**, causing re-trigger stabs at the end of recordings. JS sets `clip.set("looping", 0)` on each created MIDI clip.
- **Disarming the audio track between demos breaks subsequent runs**. Track stays armed for the whole batch; user disarms manually when done.

### Render results from this session

Rendered to `build/ableton-devices/audio/clips/e01-operator/` (gitignored). 24-bit / 48kHz stereo AIFF.

| Demo | File | Duration | Audio level |
|---|---|---|---|
| op-ratio-1to1 | 1.5MB | 5.0s | ✓ -17 dB mean |
| op-ratio-1to2 | 1.5MB | 5.0s | ✓ -20 dB mean |
| op-ratio-1to3 | 1.5MB | 5.0s | ✓ -17 dB mean |
| op-ratio-1-sqrt2 | 1.5MB | 5.0s | ✓ -17 dB mean |
| op-ratio-1-phi | 1.5MB | 5.0s | ✓ -17 dB mean |
| op-poly-bell-step1 | 1.0MB | 3.5s | ✓ -17 dB mean |
| op-poly-bell-step2 | 0.9MB | 3.0s | ⚠ -90 dB mean (too quiet) |
| op-poly-bell-step3 | 0.9MB | 3.0s | ⚠ -86 dB mean (too quiet) |
| op-poly-bell-step4 | 0.9MB | 3.0s | ⚠ -90 dB mean (too quiet) |
| op-poly-bell-step5 | 0.9MB | 3.0s | ⚠ -86 dB mean (too quiet) |
| op-poly-bell-step6 | — | — | ✗ Recording didn't start (transient `has_clip=0 after fire`) |

The 4 quiet step-2..5 demos have audio (max ~ -55 dB) but the envelope decays to Sustain=0 within 400ms and the manifest sets `Osc-A Level: 0.25` (= -12 dB), so the average across 3 seconds is nearly silent. They're audible but way under the ratio demos.

### Auto-renderable vs manual

11 of 17 operator demos have explicit `params:` blocks in `clip_manifest.yaml`. The other 6 require automation / multi-note MIDI / second Operator instance, which the M4L pipeline can't drive (yet). Those need manual rendering:

- `op-mod-index-sweep` — Level automation 0→100 over 8s
- `op-feedback-bifurcation` — stepped feedback 0→4→6→7
- `op-poly-bell-step7` — velocity routing + soft/hard note pair
- `op-poly-bell-final` — C3-Eb3-G3-C4 16ths, 4 bars
- `op-rhythmic-single` — Beat envelope mode at 1/16
- `op-rhythmic-layered` — two Operator instances at 1/16 + 1/8 dotted

Build them by hand in Live, then either:
- Drop the rendered WAV/AIF into `build/ableton-devices/audio/clips/e01-operator/<demo_id>.aif`, OR
- Use `device_render.py --list` to see which IDs are missing, then drop files matching those IDs

`build_episode.py` already accepts `.wav`, `.aif`, and `.aiff`.

---

## Commits this session

| SHA | Message |
|---|---|
| `3a7f3cb` | Phase 3a + Phase 4 + operator_render scaffold |
| `b3dc68d` | Generalize device_render to cover all 10 episodes |
| `c35fdec` | Operator param map + 11/17 demo params translated |
| `0c12b71` | Pivot device_render from track.freeze to Resampling capture |
| `26749b1` | Poll until Live finalizes the recorded WAV before copying |
| `653eca8` | Fix Task.cancel + handle .aif (Live's default record format) |
| `64c30bc` | Move file copy from Max JS to Python CLI |
| `9a32757` | Add MIDI/audio passthrough to render M4L patchers |
| `8863e68` | Disable MIDI clip looping to avoid re-trigger stab |
| `87e4eef` | Add diagnostics to startResamplingRecord |
| `ee4c710` | Keep audio track armed across the batch |

---

## What's next

### Immediate (10 min)

1. **Re-render `op-poly-bell-step6`** — single-demo retry usually succeeds:
   ```bash
   python courses/ableton-devices/tools/device_render/device_render.py \
       --course-root courses/ableton-devices --episode e01-operator \
       --device Operator --demo op-poly-bell-step6
   ```
   In Live: load_spec → RENDER. If it fails again with `has_clip=0`, restart Live and re-run.

2. **Re-tune step2-5 manifest values** so they're audible. The fix is in [`clip_manifest.yaml`](../../courses/ableton-devices/episodes/e01-operator/clip_manifest.yaml). Suggested change for each step2-5 demo:
   - `Osc-A Level`: bump `0.25` → `0.7` (= ~-3 dB instead of -12 dB), OR
   - `Ae Sustain`: bump `0.0` → `0.25-0.5` so the note has body after the decay phase, OR
   - `Ae Decay`: stretch `0.40` → `0.6` so the envelope falls more slowly

   Then re-render with `--clear` and the full batch. The cleanest fix is probably bumping levels — keeps the pluck character but makes it audible.

3. **Manually render the 6 complex demos** (see "Auto-renderable vs manual" above). For each:
   - Build the patch in Live
   - Use Live's normal Export Audio (Cmd+Shift+R) or Resampling
   - Save the resulting AIF/WAV as `build/ableton-devices/audio/clips/e01-operator/<demo_id>.aif`

### Phase 4 — episode assembly (will work after demos are done)

The narration WAVs aren't rendered yet. Run:
```bash
python shared/tools/render_voiceover.py --course-root courses/ableton-devices --lesson e01-operator
```
~5 min, ~$2 OpenAI cost first run, content-cached after. Produces 34 narration WAVs.

Then:
```bash
python shared/tools/build_episode.py --course-root courses/ableton-devices --lesson e01-operator
```
Produces `build/ableton-devices/audio/episodes/e01-operator.mp3` with chapter markers, every demo spliced after its slide's narration.

### Phase 5 — publish

After audition and tweaks:
1. Port `tools/build_podcast_art.py` for ableton-devices (Operator-themed cover art)
2. `python shared/tools/build_podcast_feed.py --course-root courses/ableton-devices` — already works
3. Subscribe URL: `https://raw.githubusercontent.com/ZacharySBrown/idm-course/main/podcast-ableton.xml`

---

## Open questions / risks

1. **op-poly-bell-step6 transient failure** — `has_clip=0` after fire happened only on step6 in a long batch. Possibly Live rate-limiting clip slot fires after many quick deletes/creates. Restarting Live between batches should fix. If it persists, add a longer cleanup delay between demos (currently 500ms).

2. **Envelope param mapping is empirical**. Operator's Attack/Decay/Sustain/Release params are normalized 0-1, but Live's UI shows them in seconds. The mapping is non-linear. The current values in `clip_manifest.yaml` are first-pass guesses based on rough scale. Audition + adjust.

3. **op-poly-bell-step4+ assumes Algorithm 1 has a C→B path**. Operator's algorithms are 11 distinct topologies; Alg. 1 may route C to A (not B). If audition shows C is hitting A, swap to a topology with C→B (e.g. Alg. 2 or 3 — check the Operator manual's algorithm diagrams).

4. **Filter Freq is 0-1 normalized log-scale**. Step6 uses 0.85 as an estimate for 8 kHz. Adjust by ear.

5. **Step2-5 are too quiet**. See Immediate #2.

---

## Quick start for next session

```bash
cd /Users/zak/zacharysbrown/idm-course
git status                     # confirm working tree (.amxd may still be modified)
git log --oneline -5           # confirm ee4c710 is HEAD

# Inventory rendered demos
python courses/ableton-devices/tools/device_render/device_render.py \
    --course-root courses/ableton-devices --episode e01-operator \
    --device Operator --list

# Re-render the missed step6
python courses/ableton-devices/tools/device_render/device_render.py \
    --course-root courses/ableton-devices --episode e01-operator \
    --device Operator --demo op-poly-bell-step6

# In Live: open ~/Desktop/rendertest Project (or wherever the .als is saved)
#   - audio track must be armed
#   - in MidiInstrumentRender.amxd: load_spec, then RENDER
```

---

## Pointer files (read these first)

| Path | What |
|---|---|
| `courses/ableton-devices/tools/device_render/README.md` | Updated — describes Resampling capture pipeline, template requirement, gotchas |
| `courses/ableton-devices/tools/device_render/m4l/midi_instrument_render.js` | Render JS, ~380 lines, well-commented |
| `courses/ableton-devices/tools/device_render/param_maps/operator.json` | 195-param dump from Live 12 |
| `courses/ableton-devices/episodes/e01-operator/clip_manifest.yaml` | 11/17 demos have `params:` blocks |
| `courses/ableton-devices/tools/device_render/device_render.py` | Python CLI, watches events.ndjson and copies files |
| `docs/handoffs/ableton-ep01-2026-05-04.md` | Earlier handoff (start of session) — context for the whole project |

---

## What the user is doing in parallel

- Has a working render template at `~/Desktop/rendertest Project/<rendertest>.als`. MIDI track 0: MidiInstrumentRender.amxd → Operator. Audio track 1: Resampling input, Monitor Off, Armed.
- Needs to remember: **leave the audio track armed** between renders. JS no longer disarms.
- Will manually render the 6 complex demos once the simple ones are tuned.

The user prefers terse end-of-turn summaries (what changed, what's next, one or two sentences). They will course-correct if something goes sideways.

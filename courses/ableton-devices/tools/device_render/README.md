# device_render

Generic Live-device render pipeline. One Python CLI + three Max for Live
devices that together cover **every** Ableton device the course visits — Operator,
Analog, Wavetable, Meld, Drum Rack, Granulator, warp modes, spectral devices,
racks. Per-device data lives in JSON files; the engine is device-agnostic.

## Architecture

```
device_render.py    ←→    spec.json    ←→    MidiInstrumentRender.amxd
(Python CLI)              (flat-file IPC)         OR
                          events.ndjson      AudioFxRender.amxd
```

- **Python CLI** reads `clip_manifest.yaml`, writes `spec.json`, watches the
  output dir + an NDJSON event log. No subprocess, no socket — just files.
- **M4L devices**:
  - `MidiInstrumentRender.amxd` — for any MIDI instrument (Operator, Analog, …).
    Drops a MIDI clip, freezes the track, copies the WAV.
  - `AudioFxRender.amxd` — for any audio FX chain (warp modes, spectral, racks).
    Triggers a clip in slot 0, freezes, copies.
- **`LomProbe.amxd`** dumps any device's parameter table to
  `param_maps/<class>.json`. Run once per device kind across the course.

The engine in each render device is identical except for the trigger step —
both share the same `loadParamMap`, `applyParams`, freeze loop, and copy code.

## Files

| Path | What |
|---|---|
| `device_render.py` | Generic Python CLI. Reads manifest, writes spec, watches outputs. |
| `m4l/LomProbe.maxpat` | Probe device source — open in Max, Save As `.amxd`. |
| `m4l/lom_probe.js` | LOM-walk JS for the probe. Writes `param_maps/<class>.json`. |
| `m4l/MidiInstrumentRender.maxpat` | MIDI instrument render device source. |
| `m4l/midi_instrument_render.js` | Render JS — MIDI clip path. |
| `m4l/AudioFxRender.maxpat` | Audio FX render device source. |
| `m4l/audio_fx_render.js` | Render JS — audio clip path (no MIDI gen). |
| `param_maps/<class>.json` | (generated) per-device LOM parameter table. |

## One-time setup

### 1. Convert `.maxpat` → `.amxd` (×3, one click each)

For each of the three `.maxpat` files in `m4l/`:

1. Open the `.maxpat` in Max (double-click, or File → Open from Max).
2. **File → Save As…**
3. Choose the matching device type:
   - `LomProbe.maxpat` → **Max for Live MIDI Effect Device** → save as `LomProbe.amxd`
   - `MidiInstrumentRender.maxpat` → **Max for Live MIDI Effect Device** → save as `MidiInstrumentRender.amxd`
   - `AudioFxRender.maxpat` → **Max for Live Audio Effect Device** → save as `AudioFxRender.amxd`
4. Save them anywhere Live can see them — recommended:
   - `~/Music/Ableton/User Library/Presets/MIDI Effects/Max MIDI Effect/` (probe + midi-instrument)
   - `~/Music/Ableton/User Library/Presets/Audio Effects/Max Audio Effect/` (audio-fx)

The canonical sources stay as the `.maxpat` files (text/JSON, diffable). Re-save
the `.amxd` when you upgrade Max.

### 2. Run the probe per device kind

For each Live device the course covers (Operator, Analog, Wavetable, Meld,
Drum Rack, Granulator, …), do this once:

1. New Live set
2. Add a MIDI track
3. Drop the device first (lands at index 0)
4. Drop `LomProbe.amxd` second (lands at index 1) — or any index; the probe walks any track/device you tell it
5. Click `dump 0 0` (or click the bang to dump selected-track/device-0)
6. Max console reports: `wrote N params → /…/param_maps/operator.json` (or `analog.json`, etc.)

The probe writes per-device — running it twice for two different devices
produces two JSON files. They're a few KB each and worth committing since
they're stable across Live versions.

## Workflow (any episode, any device)

```bash
# Generate the spec from clip_manifest.yaml
python courses/ableton-devices/tools/device_render/device_render.py \
    --course-root courses/ableton-devices --episode e01-operator \
    --device Operator

# (other episodes)
# --episode e02-analog --device Analog --demos-key analog_demos
# --episode e05-warp-modes --device Warp --kind audio-fx --demos-key warp_demos
```

Output:
```
Spec → build/ableton-devices/tmp/device-render/e01-operator/spec.json
Events → build/ableton-devices/tmp/device-render/e01-operator/events.ndjson
Output → build/ableton-devices/audio/clips/e01-operator/
Waiting on N demo(s). Click RENDER in MidiInstrumentRender.amxd. Ctrl-C to exit.
```

In Live, with the right template set open:
1. The spec-path message box in the M4L device already points at the spec for
   `e01-operator`. For other episodes, click the message box and edit the path.
2. Click the message box (sends `load_spec`).
3. Click the RENDER button.
4. Watch Max console + the Python terminal — each demo emits `render_start` /
   `render_done` / `error` over the events file.

Flags:
- `--list` — show which demos have been rendered
- `--demo <id>` — only render one demo
- `--clear` — wipe rendered WAVs to force re-render
- `--dry-run` — print spec to stdout

## Filling out `params:` blocks

The render JS only renders demos that have an explicit `params:` map. Out of
the 17 operator demos in `e01`'s manifest, none currently do — only free-form
descriptions. Two paths forward:

1. **Hand-translate descriptions → params.** Add a `params:` block alongside
   each entry in `clip_manifest.yaml`. Use names from `param_maps/operator.json`
   (run the probe first):
   ```yaml
   - id: op-ratio-1to1
     description: "Algorithm 1, A and B sine. Coarse 1:1. Modulator Level 80."
     duration_s: 5
     midi: { note: "C3", length_s: 4.5 }
     params:
       Algorithm: 1
       "Osc-A Wave": "Sine"
       "Osc-B Wave": "Sine"
       "Osc-B Coarse": 1
       "Osc-B Level": 80
   ```

2. **Render complex demos by hand.** Demos with `automation:` blocks
   (`op-mod-index-sweep`, `op-feedback-bifurcation`) or multi-note MIDI
   (`op-poly-bell-step7`, `op-poly-bell-final`, `op-rhythmic-layered`) are
   easier to render manually. Build the patch, freeze + flatten, drop the WAV
   into `build/ableton-devices/audio/clips/<episode>/<demo_id>.wav`. The
   Python CLI's poll loop sees the file appear and marks it done.

## Known gotchas

- **`freeze_state` LOM property name is unverified.** Live's LOM exposes track
  freeze status, but third-party docs disagree on the property name across
  Live versions (`freeze_state`, `is_frozen`, `freezing`). Verify with a
  message-box test in your Live version and adjust `pollFreeze()` if needed.

- **Frozen WAV tail buffer.** Long envelope D/R extends past note-off. Both
  render JS files add `TAIL_BUFFER_S = 0.5s` to the MIDI clip length to
  capture release. Bump if you hear cut-offs.

- **Freeze dir requires saved `.als`.** `track.freeze()` writes WAVs to
  `<set_dir>/Samples/Processed/Freeze/`. An unsaved set has no `set_dir` —
  save the template `.als` somewhere stable before rendering.

- **Track freeze includes the entire device chain before the frozen point**,
  not just the target device. The render M4L device is at index 0, the target
  at index 1 — both are frozen as a unit. The render M4L is pass-through, so
  this is fine.

## Lifting to stemforge later

Once stemforge stabilizes, lift this whole tool into `stemforge/m4l/` as a
sibling of the StemForge bounce pipeline. The patterns are intentionally
similar (NDJSON events, flat-file IPC, JS engine separated from a Python
driver). For now it lives here.

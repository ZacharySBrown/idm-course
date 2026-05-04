# operator_render

Render Operator patches declared in `episodes/e01-operator/clip_manifest.yaml`'s
`operator_demos:` block into `<demo_id>.wav` files, ready for `build_episode.py`
to splice into the assembled MP3.

## Architecture

```
operator_render.py    ←→    spec.json    ←→    OperatorRender.amxd
(Python CLI)                (flat-file IPC)    (Max for Live device)
                            events.ndjson
```

- **Python CLI** reads `clip_manifest.yaml`, writes `spec.json` to a known path,
  then watches the output dir + an NDJSON event log. Has no IPC beyond flat files.
- **M4L device** (you build this in Max — see below) loads `spec.json` on demand,
  applies LOM parameters per demo, drops a MIDI clip on the track, calls
  `track.freeze()`, and copies the frozen WAV to the spec's `output_dir`.

## Status

V1 scaffold. The Python CLI runs end-to-end. The M4L device is **not yet built** —
the JS files in `m4l/` are scaffolds; you need to wire them into a `.maxpat` and
freeze it as `OperatorRender.amxd`. Steps below.

## Files

| Path | What |
|---|---|
| `operator_render.py` | Python CLI — entry point. |
| `m4l/operator_render.js` | Classic JS — parses spec, applies params, freezes, copies WAVs. |
| `m4l/operator_render_probe.js` | One-shot LOM-param dump. Run once to populate `lom_param_map.json`. |
| `lom_param_map.json` | (generated) Operator's LOM parameter index → name table. |

## Setup (one-time)

### 1. Build the LOM-probe device

Open Max. Create a new Max for Live MIDI Effect device.

```
[bpatcher]    [button "DUMP"]
                 |
                 v
    [js operator_render_probe.js]
              |    |
              v    v
        [print]  [print]
```

- Drop a `[js operator_render_probe.js]` box in the patcher
- Wire a button to its inlet (sends `bang`)
- Optionally add `[message dump $1 $2]` boxes for explicit `dump <track_idx> <device_idx>`
- Save as `OperatorProbe.amxd` somewhere convenient (e.g. `~/Music/Ableton/User Library/Presets/MIDI Effects/Max MIDI Effect/`)

### 2. Run the probe

In Live:

1. New Live set
2. Add a MIDI track
3. Drop **Operator** onto the track first (so it's at device index 0)
4. Drop **OperatorProbe.amxd** onto the same track (it'll land at device index 1, but the probe walks any index you tell it)
5. Send `dump 0 0` to the probe (or click the button if you wired it without args — defaults to selected track, device 0)
6. Watch Max console for: `wrote N params → /Users/zak/zacharysbrown/idm-course/courses/ableton-devices/tools/operator_render/lom_param_map.json`

That writes `lom_param_map.json` next to this README. Commit it — it's reference data the render JS needs to translate friendly names like `Algorithm`, `OscB_Coarse`, `OscB_Level` into LiveAPI parameter indices.

### 3. Build the OperatorRender device

```
[message load_spec /abs/path/to/spec.json]
[message render]                 ← user clicks this after loading spec
[message render_one op-ratio-1to1]
              |
              v
   [js operator_render.js]
            |  |  |
            v  v  v
       [print][print][print]    (status, render_done, error outlets)
```

- New M4L MIDI Effect device
- Drop `[js operator_render.js]` (sets `OPERATOR_DEV_IDX = 1` — i.e. expects this device at index 0, Operator at index 1)
- Wire three message boxes to its inlet: `load_spec`, `render`, `render_one`
- Save as `OperatorRender.amxd`

### 4. Build the render template set

Save a `.als` template with this track layout:

```
Track 0: MIDI track named "Operator Render"
    Device chain:
        [0] OperatorRender.amxd
        [1] Operator (default state)
```

Save somewhere known and stable (e.g. `~/Ableton/templates/operator-render.als`).
Open this set every time you render demos.

## Workflow

```bash
# 1. Generate the spec file
python courses/ableton-devices/tools/operator_render/operator_render.py \
    --course-root courses/ableton-devices --episode e01-operator

# Output:
#   Spec → build/ableton-devices/tmp/operator-render/e01-operator/spec.json
#   Events → build/ableton-devices/tmp/operator-render/e01-operator/events.ndjson
#   Output → build/ableton-devices/audio/clips/e01-operator/
#   Waiting on N demo(s). Click RENDER in OperatorRender.amxd. Ctrl-C to exit.

# 2. In Live (with the template set open):
#    a. Send `load_spec /full/path/to/spec.json` to the M4L device
#    b. Click RENDER (sends `render`)
#    c. Watch Max console + Python CLI as each demo renders sequentially

# 3. The Python CLI exits 0 once all demos have produced WAVs.
```

Convenience flags:
- `--list` — show which demos have been rendered, then exit
- `--demo op-ratio-1to1` — only render that one
- `--clear` — wipe rendered WAVs to force re-render
- `--dry-run` — print spec to stdout, don't write anything

## Filling out `params:` blocks in clip_manifest.yaml

The render JS only renders demos that have a `params:` map. Out of the 17 demos
in e01-operator's manifest, none currently have explicit `params:` — only
free-form `description:` strings. Two paths forward:

1. **Hand-translate descriptions → params.** Edit `clip_manifest.yaml` and add a
   `params:` block alongside each `operator_demos` entry. The JS uses the names
   from `lom_param_map.json` directly. Example:
   ```yaml
   - id: op-ratio-1to1
     description: "Algorithm 1, A and B sine. Coarse 1:1. Modulator Level 80. Hold C3 5s."
     duration_s: 5
     midi: { note: "C3", length_s: 4.5 }
     params:
       Algorithm: 1
       "Osc-A Wave": "Sine"
       "Osc-B Wave": "Sine"
       "Osc-B Coarse": 1
       "Osc-B Level": 80
   ```
   (Exact parameter names come from `lom_param_map.json` after the probe runs —
   Operator's exposed names use spaces, not underscores, in some Live versions.)

2. **Fall back to manual rendering for complex demos.** Demos with `automation:`
   blocks (`op-mod-index-sweep`, `op-feedback-bifurcation`) or multi-note MIDI
   (`op-poly-bell-step7`, `op-poly-bell-final`, `op-rhythmic-layered`) are
   easier to render by hand: open Live, build the patch, record/freeze/export,
   drop the WAV into `build/ableton-devices/audio/clips/e01-operator/<demo_id>.wav`
   manually. The Python CLI's poll loop sees the file appear and marks it done.

## Known gotchas

- **`freeze_state` LOM property name is unverified.** Live's LOM exposes track
  freeze status, but the property name varies across Live versions
  (`freeze_state`, `is_frozen`, `freezing` have all appeared in third-party
  docs). The probe script doesn't probe track-level properties; verify in your
  Live version with a quick `[live_set view selected_track] → get freeze_state`
  and adjust `pollFreeze()` if needed.

- **Frozen WAV tail buffer.** Operator releases (especially with long envelope
  D/R) extend past the MIDI clip's note-off. The render JS adds
  `TAIL_BUFFER_S = 0.5s` of silence to the clip length to capture release.
  Increase if you hear cut-offs on long-tail patches.

- **Freeze dir requires saved `.als`.** `freeze_state` writes WAVs to
  `<set_dir>/Samples/Processed/Freeze/`. An unsaved Live set has no `set_dir`,
  so save the template `.als` somewhere stable before rendering.

- **Track freeze includes the entire device chain before the frozen point**,
  not just Operator. The OperatorRender M4L device is at index 0; Operator at
  index 1 — both are frozen as a unit. That's fine because the M4L device is
  pass-through for MIDI/audio.

## Lifting to stemforge later

The handoff plan: once stemforge stabilizes, lift this whole tool into
`stemforge/m4l/` as a sibling of the StemForge bounce pipeline. The patterns
are intentionally similar (NDJSON events, flat-file IPC, JS engine separated
from a Python driver). For now it lives here.

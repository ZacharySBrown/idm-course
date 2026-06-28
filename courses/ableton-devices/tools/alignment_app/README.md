# Alignment Spot-Check

A single-page, zero-build studio utility for A/B-ing **before** vs **after** audio
for every demo slot in a narrated podcast episode. "Before" is a window of the
already-shipped episode MP3 around the demo; "after" is either the same window of a
rebuilt episode MP3 (in-context, with narration) or a bare re-rendered WAV clip when
the episode has not been rebuilt yet. Use it to find demos that shipped silent and
confirm the re-renders are good.

Vanilla JS + Web Audio API. No framework, no build step.

## Run it

Serve from the **repo root** (not this folder) — the report references audio under
`build/…`, which only a root-level server can reach. `fetch`/`decodeAudioData` also
require HTTP, not `file://`.

```bash
cd /Users/zak/zacharysbrown/idm-course      # repo root
python3 -m http.server 8000
```

Then open
<http://localhost:8000/courses/ableton-devices/tools/alignment_app/>.

The app fetches `./alignment_report.json` relative to that URL; the report's
`before_mp3` / `after.path` are written relative to this folder and resolve
correctly under the root server. (Any static server works, e.g. `npx serve`.)

## Data contract

On load the app fetches `./alignment_report.json`, and falls back to
`./sample_report.json` if that 404s. Shape:

```jsonc
{
  "episode_id": "e01-operator",
  "episode_title": "Operator: The FM Machine",
  "generated_at": "2026-06-27T12:00:00Z",
  "before_mp3": "../../path/to/episode.before.mp3", // shared player for BEFORE mp3 windows
  "after_mp3":  "../../path/to/episode.after.mp3",  // shared player for AFTER mp3 windows, or null
  "lead_in_ms": 3500,                               // narration before the demo, inside the window
  "lead_out_ms": 3500,                              // narration after the demo, inside the window
  "duration_ms": 2267107,
  "slots": [
    {
      "index": 0,
      "section": "Section 5 — Patch Walkthrough",  // rows are grouped under section subheaders
      "slide_id": "05a-algo1",
      "heading": "Step 1: Algorithm 1, all sines",
      "cue_id": "op-poly-bell-step1",
      "kind": "operator-demo",                      // or "song-clip" — shown as a badge
      "narration_before": "…Listen.",               // revealed when a row is expanded

      // BEFORE is always an mp3 window of before_mp3. start_ms..end_ms is the play
      // window (narration lead-in + demo + lead-out); demo_start_ms..demo_end_ms is
      // the demo region inside it (drawn as a bracket on the waveform).
      "before": {
        "available": true,
        "source": "mp3",
        "start_ms": 1659600, "end_ms": 1671100,
        "demo_start_ms": 1663100, "demo_end_ms": 1667600,
        "mean_db": -34.5, "peak_db": -10.0,
        "status": "silent"                          // ok | quiet | silent | missing
      },

      // AFTER is one of three shapes:
      //  (a) in-context mp3 window of after_mp3 (when the episode was rebuilt):
      "after": {
        "available": true,
        "source": "mp3",
        "start_ms": 1659600, "end_ms": 1671100,
        "demo_start_ms": 1663100, "demo_end_ms": 1667600,
        "clip_path": "clips/op-poly-bell-step1.wav", // isolated demo wav (metadata; not played)
        "mean_db": -18.0, "peak_db": -3.0,
        "status": "ok"
      }
      //  (b) bare wav clip (no narration) when the episode is not rebuilt yet:
      //      { "available": true, "source": "wav", "in_context": false,
      //        "path": "clips/op-poly-bell-step1.wav", "mean_db": -18.0,
      //        "peak_db": -3.0, "status": "ok" }
      //  (c) not rendered:
      //      { "available": false, "source": "wav", "status": "missing",
      //        "mean_db": null, "peak_db": null }
    }
  ]
}
```

Notes:

- All paths (`before_mp3`, `after_mp3`, `after.path`, `after.clip_path`) are
  **relative to this app folder**.
- A side with `"source": "mp3"` is played by seeking the matching shared `<audio>`
  element (`before` → `before_mp3`, `after` → `after_mp3`) to `start_ms`, playing,
  and auto-stopping at `end_ms` via a timer. The window includes narration lead-in +
  demo + lead-out; the waveform shades the lead-in/lead-out and brackets the demo
  region between `demo_start_ms` and `demo_end_ms`.
- A side with `"source": "wav"` is a bare clip played in full from `path`; the whole
  clip is the demo, so no bracket is drawn.
- `after_mp3` may be `null` (episode not rebuilt). Then no after-as-mp3 slots occur —
  afters are `wav` or `missing` — handled gracefully.
- Only one thing plays at a time across **both** shared mp3 elements and any wav
  `Audio`; clicking any play (or pressing B/A) stops the others.
- Either side may have `"available": false` — its play button is disabled and shows
  "not rendered yet".
- Missing/404 audio is handled gracefully: the button is marked with an error state
  and a "file not found" tooltip; the page never crashes.

## Features

- Header: episode title / id / generated_at + status-color legend.
- Summary strip: slot counts by after-status, plus how many **improved**
  (before silent/quiet → after ok).
- Scrollable list grouped by section, one row per slot: index, heading, `cue_id`
  (mono), kind badge, before→after status chips with mean_db.
- Per-row **Before** / **After** play buttons; only one plays at a time; the active
  row shows a playing indicator.
- Expand a row (click the title or press Enter) to read `narration_before` and see a
  retina-crisp canvas **waveform** of whichever clip was most recently played, with
  an RMS/peak readout. For mp3 windows the narration lead-in/lead-out is shaded and
  the demo region (`demo_start_ms`..`demo_end_ms`) is bracketed; bare wav clips have
  no bracket. Decoding is lazy and cached.
- Filter toggle: **problem slots only** (after ≠ ok, or before silent/quiet).
- Keyboard: `J`/`K` or arrows to move, `B` before, `A` after, `Space` stop,
  `Enter` expand.

## Files

- `index.html` — markup + top bar.
- `app.js` — all logic (loading, playback, decode/waveform, keyboard).
- `style.css` — dark DAW-utility theme.
- `sample_report.json` — fallback/dev fixture (~10 slots, mixed statuses).

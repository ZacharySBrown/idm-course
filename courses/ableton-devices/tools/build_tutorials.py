#!/usr/bin/env python3
"""
build_tutorials.py — turn every Operator demo's patch into a reproducible,
click-by-click tutorial (from the DEFAULT device) and check its preset.

Requirement (from the user): anything done in Ableton must be persisted as a
preset, with a tutorial on how to produce it from the base device; any long
string of device settings must come with a tutorial so it's reproducible.

For each `operator_demos` entry with a `params:` block this emits:
  episodes/<ep>/tutorials/<id>.md   — ordered step table: panel · param · value · (hear)

and reports whether the matching preset exists:
  episodes/<ep>/presets/<id>.adv    — saved from Live (right-click Operator → Save Preset)

The step ORDER is deterministic: Algorithm → Osc A → B → C → D → Filter/Global,
each operator grouped (wave, tuning, level, feedback, envelope). The generated
table is a first draft the Ableton Expert refines (fills the "you should hear"
column, sanity-checks envelope ms). Keeping the tutorial generated FROM the same
params the renderer uses keeps patch, render, and tutorial in sync.

Usage:
  python courses/ableton-devices/tools/build_tutorials.py \
      --course-root courses/ableton-devices --episode e01-operator
  python ... --demo op-poly-bell-final        # one demo
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "shared" / "tools"))
from _course_lib import load_course, episodes_dir, lessons_dir  # noqa: E402

# ── ordering: which params belong to which panel, and in what order ──────────
GLOBAL_FIRST = ["Algorithm"]
OSC_ORDER = ["A", "B", "C", "D"]
# per-operator param suffixes in teaching order
OSC_FIELDS = [
    ("Osc-{o} On", "On/Off"), ("Osc-{o} Wave", "Wave"),
    ("{o} Coarse", "Coarse"), ("{o} Fine", "Fine"),
    ("Osc-{o} Level", "Level"), ("Osc-{o} Feedb", "Feedback"),
    ("Osc-{o} Lev < Vel", "Level<Vel"),
    ("{o}e Mode", "Env Mode"), ("{o}e Retrig", "Env Retrig"),
    ("{o}e Attack", "Env Attack"), ("{o}e Decay", "Env Decay"),
    ("{o}e Sustain", "Env Sustain"), ("{o}e Release", "Env Release"),
]
GLOBAL_LAST = [
    ("Spread", "Spread"), ("Filter On", "Filter On"), ("Filter Type", "Filter Type"),
    ("Filter Slope", "Filter Slope"), ("Filter Circuit - LP/HP", "Filter Circuit"),
    ("Filter Freq", "Filter Freq"), ("Filter Drive", "Filter Drive"),
]


def fmt_val(name: str, v) -> str:
    """Human-readable value. Envelope times are normalized 0-1 in the manifest;
    flag them so the Expert sets the real ms by ear (Operator's mapping is non-linear)."""
    if isinstance(v, float) and name.split()[-1] in ("Attack", "Decay", "Sustain", "Release"):
        return f"{v:g}  *(norm 0–1; set by ear)*"
    if isinstance(v, float) and "Level" in name and 0.0 <= v <= 1.0:
        return f"{v:g}  *(0–1 ≈ {round(v*100)}%)*"
    return f"{v}"


def build_steps(params: dict) -> list[tuple[str, str, str]]:
    """Return ordered (panel, param-label, value) rows from a flat params dict."""
    rows: list[tuple[str, str, str]] = []
    rows.append(("Load", "Default Operator", "init"))
    for p in GLOBAL_FIRST:
        if p in params:
            rows.append(("Global", p, fmt_val(p, params[p])))
    for o in OSC_ORDER:
        on_key = f"Osc-{o} On"
        # skip operators that are off and otherwise unconfigured
        if params.get(on_key) in ("Off", 0) and not any(
            f.format(o=o) in params for f, _ in OSC_FIELDS if "On" not in f):
            if on_key in params:
                rows.append((f"Osc {o}", "On/Off", fmt_val(on_key, params[on_key])))
            continue
        for fmt, label in OSC_FIELDS:
            key = fmt.format(o=o)
            if key in params:
                rows.append((f"Osc {o}", label, fmt_val(key, params[key])))
    for key, label in GLOBAL_LAST:
        if key in params:
            rows.append(("Global", label, fmt_val(key, params[key])))
    return rows


def render_md(demo: dict) -> str:
    did = demo["id"]
    params = demo.get("params") or {}
    concept = demo.get("concept", "")
    desc = demo.get("description", "")
    what = demo.get("what_you_hear", "")
    rows = build_steps(params)
    lines = [
        f"# Patch tutorial — `{did}`",
        "",
        f"**Preset:** `presets/{did}.adv`  ·  **Concept:** {concept or '_(add concept)_'}",
        "",
        (f"> {desc}" if desc else ""),
        (f">\n> **You should hear:** {what}" if what else ""),
        "",
        "Build from a **freshly loaded Operator** (init). One parameter per step;",
        "the right column is your self-check.",
        "",
        "| # | Panel | Parameter | Value | You should now hear |",
        "|---|---|---|---|---|",
    ]
    for i, (panel, label, val) in enumerate(rows):
        hear = "A single pure sine on each note" if val == "init" else ""
        lines.append(f"| {i} | {panel} | {label} | {val} | {hear} |")
    lines += [
        "",
        "_Final check: it should match the preset and the demo render._",
        "_To persist: in Live, right-click the Operator title bar → **Save Preset** → "
        f"save as `{did}` into the episode's `presets/` folder._",
        "",
    ]
    return "\n".join(l for l in lines if l is not None)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--course-root", required=True)
    ap.add_argument("--episode", "--lesson", dest="episode", required=True)
    ap.add_argument("--demo")
    args = ap.parse_args()

    cfg = load_course(args.course_root)
    base = episodes_dir(cfg) if cfg.get("content_kind") == "episode" else lessons_dir(cfg)
    ep_dir = base / args.episode
    man = yaml.safe_load((ep_dir / "clip_manifest.yaml").read_text()) or {}

    tut_dir = ep_dir / "tutorials"
    pre_dir = ep_dir / "presets"
    tut_dir.mkdir(exist_ok=True)
    pre_dir.mkdir(exist_ok=True)

    demos = [d for d in (man.get("operator_demos") or []) if d.get("params")]
    if args.demo:
        demos = [d for d in demos if d["id"] == args.demo]

    written, missing_preset = 0, []
    for d in demos:
        (tut_dir / f"{d['id']}.md").write_text(render_md(d))
        written += 1
        if not (pre_dir / f"{d['id']}.adv").exists():
            missing_preset.append(d["id"])

    print(f"tutorials → {tut_dir}  ({written} written)")
    if missing_preset:
        print(f"\n⚠ {len(missing_preset)} demos have NO saved preset (presets/<id>.adv):")
        for m in missing_preset:
            print(f"    {m}")
        print("  Save each from Live: right-click Operator → Save Preset → presets/<id>.adv")
    return 0


if __name__ == "__main__":
    sys.exit(main())

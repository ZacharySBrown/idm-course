#!/usr/bin/env python3
"""
build_tutorials.py — turn every demo's patch into a reproducible, click-by-click
preset build book, for ANY device (Operator, Analog, Wavetable, Meld, …).

Requirement (from the user): EVERY described preset (a demo with a `params:` block)
must have a build book so it's reproducible from the default device — and the
readiness gate (`shared/tools/episode_readiness.py`, check `preset_books`) FAILS
the build if any is missing. This tool generates/refreshes those books.

Device-generic by construction: instead of hardcoding one device's panels, it
orders each demo's params by their INDEX in that device's dumped param map
(`device_render/param_maps/<device>.json`) — i.e. the device's own natural
parameter order — and groups them by the leading token of the param name
("OSC1", "F1", "AEG1", "A Osc", "Osc 1", …). Enum values are shown with their
human label from the map's `value_items`; normalized-0–1 params are flagged.

For each demo with params it writes:
  episodes/<ep>/tutorials/<id>.md   — step # · panel · parameter · value · (hear)
and reports which presets/<id>.adv files are still missing (saved from Live).

Usage:
  python courses/ableton-devices/tools/build_tutorials.py \
      --course-root courses/ableton-devices --episode e02-analog
  # --device Analog      override the episode.yaml `device:` field
  # --only-missing       only generate books that don't already exist (don't clobber)
  # --demo <id>          a single demo
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "shared" / "tools"))
from _course_lib import load_course, episodes_dir, lessons_dir  # noqa: E402

PARAM_MAPS = HERE / "device_render" / "param_maps"
DEMO_KEYS = ("device_demos", "operator_demos")


def load_param_map(device: str) -> dict:
    """name -> {index, min, max, is_quantized, value_items}. Empty if no map."""
    p = PARAM_MAPS / f"{device.lower()}.json"
    if not p.exists():
        return {}
    data = json.loads(p.read_text())
    return {pp["name"]: pp for pp in data.get("parameters", [])}


def panel_of(name: str) -> str:
    """Group label = the param's leading token(s). 'F1 Freq' -> 'F1';
    'A Osc Type' -> 'A Osc'; 'Osc 1 Pos' -> 'Osc 1'; 'AEG1 Attack' -> 'AEG1'."""
    toks = name.split()
    if not toks:
        return "Global"
    head = toks[0]
    # bi-timbral 'A '/'B ' engines: keep the engine + section word
    if head in ("A", "B") and len(toks) > 1:
        return f"{head} {toks[1]}"
    if len(head) <= 2 and len(toks) > 1 and toks[1].isdigit():  # 'Osc 1'
        return f"{head} {toks[1]}"
    return head


def fmt_val(name: str, v, pm: dict) -> str:
    """Human value, using the device param map: enum index -> label, normalized flag."""
    meta = pm.get(name)
    if meta and meta.get("is_quantized") and meta.get("value_items"):
        items = meta["value_items"]
        if isinstance(v, (int, float)) and 0 <= int(v) < len(items):
            return f"{items[int(v)]}  *(index {int(v)})*"
        return f"{v}"
    if isinstance(v, float) and 0.0 <= v <= 1.0 and meta and float(meta.get("max", 1)) <= 1.0:
        tail = ""
        low = name.lower()
        if any(k in low for k in ("attack", "decay", "release", "time", "rate", "speed", "freq", "pos")):
            tail = "  *(norm 0–1; confirm by ear)*"
        return f"{v:g}{tail}"
    return f"{v}"


def build_steps(params: dict, pm: dict) -> list[tuple[str, str, str]]:
    rows: list[tuple[str, str, str]] = [("Load", "Default device", "init")]
    # device-native order: by param-map index; unknown names sink to the end (stable)
    def key(item):
        meta = pm.get(item[0])
        return (0, meta["index"]) if meta else (1, item[0])
    for name, val in sorted(params.items(), key=key):
        rows.append((panel_of(name), name, fmt_val(name, val, pm)))
    return rows


def render_md(demo: dict, pm: dict, device: str) -> str:
    did = demo["id"]
    rows = build_steps(demo.get("params") or {}, pm)
    what = demo.get("what_you_hear", "")
    lines = [
        f"# Patch build book — `{did}`",
        "",
        f"**Device:** {device}  ·  **Preset:** `presets/{did}.adv`  ·  "
        f"**Concept:** {demo.get('concept', '_(add)_')}",
        "",
        (f"> **You should hear:** {what}" if what else ""),
        "",
        f"Build from a **freshly loaded {device}** (init). One parameter per step;",
        "the right column is your self-check. Values map to the device's real LOM",
        "parameters (enum values show their label + index).",
        "",
        "| # | Panel | Parameter | Value |",
        "|---|---|---|---|",
    ]
    for i, (panel, label, val) in enumerate(rows):
        lines.append(f"| {i} | {panel} | {label} | {val} |")
    sweeps = demo.get("automation") or {}
    if sweeps:
        lines += ["", "**Automation / sweeps** (draw as a clip envelope or move by hand):"]
        for nm, spec in sweeps.items():
            if isinstance(spec, dict) and "from" in spec:
                lines.append(f"- `{nm}`: {spec['from']} → {spec['to']} over {spec.get('ramp_s', '?')}s")
    if demo.get("ab_param"):
        lines += ["", f"**A/B:** flip `{demo['ab_param']}` between {demo['ab_values']} (one variable, all else held)."]
    lines += [
        "",
        f"_To persist: in Live, right-click the {device} title bar → **Save Preset** → "
        f"save as `{did}` into this episode's `presets/` folder._",
        "",
    ]
    return "\n".join(l for l in lines if l is not None)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--course-root", required=True)
    ap.add_argument("--episode", "--lesson", dest="episode", required=True)
    ap.add_argument("--device")
    ap.add_argument("--demo")
    ap.add_argument("--only-missing", action="store_true")
    args = ap.parse_args()

    cfg = load_course(args.course_root)
    base = episodes_dir(cfg) if cfg.get("content_kind") == "episode" else lessons_dir(cfg)
    ep_dir = base / args.episode
    ep_yaml = yaml.safe_load((ep_dir / "episode.yaml").read_text()) or {}
    device = args.device or ep_yaml.get("device", "Operator")
    pm = load_param_map(device)
    if not pm:
        print(f"[warn] no param map for {device!r} at {PARAM_MAPS}/{device.lower()}.json — "
              f"ordering falls back to alphabetical, values shown raw")

    man = yaml.safe_load((ep_dir / "clip_manifest.yaml").read_text()) or {}
    demos = []
    for k in DEMO_KEYS:
        demos += man.get(k) or []
    demos = [d for d in demos if d.get("params")]
    if args.demo:
        demos = [d for d in demos if d["id"] == args.demo]

    tut_dir = ep_dir / "tutorials"
    pre_dir = ep_dir / "presets"
    tut_dir.mkdir(exist_ok=True)
    pre_dir.mkdir(exist_ok=True)

    written, skipped, missing_preset = 0, 0, []
    for d in demos:
        out = tut_dir / f"{d['id']}.md"
        if args.only_missing and out.exists():
            skipped += 1
        else:
            out.write_text(render_md(d, pm, device))
            written += 1
        if not (pre_dir / f"{d['id']}.adv").exists():
            missing_preset.append(d["id"])

    print(f"tutorials → {tut_dir}  ({written} written, {skipped} kept) for device {device!r}")
    if missing_preset:
        print(f"\n⚠ {len(missing_preset)} described presets have NO saved .adv "
              f"(save from Live → presets/<id>.adv):")
        for m in missing_preset:
            print(f"    {m}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

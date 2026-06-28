#!/usr/bin/env python3
"""
make_render_template.py — author a render-ready Ableton Live set with an
Operator instrument, by splicing Live's factory Operator default device into a
known-valid factory template. Lets us drive a fully-headless Operator render
(see operator_render_osc.py) without the user hand-building a set.

Why splice: AbletonOSC / the Live Object Model cannot *instantiate* a device
(no "load Operator" call). So we take a factory template that already loads
cleanly in this exact Live build, and replace the first MIDI track's instrument
with the factory Operator.adv device block. The resampling capture track is NOT
baked in — operator_render_osc.py creates and routes it over OSC at run time.

Output (committed so the build is reproducible):
    courses/ableton-devices/tools/device_render/templates/operator-render/operator-render.als
    courses/ableton-devices/tools/device_render/templates/operator-render/Samples/Recorded/   (Live writes resampled .aif here)

Validate after generating: open it in Live and confirm an Operator appears on
track 1 (operator_render_osc.py --selftest probes this over OSC).

Usage:
    python courses/ableton-devices/tools/device_render/make_render_template.py
    python ... --seed "/path/to/Some Template.als" --live-app "/Applications/Ableton Live 12 Beta.app"
"""
from __future__ import annotations

import argparse
import gzip
import sys
from pathlib import Path

DEFAULT_LIVE_APP = "/Applications/Ableton Live 12 Beta.app"
SEED_REL = "Contents/App-Resources/Core Library/Templates/Quick Start Beat.als"
OPERATOR_ADV_REL = "Contents/App-Resources/Core Library/Defaults/Instruments/Operator.adv"


def read_gzip_xml(path: Path) -> str:
    with gzip.open(path, "rb") as f:
        return f.read().decode("utf-8")


def write_gzip_xml(path: Path, xml: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(path, "wb") as f:
        f.write(xml.encode("utf-8"))


def extract_operator_block(adv_xml: str) -> str:
    """Pull the <Operator ...>...</Operator> device element out of an .adv preset."""
    start = adv_xml.find("<Operator")
    end = adv_xml.rfind("</Operator>")
    if start < 0 or end < 0:
        raise SystemExit("could not find <Operator>…</Operator> in Operator.adv")
    return adv_xml[start:end + len("</Operator>")]


def first_midi_track_devices_span(xml: str) -> tuple[int, int]:
    """Return (inner_start, inner_end) of the first MIDI track's instrument
    <Devices> … </Devices> inner content. Depth-aware: the instrument may be a
    rack whose branches contain their own nested <Devices>, so we must walk to
    the MATCHING close tag, not the first one."""
    mt = xml.find("<MidiTrack ")
    if mt < 0:
        raise SystemExit("seed has no <MidiTrack>")
    dev_open = xml.find("<Devices>", mt)
    if dev_open < 0:
        raise SystemExit("first MIDI track has no <Devices>")
    inner_start = dev_open + len("<Devices>")
    # walk forward tracking <Devices>/</Devices> depth (also handle <Devices/>)
    depth = 1
    i = inner_start
    while depth > 0:
        nxt_open = xml.find("<Devices>", i)
        nxt_close = xml.find("</Devices>", i)
        if nxt_close < 0:
            raise SystemExit("unterminated <Devices> on first MIDI track")
        if nxt_open != -1 and nxt_open < nxt_close:
            depth += 1
            i = nxt_open + len("<Devices>")
        else:
            depth -= 1
            i = nxt_close + len("</Devices>")
            if depth == 0:
                return inner_start, nxt_close
    raise SystemExit("could not match </Devices>")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--live-app", default=DEFAULT_LIVE_APP)
    ap.add_argument("--seed", help="override seed .als (default: Quick Start Beat)")
    ap.add_argument("--out", help="output .als path")
    args = ap.parse_args()

    live = Path(args.live_app)
    seed = Path(args.seed) if args.seed else live / SEED_REL
    adv = live / OPERATOR_ADV_REL
    for p in (seed, adv):
        if not p.exists():
            sys.stderr.write(f"missing: {p}\n")
            return 2

    repo_root = Path(__file__).resolve().parents[4]
    out = Path(args.out) if args.out else (
        repo_root / "courses/ableton-devices/tools/device_render/templates"
        / "operator-render" / "operator-render.als"
    )

    seed_xml = read_gzip_xml(seed)
    op_block = extract_operator_block(read_gzip_xml(adv))

    inner_start, inner_end = first_midi_track_devices_span(seed_xml)
    new_xml = seed_xml[:inner_start] + "\n" + op_block + "\n" + seed_xml[inner_end:]

    # sanity: well-formed XML + exactly one Operator device root
    import xml.etree.ElementTree as ET
    try:
        ET.fromstring(new_xml)
    except ET.ParseError as e:
        raise SystemExit(f"spliced set is not well-formed XML: {e}")
    n_dev = new_xml.count("<Operator>")
    if n_dev != 1:
        sys.stderr.write(f"[warn] expected 1 <Operator> device root, got {n_dev}\n")

    write_gzip_xml(out, new_xml)
    (out.parent / "Samples" / "Recorded").mkdir(parents=True, exist_ok=True)

    print(f"Seed:     {seed}")
    print(f"Operator: {adv.name} ({len(op_block)} bytes spliced)")
    print(f"Wrote:    {out}")
    print(f"Recorded: {out.parent / 'Samples' / 'Recorded'}")
    print("\nNext: open this set in Live, then run operator_render_osc.py "
          f"--project '{out.parent}'")
    return 0


if __name__ == "__main__":
    sys.exit(main())

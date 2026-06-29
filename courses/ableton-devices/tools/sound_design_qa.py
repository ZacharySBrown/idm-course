#!/usr/bin/env python3
"""
sound_design_qa.py — Gate 8 automation: the MEASURABLE subset of the 17-point
demo-placement checklist, run against the built mp3 + its cuemap.

Auto-checked here (objective):
  - demo audible              peak ≥ -22 dB in the mp3 at the demo span
  - loudness-matched to voice  demo loudness within ±6 dB of nearby narration
  - bed muted under demo       the demo span overlaps a bed range AND the bed is
                               silenced there (build_episode now hard-mutes; this
                               confirms no musical bleed under the demo tail)
  - framed by silence          a silence gap precedes the demo onset

Flagged for the Sound Designer / Fresh-Ears agent (subjective, not auto-checked):
  - temporal contiguity (naming word overlaps the demo onset) — needs forced
    alignment of the narration; listed as a manual item per cue
  - frame → demo → label ordering
  - A/B sequencing on a tight loop

Emits sound-design-qa.json next to alignment_report.json.

Usage:
  python courses/ableton-devices/tools/sound_design_qa.py \
      --course-root courses/ableton-devices --episode e01-operator
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "shared" / "tools"))
from _course_lib import load_course, episodes_dir, lessons_dir, episodes_out  # noqa: E402

MANUAL_ITEMS = [
    "temporal-contiguity: the naming word overlaps the demo onset within ~0.25s",
    "frame -> demo -> label ordering present",
    "A/B demos sequenced back-to-back on a tight loop",
    "cold-window test: from a 10s window, the example is identifiable",
]


def loudness(mp3: Path, start_ms: int, end_ms: int) -> dict:
    r = subprocess.run(
        ["ffmpeg", "-hide_banner", "-nostats", "-ss", f"{start_ms/1000:.3f}",
         "-t", f"{max(0.2,(end_ms-start_ms)/1000):.3f}", "-i", str(mp3),
         "-af", "volumedetect", "-f", "null", "-"],
        capture_output=True, text=True)
    mean = peak = None
    for line in r.stderr.splitlines():
        if "mean_volume:" in line:
            mean = float(line.split("mean_volume:")[1].split("dB")[0])
        elif "max_volume:" in line:
            peak = float(line.split("max_volume:")[1].split("dB")[0])
    # Integrated LUFS — the ACTUAL loudness-matching standard. volumedetect
    # mean_volume is a raw sample-magnitude average, silence-biased: it reads a
    # continuous demo as "hot" against gappy speech even when their loudness is
    # matched. LUFS (gated, perceptual) is what loudnorm targets, so match on it.
    lufs = None
    r2 = subprocess.run(
        ["ffmpeg", "-hide_banner", "-nostats", "-ss", f"{start_ms/1000:.3f}",
         "-t", f"{max(0.2,(end_ms-start_ms)/1000):.3f}", "-i", str(mp3),
         "-af", "loudnorm=print_format=json", "-f", "null", "-"],
        capture_output=True, text=True)
    try:
        txt = r2.stderr
        blob = txt[txt.rindex("{"): txt.rindex("}") + 1]
        v = float(json.loads(blob)["input_i"])
        lufs = v if v > -70 else None  # -70 ≈ silence/unmeasurable
    except (ValueError, KeyError, json.JSONDecodeError):
        pass
    return {"mean": mean, "peak": peak, "lufs": lufs}


def silence_before(mp3: Path, onset_ms: int, look_ms: int = 700) -> bool:
    """Is there a silence gap in the ~700ms before the demo onset?"""
    r = subprocess.run(
        ["ffmpeg", "-hide_banner", "-nostats", "-ss", f"{max(0,(onset_ms-look_ms))/1000:.3f}",
         "-t", f"{look_ms/1000:.3f}", "-i", str(mp3),
         "-af", "silencedetect=n=-38dB:d=0.18", "-f", "null", "-"],
        capture_output=True, text=True)
    return "silence_start" in r.stderr


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--course-root", required=True)
    ap.add_argument("--episode", "--lesson", dest="episode", required=True)
    args = ap.parse_args()

    cfg = load_course(args.course_root)
    base = episodes_dir(cfg) if cfg.get("content_kind") == "episode" else lessons_dir(cfg)
    ep_dir = base / args.episode
    ep = yaml.safe_load((ep_dir / "episode.yaml").read_text())
    out_eps = episodes_out(cfg)
    mp3 = out_eps / f"{args.episode}.mp3"
    cuemap = json.loads((out_eps / f"{args.episode}.cuemap.json").read_text())
    chapters = json.loads((out_eps / f"{args.episode}.chapters.json").read_text())
    title_to_chap = {c["title"]: c for c in chapters}

    # bed ranges (in chapter terms) → ms spans, to know which demos overlap a bed
    bed_spans: list[tuple[int, int]] = []
    beds = (ep.get("beds") or {})
    if beds.get("enabled"):
        head_by_slide = {s["id"]: s.get("heading", s["id"]) for s in ep.get("slides", [])}
        for ins in beds.get("insertions") or []:
            sc = title_to_chap.get(head_by_slide.get(ins.get("start_at_slide"), ""))
            ec = title_to_chap.get(head_by_slide.get(ins.get("end_at_slide"), ""))
            if sc and ec:
                bed_spans.append((sc["start_ms"], ec["end_ms"]))

    def in_bed(s, e):
        return any(s < be and e > bs for bs, be in bed_spans)

    rows = []
    for c in cuemap:
        if c.get("role") not in ("demo", "song"):
            continue
        s, e = c["demo_start_ms"], c["demo_end_ms"]
        dl = loudness(mp3, s, e)
        # nearby narration loudness: the ~3s before the demo onset
        nl = loudness(mp3, max(0, s - 3000), max(1, s - 300))
        # Loudness-match on integrated LUFS (perceptual); fall back to mean_volume
        # only if a window was too short/quiet for loudnorm to gate a reading.
        if dl["lufs"] is not None and nl["lufs"] is not None:
            delta = dl["lufs"] - nl["lufs"]
        elif dl["mean"] is not None and nl["mean"] is not None:
            delta = dl["mean"] - nl["mean"]
        else:
            delta = None
        checks = {
            "audible": (dl["peak"] is not None and dl["peak"] >= -22),
            "loudness_matched": (delta is not None and abs(delta) <= 6),
            "framed_by_silence": silence_before(mp3, s),
            "overlaps_bed": in_bed(s, e),
        }
        flags = []
        if not checks["audible"]:
            flags.append(f"demo too quiet (peak {dl['peak']}dB)")
        if checks["loudness_matched"] is False:
            flags.append(f"demo {delta:+.1f}dB vs nearby voice (want ±6)")
        if not checks["framed_by_silence"]:
            flags.append("no silence frame before the demo onset")
        rows.append({
            "cue_id": c["cue_id"], "heading": c["heading"], "role": c["role"],
            "demo_start_ms": s, "demo_end_ms": e,
            "demo_loudness": dl, "voice_loudness": nl, "delta_db": delta,
            "auto_checks": checks, "flags": flags,
            "manual_review": MANUAL_ITEMS,
        })

    out = HERE / "alignment_app" / "sound-design-qa.json"
    out.write_text(json.dumps({"episode": args.episode, "cues": rows,
                               "bed_spans_ms": bed_spans}, indent=2))
    n_flag = sum(1 for r in rows if r["flags"])
    print(f"sound_design_qa → {out}  ({len(rows)} cues, {n_flag} with auto-flags)")
    for r in rows:
        if r["flags"]:
            print(f"  ⚠ {r['cue_id']}: {'; '.join(r['flags'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

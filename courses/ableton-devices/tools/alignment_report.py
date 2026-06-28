#!/usr/bin/env python3
"""
alignment_report.py — emit alignment_report.json for the spot-check web app.

For every cued demo slot in an episode it records:
  - slide id / heading / section
  - cue id + kind (operator-demo | song-clip)
  - the narration text right before the cue ("…Listen.")
  - BEFORE: where that moment sits in the *shipped* episode mp3 (snapshot
    e01-operator.before.mp3) + measured loudness of the demo window
  - AFTER: the freshly re-rendered standalone clip + its loudness (or
    available:false if not rendered yet)

Writes the report into the web app folder so it's served alongside the page:
  courses/ableton-devices/tools/alignment_app/alignment_report.json

Usage:
  python courses/ableton-devices/tools/alignment_report.py \
      --course-root courses/ableton-devices --episode e01-operator
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "shared" / "tools"))
from _course_lib import load_course, episodes_dir, lessons_dir, build_audio, narration_out, episodes_out  # noqa: E402

CUE_RE = re.compile(r"^\s*\[cue:\s*([a-zA-Z0-9_-]+)\]\s*$", re.MULTILINE)
MARKER_RE = re.compile(r"\[(pause|bed|cue)[^\]]*\]")

SECTION_OF = [
    ("01", "Cold Open"), ("02", "Section 2 — FM History"),
    ("03", "Section 3 — Synthesis Deep Dive"), ("04", "Section 4 — Ableton Deep Dive"),
    ("05", "Section 5 — Patch Walkthrough"), ("06", "Section 6 — IDM Application"),
]


def section_for(slide_id: str) -> str:
    for pfx, name in SECTION_OF:
        if slide_id.startswith(pfx):
            return name
    return "Other"


def measure_db(path: Path, start_s: float | None = None, dur_s: float | None = None) -> dict:
    cmd = ["ffmpeg", "-hide_banner", "-nostats"]
    if start_s is not None:
        cmd += ["-ss", f"{start_s:.3f}"]
    cmd += ["-i", str(path)]
    if dur_s is not None:
        cmd += ["-t", f"{dur_s:.3f}"]
    cmd += ["-af", "volumedetect", "-f", "null", "-"]
    r = subprocess.run(cmd, capture_output=True, text=True)
    mean = peak = None
    for line in r.stderr.splitlines():
        if "mean_volume:" in line:
            mean = float(line.split("mean_volume:")[1].split("dB")[0])
        elif "max_volume:" in line:
            peak = float(line.split("max_volume:")[1].split("dB")[0])
    return {"mean": mean, "peak": peak}


def status_from_db(mean: float | None, peak: float | None = None) -> str:
    # Plucks decay to silence within their clip, so MEAN over the demo window is
    # misleadingly low even when the attack is loud. Use PEAK as the primary
    # audibility signal when available; fall back to mean.
    if mean is None and peak is None:
        return "missing"
    if peak is not None:
        if peak <= -40:
            return "silent"
        if peak <= -22:
            return "quiet"
        return "ok"
    if mean <= -45:
        return "silent"
    if mean <= -30:
        return "quiet"
    return "ok"


def narration_chunks(script_md: str) -> list[tuple[str, str | None]]:
    """Return [(text_before_cue, cue_id_or_None), ...] from a script."""
    parts = CUE_RE.split(script_md)
    # re.split with one capture group yields [text, cue, text, cue, ..., text]
    out = []
    i = 0
    while i < len(parts):
        text = MARKER_RE.sub("", parts[i]).strip()
        text = re.sub(r"\s+", " ", text)
        cue = parts[i + 1] if i + 1 < len(parts) else None
        out.append((text, cue))
        i += 2
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--course-root", required=True)
    ap.add_argument("--episode", "--lesson", dest="episode", required=True)
    ap.add_argument("--out", help="output json (default: alignment_app/alignment_report.json)")
    ap.add_argument("--lead-in-ms", type=int, default=1200,
                    help="narration to play before each demo (lead-in) — minimal, just to hear the edge")
    ap.add_argument("--lead-out-ms", type=int, default=1200,
                    help="narration to play after each demo (lead-out) — minimal, just to hear the edge")
    args = ap.parse_args()

    cfg = load_course(args.course_root)
    content_kind = cfg.get("content_kind", "lesson")
    base = episodes_dir(cfg) if content_kind == "episode" else lessons_dir(cfg)
    ep_dir = base / args.episode
    ep = yaml.safe_load((ep_dir / "episode.yaml").read_text())

    # demo durations (manifest) — used to isolate the demo region inside a
    # chapter so the BEFORE loudness reflects the demo, not the narration tail.
    manifest = yaml.safe_load((ep_dir / "clip_manifest.yaml").read_text()) or {}
    demo_dur: dict[str, float] = {}
    for d in manifest.get("operator_demos", []) or []:
        if d.get("duration_s"):
            demo_dur[d["id"]] = float(d["duration_s"])

    def parse_ts(s) -> float:
        s = str(s)
        if ":" in s:
            m, sec = s.split(":")
            return int(m) * 60 + float(sec)
        return float(s)

    for c in manifest.get("song_clips", []) or []:
        if c.get("start") is not None and c.get("end") is not None:
            demo_dur[c["id"]] = max(0.5, parse_ts(c["end"]) - parse_ts(c["start"]))

    # Slides with a trailing transition clip: the demo isn't at the chapter tail,
    # so the BEFORE approximation must subtract the transition (+ inter-piece gap).
    trans_after: dict[str, str] = {}
    tcfg = ep.get("transitions") or {}
    if tcfg.get("enabled"):
        for ins in tcfg.get("insertions") or []:
            if ins.get("after_slide") and ins.get("clip_id"):
                trans_after[ins["after_slide"]] = ins["clip_id"]

    clips_dir = build_audio(cfg) / "clips" / args.episode

    def clip_dur_ms(cid: str) -> int:
        for ext in (".wav", ".aif", ".aiff"):
            p = clips_dir / f"{cid}{ext}"
            if p.exists():
                r = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                                    "format=duration", "-of", "csv=p=0", str(p)],
                                   capture_output=True, text=True)
                try:
                    return int(float(r.stdout.strip()) * 1000)
                except ValueError:
                    return 0
        return 0
    out_eps = episodes_out(cfg)
    before_mp3 = out_eps / f"{args.episode}.before.mp3"
    before_chapters_p = out_eps / f"{args.episode}.before.chapters.json"
    chapters = json.loads(before_chapters_p.read_text()) if before_chapters_p.exists() else []
    chap_by_title = {c["title"]: c for c in chapters}
    total_ms = chapters[-1]["end_ms"] if chapters else 0

    # AFTER context: once the episode is rebuilt with the fresh demos, the new
    # <ep>.chapters.json gives each slide's span in the new mp3. We locate the
    # demo by the same chapter-tail method as "before" so both sides are
    # symmetric, and play it in-context (narration lead-in/out) from the new mp3.
    after_mp3 = out_eps / f"{args.episode}.mp3"
    after_chapters_p = out_eps / f"{args.episode}.chapters.json"
    after_cuemap_p = out_eps / f"{args.episode}.cuemap.json"
    after_cue: dict[tuple, dict] = {}   # (heading, cue_id) -> exact demo span
    after_total_ms = 0
    # only treat the new mp3 as "after" if it's a fresh rebuild (cuemap present
    # and newer than the snapshot we took as "before").
    after_is_rebuilt = after_mp3.exists() and before_mp3.exists() and after_cuemap_p.exists() and \
        after_mp3.stat().st_mtime > before_mp3.stat().st_mtime
    if after_is_rebuilt:
        for e in json.loads(after_cuemap_p.read_text()):
            after_cue[(e["heading"], e["cue_id"])] = e
        if after_chapters_p.exists():
            ac = json.loads(after_chapters_p.read_text())
            after_total_ms = ac[-1]["end_ms"] if ac else 0

    LEAD_IN, LEAD_OUT = args.lead_in_ms, args.lead_out_ms

    def context_window(total: int, demo_start: int, demo_end: int) -> tuple[int, int]:
        return max(0, demo_start - LEAD_IN), min(total or demo_end + LEAD_OUT, demo_end + LEAD_OUT)

    def demo_span(chap: dict, n_in_slide: int, ddur_ms: int) -> tuple[int, int, int, int]:
        """(demo_start, demo_end, meas_start, meas_end) within a chapter. For a
        single-demo slide the demo sits at the chapter tail; multi-demo chapters
        can't be isolated from chapters alone, so fall back to the whole span."""
        cs, ce = chap["start_ms"], chap["end_ms"]
        if n_in_slide == 1:
            return max(cs, ce - ddur_ms), ce, max(cs, ce - ddur_ms - 300), ce
        return cs, ce, cs, ce

    def measured(mp3: Path, meas_start: int, meas_end: int) -> dict:
        return measure_db(mp3, start_s=meas_start / 1000.0, dur_s=max(0.3, (meas_end - meas_start) / 1000.0))

    app_dir = HERE / "alignment_app"
    out = Path(args.out) if args.out else app_dir / "alignment_report.json"

    def rel_to_app(p: Path) -> str:
        import os
        return os.path.relpath(p.resolve(), app_dir.resolve())

    slots = []
    idx = 0
    for slide in ep.get("slides", []):
        sid = slide["id"]
        script_rel = slide.get("script_md")
        if not script_rel:
            continue
        script_md = (ep_dir / script_rel).read_text()
        chunks = narration_chunks(script_md)
        heading = slide.get("heading", sid)
        chap = chap_by_title.get(heading)
        # demos declared but not cued get appended at slide end (legacy);
        # build a cue→narration map, then fall back for uncued demos.
        cued = [(t, c) for (t, c) in chunks if c]
        declared = slide.get("demos", []) or []
        cued_ids = {c for _, c in cued}

        ordered = []
        for text, cue in cued:
            ordered.append((cue, text))
        for d in declared:
            if d not in cued_ids:
                # uncued: narration_before = whole slide text
                whole = " ".join(t for t, _ in chunks).strip()
                ordered.append((d, whole))

        n_in_slide = len(ordered)
        for j, (cue, narration_before) in enumerate(ordered):
            kind = "operator-demo" if cue.startswith("op-") else "song-clip"
            after_path = None
            for ext in (".wav", ".aif", ".aiff"):
                cand = clips_dir / f"{cue}{ext}"
                if cand.exists():
                    after_path = cand
                    break
            ddur_ms = int(demo_dur.get(cue, 4.0) * 1000)

            # ── AFTER: exact demo span from the build cuemap (no narration bleed) ──
            after = {"available": False, "source": "wav", "status": "missing", "mean_db": None, "peak_db": None}
            ace = after_cue.get((heading, cue))
            if after_is_rebuilt and ace:
                ds, de = ace["demo_start_ms"], ace["demo_end_ms"]
                ps, pe = context_window(after_total_ms, ds, de)
                m = measured(after_mp3, ds, de)   # measure ONLY the demo → reliable status
                after = {"available": True, "source": "mp3", "in_context": True,
                         "start_ms": ps, "end_ms": pe, "demo_start_ms": ds, "demo_end_ms": de,
                         "mean_db": m["mean"], "peak_db": m["peak"], "status": status_from_db(m["mean"], m["peak"])}
                if after_path:
                    after["clip_path"] = rel_to_app(after_path)  # isolated-clip waveform
            elif after_path:
                db = measure_db(after_path)
                after = {"available": True, "source": "wav", "in_context": False, "path": rel_to_app(after_path),
                         "mean_db": db["mean"], "peak_db": db["peak"], "status": status_from_db(db["mean"], db["peak"])}

            # ── BEFORE: the shipped snapshot. The demo sits at the chapter tail;
            #    use the (now-known) demo duration from the cuemap to isolate it. ──
            before = {"available": False, "source": "mp3", "status": "missing"}
            if chap and before_mp3.exists():
                cs, ce = chap["start_ms"], chap["end_ms"]
                # if this slide has a trailing transition, the demo ends before it
                eff_ce = ce
                tcid = trans_after.get(sid)
                if tcid:
                    eff_ce = max(cs, ce - clip_dur_ms(tcid) - 400)
                bdur = (de - ds) if ace else ddur_ms
                if n_in_slide == 1:
                    bds, bde = max(cs, eff_ce - bdur), eff_ce
                else:
                    bds, bde = cs, ce  # multi-demo chapter: can't isolate per-cue
                ps, pe = context_window(total_ms, bds, bde)
                m = measured(before_mp3, bds, bde)
                before = {"available": True, "source": "mp3", "in_context": True,
                          "start_ms": ps, "end_ms": pe, "demo_start_ms": bds, "demo_end_ms": bde,
                          "mean_db": m["mean"], "peak_db": m["peak"], "status": status_from_db(m["mean"], m["peak"]),
                          "measured_from_ms": bds}

            slots.append({
                "index": idx,
                "section": section_for(sid),
                "slide_id": sid,
                "heading": heading,
                "cue_id": cue,
                "kind": kind,
                "narration_before": narration_before[-400:],
                "before": before,
                "after": after,
            })
            idx += 1

    report = {
        "episode_id": args.episode,
        "episode_title": ep.get("title", args.episode),
        "generated_note": "before = shipped e01-operator.before.mp3 snapshot; "
                          "after = rebuilt mp3 in-context if present, else bare clip",
        "before_mp3": rel_to_app(before_mp3),
        "after_mp3": rel_to_app(after_mp3) if after_is_rebuilt else None,
        "lead_in_ms": LEAD_IN,
        "lead_out_ms": LEAD_OUT,
        "duration_ms": total_ms,
        "slots": slots,
    }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2))

    n_before_bad = sum(1 for s in slots if s["before"].get("status") in ("silent", "quiet", "missing"))
    n_after_ok = sum(1 for s in slots if s["after"].get("status") == "ok")
    print(f"Wrote {out} — {len(slots)} slots; "
          f"before problematic: {n_before_bad}; after ok: {n_after_ok}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""
episode_readiness.py — the harness's single build-blocking READINESS GATE.

The harness weakness this fixes: gates ran but emitted no receipts, and
consistency was enforced only on the narrative. This tool turns every
consistency/coverage requirement into a machine check that:
  • emits a structured receipt   episodes/<ep>/gate-report.json   (+ .md)
  • returns a non-zero exit code on any hard FAIL (so a build can block on it)
  • is deterministic + re-runnable, so you can ITERATE and diff between runs.

Checks (each a receipt line with status pass/fail/warn/skip + details):
  1. preset_books   — EVERY described preset (a demo with a `params:` block) MUST
                      have a build book: tutorials/<id>.md AND an entry in
                      presets/SAVE_CHECKLIST.md.  Hard fail on any gap.
  2. demo_clips     — every [cue: id] in the scripts resolves to a clip_manifest
                      id; for BUILT episodes, every cued device-demo has a rendered
                      clip on disk (or is declared headless:false / hand-build).
  3. beds           — no `TBD`/unresolved bed or transition clip_ids; every act
                      (slide-number group) has background-bed coverage.
  4. audio_style    — (built only) parse sound-design-qa: no demo > ±6 dB vs voice.
  5. loudness       — (built only) integrated −16±1 LUFS and true-peak ≤ −1 dBTP.
  6. lexicon        — scripts carry zero banned phrases / exclamations / emojis
                      (single source of truth: shared/style/lexicon.md).

Usage:
  python shared/tools/episode_readiness.py --course-root courses/ableton-devices --episode e02-analog
  python shared/tools/episode_readiness.py --course-root courses/ableton-devices --all
  # --strict promotes warnings to failures.
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
sys.path.insert(0, str(HERE))
from _course_lib import load_course, episodes_dir, lessons_dir, build_audio, shared_style_dir  # noqa: E402

CUE_RE = re.compile(r"\[cue:\s*([a-z0-9][a-z0-9-]*)\]")
EMOJI_RE = re.compile("[\U0001F000-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF✀-➿☀-⛿]")
DEMO_KEYS = ("device_demos", "operator_demos")


# ── small helpers ────────────────────────────────────────────────────────────
def _result(name, status, summary, problems=None, data=None):
    return {"check": name, "status": status, "summary": summary,
            "problems": problems or [], "data": data or {}}


def load_banned_phrases(style_dir: Path) -> list[str]:
    """Single source of truth: the backtick-quoted phrases under the BANNED
    hard-fail section of lexicon.md."""
    lex = style_dir / "lexicon.md"
    if not lex.exists():
        return []
    out, in_ban = [], False
    for line in lex.read_text().splitlines():
        s = line.strip()
        if s.startswith("## BANNED") and "hard fail" in s.lower():
            in_ban = True
            continue
        if s.startswith("## ") and "BANNED — hard fail" not in s:
            if in_ban and not s.startswith("## BANNED"):
                in_ban = False
        if in_ban and s.startswith("- "):
            for m in re.findall(r"`([^`]+)`", s):
                # drop parentheticals, split slash-alternatives
                m = re.sub(r"\([^)]*\)", "", m).strip()
                for part in m.split(" / "):
                    part = part.strip()
                    if part:
                        out.append(part.lower())
    return sorted(set(out))


def measure_loudness(mp3: Path) -> dict | None:
    r = subprocess.run(
        ["ffmpeg", "-hide_banner", "-nostats", "-i", str(mp3),
         "-af", "loudnorm=print_format=json", "-f", "null", "-"],
        capture_output=True, text=True)
    txt = r.stderr
    try:
        blob = txt[txt.rindex("{"): txt.rindex("}") + 1]
        j = json.loads(blob)
        return {"integrated_lufs": float(j["input_i"]), "true_peak_db": float(j["input_tp"])}
    except (ValueError, KeyError, json.JSONDecodeError):
        return None


def act_of(slide_id: str) -> str | None:
    m = re.match(r"(\d+)", slide_id)
    return m.group(1) if m else None


# ── the checks ───────────────────────────────────────────────────────────────
def check_preset_books(ep_dir: Path, demos: list[dict]) -> dict:
    """EVERY described preset (demo with a params block) needs a build book."""
    tut_dir = ep_dir / "tutorials"
    checklist = ep_dir / "presets" / "SAVE_CHECKLIST.md"
    checklist_txt = checklist.read_text() if checklist.exists() else ""
    described = [d for d in demos if d.get("params")]
    composed = [d for d in demos if not d.get("params") and (d.get("concat_from") or d.get("mix_from"))]
    problems = []
    for d in described:
        did = d["id"]
        has_tut = (tut_dir / f"{did}.md").exists()
        in_check = did in checklist_txt
        if not has_tut:
            problems.append(f"{did}: NO build book (tutorials/{did}.md missing)")
        elif not in_check:
            problems.append(f"{did}: tutorial exists but not listed in presets/SAVE_CHECKLIST.md")
    status = "fail" if problems else "pass"
    return _result("preset_books", status,
                   f"{len(described) - len(problems)}/{len(described)} described presets have a build book"
                   + (f" (+{len(composed)} composed demos exempt)" if composed else ""),
                   problems, {"described": len(described), "composed": len(composed)})


def check_demo_clips(ep_dir: Path, demos: list[dict], scripts: list[Path],
                     manifest: dict, clips_dir: Path | None, built: bool) -> dict:
    demo_ids = {d["id"] for d in demos}
    song_ids = {s["id"] for s in (manifest.get("song_clips") or [])}
    ep = yaml.safe_load((ep_dir / "episode.yaml").read_text()) or {}
    trans_ids = {i.get("clip_id") for i in (ep.get("transitions", {}).get("insertions") or [])}
    bed_ids = {i.get("clip_id") for i in (ep.get("beds", {}).get("insertions") or [])}
    known = demo_ids | song_ids | trans_ids | bed_ids
    problems, cues = [], set()
    for sp in scripts:
        for cid in CUE_RE.findall(sp.read_text()):
            cues.add(cid)
            if cid not in known:
                problems.append(f"{sp.name}: [cue: {cid}] resolves to NO manifest id")
    # headless flag: a demo may declare it can't render (hand-build); else expect a clip
    unrendered = []
    if built and clips_dir is not None:
        for d in demos:
            did = d["id"]
            if d.get("headless") is False or d.get("hand_build"):
                continue
            if not any((clips_dir / f"{did}{e}").exists() for e in (".wav", ".aif", ".aiff")):
                unrendered.append(did)
    status = "fail" if problems else ("warn" if unrendered else "pass")
    summ = f"{len(cues)} cues, {len(problems)} unresolved"
    if built:
        summ += f"; {len(unrendered)} cued/demo clips not rendered"
    return _result("demo_clips", status, summ,
                   problems + [f"unrendered (no headless:false flag): {u}" for u in unrendered],
                   {"cues": len(cues), "unrendered": unrendered})


def check_beds(ep_dir: Path, clips_dir: Path | None, built: bool) -> dict:
    ep = yaml.safe_load((ep_dir / "episode.yaml").read_text()) or {}
    trans = ep.get("transitions", {}).get("insertions") or []
    beds = ep.get("beds", {}).get("insertions") or []
    slides = [s["id"] for s in (ep.get("slides") or [])]
    acts = sorted({a for s in slides if (a := act_of(s))})
    problems = []

    def resolves(cid):
        if not cid or cid == "TBD":
            return False
        if not built or clips_dir is None:
            return True  # can't check files pre-build; TBD is still a fail above
        return any((clips_dir / f"{cid}{e}").exists() for e in (".wav", ".aif", ".aiff"))

    for kind, items, key in (("transition", trans, "after_slide"), ("bed", beds, "start_at_slide")):
        for it in items:
            cid = it.get("clip_id")
            if not cid or cid == "TBD":
                problems.append(f"{kind} @ {it.get(key)}: clip_id is {cid or 'missing'} (placeholder)")
            elif not resolves(cid):
                problems.append(f"{kind} {cid}: declared but no rendered clip on disk")
    # bed coverage: which acts have at least one bed spanning them
    covered = set()
    sidx = {s: i for i, s in enumerate(slides)}
    for b in beds:
        s, e = sidx.get(b.get("start_at_slide")), sidx.get(b.get("end_at_slide", b.get("start_at_slide")))
        if s is not None and e is not None:
            for s2 in slides[s:e + 1]:
                if (a := act_of(s2)):
                    covered.add(a)
    # TBD / unresolved clip = HARD FAIL (the real silent-skip gap). An act that is
    # intentionally demo-dense with no bed = WARN (surface it, don't block).
    hard = bool(problems)  # everything appended so far is placeholder/unresolved-on-disk
    uncovered = [a for a in acts if a not in covered and a != "01"]  # 01 = cold open, bed optional
    for a in uncovered:
        problems.append(f"act {a}: no background-bed coverage (warn — fill or confirm demo-dense)")
    status = "fail" if hard else ("warn" if uncovered else "pass")
    return _result("beds", status,
                   f"{len(trans)} transitions, {len(beds)} beds; acts covered {len(covered)}/{len(acts)}",
                   problems, {"acts": acts, "covered": sorted(covered), "uncovered": uncovered})


def check_narration(ep_dir: Path, narr_dir: Path) -> dict:
    """EVERY slide in episode.yaml must have a rendered narration WAV — else the
    build SILENTLY drops it and the episode ships truncated (this is exactly how
    e02 shipped missing its last 4 slides)."""
    ep = yaml.safe_load((ep_dir / "episode.yaml").read_text()) or {}
    slides = [s["id"] for s in (ep.get("slides") or [])]
    if not narr_dir.exists():
        return _result("narration", "skip", "no narration rendered yet",
                       data={"slides": len(slides)})
    have = set()
    for f in narr_dir.glob("*.wav"):
        have.add(re.sub(r"\.\d{3}\.wav$", "", f.name).replace(".wav", ""))
    missing = [s for s in slides if s not in have]
    status = "fail" if missing else "pass"
    return _result("narration", status,
                   f"{len(slides) - len(missing)}/{len(slides)} slides narrated",
                   [f"{m}: script exists but NO narration WAV (build will drop it)" for m in missing],
                   {"slides": len(slides), "missing": missing})


def check_audio_style(course_root: Path, ep_id: str, built: bool) -> dict:
    """Run sound_design_qa for THIS episode (it writes one shared json), then judge
    demo-vs-voice consistency. >6 dB = warn (jarring), >12 dB = hard fail."""
    if not built:
        return _result("audio_style", "skip", "episode not built")
    tool = Path(course_root) / "tools" / "sound_design_qa.py"
    qa = Path(course_root) / "tools" / "alignment_app" / "sound-design-qa.json"
    if tool.exists():
        subprocess.run([sys.executable, str(tool), "--course-root", str(course_root),
                        "--lesson", ep_id], capture_output=True, text=True)
    if not qa.exists():
        return _result("audio_style", "skip", "no sound-design-qa.json")
    data = json.loads(qa.read_text())
    if (data.get("lesson") or data.get("episode")) not in (ep_id, None):
        return _result("audio_style", "skip", f"QA json is for {data.get('lesson')}, not {ep_id}")
    cues = data.get("cues", data if isinstance(data, list) else [])
    warn = [c for c in cues if isinstance(c, dict) and 6 < abs(c.get("delta_db", 0)) <= 12]
    fail = [c for c in cues if isinstance(c, dict) and abs(c.get("delta_db", 0)) > 12]
    problems = [f"{c.get('cue_id')}: demo {c.get('delta_db')}dB vs voice ({'FAIL >12' if abs(c.get('delta_db',0))>12 else 'warn >6'})"
                for c in fail + warn]
    status = "fail" if fail else ("warn" if warn else "pass")
    return _result("audio_style", status,
                   f"{len(fail)} demos >12dB, {len(warn)} demos 6-12dB off voice", problems)


def check_loudness(mp3: Path | None) -> dict:
    if not mp3 or not mp3.exists():
        return _result("loudness", "skip", "episode not built")
    m = measure_loudness(mp3)
    if not m:
        return _result("loudness", "warn", "could not measure loudness")
    problems = []
    if abs(m["integrated_lufs"] + 16) > 1.0:
        problems.append(f"integrated {m['integrated_lufs']} LUFS (want -16 ±1)")
    if m["true_peak_db"] > -1.0:
        problems.append(f"true peak {m['true_peak_db']} dBTP (want ≤ -1.0)")
    status = "fail" if problems else "pass"
    return _result("loudness", status,
                   f"{m['integrated_lufs']} LUFS / {m['true_peak_db']} dBTP", problems, m)


def check_lexicon(scripts: list[Path], banned: list[str]) -> dict:
    problems = []
    for sp in scripts:
        txt = sp.read_text()
        low = txt.lower()
        for b in banned:
            if b in low:
                problems.append(f"{sp.name}: banned phrase '{b}'")
        ex = txt.count("!")
        if ex:
            problems.append(f"{sp.name}: {ex} exclamation point(s)")
        if EMOJI_RE.search(txt):
            problems.append(f"{sp.name}: emoji present")
    status = "fail" if problems else "pass"
    return _result("lexicon", status, f"{len(scripts)} scripts, {len(problems)} violations",
                   problems, {"banned_terms_checked": len(banned)})


# ── runner ───────────────────────────────────────────────────────────────────
def run_episode(cfg, course_root, ep_id: str, strict: bool) -> dict:
    base = episodes_dir(cfg) if cfg.get("content_kind") == "episode" else lessons_dir(cfg)
    ep_dir = base / ep_id
    manifest = yaml.safe_load((ep_dir / "clip_manifest.yaml").read_text()) or {}
    demos = []
    for k in DEMO_KEYS:
        demos += manifest.get(k) or []
    scripts = sorted((ep_dir / "script").glob("*.md")) if (ep_dir / "script").exists() else []
    clips_dir = build_audio(cfg) / "clips" / ep_id
    narr_dir = build_audio(cfg) / "narration" / ep_id
    mp3 = build_audio(cfg) / "episodes" / f"{ep_id}.mp3"
    built = mp3.exists()
    banned = load_banned_phrases(shared_style_dir(cfg))

    checks = [
        check_narration(ep_dir, narr_dir),
        check_preset_books(ep_dir, demos),
        check_demo_clips(ep_dir, demos, scripts, manifest, clips_dir, built),
        check_beds(ep_dir, clips_dir, built),
        check_audio_style(course_root, ep_id, built),
        check_loudness(mp3 if built else None),
        check_lexicon(scripts, banned),
    ]
    # strict promotes warn → fail
    if strict:
        for c in checks:
            if c["status"] == "warn":
                c["status"] = "fail"
    hard_fail = any(c["status"] == "fail" for c in checks)
    report = {"episode": ep_id, "built": built, "ready": not hard_fail, "checks": checks}

    (ep_dir / "gate-report.json").write_text(json.dumps(report, indent=2))
    (ep_dir / "gate-report.md").write_text(render_md(report))
    return report


def render_md(report: dict) -> str:
    icon = {"pass": "✅", "fail": "❌", "warn": "⚠️", "skip": "—"}
    lines = [f"# Gate report — `{report['episode']}`",
             "",
             f"**Built:** {report['built']}  ·  **READY:** {'YES' if report['ready'] else 'NO'}",
             "",
             "| Check | Status | Summary |", "|---|---|---|"]
    for c in report["checks"]:
        lines.append(f"| {c['check']} | {icon.get(c['status'], c['status'])} {c['status']} | {c['summary']} |")
    for c in report["checks"]:
        if c["problems"]:
            lines += ["", f"### {c['check']} — {len(c['problems'])} item(s)"]
            lines += [f"- {p}" for p in c["problems"]]
    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--course-root", required=True)
    ap.add_argument("--episode", "--lesson", dest="episode")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()
    cfg = load_course(args.course_root)
    if args.all:
        eps = [e["id"] for e in (cfg.get("episodes") or cfg.get("weeks") or [])]
    elif args.episode:
        eps = [args.episode]
    else:
        sys.stderr.write("need --episode or --all\n")
        return 2

    base = episodes_dir(cfg) if cfg.get("content_kind") == "episode" else lessons_dir(cfg)
    any_fail = False
    print(f"{'episode':16} ready  " + "  ".join(f"{c:>11}" for c in
          ["narration", "preset_books", "demo_clips", "beds", "audio_style", "loudness", "lexicon"]))
    for ep_id in eps:
        if not (base / ep_id / "clip_manifest.yaml").exists():
            continue
        rep = run_episode(cfg, args.course_root, ep_id, args.strict)
        any_fail = any_fail or not rep["ready"]
        st = {c["check"]: c["status"] for c in rep["checks"]}
        row = "  ".join(f"{st.get(c, '-'):>11}" for c in
               ["narration", "preset_books", "demo_clips", "beds", "audio_style", "loudness", "lexicon"])
        print(f"{ep_id:16} {'OK ' if rep['ready'] else 'FAIL':5} {row}")
    return 1 if any_fail else 0


if __name__ == "__main__":
    sys.exit(main())

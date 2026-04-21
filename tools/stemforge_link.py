#!/usr/bin/env python3
"""
stemforge_link.py — bridge stemforge's native output convention to the course's
declared render paths.

Stemforge writes to ~/stemforge/processed/<slug>/{drums,bass,vocals,other}.wav
The course recipes in recipes.yaml declare custom render paths per lesson.
This script resolves each recipe by matching source_file in stems.json and
symlinks the actual stem WAVs to the expected paths.

Usage:
    python3 tools/stemforge_link.py
    python3 tools/stemforge_link.py --dry-run

Re-run safe: re-creates symlinks, overwrites stale.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.stderr.write("pyyaml missing. pip install pyyaml\n")
    sys.exit(2)

ROOT = Path(__file__).resolve().parent.parent
RECIPES_PATH = ROOT / "stemforge-demo-material" / "recipes.yaml"
PROCESSED = Path.home() / "stemforge" / "processed"


def expand(value: str, ctx: dict[str, str]) -> str:
    for k, v in ctx.items():
        value = value.replace("${" + k + "}", v)
    return value


def find_processed_dir_by_source(source_path: Path) -> Path | None:
    """Look through ~/stemforge/processed/ for a stems.json whose source_file matches."""
    target_resolved = str(source_path.resolve())
    if not PROCESSED.exists():
        return None
    for sj in PROCESSED.glob("*/stems.json"):
        try:
            data = json.loads(sj.read_text())
        except json.JSONDecodeError:
            continue
        if str(Path(data.get("source_file", "")).resolve()) == target_resolved:
            return sj.parent
    return None


def link_one(recipe: dict, ctx: dict[str, str], dry_run: bool) -> dict:
    rid = recipe["recipe_id"]
    source = Path(expand(recipe["input"], ctx))
    processed_dir = find_processed_dir_by_source(source)
    if processed_dir is None:
        return {"recipe_id": rid, "status": "no-processed-dir", "source": str(source)}

    renders = recipe.get("renders", {})
    linked = []
    skipped = []

    for name, target_rel in renders.items():
        target_abs = ROOT / expand(target_rel, ctx)
        target_abs.parent.mkdir(parents=True, exist_ok=True)

        # Map the logical name to an actual stemforge output.
        # Naming convention used in recipes:
        #   drums/bass/vocals/other    → <stem>.wav
        #   dry                        → drums.wav (raw stem as 'dry' reference)
        #   wet                        → drums.wav (same file — course uses it as a label;
        #                                the 'tuned' / 'glitch' / 'ambient' flavor is applied
        #                                by the student in Ableton via the pipeline's effect chain)
        #   oneshots_dir / chops_dir / loops_dir → the <stem>_bars/_beats/curated directory
        mapping = {
            "drums": "drums.wav",
            "bass": "bass.wav",
            "vocals": "vocals.wav",
            "other": "other.wav",
            "dry": "drums.wav",
            "wet": "drums.wav",
        }

        if name in mapping:
            src_path = processed_dir / mapping[name]
            if not src_path.exists():
                skipped.append({"name": name, "reason": f"stem missing in processed dir: {src_path}"})
                continue
        elif name.endswith("_dir"):
            # Prefer curated/ if present (max-diversity output), else <stem>_bars/
            candidates = [
                processed_dir / "curated",
                processed_dir / "drums_bars",
                processed_dir / "drums_beats",
            ]
            src_path = next((c for c in candidates if c.exists()), None)
            if src_path is None:
                skipped.append({"name": name, "reason": "no curated/bars/beats dir in processed dir"})
                continue
        else:
            skipped.append({"name": name, "reason": f"unknown render label: {name}"})
            continue

        if dry_run:
            linked.append({"name": name, "from": str(src_path), "to": str(target_abs)})
            continue

        # Remove stale symlink/file if present
        if target_abs.exists() or target_abs.is_symlink():
            target_abs.unlink()
        try:
            target_abs.symlink_to(src_path)
            linked.append({"name": name, "from": str(src_path), "to": str(target_abs)})
        except OSError as e:
            skipped.append({"name": name, "reason": f"symlink failed: {e}"})

    return {
        "recipe_id": rid,
        "status": "ok" if linked and not skipped else ("partial" if linked else "failed"),
        "processed_dir": str(processed_dir),
        "linked": linked,
        "skipped": skipped,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    with RECIPES_PATH.open() as f:
        doc = yaml.safe_load(f)
    ctx = {"stemforge_root": doc.get("stemforge_root", "/Users/zak/zacharysbrown/stemforge")}

    results = [link_one(r, ctx, args.dry_run) for r in doc.get("recipes", [])]

    for r in results:
        linked_n = len(r.get("linked", []))
        skipped_n = len(r.get("skipped", []))
        print(f"[link] {r['recipe_id']}: {r['status']} — {linked_n} linked, {skipped_n} skipped")
        for s in r.get("skipped", []):
            print(f"    skip {s['name']}: {s['reason']}")

    out_status = ROOT / "build" / "audio" / "stemforge-renders" / "_link_status.json"
    out_status.parent.mkdir(parents=True, exist_ok=True)
    out_status.write_text(json.dumps(results, indent=2))

    ok = sum(1 for r in results if r["status"] == "ok")
    print(f"\nstemforge_link: {ok}/{len(results)} fully linked — status: {out_status}")
    return 0 if ok == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())

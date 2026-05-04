#!/usr/bin/env python3
"""
stemforge_runner.py — walks <course_root>/stemforge-demo-material/recipes.yaml
and invokes the stemforge CLI for each recipe, writing outputs to the declared
paths (resolved against the repo root).

Usage:
    python shared/tools/stemforge_runner.py --course-root courses/idm-12x12
    python shared/tools/stemforge_runner.py --course-root courses/idm-12x12 --week 5
    python shared/tools/stemforge_runner.py --course-root courses/idm-12x12 --recipe w05-express-tuned-ab
    python shared/tools/stemforge_runner.py --course-root courses/idm-12x12 --dry-run
    python shared/tools/stemforge_runner.py --course-root courses/idm-12x12 --no-skip-existing

Requires: stemforge CLI on PATH (source: ~/zacharysbrown/stemforge).

Writes (paths declared in recipes.yaml are repo-root-relative):
    build/audio/stemforge-renders/<week>/<...>.wav
    <build_root>/audio/stemforge-renders/_runner_status.json
"""
from __future__ import annotations

import argparse
import json
import os
import shlex
import subprocess
import sys
import time
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.stderr.write(
        "pyyaml missing. Install with: uv pip install pyyaml   (or pip install pyyaml)\n"
    )
    sys.exit(2)

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _course_lib import load_course, stemforge_out  # noqa: E402


def expand(value: str, ctx: dict[str, str]) -> str:
    for k, v in ctx.items():
        value = value.replace("${" + k + "}", v)
    return value


def run_one(
    recipe: dict,
    ctx: dict[str, str],
    repo_root: Path,
    dry_run: bool,
    skip_existing: bool,
) -> dict:
    rid = recipe["recipe_id"]
    cmd_tpl = recipe["cmd"]
    input_path = expand(recipe["input"], ctx)
    cmd_str = cmd_tpl.replace("{input}", shlex.quote(input_path))
    venv_bin = os.environ.get(
        "STEMFORGE_BIN", "/Users/zak/zacharysbrown/stemforge/.venv/bin/stemforge"
    )
    if os.path.exists(venv_bin) and cmd_str.startswith("stemforge "):
        cmd_str = shlex.quote(venv_bin) + cmd_str[len("stemforge"):]

    renders = {
        k: repo_root / expand(v, ctx) for k, v in recipe.get("renders", {}).items()
    }

    if skip_existing and renders and all(p.exists() for p in renders.values()):
        return {"recipe_id": rid, "status": "skipped-existing", "cmd": cmd_str}

    for p in renders.values():
        p.parent.mkdir(parents=True, exist_ok=True)

    print(f"[stemforge] {rid}: {cmd_str}", flush=True)
    if dry_run:
        return {"recipe_id": rid, "status": "dry-run", "cmd": cmd_str}

    t0 = time.time()
    try:
        proc = subprocess.run(
            cmd_str,
            shell=True,
            cwd=str(repo_root),
            check=False,
            capture_output=True,
            text=True,
            timeout=1800,
        )
    except subprocess.TimeoutExpired:
        return {"recipe_id": rid, "status": "timeout-1800s", "cmd": cmd_str}

    elapsed = round(time.time() - t0, 2)

    if proc.returncode != 0:
        return {
            "recipe_id": rid,
            "status": "failed",
            "cmd": cmd_str,
            "elapsed_s": elapsed,
            "stderr_tail": proc.stderr.strip().splitlines()[-20:],
        }

    missing = [str(p) for p in renders.values() if not p.exists()]
    if missing:
        return {
            "recipe_id": rid,
            "status": "cmd-ok-outputs-missing",
            "cmd": cmd_str,
            "elapsed_s": elapsed,
            "missing": missing,
            "note": "stemforge output path convention may not match declared renders — inspect manually",
        }

    return {"recipe_id": rid, "status": "ok", "cmd": cmd_str, "elapsed_s": elapsed}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--course-root", required=True)
    ap.add_argument("--week", type=int)
    ap.add_argument("--recipe")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-skip-existing", action="store_true")
    args = ap.parse_args()

    cfg = load_course(args.course_root)
    recipes_path = cfg["_course_root"] / "stemforge-demo-material" / "recipes.yaml"
    status_out = stemforge_out(cfg) / "_runner_status.json"

    with recipes_path.open() as f:
        doc = yaml.safe_load(f)

    ctx = {
        "stemforge_root": doc.get(
            "stemforge_root", "/Users/zak/zacharysbrown/stemforge"
        )
    }

    recipes = doc.get("recipes", [])
    if args.recipe:
        recipes = [r for r in recipes if r["recipe_id"] == args.recipe]
    if args.week is not None:
        week_tag = f"w{args.week:02d}"
        recipes = [r for r in recipes if r["lesson"].startswith(week_tag)]

    if not recipes:
        print("no recipes matched filter", file=sys.stderr)
        return 1

    results = []
    for r in recipes:
        results.append(
            run_one(
                r,
                ctx,
                repo_root=cfg["_repo_root"],
                dry_run=args.dry_run,
                skip_existing=not args.no_skip_existing,
            )
        )

    status_out.parent.mkdir(parents=True, exist_ok=True)
    status_out.write_text(json.dumps(results, indent=2))

    ok = sum(1 for r in results if r["status"] in ("ok", "skipped-existing", "dry-run"))
    print(f"\nstemforge_runner: {ok}/{len(results)} ok — status: {status_out}")
    return 0 if ok == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())

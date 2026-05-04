"""Common path resolution for course-aware tools.

Every shared tool that operates on a course takes --course-root <path>.
Helpers here normalize the file layout:

    <repo_root>/                ← repo (where podcast.xml lives)
        build/                  ← shared output dir
            audio/episodes/...  ← IDM episodes (load-bearing URLs)
            html/...            ← IDM decks
            <subdir>/...        ← per-course output for non-IDM courses
        courses/
            <course_id>/
                course.yaml     ← declares id, content_kind, build_subdir, etc.
                lessons/ | episodes/
                style/
                tools/

The course.yaml `build_subdir` field controls where outputs land:
    "" (empty)     → <repo_root>/build/...                 (IDM — preserves published URLs)
    "ableton"      → <repo_root>/build/ableton/...
"""
from __future__ import annotations

import subprocess
from pathlib import Path

import yaml


def repo_root() -> Path:
    return Path(
        subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"], text=True
        ).strip()
    )


def load_course(course_root: Path | str) -> dict:
    course_root = Path(course_root).resolve()
    cfg_path = course_root / "course.yaml"
    if not cfg_path.exists():
        raise SystemExit(f"course.yaml not found at {cfg_path}")
    cfg = yaml.safe_load(cfg_path.read_text()) or {}
    cfg["_course_root"] = course_root
    cfg["_repo_root"] = repo_root()
    subdir = (cfg.get("build_subdir") or "").strip()
    cfg["_build_root"] = (
        cfg["_repo_root"] / "build" / subdir if subdir else cfg["_repo_root"] / "build"
    )
    return cfg


def lessons_dir(cfg: dict) -> Path:
    return cfg["_course_root"] / cfg.get("lesson_dir", "lessons")


def episodes_dir(cfg: dict) -> Path:
    return cfg["_course_root"] / cfg.get("episode_dir", "episodes")


def references_dir(cfg: dict) -> Path:
    return cfg["_course_root"] / cfg.get("references_dir", "references")


def style_dir(cfg: dict) -> Path:
    return cfg["_course_root"] / "style"


def shared_style_dir(cfg: dict) -> Path:
    return cfg["_repo_root"] / "shared" / "style"


def build_audio(cfg: dict) -> Path:
    return cfg["_build_root"] / "audio"


def build_html(cfg: dict) -> Path:
    return cfg["_build_root"] / "html"


def episodes_out(cfg: dict) -> Path:
    return build_audio(cfg) / "episodes"


def narration_out(cfg: dict) -> Path:
    return build_audio(cfg) / "narration"


def stemforge_out(cfg: dict) -> Path:
    return build_audio(cfg) / "stemforge-renders"

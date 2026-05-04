#!/usr/bin/env bun
// validate.ts — parallel-agent authoring safety net.
// Validates a course's lessons or episodes against:
//   - shared/style/lexicon.md banned-phrases (+ per-course extension)
//   - exclamation/emoji policies
//   - bibliography.json citation IDs (lesson.references)
//   - teaser-calendar.yaml scheduling (if present)
//   - minimum script length
//
// Usage:
//   bun run shared/tools/validate.ts --course-root courses/idm-12x12
//   bun run shared/tools/validate.ts --course-root courses/idm-12x12 --week 5
//   bun run shared/tools/validate.ts --course-root courses/idm-12x12 --all
//   bun run shared/tools/validate.ts --course-root courses/idm-12x12 --allow-empty
//   bun run shared/tools/validate.ts --course-root courses/idm-12x12 --style
//
// Exits 0 on pass, 1 on fail.

import { readFileSync, existsSync, readdirSync, statSync } from "node:fs";
import { join, resolve } from "node:path";
import { execSync } from "node:child_process";
import { parse as parseYaml } from "yaml";

function arg(name: string): string | undefined {
  const i = process.argv.findIndex((a) => a === name);
  return i >= 0 ? process.argv[i + 1] : undefined;
}

const courseRootArg = arg("--course-root");
if (!courseRootArg) {
  console.error("--course-root is required (e.g., courses/idm-12x12)");
  process.exit(2);
}

const COURSE_ROOT = resolve(courseRootArg);
const REPO_ROOT = execSync("git rev-parse --show-toplevel", { encoding: "utf8" }).trim();
const SHARED_STYLE = join(REPO_ROOT, "shared", "style");
const COURSE_STYLE = join(COURSE_ROOT, "style");
const REFS = join(COURSE_ROOT, "references");

const courseYaml = parseYaml(readFileSync(join(COURSE_ROOT, "course.yaml"), "utf8")) ?? {};
const contentKind: "lesson" | "episode" = courseYaml.content_kind === "episode" ? "episode" : "lesson";
const itemsDir = join(
  COURSE_ROOT,
  contentKind === "episode" ? courseYaml.episode_dir ?? "episodes" : courseYaml.lesson_dir ?? "lessons",
);
const itemYamlName = contentKind === "episode" ? "episode.yaml" : "lesson.yaml";

type Failure = { where: string; msg: string; severity: "fail" | "warn" };
const problems: Failure[] = [];
const fail = (where: string, msg: string) => problems.push({ where, msg, severity: "fail" });
const warn = (where: string, msg: string) => problems.push({ where, msg, severity: "warn" });

function loadBannedFromLexicon(text: string): string[] {
  const out: string[] = [];
  const sec = text.split("## APPROVED")[0] ?? "";
  for (const line of sec.split("\n")) {
    const m = line.match(/^- `([^`]+)`/);
    if (m) out.push(m[1].toLowerCase());
  }
  return out;
}

const baseLex = existsSync(join(SHARED_STYLE, "lexicon.md"))
  ? readFileSync(join(SHARED_STYLE, "lexicon.md"), "utf8")
  : "";
const extLex = existsSync(join(COURSE_STYLE, "lexicon-extension.md"))
  ? readFileSync(join(COURSE_STYLE, "lexicon-extension.md"), "utf8")
  : "";
const BANNED = [...new Set([...loadBannedFromLexicon(baseLex), ...loadBannedFromLexicon(extLex)])];

let bib: Record<string, unknown> = {};
if (existsSync(join(REFS, "bibliography.json"))) {
  bib = JSON.parse(readFileSync(join(REFS, "bibliography.json"), "utf8"));
}
const bibIds = new Set(Object.keys(bib).filter((k) => k.startsWith("bib:")));

let teaserCal: Record<string, { week: number; paragraph: string }> = {};
if (existsSync(join(COURSE_STYLE, "teaser-calendar.yaml"))) {
  teaserCal = parseYaml(readFileSync(join(COURSE_STYLE, "teaser-calendar.yaml"), "utf8")) ?? {};
}

function relRepo(p: string): string {
  return p.startsWith(REPO_ROOT + "/") ? p.slice(REPO_ROOT.length + 1) : p;
}

function scanFileForBanned(path: string, label: string) {
  if (!existsSync(path)) return;
  const raw = readFileSync(path, "utf8");
  const text = raw.toLowerCase();
  for (const phrase of BANNED) {
    if (text.includes(phrase)) fail(label, `banned phrase: "${phrase}"`);
  }
  const exclamations = (raw.match(/!/g) ?? []).length;
  if (exclamations > 0) fail(label, `${exclamations} exclamation points (policy: zero)`);
  if (/[\u{1F300}-\u{1FAFF}\u{2600}-\u{27BF}]/u.test(raw)) {
    fail(label, "emoji detected (policy: zero)");
  }
}

function validateItemDir(dir: string) {
  const itemYamlPath = join(dir, itemYamlName);
  if (!existsSync(itemYamlPath)) {
    if (process.argv.includes("--allow-empty")) return;
    fail(dir, `missing ${itemYamlName}`);
    return;
  }
  const item = parseYaml(readFileSync(itemYamlPath, "utf8"));
  if (!item) {
    fail(dir, `empty ${itemYamlName}`);
    return;
  }

  for (const ref of item.references ?? []) {
    if (!bibIds.has(ref)) fail(itemYamlPath, `unresolved citation ${ref}`);
  }

  if (contentKind === "lesson") {
    const scheduled = Object.entries(teaserCal)
      .filter(([, v]) => v?.week === item.week)
      .map(([k]) => k);
    for (const t of scheduled) {
      const declared = (item.teasers ?? []).includes(t);
      if (!declared)
        warn(itemYamlPath, `teaser "${t}" scheduled for W${item.week} but not declared in ${itemYamlName}.teasers`);
    }
  }

  const walk = (d: string) => {
    if (!existsSync(d)) return;
    for (const entry of readdirSync(d)) {
      const p = join(d, entry);
      if (statSync(p).isFile() && (p.endsWith(".md") || p.endsWith(".yaml"))) {
        scanFileForBanned(p, relRepo(p));
      }
    }
  };
  walk(join(dir, "slides"));
  walk(join(dir, "script"));
  scanFileForBanned(itemYamlPath, relRepo(itemYamlPath));

  const scriptDir = join(dir, "script");
  if (existsSync(scriptDir)) {
    let totalWords = 0;
    for (const f of readdirSync(scriptDir)) {
      if (f.endsWith(".md")) {
        const wc = readFileSync(join(scriptDir, f), "utf8").split(/\s+/).filter(Boolean).length;
        totalWords += wc;
      }
    }
    if (totalWords < 600 && !process.argv.includes("--allow-empty")) {
      warn(dir, `script total ${totalWords} words — likely < 4 min read`);
    }
  }
}

const weekArg = process.argv.findIndex((a) => a === "--week");
const weekNum = weekArg >= 0 ? Number(process.argv[weekArg + 1]) : undefined;

const dirs = existsSync(itemsDir)
  ? readdirSync(itemsDir)
      .map((d) => join(itemsDir, d))
      .filter((p) => statSync(p).isDirectory())
      .filter((p) => {
        if (weekNum === undefined) return true;
        const m = p.match(/\/w(\d{2})-/);
        return m ? Number(m[1]) === weekNum : false;
      })
  : [];

for (const d of dirs) validateItemDir(d);

const fails = problems.filter((p) => p.severity === "fail");
const warns = problems.filter((p) => p.severity === "warn");
for (const p of fails) console.error(`FAIL ${p.where}: ${p.msg}`);
for (const p of warns) console.error(`WARN ${p.where}: ${p.msg}`);
console.error(`\nsummary: ${fails.length} fail / ${warns.length} warn / ${dirs.length} ${contentKind}s`);
process.exit(fails.length > 0 ? 1 : 0);

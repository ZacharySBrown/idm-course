#!/usr/bin/env bun
// validate_lesson.ts — parallel-agent authoring safety net.
// Usage:
//   bun run tools/validate_lesson.ts --week 5
//   bun run tools/validate_lesson.ts --all
//   bun run tools/validate_lesson.ts --allow-empty   (Wave 0 scaffold check)
//   bun run tools/validate_lesson.ts --style         (lexicon + tone rules only)
//
// Exits 0 on pass, 1 on fail, 2 on warn-with-fail-flag.

import { readFileSync, existsSync, readdirSync, statSync } from "node:fs";
import { join, resolve } from "node:path";
import { parse as parseYaml } from "yaml";

const ROOT = resolve(import.meta.dir, "..");
const LESSONS = join(ROOT, "lessons");
const STYLE = join(ROOT, "style");
const REFS = join(ROOT, "references");

type Failure = { where: string; msg: string; severity: "fail" | "warn" };
const problems: Failure[] = [];
const fail = (where: string, msg: string) => problems.push({ where, msg, severity: "fail" });
const warn = (where: string, msg: string) => problems.push({ where, msg, severity: "warn" });

// --- Banned phrases from style/lexicon.md ---
const bannedRaw = existsSync(join(STYLE, "lexicon.md"))
  ? readFileSync(join(STYLE, "lexicon.md"), "utf8")
  : "";
const BANNED: string[] = [];
const bannedSection = bannedRaw.split("## APPROVED")[0] ?? "";
for (const line of bannedSection.split("\n")) {
  const m = line.match(/^- `([^`]+)`/);
  if (m) BANNED.push(m[1].toLowerCase());
}

// --- Bibliography IDs ---
let bib: Record<string, unknown> = {};
if (existsSync(join(REFS, "bibliography.json"))) {
  bib = JSON.parse(readFileSync(join(REFS, "bibliography.json"), "utf8"));
}
const bibIds = new Set(Object.keys(bib).filter((k) => k.startsWith("bib:")));

// --- Teaser calendar ---
let teaserCal: Record<string, { week: number; paragraph: string }> = {};
if (existsSync(join(STYLE, "teaser-calendar.yaml"))) {
  teaserCal = parseYaml(readFileSync(join(STYLE, "teaser-calendar.yaml"), "utf8")) ?? {};
}

function scanFileForBanned(path: string, label: string) {
  if (!existsSync(path)) return;
  const text = readFileSync(path, "utf8").toLowerCase();
  for (const phrase of BANNED) {
    if (text.includes(phrase)) fail(label, `banned phrase: "${phrase}"`);
  }
  const exclamations = (text.match(/!/g) ?? []).length;
  if (exclamations > 0) fail(label, `${exclamations} exclamation points (policy: zero)`);
  // quick emoji sniff (BMP pictographs + astral plane)
  if (/[\u{1F300}-\u{1FAFF}\u{2600}-\u{27BF}]/u.test(readFileSync(path, "utf8"))) {
    fail(label, "emoji detected (policy: zero)");
  }
}

function validateLessonDir(dir: string) {
  const lessonYamlPath = join(dir, "lesson.yaml");
  if (!existsSync(lessonYamlPath)) {
    if (process.argv.includes("--allow-empty")) return;
    fail(dir, "missing lesson.yaml");
    return;
  }
  const lesson = parseYaml(readFileSync(lessonYamlPath, "utf8"));
  if (!lesson) {
    fail(dir, "empty lesson.yaml");
    return;
  }

  // citations resolve
  for (const ref of lesson.references ?? []) {
    if (!bibIds.has(ref)) fail(lessonYamlPath, `unresolved citation ${ref}`);
  }

  // teaser presence if scheduled
  const scheduled = Object.entries(teaserCal)
    .filter(([, v]) => v?.week === lesson.week)
    .map(([k]) => k);
  for (const t of scheduled) {
    const declared = (lesson.teasers ?? []).includes(t);
    if (!declared) warn(lessonYamlPath, `teaser "${t}" scheduled for W${lesson.week} but not declared in lesson.teasers`);
  }

  // scan slides + scripts for banned phrases
  const walk = (d: string) => {
    if (!existsSync(d)) return;
    for (const entry of readdirSync(d)) {
      const p = join(d, entry);
      if (statSync(p).isFile() && (p.endsWith(".md") || p.endsWith(".yaml"))) {
        scanFileForBanned(p, p.replace(ROOT + "/", ""));
      }
    }
  };
  walk(join(dir, "slides"));
  walk(join(dir, "script"));
  scanFileForBanned(lessonYamlPath, lessonYamlPath.replace(ROOT + "/", ""));

  // script length sanity — 160 words/min, 45-min lesson target => >600 words minimum across all scripts
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
      warn(dir, `script total ${totalWords} words — likely < 4 min read, target ~28 min`);
    }
  }
}

// --- Dispatch ---
const weekArg = process.argv.findIndex((a) => a === "--week");
const weekNum = weekArg >= 0 ? Number(process.argv[weekArg + 1]) : undefined;

const dirs = readdirSync(LESSONS)
  .map((d) => join(LESSONS, d))
  .filter((p) => statSync(p).isDirectory())
  .filter((p) => {
    if (weekNum === undefined) return true;
    const m = p.match(/\/w(\d{2})-/);
    return m ? Number(m[1]) === weekNum : false;
  });

for (const d of dirs) validateLessonDir(d);

// Summary
const fails = problems.filter((p) => p.severity === "fail");
const warns = problems.filter((p) => p.severity === "warn");
for (const p of fails) console.error(`FAIL ${p.where}: ${p.msg}`);
for (const p of warns) console.error(`WARN ${p.where}: ${p.msg}`);
console.error(`\nsummary: ${fails.length} fail / ${warns.length} warn / ${dirs.length} lessons`);
process.exit(fails.length > 0 ? 1 : 0);

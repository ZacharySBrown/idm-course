export const meta = {
  name: 'finish-episode',
  description: 'Story-edit + validate an episode through the production gates (story-editor → writer → lock → fact-check), personas loaded from .claude/agents',
  phases: [
    { title: 'Structural review', detail: 'Story Editor diagnoses arc/jumpiness' },
    { title: 'Revision', detail: 'Writer applies targeted fixes' },
    { title: 'Script lock', detail: 'Story Editor re-checks → lock' },
    { title: 'Fact-check', detail: 'isolated Fact-Checker verifies claims' },
  ],
}

const EP = (args && args.episode) || 'e01-operator'
const EPD = `courses/ableton-devices/episodes/${EP}`
const RESEARCH = (args && args.research) || 'specs/ableton_course_ep1_research.md'
const persona = (f) => `You ARE the persona defined in /Users/zak/zacharysbrown/idm-course/.claude/agents/${f}. ` +
  `FIRST read that file in full and adopt its mandate, method, and gate rubric. Then do the task below.\n\n`

const REVIEW = { type: 'object', properties: {
  focus_sentence: { type: 'string' }, arc_ok: { type: 'boolean' },
  jumpy_spots: { type: 'array', items: { type: 'object', properties: {
    script: { type: 'string' }, problem: { type: 'string' }, fix: { type: 'string' } },
    required: ['script', 'problem', 'fix'] } },
  summary: { type: 'string' } },
  required: ['focus_sentence', 'arc_ok', 'jumpy_spots', 'summary'] }
const LOCK = { type: 'object', properties: {
  locked: { type: 'boolean' }, issues: { type: 'array', items: { type: 'string' } } },
  required: ['locked', 'issues'] }
const FACTS = { type: 'object', properties: {
  cleared: { type: 'boolean' },
  corrections: { type: 'array', items: { type: 'object', properties: {
    file: { type: 'string' }, claim: { type: 'string' }, issue: { type: 'string' }, correction: { type: 'string' } },
    required: ['file', 'claim', 'issue', 'correction'] } } },
  required: ['cleared', 'corrections'] }

phase('Structural review')
const review = await agent(
  persona('story-editor.md') +
  `Read ${EPD}/episode.yaml and EVERY script in ${EPD}/script/ in slide order. A listener called this episode "jumpy" and "strange" — diagnose WHY at the structural level against your Gate 2/Gate 5 rubric. ` +
  `Write a prioritized ${EPD}/structural-notes.md: the focus sentence, the arc, abrupt/unmotivated transitions, beats that don't raise→answer, missing signposts — each with the exact script file and a concrete fix (a transition line to add, a reorder, a signpost). Diagnose and prescribe only; do NOT rewrite scripts. Then return the structured summary.`,
  { agentType: 'general-purpose', phase: 'Structural review', schema: REVIEW })

phase('Revision')
const revised = await agent(
  persona('writer.md') +
  `Read ${EPD}/structural-notes.md and apply ONLY those targeted fixes to the flagged scripts in ${EPD}/script/. ` +
  `Preserve the voice (shared/style/voice.md), every fact, and EVERY [cue: id] / [bed: ...] / [pause Nms] marker exactly. Make transitions motivated, add signposts, leave working beats alone. Report which files changed and what changed.`,
  { agentType: 'general-purpose', phase: 'Revision' })

phase('Script lock')
const lock = await agent(
  persona('story-editor.md') +
  `Re-read the revised ${EPD}/script/ in order, cold. Confirm the jumpy transitions now flow, each beat raises→answers, signposts present, and NO [cue]/[bed]/[pause] marker was lost (compare counts). locked=true only if it passes; else list specific remaining issues.`,
  { agentType: 'general-purpose', phase: 'Script lock', schema: LOCK })

phase('Fact-check')
const facts = await agent(
  persona('fact-checker.md') +
  `ISOLATED check. Use only the scripts in ${EPD}/script/, the dossier ${RESEARCH}, and the web. Verify every nontrivial claim (dates, names, gear, quotes, technical assertions). Flag anything unsupported/wrong with the file and a correction. Don't assume the writers' intent.`,
  { agentType: 'general-purpose', phase: 'Fact-check', schema: FACTS })

log(`finish-episode(${EP}): arc_ok=${review.arc_ok} jumpy=${review.jumpy_spots.length} locked=${lock.locked} facts_cleared=${facts.cleared}`)
return { episode: EP, review, revised, lock, facts }

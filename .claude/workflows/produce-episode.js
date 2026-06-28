export const meta = {
  name: 'produce-episode',
  description: 'Produce a new episode editorial package from its research dossier: outline → demo design → scripts → story-edit lock → fact-check',
  phases: [
    { title: 'Outline', detail: 'Story Editor builds episode.yaml + beat sheet from the dossier' },
    { title: 'Demo design', detail: 'Ableton Expert specs the device demos + tutorials' },
    { title: 'Scripts', detail: 'Writer writes all slides in voice' },
    { title: 'Story-edit lock', detail: 'Story Editor validates the arc → lock' },
    { title: 'Fact-check', detail: 'isolated Fact-Checker verifies against dossier + web' },
  ],
}

const EP = (args && args.episode)
const TITLE = (args && args.title)
const DEVICE = (args && args.device)
const RESEARCH = (args && args.research)
const EPD = `courses/ableton-devices/episodes/${EP}`
const TEMPLATE = 'courses/ableton-devices/episodes/e01-operator'
const persona = (f) => `You ARE the persona in /Users/zak/zacharysbrown/idm-course/.claude/agents/${f}. FIRST read that file and adopt its mandate, method, and gate rubric. Then do the task.\n\n`
const ctx = `Episode: ${EP} — "${TITLE}" (Ableton ${DEVICE}). Research dossier: /Users/zak/zacharysbrown/idm-course/${RESEARCH}. ` +
  `Structural template to MATCH (format, slide granularity, voice, cue/bed/pause markers, section arc): ${TEMPLATE}/ (read episode.yaml + several script/*.md + clip_manifest.yaml). ` +
  `Voice bible: shared/style/voice.md + lexicon.md (NO banned phrases, no exclamations/emojis; concrete-before-abstract; deflate-before-inflate). All work goes under /Users/zak/zacharysbrown/idm-course/${EPD}/.\n\n`

phase('Outline')
const outline = await agent(
  persona('story-editor.md') + ctx +
  `Create the episode skeleton from the dossier. Write ${EPD}/episode.yaml mirroring the template's schema (id, title, device, week, target_duration_minutes, references, transitions/beds blocks left minimal, and a full slides: list — each slide id, heading, script_md path, and a demos: list of cue ids). Plant a real ARC (cold open → history → synthesis deep-dive → device deep-dive → patch walkthrough → IDM application) with a writeable focus sentence, anecdote/reflection alternation, and act-boundary signposts (the ep1 lesson). Also write ${EPD}/outline.md (the beat sheet: focus sentence, the arc, each section's beats, and where each demo goes conceptually). Return the focus sentence, the section list, and the slide count.`,
  { agentType: 'general-purpose', phase: 'Outline', schema: { type: 'object', properties: {
    focus_sentence: { type: 'string' }, sections: { type: 'array', items: { type: 'string' } }, slide_count: { type: 'integer' } },
    required: ['focus_sentence', 'sections', 'slide_count'] } })

phase('Demo design')
const demos = await agent(
  persona('ableton-expert.md') + ctx +
  `Read ${EPD}/outline.md and the dossier's demo-mapping + technical-depth sections. Write ${EPD}/clip_manifest.yaml: (a) operator_demos-style DEVICE demos for Ableton ${DEVICE} — but use the key name "device_demos" — each with id, concept, what_you_hear, structure (ab/sweep/ladder/single), isolates (the ONE variable), a verification block ({check: ...}), a params block (best-effort ${DEVICE} parameter names + values; mark uncertain ones), midi, and duration_s; (b) song_clips specs from the dossier's song mapping (id, source filename, start/end, fades, normalize_lufs, notes) — these need the user to acquire the WAVs, so add a top comment listing the required source files. Every demo must isolate one variable and have a teaching structure that's obvious on bad speakers. Return the count of device demos and song clips, and the list of required song source files.`,
  { agentType: 'general-purpose', phase: 'Demo design', schema: { type: 'object', properties: {
    device_demos: { type: 'integer' }, song_clips: { type: 'integer' }, required_songs: { type: 'array', items: { type: 'string' } } },
    required: ['device_demos', 'song_clips', 'required_songs'] } })

phase('Scripts')
const scripts = await agent(
  persona('writer.md') + ctx +
  `Read ${EPD}/episode.yaml, ${EPD}/outline.md, ${EPD}/clip_manifest.yaml, and the dossier. Write EVERY slide's script to ${EPD}/script/<slide-id>.md in the show's voice. Use [pause Nms] for timing and place a [cue: <demo-or-clip-id>] exactly where each demo should play, with the frame→demo→label shape (attention cue BEFORE the demo, name AFTER). Ground every claim in the dossier (cite-able). Hit ~40 minutes total across the slides. Stay strictly in voice (no banned phrases/exclamations/emojis). Report how many scripts you wrote.`,
  { agentType: 'general-purpose', phase: 'Scripts' })

phase('Story-edit lock')
const lock = await agent(
  persona('story-editor.md') + ctx +
  `Read every ${EPD}/script/*.md in slide order as a cold table-read. Apply your Gate 2/Gate 5 rubric: arc present, anecdote/reflection alternate, act-boundary signposts, each beat raises→answers, transitions motivated, every [cue] resolves to a clip_manifest id, focus sentence holds. Fix only abrupt seams if needed (light touch). locked=true only if it passes; else list issues.`,
  { agentType: 'general-purpose', phase: 'Story-edit lock', schema: { type: 'object', properties: {
    locked: { type: 'boolean' }, issues: { type: 'array', items: { type: 'string' } } }, required: ['locked', 'issues'] } })

phase('Fact-check')
const facts = await agent(
  persona('fact-checker.md') + ctx +
  `ISOLATED check. Use only ${EPD}/script/*.md, the dossier ${RESEARCH}, and the web. Verify every nontrivial claim (dates, names, gear, quotes, technical assertions). The dossier itself may contain errors — do not treat it as ground truth; cross-check the web. Flag anything unsupported/wrong with the file and a correction.`,
  { agentType: 'general-purpose', phase: 'Fact-check', schema: { type: 'object', properties: {
    cleared: { type: 'boolean' }, corrections: { type: 'array', items: { type: 'object', properties: {
      file: { type: 'string' }, claim: { type: 'string' }, issue: { type: 'string' }, correction: { type: 'string' } },
      required: ['file', 'claim', 'issue', 'correction'] } } }, required: ['cleared', 'corrections'] } })

log(`produce-episode(${EP}): slides=${outline.slide_count} demos=${demos.device_demos} songs_needed=${demos.required_songs.length} locked=${lock.locked} facts_cleared=${facts.cleared}`)
return { episode: EP, outline, demos, lock, facts }

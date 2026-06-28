/* Alignment Spot-Check — vanilla JS + Web Audio API.
   Loads ./alignment_report.json, falls back to ./sample_report.json.
   A/B "before" vs "after" for each demo slot.
   A side may be source=="mp3" (a window of the shared before_mp3 / after_mp3
   that includes narration lead-in + demo + lead-out, with demo_start_ms/
   demo_end_ms marking the demo region) or source=="wav" (a bare standalone
   clip played whole). Only one thing plays at a time across both shared mp3
   elements and any wav Audio. */

(() => {
  'use strict';

  // ---------- state ----------
  const state = {
    report: null,
    slots: [],            // flat list with derived fields
    visible: [],          // slots after filter, in render order
    selectedIndex: -1,    // index into state.slots (the slot.index)
    problemsOnly: false,
    playing: null,        // { slotIndex, which: 'before'|'after' } | null
    audioCtx: null,
    decodeCache: new Map(), // key -> { buffer, peak, rms } | Promise | { error }
    lastWave: new Map(),    // slotIndex -> { which, key }
    stopTimer: null,
  };

  // ---------- dom ----------
  const $ = (sel) => document.querySelector(sel);
  const el = {
    epTitle: $('#epTitle'),
    epId: $('#epId'),
    epGenerated: $('#epGenerated'),
    summary: $('#summary'),
    list: $('#list'),
    problemsOnly: $('#problemsOnly'),
    transport: $('#transport'),
    transportLabel: $('#transport .transport-label'),
    reportSource: $('#reportSource'),
    beforeAudio: $('#beforeAudio'),
    afterAudio: $('#afterAudio'),
  };

  // shared mp3 element for a given side ('before' -> before_mp3, 'after' -> after_mp3)
  function mp3ElFor(which) { return which === 'before' ? el.beforeAudio : el.afterAudio; }
  function mp3SrcFor(which) {
    return which === 'before' ? state.report.before_mp3 : state.report.after_mp3;
  }

  // ---------- boot ----------
  init();

  async function init() {
    el.problemsOnly.addEventListener('change', () => {
      state.problemsOnly = el.problemsOnly.checked;
      render();
    });
    document.addEventListener('keydown', onKey);

    const { report, source } = await loadReport();
    if (!report) {
      el.reportSource.textContent = 'no report found';
      el.list.innerHTML =
        '<div class="banner">Could not load <code>alignment_report.json</code> or ' +
        '<code>sample_report.json</code>. Serve this folder over HTTP ' +
        '(<code>python3 -m http.server</code>) and reload.</div>';
      return;
    }

    state.report = report;
    state.slots = (report.slots || []).slice().sort((a, b) => a.index - b.index);
    el.reportSource.textContent = 'source: ' + source;

    el.epTitle.textContent = report.episode_title || report.episode_id || 'untitled';
    el.epId.textContent = report.episode_id || '—';
    el.epGenerated.textContent = fmtDate(report.generated_at);
    if (report.generated_note) el.epGenerated.title = report.generated_note;
    el.beforeAudio.src = report.before_mp3 || '';
    if (report.after_mp3) el.afterAudio.src = report.after_mp3;

    if (state.slots.length) state.selectedIndex = state.slots[0].index;

    renderSummary();
    render();
  }

  async function loadReport() {
    for (const path of ['./alignment_report.json', './sample_report.json']) {
      try {
        const res = await fetch(path, { cache: 'no-store' });
        if (!res.ok) continue;
        const json = await res.json();
        return { report: json, source: path.replace('./', '') };
      } catch (_) { /* try next */ }
    }
    return { report: null, source: null };
  }

  // ---------- summary ----------
  function renderSummary() {
    const slots = state.slots;
    const counts = { ok: 0, quiet: 0, silent: 0, missing: 0 };
    let improved = 0;
    for (const s of slots) {
      const aStatus = s.after && s.after.status;
      if (aStatus && counts[aStatus] !== undefined) counts[aStatus]++;
      const bBad = s.before && (s.before.status === 'silent' || s.before.status === 'quiet');
      const aGood = s.after && s.after.status === 'ok';
      if (bBad && aGood) improved++;
    }
    const cards = [
      { k: 'slots', v: slots.length, cls: '' },
      { k: 'after ok', v: counts.ok, cls: 'ok' },
      { k: 'after quiet', v: counts.quiet, cls: 'warn' },
      { k: 'after silent', v: counts.silent, cls: 'bad' },
      { k: 'after missing', v: counts.missing, cls: 'bad' },
      { k: 'improved', v: improved, cls: 'accent' },
    ];
    el.summary.innerHTML = cards.map(c =>
      `<div class="stat ${c.cls}"><div class="v">${c.v}</div><div class="k">${c.k}</div></div>`
    ).join('');
  }

  // ---------- filter ----------
  function isProblem(s) {
    const aBad = !s.after || s.after.status !== 'ok';
    const bBad = s.before && (s.before.status === 'silent' || s.before.status === 'quiet');
    return aBad || bBad;
  }

  // ---------- render ----------
  function render() {
    state.visible = state.problemsOnly
      ? state.slots.filter(isProblem)
      : state.slots.slice();

    // keep selection valid/visible
    if (!state.visible.some(s => s.index === state.selectedIndex)) {
      state.selectedIndex = state.visible.length ? state.visible[0].index : -1;
    }

    const frag = document.createDocumentFragment();
    let currentSection = null;

    state.visible.forEach((slot) => {
      if (slot.section !== currentSection) {
        currentSection = slot.section;
        const n = state.visible.filter(s => s.section === currentSection).length;
        const head = document.createElement('div');
        head.className = 'section-head';
        head.innerHTML = `<span>${esc(currentSection)}</span><span class="count">${n} slot${n === 1 ? '' : 's'}</span>`;
        frag.appendChild(head);
      }
      frag.appendChild(buildRow(slot));
    });

    el.list.innerHTML = '';
    if (!state.visible.length) {
      const empty = document.createElement('div');
      empty.className = 'wave-empty';
      empty.style.padding = '48px';
      empty.textContent = state.problemsOnly ? 'No problem slots. All clear.' : 'No slots in report.';
      el.list.appendChild(empty);
    } else {
      el.list.appendChild(frag);
    }
  }

  function buildRow(slot) {
    const row = document.createElement('div');
    row.className = 'row';
    row.dataset.index = String(slot.index);
    if (slot.index === state.selectedIndex) row.classList.add('selected');
    if (state.playing && state.playing.slotIndex === slot.index) row.classList.add('playing');

    const before = slot.before || {};
    const after = slot.after || {};

    row.innerHTML = `
      <div class="row-main">
        <div class="idx">${pad2(slot.index)}</div>
        <div class="title-cell">
          <div class="heading">${esc(slot.heading || slot.slide_id || '')}</div>
          <div class="subline">
            <span class="cue mono">${esc(slot.cue_id || '')}</span>
            <span class="badge ${esc(slot.kind || '')}">${esc(slot.kind || '')}</span>
          </div>
        </div>
        <div class="compare">
          ${chip('before', before)}
          <span class="arrow">&rarr;</span>
          ${chip('after', after)}
        </div>
        <div class="controls">
          ${playBtn('before', slot, before)}
          ${playBtn('after', slot, after)}
        </div>
      </div>
      <div class="detail">
        <div class="narration"><span class="lab">narration before</span>${narration(slot.narration_before)}</div>
        ${waveBlock(slot)}
      </div>`;

    if (slot.index === state.selectedIndex && state._expanded === slot.index) {
      row.classList.add('expanded');
    }

    // events
    row.querySelector('.title-cell').addEventListener('click', (e) => {
      e.stopPropagation();
      selectSlot(slot.index);
      toggleExpand(slot.index);
    });
    row.addEventListener('click', () => selectSlot(slot.index));

    const bBtn = row.querySelector('[data-which="before"]');
    const aBtn = row.querySelector('[data-which="after"]');
    if (bBtn && !bBtn.disabled) bBtn.addEventListener('click', (e) => { e.stopPropagation(); selectSlot(slot.index); play(slot, 'before'); });
    if (aBtn && !aBtn.disabled) aBtn.addEventListener('click', (e) => { e.stopPropagation(); selectSlot(slot.index); play(slot, 'after'); });

    // if expanded, draw any cached waveform
    if (row.classList.contains('expanded')) {
      const last = state.lastWave.get(slot.index);
      if (last) drawWaveInto(row, slot, last.which);
    }

    return row;
  }

  function chip(label, side) {
    if (!side || side.available === false) {
      const st = (side && side.status) || 'missing';
      return `<div class="chip st-${esc(st)} unavailable">
        <span class="lab">${label}</span>
        <span class="stat-name">${esc(st)}</span>
        <span class="db">n/a</span></div>`;
    }
    const st = side.status || 'missing';
    return `<div class="chip st-${esc(st)}">
      <span class="lab">${label}</span>
      <span class="stat-name">${esc(st)}</span>
      <span class="db">${fmtDb(side.mean_db)}</span></div>`;
  }

  function sideIsMp3(side) { return side && side.source === 'mp3'; }

  function sidePlayable(which, side) {
    if (!side || side.available === false) return false;
    if (sideIsMp3(side)) {
      return !!(state.report && mp3SrcFor(which)) && side.start_ms != null && side.end_ms != null;
    }
    // wav (whole-file)
    return !!side.path;
  }

  function playBtn(which, slot, side) {
    const avail = sidePlayable(which, side);
    const active = state.playing && state.playing.slotIndex === slot.index && state.playing.which === which;
    const label = which === 'before' ? 'Before' : 'After';
    const dis = avail ? '' : 'disabled';
    let title;
    if (avail) title = `play ${label.toLowerCase()}`;
    else if (side && side.available === false) title = 'not rendered yet';
    else if (sideIsMp3(side) && !mp3SrcFor(which)) title = which === 'after' ? 'no after_mp3 in report' : 'no episode mp3';
    else title = 'unavailable';
    return `<button class="pbtn ${active ? 'active' : ''}" data-which="${which}" ${dis} title="${esc(title)}">
      <span class="glyph">&#9658;</span>${label}</button>`;
  }

  function waveBlock(slot) {
    return `<div class="wave-wrap">
      <div class="wave-head">
        <span class="which">waveform: <b data-wave-which>none</b></span>
        <span class="readout" data-wave-readout>play a clip to render</span>
      </div>
      <canvas class="wave" data-wave></canvas>
      <div class="wave-empty" data-wave-empty>No clip decoded yet for this slot.</div>
    </div>`;
  }

  function narration(text) {
    if (!text) return '<em style="color:var(--txt-faint)">— none —</em>';
    // emphasize a trailing "Listen." cue
    return esc(text).replace(/\b(Listen\.?)\s*$/i, '<em>$1</em>');
  }

  // ---------- selection / expand ----------
  function selectSlot(index) {
    if (state.selectedIndex === index) return;
    state.selectedIndex = index;
    el.list.querySelectorAll('.row.selected').forEach(r => r.classList.remove('selected'));
    const row = rowEl(index);
    if (row) row.classList.add('selected');
  }

  function toggleExpand(index) {
    const row = rowEl(index);
    if (!row) return;
    const isExp = row.classList.contains('expanded');
    if (isExp) {
      row.classList.remove('expanded');
      state._expanded = null;
    } else {
      // collapse others
      el.list.querySelectorAll('.row.expanded').forEach(r => r.classList.remove('expanded'));
      row.classList.add('expanded');
      state._expanded = index;
      const last = state.lastWave.get(index);
      const slot = slotBy(index);
      if (last && slot) drawWaveInto(row, slot, last.which);
    }
  }

  // ---------- playback ----------
  // Only one thing plays at a time across BOTH shared mp3 elements and any wav Audio.
  function stopAll() {
    if (state.stopTimer) { clearTimeout(state.stopTimer); state.stopTimer = null; }
    try { el.beforeAudio.pause(); } catch (_) {}
    try { el.afterAudio.pause(); } catch (_) {}
    if (state._wavEl) { try { state._wavEl.pause(); } catch (_) {} state._wavEl = null; }
    state.playing = null;
    el.list.querySelectorAll('.row.playing').forEach(r => r.classList.remove('playing'));
    el.list.querySelectorAll('.pbtn.active').forEach(b => b.classList.remove('active'));
    el.transport.classList.remove('is-playing');
    el.transportLabel.textContent = 'STOPPED';
  }

  function play(slot, which) {
    stopAll();
    const side = which === 'before' ? slot.before : slot.after;
    if (!sidePlayable(which, side)) return;

    if (sideIsMp3(side)) playMp3Segment(slot, which, side);
    else playWav(slot, which, side);

    // decode + draw waveform lazily for whichever just played
    decodeAndDraw(slot, which);
  }

  // Play start_ms..end_ms of the shared mp3 element for this side (before_mp3 / after_mp3).
  function playMp3Segment(slot, which, side) {
    const a = mp3ElFor(which);
    if (!a.src || !mp3SrcFor(which)) return;
    const startSec = (side.start_ms || 0) / 1000;
    const durMs = Math.max(0, (side.end_ms || 0) - (side.start_ms || 0));

    const begin = () => {
      try {
        a.currentTime = startSec;
        const p = a.play();
        if (p && p.catch) p.catch((err) => onPlayError(slot, which, err));
      } catch (err) { onPlayError(slot, which, err); }
      state.stopTimer = setTimeout(stopAll, durMs + 60);
    };

    setPlaying(slot.index, which);

    if (a.readyState >= 1 && isFinite(a.duration)) {
      begin();
    } else {
      const onReady = () => { a.removeEventListener('loadedmetadata', onReady); begin(); };
      a.addEventListener('loadedmetadata', onReady);
      a.addEventListener('error', () => onPlayError(slot, which, new Error('mp3 load error')), { once: true });
      try { a.load(); } catch (_) {}
    }
  }

  // Play a whole standalone wav (bare clip, no narration) via its own element.
  function playWav(slot, which, side) {
    const url = side.path;
    const audio = new Audio();
    audio.src = url;
    setPlaying(slot.index, which);
    state._wavEl = audio;
    audio.addEventListener('ended', () => { if (state.playing && state.playing.which === which) stopAll(); });
    audio.addEventListener('error', () => onPlayError(slot, which, new Error('wav load error')));
    const p = audio.play();
    if (p && p.catch) p.catch((err) => onPlayError(slot, which, err));
  }

  function setPlaying(slotIndex, which) {
    state.playing = { slotIndex, which };
    const row = rowEl(slotIndex);
    if (row) {
      row.classList.add('playing');
      const btn = row.querySelector(`.pbtn[data-which="${which}"]`);
      if (btn) btn.classList.add('active');
    }
    el.transport.classList.add('is-playing');
    el.transportLabel.textContent = `PLAYING ${which.toUpperCase()} · #${pad2(slotIndex)}`;
  }

  function onPlayError(slot, which, err) {
    console.warn('playback error', slot.cue_id, which, err);
    const row = rowEl(slot.index);
    if (row) {
      const btn = row.querySelector(`.pbtn[data-which="${which}"]`);
      if (btn) { btn.classList.add('err'); btn.title = 'file not found'; }
    }
    stopAll();
  }

  // ---------- decode + waveform ----------
  function getCtx() {
    if (!state.audioCtx) {
      const AC = window.AudioContext || window.webkitAudioContext;
      state.audioCtx = new AC();
    }
    if (state.audioCtx.state === 'suspended') state.audioCtx.resume().catch(() => {});
    return state.audioCtx;
  }

  function clipKey(slot, which) {
    const side = which === 'before' ? slot.before : slot.after;
    const s = side || {};
    if (sideIsMp3(s)) {
      return `${which}:mp3:${mp3SrcFor(which)}:${s.start_ms}:${s.end_ms}`;
    }
    return `${which}:wav:${s.path}`;
  }

  async function decodeAndDraw(slot, which) {
    const key = clipKey(slot, which);
    state.lastWave.set(slot.index, { which, key });
    // reflect immediately
    const row = rowEl(slot.index);
    if (row && row.classList.contains('expanded')) markWaveLoading(row, which);

    try {
      const data = await decodeClip(slot, which, key);
      const r = rowEl(slot.index);
      if (r && r.classList.contains('expanded')) drawWave(r, data, which);
    } catch (err) {
      const r = rowEl(slot.index);
      if (r && r.classList.contains('expanded')) drawWaveError(r, which);
    }
  }

  function decodeClip(slot, which, key) {
    const cached = state.decodeCache.get(key);
    if (cached) {
      if (cached.error) return Promise.reject(cached.error);
      if (cached instanceof Promise) return cached;
      return Promise.resolve(cached);
    }
    const p = (async () => {
      const side = which === 'before' ? slot.before : slot.after;
      const s = side || {};
      let url, segment = null, demo = null;
      if (sideIsMp3(s)) {
        // segment of the shared mp3; demo region sits inside the window
        url = mp3SrcFor(which);
        const startMs = s.start_ms || 0;
        const endMs = s.end_ms || 0;
        segment = { start: startMs / 1000, end: endMs / 1000 };
        if (s.demo_start_ms != null && s.demo_end_ms != null && endMs > startMs) {
          // demo bracket as a fraction of the played window
          demo = {
            from: clamp01((s.demo_start_ms - startMs) / (endMs - startMs)),
            to: clamp01((s.demo_end_ms - startMs) / (endMs - startMs)),
          };
        }
      } else {
        // bare wav clip: the whole file is the demo, no bracket
        url = s.path;
      }
      const res = await fetch(url, { cache: 'force-cache' });
      if (!res.ok) throw new Error('HTTP ' + res.status);
      const arr = await res.arrayBuffer();
      const ctx = getCtx();
      const buffer = await ctx.decodeAudioData(arr.slice(0));
      const analyzed = analyze(buffer, segment);
      analyzed.demo = demo;
      state.decodeCache.set(key, analyzed);
      return analyzed;
    })();
    state.decodeCache.set(key, p);
    p.catch((err) => state.decodeCache.set(key, { error: err }));
    return p;
  }

  // reduce buffer to peak/min bins + rms/peak readout. segment in seconds (optional).
  function analyze(buffer, segment) {
    const ch0 = buffer.getChannelData(0);
    const sr = buffer.sampleRate;
    let s0 = 0, s1 = ch0.length;
    if (segment) {
      s0 = Math.max(0, Math.floor(segment.start * sr));
      s1 = Math.min(ch0.length, Math.ceil(segment.end * sr));
      if (s1 <= s0) { s0 = 0; s1 = ch0.length; }
    }
    const n = s1 - s0;
    const BINS = 900;
    const mins = new Float32Array(BINS);
    const maxs = new Float32Array(BINS);
    let sumSq = 0, peak = 0;
    const step = n / BINS;
    for (let b = 0; b < BINS; b++) {
      const from = s0 + Math.floor(b * step);
      const to = s0 + Math.floor((b + 1) * step);
      let mn = 1, mx = -1;
      for (let i = from; i < to && i < s1; i++) {
        const v = ch0[i];
        if (v < mn) mn = v;
        if (v > mx) mx = v;
      }
      if (mn === 1 && mx === -1) { mn = 0; mx = 0; }
      mins[b] = mn; maxs[b] = mx;
    }
    // rms/peak across whole segment (decimated for speed)
    const stride = Math.max(1, Math.floor(n / 50000));
    let cnt = 0;
    for (let i = s0; i < s1; i += stride) {
      const v = ch0[i];
      sumSq += v * v;
      const a = Math.abs(v);
      if (a > peak) peak = a;
      cnt++;
    }
    const rms = cnt ? Math.sqrt(sumSq / cnt) : 0;
    return {
      mins, maxs, bins: BINS,
      durationSec: n / sr,
      rmsDb: toDb(rms),
      peakDb: toDb(peak),
    };
  }

  function markWaveLoading(row, which) {
    const w = row.querySelector('[data-wave-which]');
    const r = row.querySelector('[data-wave-readout]');
    const empty = row.querySelector('[data-wave-empty]');
    const canvas = row.querySelector('[data-wave]');
    if (w) w.textContent = which;
    if (r) r.textContent = 'decoding…';
    if (empty) empty.style.display = 'none';
    if (canvas) canvas.style.display = 'block';
  }

  function drawWaveInto(row, slot, which) {
    const data = state.decodeCache.get(clipKey(slot, which));
    if (data && !(data instanceof Promise) && !data.error) drawWave(row, data, which);
    else decodeAndDraw(slot, which);
  }

  function drawWaveError(row, which) {
    const w = row.querySelector('[data-wave-which]');
    const r = row.querySelector('[data-wave-readout]');
    const empty = row.querySelector('[data-wave-empty]');
    const canvas = row.querySelector('[data-wave]');
    if (w) w.textContent = which;
    if (canvas) canvas.style.display = 'none';
    if (empty) { empty.style.display = 'block'; empty.textContent = 'file not found — could not decode'; }
    if (r) r.textContent = '—';
  }

  function drawWave(row, data, which) {
    const canvas = row.querySelector('[data-wave]');
    const whichEl = row.querySelector('[data-wave-which]');
    const readout = row.querySelector('[data-wave-readout]');
    const empty = row.querySelector('[data-wave-empty]');
    if (!canvas) return;

    if (empty) empty.style.display = 'none';
    canvas.style.display = 'block';
    if (whichEl) whichEl.textContent = data.demo ? `${which} (demo bracketed)` : which;
    if (readout) {
      let html =
        `rms <span>${fmtDb(data.rmsDb)}</span> &middot; peak <span>${fmtDb(data.peakDb)}</span> &middot; ` +
        `win <span>${data.durationSec.toFixed(2)}s</span>`;
      if (data.demo) {
        const demoSec = data.durationSec * (data.demo.to - data.demo.from);
        html += ` &middot; demo <span>${demoSec.toFixed(2)}s</span>`;
      }
      readout.innerHTML = html;
    }

    const dpr = window.devicePixelRatio || 1;
    const cssW = canvas.clientWidth || 600;
    const cssH = canvas.clientHeight || 90;
    canvas.width = Math.round(cssW * dpr);
    canvas.height = Math.round(cssH * dpr);
    const ctx = canvas.getContext('2d');
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, cssW, cssH);

    const mid = cssH / 2;
    const demo = data.demo; // {from,to} fractions of window, or null

    // lead-in / lead-out shading: dim the narration portions outside the demo region
    if (demo) {
      const dx0 = demo.from * cssW;
      const dx1 = demo.to * cssW;
      ctx.fillStyle = 'rgba(0,0,0,0.42)';
      if (dx0 > 0) ctx.fillRect(0, 0, dx0, cssH);
      if (dx1 < cssW) ctx.fillRect(dx1, 0, cssW - dx1, cssH);
      // subtle highlight band behind the demo region
      ctx.fillStyle = 'rgba(78,161,255,0.08)';
      ctx.fillRect(dx0, 0, dx1 - dx0, cssH);
    }

    // grid: center line + quarter lines
    ctx.strokeStyle = '#1c242e';
    ctx.lineWidth = 1;
    ctx.beginPath(); ctx.moveTo(0, mid); ctx.lineTo(cssW, mid); ctx.stroke();
    ctx.strokeStyle = '#141a22';
    [0.25, 0.75].forEach(f => {
      ctx.beginPath(); ctx.moveTo(0, cssH * f); ctx.lineTo(cssW, cssH * f); ctx.stroke();
    });

    // waveform fill — dim outside the demo bracket, full color inside
    const bins = data.bins;
    const bw = cssW / bins;
    const fullColor = which === 'before' ? '#6e93bd' : '#4ea1ff';
    const dimColor = which === 'before' ? '#3c4f63' : '#2f5b86';
    for (let b = 0; b < bins; b++) {
      const x = b * bw;
      const frac = (b + 0.5) / bins;
      const inDemo = !demo || (frac >= demo.from && frac <= demo.to);
      ctx.fillStyle = inDemo ? fullColor : dimColor;
      const top = mid - Math.max(0, data.maxs[b]) * mid;
      const bot = mid - Math.min(0, data.mins[b]) * mid;
      const h = Math.max(1, bot - top);
      ctx.fillRect(x, top, Math.max(0.6, bw - 0.2), h);
    }

    // demo bracket: vertical boundary lines + labels
    if (demo) {
      const dx0 = demo.from * cssW;
      const dx1 = demo.to * cssW;
      ctx.strokeStyle = '#4ea1ff';
      ctx.lineWidth = 1;
      ctx.setLineDash([3, 3]);
      [dx0, dx1].forEach(x => {
        ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, cssH); ctx.stroke();
      });
      ctx.setLineDash([]);
      ctx.font = '9px ui-monospace, monospace';
      ctx.textBaseline = 'top';
      ctx.fillStyle = '#7d8997';
      if (dx0 > 22) ctx.fillText('lead-in', 4, 3);
      ctx.fillStyle = '#9cc6ff';
      ctx.fillText('demo', Math.min(cssW - 30, dx0 + 4), 3);
      if (cssW - dx1 > 26) {
        ctx.fillStyle = '#7d8997';
        ctx.textAlign = 'right';
        ctx.fillText('lead-out', cssW - 4, 3);
        ctx.textAlign = 'left';
      }
    }
  }

  // ---------- keyboard ----------
  function onKey(e) {
    const tag = (e.target && e.target.tagName) || '';
    if (tag === 'INPUT' || tag === 'TEXTAREA') return;

    const key = e.key;
    if (key === 'j' || key === 'J' || key === 'ArrowDown') { e.preventDefault(); move(1); }
    else if (key === 'k' || key === 'K' || key === 'ArrowUp') { e.preventDefault(); move(-1); }
    else if (key === 'b' || key === 'B') { e.preventDefault(); withSelected(s => play(s, 'before')); }
    else if (key === 'a' || key === 'A') { e.preventDefault(); withSelected(s => play(s, 'after')); }
    else if (key === ' ') { e.preventDefault(); stopAll(); }
    else if (key === 'Enter') { e.preventDefault(); if (state.selectedIndex >= 0) toggleExpand(state.selectedIndex); }
  }

  function move(delta) {
    const vis = state.visible;
    if (!vis.length) return;
    let pos = vis.findIndex(s => s.index === state.selectedIndex);
    if (pos < 0) pos = 0;
    else pos = Math.min(vis.length - 1, Math.max(0, pos + delta));
    const next = vis[pos].index;
    selectSlot(next);
    const row = rowEl(next);
    if (row) row.scrollIntoView({ block: 'nearest' });
  }

  function withSelected(fn) {
    const s = slotBy(state.selectedIndex);
    if (s) fn(s);
  }

  // ---------- helpers ----------
  function rowEl(index) { return el.list.querySelector(`.row[data-index="${index}"]`); }
  function slotBy(index) { return state.slots.find(s => s.index === index); }

  function toDb(lin) {
    if (!lin || lin <= 0) return -Infinity;
    return 20 * Math.log10(lin);
  }
  function fmtDb(db) {
    if (db == null || !isFinite(db)) return '−∞ dB';
    return (db <= -120 ? '−∞' : db.toFixed(1)) + ' dB';
  }
  function fmtDate(iso) {
    if (!iso) return '—';
    const d = new Date(iso);
    if (isNaN(d)) return iso;
    return d.toISOString().replace('T', ' ').replace(/\.\d+Z$/, 'Z');
  }
  function pad2(n) { return String(n).padStart(2, '0'); }
  function clamp01(x) { return x < 0 ? 0 : x > 1 ? 1 : x; }
  function esc(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }
})();

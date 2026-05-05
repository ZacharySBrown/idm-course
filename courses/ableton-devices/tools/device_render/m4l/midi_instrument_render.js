// midi_instrument_render.js
// ─────────────────────────────────────────────────────────────────────────────
// Classic Max [js] script for the MidiInstrumentRender.amxd device. Generic —
// works for any Live MIDI instrument (Operator, Analog, Wavetable, Meld, Drum
// Rack/Simpler, Granulator). Reads a spec.json produced by device_render.py,
// applies LOM-set parameters per demo onto the instrument, drops a MIDI clip,
// records via a Resampling audio track, then copies the resulting WAV.
//
// Why no track.freeze(): Live's LOM does not expose freeze/unfreeze. Instead
// we use Live's standard Session-view recording into an armed audio track
// whose input is "Resampling" — captures the master output exactly like
// freeze would, fully automatable via LOM.
//
// Track layout required (the user builds a `.als` template like this):
//     [0] MIDI track:
//             devices: [MidiInstrumentRender.amxd, target instrument]
//     [1] AUDIO track:
//             Input Type:    "Resampling"
//             Monitor:       "Off"
//             Arm:            on
// Edit TRACK_INDICES below if your layout differs.
//
// The script loads param_maps/<spec.device_class>.json automatically so it
// can translate friendly param names ("Algorithm", "OSC1 Wave") into LiveAPI
// indices. Run lom_probe first to generate this file.
//
// Inlet messages:
//     load_spec <abs_spec_path>       — load + parse spec.json
//     render                           — render every demo in the spec, sequentially
//     render_one <demo_id>             — render just one demo
//     status                           — outlet 0: dump current state
//
// Outlets:
//     0: status / progress messages (free-form)
//     1: render_done <demo_id>         — emitted per completed demo
//     2: error <message>               — emitted on any failure
// ─────────────────────────────────────────────────────────────────────────────

inlets  = 1;
outlets = 3;

var MIDI_TRACK_IDX   = 0;     // MIDI track with [this M4L, target instrument]
var AUDIO_TRACK_IDX  = 1;     // Audio track with Resampling input
var TARGET_DEV_IDX   = 1;     // Target instrument index on the MIDI track
var POLL_MS          = 100;
var TAIL_BUFFER_S    = 0.5;   // extra time to capture release tail
var STOP_SETTLE_MS   = 1500;  // initial wait after stop before polling
var FLUSH_TIMEOUT_S  = 10;    // max time to wait for Live to flush WAV
var MIN_VALID_BYTES  = 1024;  // a real captured WAV must be larger than this
var INTER_DEMO_MS    = 1500;  // delay between cleanup of one demo and start of next
var MAX_RETRIES      = 2;     // auto-retry a demo after a transient "no clip recorded"

var REPO_ROOT     = "/Users/zak/zacharysbrown/idm-course";
var PARAM_MAP_DIR = "/courses/ableton-devices/tools/device_render/param_maps";

var spec = null;              // parsed spec.json
var paramMap = null;          // loaded from param_maps/<device_class>.json
var renderQueue = [];
var currentDemo = null;
var currentRender = null;     // { audioSlotIdx, durationS, startedAt }
var flushTask = null;         // module-level so pollFlush can cancel itself
var automationTasks = [];     // pending per-demo automation Tasks
var sanityTask = null;        // post-fire 300ms diagnostic
var fireTask = null;          // delayed clip fire after record_mode set
var stopTask = null;          // scheduled stopResamplingRecord

function status(msg) {
    outlet(0, "status", String(msg));
    post(msg + "\n");
}

function emitEvent(obj) {
    if (!spec || !spec.events_path) return;
    obj.ts = Date.now();
    var f = new File(toMaxPath(spec.events_path), "readwrite");
    if (!f.isopen) return;
    try {
        f.position = f.eof;
        f.writestring(JSON.stringify(obj) + "\n");
        f.close();
    } catch (e) {
        try { f.close(); } catch (_e) {}
    }
}

function load_spec() {
    var args = arrayfromargs(messagename, arguments);
    if (args.length < 2) {
        status("load_spec: need spec path");
        return;
    }
    var path = String(args[1]);
    var raw;
    try {
        var f = new File(toMaxPath(path), "read");
        if (!f.isopen) { status("cannot open " + path); return; }
        raw = "";
        while (f.position < f.eof) raw += f.readstring(4096);
        f.close();
    } catch (e) {
        status("read failed: " + e);
        return;
    }
    try {
        spec = JSON.parse(raw);
    } catch (e) {
        status("parse spec failed: " + e);
        return;
    }
    status("spec loaded: " + spec.episode_id + " (" + spec.demos.length + " demos, device=" + (spec.device_class || "?") + ")");
    loadParamMap();
}

function loadParamMap() {
    if (!spec) return;
    var slug = (spec.device_class || "").toLowerCase().replace(/[^a-z0-9]+/g, "_");
    if (!slug) { status("spec missing device_class — paramMap not loaded"); return; }
    var path = REPO_ROOT + PARAM_MAP_DIR + "/" + slug + ".json";
    try {
        var f = new File(toMaxPath(path), "read");
        if (!f.isopen) {
            status("paramMap not found: " + path + " (run LomProbe first)");
            return;
        }
        var raw = "";
        while (f.position < f.eof) raw += f.readstring(4096);
        f.close();
        paramMap = JSON.parse(raw);
        status("paramMap loaded: " + paramMap.parameter_count + " params for " + paramMap.device_class);
    } catch (e) {
        status("paramMap load failed: " + e);
    }
}

function render() {
    if (!spec) { status("no spec loaded"); return; }
    renderQueue = spec.demos.map(function(d) { return d.id; });
    status("queued " + renderQueue.length + " demo(s)");
    nextRender();
}

function render_one() {
    if (!spec) { status("no spec loaded"); return; }
    var args = arrayfromargs(messagename, arguments);
    if (args.length < 2) { status("render_one: need demo id"); return; }
    var did = String(args[1]);
    if (!findDemo(did)) { status("demo not found: " + did); return; }
    renderQueue = [did];
    nextRender();
}

function nextRender() {
    if (renderQueue.length === 0) {
        status("render queue empty");
        return;
    }
    var did = renderQueue.shift();
    var demo = findDemo(did);
    if (!demo) { status("demo missing: " + did); nextRender(); return; }

    currentDemo = demo;
    if (demo._retry === undefined) demo._retry = 0;
    var retryNote = demo._retry > 0 ? " (retry " + demo._retry + "/" + MAX_RETRIES + ")" : "";
    status("rendering " + did + retryNote);
    emitEvent({ event: "render_start", demo_id: did, retry: demo._retry });

    if (!demo.params) {
        status("demo " + did + " has no params block — skipping (manual render needed)");
        emitEvent({ event: "render_skipped", demo_id: did, reason: "no params block" });
        currentDemo = null;
        nextRender();
        return;
    }

    try {
        applyParams(demo.params);
        ensureMidiClip(demo);
        startResamplingRecord(demo);
    } catch (e) {
        status("render failed: " + e);
        emitEvent({ event: "error", demo_id: did, message: String(e) });
        currentDemo = null;
        nextRender();
    }
}

function startResamplingRecord(demo) {
    var audioPath = "live_set tracks " + AUDIO_TRACK_IDX;
    var audio = new LiveAPI(audioPath);
    if (!audio || audio.id === "0") {
        throw new Error("audio render track at index " + AUDIO_TRACK_IDX + " not found");
    }

    // Diagnostics: confirm the audio track is configured for capture.
    var inputType = "?", monitor = "?";
    try { inputType = stringVal(audio.get("input_routing_type")); } catch (e) {}
    try { monitor = stringVal(audio.get("current_monitoring_state")); } catch (e) {}
    status("audio track: arm=" + audio.get("arm") +
           " input_routing_type=" + inputType +
           " monitor=" + monitor);

    // Find first empty audio clip slot
    var slotCount = parseInt(audio.getcount("clip_slots"));
    var slotIdx = -1;
    for (var i = 0; i < slotCount; i++) {
        var s = new LiveAPI(audioPath + " clip_slots " + i);
        if (parseInt(s.get("has_clip")) === 0) { slotIdx = i; break; }
    }
    if (slotIdx < 0) throw new Error("no empty audio clip slot on track " + AUDIO_TRACK_IDX);
    status("using audio slot " + slotIdx);

    audio.set("arm", 1);

    var song = new LiveAPI("live_set");
    try { song.set("clip_trigger_quantization", 0); } catch (e) {}

    var midi = demo.midi || {};
    var len_s = (midi.length_s || demo.duration_s || 4) + TAIL_BUFFER_S;

    currentRender = {
        audioSlotIdx: slotIdx,
        durationS: len_s,
        startedAt: Date.now()
    };

    song.set("record_mode", 1);
    status("record_mode set; will fire after settle");

    // Brief delay so Live commits record_mode=1 before fires register.
    if (fireTask) { try { fireTask.cancel(); } catch (e) {} }
    fireTask = new Task(function() {
        new LiveAPI("live_set tracks " + MIDI_TRACK_IDX + " clip_slots 0").call("fire");
        new LiveAPI(audioPath + " clip_slots " + slotIdx).call("fire");
        scheduleAutomation(demo.automation);
        // Sanity check 350ms after the fire actually happened.
        if (sanityTask) { try { sanityTask.cancel(); } catch (e) {} }
        sanityTask = new Task(function() { fireSanityCheck(audioPath, slotIdx); });
        sanityTask.schedule(350);
    });
    fireTask.schedule(150);

    if (stopTask) { try { stopTask.cancel(); } catch (e) {} }
    stopTask = new Task(stopResamplingRecord);
    stopTask.schedule(150 + len_s * 1000);
}

function fireSanityCheck(audioPath, slotIdx) {
    var slot = new LiveAPI(audioPath + " clip_slots " + slotIdx);
    var hasC = parseInt(slot.get("has_clip"));
    var rec = "?";
    if (hasC === 1) {
        try { rec = String(new LiveAPI(audioPath + " clip_slots " + slotIdx + " clip").get("is_recording")); } catch (e) {}
    }
    status("post-fire: slot " + slotIdx + " has_clip=" + hasC + " is_recording=" + rec);

    if (hasC === 0) {
        // Recording did not start. Don't wait for the full demo duration —
        // abort immediately and let the retry path run.
        status("recording never started; aborting demo to retry");
        if (stopTask) { try { stopTask.cancel(); } catch (e) {} stopTask = null; }
        cancelAutomation();
        try { new LiveAPI("live_set").set("record_mode", 0); } catch (e) {}
        try { new LiveAPI("live_set tracks " + MIDI_TRACK_IDX + " clip_slots 0").call("stop"); } catch (e) {}
        try { new LiveAPI(audioPath + " clip_slots " + slotIdx).call("stop"); } catch (e) {}
        if (currentDemo && currentDemo._retry < MAX_RETRIES) {
            currentDemo._retry++;
            status("re-queueing " + currentDemo.id + " for retry " + currentDemo._retry + "/" + MAX_RETRIES);
            renderQueue.unshift(currentDemo.id);
        } else {
            var did = currentDemo ? currentDemo.id : "?";
            emitEvent({ event: "error", demo_id: did, message: "recording never started after " + MAX_RETRIES + " retries" });
        }
        cleanupAndNext();
    }
}

function scheduleAutomation(automation) {
    cancelAutomation();
    if (!automation) return;
    var devPath = "live_set tracks " + MIDI_TRACK_IDX + " devices " + TARGET_DEV_IDX;
    for (var paramName in automation) {
        if (!automation.hasOwnProperty(paramName)) continue;
        var idx = lookupParamIndex(paramName);
        if (idx === null) {
            status("automation: unknown param '" + paramName + "' (skipped)");
            continue;
        }
        var auto = automation[paramName];
        scheduleParamAutomation(devPath, idx, paramName, auto);
    }
}

function scheduleParamAutomation(devPath, paramIdx, paramName, auto) {
    var paramPath = devPath + " parameters " + paramIdx;
    if (auto.steps && auto.step_s !== undefined) {
        // Discrete steps: e.g. {steps: [0, 40, 60, 70], step_s: 1.5}
        for (var i = 0; i < auto.steps.length; i++) {
            (function(stepIdx, value) {
                var t = new Task(function() {
                    try { new LiveAPI(paramPath).set("value", value); }
                    catch (e) { status("automation set failed: " + e); }
                });
                t.schedule(stepIdx * auto.step_s * 1000);
                automationTasks.push(t);
            })(i, auto.steps[i]);
        }
        status("automation: " + paramName + " stepped " + auto.steps.length + "x every " + auto.step_s + "s");
    } else if (auto.from !== undefined && auto.to !== undefined && auto.ramp_s !== undefined) {
        // Continuous ramp: e.g. {from: 0, to: 100, ramp_s: 8}
        var hz = auto.rate_hz || 30;
        var totalSteps = Math.max(2, Math.round(auto.ramp_s * hz));
        var dt = (auto.ramp_s * 1000) / totalSteps;
        for (var j = 0; j <= totalSteps; j++) {
            (function(stepIdx) {
                var v = auto.from + (auto.to - auto.from) * (stepIdx / totalSteps);
                var t = new Task(function() {
                    try { new LiveAPI(paramPath).set("value", v); }
                    catch (e) { status("automation set failed: " + e); }
                });
                t.schedule(stepIdx * dt);
                automationTasks.push(t);
            })(j);
        }
        status("automation: " + paramName + " ramp " + auto.from + "→" + auto.to + " over " + auto.ramp_s + "s");
    } else {
        status("automation: '" + paramName + "' has unrecognized shape");
    }
}

function cancelAutomation() {
    for (var i = 0; i < automationTasks.length; i++) {
        try { automationTasks[i].cancel(); } catch (e) {}
    }
    automationTasks = [];
}

function stopResamplingRecord() {
    if (!currentRender) return;
    var audioPath = "live_set tracks " + AUDIO_TRACK_IDX;
    var midiPath  = "live_set tracks " + MIDI_TRACK_IDX;

    // Stop global record + both clips. Leave the audio track ARMED so the
    // next demo in the batch can fire into it without re-arming.
    new LiveAPI("live_set").set("record_mode", 0);
    try { new LiveAPI(midiPath  + " clip_slots 0").call("stop"); } catch (e) {}
    try { new LiveAPI(audioPath + " clip_slots " + currentRender.audioSlotIdx).call("stop"); } catch (e) {}

    var captureT = new Task(captureRecorded);
    captureT.schedule(STOP_SETTLE_MS);
}

function captureRecorded() {
    if (!currentRender || !currentDemo) return;
    var did = currentDemo.id;
    var slotPath = "live_set tracks " + AUDIO_TRACK_IDX + " clip_slots " + currentRender.audioSlotIdx;
    var slot = new LiveAPI(slotPath);

    if (parseInt(slot.get("has_clip")) !== 1) {
        status("no clip recorded into slot " + currentRender.audioSlotIdx);
        // Transient — retry up to MAX_RETRIES before giving up.
        if (currentDemo && currentDemo._retry < MAX_RETRIES) {
            currentDemo._retry++;
            status("re-queueing " + currentDemo.id + " for retry " + currentDemo._retry + "/" + MAX_RETRIES);
            renderQueue.unshift(currentDemo.id);
        } else {
            emitEvent({ event: "error", demo_id: did, message: "no recorded clip after " + MAX_RETRIES + " retries" });
        }
        cleanupAndNext();
        return;
    }

    var clip = new LiveAPI(slotPath + " clip");
    var isRec = parseInt(clip.get("is_recording") || 0);
    var src = stringVal(clip.get("file_path"));
    status("clip state: is_recording=" + isRec + ", file_path=" + src);

    if (!src || src === "0" || src === "") {
        status("recorded clip has no file_path");
        emitEvent({ event: "error", demo_id: did, message: "no file_path" });
        cleanupAndNext();
        return;
    }

    currentRender.src = src;
    currentRender.flushStartedAt = Date.now();
    currentRender.lastSize = -1;
    if (flushTask) { try { flushTask.cancel(); } catch (e) {} }
    flushTask = new Task(pollFlush);
    flushTask.interval = 250;
    flushTask.repeat();
}

function stopFlushTask() {
    if (flushTask) {
        try { flushTask.cancel(); } catch (e) {}
        flushTask = null;
    }
}

function pollFlush() {
    if (!currentRender || !currentDemo) { stopFlushTask(); return; }
    var did = currentDemo.id;
    var src = currentRender.src;

    var slotPath = "live_set tracks " + AUDIO_TRACK_IDX + " clip_slots " + currentRender.audioSlotIdx;
    var clip = new LiveAPI(slotPath + " clip");
    var isRec = 0;
    try { isRec = parseInt(clip.get("is_recording") || 0); } catch (e) {}

    var size = fileSize(src);
    var elapsed = (Date.now() - currentRender.flushStartedAt) / 1000;

    if (isRec === 0 && size >= MIN_VALID_BYTES && size === currentRender.lastSize) {
        stopFlushTask();
        finalizeCopy(src, did);
        return;
    }
    currentRender.lastSize = size;

    if (elapsed > FLUSH_TIMEOUT_S) {
        stopFlushTask();
        status("flush timeout after " + elapsed + "s (size=" + size + ", is_recording=" + isRec + ")");
        emitEvent({ event: "error", demo_id: did, message: "flush timeout (size=" + size + ")" });
        cleanupAndNext();
    }
}

function finalizeCopy(src, did) {
    // Don't copy from Max — its File API mangles binary copies on paths with
    // spaces. Instead emit the source path as an event; the Python CLI sees
    // it and does the copy with shutil.copyfile (reliable).
    var size = fileSize(src);
    status("recorded " + size + " bytes at " + src);
    emitEvent({
        event: "render_done",
        demo_id: did,
        src_path: src,
        bytes: size
    });
    cleanupAndNext();
}

function fileSize(posixPath) {
    var f = new File(toMaxPath(posixPath), "read");
    if (!f.isopen) return -1;
    var sz = f.eof;
    f.close();
    return sz;
}

function cleanupAndNext() {
    cancelAutomation();
    if (fireTask)   { try { fireTask.cancel();   } catch (e) {} fireTask = null; }
    if (stopTask)   { try { stopTask.cancel();   } catch (e) {} stopTask = null; }
    if (sanityTask) { try { sanityTask.cancel(); } catch (e) {} sanityTask = null; }
    if (flushTask)  { try { flushTask.cancel();  } catch (e) {} flushTask = null; }
    var audioPath = "live_set tracks " + AUDIO_TRACK_IDX;
    var midiPath  = "live_set tracks " + MIDI_TRACK_IDX;
    if (currentRender) {
        try { new LiveAPI(audioPath + " clip_slots " + currentRender.audioSlotIdx).call("delete_clip"); } catch (e) {}
    }
    try { new LiveAPI(midiPath + " clip_slots 0").call("delete_clip"); } catch (e) {}
    currentRender = null;
    currentDemo = null;
    var t = new Task(nextRender);
    t.schedule(INTER_DEMO_MS);
}

function applyParams(params) {
    var devPath = "live_set tracks " + MIDI_TRACK_IDX + " devices " + TARGET_DEV_IDX;
    var device = new LiveAPI(devPath);
    if (!device || device.id === "0") {
        throw new Error("target device not at index " + TARGET_DEV_IDX);
    }
    for (var name in params) {
        if (!params.hasOwnProperty(name)) continue;
        var idx = lookupParamIndex(name);
        if (idx === null) {
            status("unknown param: " + name + " (skipped)");
            continue;
        }
        var p = new LiveAPI(devPath + " parameters " + idx);
        var v = params[name];
        if (typeof v === "string" && p.getcount("value_items") > 0) {
            v = enumValueIndex(p, v);
            if (v === null) { status("bad enum for " + name); continue; }
        }
        p.set("value", Number(v));
    }
}

function lookupParamIndex(name) {
    if (!paramMap || !paramMap.parameters) return null;
    for (var i = 0; i < paramMap.parameters.length; i++) {
        var p = paramMap.parameters[i];
        if (p.name === name || p.original_name === name) return p.index;
    }
    return null;
}

function enumValueIndex(p, label) {
    // value_items returns the full list — indexed access doesn't work.
    var v = p.get("value_items");
    if (!v || typeof v !== "object" || !v.length) return null;
    for (var i = 0; i < v.length; i++) {
        if (String(v[i]) === label) return i;
    }
    return null;
}

function ensureMidiClip(demo) {
    var trackPath = "live_set tracks " + MIDI_TRACK_IDX;
    var slot = new LiveAPI(trackPath + " clip_slots 0");
    if (parseInt(slot.get("has_clip")) === 1) {
        slot.call("delete_clip");
    }
    var midi = demo.midi || { note: "C3", length_s: 4 };
    // Resolve the clip length: explicit `length_s`, else demo.duration_s, else 4.
    var clip_audio_s = midi.length_s || demo.duration_s || 4;
    var clip_total_s = clip_audio_s + TAIL_BUFFER_S;
    slot.call("create_clip", secondsToBeats(clip_total_s));
    var clip = new LiveAPI(trackPath + " clip_slots 0 clip");
    try { clip.set("looping", 0); } catch (e) {}

    // Build the notes list. Three input shapes (in priority order):
    //   1. midi.notes: [{ pitch|note, start_time?|t?, duration|dur_s?, velocity|vel?, mute? }, ...]
    //      — explicit, multi-note. Times in seconds (we convert).
    //   2. midi.note: "C3" (single note from t=0 for clip_audio_s)
    //   3. fallback: C3 from t=0 for clip_audio_s
    var notesIn = midi.notes;
    if (!notesIn) {
        notesIn = [{ note: midi.note || "C3", t: 0, dur_s: clip_audio_s, vel: midi.vel || 100 }];
    }
    var notesOut = [];
    for (var i = 0; i < notesIn.length; i++) {
        var n = notesIn[i];
        var pitch = (typeof n.pitch === "number") ? n.pitch : noteNameToMidi(n.note || "C3");
        var t_s = (n.t !== undefined) ? n.t : (n.start_time !== undefined ? n.start_time : 0);
        var dur_s = (n.dur_s !== undefined) ? n.dur_s : (n.duration !== undefined ? n.duration : (clip_audio_s - t_s));
        if (dur_s <= 0) dur_s = 0.05;
        var vel = (n.vel !== undefined) ? n.vel : (n.velocity !== undefined ? n.velocity : 100);
        notesOut.push({
            pitch: pitch,
            start_time: secondsToBeats(t_s),
            duration: secondsToBeats(dur_s),
            velocity: vel,
            mute: n.mute || 0
        });
    }
    clip.call("add_new_notes", JSON.stringify({ notes: notesOut }));
}

function secondsToBeats(s) {
    var bpm = parseFloat(new LiveAPI("live_set").get("tempo"));
    return s * bpm / 60.0;
}

function noteNameToMidi(name) {
    var map = { C: 0, "C#": 1, Db: 1, D: 2, "D#": 3, Eb: 3, E: 4, F: 5, "F#": 6, Gb: 6, G: 7, "G#": 8, Ab: 8, A: 9, "A#": 10, Bb: 10, B: 11 };
    var m = String(name).match(/^([A-G][b#]?)(-?\d+)$/);
    if (!m) return 60;
    return (parseInt(m[2]) + 2) * 12 + map[m[1]];  // Live convention: C3 = 60
}

function copyFile(srcPosix, dstPosix) {
    try {
        var src = new File(toMaxPath(srcPosix), "read");
        if (!src.isopen) return false;
        var dst = new File(toMaxPath(dstPosix), "write");
        if (!dst.isopen) { src.close(); return false; }
        while (src.position < src.eof) {
            dst.writebytes(src.readbytes(65536));
        }
        src.close();
        dst.close();
        return true;
    } catch (e) {
        return false;
    }
}

function findDemo(did) {
    if (!spec) return null;
    for (var i = 0; i < spec.demos.length; i++) {
        if (spec.demos[i].id === did) return spec.demos[i];
    }
    return null;
}

function stringVal(v) {
    if (v && typeof v === "object" && v.length !== undefined) v = v[0];
    return String(v);
}

function toMaxPath(posixPath) {
    var p = String(posixPath);
    if (p.indexOf("/") === 0) return "Macintosh HD:" + p;
    return p;
}

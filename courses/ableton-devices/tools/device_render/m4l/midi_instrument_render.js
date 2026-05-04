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
var STOP_SETTLE_MS   = 800;   // wait after stop before reading file_path

var REPO_ROOT     = "/Users/zak/zacharysbrown/idm-course";
var PARAM_MAP_DIR = "/courses/ableton-devices/tools/device_render/param_maps";

var spec = null;              // parsed spec.json
var paramMap = null;          // loaded from param_maps/<device_class>.json
var renderQueue = [];
var currentDemo = null;
var currentRender = null;     // { audioSlotIdx, durationS, startedAt }

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
    status("rendering " + did);
    emitEvent({ event: "render_start", demo_id: did });

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

    // Find first empty audio clip slot
    var slotCount = parseInt(audio.getcount("clip_slots"));
    var slotIdx = -1;
    for (var i = 0; i < slotCount; i++) {
        var s = new LiveAPI(audioPath + " clip_slots " + i);
        if (parseInt(s.get("has_clip")) === 0) { slotIdx = i; break; }
    }
    if (slotIdx < 0) throw new Error("no empty audio clip slot on track " + AUDIO_TRACK_IDX);

    audio.set("arm", 1);

    // Disable session clip-trigger quantization so both clips fire instantly,
    // not on the next bar boundary. (We restore on cleanup.)
    var song = new LiveAPI("live_set");
    try { song.set("clip_trigger_quantization", 0); } catch (e) {}  // 0 = "None"

    var midi = demo.midi || {};
    var len_s = (midi.length_s || demo.duration_s || 4) + TAIL_BUFFER_S;

    currentRender = {
        audioSlotIdx: slotIdx,
        durationS: len_s,
        startedAt: Date.now()
    };

    // Fire both clips simultaneously. The audio slot fires into record because
    // (a) the track is armed and (b) we set Song.record_mode = 1.
    var song = new LiveAPI("live_set");
    song.set("record_mode", 1);
    new LiveAPI("live_set tracks " + MIDI_TRACK_IDX + " clip_slots 0").call("fire");
    new LiveAPI(audioPath + " clip_slots " + slotIdx).call("fire");

    // Schedule stop after duration. Task.schedule takes ms.
    var stopT = new Task(stopResamplingRecord);
    stopT.schedule(len_s * 1000);
}

function stopResamplingRecord() {
    if (!currentRender) return;
    var audioPath = "live_set tracks " + AUDIO_TRACK_IDX;
    var midiPath  = "live_set tracks " + MIDI_TRACK_IDX;

    // Stop global record + both clips
    new LiveAPI("live_set").set("record_mode", 0);
    try { new LiveAPI(midiPath  + " clip_slots 0").call("stop"); } catch (e) {}
    try { new LiveAPI(audioPath + " clip_slots " + currentRender.audioSlotIdx).call("stop"); } catch (e) {}
    new LiveAPI(audioPath).set("arm", 0);

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
        emitEvent({ event: "error", demo_id: did, message: "no recorded clip" });
        cleanupAndNext();
        return;
    }

    var clip = new LiveAPI(slotPath + " clip");
    var src = stringVal(clip.get("file_path"));
    if (!src || src === "0" || src === "") {
        status("recorded clip has no file_path");
        emitEvent({ event: "error", demo_id: did, message: "no file_path" });
        cleanupAndNext();
        return;
    }

    var dest = spec.output_dir + "/" + did + ".wav";
    if (copyFile(src, dest)) {
        status("wrote " + dest);
        emitEvent({ event: "render_done", demo_id: did, path: dest });
    } else {
        status("copy failed: " + src + " → " + dest);
        emitEvent({ event: "error", demo_id: did, message: "copy failed" });
    }

    cleanupAndNext();
}

function cleanupAndNext() {
    var audioPath = "live_set tracks " + AUDIO_TRACK_IDX;
    var midiPath  = "live_set tracks " + MIDI_TRACK_IDX;
    if (currentRender) {
        try { new LiveAPI(audioPath + " clip_slots " + currentRender.audioSlotIdx).call("delete_clip"); } catch (e) {}
    }
    try { new LiveAPI(midiPath + " clip_slots 0").call("delete_clip"); } catch (e) {}
    currentRender = null;
    currentDemo = null;
    var t = new Task(nextRender);
    t.schedule(500);
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
    var len_s = (midi.length_s || demo.duration_s || 4) + TAIL_BUFFER_S;
    var len_beats = secondsToBeats(len_s);
    slot.call("create_clip", len_beats);
    var clip = new LiveAPI(trackPath + " clip_slots 0 clip");
    var pitch = noteNameToMidi(midi.note || "C3");
    var dur_beats = secondsToBeats(midi.length_s || (len_s - TAIL_BUFFER_S));
    var vel = midi.vel || 100;
    clip.call("add_new_notes", JSON.stringify({
        notes: [{ pitch: pitch, start_time: 0, duration: dur_beats, velocity: vel, mute: 0 }]
    }));
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

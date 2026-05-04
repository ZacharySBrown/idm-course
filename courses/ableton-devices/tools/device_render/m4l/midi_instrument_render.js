// midi_instrument_render.js
// ─────────────────────────────────────────────────────────────────────────────
// Classic Max [js] script for the MidiInstrumentRender.amxd device. Generic —
// works for any Live MIDI instrument (Operator, Analog, Wavetable, Meld, Drum
// Rack/Simpler, Granulator). Reads a spec.json produced by device_render.py,
// applies LOM-set parameters per demo onto the instrument, drops a MIDI clip,
// runs the track through `track.freeze()`, then copies the frozen WAV to the
// spec's output_dir under <demo_id>.wav. Emits one NDJSON line per state
// transition into spec.events_path so the Python CLI can tail.
//
// Track layout assumed:
//     [0] MidiInstrumentRender.amxd
//     [1] target instrument
// Edit TARGET_DEV_IDX if your layout differs.
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

var TARGET_DEV_IDX   = 1;     // Target instrument is at device index 1 (0 = this M4L)
var FREEZE_POLL_MS   = 250;   // poll interval for freeze completion
var FREEZE_TIMEOUT_S = 60;    // give up after this many seconds
var TAIL_BUFFER_S    = 0.5;   // extra silence at end of MIDI clip for release

var REPO_ROOT     = "/Users/zak/zacharysbrown/idm-course";
var PARAM_MAP_DIR = "/courses/ableton-devices/tools/device_render/param_maps";

var spec = null;              // parsed spec.json
var paramMap = null;          // loaded from param_maps/<device_class>.json
var renderQueue = [];
var currentDemo = null;
var freezeStartedAt = 0;
var preFreezeFiles = null;

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
        snapshotFreezeDir();
        var track = new LiveAPI("this_device canonical_parent");
        track.call("freeze");
        freezeStartedAt = Date.now();
        var t = new Task(pollFreeze);
        t.interval = FREEZE_POLL_MS;
        t.repeat();
    } catch (e) {
        status("render failed: " + e);
        emitEvent({ event: "error", demo_id: did, message: String(e) });
        currentDemo = null;
        nextRender();
    }
}

function pollFreeze() {
    var track = new LiveAPI("this_device canonical_parent");
    var frozen = parseInt(track.get("freeze_state"));
    var elapsed = (Date.now() - freezeStartedAt) / 1000;

    if (frozen === 2) {
        this.cancel();
        completeFreeze();
    } else if (elapsed > FREEZE_TIMEOUT_S) {
        this.cancel();
        var did = currentDemo ? currentDemo.id : "?";
        status("freeze timed out for " + did);
        emitEvent({ event: "error", demo_id: did, message: "freeze timeout" });
        currentDemo = null;
        nextRender();
    }
}

function completeFreeze() {
    if (!currentDemo) return;
    var did = currentDemo.id;
    var track = new LiveAPI("this_device canonical_parent");

    var newWav = findNewFreezeWav();
    if (!newWav) {
        status("freeze complete but no new WAV found");
        emitEvent({ event: "error", demo_id: did, message: "no freeze wav found" });
        try { track.call("unfreeze"); } catch (e) {}
        currentDemo = null;
        nextRender();
        return;
    }

    var dest = spec.output_dir + "/" + did + ".wav";
    if (copyFile(newWav, dest)) {
        status("wrote " + dest);
        emitEvent({ event: "render_done", demo_id: did, path: dest });
    } else {
        status("copy failed: " + newWav + " → " + dest);
        emitEvent({ event: "error", demo_id: did, message: "copy failed" });
    }

    try { track.call("unfreeze"); } catch (e) {}
    currentDemo = null;
    var t = new Task(nextRender);
    t.schedule(500);
}

function applyParams(params) {
    var devPath = "this_device canonical_parent devices " + TARGET_DEV_IDX;
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
    var n = parseInt(p.getcount("value_items"));
    for (var i = 0; i < n; i++) {
        if (String(p.get("value_items " + i)) === label) return i;
    }
    return null;
}

function ensureMidiClip(demo) {
    var trackPath = "this_device canonical_parent";
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

function snapshotFreezeDir() { preFreezeFiles = listDir(freezeDir()); }

function findNewFreezeWav() {
    var now = listDir(freezeDir());
    var pre = preFreezeFiles || [];
    for (var i = 0; i < now.length; i++) {
        if (pre.indexOf(now[i]) === -1 && /\.wav$/i.test(now[i])) {
            return freezeDir() + "/" + now[i];
        }
    }
    var newest = null, newestT = 0;
    for (var j = 0; j < now.length; j++) {
        if (!/\.wav$/i.test(now[j])) continue;
        var p = freezeDir() + "/" + now[j];
        var f = new File(toMaxPath(p), "read");
        if (!f.isopen) continue;
        var t = f.modified || 0;
        f.close();
        if (t > newestT) { newestT = t; newest = p; }
    }
    return newest;
}

function freezeDir() {
    var setPath = stringVal(new LiveAPI("live_set").get("file_path"));
    var setDir = setPath.replace(/\/[^/]+$/, "");
    return setDir + "/Samples/Processed/Freeze";
}

function listDir(posixPath) {
    var folder = new Folder(toMaxPath(posixPath));
    var names = [];
    while (!folder.end) {
        if (folder.filename) names.push(folder.filename);
        folder.next();
    }
    folder.close();
    return names;
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

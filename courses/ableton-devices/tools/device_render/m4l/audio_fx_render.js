// audio_fx_render.js
// ─────────────────────────────────────────────────────────────────────────────
// Classic Max [js] script for the AudioFxRender.amxd device. Generic — works
// for any Live audio effect (Saturator, Reverb, Spectral devices, racks).
//
// Same shape as midi_instrument_render.js, with two differences:
//   1. The track is an AUDIO track. We do not create a MIDI clip — the user
//      places an audio clip in slot 0 (or arrangement) before triggering.
//   2. The render flow: trigger slot 0 → wait `duration_s` → freeze → copy →
//      stop → unfreeze.
//
// V1: this is a scaffold for ep05+ (warp modes, spectral, racks). Not used by
// e01-operator. The midi_instrument_render variant is the one ep01 needs.
//
// Track layout assumed:
//     [0] AudioFxRender.amxd
//     [1..] target effect chain (any Live audio device or rack)
// Edit TARGET_DEV_IDX if your layout differs.
//
// Inlet messages:
//     load_spec <abs_spec_path>       — load + parse spec.json
//     render                           — render every demo in the spec
//     render_one <demo_id>             — render just one demo
//
// Outlets:
//     0: status / progress messages
//     1: render_done <demo_id>
//     2: error <message>
// ─────────────────────────────────────────────────────────────────────────────

inlets  = 1;
outlets = 3;

var TARGET_DEV_IDX   = 1;
var FREEZE_POLL_MS   = 250;
var FREEZE_TIMEOUT_S = 60;

var REPO_ROOT     = "/Users/zak/zacharysbrown/idm-course";
var PARAM_MAP_DIR = "/courses/ableton-devices/tools/device_render/param_maps";

var spec = null;
var paramMap = null;
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
    if (args.length < 2) { status("load_spec: need spec path"); return; }
    var path = String(args[1]);
    try {
        var f = new File(toMaxPath(path), "read");
        if (!f.isopen) { status("cannot open " + path); return; }
        var raw = "";
        while (f.position < f.eof) raw += f.readstring(4096);
        f.close();
        spec = JSON.parse(raw);
    } catch (e) {
        status("load failed: " + e);
        return;
    }
    status("spec loaded: " + spec.episode_id + " (" + spec.demos.length + " demos)");
    loadParamMap();
}

function loadParamMap() {
    if (!spec) return;
    var slug = (spec.device_class || "").toLowerCase().replace(/[^a-z0-9]+/g, "_");
    if (!slug) return;
    var path = REPO_ROOT + PARAM_MAP_DIR + "/" + slug + ".json";
    try {
        var f = new File(toMaxPath(path), "read");
        if (!f.isopen) { status("paramMap not found: " + path); return; }
        var raw = "";
        while (f.position < f.eof) raw += f.readstring(4096);
        f.close();
        paramMap = JSON.parse(raw);
        status("paramMap loaded: " + paramMap.parameter_count + " params");
    } catch (e) { status("paramMap load failed: " + e); }
}

function render() {
    if (!spec) { status("no spec loaded"); return; }
    renderQueue = spec.demos.map(function(d) { return d.id; });
    nextRender();
}

function render_one() {
    if (!spec) { status("no spec loaded"); return; }
    var args = arrayfromargs(messagename, arguments);
    if (args.length < 2) { status("render_one: need demo id"); return; }
    renderQueue = [String(args[1])];
    nextRender();
}

function nextRender() {
    if (renderQueue.length === 0) { status("queue empty"); return; }
    var did = renderQueue.shift();
    var demo = findDemo(did);
    if (!demo) { nextRender(); return; }

    currentDemo = demo;
    status("rendering " + did);
    emitEvent({ event: "render_start", demo_id: did });

    if (!demo.params) {
        emitEvent({ event: "render_skipped", demo_id: did, reason: "no params block" });
        currentDemo = null;
        nextRender();
        return;
    }

    try {
        applyParams(demo.params);
        snapshotFreezeDir();

        // Trigger clip slot 0 (audio source) and freeze
        var trackPath = "this_device canonical_parent";
        var slot = new LiveAPI(trackPath + " clip_slots 0");
        if (parseInt(slot.get("has_clip")) !== 1) {
            throw new Error("audio clip slot 0 is empty — drop a source clip first");
        }
        slot.call("fire");

        var track = new LiveAPI(trackPath);
        track.call("freeze");
        freezeStartedAt = Date.now();
        var t = new Task(pollFreeze);
        t.interval = FREEZE_POLL_MS;
        t.repeat();
    } catch (e) {
        status("render failed: " + e);
        emitEvent({ event: "error", demo_id: currentDemo.id, message: String(e) });
        currentDemo = null;
        nextRender();
    }
}

function pollFreeze() {
    var track = new LiveAPI("this_device canonical_parent");
    var frozen = parseInt(track.get("freeze_state"));
    var elapsed = (Date.now() - freezeStartedAt) / 1000;
    if (frozen === 2) { this.cancel(); completeFreeze(); }
    else if (elapsed > FREEZE_TIMEOUT_S) {
        this.cancel();
        emitEvent({ event: "error", demo_id: currentDemo ? currentDemo.id : "?", message: "freeze timeout" });
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
        emitEvent({ event: "error", demo_id: did, message: "no freeze wav found" });
        try { track.call("unfreeze"); } catch (e) {}
        currentDemo = null;
        nextRender();
        return;
    }
    var dest = spec.output_dir + "/" + did + ".wav";
    if (copyFile(newWav, dest)) {
        emitEvent({ event: "render_done", demo_id: did, path: dest });
    } else {
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
    if (!device || device.id === "0") throw new Error("no device at index " + TARGET_DEV_IDX);
    for (var name in params) {
        if (!params.hasOwnProperty(name)) continue;
        var idx = lookupParamIndex(name);
        if (idx === null) { status("unknown param: " + name); continue; }
        var p = new LiveAPI(devPath + " parameters " + idx);
        var v = params[name];
        if (typeof v === "string" && p.getcount("value_items") > 0) {
            v = enumValueIndex(p, v);
            if (v === null) continue;
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

function snapshotFreezeDir() { preFreezeFiles = listDir(freezeDir()); }

function findNewFreezeWav() {
    var now = listDir(freezeDir());
    var pre = preFreezeFiles || [];
    for (var i = 0; i < now.length; i++) {
        if (pre.indexOf(now[i]) === -1 && /\.wav$/i.test(now[i])) {
            return freezeDir() + "/" + now[i];
        }
    }
    return null;
}

function freezeDir() {
    var setPath = stringVal(new LiveAPI("live_set").get("file_path"));
    return setPath.replace(/\/[^/]+$/, "") + "/Samples/Processed/Freeze";
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
        while (src.position < src.eof) dst.writebytes(src.readbytes(65536));
        src.close();
        dst.close();
        return true;
    } catch (e) { return false; }
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

// operator_render_probe.js
// ─────────────────────────────────────────────────────────────────────────────
// One-shot LOM parameter dump. Drop into a [js operator_render_probe.js] box
// in a Max for Live device on a track that has Operator (or any device) at a
// known device index. Send `dump <track_idx> <device_idx>` to the inlet — gets
// every parameter name + index + min/max/value from that device, plus any
// nested chain devices, and writes the result to:
//
//     <repo_root>/courses/ableton-devices/tools/operator_render/lom_param_map.json
//
// (The repo root is hardcoded below — edit if your checkout lives elsewhere.)
//
// Usage from Max:
//     [dump 0 0]    → walk track 0, device 0 (assumes Operator is at device 0)
//     [dump]        → defaults to (selected_track, device 0)
//
// Outlets:
//     0: status messages
//     1: complete: <count> when finished
// ─────────────────────────────────────────────────────────────────────────────

inlets  = 1;
outlets = 2;

// EDIT if your repo lives elsewhere. POSIX path; toMaxPath() converts.
var REPO_ROOT = "/Users/zak/zacharysbrown/idm-course";
var OUT_REL   = "/courses/ableton-devices/tools/operator_render/lom_param_map.json";

function status(msg) {
    outlet(0, "status", String(msg));
    post(msg + "\n");
}

function dump() {
    var args = arrayfromargs(messagename, arguments);
    var trackIdx = args.length > 1 ? parseInt(args[1]) : null;
    var deviceIdx = args.length > 2 ? parseInt(args[2]) : 0;

    var trackPath;
    if (trackIdx === null || isNaN(trackIdx)) {
        trackPath = "live_set view selected_track";
    } else {
        trackPath = "live_set tracks " + trackIdx;
    }

    var track = new LiveAPI(trackPath);
    if (!track || track.id === "0") {
        status("track not found at " + trackPath);
        return;
    }

    var devCount = parseInt(track.getcount("devices"));
    if (deviceIdx >= devCount) {
        status("track has " + devCount + " devices; index " + deviceIdx + " out of range");
        return;
    }

    var devicePath = trackPath + " devices " + deviceIdx;
    var device = new LiveAPI(devicePath);
    if (!device || device.id === "0") {
        status("device not found at " + devicePath);
        return;
    }

    var deviceName = stringVal(device.get("name"));
    var deviceClass = stringVal(device.get("class_name"));
    status("dumping device " + deviceIdx + ": " + deviceName + " [" + deviceClass + "]");

    var paramCount = parseInt(device.getcount("parameters"));
    var params = [];
    for (var i = 0; i < paramCount; i++) {
        var p = new LiveAPI(devicePath + " parameters " + i);
        if (!p || p.id === "0") continue;
        try {
            params.push({
                index: i,
                name: stringVal(p.get("name")),
                original_name: stringVal(p.get("original_name")),
                value: parseFloat(p.get("value")),
                min: parseFloat(p.get("min")),
                max: parseFloat(p.get("max")),
                is_quantized: parseInt(p.get("is_quantized")) === 1,
                value_items: getValueItems(p)
            });
        } catch (e) {
            params.push({ index: i, error: String(e) });
        }
    }

    var result = {
        captured_at: Date.now(),
        track_path: trackPath,
        device_path: devicePath,
        device_name: deviceName,
        device_class: deviceClass,
        parameter_count: paramCount,
        parameters: params
    };

    var outPath = REPO_ROOT + OUT_REL;
    if (writeJson(outPath, result)) {
        status("wrote " + paramCount + " params → " + outPath);
        outlet(1, "complete", paramCount);
    } else {
        status("write failed: " + outPath);
    }
}

function getValueItems(p) {
    // Quantized params (enum-like, e.g. Algorithm, Wave) expose enumerated
    // string values via `value_items`. Continuous params don't.
    try {
        var n = parseInt(p.getcount("value_items"));
        if (!n || isNaN(n)) return null;
        var items = [];
        for (var i = 0; i < n; i++) {
            var v = p.get("value_items " + i);
            items.push(stringVal(v));
        }
        return items;
    } catch (e) {
        return null;
    }
}

function stringVal(v) {
    if (v && typeof v === "object" && v.length !== undefined) v = v[0];
    return String(v);
}

function writeJson(posixPath, obj) {
    var maxPath = toMaxPath(posixPath);
    var f = new File(maxPath, "write");
    if (!f.isopen) return false;
    try {
        f.writestring(JSON.stringify(obj, null, 2));
        f.close();
        return true;
    } catch (e) {
        try { f.close(); } catch (_e) {}
        return false;
    }
}

function toMaxPath(posixPath) {
    var p = String(posixPath);
    if (p.indexOf("/") === 0) return "Macintosh HD:" + p;
    return p;
}

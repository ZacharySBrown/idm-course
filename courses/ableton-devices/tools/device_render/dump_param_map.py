#!/usr/bin/env python3
"""Dump a device's parameter map (name→index, ranges, enum value_items) over
AbletonOSC into param_maps/<device>.json, matching the analog.json/operator.json
schema. Usage: dump_param_map.py --track 2 --device-index 0 --out param_maps/wavetable.json
"""
import argparse, json, queue, threading, time
from datetime import datetime, timezone
from pathlib import Path
from pythonosc.udp_client import SimpleUDPClient
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer

HERE = Path(__file__).resolve().parent


class Live:
    def __init__(self, send=11000, reply=11001, host="127.0.0.1", timeout=4.0):
        self.timeout = timeout
        self._q: queue.Queue = queue.Queue()
        disp = Dispatcher(); disp.set_default_handler(lambda a, *x: self._q.put((a, x)))
        self._srv = BlockingOSCUDPServer((host, reply), disp)
        threading.Thread(target=self._srv.serve_forever, daemon=True).start()
        self._cli = SimpleUDPClient(host, send)

    def ask(self, addr, *args, want=None):
        while not self._q.empty(): self._q.get_nowait()
        self._cli.send_message(addr, list(args))
        t0 = time.time()
        while time.time() - t0 < self.timeout:
            try:
                a, x = self._q.get(timeout=self.timeout)
            except queue.Empty:
                return None
            if want is None or a == want:
                return x
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--track", type=int, required=True)
    ap.add_argument("--device-index", type=int, default=0)
    ap.add_argument("--out", required=True)
    ap.add_argument("--vi-timeout", type=float, default=0.6, help="per-param value_items wait")
    args = ap.parse_args()
    L = Live()
    t, dv = args.track, args.device_index
    name = L.ask("/live/device/get/name", t, dv, want="/live/device/get/name")
    cls = L.ask("/live/device/get/class_name", t, dv, want="/live/device/get/class_name")
    names = L.ask("/live/device/get/parameters/name", t, dv, want="/live/device/get/parameters/name")
    mins = L.ask("/live/device/get/parameters/min", t, dv, want="/live/device/get/parameters/min")
    maxs = L.ask("/live/device/get/parameters/max", t, dv, want="/live/device/get/parameters/max")
    vals = L.ask("/live/device/get/parameters/value", t, dv, want="/live/device/get/parameters/value")
    quant = L.ask("/live/device/get/parameters/is_quantized", t, dv, want="/live/device/get/parameters/is_quantized")
    # strip the (track, device) prefix from each bulk reply
    def body(r): return list(r[2:]) if r and len(r) > 2 else []
    pnames, pmin, pmax, pval, pq = body(names), body(mins), body(maxs), body(vals), body(quant)
    n = len(pnames)
    params = []
    for i in range(n):
        is_q = bool(int(pq[i])) if i < len(pq) else False
        p = {"index": i, "name": str(pnames[i]),
             "value": float(pval[i]) if i < len(pval) else 0.0,
             "min": float(pmin[i]) if i < len(pmin) else 0.0,
             "max": float(pmax[i]) if i < len(pmax) else 1.0,
             "is_quantized": is_q}
        if is_q:
            _saved = L.timeout; L.timeout = args.vi_timeout
            vi = L.ask("/live/device/get/parameter/value_items", t, dv, i,
                       want="/live/device/get/parameter/value_items")
            L.timeout = _saved
            items = [str(x) for x in (vi[3:] if vi and len(vi) > 3 else [])]
            p["value_items"] = items
        params.append(p)
    out = {"captured_at": datetime.now(timezone.utc).isoformat(),
           "device_name": str(name[2]) if name and len(name) > 2 else "?",
           "device_class": str(cls[2]) if cls and len(cls) > 2 else "?",
           "track_path": f"track {t} device {dv}",
           "parameter_count": n, "parameters": params}
    Path(args.out).write_text(json.dumps(out, indent=2))
    print(f"dumped {n} params for {out['device_name']!r} ({out['device_class']}) -> {args.out}")


if __name__ == "__main__":
    main()

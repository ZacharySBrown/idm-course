#!/usr/bin/env python3
"""
verify_demo.py — Gate 7 "demonstration-verification": prove a rendered demo
actually DEMONSTRATES its concept, not just that it isn't silent.

A demo that fails its assertion is rejected and sent back for redesign. This is
the check that would have caught ep1's `op-rhythmic-single == op-rhythmic-instance2`
(identical audio) and the section-5 "plucks" that were 40 ms clicks.

Each concept maps to a machine-checkable assertion:

  index-sweep   loudness ~flat AND spectral centroid rises monotonically
  harmonic      partials land on an integer comb of f0 (pitched)
  inharmonic    partials do NOT (bell/metallic) — comb score below a floor
  feedback-sweep spectral spread/centroid grows over the clip
  rhythmic      onset rate ≈ a target events/sec (grid-locked, not a drone)
  louder-brighter  the second half has more high-band energy than the first
                   (velocity→depth: soft then hard)
  distinct      two clips have meaningfully different onset rate / spectrum
                (used for layered polyrhythm: the two layers aren't the same)

Usage:
  verify_demo.py --clip a.wav --check index-sweep
  verify_demo.py --clip a.wav --check rhythmic --target-rate 8 --tol 0.4
  verify_demo.py --clip a.wav --check harmonic
  verify_demo.py --a one.wav --b two.wav --check distinct
  verify_demo.py --manifest clip_manifest.yaml --clips-dir <dir>   # batch from `verification:` specs
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np

try:
    import soundfile as sf
    import librosa
except ImportError:
    sys.stderr.write("need numpy, soundfile, librosa (uv pip install librosa soundfile)\n")
    sys.exit(2)


def load(path: str) -> tuple[np.ndarray, int]:
    x, sr = sf.read(path)
    if x.ndim > 1:
        x = x.mean(axis=1)
    return x.astype(np.float64), sr


def _active(x: np.ndarray, sr: int, thr_db: float = -45.0) -> np.ndarray:
    """Trim leading/trailing silence so trends reflect the actual sound."""
    env = np.abs(x)
    pk = env.max() or 1.0
    thr = pk * (10 ** (thr_db / 20))
    nz = np.where(env > thr)[0]
    if len(nz) == 0:
        return x
    return x[nz[0]: nz[-1] + 1]


def centroid_trend(x, sr) -> dict:
    c = librosa.feature.spectral_centroid(y=x, sr=sr)[0]
    if len(c) < 4:
        return {"start": float(c.mean()), "end": float(c.mean()), "ratio": 1.0, "monotonic_frac": 0.0}
    n = max(1, len(c) // 5)
    start = float(np.median(c[:n])); end = float(np.median(c[-n:]))
    # fraction of frames where centroid is non-decreasing (smoothed)
    cs = np.convolve(c, np.ones(5) / 5, mode="valid")
    mono = float(np.mean(np.diff(cs) >= -1e-6))
    return {"start": start, "end": end, "ratio": end / max(start, 1e-9), "monotonic_frac": mono}


def rms_flatness(x, sr) -> float:
    """1.0 = perfectly flat loudness; lower = collapsing (a pluck dying)."""
    r = librosa.feature.rms(y=x)[0]
    r = r[r > r.max() * 0.05] if r.max() > 0 else r
    if len(r) < 4:
        return 1.0
    return float(1.0 - min(1.0, np.std(r) / (np.mean(r) + 1e-9)))


def harmonic_comb_score(x, sr) -> dict:
    """Fraction of partial-band energy that sits on an integer comb of f0.
    High → harmonic/pitched; low → inharmonic/bell."""
    seg = _active(x, sr)
    # average magnitude spectrum over the sustained region
    S = np.abs(librosa.stft(seg, n_fft=8192))
    mag = S.mean(axis=1)
    freqs = librosa.fft_frequencies(sr=sr, n_fft=8192)
    # estimate f0 via yin on the active region
    try:
        f0 = librosa.yin(seg, fmin=50, fmax=1000, sr=sr)
        f0 = float(np.median(f0[np.isfinite(f0)]))
    except Exception:
        f0 = 0.0
    if not (50 <= f0 <= 1000):
        # fallback: strongest peak below 1k
        lowband = (freqs > 50) & (freqs < 1000)
        f0 = float(freqs[lowband][np.argmax(mag[lowband])]) if lowband.any() else 130.0
    band = (freqs > 40) & (freqs < 8000)
    total = float(mag[band].sum()) + 1e-9
    tol = f0 * 0.06  # ±6% window around each harmonic
    comb = 0.0
    for n in range(1, 40):
        fc = f0 * n
        if fc > 8000:
            break
        w = (freqs > fc - tol) & (freqs < fc + tol)
        comb += float(mag[w].sum())
    return {"f0": f0, "comb_score": comb / total}


def onset_rate(x, sr) -> dict:
    seg = _active(x, sr)
    on = librosa.onset.onset_detect(y=seg, sr=sr, units="time", backtrack=False)
    dur = len(seg) / sr
    return {"onsets": int(len(on)), "dur_s": dur, "rate": (len(on) / dur if dur else 0.0)}


def high_band_ratio(x, sr, split: float = 0.5, cutoff_hz: float = 1500) -> dict:
    """Compare high-frequency energy in first vs second portion (velocity→depth)."""
    seg = _active(x, sr)
    mid = int(len(seg) * split)
    def hb(a):
        S = np.abs(librosa.stft(a, n_fft=4096))
        freqs = librosa.fft_frequencies(sr=sr, n_fft=4096)
        hi = S[freqs > cutoff_hz].sum(); lo = S.sum() + 1e-9
        return float(hi / lo)
    a, b = hb(seg[:mid]), hb(seg[mid:])
    return {"first_hf": a, "second_hf": b, "delta": b - a}


# ── checks: return (passed, detail) ──────────────────────────────────────────
def check(kind: str, clip: str, b: str | None = None, **kw):
    x, sr = load(clip)
    seg = _active(x, sr)
    peak_db = 20 * np.log10(np.abs(x).max() + 1e-12)

    if kind == "index-sweep":
        ct = centroid_trend(seg, sr); fl = rms_flatness(seg, sr)
        ok = ct["ratio"] >= 1.3 and ct["monotonic_frac"] >= 0.6 and fl >= 0.5
        return ok, {"centroid": ct, "rms_flatness": round(fl, 3),
                    "why": "centroid must rise ≥1.3x monotonically while loudness stays flat"}

    if kind in ("harmonic", "inharmonic"):
        h = harmonic_comb_score(seg, sr)
        if kind == "harmonic":
            ok = h["comb_score"] >= 0.55
            why = "≥55% of partial energy on the integer comb (pitched)"
        else:
            ok = h["comb_score"] <= 0.45
            why = "≤45% of partial energy on the integer comb (inharmonic/bell)"
        return ok, {**h, "why": why}

    if kind == "feedback-sweep":
        ct = centroid_trend(seg, sr)
        ok = ct["ratio"] >= 1.4 and ct["monotonic_frac"] >= 0.55
        return ok, {"centroid": ct, "why": "spectral centroid must grow across the clip"}

    if kind == "rhythmic":
        o = onset_rate(seg, sr)
        target = kw.get("target_rate"); tol = kw.get("tol", 0.5)
        if target:
            ok = abs(o["rate"] - target) <= target * tol and o["onsets"] >= 4
            why = f"onset rate {o['rate']:.1f}/s within ±{int(tol*100)}% of {target}/s"
        else:
            ok = o["rate"] >= 2.0 and o["onsets"] >= 4
            why = "rhythmic: ≥2 onsets/s (not a drone)"
        return ok, {**o, "why": why}

    if kind == "louder-brighter":
        hb = high_band_ratio(seg, sr)
        ok = hb["delta"] > 0.02
        return ok, {**hb, "why": "second (hard) segment must be brighter than the first (soft)"}

    if kind == "distinct":
        if not b:
            return False, {"why": "distinct needs --a and --b"}
        xb, srb = load(b)
        ra = onset_rate(seg, sr)["rate"]; rb = onset_rate(_active(xb, srb), srb)["rate"]
        # different rhythm OR different spectral centroid
        ca = centroid_trend(seg, sr)["start"]; cb = centroid_trend(_active(xb, srb), srb)["start"]
        rate_diff = abs(ra - rb) / (max(ra, rb) + 1e-9)
        cen_diff = abs(ca - cb) / (max(ca, cb) + 1e-9)
        ok = rate_diff >= 0.25 or cen_diff >= 0.2
        return ok, {"rate_a": ra, "rate_b": rb, "rate_diff": round(rate_diff, 3),
                    "cen_diff": round(cen_diff, 3), "why": "clips must differ in rhythm or timbre"}

    if kind == "audible":
        ok = peak_db >= -22
        return ok, {"peak_db": round(float(peak_db), 1), "why": "peak ≥ -22 dB"}

    return False, {"why": f"unknown check {kind!r}"}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--clip")
    ap.add_argument("--a"); ap.add_argument("--b")
    ap.add_argument("--check", required=False)
    ap.add_argument("--target-rate", type=float)
    ap.add_argument("--tol", type=float, default=0.5)
    ap.add_argument("--manifest"); ap.add_argument("--clips-dir")
    args = ap.parse_args()

    if args.manifest:
        import yaml
        man = yaml.safe_load(Path(args.manifest).read_text())
        clips = Path(args.clips_dir)
        results = []
        for d in man.get("operator_demos", []) or []:
            v = d.get("verification") or {}
            kind = v.get("check")
            if not kind:
                continue
            cand = None
            for ext in (".wav", ".aif", ".aiff"):
                p = clips / f"{d['id']}{ext}"
                if p.exists():
                    cand = p; break
            if not cand:
                results.append({"id": d["id"], "status": "missing"}); continue
            ok, detail = check(kind, str(cand), b=(str(clips / f"{v['vs']}.wav") if v.get("vs") else None),
                               target_rate=v.get("target_rate"), tol=v.get("tol", 0.5))
            results.append({"id": d["id"], "check": kind, "pass": ok, **detail})
        n_ok = sum(1 for r in results if r.get("pass"))
        print(json.dumps(results, indent=2))
        print(f"\nverify_demo: {n_ok}/{sum(1 for r in results if 'pass' in r)} passed", file=sys.stderr)
        return 0 if all(r.get("pass", r.get("status") == "missing") for r in results) else 1

    clip = args.clip or args.a
    ok, detail = check(args.check, clip, b=args.b, target_rate=args.target_rate, tol=args.tol)
    print(json.dumps({"clip": clip, "check": args.check, "pass": ok, **detail}, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

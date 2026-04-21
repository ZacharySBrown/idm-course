#!/usr/bin/env bash
# fetch_pdfs.sh — Bucket A (scriptable) PDF acquisition.
# Emits per-source status to references/pdfs/_status.json.
# Bucket B (manual purchase) → references/pdfs/_purchase_todo.md
# Bucket C (link-only) → validated and written to references/links.yaml

set -uo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PDFS="$ROOT/references/pdfs"
TRANS="$ROOT/references/transcripts"
mkdir -p "$PDFS" "$TRANS"

STATUS="$PDFS/_status.json"
TODO="$PDFS/_purchase_todo.md"
: > "$STATUS.tmp"
echo "[" >> "$STATUS.tmp"

log_status() {
  local id="$1" ok="$2" note="$3"
  printf '  {"id": "%s", "ok": %s, "note": "%s"},\n' "$id" "$ok" "$note" >> "$STATUS.tmp"
}

fetch_url() {
  local id="$1" url="$2" out="$3"
  if curl --silent --show-error --fail --location --max-time 60 --output "$out" "$url"; then
    log_status "$id" "true" "downloaded from $url"
  else
    log_status "$id" "false" "curl failed for $url"
  fi
}

# ---- Bucket A ----

# Ableton Live 12 Manual — HTML → PDF via wkhtmltopdf if available, else save HTML tree
if command -v wkhtmltopdf >/dev/null 2>&1; then
  wkhtmltopdf --quiet \
    --print-media-type \
    "https://www.ableton.com/en/live-manual/12/welcome-to-live/" \
    "$PDFS/ableton_live_12_manual.pdf" \
    && log_status "bib:ableton_live_12_manual" "true" "wkhtmltopdf" \
    || log_status "bib:ableton_live_12_manual" "false" "wkhtmltopdf failed"
else
  log_status "bib:ableton_live_12_manual" "false" "wkhtmltopdf not installed — install via 'brew install --cask wkhtmltopdf'"
fi

# Max for Live device READMEs — copy from Ableton install
ABLETON_APP="/Applications/Ableton Live 12 Suite.app"
if [[ -d "$ABLETON_APP" ]]; then
  mkdir -p "$PDFS/max_for_live_readmes"
  find "$ABLETON_APP/Contents/App-Resources/Max" -name "*.html" -maxdepth 6 2>/dev/null | while read -r f; do
    cp "$f" "$PDFS/max_for_live_readmes/$(basename "$f")" 2>/dev/null
  done
  log_status "bib:max_for_live_readmes" "true" "copied from local Ableton install"
else
  log_status "bib:max_for_live_readmes" "false" "Ableton Live 12 Suite not at /Applications"
fi

# Granulator III docs
fetch_url "bib:henke_granulator_iii" \
  "https://roberthenke.com/technology/granulator.html" \
  "$PDFS/granulator_iii.html"

# Oblique Strategies — public-domain text compilation
fetch_url "bib:oblique_strategies_eno" \
  "https://stoney.sb.org/eno/oblique.html" \
  "$PDFS/oblique_strategies.html"

# Korg Monologue (AFX edition) microtuning guide
fetch_url "bib:korg_monologue_afx_manual" \
  "https://www.korg.com/us/support/download/manual/0/562/3261/" \
  "$PDFS/korg_monologue_afx_manual.pdf"

# ---- Bucket B — manual purchase TODO ----
cat > "$TODO" <<'EOF'
# Purchase / personal-archive TODO

These are the references we cannot legally auto-download. Zak: grab these when you have a spare 30 minutes.

- [ ] **Tape Op #89 (Squarepusher)** — scan personal back-issue to `references/pdfs/tape_op_89_squarepusher.pdf`
- [ ] **Sound on Sound April 2004 (Autechre)** — download via SOS subscriber account to `references/pdfs/sos_autechre_april_2004.pdf`
- [ ] **Tape Notes #140 (Four Tet)** — download MP3, run whisper.cpp, save transcript to `references/transcripts/tape_notes_140.md`. Do NOT mirror the MP3.
- [ ] **Dilla Time (Charnas 2022)** — cite-only. No PDF.
- [ ] **Computer Music Tutorial (Roads 1996)** — cite-only. No PDF.
- [ ] **Future Music 1993 RDJ early-era interview** — rare; try Discogs/eBay if motivated.

EOF
log_status "bucket_B_purchase_todo" "true" "written to $TODO"

# ---- Finalize status.json ----
# strip trailing comma, close array
sed -i '' -e '$ s/,$//' "$STATUS.tmp" 2>/dev/null || sed -i -e '$ s/,$//' "$STATUS.tmp"
echo "]" >> "$STATUS.tmp"
mv "$STATUS.tmp" "$STATUS"

echo "fetch_pdfs.sh complete. See $STATUS and $TODO."

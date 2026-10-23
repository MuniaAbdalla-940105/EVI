#!/usr/bin/env bash
# Export Markdown documents to print-ready PDFs for factories and partners.
# Usage: scripts/export_pdf.sh <output-dir> <file.md> [file.md ...]
# Needs pandoc and Chrome/Chromium. Output goes to exports/ (git-ignored).
set -euo pipefail

if [ $# -lt 2 ]; then
  echo "Usage: $0 <output-dir> <file.md> [file.md ...]" >&2
  exit 1
fi

out_dir=$1
shift
mkdir -p "$out_dir"

browser=${CHROME:-}
if [ -z "$browser" ]; then
  for candidate in chromium chromium-browser google-chrome google-chrome-stable \
    /opt/pw-browsers/chromium/chrome-linux*/chrome /opt/pw-browsers/chromium-*/chrome-linux*/chrome \
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"; do
    if command -v "$candidate" > /dev/null 2>&1 || [ -x "$candidate" ]; then
      browser=$candidate
      break
    fi
  done
fi
if [ -z "$browser" ]; then
  echo "Chrome or Chromium not found. Set CHROME=/path/to/chrome." >&2
  exit 1
fi

css=$(mktemp --suffix=.css)
trap 'rm -f "$css"' EXIT
cat > "$css" <<'EOF'
@page { size: A4; margin: 15mm; }
body { font-family: Arial, Helvetica, sans-serif; font-size: 10pt; color: #000; max-width: none; }
h1 { font-size: 16pt; } h2 { font-size: 13pt; margin-top: 1.4em; } h3 { font-size: 11pt; }
table { border-collapse: collapse; width: 100%; margin: 0.6em 0; page-break-inside: auto; }
th, td { border: 1px solid #444; padding: 3px 5px; text-align: left; vertical-align: top; }
th { background: #eee; }
tr { page-break-inside: avoid; }
EOF

for md in "$@"; do
  name=$(basename "${md%.md}")
  html="$out_dir/$name.html"
  pandoc "$md" --from markdown+yaml_metadata_block --standalone --embed-resources \
    --resource-path "$(dirname "$md")" --css "$css" --metadata pagetitle="$name" -o "$html"
  "$browser" --headless --disable-gpu --no-sandbox --no-pdf-header-footer \
    --print-to-pdf="$out_dir/$name.pdf" "file://$(realpath "$html")" 2> /dev/null
  rm -f "$html"
  echo "$out_dir/$name.pdf"
done

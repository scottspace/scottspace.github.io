# Industry AI Report — 1Q26 · Source Bundle

This folder is the reproducible source for the PDF published at
[`/insights/industry_1q26.pdf`](../../industry_1q26.pdf).

It exists so the report can be re-rendered, amended, or audited without
losing the original inputs and layout.

## Contents

| File | Purpose |
|---|---|
| `report.html` | The hand-authored HTML that renders to the PDF. Viewable standalone in a browser. |
| `source.md` | The raw strategic analysis that seeded the report. |
| `images/` | Seven 16:9 images embedded in the PDF. One cover plus one per industry pillar. |

## About the Report

A quarterly personal research project by Scott Penberthy. The analysis
correlates risk-adjusted public-market performance with the AI application
portfolios of 4,198 companies. Each application is classified by business
focus (Run, Build, Grow) and by occupation using the U.S. Standard
Occupational Classification (SOC). The goal is to isolate the AI behaviors
the market is actively rewarding.

See the PDF itself for methodology, scope, and the full disclaimer.

## Regenerating the PDF

From the openclaw workspace:

```bash
cd agents/main/insights/pdf
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new --disable-gpu --no-pdf-header-footer \
  --print-to-pdf=../INDUSTRY_AI_REPORT_1Q26.pdf \
  "file://$(pwd)/report.html"
```

## How the Images Were Made

Each image was generated with fal.ai Nano Banana Pro through a small shell
wrapper called `nb`. The wrapper lives at `~/bin/nb` and polls the fal.ai
queue until the image is ready. Images were downsampled to 1600px and
encoded as JPEG at quality 88 to keep the PDF near 4.5 MB.

## Disclaimer

These are the author's personal observations. They do not represent the
views of his employer or any advisory boards he serves on. The report is
not investing advice.

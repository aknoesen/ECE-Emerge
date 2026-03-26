# TikZ/CircuitiKZ Figure Extraction — Report

**Date:** 2026-03-25
**Script:** `extract_tikz_figures.py` (maintained in this folder)

---

## What Was Done

A Python script was written to automate the extraction of TikZ and CircuitiKZ
figures from LaTeX lab manuals and render them as high-resolution PNG images
(1200 dpi) for use in ADA-compliant Markdown web pages.

**Pipeline per figure:**
1. Regex-parse `\begin{figure}...\end{figure}` blocks in the source `.tex` file
2. Skip figures that only contain `\includegraphics` (already image files)
3. Strip `\savebox` / `\pdftooltip` wrappers; extract the inner `circuitikz` or
   `tikzpicture` environment
4. Build a `\documentclass[border=8pt]{standalone}` LaTeX document with a fixed
   preamble (tikz, circuitikz, pgfplots, amsmath, xcolor) plus any `\definecolor`
   definitions from the source file
5. Compile with `pdflatex`
6. Convert to PNG with `pdftoppm -r 1200 -png`
7. Name output files from the figure's `\label` (with `fig:` prefix stripped)

---

## Results by Lab

| Lab | Source file | Figures found | Rendered | Output folder |
|-----|-------------|:---:|:---:|---------------|
| Lab 1 | `Labs/Lab 1/Lab1Instructions.tex` | 2 | 2 | `Lab1/media/` |
| Lab 2 | `Labs/Lab 2/Lab2Instructions.tex` | 6 | 6 | `Lab2/media/` |
| Lab 3 | `Labs/Lab 3/Lab3Instructions.tex` | 7 | 7 | `Lab3/media/` |
| Lab 4 | `Labs/Lab 4/Lab4Instructions.tex` | 7 | 7 | `Lab4/media/` |
| Lab 5 | `Labs/Lab 5/Lab5Instructions.tex` | 3 | 3 | `Lab5/media/` |
| Lab 6 | `Labs/Lab 6 & 7 .../Lab6Instructions.tex` | 5 | 5 | `Lab6/media/` |
| Lab 7 | `Labs/Lab 6 & 7 .../Lab7Instructions.tex` | 3 | 3 | `Lab7/media/` |
| Lab 8 | `Project/Lab8Instructions.tex` | 1 | 1 | `Lab8/media/` |

**Total: 34 figures extracted, 34 rendered successfully.**

One script fix was required mid-run: Labs 3–8 use `pgfplots` (`\begin{axis}`)
for IV-characteristic and spectrum plots, which was not in the initial preamble.
`\usepackage{pgfplots}` and `\pgfplotsset{compat=1.18}` were added; all
subsequent runs succeeded.

---

## Issues to Attend To

### 1. Lab 4 — Duplicate `\label{fig:rl-setup}` (ACTION REQUIRED)

Two distinct figures in `Lab4Instructions.tex` share the same label:

- Figure 2: *"RL circuit experimental setup. The generator internal resistance..."*
- Figure 7: *"RL circuit experimental setup. The generator has an internal..."*

Both map to `rl-setup-1.png`. The **second figure silently overwrote the first**
during extraction. One of these labels must be made unique in the source `.tex`
(e.g., change one to `fig:rl-setup2`), then re-run the script for Lab 4.

---

### 2. Lab 5 — Unlabelled figure inside `subfigure` environment (VERIFY OUTPUT)

The first figure in `Lab5Instructions.tex` uses `\begin{subfigure}` internally.
The script found a tikz environment inside it and saved it as `fig_01-1.png`,
but the extracted caption was garbled:

> `Circuit~1} \end{subfigure} \hfill \begin{subfigure}{0.4\text…`

This indicates the figure contains multiple subfigures and only the first
TikZ environment was extracted. **Please check `fig_01-1.png`** to confirm it
looks correct. If the subfigure layout is important (e.g., side-by-side
circuits), the script would need an extension to handle `subfigure` environments
— or the subfigures can be manually split into separate `figure` environments
with individual `\label` tags in the source.

---

### 3. Lab 2 — Label with embedded `.png` extension (MINOR / COSMETIC)

One figure in `Lab2Instructions.tex` has the label `fig:Lab3Fig1.png` — the
`.png` is part of the label string. The script sanitised this to
`Lab3Fig1_png-1.png`. The figure itself rendered correctly, but the filename
is slightly awkward. Consider renaming the label in the source to
`fig:Lab3Fig1` and re-running.

---

### 4. Stale script copy in `Labs/Lab 2/` (HOUSEKEEPING)

A copy of the script was originally developed in
`Labs/Lab 2/extract_tikz_figures.py`. It was kept in sync through Lab 4 but
the agreed canonical location is this folder (`Lab Manuals/`). The copy in
`Labs/Lab 2/` can be deleted to avoid future confusion.

---

## Script Reference

**Location:** `Lab Manuals/extract_tikz_figures.py`
**Usage notes:** `Lab Manuals/extract_tikz_figures_usage.txt`

To re-run any lab after fixing source `.tex` issues:

```
python "C:\...\Lab Manuals\extract_tikz_figures.py" ^
  "C:\...\Labs\Lab N\LabNInstructions.tex" ^
  "C:\...\Lab Manuals\LabN\media"
```

To add support for a new LaTeX package (e.g., if a future lab introduces one),
add `\usepackage{...}` to `STANDALONE_PREAMBLE` near the top of the script.

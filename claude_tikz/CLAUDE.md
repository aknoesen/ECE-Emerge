# Claude Context — TikZ Figure Extraction Workflow

## What This Is

A Python script (`extract_tikz_figures.py`) that extracts TikZ/CircuitiKZ
figures from the EEC1 Spring 2026 LaTeX lab manuals and renders them as
high-resolution PNGs for use in ADA-compliant Markdown web pages.

## Script Location

```
C:\Users\aknoesen\Documents\Knoesen\EEC1 Spring 2026\
  ADA Compliant Webpage Materials\Lab Manuals\
    extract_tikz_figures.py       ← canonical copy (only copy to maintain)
    extract_tikz_figures_usage.txt
```

There is a stale copy at `Labs\Lab 2\extract_tikz_figures.py` — ignore it.

## What the Script Produces Per Run

Given `<input.tex>` and `<output_dir>` (the lab's `media/` folder):

1. **`LabN/media/<label>-1.png`** — one PNG per TikZ/CircuitiKZ figure, 1200 dpi
2. **`LabN/tikz_figures.tex`** — editable article LaTeX document, one figure
   per page with `\label` and `\caption` shown; compile with `pdflatex` to
   browse or edit circuits

Figures containing only `\includegraphics` are skipped.

## Pipeline

```
\begin{figure}...\end{figure}  (regex extraction)
  -> strip \savebox / \pdftooltip wrappers
  -> extract inner circuitikz or tikzpicture environment
  -> standalone .tex  ->  pdflatex  ->  pdftoppm -r 1200 -png  ->  PNG
  -> article .tex (tikz_figures.tex) written to LabN/
```

## Preamble (both standalone and article)

```latex
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\usepackage[american voltages, european currents]{circuitikz}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage[table,dvipsnames]{xcolor}
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}
```

`\definecolor` definitions are auto-extracted from the source file.
To support new packages in future labs, add to `STANDALONE_PREAMBLE` and
`ARTICLE_PREAMBLE` near the top of the script.

## Lab Source Files

All relative to `C:\Users\aknoesen\Documents\Knoesen\EEC1 Spring 2026\`:

| Lab | Source `.tex` | Output `media/` | Figures |
|-----|--------------|-----------------|:-------:|
| 1 | `Labs\Lab 1\Lab1Instructions.tex` | `Lab1\media` | 2 |
| 2 | `Labs\Lab 2\Lab2Instructions.tex` | `Lab2\media` | 6 |
| 3 | `Labs\Lab 3\Lab3Instructions.tex` | `Lab3\media` | 7 |
| 4 | `Labs\Lab 4\Lab4Instructions.tex` | `Lab4\media` | 7 |
| 5 | `Labs\Lab 5\Lab5Instructions.tex` | `Lab5\media` | 3 |
| 6 | `Labs\Lab 6 & 7 Operational Amplifiers\Lab6Instructions.tex` | `Lab6\media` | 5 |
| 7 | `Labs\Lab 6 & 7 Operational Amplifiers\Lab7Instructions.tex` | `Lab7\media` | 3 |
| 8 | `Project\Lab8Instructions.tex` | `Lab8\media` | 1 |

## Known Issues (as of 2026-03-25)

- **Lab 4 — duplicate label `fig:rl-setup`**: two distinct figures share the
  same label; `rl-setup-1.png` is overwritten by the second. Fix the label in
  `Lab4Instructions.tex` and re-run.
- **Lab 5 — subfigure**: the first figure uses `\begin{subfigure}` internally;
  only the first TikZ env is captured. Verify `fig_01-1.png`. May need the
  source split into separate `\begin{figure}` environments.
- **Lab 2 — label with `.png`**: `\label{fig:Lab3Fig1.png}` produces the
  filename `Lab3Fig1_png-1.png`. Consider renaming the label in the source.

## Workflow for Editing a Circuit

1. Open `LabN/tikz_figures.tex` — find the figure by its `\label` heading
2. Edit the TikZ code; compile with `pdflatex tikz_figures.tex` to preview
3. Copy the edited block back into `LabNInstructions.tex`
4. Re-run the script to regenerate the PNG:
   ```
   python "...\Lab Manuals\extract_tikz_figures.py" ^
     "...\LabNInstructions.tex" ^
     "...\Lab Manuals\LabN\media"
   ```

## User Profile

- **Course**: EEC1 (ECE Emerge), Spring 2026, ECE Department
- **Context**: Converting LaTeX lab manuals to ADA-compliant Markdown web pages
- **TeX distribution**: TeX Live 2025 (confirmed from log paths)
- **Tools in use**: `pdflatex`, `pdftoppm` (poppler), Python 3.10+

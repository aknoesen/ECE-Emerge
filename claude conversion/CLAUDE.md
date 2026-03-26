# CLAUDE.md — EEC1 Lab Manual Conversion Context

## What this project is

Converting 8 EEC1 Spring 2026 lab manuals from LaTeX (.tex) to ADA-compliant HTML.
Pipeline: LaTeX → Markdown (.md) → HTML via `md2ada.py`

**Labs 1–8 MD and HTML complete. Image sizing and math rendering updated 2026-03-26.**

---

## Key paths

| Item | Path |
|---|---|
| Authoritative procedure | `Lab Manuals/CONVERSION_PROCEDURE.md` |
| Converter script | `ADA Compliant Webpage Materials/md2ADAhtml/md2ada.py` |
| Lab source .tex files | `EEC1 Spring 2026/Labs/LabN/LabNInstructions.tex` |
| Lab 6 & 7 source | `EEC1 Spring 2026/Labs/Lab 6 & 7 Operational Amplifiers/` |
| Lab 8 source | `EEC1 Spring 2026/Project/Lab8Instructions.tex` |
| MD + HTML outputs | `Lab Manuals/LabN/LabNInstructions.md` and `LabN/htmlconversion/` |
| Media (images) | `Lab Manuals/LabN/media/` |
| This TODO + context dir | `Lab Manuals/claude conversion/` |

---

## Current status

| Lab | MD | HTML | Open issues |
|-----|-----|------|-------------|
| Lab 1 | Done | Done | None |
| Lab 2 | Done | Done | None |
| Lab 3 | Done | Done | None |
| Lab 4 | Done | Done | Duplicate `rl-setup` figure label — see TODO.md |
| Lab 5 | Done | Done | Verify `fig_01-1.png`; clean stray bullet in .tex — see TODO.md |
| Lab 6 | Done | Done | Missing `fig:powerconnection` figure — see TODO.md |
| Lab 7 | Done | Done | Verify HTML output path spelling — see TODO.md |
| Lab 8 | Done | Done | Duplicate `\prelabdeliverable{1}` numbering — see TODO.md |

---

## Rules to follow every time

- Always read `CONVERSION_PROCEDURE.md` before starting any conversion work
- Never modify `md2ada.py` CSS between labs
- Preserve `\pdftooltip` alt text verbatim — this is the ADA asset
- Keep all math as LaTeX `$...$` syntax — never flatten to Unicode
- circuitikz PNG filenames are label-derived: `labelname-1.png` (strip `fig:` prefix)
- Images sourced from `Labs/LabN/graphics/` OR `Labs/LabN/media/` OR `Labs/LabN/Media/` — check which exists per lab
- Filename sanitization: spaces → `_`, remove parentheses
- All images use inline HTML — `<img src="..." alt="..." style="width: 60%; display: block; margin: 0 auto;" />` — not `![alt](src)` markdown syntax

## Patterns established across Labs 1–8

| Construct | Handling |
|---|---|
| `\begin{verbatim}` or `\lstlisting[style=matlab]` | Fenced ` ```matlab ``` ` code block |
| `\newsavebox`/`\savebox`/`\usebox` + `\pdftooltip` | Extract alt text from `\pdftooltip`; use label-derived PNG name |
| `\begin{subfigure}` pair (no outer label) | Single image `fig_01-1.png` with combined alt text |
| Named tcolorbox (`Interactive Widget: ...`) | `> **Interactive Widget: ...**` blockquote |
| `\appendix` + subsequent `\section{}` | `## Appendix A/B/C: ...`; subsections `### A.1` etc. |
| `\begin{description}` | `- **term** -- text` |
| `\textdegree{}` outside math | `°` Unicode |
| Dangling `\ref{}` (undefined label) | Plain text placeholder; flag for human review |

---

## Do NOT

- Start a conversion without running the pre-assessment (Step 1 in CONVERSION_PROCEDURE.md)
- Flatten math to Unicode (e.g., write `$V = IR$` not `V = I×R`)
- Shorten or rewrite `\pdftooltip` alt text
- Copy the entire `graphics/` folder — only copy images referenced in `\includegraphics{}`
- Add deadlines, "submit to Gradescope", or "compile to PDF" language anywhere
- Use `![alt](src)` markdown image syntax — always use inline `<img>` HTML for per-image size control

## md2ada.py capabilities (as of 2026-03-26)

- Injects KaTeX CDN into every HTML output — math renders in any browser without configuration
- Protects `$...$` and `$$...$$` from the markdown parser — subscripts/superscripts inside math are safe
- Embeds all images as base64 data URIs — HTML is self-contained for Canvas/LMS upload
- Wraps tables with scrollable region and adds `<caption>` and `scope="col"` for ADA compliance

# LaTeX → ADA-Compliant HTML Conversion Procedure
## EEC1 Spring 2026 Lab Manuals

**Pipeline:** LaTeX source (`.tex`) → Markdown (`.md`) → ADA HTML (`.html`)
**Converter script:** `../md2ADAhtml/md2ada.py`
**Established with Lab 1 (March 2026). Validated on Lab 2 assessment.**

---

## Directory Structure Convention

```
ADA Compliant Webpage Materials/
  md2ADAhtml/
    md2ada.py                  ← shared converter, do not modify CSS between labs
  Lab Manuals/
    CONVERSION_PROCEDURE.md    ← this file
    Lab1/
      Lab1Instructions.md
      media/                   ← images only (no subdirs)
        [image files]
      htmlconversion/          ← auto-created by md2ada.py
        Lab1Instructions.html
    Lab2/
      Lab2Instructions.md
      media/
      htmlconversion/
    ...
```

---

## Step 1: Pre-Conversion Assessment (do this first, every lab)

Before writing any Markdown, read the `.tex` file in chunks and log:

1. **circuitikz / tikzpicture figures** — count them; each needs a pre-rendered PNG from the user. Note the figure label and a short filename for each placeholder.
2. **Math content** — note if heavier than Lab 1 (fractions, display equations, etc.). Math always stays as-is; this is just a heads-up.
3. **New LaTeX environments** — anything not in the table below (Section 4). Flag and decide handling before starting.
4. **Images referenced** — list filenames from `\includegraphics{}` calls; note any with spaces or special characters that need renaming.
5. **Appendix structure** — some labs have appendices, some don't; affects heading level choices.

**Do not start conversion until assessment is complete and any new elements have a handling decision.**

---

## Step 2: Image Handling

### Copy images

- Copy **only images actually referenced** in the `.tex` (not everything in `graphics/`).
- Source: `Labs/LabN/graphics/`
- Destination: `Lab Manuals/LabN/media/`

### Filename sanitization

Rename during copy if the original has:

| Issue | Rule | Example |
|-------|------|---------|
| Spaces | Replace with `_` | `M2K connectionV2.png` → `M2K_connectionV2.png` |
| Parentheses | Remove | `ADALM200 Overview 252057-fig-02(2).png` → `ADALM2000_Overview.png` |

Update the filename reference in the Markdown accordingly.

### Image sizing

All images use inline HTML. The default width is 60%, centered. Adjust the percentage per image after reviewing the HTML output.

```html
<img src="media/file.png" alt="full alt text here" style="width: 60%; display: block; margin: 0 auto;" />
```

Do not use standard `![alt](src)` markdown syntax for images — use the inline HTML form above for all images. This gives per-image size control without needing CSS overrides.

To resize after reviewing: change the `60%` value in the `.md` file and re-run the converter on that lab.

### circuitikz / tikzpicture placeholders

For figures generated entirely from LaTeX drawing code (no external image file):

```markdown
<!-- CIRCUITIKZ FIGURE: Render from LaTeX source as media/fig_NAME.png -->
<img src="media/fig_NAME.png" alt="Full alt text from \pdftooltip argument" style="width: 60%; display: block; margin: 0 auto;" />

*Figure N: Caption text.*
```

The placeholder means:
- The alt text is already in place for ADA compliance
- When the user drops the rendered PNG into `media/` with the matching filename, it works immediately
- The converter will warn `[WARN] image not found` until the PNG is provided — this is expected

**Important — rendered PNG naming convention:**
The LaTeX renderer names output files after the `\label{}` of the figure, not after placeholder names used in the Markdown. Always check actual filenames in `media/` before running the converter and update the Markdown references to match. From Lab 2, the pattern observed was:

| LaTeX `\label{}` | Rendered filename |
|-----------------|-------------------|
| `fig:Lab3Fig1.png` | `Lab3Fig1_png-1.png` |
| `fig:seriesparallel` | `seriesparallel-1.png` |
| `fig:acpec` | `acpec-1.png` |
| `fig:Lab3Fig1211` | `Lab3Fig1211-1.png` |
| `fig:resistivenet2` | `resistivenet2-1.png` |
| `fig:labConnnection1` | `labConnnection1-1.png` |

General pattern: `labelname-1.png` (label with `fig:` prefix stripped, special chars removed, `-1` suffix appended). **Always verify — do not assume placeholder names match rendered names.**

---

## Step 3: Markdown Conversion Rules

### Mathematics — CRITICAL

**Preserve all math exactly as LaTeX syntax.** Do not flatten to Unicode.

| LaTeX | Markdown |
|-------|----------|
| `$V = IR$` | `$V = IR$` (unchanged) |
| `$\frac{1}{R_{eq}}$` | `$\frac{1}{R_{eq}}$` (unchanged) |
| `$$...$$` display math | `$$...$$` (unchanged) |
| `\,` thin space in math | leave inside `$...$` unchanged |

`md2ada.py` automatically:
- Protects `$...$` and `$$...$$` spans from the markdown parser (prevents `_` inside math being converted to `<em>` tags)
- Injects KaTeX CDN scripts into every generated HTML file

No external viewer or manual configuration needed — math renders correctly in any browser.

### Section headings

| LaTeX | Markdown |
|-------|----------|
| `\section*{Overview}` | `## Overview` |
| `\section{Prelab Assignment}` | `## 1. Prelab Assignment` |
| `\subsection{...}` | `### 1.1 ...` |
| `\subsubsection{...}` | `#### ...` |
| `\subsubsection*{...}` | `#### ...` |
| `\paragraph{...}` | `##### ...` or bold paragraph heading |

For appendices: `\section*{Appendix A: ...}` → `## Appendix A: ...`, then sub-items as `###`.

### tcolorbox environments → blockquotes

All colored boxes become `> **LABEL**` blockquotes. The color is lost; the label carries the meaning.

| LaTeX command | Markdown pattern |
|---------------|-----------------|
| `\important{text}` | `> **IMPORTANT**` + `>` + text |
| `\deliverable{N}{text}` | `> **Lab Deliverable #N**` + `>` + text |
| `\prelabdeliverable{N}{text}` | `> **Prelab Deliverable #N**` + `>` + text |
| `\warningbox{text}` | `> **WARNING**` + `>` + text |
| `\guidancebox{Title}{text}` | `> **Title**` + `>` + text |
| `\begin{tcolorbox}[title=CHECKPOINT]` | `> **CHECKPOINT**` + `>` + text |
| `\begin{tcolorbox}[title=Self-Verification...]` | `> **Self-Verification Checklist**` + `>` + items |
| `\begin{tcolorbox}[title=Required Documentation]` | `> **Required Documentation**` + `>` + items |

Nested lists inside blockquotes: prefix every line with `>` and use `>   -` for list items.

### Figures and alt text — CRITICAL for ADA

The `\pdftooltip` argument is the ADA alt text. **Preserve it verbatim — do not shorten or paraphrase.**

```latex
\pdftooltip{\includegraphics[...]{graphics/file.png}}{Long alt text here.}
```
becomes:
```html
<img src="media/file.png" alt="Long alt text here." style="width: 60%; display: block; margin: 0 auto;" />
```

For figures that use `\includegraphics` without `\pdftooltip` (rare — check each lab), write a descriptive alt text based on the figure caption and visible content.

### Other common elements

| LaTeX | Markdown |
|-------|----------|
| `\texttrademark{}` or `\texttrademark` | `™` |
| `\textbf{text}` | `**text**` |
| `\textit{text}` or `\emph{text}` | `*text*` |
| `\texttt{text}` | `` `text` `` |
| `\underline{text}` | `<u>text</u>` (use sparingly) |
| `\textcolor{red}{text}` | `**text**` (drop color; bold preserves emphasis) |
| `\href{url}{text}` | `[text](url)` |
| `\url{url}` | `<url>` or bare URL |
| `\footnote{text}` | Inline parenthetical: `*(Note: text)*` |
| `\begin{quote}...\end{quote}` | `> *"quoted text"*` |
| `\begin{description}\item[term] text` | `- **term** — text` |
| `$\square$` (checklist) | `- [ ]` |
| `\vspace{}`, `\medskip`, `\noindent` | Delete |
| `\newpage` | `---` (horizontal rule) or delete |
| `\textsuperscript{st}` / `{rd}` / `{th}` | Plain text: `1st`, `3rd`, `5th` |
| `\pm` outside math | `±` |
| `\times` outside math | `×` |
| `\ldots` outside math | `…` |
| `\,` (thin space) outside math | regular space or delete |

### Figure captions

No native Markdown caption. Use italicized text on the line immediately after the image:

```html
<img src="media/file.png" alt="alt text" style="width: 60%; display: block; margin: 0 auto;" />

*Figure N: Caption text here.*
```

### Tables

Simple tables → standard Markdown table syntax. For tables with `\rowcolor` header rows (appears in Lab 2+), the CSS in `md2ada.py` already styles `<th>` with a blue background — no special treatment needed in Markdown, just use `|---|` header separators normally.

For fill-in blank tables (`\rule{0pt}{2cm}` cells in LaTeX — printable forms): render as a standard Markdown table with empty cells.

---

## Step 4: Run the Converter

```
python md2ada.py "C:\...\Lab Manuals\LabN\LabNInstructions.md"
```

Output is written to `LabN/htmlconversion/LabNInstructions.html`.

**Expected warnings (not errors):**
- `[WARN] image not found` for circuitikz placeholder filenames — expected until user provides rendered PNGs.

---

## Step 5: Quality Checks

After conversion, open the HTML and verify:

- [ ] All images display and are centered
- [ ] Small images (≤0.35\textwidth) are visibly smaller than default images
- [ ] All math renders correctly (requires KaTeX/MathJax in the viewer)
- [ ] All deliverable blockquotes are visually distinct
- [ ] Tables have header row styling
- [ ] No broken layout from nested blockquote lists
- [ ] circuitikz placeholder images show the correct alt text (screen reader accessible even before PNG is provided)

---

## DO's

- **Do** preserve `\pdftooltip` alt text verbatim — this is the primary ADA asset
- **Do** keep all math as LaTeX syntax — KaTeX/MathJax handles it
- **Do** run the assessment step before each lab — new elements appear (Lab 2 introduced `\rowcolor` tables, `\paragraph`, fill-in forms)
- **Do** use the exact blockquote pattern for deliverables — students and graders rely on visual consistency
- **Do** note circuitikz placeholders clearly with the `<!-- CIRCUITIKZ FIGURE: ... -->` comment so nothing gets missed
- **Do** check actual rendered PNG filenames in `media/` before writing Markdown references — the renderer uses `\label{}`-derived names, not placeholder names (see circuitikz section above)

## DON'Ts

- **Don't** modify `md2ada.py` CSS between labs — it is correctly configured
- **Don't** use standard `![alt](src)` markdown image syntax — use inline `<img>` HTML so sizes are adjustable per image
- **Don't** flatten math to Unicode approximations (e.g., don't write `V = I×R` instead of `$V = IR$`) — future labs have complex equations
- **Don't** shorten or rewrite alt text — even if it seems long; length is not a problem, missing or vague alt text is
- **Don't** copy the entire `graphics/` folder — only copy images that appear in `\includegraphics{}` calls
- **Don't** rename image files in `media/` after the Markdown references them
- **Don't** start converting without the pre-assessment — it prevents mid-conversion surprises

---

## Lab Status

| Lab | Assessment | MD Created | Images Copied | circuitikz PNGs | HTML Generated |
|-----|-----------|-----------|--------------|----------------|----------------|
| Lab 1 | ✓ | ✓ | ✓ (24 images) | ✓ (2 embedded) | ✓ |
| Lab 2 | ✓ | ✓ | ✓ (7 images) | ✓ (6 embedded) | ✓ |
| Lab 3 | ✓ | ✓ | ✓ (27 images) | ✓ (7 embedded) | ✓ |
| Lab 4 | ✓ | ✓ | ✓ (2 images) | ✓ (6 embedded) | ✓ |
| Lab 5 | ✓ | ✓ | ✓ (3 images) | ✓ (3 embedded) | ✓ |
| Lab 6 | ✓ | ✓ | ✓ (4 images) | ✓ (5 embedded) | ✓ |
| Lab 7 | ✓ | ✓ | ✓ (2 images) | ✓ (3 embedded) | ✓ |
| Lab 8 | ✓ | ✓ | ✓ (0 images) | ✓ (1 embedded) | ✓ |

---

## Lab-Specific Notes

### Lab 1
- 2 circuitikz figures: `SingleMeas1-1.png` (Figure 13), `differential-1.png` (Figure 15)
- 2 small images overridden to 35%: `ADALM2000_Overview.png`, `GenderConnections.png`
- Image `ADALM200 Overview 252057-fig-02(2).png` renamed to `ADALM2000_Overview.png`
- Image `M2K connectionV2.png` renamed to `M2K_connectionV2.png`

### Lab 2
- 5 circuitikz figures + 1 pure tikzpicture (bullseye precision/accuracy diagram) — all 6 rendered and embedded
- Rendered filenames (label-derived): `Lab3Fig1_png-1.png`, `seriesparallel-1.png`, `acpec-1.png`, `Lab3Fig1211-1.png`, `resistivenet2-1.png`, `labConnnection1-1.png`
- `\rowcolor{blue!20}` table headers → standard Markdown `th` (CSS handles styling)
- Fill-in blank resistor measurement table (`\rule{0pt}{2cm}`) → empty table cells
- Tables inside `\deliverable{}` boxes (post-lab deliverables 18 and 21) placed after the blockquote, not inside it
- `\paragraph{}` used for "Optional Explorations" sub-items → `#####` heading level
- No appendices (simpler than Lab 1)
- No footnotes
- `Steps to enable XY mode.png` renamed to `Steps_to_enable_XY_mode.png`

### Lab 3
- 7 circuitikz/tikz figures: `connection-1.png`, `diode-symbol-lab-1.png`, `diode-iv-lab-1.png`, `zener-iv-lab-1.png`, `iv-circuit-planning-1.png`, `square_wave_spectrum-1.png`, `iv-circuit-1.png`
- 20 regular graphics — all `scale=2` screenshots; default 70% CSS used for all (no size overrides needed)
- Key filename renames: spaces→`_`, parentheses removed; `.csv` retained in names like `sine_100ksps_time_ch1_csv_line_4-11.png`; `1st + 3rd` → `1st_3rd` (dropped `+` for cleanliness)
- `[enumerate, resume]` lists: handled by explicit numbering continuation after figures (4., 5., etc.)
- `\textsuperscript{st/rd/th}` ordinals → plain text (1st, 3rd, 5th)
- MATLAB `\lstlisting[style=matlab]` → fenced ` ```matlab ``` ` code blocks
- WARNING tcolorbox wrapping lstlisting (invalid in LaTeX warningbox) → `> **WARNING**` blockquote + separate fenced code block immediately after
- Unnamed orange/yellow tcolorboxes (no title) → `> **Note**`
- `pgfplots` IV curve and spectrum figures → rendered as circuitikz PNGs (same rendering pipeline)
- No appendices, no tables inside deliverable boxes

### Lab 4
- 6 circuitikz figures: `cl-circuit-1.png`, `rl-setup-1.png` (used twice -- prelab and procedure share same label), `prelab-rc-1.png`, `prelab-rl-1.png`, `rc-setup-1.png`, `rl-setup1-1.png`
- 2 regular images sourced from `Labs/Lab 4/media/` (no `graphics/` folder): `Waveformsforpulsewidthequalto5tRC.png`, `Waveformsforpulsewidthequalto5tRL.png` (no renames needed)
- `\newsavebox` + `\savebox` + `\usebox` pattern for circuitikz -- renders normally; label-derived PNG naming still applies
- Duplicate `\label{fig:rl-setup}` on two slightly different circuits -- both reference `rl-setup-1.png`
- `\begin{verbatim}` code blocks → fenced generic ` ``` ``` ` code blocks
- Custom tcolorbox variants: `Practice Problem (Ungraded)`, `Why $R_G$ matters...`, `Interactive Widget: RC/RL` → blockquotes with title as bold label
- 3 appendices (A, B, C) -- `\section{Appendix A/B/C}` → `## Appendix A/B/C: ...`; subsections → `### A.1`, `### B.1`, etc.
- `\begin{description}` environment (Appendix C) → `- **term** -- text` bullet list
- Converter ran with zero warnings -- all 8 images found in media/

### Lab 5
- 3 circuitikz figures: `fig_01-1.png` (subfigure pair, Circuit 1 and 2), `lp-circuit-1.png` (low-pass connection diagram), `hp-circuit-1.png` (high-pass connection diagram)
- 3 regular screenshots (no filename renames needed -- no spaces or parens): `Stepstomeasuretimedelay.png`, `ScopyNetworkAnalyzerLPF.png`, `ScopyNetworkAnalyzerLPExport.png`
- Images sourced from `Labs/Lab 5/Media/` (capitalized) not `graphics/` -- no `graphics/` folder exists for this lab
- `\begin{subfigure}` pair → single image reference `fig_01-1.png` with combined alt text describing both circuits
- Named tcolorboxes without standard macro (Interactive Widget: ...) → `> **Interactive Widget: ...**` blockquote
- `\begin{verbatim}` MATLAB code block → fenced ` ```matlab ``` ` code block
- `\begin{description}` environment → `- **term** -- text` list items
- Numbered prelab deliverables with dot notation (1d.A, 1d.B, 1d.C, 1ei, 1eii, etc.) → `> **Prelab Deliverable #1d.A**` etc.
- `●` bullet character in source (line 153) → treated as start of `\prelabdeliverable{}` block, not a separate element
- `\newsavebox`/`\savebox`/`\usebox` pattern: pdftooltip wraps usebox → alt text from pdftooltip argument as usual
- No appendices; no tables inside deliverable boxes; fill-in measurement tables → standard Markdown tables with empty cells
- Converter produced clean output (no [WARN] messages); em-dash in output is from md2ada.py CSS template comment, not lab content

### Lab 6
- 5 circuitikz figures (all pre-rendered and present in media/ before conversion): `unity-gain-1.png`, `buffer-example-1.png`, `buffer-example2-1.png`, `buffer-example3-1.png`, `lm6134-pins2-1.png`
- 4 regular images copied from `Labs/Lab 6 & 7 Operational Amplifiers/Media/` (capitalized, no `graphics/` folder): `v_follower-waveform.png`, `slewrate.png`, `Rising edge with cursors.png` → `Rising_edge_with_cursors.png`, `LM6132Pinout.png`
- `LM6132Pinout.png` is small (2.6in LaTeX width) → overridden to `style="max-width:35%;"` inline HTML
- `\newsavebox`/`\savebox`/`\usebox` pattern for all circuitikz figures; `\pdftooltip` wraps `\usebox` → alt text from pdftooltip argument
- `\begin{verbatim}` blocks for MATLAB code → fenced ` ```matlab ``` ` code blocks
- `\begin{description}` environment in AI exercise Part 3 → `- **term** -- text` list items
- `\appendix` command: subsequent `\section{}` become Appendix A, Appendix B with `### A.1`, `### B.1` subsections
- `\footnote{}` in title → inline parenthetical `*(Note: ...)*`
- Dangling `\ref{fig:powerconnection}` (figure defined nowhere in file) → replaced with plain "Figure 1"; no image is missing
- Fill-in tables inside `\prelabdeliverable{}` boxes → Markdown tables with empty cells, inside blockquote
- Self-Verification Checklist tcolorbox with `$\square$` → `- [ ]` checklist items
- Converter produced clean output (no [WARN] messages); all 9 images found and base64-embedded (~2 MB HTML)

### Lab 7
- 3 circuitikz figures (all pre-rendered in media/): `non-inverting-amp-1.png` (Figure 1), `inverting-amp-1.png` (Figure 3), `summing-amp-1.png` (Figure 5)
- 2 regular screenshots from `Labs/Lab 6 & 7 Operational Amplifiers/Media/` (no renames needed): `noninverting_amp-waveform.png`, `inverting_amp-waveform.png`
- `\newsavebox`/`\savebox`/`\usebox` pattern for circuitikz; `\pdftooltip` wraps `\usebox` → alt text from pdftooltip
- `\begin{description}` environment → `- **term** -- text` list items
- `\textdegree{}` → `°` Unicode (outside math context)
- `\footnote{}` in title block → inline parenthetical `*(Note: ...)*`
- Deliverable numbers start at 4a (1, 2 are prelab; 3, 7a belong to Lab 6 shared numbering) — preserved verbatim from source
- Converter produced clean output (no [WARN] messages); all 5 images found and base64-embedded

### Lab 8
- 1 circuitikz figure (pre-rendered in media/): `INA125_complete-1.png`
- 0 regular images — Lab 8 has no `\includegraphics{}` calls
- `\begin{description}` environment → `- **term** -- text` list items
- `\begin{quote}\textit{...}` → `> *"..."*`
- `\section*{Individual and Team Work}` (unnumbered) → `## Individual and Team Work`
- `\subsection*{Next Step:}` and `\subsection*{Section N:}` (unnumbered) → `###` without section numbers
- Duplicate `\prelabdeliverable{1}` in source: used in Section 1 (reflection) and again in Section 2 (INA gain selection) — preserved verbatim; may need renumbering in source
- Converter produced clean output (no [WARN] messages); 1 image embedded (~699 KB HTML)

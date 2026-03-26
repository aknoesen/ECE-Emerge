#!/usr/bin/env python3
"""
extract_tikz_figures.py

Extracts tikz/circuitikz figures from a LaTeX file and:
  1. Renders each figure as a high-resolution PNG in <output_dir>
  2. Writes an editable LaTeX reference document (<lab_folder>/tikz_figures.tex)
     containing all figures one per page with label and caption, ready to compile.

Figures containing only \\includegraphics are skipped.

Usage:
    python extract_tikz_figures.py <input.tex> <output_dir>

  output_dir is expected to be the media/ subfolder of the lab folder, e.g.:
    .../Lab Manuals/Lab2/media
  tikz_figures.tex is written one level up, into .../Lab Manuals/Lab2/

Requirements:
    - pdflatex (in PATH, part of MiKTeX / TeX Live)
    - pdftoppm  (in PATH, part of poppler-utils / MiKTeX)
"""

import re
import subprocess
import os
import sys
import tempfile

# ---------------------------------------------------------------------------
# Standalone preamble — used when compiling individual PNGs.
# ---------------------------------------------------------------------------
STANDALONE_PREAMBLE = r"""\documentclass[border=8pt]{standalone}
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\usepackage[american voltages, european currents]{circuitikz}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage[table,dvipsnames]{xcolor}
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}
"""

# ---------------------------------------------------------------------------
# Article preamble — used for the editable reference document.
# ---------------------------------------------------------------------------
ARTICLE_PREAMBLE = r"""\documentclass[12pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\usepackage[american voltages, european currents]{circuitikz}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage[table,dvipsnames]{xcolor}
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}
\usepackage{float}
\usepackage{caption}
\usepackage{parskip}
"""


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def extract_definecolors(tex: str) -> str:
    """Return all \\definecolor lines found in the source file."""
    colors = re.findall(r'\\definecolor\{[^}]+\}\{[^}]+\}\{[^}]+\}', tex)
    return '\n'.join(colors)


def label_to_filename(label: str) -> str:
    """Turn a \\label value into a safe filename stem."""
    name = re.sub(r'^fig:', '', label)
    name = re.sub(r'[^a-zA-Z0-9_-]', '_', name)
    name = name.strip('_')
    return name or 'fig'


def tex_escape(s: str) -> str:
    """Escape characters that are special in LaTeX text mode."""
    s = s.replace('\\', r'\textbackslash{}')
    for ch in ('_', '#', '$', '%', '&', '{', '}', '^', '~'):
        s = s.replace(ch, '\\' + ch)
    return s


def extract_inner_tikz(fig_block: str) -> str | None:
    """
    Return the first tikzpicture or circuitikz environment found inside a
    figure block, regardless of savebox / pdftooltip wrappers.
    """
    for env in ('circuitikz', 'tikzpicture'):
        m = re.search(
            r'(\\begin\{' + env + r'\}.*?\\end\{' + env + r'\})',
            fig_block, re.DOTALL
        )
        if m:
            return m.group(1)
    return None


def extract_caption(fig_block: str) -> str:
    m = re.search(r'\\caption\{(.*?)\}(?=\s*\\label|\s*\\end\{figure\})',
                  fig_block, re.DOTALL)
    if m:
        return re.sub(r'\s+', ' ', m.group(1)).strip()
    return ''


def extract_label(fig_block: str) -> str | None:
    m = re.search(r'\\label\{([^}]+)\}', fig_block)
    return m.group(1) if m else None


def extract_figures(tex: str) -> list[dict]:
    """
    Find every \\begin{figure}...\\end{figure} block that contains a
    tikzpicture or circuitikz environment.  Returns a list of dicts with
    keys: label, filename, caption, tikz.
    """
    figures = []
    pattern = re.compile(r'\\begin\{figure\}.*?\\end\{figure\}', re.DOTALL)

    for i, m in enumerate(pattern.finditer(tex), start=1):
        block = m.group(0)

        tikz = extract_inner_tikz(block)
        if tikz is None:
            continue  # \includegraphics-only figure — skip

        label   = extract_label(block)
        caption = extract_caption(block)

        filename = label_to_filename(label) if label else f'fig_{i:02d}'

        figures.append({
            'label':    label or f'(unlabelled #{i})',
            'filename': filename,
            'caption':  caption,
            'tikz':     tikz,
        })

    return figures


# ---------------------------------------------------------------------------
# Build LaTeX documents
# ---------------------------------------------------------------------------

def build_standalone(tikz: str, extra_preamble: str) -> str:
    lines = [STANDALONE_PREAMBLE]
    if extra_preamble:
        lines.append('% -- colors from source file --')
        lines.append(extra_preamble)
    lines.append(r'\begin{document}')
    lines.append(tikz)
    lines.append(r'\end{document}')
    return '\n'.join(lines) + '\n'


def build_editable_latex(figures: list[dict], extra_preamble: str,
                         source_name: str) -> str:
    """
    Build a compilable article document with all figures one per page.
    Each page shows the \\label, caption, and the editable TikZ source.
    """
    lines = [ARTICLE_PREAMBLE]
    if extra_preamble:
        lines.append('% -- colors from source file --')
        lines.append(extra_preamble)
    lines.append('')
    lines.append(r'\begin{document}')
    lines.append('')
    lines.append(r'\begin{center}')
    lines.append(r'  {\LARGE\textbf{TikZ / CircuitiKZ Figures}}\\[0.4em]')
    lines.append(r'  {\large\texttt{' + tex_escape(source_name) + r'}}')
    lines.append(r'\end{center}')
    lines.append(r'\vspace{1em}')
    lines.append(r'\noindent Edit the TikZ code in this file, then recompile')
    lines.append(r'with \texttt{pdflatex} to preview changes.  Run')
    lines.append(r'\texttt{extract\_tikz\_figures.py} to regenerate the PNGs.')

    for fig in figures:
        lines.append('')
        lines.append(r'\clearpage')
        lines.append('')
        # Label banner
        lines.append(r'\noindent\textbf{Label:} \texttt{'
                     + tex_escape(fig['label']) + r'}\\[0.5em]')
        # Figure
        lines.append(r'\begin{figure}[H]')
        lines.append(r'  \centering')
        # Indent the tikz block for readability
        for tikz_line in fig['tikz'].splitlines():
            lines.append('  ' + tikz_line)
        if fig['caption']:
            lines.append(r'  \caption{' + fig['caption'] + r'}')
        lines.append(r'\end{figure}')

    lines.append('')
    lines.append(r'\end{document}')
    return '\n'.join(lines) + '\n'


# ---------------------------------------------------------------------------
# Compilation helpers
# ---------------------------------------------------------------------------

def run(cmd: list[str], cwd: str) -> tuple[int, str]:
    """Run a command, return (returncode, combined stdout+stderr)."""
    result = subprocess.run(
        cmd, cwd=cwd,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        text=True
    )
    return result.returncode, result.stdout


def compile_figure(standalone_tex: str, stem: str,
                   output_dir: str, work_dir: str) -> bool:
    """
    Write standalone_tex to work_dir/<stem>.tex, compile with pdflatex,
    then convert the PDF to PNG via pdftoppm.
    Returns True on success.
    """
    tex_path = os.path.join(work_dir, stem + '.tex')
    pdf_path = os.path.join(work_dir, stem + '.pdf')

    with open(tex_path, 'w', encoding='utf-8') as f:
        f.write(standalone_tex)

    rc, log = run(
        ['pdflatex', '-interaction=nonstopmode', '-halt-on-error', tex_path],
        cwd=work_dir
    )
    if rc != 0 or not os.path.exists(pdf_path):
        print(f'    [FAIL] pdflatex returned {rc}')
        tail = '\n'.join(log.splitlines()[-40:])
        print(tail)
        return False

    png_prefix = os.path.join(output_dir, stem)
    rc, log = run(
        ['pdftoppm', '-r', '1200', '-png', pdf_path, png_prefix],
        cwd=work_dir
    )
    if rc != 0:
        print(f'    [FAIL] pdftoppm returned {rc}: {log.strip()}')
        return False

    return True


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    input_tex  = sys.argv[1]
    output_dir = sys.argv[2]

    if not os.path.isfile(input_tex):
        print(f'ERROR: cannot find {input_tex}')
        sys.exit(1)

    os.makedirs(output_dir, exist_ok=True)

    with open(input_tex, 'r', encoding='utf-8') as f:
        tex = f.read()

    extra_preamble = extract_definecolors(tex)

    figures = extract_figures(tex)
    if not figures:
        print('No tikz/circuitikz figures found.')
        return

    source_name = os.path.basename(input_tex)
    print(f'Found {len(figures)} tikz/circuitikz figure(s) in {source_name}\n')

    # --- Render PNGs ---
    ok_count = 0
    with tempfile.TemporaryDirectory() as work_dir:
        for i, fig in enumerate(figures, 1):
            short_caption = (fig['caption'][:60] + '…') if len(fig['caption']) > 60 else fig['caption']
            print(f'[{i}/{len(figures)}] {fig["filename"]}')
            print(f'        label  : {fig["label"]}')
            print(f'        caption: {short_caption or "(none)"}')

            standalone = build_standalone(fig['tikz'], extra_preamble)
            success = compile_figure(standalone, fig['filename'], output_dir, work_dir)

            if success:
                produced = sorted(
                    f for f in os.listdir(output_dir)
                    if f.startswith(fig['filename']) and f.endswith('.png')
                )
                print(f'        -> {", ".join(produced)}')
                ok_count += 1
            print()

    print(f'Done: {ok_count}/{len(figures)} figures rendered.')
    print(f'PNGs in: {output_dir}')

    # --- Write editable LaTeX reference document ---
    # Place it in the lab folder (one level above media/)
    lab_dir = os.path.dirname(os.path.abspath(output_dir))
    editable_path = os.path.join(lab_dir, 'tikz_figures.tex')
    editable_tex = build_editable_latex(figures, extra_preamble, source_name)
    with open(editable_path, 'w', encoding='utf-8') as f:
        f.write(editable_tex)
    print(f'Editable LaTeX: {editable_path}')


if __name__ == '__main__':
    main()

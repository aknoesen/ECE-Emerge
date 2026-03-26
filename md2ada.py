"""
Universal Markdown -> ADA-Compliant HTML Converter
----------------------------------------------------
Usage:
    python md2ada.py [path/to/file.md]

If no argument is given, the script prompts for a file path.

Output is written to an  htmlconversion/  subdirectory
created next to the input .md file.

Requires:
    pip install markdown beautifulsoup4

ADA compliance features:
    - <html lang="en">
    - <meta charset="UTF-8"> and viewport meta
    - Skip-to-content link
    - <main> landmark region
    - Table <caption> elements (screen reader table identification)
    - scope="col" on all <th> elements
    - Responsive table wrapper with role="region" and aria-label
    - High-contrast color scheme (all foreground/background pairs >= 4.5:1)
    - Images embedded as base64 data URIs (self-contained for LMS upload)
    - Images require alt text in the Markdown source
"""

import sys
import re
import base64
import mimetypes
from pathlib import Path

# ── dependency check ──────────────────────────────────────────────────────────
try:
    import markdown
    from bs4 import BeautifulSoup
except ImportError:
    print("Installing required packages...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install",
                           "markdown", "beautifulsoup4", "-q"])
    import markdown
    from bs4 import BeautifulSoup

# ── CSS (ADA-compliant styling) ───────────────────────────────────────────────
CSS = """
    /* ── Skip navigation (ADA requirement) ── */
    .skip-link {
      position: absolute;
      left: -9999px;
      top: auto;
      width: 1px;
      height: 1px;
      overflow: hidden;
    }
    .skip-link:focus {
      position: static;
      width: auto;
      height: auto;
      display: block;
      padding: 8px 16px;
      background: #005a9c;
      color: #ffffff;
      font-weight: bold;
      text-decoration: none;
    }

    /* ── Base typography ── */
    body {
      font-family: Georgia, "Times New Roman", serif;
      font-size: 1rem;
      line-height: 1.6;
      color: #1a1a1a;
      background: #ffffff;
      margin: 0;
      padding: 0;
    }
    main {
      max-width: 960px;
      margin: 0 auto;
      padding: 1.5rem 1.25rem 3rem;
    }

    /* ── Headings ── */
    h1 {
      font-size: 1.75rem;
      border-bottom: 3px solid #005a9c;
      padding-bottom: 0.4rem;
      color: #003366;
    }
    h2 {
      font-size: 1.3rem;
      margin-top: 2.25rem;
      color: #003366;
      border-left: 5px solid #005a9c;
      padding-left: 0.6rem;
    }
    h3 {
      font-size: 1.05rem;
      margin-top: 1.5rem;
      color: #003366;
    }

    /* ── Blockquote (callout boxes) ── */
    blockquote {
      border-left: 4px solid #6699cc;
      margin: 0.75rem 0;
      padding: 0.5rem 1rem;
      background: #f0f5ff;
      color: #1a1a1a;
    }

    /* ── Inline code ── */
    code {
      font-family: "Courier New", Courier, monospace;
      font-size: 0.9em;
      background: #f4f4f4;
      padding: 0.1em 0.35em;
      border-radius: 3px;
      color: #1a1a1a;
    }

    /* ── Images ── */
    img {
      max-width: 70%;
      height: auto;
      display: block;
      margin: 1rem auto;
    }

    /* ── Horizontal rule ── */
    hr {
      border: none;
      border-top: 1px solid #cccccc;
      margin: 1.5rem 0;
    }

    /* ── Responsive table wrapper ── */
    .table-wrapper {
      overflow-x: auto;
      margin: 1rem 0 1.5rem;
      border: 1px solid #aaaaaa;
      border-radius: 4px;
    }

    /* ── Tables ── */
    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.93rem;
    }
    caption {
      caption-side: top;
      text-align: left;
      font-weight: bold;
      font-size: 0.95rem;
      padding: 0.5rem 0.75rem;
      background: #003366;
      color: #ffffff;
    }
    th {
      background: #005a9c;
      color: #ffffff;
      text-align: left;
      padding: 0.5rem 0.75rem;
      white-space: nowrap;
    }
    td {
      padding: 0.45rem 0.75rem;
      border-top: 1px solid #dddddd;
      vertical-align: top;
    }
    tr:nth-child(even) td {
      background: #f7f9ff;
    }
    tr:hover td {
      background: #eef3ff;
    }

    /* ── Strong / emphasis ── */
    strong {
      color: #8b0000;  /* dark red — passes 4.5:1 contrast on white */
    }
    em {
      color: #555555;
    }

    /* ── Focus visible for keyboard navigation ── */
    a:focus, button:focus, [tabindex]:focus {
      outline: 3px solid #005a9c;
      outline-offset: 2px;
    }
"""


# ── KaTeX CDN (math rendering) ───────────────────────────────────────────────
KATEX_HEAD = """  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16/dist/katex.min.css" crossorigin="anonymous" />
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16/dist/katex.min.js" crossorigin="anonymous"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16/dist/contrib/auto-render.min.js" crossorigin="anonymous"
    onload="renderMathInElement(document.body, {
      delimiters: [
        {left: '$$', right: '$$', display: true},
        {left: '$',  right: '$',  display: false}
      ],
      throwOnError: false
    });"></script>"""


# ── math protection (prevents markdown parser mangling $...$ content) ─────────
def _protect_math(text: str) -> tuple[str, dict]:
    """Replace math spans with unique placeholders before markdown conversion."""
    placeholders: dict[str, str] = {}
    counter = [0]

    def _store(m: re.Match) -> str:
        key = f"XMATH{counter[0]}X"
        placeholders[key] = m.group(0)
        counter[0] += 1
        return key

    # Display math first (must come before inline to avoid partial matches)
    text = re.sub(r'\$\$[\s\S]+?\$\$', _store, text)
    # Inline math
    text = re.sub(r'\$[^$\n]+?\$', _store, text)
    return text, placeholders


def _restore_math(html: str, placeholders: dict) -> str:
    for key, value in placeholders.items():
        html = html.replace(key, value)
    return html


# ── conversion function ───────────────────────────────────────────────────────
def convert(md_path: Path) -> Path:
    """Convert a Markdown file to ADA-compliant HTML.

    The output HTML is written to an  htmlconversion/  subdirectory
    created inside the same directory as the input file.

    Returns the path of the generated HTML file.
    """
    md_path = md_path.resolve()
    if not md_path.exists():
        raise FileNotFoundError(f"Input file not found: {md_path}")
    if md_path.suffix.lower() != ".md":
        raise ValueError(f"Expected a .md file, got: {md_path.name}")

    # Output directory: htmlconversion/ next to the input file
    out_dir = md_path.parent / "htmlconversion"
    out_dir.mkdir(parents=True, exist_ok=True)
    html_path = out_dir / (md_path.stem + ".html")

    md_text = md_path.read_text(encoding="utf-8")

    # Protect math spans from the markdown parser before conversion
    md_text, math_placeholders = _protect_math(md_text)

    # Convert MD -> HTML fragment
    conv = markdown.Markdown(extensions=["tables", "nl2br"])
    body_html = conv.convert(md_text)

    # Restore math spans (placeholders are in text nodes; restore before soup parse)
    body_html = _restore_math(body_html, math_placeholders)

    soup = BeautifulSoup(body_html, "html.parser")

    # Page title: first <h1>, else filename stem
    h1 = soup.find("h1")
    page_title = h1.get_text(strip=True) if h1 else md_path.stem.replace("_", " ")

    # 0. Embed images as base64 data URIs (self-contained for Canvas / LMS)
    for img in soup.find_all("img"):
        src = img.get("src", "")
        if src.startswith("data:"):
            continue  # already embedded
        img_path = (md_path.parent / src).resolve()
        if img_path.exists():
            mime, _ = mimetypes.guess_type(str(img_path))
            mime = mime or "image/png"
            b64 = base64.b64encode(img_path.read_bytes()).decode("ascii")
            img["src"] = f"data:{mime};base64,{b64}"
        else:
            print(f"  [WARN] image not found, skipping embed: {img_path}")

    # 1. scope="col" on every <th>
    for th in soup.find_all("th"):
        th["scope"] = "col"

    # 2. <caption> + scrollable wrapper on every <table>
    for table in soup.find_all("table"):
        # Nearest preceding h2 or h3 becomes the caption
        caption_text = page_title
        for prev in table.find_all_previous(["h2", "h3"]):
            caption_text = prev.get_text(strip=True)
            break

        caption_tag = soup.new_tag("caption")
        caption_tag.string = caption_text
        table.insert(0, caption_tag)

        wrapper = soup.new_tag(
            "div",
            attrs={
                "class": "table-wrapper",
                "role": "region",
                "aria-label": caption_text,
                "tabindex": "0",
            },
        )
        table.wrap(wrapper)

    html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{page_title}</title>
  <style>{CSS}  </style>
{KATEX_HEAD}
</head>
<body>
  <a class="skip-link" href="#main-content">Skip to main content</a>
  <main id="main-content" role="main">
    {str(soup)}
  </main>
</body>
</html>
"""

    html_path.write_text(html_doc, encoding="utf-8")
    return html_path


# ── main ──────────────────────────────────────────────────────────────────────
def main() -> None:
    if len(sys.argv) >= 2:
        md_input = sys.argv[1]
    else:
        md_input = input("Enter path to Markdown file: ").strip().strip('"').strip("'")

    md_path = Path(md_input)

    print(f"\nConverting: {md_path.name}")
    try:
        html_path = convert(md_path)
        print(f"  [OK]  ->  {html_path}")
    except (FileNotFoundError, ValueError) as exc:
        print(f"  [ERROR]  {exc}")
        sys.exit(1)

    print("\nTo use in Canvas:")
    print("  1. Create or edit a Canvas Page")
    print("  2. Click the '<>' (HTML Editor) button in the toolbar")
    print(f"  3. Paste the contents of:  {html_path}")


if __name__ == "__main__":
    main()

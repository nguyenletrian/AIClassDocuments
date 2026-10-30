#!/usr/bin/env python3
"""Render one A4 landscape, print-ready PDF for each bilingual lab/exercise handout."""
from __future__ import annotations

import ast
import html
import re
from pathlib import Path

import fitz
import mistune
from weasyprint import HTML

ROOT = Path(__file__).resolve().parents[1]
PRINT = ROOT / "exports" / "print"
PDF_DIR = PRINT / "pdf"
DOCUMENTS = [
    "exercises/ASSIGNMENT-01.md",
    "labs/LAB-04.md",
    "labs/LAB-05.md",
    "labs/LAB-05-06.md",
    "labs/LAB-07.md",
    "labs/LAB-08.md",
    "labs/LAB-10.md",
    "exercises/PRETEST.md",
    "exercises/LAB-MATH-02.md",
    "exercises/LAB-MATH-03-04.md",
]
EXPECTED = (
    "## 1. Đề bài tiếng Anh",
    "## 2. Đề bài tiếng Việt",
    "## 3. Code Python có chú thích",
    "## 4. Giải thích nội dung và cách giải",
)
CSS = """
@page {
  size: A4 landscape;
  margin: 10mm 12mm 11mm;
  @top-right { content: "AIClassDocuments · Lab & Exercise"; font: 7pt 'Noto Sans'; color: #666; }
  @bottom-center { content: counter(page); font: 7.3pt 'Noto Sans'; color: #555; }
}
html { font-family: 'Noto Sans', 'DejaVu Sans', sans-serif; color: #182331; }
body { margin: 0; font-size: 9.15pt; line-height: 1.37; overflow-wrap: break-word;
       columns: 1; column-count: 1; column-width: auto; }
h1 { font-size: 15pt; line-height: 1.2; color: #173d5e; margin: 0 0 4mm; }
h2 { font-size: 11pt; line-height: 1.3; color: #173d5e; background: #edf2f6;
     border-left: 2.5pt solid #4a718c; margin: 4mm 0 2mm; padding: 1.2mm 2mm;
     break-after: avoid; }
h3 { font-size: 9.6pt; color: #24475e; margin: 3mm 0 1mm; break-after: avoid; }
h4 { font-size: 9pt; margin: 2mm 0 1mm; break-after: avoid; }
p { margin: 0 0 1.5mm; orphans: 2; widows: 2; }
ol, ul { padding-left: 6.5mm; margin: 1mm 0 2mm; }
li { margin: .6mm 0; }
pre { font: 7.15pt/1.28 'DejaVu Sans Mono', monospace; white-space: pre-wrap;
      overflow-wrap: anywhere; word-break: break-word; background: #fafafa;
      padding: 1.8mm 2mm; margin: 1.4mm 0 2.4mm; }
code { font-family: 'DejaVu Sans Mono', monospace; font-size: .87em;
       overflow-wrap: anywhere; }
pre code { font-size: 1em; }
table { border-collapse: collapse; width: 100%; margin: 2mm 0; font-size: 8.2pt; }
th, td { border-bottom: .45pt solid #c4cbd3; padding: 1.1mm 2mm; text-align: left; }
th { background: #edf2f6; }
blockquote { border-left: 2pt solid #a9b8c8; padding-left: 3mm; margin: 2mm 0; }
"""

def extract_blocks(document: str, filename: str):
    headings = list(re.finditer(r"^## (?:[1-4])\. .+$", document, flags=re.M))
    if [item.group().strip() for item in headings] != list(EXPECTED):
        raise ValueError(f"{filename}: missing/incorrect section order")
    text_sections = []
    for i, match in enumerate(headings):
        end = headings[i + 1].start() if i + 1 < len(headings) else len(document)
        section = document[match.end():end].strip()
        if not section:
            raise ValueError(f"{filename}: empty section {i + 1}")
        text_sections.append(section)
    return text_sections

def validate_source(content: str, filename: str):
    sections = extract_blocks(content, filename)
    python_blocks = re.findall(r"(?ms)^" + chr(96) * 3 + r"python\n(.*?)^" + chr(96) * 3 + r"$", sections[2])
    if len(python_blocks) != 1:
        raise ValueError(f"{filename}: expected one complete Python code block, got {len(python_blocks)}")
    # Exactly one executable Python code listing in the entire handout.
    # Input datasets may use a csv/text block, but never another Python snippet.
    all_python_blocks = re.findall(
        r"(?ms)^" + chr(96) * 3 + r"python\n(.*?)^" + chr(96) * 3 + r"$",
        content
    )
    if len(all_python_blocks) != 1 or re.search(r"(?m)^~~~python\s*$", content):
        raise ValueError(f"{filename}: expected ONE complete Python program, with no example snippets")
    if "~~" in sections[3] and re.search(r"(?m)^~~~", sections[3]):
        raise ValueError(f"{filename}: duplicate code-like examples found in explanation")
    if len(sections[3]) < 1600:
        raise ValueError(f"{filename}: final explanation is too short to teach the solution")
    code = python_blocks[0]
    ast.parse(code, filename=filename)
    if re.search(r"(?m)^\s*assert\b", code):
        raise ValueError(f"{filename}: use if instead of assert in student code")
    if " # " not in code:
        raise ValueError(f"{filename}: Python code has no inline comments")
    useful_comment_lines = sum(" # " in line for line in code.splitlines())
    if useful_comment_lines >= 0.52 * len(code.splitlines()):
        raise ValueError(f"{filename}: notes are too dense for a focused study printout")

    # The code has enough substance to constitute the whole answer, not a placeholder.
    if len(code.splitlines()) < 35:
        raise ValueError(f"{filename}: suspiciously short complete Python solution")
    return sections, len(code.splitlines())

def render_pdf(path: Path):
    text = path.read_text(encoding="utf-8")
    _, code_lines = validate_source(text, path.name)
    markdown = mistune.create_markdown(escape=True, plugins=["table", "strikethrough"])
    if "columns: 1" not in CSS or "column-count: 1" not in CSS:
        raise ValueError("The print stylesheet must use ONE column across A4 landscape")
    html_body = markdown(text)
    document = '<!doctype html><html lang="vi"><head><meta charset="utf-8"><style>' + CSS + \
               '</style></head><body>' + html_body + '</body></html>'
    destination = PDF_DIR / (path.stem + ".pdf")
    HTML(string=document, base_url=path.parent.as_uri()).write_pdf(str(destination))
    with fitz.open(destination) as pdf:
        if len(pdf) == 0 or len(pdf) > 45:
            raise ValueError(f"Unexpected page count for {path.name}: {len(pdf)}")
        text = "\n".join(page.get_text() for page in pdf)
        if "Đề bài tiếng Anh" not in text or "Đề bài tiếng Việt" not in text or \
                "Code Python có chú thích" not in text or "Giải thích nội dung" not in text:
            raise ValueError(f"PDF lost a section for {path.name}")
        for index, page in enumerate(pdf):
            if page.rect.width <= page.rect.height:
                raise ValueError(f"Not A4 landscape: {destination}, page {index + 1}")
            if abs(page.rect.width - 841.9) > 2 or abs(page.rect.height - 595.3) > 2:
                raise ValueError(f"Unexpected page size: {page.rect}")
            for block in page.get_text("blocks"):
                x0,y0,x1,y1 = block[:4]
                if x0 < -1 or x1 > page.rect.width + 1 or y0 < -1 or y1 > page.rect.height + 1:
                    raise ValueError(f"PDF content clipped on {destination.name} page {index + 1}")
        print(f"PRINT_GUIDE_OK file={destination.name} pages={len(pdf)} code_lines={code_lines} bytes={destination.stat().st_size}")

def build():
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    if len(DOCUMENTS) != 10 or len(set(DOCUMENTS)) != 10:
        raise ValueError("Expected ten unique independent study guides")
    for name in DOCUMENTS:
        source = PRINT / name
        if not source.is_file():
            raise FileNotFoundError(source)
        render_pdf(source)
    pdf_count = len(list(PDF_DIR.glob("*.pdf")))
    if pdf_count != len(DOCUMENTS):
        raise ValueError(f"Expected {len(DOCUMENTS)} PDF outputs, got {pdf_count}")
    print(f"PRINT_BUNDLE_OK files={len(DOCUMENTS)} layout=A4-landscape")

if __name__ == "__main__":
    build()

#!/usr/bin/env python3
"""Render all 46 bilingual AIClassDocuments chapters to a preview PDF."""
from pathlib import Path
from urllib.parse import urlparse, unquote
import html
import re
import mistune
import fitz
from weasyprint import HTML
from latex2mathml.converter import convert as mathml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "exports/pdf/AIClassDocuments-PY01-PY46-PREVIEW.vi.pdf"
CHAPTERS = sorted((ROOT / "lessons/chapters").glob("PY-[0-9][0-9]-*.vi.md"))

CSS = """
@page { size:A4; margin:18mm 15mm 19mm; @bottom-center { content:counter(page); color:#687b90; font-size:8pt; } }
@page:first { @bottom-center { content:none; } }
html { font-family:'Noto Sans','DejaVu Sans',sans-serif; font-size:10pt; color:#182b43; }
body { line-height:1.5; overflow-wrap:anywhere; }
.cover { padding:70mm 6mm 0; text-align:center; break-after:page; }
.cover h1 { font-size:30pt; color:#154766; }
.cover p { color:#526d83; font-size:12pt; }
.toc { break-after:page; }
.toc p { font-size:9pt; margin:2mm 0; }
.chapter { break-before:page; }
h1 { font-size:19pt; color:#13466b; line-height:1.2; border-bottom:1.5pt solid #bad2e4; padding-bottom:3mm; }
h2 { font-size:14pt; color:#205d80; margin-top:7mm; break-after:avoid; }
h3 { font-size:11.5pt; color:#275978; margin-top:5mm; break-after:avoid; }
p { margin:2mm 0 3mm; }
ul,ol { padding-left:7mm; }
pre { white-space:pre-wrap; overflow-wrap:anywhere; background:#f1f5fa; padding:3mm; border:0.5pt solid #d6dfeb; font:8pt/1.38 'DejaVu Sans Mono',monospace; }
code { font-family:'DejaVu Sans Mono',monospace; font-size:0.88em; overflow-wrap:anywhere; }
pre code { font-size:inherit; }
table { border-collapse:collapse; table-layout:fixed; width:100%; font-size:8pt; margin:3mm 0; }
th,td { border:0.5pt solid #c8d5e0; padding:1.8mm 1.5mm; vertical-align:top; overflow-wrap:anywhere; word-break:break-word; }
th { background:#e8f2f9; color:#143951; }
tr { break-inside:avoid; }
img { max-width:100%; max-height:180mm; object-fit:contain; }
blockquote { border-left:2pt solid #a5bfd3; padding-left:3mm; color:#45596b; }
"""

class Renderer(mistune.HTMLRenderer):
    def __init__(self, folder):
        super().__init__(escape=True)
        self.folder = folder
    def image(self, text, url, title=None):
        parsed = urlparse(url)
        if parsed.scheme in ("http", "https", "data"):
            src = url
        elif not parsed.scheme:
            path = (self.folder / unquote(parsed.path)).resolve()
            if not path.is_file():
                raise FileNotFoundError("Lesson figure missing: " + str(path))
            src = path.as_uri()
        else:
            raise ValueError("Unsupported image scheme: " + url)
        return '<img src="' + html.escape(src, quote=True) + '" alt="' + html.escape(text or "", quote=True) + '"/>'

def render_math(latex, display):
    try:
        return mathml(latex, display="block" if display else "inline")
    except Exception:
        return '<code>' + html.escape(latex) + '</code>'

def build():
    if len(CHAPTERS) != 46:
        raise RuntimeError("Expected 46 chapters, found " + str(len(CHAPTERS)))
    body = ['<section class="cover"><h1>AIClassDocuments</h1><p>Giáo trình Python, Toán, Thống kê, Machine Learning và AI</p><p>46 chương · Song ngữ Anh - Việt</p><p>Bản xem trước để học tập và rà soát. Chưa phải chứng nhận học thuật độc lập.</p></section>',
            '<section class="toc"><h2>Mục lục / Contents</h2>']
    num_questions = 0
    for chapter in CHAPTERS:
        source = chapter.read_text(encoding="utf-8")
        heading = next((x.removeprefix("# ").strip() for x in source.splitlines() if x.startswith("# ")), chapter.stem)
        body.append('<p><b>' + html.escape(chapter.stem[:5]) + '</b> - ' + html.escape(heading) + '</p>')
    body.append("</section>")
    for chapter in CHAPTERS:
        source = chapter.read_text(encoding="utf-8")
        num_questions += len(re.findall(r"^\*\*Q\d+\.", source, flags=re.M))
        renderer = Renderer(chapter.parent)
        md = mistune.create_markdown(renderer=renderer, plugins=["table", "strikethrough", "math"])
        renderer.register("block_math", lambda _r, t: '<div class="mathblock">' + render_math(t, True) + '</div>')
        renderer.register("inline_math", lambda _r, t: render_math(t, False))
        body.append('<section class="chapter">' + md(source) + '</section>')
    if num_questions != 920:
        raise RuntimeError("Expected 920 multiple-choice questions, got " + str(num_questions))
    doc = '<!DOCTYPE html><html lang="vi"><head><meta charset="utf-8"><style>' + CSS + '</style></head><body>' + "".join(body) + '</body></html>'
    OUT.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=doc, base_url=ROOT.as_uri()).write_pdf(str(OUT))
    pdf = fitz.open(OUT)
    if len(pdf) < 46 or OUT.stat().st_size < 50000:
        raise RuntimeError("Generated PDF failed basic file/page preflight")
    extracted = "\n".join(page.get_text() for page in pdf)
    for no in [1, 10, 20, 30, 40, 46]:
        if "PY-" + str(no).zfill(2) not in extracted:
            raise RuntimeError("Missing chapter in rendered PDF: " + str(no))
    if "Trắc nghiệm" not in extracted or "Giải thích" not in extracted:
        raise RuntimeError("Required bilingual content missing from PDF")
    print("PDF_EXPORTED", OUT, "chapters=46", "questions=920", "pages=", len(pdf), "bytes=", OUT.stat().st_size)

if __name__ == "__main__":
    build()

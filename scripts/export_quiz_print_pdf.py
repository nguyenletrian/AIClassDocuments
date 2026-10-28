#!/usr/bin/env python3
"""Generate dense A4 landscape print edition of 936 existing MCQs."""
from pathlib import Path
import re
import fitz
import mistune
from weasyprint import HTML

ROOT=Path(__file__).resolve().parents[1]
ORIGINAL=ROOT/"exports/markdown/AIClassDocuments-920-TracNghiem-PY01-PY46.vi.md"
ADDED=ROOT/"exports/markdown/AIClassDocuments-16-CauBoSung-20261028.vi.md"
COMBINED=ROOT/"exports/markdown/AIClassDocuments-936-TracNghiem-PY01-PY46.vi.md"
OUTPUT=ROOT/"exports/pdf/AIClassDocuments-936-TracNghiem-A4-Ngang-2Cot.vi.pdf"

def build():
    original=ORIGINAL.read_text(encoding="utf-8")
    added=ADDED.read_text(encoding="utf-8")
    base=original.replace("Bộ 920 câu","Bộ 936 câu",1)
    combined=base.rstrip()+"\n\n## BỔ SUNG — 16 câu mới\n\n"+added.split("\n",1)[1].strip()+"\n"
    if len(re.findall(r"(?m)^\\*\\*Q\\d+\\.",combined))!=936:
        raise ValueError("Total question count differs from 936")
    COMBINED.write_text(combined,encoding="utf-8")
    md=mistune.create_markdown(plugins=["table"])
    sections=re.split(r"(?=^## (?:PY-\\d\\d|BỔ SUNG))",combined,flags=re.M)
    html_parts=[]
    for section in sections[1:]:
        title,_,body=section.partition("\n")
        items=re.split(r"(?=^\\*\\*Q\\d+\\.)",body,flags=re.M)
        html_parts.append("<h2>"+md(title.removeprefix("## ").strip())+"</h2>")
        html_parts.append('<div class="intro">'+md(items[0])+"</div>")
        for q in items[1:]:
            html_parts.append('<div class="question">'+md(q)+"</div>")
    css="""@page {size:A4 landscape;margin:7mm 8mm 9mm;@bottom-center{content:counter(page);font:7pt 'Noto Sans';}} body{font:7.8pt/1.16 'Noto Sans',sans-serif;columns:2;column-gap:7mm;overflow-wrap:anywhere;} h2{font-size:9pt;break-after:avoid;margin:2mm 0 1mm;} .intro{font-size:7pt;color:#555;} .question{break-inside:avoid;margin-bottom:1.5mm;border-bottom:.2pt solid #ccc;padding-bottom:1mm;} .question p{margin:0 0 .4mm;} .question p:first-child{font-weight:600;} .question p:last-child{font-size:7.3pt;} code{font-family:'DejaVu Sans Mono';font-size:.9em;}"""
    html_doc='<html lang="vi"><meta charset="utf-8"><style>'+css+'</style><body>'+"".join(html_parts)+"</body></html>"
    HTML(string=html_doc,base_url=ROOT.as_uri()).write_pdf(str(OUTPUT))
    pdf=fitz.open(OUTPUT)
    if not 35<len(pdf)<200 or any(p.rect.width<p.rect.height for p in pdf):
        raise ValueError("Invalid PDF length or orientation")
    print(f"QUIZ_PRINT_OK questions=936 pages={len(pdf)} bytes={OUTPUT.stat().st_size}")

if __name__=="__main__":
    build()

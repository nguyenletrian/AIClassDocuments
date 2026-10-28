#!/usr/bin/env python3
"""Generate dense A4 landscape print edition of 936 existing MCQs."""
from pathlib import Path
import re
import html
import fitz
import mistune
from weasyprint import HTML

ROOT=Path(__file__).resolve().parents[1]
ORIGINAL=ROOT/"exports/markdown/AIClassDocuments-920-TracNghiem-PY01-PY46.vi.md"
ADDED=ROOT/"exports/markdown/AIClassDocuments-16-CauBoSung-20261028.vi.md"
COMBINED=ROOT/"exports/markdown/AIClassDocuments-936-TracNghiem-PY01-PY46.vi.md"
OUTPUT=ROOT/"exports/pdf/AIClassDocuments-936-TracNghiem-A4-Ngang-2Cot.vi.pdf"


def inline_html(md, value):
    """Render one Markdown fragment without creating an extra paragraph."""
    rendered = md(value.strip()).strip()
    if rendered.startswith("<p>") and rendered.endswith("</p>"):
        return rendered[3:-4]
    return rendered


def question_html(md, question):
    """One question; answer and rationale share a single paragraph."""
    lines = [line.strip() for line in question.splitlines() if line.strip()]
    if not lines or not lines[0].startswith("**Q"):
        raise ValueError("Question heading is missing")
    choices = re.findall(r"(?m)^([ABCD])\. (.+)$", question)
    if [label for label, _ in choices] != list("ABCD"):
        raise ValueError("Each question must contain choices A through D")
    match = re.search(r"(?m)^\*\*Đáp án: ([ABCD])\*\*$", question)
    if match is None or "**Giải thích:**" not in question:
        raise ValueError("Question is missing answer or explanation")
    answer = match.group(1)
    explanation = question.split("**Giải thích:**", 1)[1].strip()

    # Inline only when four options fit comfortably in one half-page column.
    visible = [
        html.unescape(re.sub(r"[\x60*_]", "", text_value))
        for _, text_value in choices
    ]
    compact = max(map(len, visible)) <= 22 and sum(map(len, visible)) <= 68
    choice_class = "choices short" if compact else "choices"
    choice_html = "".join(
        '<span class="choice"><b>' + label + ".</b> " + inline_html(md, value) + "</span>"
        for label, value in choices
    )
    return (
        '<article class="question">'
        '<p class="stem">' + inline_html(md, lines[0]) + "</p>"
        '<div class="' + choice_class + '">' + choice_html + "</div>"
        '<p class="answer"><strong>Đáp án ' + answer + ":</strong> "
        + inline_html(md, explanation) + "</p>"
        "</article>"
    )


def build():
    original=ORIGINAL.read_text(encoding="utf-8")
    added=ADDED.read_text(encoding="utf-8")
    base=original.replace("Bộ 920 câu","Bộ 936 câu",1)
    combined=base.rstrip()+"\n\n## BỔ SUNG — 16 câu mới\n\n"+added.split("\n",1)[1].strip()+"\n"
    if len(re.findall(r"(?m)^\*\*Q\d+\.",combined))!=936:
        raise ValueError("Total question count differs from 936")
    COMBINED.write_text(combined,encoding="utf-8")
    md=mistune.create_markdown(plugins=["table"])
    sections=re.split(r"(?=^## (?:PY-\d\d|BỔ SUNG))",combined,flags=re.M)
    html_parts=[]
    for section in sections[1:]:
        title,_,body=section.partition("\n")
        items=re.split(r"(?=^\*\*Q\d+\.)",body,flags=re.M)
        lesson_title = title.removeprefix("## ").strip()
        lesson_title = re.sub(r"^(PY-\d\d) — \1 — ", r"\1 — ", lesson_title)
        html_parts.append("<h2>"+html.escape(lesson_title)+"</h2>")
        intro = re.sub(r"(?m)^\*\*Từ vựng trong mục:\*\*[^\n]*", "", items[0]).strip()
        if intro:
            html_parts.append('<div class="intro">'+md(intro)+"</div>")
        for q in items[1:]:
            if q.strip():
                html_parts.append(question_html(md, q))
    css="""@page {
      size:A4 landscape;
      margin:7mm 8mm 9mm;
      @bottom-center {content:counter(page);font:7pt 'Noto Sans';}
    }
    body {font:7.9pt/1.19 'Noto Sans',sans-serif;
          columns:2;column-gap:7mm;overflow-wrap:anywhere;}
    h2 {font-size:9.6pt;font-weight:700;color:#153b5c;
        background:#e8eef5;padding:1.15mm 1.6mm;
        break-after:avoid; margin:2.2mm 0 1.3mm;}
    .intro {font-size:7pt;color:#555;margin:0 0 1mm;}
    .question {break-inside:avoid;margin:0 0 1.2mm;padding:0;}
    .question .stem {font-weight:600;margin:0 0 .48mm;}
    .choices {margin:0 0 .4mm;}
    .choice {display:block;margin:0 0 .12mm;}
    .choices.short {display:grid;grid-template-columns:repeat(4,minmax(0,1fr));
                    column-gap:1.4mm;}
    .choices.short .choice {display:block;white-space:nowrap;}
    .answer {margin:0;font-size:7.55pt;color:#333;}
    .answer strong {color:#151515;}
    code {font-family:'DejaVu Sans Mono';font-size:.9em;}
    """
    html_doc='<html lang="vi"><meta charset="utf-8"><style>'+css+'</style><body>'+"".join(html_parts)+"</body></html>"
    HTML(string=html_doc,base_url=ROOT.as_uri()).write_pdf(str(OUTPUT))
    pdf=fitz.open(OUTPUT)
    if not 30<len(pdf)<200 or any(p.rect.width<p.rect.height for p in pdf):
        raise ValueError("Invalid PDF length or orientation")
    if html_doc.count('<article class="question">') != 936:
        raise ValueError("Rendered question count mismatch")
    if html_doc.count('<p class="answer"><strong>Đáp án ') != 936:
        raise ValueError("Rendered inline answer count mismatch")
    if html_doc.count('class="choices short"') < 1:
        raise ValueError("Short choices were not placed on a single row")
    if "Từ vựng trong mục" in html_doc or "Giải thích:" in html_doc:
        raise ValueError("Unwanted print-only labels still present")
    print(f"QUIZ_PRINT_OK questions=936 pages={len(pdf)} inline_choice_questions={html_doc.count('class=' + chr(34) + 'choices short' + chr(34))} bytes={OUTPUT.stat().st_size}")

if __name__=="__main__":
    build()

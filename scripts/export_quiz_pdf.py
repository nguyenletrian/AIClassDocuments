#!/usr/bin/env python3
"""Collect every chapter's section 7 MCQs and render a bilingual PDF."""
from __future__ import annotations

import html
import re
from pathlib import Path

import fitz
import mistune
from weasyprint import HTML

ROOT = Path(__file__).resolve().parents[1]
CHAPTER_DIR = ROOT / "lessons" / "chapters"
OUTPUT_PDF = ROOT / "exports" / "pdf" / "AIClassDocuments-920-TracNghiem-PY01-PY46.vi.pdf"
OUTPUT_MD = ROOT / "exports" / "markdown" / "AIClassDocuments-920-TracNghiem-PY01-PY46.vi.md"
EXPECTED_QUESTIONS = 46 * 20

CSS = """
@page { size: A4; margin: 18mm 17mm 18mm;
        @bottom-center { content: "AIClassDocuments · Trắc nghiệm   |   " counter(page);
                         font: 8pt 'Noto Sans', sans-serif; color: #637990; } }
@page:first { @bottom-center { content: none; } }
html { font-family: 'Noto Sans', 'DejaVu Sans', sans-serif; font-size: 10pt; color: #162d43; }
body { line-height: 1.55; overflow-wrap: anywhere; }
.cover { text-align: center; padding: 67mm 5mm 0; break-after: page; }
.cover h1 { font-size: 27pt; color: #164e76; border: none; }
.cover .lead { font-size: 14pt; color: #4b6f88; }
.toc { break-after: page; }
.toc h2 { margin-bottom: 8mm; }
.toc ul { columns: 2; padding-left: 6mm; column-gap: 8mm; }
.toc li { break-inside: avoid; margin: 0 0 2.5mm; font-size: 8.7pt; }
a { color: #1d6087; text-decoration: none; }
.lesson { break-before: page; }
.lesson h2 { color: #195879; font-size: 16pt; border-bottom: 1.2pt solid #bbd5e5;
             padding-bottom: 3mm; margin-bottom: 4mm; }
.lesson h3 { color: #245a7a; }
.question { break-inside: avoid; border-bottom: .45pt solid #d6e1eb;
            padding: 3mm 1.5mm 3.6mm; margin: 0 0 2.4mm; }
.question p { margin: 0 0 2mm; }
.question p:first-child { color: #143e5e; font-weight: 600; }
.question p:nth-last-child(2) { color: #165e3d; }
.question p:last-child { color: #45596c; }
code { font-family: 'DejaVu Sans Mono', monospace; font-size: .88em; overflow-wrap: anywhere; }
pre { font: 8.5pt 'DejaVu Sans Mono', monospace; white-space: pre-wrap; }
.lesson-intro { margin: 0 0 5mm; color: #546b81; font-size: 9pt; }
"""

def extract_quiz(source: str, path: Path) -> tuple[str, list[str]]:
    match = re.search(r"^## 7\. Trắc nghiệm\s*$([\s\S]*?)(?=^## 8\.|\Z)", source, re.M)
    if not match:
        raise ValueError(f"Missing section 7 quiz: {path.name}")
    body = match.group(1).strip()
    questions = re.findall(r"^\*\*Q(\d+)\.", body, re.M)
    if questions != [str(i) for i in range(1, 21)]:
        raise ValueError(f"Expected Q1..Q20 in order: {path.name}: {questions}")
    if len(re.findall(r"^\*\*Đáp án: [A-D]\*\*", body, re.M)) != 20:
        raise ValueError(f"Expected 20 answer keys: {path.name}")
    if len(re.findall(r"^\*\*Giải thích:\*\*", body, re.M)) != 20:
        raise ValueError(f"Expected 20 explanations: {path.name}")
    chunks = re.split(r"(?=^\*\*Q\d+\.)", body, flags=re.M)
    intro = chunks[0].strip()
    quizzes = [c.strip() for c in chunks[1:] if c.strip()]
    if len(quizzes) != 20:
        raise ValueError(f"Split failure: {path.name}")
    for q_num, q in enumerate(quizzes, 1):
        options = re.findall(r"^([ABCD])\. ", q, flags=re.M)
        if options != ["A", "B", "C", "D"]:
            raise ValueError(f"Expected options A-D for Q{q_num}: {path.name}")
        if len(re.findall(r"^\*\*Đáp án: [A-D]\*\*", q, re.M)) != 1:
            raise ValueError(f"Expected one answer for Q{q_num}: {path.name}")
        if len(re.findall(r"^\*\*Giải thích:\*\*", q, re.M)) != 1:
            raise ValueError(f"Expected one explanation for Q{q_num}: {path.name}")
    return intro, quizzes

def build() -> None:
    files = sorted(CHAPTER_DIR.glob("PY-[0-9][0-9]-*.vi.md"))
    ids = [f.name[:5] for f in files]
    expected = [f"PY-{i:02d}" for i in range(1, 47)]
    if ids != expected:
        raise ValueError(f"Expected exactly 46 ordered chapters, got {ids}")
    md = mistune.create_markdown(plugins=["table", "strikethrough", "math"])
    md_parts = [
        "# AIClassDocuments — Bộ 920 câu trắc nghiệm Python và AI",
        "",
        "46 bài PY-01–PY-46 · Song ngữ Anh–Việt · Có đáp án và giải thích.",
        "",
        "Nội dung được trích nguyên văn từ mục 7 của từng bài trên nhánh main, không viết lại câu hỏi hay đáp án.",
        "",
    ]
    toc = []
    pdf_lessons = []
    total = 0
    for i, path in enumerate(files, 1):
        source = path.read_text(encoding="utf-8")
        heading = next((s.removeprefix("# ").strip() for s in source.splitlines() if s.startswith("# ")), path.stem)
        intro, quizzes = extract_quiz(source, path)
        total += len(quizzes)
        name = f"PY-{i:02d}"
        toc.append(f'<li><a href="#{name}">{html.escape(name)} · {html.escape(heading)}</a></li>')
        md_parts.extend([f"## {name} — {heading}", "", intro, ""])
        for question in quizzes:
            md_parts.extend([question, ""])
        intro_html = '<div class="lesson-intro">' + md(intro) + '</div>' if intro else ''
        quiz_html = "".join('<section class="question">' + md(q) + '</section>' for q in quizzes)
        pdf_lessons.append(f'<section class="lesson" id="{name}"><h2>{html.escape(name)} — {html.escape(heading)}</h2>{intro_html}{quiz_html}</section>')
    if total != EXPECTED_QUESTIONS:
        raise ValueError(f"Expected {EXPECTED_QUESTIONS} questions; got {total}")
    OUTPUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PDF.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_MD.write_text("\n".join(md_parts).rstrip() + "\n", encoding="utf-8")
    cover = '<section class="cover"><h1>AIClassDocuments</h1><p class="lead">920 CÂU TRẮC NGHIỆM PYTHON VÀ AI</p><p>46 bài học · Song ngữ Anh–Việt</p><p>Gồm 4 lựa chọn, đáp án và giải thích ngay dưới từng câu</p></section>'
    toc_html = '<section class="toc"><h2>Mục lục · 46 bài học</h2><ul>' + "".join(toc) + '</ul></section>'
    document = '<!doctype html><html lang="vi"><head><meta charset="utf-8"><style>' + CSS + '</style></head><body>' + cover + toc_html + "".join(pdf_lessons) + '</body></html>'
    HTML(string=document, base_url=ROOT.as_uri()).write_pdf(str(OUTPUT_PDF))
    pdf = fitz.open(OUTPUT_PDF)
    if len(pdf) < 90 or OUTPUT_PDF.stat().st_size < 100_000:
        raise AssertionError("PDF appears incomplete")
    text = "\n".join(page.get_text() for page in pdf)
    for n in (1, 10, 20, 30, 40, 46):
        if f"PY-{n:02d}" not in text:
            raise AssertionError(f"Missing rendered chapter PY-{n:02d}")
    if "Giải thích" not in text or "Trắc nghiệm" not in text or "Đáp án" not in text:
        raise AssertionError("Required bilingual quiz text missing in PDF")
    print(f"QUIZ_EXPORT_OK chapters=46 questions={total} pages={len(pdf)} bytes={OUTPUT_PDF.stat().st_size}")
    print(OUTPUT_PDF)
    print(OUTPUT_MD)

if __name__ == "__main__":
    build()

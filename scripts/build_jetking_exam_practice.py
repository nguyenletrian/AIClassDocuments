#!/usr/bin/env python3
"""Curate 10 × 16 bilingual AI-foundation practice exams from approved course MCQs.

The 16 questions supplied by the student form mock 1. The remaining nine
mocks use unique questions from approved PY-24..PY-37 lessons. This is NOT
a claimed official FPT Jetking paper or specification.
"""
from __future__ import annotations

import html
import re
from pathlib import Path

import fitz
import mistune
from weasyprint import HTML

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "exports/markdown/AIClassDocuments-936-TracNghiem-PY01-PY46.vi.md"
OUT_MD = ROOT / "exports/markdown/AIClassDocuments-FPT-Jetking-10-DeOnTap-160Cau.vi.md"
OUT_TEST = ROOT / "exports/pdf/AIClassDocuments-FPT-Jetking-10-DeOnTap-160Cau-A4-Ngang.vi.pdf"
OUT_SOLUTIONS = ROOT / "exports/pdf/AIClassDocuments-FPT-Jetking-DapAn-GiaiThich-160Cau-A4-Ngang.vi.pdf"

# Nine unique question IDs from each corresponding lesson, matching the
# relative position of the student's 16-question reference mock.
PLAN = [
    ("PY-24", [9, 11, 12, 13, 10, 16, 17, 18, 19], "Vector, tích vô hướng"),
    ("PY-25", [1, 3, 5, 6, 7, 8, 9, 17, 18], "Ma trận, nhân ma trận"),
    ("PY-26", [5, 13, 12, 16, 14, 18, 15, 11, 19], "Hệ phương trình tuyến tính"),
    ("PY-25", [4, 10, 11, 12, 13, 14, 15, 16, 20], "Định thức, nghịch đảo"),
    ("PY-31", [9, 10, 11, 12, 14, 15, 17, 18, 19], "Đạo hàm"),
    ("PY-33", [3, 9, 10, 11, 13, 14, 15, 16, 20], "Đạo hàm và cực trị"),
    ("PY-32", [6, 9, 10, 11, 12, 17, 18, 19, 20], "Gradient Descent, cập nhật tham số"),
    ("PY-32", [1, 2, 3, 4, 5, 7, 8, 13, 14], "Learning rate và gradient"),
    ("PY-34", [5, 6, 7, 8, 9, 10, 11, 12, 13], "Xác suất cơ bản"),
    ("PY-34", [1, 2, 3, 4, 14, 15, 16, 18, 19], "Biến cố đối, xác suất"),
    ("PY-37", [1, 2, 5, 9, 10, 15, 16, 17, 18], "Mean, median, mode"),
    ("PY-36", [3, 10, 11, 13, 14, 16, 18, 19, 20], "Phân phối, chuẩn hóa và xác suất"),
    ("PY-35", [1, 3, 5, 7, 9, 10, 11, 12, 13], "Xác suất có điều kiện, Bayes"),
    ("PY-27", [3, 4, 9, 12, 13, 14, 18, 19, 20], "Eigenvalue và PCA"),
    ("PY-30", [1, 6, 7, 9, 13, 14, 15, 18, 19], "Loss và đánh giá sai số"),
    ("PY-35", [2, 6, 8, 14, 15, 16, 17, 18, 20], "Biến cố độc lập"),
]
TOPICS = [row[2] for row in PLAN]
TOTAL_MOCKS = 10
QUESTIONS_PER_MOCK = 16

CSS = """
@page {
    size: A4 landscape;
    margin: 7.5mm 8mm 9mm;
    @bottom-center {
        content: counter(page);
        font: 7pt 'Noto Sans';
    }
}
body {
    font: 8.25pt/1.2 'Noto Sans', 'DejaVu Sans', sans-serif;
    color: #1b2730;
    columns: 2;
    column-gap: 8mm;
    overflow-wrap: anywhere;
}
h2 {
    font-size: 10.1pt;
    background: #e5edf5;
    color: #17364e;
    padding: 1.4mm 1.7mm;
    margin: 3mm 0 1.3mm;
    break-after: avoid;
}
h3 {
    font-size: 8.5pt;
    margin: 0 0 1.2mm;
}
.tip { font-size: 7.6pt; margin: 0 0 2mm; color: #34485b; }
.question { break-inside: avoid; margin: 0 0 1.7mm; }
.question p { margin: 0 0 .5mm; }
.question .stem { font-weight: 650; }
.choices { margin: 0 0 .4mm; }
.choice { display: block; margin-bottom: .22mm; }
.choices.short { display: grid; grid-template-columns: repeat(4,minmax(0,1fr)); gap: 1mm; }
.choices.short .choice { white-space: nowrap; }
.answer { font-size: 7.8pt; color: #293b48; }
code { font-family: 'DejaVu Sans Mono', monospace; font-size: .87em; }
"""

def load_questions(content: str):
    bank: dict[str, dict[int, str]] = {}
    for section in re.split(r"(?=^## (?:PY-\d\d|BỔ SUNG))", content, flags=re.M)[1:]:
        title = section.splitlines()[0]
        key = re.match(r"^## (PY-\d\d|BỔ SUNG)", title).group(1)
        items = re.split(r"(?=^\*\*Q\d+\.)", section, flags=re.M)[1:]
        bank[key] = {}
        for q in items:
            match = re.match(r"\*\*Q(\d+)\.", q)
            if match:
                bank[key][int(match.group(1))] = q.strip()
    return bank

def inspect_question(q: str):
    opts = re.findall(r"(?m)^([ABCD])\. (.+)$", q)
    key = re.findall(r"(?m)^\*\*Đáp án: ([ABCD])\*\*$", q)
    explanations = q.split("**Giải thích:**", 1)
    if [a for a, _ in opts] != list("ABCD") or len(key) != 1 or len(explanations) != 2:
        raise ValueError("A-D, correct key, or explanation missing in MCQ: " + q[:100])
    if any(not t.strip() for _, t in opts) or not explanations[1].strip():
        raise ValueError("Empty option/explanation")
    return opts, key[0], explanations[1].strip()

def prepare_mocks(bank):
    if len(bank.get("BỔ SUNG", {})) != 16:
        raise ValueError("The original 16-question sample is missing")
    mocks = []
    reference = [bank["BỔ SUNG"][i] for i in range(1, 17)]
    mocks.append(reference)
    seen = set()
    for exam_idx in range(9):
        items = []
        for lesson, indices, _topic in PLAN:
            idx = indices[exam_idx]
            identity = (lesson, idx)
            if identity in seen:
                raise ValueError(f"Duplicate bank question {identity}")
            seen.add(identity)
            items.append(bank[lesson][idx])
        mocks.append(items)
    if len(mocks) != TOTAL_MOCKS or any(len(m) != QUESTIONS_PER_MOCK for m in mocks):
        raise ValueError("Mock count is wrong")
    for mock in mocks:
        for q in mock:
            inspect_question(q)
    return mocks

def renumber(q, index):
    return re.sub(r"^\*\*Q\d+\.", f"**Q{index}.", q, count=1)

def render_inline(md, text):
    h = md(text).strip()
    return h[3:-4] if h.startswith("<p>") and h.endswith("</p>") else h

def render_question(md, q, include_answer):
    parts = re.split(r"\n", q.strip())
    opts, key, explanation = inspect_question(q)
    question_text = parts[0]
    options_text = [html.unescape(re.sub(r"[\x60*_]", "", content)) for _, content in opts]
    short = max(map(len, options_text)) <= 23 and sum(map(len, options_text)) <= 74
    div_class = "choices short" if short else "choices"
    html_options = "".join(
        '<span class="choice"><b>' + letter + ".</b> " + render_inline(md, option) + "</span>"
        for letter, option in opts
    )
    answer_html = (
        '<p class="answer"><strong>Đáp án ' + key + ':</strong> '
        + render_inline(md, explanation) + '</p>' if include_answer else ''
    )
    return (
        '<article class="question"><p class="stem">' + render_inline(md, question_text)
        + '</p><div class="' + div_class + '">' + html_options
        + '</div>' + answer_html + '</article>'
    )

def make_html(mocks, include_answer):
    md = mistune.create_markdown(escape=True)
    contents = []
    for n, mock in enumerate(mocks, 1):
        contents.append('<h2>ĐỀ ' + str(n).zfill(2) +
                        (' · 16 câu tham chiếu' if n == 1 else ' · 16 câu ôn tập') + '</h2>')
        contents.append('<p class="tip">Chuyên đề: ' +
                        'vector · ma trận · đạo hàm · Gradient Descent · xác suất · thống kê · PCA' +
                        '. Thời gian tự luyện: khoảng 9 phút (không phải thời lượng thi chính thức).</p>')
        for idx, q in enumerate(mock, 1):
            contents.append(render_question(md, renumber(q, idx), include_answer))
    content = ''.join(contents)
    if content.count('<article class="question">') != TOTAL_MOCKS * QUESTIONS_PER_MOCK:
        raise ValueError("Lost a rendered question")
    if include_answer and content.count('class="answer"') != 160:
        raise ValueError("Lost an answer")
    if not include_answer and 'class="answer"' in content:
        raise ValueError("Answer leaked into exam-only version")
    return (
        '<!doctype html><html lang="vi"><meta charset="utf-8"><style>'
        + CSS + '</style><body>' + content + '</body></html>'
    )

def make_markdown(mocks):
    lines = [
        "# Bộ đề ôn tập nền tảng AI theo 16 câu mẫu FPT Jetking",
        "",
        "**Lưu ý:** Đây là tài liệu luyện tập do AIClassDocuments biên soạn từ bộ 936 câu đã có,",
        "không phải đề thi chính thức hay dự đoán chính xác câu hỏi sẽ xuất hiện.",
        "Đề 01 giữ nguyên 16 câu mẫu đã cung cấp; Đề 02–10 lấy 144 câu riêng biệt",
        "từ các bài PY-24–PY-37, ưu tiên toán, tối ưu hóa, xác suất và thống kê.",
        "",
        "**Cách làm:** Mỗi đề gồm 16 câu, 4 lựa chọn, mỗi câu 1 điểm; tự đặt khoảng 9 phút",
        "để luyện tốc độ theo các câu mẫu. Đáp án và giải thích được giữ bên dưới mỗi câu.",
        "",
    ]
    for num, mock in enumerate(mocks, 1):
        lines.extend([f"## Đề {num:02d} — 16 câu", ""])
        for index, q in enumerate(mock, 1):
            lines.extend([renumber(q, index), ""])
    return "\n".join(lines).rstrip() + "\n"

def build():
    source = SOURCE.read_text(encoding="utf-8")
    bank = load_questions(source)
    mocks = prepare_mocks(bank)
    markdown = make_markdown(mocks)
    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_TEST.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.write_text(markdown, encoding="utf-8")
    for output, with_answers in [(OUT_TEST, False), (OUT_SOLUTIONS, True)]:
        HTML(string=make_html(mocks, with_answers), base_url=ROOT.as_uri()).write_pdf(str(output))
        with fitz.open(output) as pdf:
            if len(pdf) < 3 or len(pdf) > 70 or any(page.rect.width < page.rect.height for page in pdf):
                raise ValueError("Unexpected pages / page orientation: " + str(output))
            all_text = "\n".join(p.get_text() for p in pdf)
            if "ĐỀ 10" not in all_text or "ĐỀ 01" not in all_text:
                raise ValueError("First/last exam missing: " + str(output))
            print(f"JETKING_MOCK_OK file={output.name} pages={len(pdf)} bytes={output.stat().st_size}")
    print("JETKING_BUNDLE_OK exams=10 questions=160 reference=16 selected=144 topics=16")

if __name__ == "__main__":
    build()

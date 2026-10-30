#!/usr/bin/env python3
"""Merge all ten print-ready lab PDFs into one searchable A4 landscape book.

The original PDFs are inserted without reflow, preserving their single-column
code, bilingual questions, worked solutions, and definitions. This generator
runs after scripts/export_lab_print_pdf.py in the same GitHub Actions workflow.
"""
from __future__ import annotations

import html
from pathlib import Path

import fitz
from weasyprint import HTML

ROOT = Path(__file__).resolve().parents[1]
PDF_DIR = ROOT / "exports" / "print" / "pdf"
OUTPUT = PDF_DIR / "AIClassDocuments-TongHop-10-Lab-BaiTap-A4-Ngang.pdf"

# Deliberately match the sequence in export_lab_print_pdf.py and README.md.
CHAPTERS = [
    ("ASSIGNMENT-01", "Assignment 01", "Dictionary - Quan ly sinh vien"),
    ("LAB-04", "Lab 04", "Dieu kien va vong lap"),
    ("LAB-05", "Lab 05", "Danh sach sinh vien"),
    ("LAB-05-06", "Lab 05-06", "Hoi quy va Gradient Descent"),
    ("LAB-07", "Lab 07", "Xac suat va Bayes"),
    ("LAB-08", "Lab 08", "Thong ke va kiem dinh"),
    ("LAB-10", "Lab 10", "CSV va phan tich diem"),
    ("PRETEST", "Pretest", "On tap tong hop"),
    ("LAB-MATH-02", "Math 02", "Tap hop, Jaccard va do thi"),
    ("LAB-MATH-03-04", "Math 03-04", "Ma tran va PCA"),
]
SECTIONS = (
    "Đề bài tiếng Anh",
    "Đề bài tiếng Việt",
    "Code Python có chú thích",
    "Giải thích nội dung và cách giải",
    "Giải thích các định nghĩa",
)

COVER_CSS = """
@page { size: A4 landscape; margin: 15mm 18mm 12mm; }
html, body { margin: 0; }
body { font-family: 'Noto Sans', 'DejaVu Sans', sans-serif;
       color: #213348; font-size: 10pt; column-count: 1; }
h1 { font-size: 24pt; margin: 0 0 2mm; color: #183d5d; }
.subtitle { color: #506275; font-size: 10pt; margin-bottom: 7mm; }
h2 { font-size: 13pt; color: #183d5d; margin: 0 0 3mm; }
table { width: 100%; border-collapse: collapse; table-layout: fixed; }
th, td { padding: 2.3mm 2.5mm; border-bottom: 0.6pt solid #d5dee8;
         text-align: left; vertical-align: middle; }
th { font-size: 9pt; background: #edf3f7; color: #193a57; }
td { font-size: 9pt; }
.num { width: 7%; text-align: center; }
.code { width: 20%; font-weight: bold; }
.title { width: 53%; }
.pages { width: 20%; text-align: right; }
.footer { margin-top: 5mm; color: #5c6977; font-size: 8pt; }
"""

def _require_a4_landscape(pdf: fitz.Document, filename: str) -> None:
    if not pdf.page_count:
        raise ValueError(f"{filename}: empty PDF")
    for page in pdf:
        if page.rect.width <= page.rect.height or \
                abs(page.rect.width - 841.89) > 2 or \
                abs(page.rect.height - 595.28) > 2:
            raise ValueError(f"{filename}: page {page.number+1} is not A4 landscape")

def _section_offsets(pdf: fitz.Document, filename: str) -> list[int]:
    page_text = [page.get_text("text") for page in pdf]
    found = []
    for section in SECTIONS:
        offset = next((i for i, text in enumerate(page_text) if section in text), None)
        if offset is None:
            raise ValueError(f"{filename}: missing section {section}")
        found.append(offset)
    if found != sorted(found):
        raise ValueError(f"{filename}: study sections are out of order")
    return found

def _toc_cover(chapters: list[dict]) -> bytes:
    rows = []
    for i, item in enumerate(chapters, 1):
        title = html.escape(item["title"])
        subject = html.escape(item["subject"])
        rows.append(
            f'<tr><td class="num">{i:02d}</td>'
            f'<td class="code">{title}</td>'
            f'<td class="title">{subject}</td>'
            f'<td class="pages">{item["start"]}–{item["end"]}</td></tr>'
        )
    body = f"""<!doctype html><html lang="vi"><head><meta charset="utf-8">
    <style>{COVER_CSS}</style></head><body>
    <h1>Bộ tài liệu Lab &amp; Bài tập</h1>
    <div class="subtitle">AIClassDocuments · Bản tổng hợp để in · A4 ngang, một cột · 10 bài</div>
    <h2>Mục lục</h2>
    <table><thead><tr><th class="num">STT</th><th class="code">Bài</th>
    <th class="title">Nội dung</th><th class="pages">Trang</th>
    </tr></thead><tbody>{''.join(rows)}</tbody></table>
    <div class="footer">Mỗi bài gồm: đề tiếng Anh, đề tiếng Việt, một chương trình Python,
    giải thích cách giải và giải thích các định nghĩa. Có thể dùng dấu trang
    (Bookmarks) trong trình đọc PDF để chuyển nhanh đến từng mục.</div>
    </body></html>"""
    return HTML(string=body).write_pdf()

def build() -> Path:
    if len(CHAPTERS) != 10 or len({x[0] for x in CHAPTERS}) != 10:
        raise ValueError("Expected exactly ten distinct study guides")

    chapters = []
    # Page 1 is the cover/index, therefore the first source starts at page 2.
    next_page = 2
    for stem, title, subject in CHAPTERS:
        source = PDF_DIR / (stem + ".pdf")
        if not source.is_file():
            raise FileNotFoundError(f"Missing source PDF: {source}")
        with fitz.open(source) as pdf:
            _require_a4_landscape(pdf, stem)
            offsets = _section_offsets(pdf, stem)
            pages = len(pdf)
        chapters.append({
            "stem": stem, "title": title, "subject": subject,
            "start": next_page, "end": next_page + pages - 1,
            "pages": pages, "offsets": offsets,
        })
        next_page += pages

    cover_bytes = _toc_cover(chapters)
    with fitz.open(stream=cover_bytes, filetype="pdf") as cover:
        if cover.page_count != 1:
            raise ValueError(f"Index must be one page; got {cover.page_count}")
        _require_a4_landscape(cover, "cover")
        book = fitz.open()
        book.insert_pdf(cover)

    bookmarks = [[1, "Mục lục", 1]]
    for item in chapters:
        with fitz.open(PDF_DIR / (item["stem"] + ".pdf")) as source:
            start_index = book.page_count
            book.insert_pdf(source, links=True, annots=True)
            bookmarks.append([1, item["title"] + " - " + item["subject"],
                              start_index + 1])
            for section, offset in zip(SECTIONS, item["offsets"]):
                bookmarks.append([2, section, start_index + offset + 1])

    book.set_toc(bookmarks)
    book.set_metadata({
        "title": "AIClassDocuments - Tong hop 10 Lab va Bai tap",
        "author": "AIClassDocuments",
        "subject": "Ten bilingual study handouts, solutions and definitions",
        "keywords": "lab, bai tap, pretest, Python, probability, statistics",
    })
    if book.page_count != next_page - 1:
        raise ValueError(f"Unexpected combined length: {book.page_count} != {next_page - 1}")
    if len(book.get_toc()) != 1 + len(CHAPTERS) * (1 + len(SECTIONS)):
        raise ValueError("Combined PDF bookmarks are incomplete")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    book.save(OUTPUT, garbage=4, deflate=True)
    book.close()

    # Reopen the output and make sure merging never altered an original page.
    with fitz.open(OUTPUT) as merged:
        if merged.page_count != next_page - 1:
            raise ValueError("Output page count changed after saving")
        _require_a4_landscape(merged, OUTPUT.name)
        for item in chapters:
            with fitz.open(PDF_DIR / (item["stem"] + ".pdf")) as source:
                for j, src_page in enumerate(source):
                    merged_page = merged[item["start"] - 1 + j]
                    if src_page.get_text("text") != merged_page.get_text("text"):
                        raise ValueError(f"Page text differs from {item['stem']} page {j+1}")
        if len(merged.get_toc()) != len(bookmarks):
            raise ValueError("Saved output lost its bookmarks")
    print(f"PRINT_COMBINED_OK files={len(CHAPTERS)} "
          f"pages={next_page-1} bookmarks={len(bookmarks)} "
          f"bytes={OUTPUT.stat().st_size} "
          f"output={OUTPUT.relative_to(ROOT)}")
    return OUTPUT

if __name__ == "__main__":
    build()

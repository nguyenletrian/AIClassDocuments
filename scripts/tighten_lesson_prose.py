#!/usr/bin/env python3
"""Remove editorial boilerplate from student Markdown, leaving QA metadata in docs.

Usage: python scripts/tighten_lesson_prose.py [--check]
By design, no changes inside fenced code blocks, tables, quiz questions, or answer options.
"""
from __future__ import annotations
import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSONS = sorted((ROOT / "lessons" / "chapters").glob("PY-*.vi.md"))
LESSONS += [ROOT / "lessons" / "pilot" / "AI-MATH-01-pca.vi.md"]

METADATA = re.compile(r"^\*(?:Trạng thái:|Trạng thái biên soạn:|DRAFT(?: ·| \b))[^\n]*\*\s*$")
DROP_LINES = [
    re.compile(r"^Các tham số được giải thích ngay cạnh hàm[^\n]*\.$"),
    re.compile(r"^Các tham số được giải thích cùng hàm[^\n]*\.$"),
    re.compile(r"^Các lựa chọn được giải thích cùng hàm[^\n]*\.$"),
    re.compile(r"^Trong code demo, chú thích dữ liệu[^\n]*\.$"),
    re.compile(r"^Các flags đã được giải thích[^\n]*\.$"),
    re.compile(r"^Không dùng thuật toán phức tạp hơn khi quy tắc đơn giản đã đủ\.$"),
    re.compile(r"^Mỗi giá trị mang ý nghĩa và đơn vị đã nêu\.$"),
]
PHRASES = [
    ("Trước khi chạy ví dụ, ", ""),
    (" Thử mã nhỏ để nhìn thấy giá trị trước khi làm bài toán phức tạp hơn.", ""),
    (" Dưới đây là thao tác tối giản trước khi kết hợp vào bài toán lớn hơn.", ""),
    (" Đây là lựa chọn đơn giản, có thể chạy thử độc lập trước khi dùng trên dữ liệu lớn.", ""),
    ("; không dùng công thức hoặc mô hình phức tạp hơn khi các giả định chưa được kiểm tra.", ""),
    ("; giải pháp phải khớp đúng bối cảnh và phạm vi dữ liệu.", ""),
    (" Các đơn vị và phép tính đã ghi trong đoạn mô tả; dữ liệu minh họa không dùng làm kết luận thực.", ""),
    ("; mỗi hàng của bảng là một mẫu, mỗi cột là một thuộc tính theo đơn vị trong mô tả. Các số là dữ liệu minh họa.", ""),
    (" Đây là tình huống học tập giả lập hoặc nguồn mẫu được nêu trong code.", ""),
    (". Không dùng thuật toán phức tạp hơn khi quy tắc đơn giản đã đủ.", ""),
    ("; không cần công cụ phức tạp hơn khi một quy tắc rõ ràng đã giải được vấn đề.", ""),
    (". Không dùng thuật toán AI phức tạp khi chỉ cần quy tắc xử lý rõ ràng.", ""),
    ("; đây là dữ liệu ví dụ, không phải hồ sơ thật. Mỗi giá trị mang ý nghĩa và đơn vị đã nêu.", "."),
    ("; đây là dữ liệu ví dụ, không phải hồ sơ thật.", "."),
    (". Mỗi giá trị mang ý nghĩa và đơn vị đã nêu.", ""),
]
# Some generated chapters use equivalent phrasing; strip only when isolated.
MORE_DROP = [
    re.compile(r"^Các tham số như .*được giải thích ngay tại bảng hàm này\.$"),
    re.compile(r"^Các tham số được giải thích ngay cùng hàm liên quan;.*\.$"),
    re.compile(r"^Đây là lựa chọn đơn giản, có thể chạy thử độc lập trước khi dùng trên dữ liệu lớn\.$"),
    re.compile(r"^Các số là dữ liệu minh họa\.$"),
    re.compile(r"^Trong code demo, chú thích dữ liệu và lý do xử lý; các flags đã được giải thích ngay tại bảng hàm này\\.$"),
    re.compile(r"^Các tham số như .*được giải thích ngay tại bảng hàm này\\.$"),
    re.compile(r"^\\*\\*Đọc kết quả:\\*\\* Kiểm tra shape và giá trị in ra\\. Không suy diễn độ chính xác một mô hình AI từ dữ liệu demo\\.$"),
    re.compile(r"^\\*\\*Đọc kết quả:\\*\\* So sánh số in ra với công thức trong bài\\. Nếu dữ liệu thực có nhiễu, phải kiểm tra điều kiện và giới hạn trước khi ứng dụng vào AI\\.$"),
    re.compile(r"^\\*\\*Kiểm tra:\\*\\* Đọc kết quả, các lỗi/trường hợp biên và cân nhắc trước khi dùng vào dự án thật\\.$"),
    re.compile(r"^\\*\\*Tự kiểm chứng:\\*\\* Đối chiếu kết quả với quy tắc và thử sửa đầu vào để kiểm tra tác động\\.$"),

]
# These statements are redundant in the lesson body, but real data provenance
# and actual sampling caveats must remain when they affect interpretation.
TRAILING = [
    "; đây là dữ liệu ví dụ, không phải hồ sơ thật. Mỗi giá trị mang ý nghĩa và đơn vị đã nêu.",
    "; đây là dữ liệu ví dụ, không phải hồ sơ thật.",
    ". Mỗi giá trị mang ý nghĩa và đơn vị đã nêu.",
    "; không dùng thuật toán AI phức tạp khi chỉ cần quy tắc xử lý rõ ràng.",
    "; không cần công cụ phức tạp hơn khi một quy tắc rõ ràng đã giải được vấn đề.",
    ". Không dùng thuật toán phức tạp hơn khi quy tắc đơn giản đã đủ.",
]

def tighten(original: str) -> str:
    out = []
    fenced = False
    for line in original.splitlines():
        if line.lstrip().startswith("```"):
            fenced = not fenced
            out.append(line)
            continue
        if fenced:
            out.append(line)
            continue
        stripped = line.strip()
        if METADATA.fullmatch(stripped) or any(rx.fullmatch(stripped) for rx in DROP_LINES + MORE_DROP):
            continue
        # Ignore bilingual quiz and code-like markdown, preserving their content.
        if not (re.match(r"^\*\*Q\d+\.", stripped) or
                re.match(r"^[A-D]\. ", stripped) or
                stripped.startswith("|") or stripped.startswith("`")):
            for old, new in PHRASES:
                line = line.replace(old, new)
            for phrase in TRAILING:
                line = line.replace(phrase, "." if phrase.startswith(";") else "")
            line = line.replace(". .", ".")
        out.append(line)
    result = "\n".join(out).replace("\n\n\n\n", "\n\n\n")
    return result + ("\n" if original.endswith("\n") else "")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    edited = []
    for path in LESSONS:
        old = path.read_text(encoding="utf-8")
        new = tighten(old)
        if new != old:
            edited.append((path.relative_to(ROOT), len(old) - len(new)))
            if not args.check:
                path.write_text(new, encoding="utf-8")
    for path, removed in edited:
        print(f"{path}: {removed} characters removed")
    print(f"CHANGED={len(edited)} of {len(LESSONS)}")
    if args.check and edited:
        raise SystemExit(1)

if __name__ == "__main__":
    main()

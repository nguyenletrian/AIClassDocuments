#!/usr/bin/env python3
"""Generate ONE Python file with complete bilingual study content and executable programs."""
from __future__ import annotations

import ast
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRINT = ROOT / "exports" / "print"
OUTPUT = PRINT / "source" / "AIClassDocuments-TongHop-10-Lab-BaiTap.py"
LABS = [
    ("assignment-01", "run_assignment_01", "Assignment 01 — Dictionary", "exercises/ASSIGNMENT-01.md"),
    ("lab-04", "run_lab_04", "Lab 04 — Điều kiện và vòng lặp", "labs/LAB-04.md"),
    ("lab-05", "run_lab_05", "Lab 05 — Danh sách sinh viên", "labs/LAB-05.md"),
    ("lab-05-06", "run_lab_05_06", "Lab 05–06 — Hồi quy và Gradient Descent", "labs/LAB-05-06.md"),
    ("lab-07", "run_lab_07", "Lab 07 — Xác suất", "labs/LAB-07.md"),
    ("lab-08", "run_lab_08", "Lab 08 — Thống kê", "labs/LAB-08.md"),
    ("lab-10", "run_lab_10", "Lab 10 — CSV và phân tích điểm", "labs/LAB-10.md"),
    ("pretest", "run_pretest", "Pretest — Ôn tập", "exercises/PRETEST.md"),
    ("math-02", "run_math_02", "Math 02 — Tập hợp và Jaccard", "exercises/LAB-MATH-02.md"),
    ("math-03-04", "run_math_03_04", "Math 03–04 — Ma trận và PCA", "exercises/LAB-MATH-03-04.md"),
]

HEADER = '''# -*- coding: utf-8 -*-
"""BỘ CODE GỐC TỔNG HỢP 10 LAB VÀ BÀI TẬP - AIClassDocuments.

Toàn bộ đề song ngữ, lời giải thích và định nghĩa có dạng chuỗi ba nháy kép.
Phần code là Python thực thi, không bị biến thành chuỗi.
Mỗi bài được đặt trong MỘT hàm run riêng, giữ nguyên logic từ code đã
xuất bản trong exports/print/*/*.md. Mỗi lần chỉ chạy bài được chọn.
Các biến/hàm "main", "validate", "add" của các bài không đè lên nhau.

Cách dùng:
    python AIClassDocuments-TongHop-10-Lab-BaiTap.py --list
    python AIClassDocuments-TongHop-10-Lab-BaiTap.py lab-04
    python AIClassDocuments-TongHop-10-Lab-BaiTap.py pretest
    python AIClassDocuments-TongHop-10-Lab-BaiTap.py assignment-01 --demo
    python AIClassDocuments-TongHop-10-Lab-BaiTap.py lab-05 --demo
    python AIClassDocuments-TongHop-10-Lab-BaiTap.py lab-07 --no-plot
    python AIClassDocuments-TongHop-10-Lab-BaiTap.py --read lab-05-06 definitions

Lab 10 dùng PythoClass/main.py: phải có students.csv trong thư mục làm việc.
Các bài dùng NumPy, Pandas, SciPy, SymPy hoặc scikit-learn cần cài thư viện.
Chương trình không tự cài thư viện, không tự chạy cả 10 bài.
"""
from __future__ import annotations

import sys


'''
END = '''}


def main():
    """Hiển thị danh sách hoặc chạy một bài theo mã lựa chọn."""
    if len(sys.argv) == 1 or sys.argv[1] in ("--list", "-l", "--help", "-h"):
        print("AIClassDocuments - 10 bai Lab / bai tap\\n")
        print("Chon 1 ma bai de chay: ")
        for code, (_, label) in RUNNERS.items():
            print(f"  {code:16s} {label}")
        print("\\nVi du: python AIClassDocuments-TongHop-10-Lab-BaiTap.py lab-04")
        print("Them --demo cho Assignment 01 va Lab 05 de chay khong can nhap.")
        print("Them --no-plot cho Lab 05-06, 07, 08 de khong tao hinh.")
        print("Lab 10 can students.csv trong thu muc dang chay.")
        print("Xem toan bo noi dung: --read lab-05-06")
        print("Xem dinh nghia: --read lab-05-06 definitions")
        return
    if sys.argv[1] == "--read":
        if len(sys.argv) < 3 or sys.argv[2] not in CONTENTS:
            raise SystemExit("Dung --read <ma-bai> [english|vietnamese|explanation|definitions]")
        lab_code = sys.argv[2]
        sections = CONTENTS[lab_code]
        key = sys.argv[3].lower() if len(sys.argv) >= 4 else None
        if key is not None and key not in sections:
            raise SystemExit("Muc khong hop le. Dung: english, vietnamese, explanation, definitions")
        for name, value in sections.items():
            if key is None or key == name:
                print(value)
                print()
        return
    code = sys.argv[1].lower()
    if code not in RUNNERS:
        raise SystemExit(f"Khong co bai '{code}'. Dung --list de xem ma bai.")
    runner, label = RUNNERS[code]
    print(f"=== {label} ===")
    runner()


if __name__ == "__main__":
    main()
'''

def _source_code(markdown: str, path: str, lab: str) -> str:
    found = re.findall(r"(?ms)^" + chr(96) * 3 +
                       r"python\n(.*?)^" + chr(96) * 3 + r"$", markdown)
    if len(found) != 1:
        raise ValueError(f"{path}: expected one full Python source block")
    code = found[0].rstrip("\n")
    # Each original module had its own main guard. Since the combined file
    # runs a single selected wrapper, move that guard's body directly inside
    # the wrapper. This also supports importing and calling run_lab_04().
    match = re.search(
        r'''(?m)^if __name__\s*==\s*["']__main__["']:[ \t]*\n''', code
    )
    if match:
        original = code[:match.start()].rstrip()
        guard_body = code[match.end():]
        if any(line.strip() and not line.startswith("    ")
               for line in guard_body.splitlines()):
            raise ValueError(f"{path}: main-guard body has unexpected indentation")
        tail = "\n".join(line[4:] if line.startswith("    ") else line
                         for line in guard_body.splitlines()).rstrip()
        code = original + "\n\n# Điểm bắt đầu chạy của bài gốc:\n" + tail
    elif lab != "lab-10":
        raise ValueError(f"{path}: expected an original __main__ guard")
    if re.search(r"(?m)^\s*assert\b", code):
        raise ValueError(f"{path}: the printable student code must not use assert")
    compile(code, path, "exec")
    return code

def _study_sections(markdown: str, path: str) -> dict[str, str]:
    """Recover all four prose parts in the same order as the Word document.

    The third part of the Markdown is the standalone Python listing, handled
    by _source_code() rather than wrapped as prose. Keep headings and tables.
    """
    headers = list(re.finditer(r"(?m)^## ([1-5])\. .+$", markdown))
    if len(headers) != 5 or [int(h.group(1)) for h in headers] != list(range(1, 6)):
        raise ValueError(f"{path}: expected five numbered Word-style sections")
    headings = [
        "Đề bài tiếng Anh", "Đề bài tiếng Việt", "Code Python có chú thích",
        "Giải thích nội dung và cách giải", "Giải thích các định nghĩa",
    ]
    if any(headings[i] not in headers[i].group() for i in range(5)):
        raise ValueError(f"{path}: unexpected section titles")
    sections = []
    for i, h in enumerate(headers):
        last = headers[i + 1].start() if i + 1 < 5 else len(markdown)
        sections.append(markdown[h.start():last].strip())
    title = markdown[:headers[0].start()].strip()
    if not title.startswith("# "):
        raise ValueError(f"{path}: missing original lab title")
    return {
        "english": title + "\n\n" + sections[0],
        "vietnamese": sections[1],
        "explanation": sections[3],
        "definitions": sections[4],
    }


def _triple_quoted(text: str) -> str:
    """Use literal Python triple-double-quoted strings, preserving all text.

    Escape inner quotes/backslashes so arbitrary Markdown remains a harmless
    string, never becomes active Python, and survives round-trip exactly.
    """
    literal = '"""' + text.replace("\\", "\\\\").replace('"""', '\\"""') + '"""'
    if ast.literal_eval(literal) != text:
        raise ValueError("Study text changed when quoted into Python")
    return literal


def _validate_generated(output: str, originals: dict[str, dict[str, str]]) -> None:
    tree = ast.parse(output)
    strings = {}
    functions = set()
    for statement in tree.body:
        if isinstance(statement, (ast.FunctionDef, ast.AsyncFunctionDef)):
            functions.add(statement.name)
        elif isinstance(statement, ast.Assign):
            if len(statement.targets) == 1 and isinstance(statement.targets[0], ast.Name):
                name = statement.targets[0].id
                if name.startswith("STUDY_"):
                    strings[name] = ast.literal_eval(statement.value)
    for lab, func, _, _ in LABS:
        if func not in functions:
            raise ValueError(f"Missing lab runner: {func}")
        prefix = "STUDY_" + func.removeprefix("run_").upper()
        for label, original in originals[lab].items():
            key = prefix + "_" + label.upper()
            if strings.get(key) != original:
                raise ValueError(f"Missing or corrupted {key}")
    if len(strings) != 4 * len(LABS):
        raise ValueError(f"Expected 40 prose fields; found {len(strings)}")


def generate() -> Path:
    output = HEADER
    originals = {}
    index = []
    for lab, func, title, path in LABS:
        source = (PRINT / path).read_text(encoding="utf-8")
        code = _source_code(source, path, lab)
        sections = _study_sections(source, path)
        originals[lab] = sections
        prefix = "STUDY_" + func.removeprefix("run_").upper()
        separator = "# " + "=" * 75 + "\n"
        output += separator
        output += f"# {title} | Nguồn: exports/print/{path}\n"
        output += separator + "\n"

        # Match the original chapter ordering: English -> Vietnamese -> Code.
        for label in ("english", "vietnamese"):
            output += f"{prefix}_{label.upper()} = {_triple_quoted(sections[label])}\n\n"
        output += "# ## 3. Code Python có chú thích (chương trình chạy được)\n"
        output += f"def {func}():\n"
        output += f'    """Chạy duy nhất {title}."""\n'
        output += "\n".join("    " + line if line else ""
                            for line in code.split("\n")) + "\n\n\n"

        # End-of-chapter explanations and definitions remain editable text.
        for label in ("explanation", "definitions"):
            output += f"{prefix}_{label.upper()} = {_triple_quoted(sections[label])}\n\n"
        index.append((lab, func, title, prefix))

    output += "CONTENTS = {\n"
    for lab, _, _, prefix in index:
        output += f'    "{lab}": {{\n'
        for part in ("english", "vietnamese", "explanation", "definitions"):
            output += f'        "{part}": {prefix}_{part.upper()},\n'
        output += "    },\n"
    output += "}\n\nRUNNERS = {\n"
    for lab, func, title, _ in index:
        output += f'    "{lab}": ({func}, "{title}"),\n'
    output += END
    compile(output, str(OUTPUT), "exec")
    _validate_generated(output, originals)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(output, encoding="utf-8")
    print(f"PY_SOURCE_OK labs={len(LABS)} content_sections={len(LABS)*5} "
          f"prose_strings={len(LABS)*4} bytes={OUTPUT.stat().st_size} "
          f"output={OUTPUT.relative_to(ROOT)}")
    return OUTPUT

if __name__ == "__main__":
    generate()

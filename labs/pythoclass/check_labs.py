"""Verify 7 Word-linked lab folders and run their reference solutions."""
import subprocess
import sys
from pathlib import Path

BASE=Path(__file__).resolve().parent
CASES={
    "ASSIGNMENT-01-student-dictionary":["--demo"],
    "LAB-04-conditions-loops":[],
    "LAB-05-student-list":["--demo"],
    "LAB-05-06-gradient-descent":["--no-plot"],
    "LAB-07-probability":["--no-plot"],
    "LAB-08-statistics":["--no-plot"],
    "LAB-10-file-csv":["--demo"],
}
def main():
    for folder,args in CASES.items():
        root=BASE/folder
        for name in ("LAB.md","DEMO.py","KNOWLEDGE.md","SOLUTION.py"):
            path=root/name
            assert path.is_file(), f"Missing {path}"
        src=root/"SOLUTION.py"
        compile(src.read_text(encoding="utf-8"),str(src),"exec")
        assert len((root/"LAB.md").read_text(encoding="utf-8"))>400
        result=subprocess.run([sys.executable,str(src),*args],cwd=BASE,
                              capture_output=True,text=True,timeout=50,check=False)
        if result.returncode:
            raise RuntimeError(f"{folder}: {result.stdout}\n{result.stderr}")
        print("PASS",folder)
    print("RESULT: 7 of 7 Word-derived labs have all 4 documents and runnable solutions")
if __name__=="__main__":
    main()

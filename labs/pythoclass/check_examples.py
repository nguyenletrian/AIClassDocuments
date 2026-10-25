"""Compile and run 13 lab examples, skipping uninstalled optional dependencies."""
import importlib.util
import subprocess
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
DEPENDENCIES={"06-numpy":["numpy"],"07-pandas":["pandas"],"09-linear-pca":["numpy","sklearn"],"12-ai-mini-project":["numpy","sklearn"]}
def main():
    examples=sorted(ROOT.glob("*/solution.py"))
    assert len(examples)==13, f"Expected 13 samples, got {len(examples)}"
    passed=skipped=0
    for path in examples:
        compile(path.read_text(encoding="utf-8"),str(path),"exec")
        missing=[lib for lib in DEPENDENCIES.get(path.parent.name,[]) if importlib.util.find_spec(lib) is None]
        if missing:
            skipped+=1
            print("SKIP",path.parent.name,", ".join(missing))
            continue
        res=subprocess.run([sys.executable,str(path)],capture_output=True,text=True,check=False)
        if res.returncode:
            raise RuntimeError(f"{path.parent.name}: {res.stderr}\n{res.stdout}")
        passed+=1
        print("PASS",path.parent.name)
    print(f"RESULT PASS={passed}, SKIP={skipped}, compile=13")
if __name__=="__main__":
    main()

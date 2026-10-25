# PY-43 — Git: quản lý phiên bản và hợp tác trên mã nguồn


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Repository** — kho mã nguồn; **Commit** — bản ghi thay đổi.

`File/Project → git init/add/commit → branch → pull/push → Review`

**Học xong dùng để làm gì?** Lưu lịch sử thay đổi code bằng commit, tạo nhánh thử nghiệm và khôi phục phiên bản chạy tốt.

**Kết nối kiến thức tiếp theo:** PY-44 đóng gói chức năng thao tác dữ liệu thành CLI có kiểm tra đầu vào.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Ý nghĩa |
|---|---|---|
| Repository | kho mã nguồn | Nơi lưu lịch sử phiên bản |
| Commit | bản ghi thay đổi | Điểm lưu thay đổi có thông điệp |
| Branch | nhánh | Hướng phát triển độc lập |
| Remote | kho từ xa | Đường dẫn đến repository cộng tác |

## 3. Hàm và cách sử dụng

**Từ vựng trong mục:** **Function** — hàm; **Option** — tùy chọn.

| Cú pháp | Mục đích và lựa chọn |
|---|---|
| `git status` | Xem file được sửa và đã stage hay chưa |
| `git add <file> / git commit -m` | Chọn thay đổi và tạo lịch sử có thông điệp |
| `git switch -c <branch>` | Tách nhánh thử nghiệm để không sửa nhánh chính |
| `git pull --ff-only / git push` | Đồng bộ an toàn khi lịch sử cho phép, kiểm tra remote trước |

## 4. Khái niệm chính và liên quan

**Mạch kiến thức:** Git theo dõi lịch sử của một repository. Ta chọn thay đổi để stage, ghi chúng vào commit, phát triển độc lập trên branch và dùng remote để đồng bộ với người khác. Bốn khái niệm này tạo thành một quy trình liền mạch.

### 4.1. Repository — Nơi lưu mã nguồn và lịch sử

**Từ vựng trong mục:** **Repository**.

Repository là thư mục dự án được Git theo dõi; bên trong `.git` lưu thông tin commit, nhánh và tham chiếu. Ví dụ bài tập có `lesson.py`. Sau khi chạy `git init`, Git chưa tự đưa mọi file vào commit; `git status` chỉ cho biết trạng thái so với commit gần nhất và khu vực stage. Lệnh dưới đây dành cho terminal trong thư mục dự án đã khởi tạo Git.

**No Note — Không chú thích**

```bash
git status
```

**Code có chú thích — Giải thích từng bước**

```bash
# Mục đích: Nơi lưu mã nguồn và lịch sử.
git status
```

**Kết quả có thể quan sát:** Trạng thái hiển thị phụ thuộc file đang sửa và các commit hiện có; xem phần Changes not staged, Staged, Untracked.

### 4.2. Commit — Bản chụp các thay đổi đã stage

**Từ vựng trong mục:** **Commit**.

Commit ghi lại một trạng thái của những file đã **stage** vào lịch sử cùng tác giả, thời gian và thông điệp. Quy trình `git add lesson.py` đưa bản đang chọn vào staging area, sau đó `git commit -m ...` tạo commit. Nếu sửa file thêm **sau khi stage**, phần sửa mới chưa tự nằm trong commit. `git log -1 --oneline` xem commit gần nhất; mã hash phụ thuộc repository.

**No Note — Không chú thích**

```bash
git log -1 --oneline
```

**Code có chú thích — Giải thích từng bước**

```bash
# Mục đích: Bản chụp các thay đổi đã stage.
git log -1 --oneline
```

**Kết quả có thể quan sát:** Lệnh in mã commit rút gọn và thông điệp của bản gần nhất nếu dự án có commit; không có một mã cố định.

### 4.3. Branch — Nhánh để phát triển song song

**Từ vựng trong mục:** **Branch**.

Branch là một **tham chiếu đến commit**, giúp làm tính năng riêng mà không làm thay đổi ngay `main`. `git switch -c feature/score` tạo nhánh mới và chuyển sang nó từ commit hiện tại; code mới chỉ có trên nhánh đó cho tới khi được merge. Để tránh nhầm, kiểm tra `git branch --show-current` trước khi làm; tên nhánh này là ví dụ, không phải chính sách của mọi nhóm.

**No Note — Không chú thích**

```bash
git switch -c feature/score
git branch --show-current
```

**Code có chú thích — Giải thích từng bước**

```bash
# Mục đích: Nhánh để phát triển song song.
git switch -c feature/score
git branch --show-current
```

**Kết quả có thể quan sát:** Sau khi tạo thành công, lệnh sau in `feature/score`; lần chạy tiếp sẽ báo nhánh đã tồn tại.

### 4.4. Remote — Liên kết đến kho Git ở nơi khác

**Từ vựng trong mục:** **Remote**.

Remote là một tên tham chiếu đến địa chỉ repository khác, thường tên `origin` dùng cho kho trên GitHub. `git remote -v` liệt kê địa chỉ fetch/push đang cấu hình; nó không tự chứng minh đã đăng nhập hay có quyền push. `git fetch` tải tham chiếu từ remote, `git pull --ff-only` chỉ nhận thay đổi khi có thể đi thẳng không tạo merge commit, còn `git push` gửi commit nếu có quyền.

**No Note — Không chú thích**

```bash
git remote -v
```

**Code có chú thích — Giải thích từng bước**

```bash
# Mục đích: Liên kết đến kho Git ở nơi khác.
git remote -v
```

**Kết quả có thể quan sát:** Lệnh hiển thị tên và URL remote đã cấu hình; repository không có remote sẽ không in dòng nào.

## 5. Năm tình huống Git thực thi an toàn — từ 10 file đến merge 20 file

### Tình huống 1 — Cấp 1: Kiểm trạng thái 10 script trước khi đưa vào Git

**Từ vựng trong mục:** **Repository** — kho phiên bản; **Untracked** — chưa được theo dõi; **Status** — trạng thái.

**Tình huống thực tế:** Một học viên vừa nhận **10 script Python**, từ `lesson01.py` đến `lesson10.py`, để bắt đầu quản lý phiên bản. Học viên muốn tạo một **repository Git thử nghiệm riêng** rồi xem cả mười file đã được Git nhận diện hay chưa, nhưng **chưa muốn đưa chúng vào lịch sử**. Mọi thao tác phải nằm trong thư mục tạm để không ảnh hưởng repository học tập đang sử dụng.

**Vì sao chọn cách này?** **Repository** là vùng dự án mà Git ghi nhận thay đổi; `git init` chỉ tạo thư mục quản lý **`.git`**, chưa tự thêm nội dung script vào lịch sử. `git status --porcelain` cho thông tin trạng thái ngắn, dễ xử lý bằng code; ký hiệu `??` nghĩa là file **chưa được Git theo dõi (untracked)**. `git diff --cached --name-only` xem phần **đã stage** để chuẩn bị commit; ở bước này danh sách đó còn rỗng. `TemporaryDirectory` cách ly tất cả thao tác trong **thư mục thử rồi tự dọn**, nên ví dụ không thay đổi repository thật của học viên.

**Quy trình:**
1. Tạo repository tạm và 10 file script có nội dung độc lập.
2. Chạy status, đếm dòng `??` và số file Git đã stage.
3. Báo cả hai số để phân biệt untracked và staged.

**No Note — Không chú thích**

```python
import subprocess
import tempfile
from pathlib import Path

def git(root, *args):
    return subprocess.run(["git", *args], cwd=root, check=True,
                          text=True, capture_output=True).stdout.strip()

with tempfile.TemporaryDirectory() as temp:
    root = Path(temp)
    git(root, "init", "-q", "-b", "main")
    for i in range(1, 11):
        (root / f"lesson{i:02d}.py").write_text(f"print({i})\n", encoding="utf-8")
    lines = git(root, "status", "--porcelain").splitlines()
    untracked = 0
    for line in lines:
        if line.startswith("?? "):
            untracked += 1
    staged = git(root, "diff", "--cached", "--name-only").splitlines()
    print("Script:", 10)
    print("Untracked:", untracked)
    print("Đã stage:", len(staged))
    print("Đúng repository tạm:", (root / ".git").exists())
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Khởi tạo một repository Git tạm với 10 script và phân biệt file untracked với staged.
# Dữ liệu: 10 file lesson01.py..lesson10.py, mọi thao tác chỉ xảy ra trong thư mục tạm tự xóa sau khi chạy.
# subprocess cho phép chạy lệnh Git CLI từ Python, thay vì mô phỏng phản hồi Git.
import subprocess
# tempfile cấp thư mục tạm để ví dụ không đụng repository thật của người học.
import tempfile
# Path đại diện đường dẫn theo hệ điều hành và hỗ trợ thao tác file với toán tử /.
from pathlib import Path

# Định nghĩa hàm trợ giúp chạy Git; *args thu các phần đối số khác nhau thành tuple, root chỉ định thư mục repository tạm.
def git(root, *args):
    # subprocess.run() chạy chương trình git theo list đối số; không dùng shell=True nên tránh diễn giải chuỗi bởi shell.
    # cwd=root đặt thư mục làm việc của Git đúng repository tạm, không vô tình thao tác trong dự án thật.
    # check=True phát sinh CalledProcessError nếu lệnh Git trả mã lỗi, tránh tiếp tục với kết quả thất bại.
    return subprocess.run(["git", *args], cwd=root, check=True,
                          # text=True giải mã stdout thành chuỗi văn bản, không phải bytes.
                          # capture_output=True thu stdout/stderr để xử lý trong Python thay vì in lẫn lên terminal.
                          # stdout là đầu ra chuẩn của lệnh Git; strip() bỏ khoảng trắng/xuống dòng hai đầu cho dễ so sánh.
                          text=True, capture_output=True).stdout.strip()

# TemporaryDirectory() tạo thư mục tạm và tự dọn toàn bộ repository khi ra khỏi khối with, kể cả khi có lỗi.
with tempfile.TemporaryDirectory() as temp:
    # Đổi chuỗi đường dẫn thư mục tạm thành Path để ghép tên file.
    root = Path(temp)
    # git init -b main tạo repository mới với nhánh chính main; -q giảm thông báo, chỉ trong root tạm.
    git(root, "init", "-q", "-b", "main")
    # range(1,11) tạo mười số 1..10; không bao gồm 11.
    for i in range(1, 11):
        # Toán tử / của Path ghép đường dẫn; :02d tạo tên lesson01..lesson10; write_text() tạo file UTF-8 có một lệnh print tương ứng.
        (root / f"lesson{i:02d}.py").write_text(f"print({i})\n", encoding="utf-8")
    # status --porcelain cho trạng thái máy đọc được, tiền tố '?? ' nghĩa Git CHƯA theo dõi file.
    # splitlines() tách chuỗi stdout thành list từng dòng, không giữ ký tự xuống dòng.
    lines = git(root, "status", "--porcelain").splitlines()
    untracked = 0
    for line in lines:
        # startswith('?? ') chỉ đếm những file chưa được Git theo dõi, không đếm file đã stage.
        if line.startswith("?? "):
            # Tăng số file chưa theo dõi khi thấy một dòng trạng thái khớp.
            untracked += 1
    # splitlines() tách chuỗi stdout thành list từng dòng, không giữ ký tự xuống dòng.
    # diff --cached --name-only liệt kê tên file trong vùng STAGING (index) khác HEAD; trước git add danh sách rỗng.
    staged = git(root, "diff", "--cached", "--name-only").splitlines()
    print("Script:", 10)
    print("Untracked:", untracked)
    # Đếm số file đã stage; bằng 0 khi chưa chạy git add.
    print("Đã stage:", len(staged))
    # exists() xác minh thư mục metadata .git được tạo bên trong root tạm, không động tới repo bài học.
    print("Đúng repository tạm:", (root / ".git").exists())
```

**Lệnh Git tương ứng:** Chỉ thực hành trong repository thử, không chạy vào repository đang làm việc.

**No Note — Không chú thích**

```bash
git status --short
```

**Code có chú thích — Giải thích từng bước**

```bash
git status --short
```

**Kết quả khi chạy:**

```text
Script: 10
Untracked: 10
Đã stage: 0
Đúng repository tạm: True
```

Thư mục tạm sẽ tự bị xóa sau ví dụ; script chỉ nghiên cứu Git **cục bộ**, không có lệnh đẩy lên GitHub.

### Tình huống 2 — Cấp 2: Chỉ stage năm trong 12 file của bản cập nhật

**Từ vựng trong mục:** **Staging area** — vùng chuẩn bị; **git add** — chọn file; **Diff cached** — khác biệt đã stage.

**Tình huống thực tế:** Nhóm phát triển chuẩn bị **12 file module Python**, từ `module01.py` đến `module12.py`. Trong đợt review này, chỉ **5 file đầu** đã được kiểm thử và được phép đưa vào lần commit tiếp theo; **7 file còn lại** vẫn đang viết. Trưởng nhóm muốn kiểm rõ năm file đã được **stage** và bảy file chưa được chọn, tránh đưa nhầm code chưa hoàn thành vào lịch sử.

**Vì sao chọn cách này?** **Staging area** là danh sách thay đổi **được chọn để đưa vào commit tiếp theo**, không phải mọi file đang nằm trong thư mục. `git add -- module01.py ... module05.py` chọn rõ **năm file đã duyệt**, khác `git add .` có thể đưa cả 12 file vào stage. `git diff --cached --name-only` cho năm file đã chọn; `git ls-files --others --exclude-standard` cho bảy file còn **untracked**. Đếm hai nhóm là cách kiểm nhanh trước khi commit: **stage chưa phải commit**, nên vẫn còn cơ hội sửa lựa chọn nếu thấy file sai.

**Quy trình:**
1. Tạo repo tạm và 12 file có dữ liệu riêng.
2. Stage đúng năm tên, không dùng ký tự chọn toàn bộ.
3. Đếm số staged/untracked và kiểm module06 chưa stage.

**No Note — Không chú thích**

```python
import subprocess
import tempfile
from pathlib import Path

def git(root, *args):
    return subprocess.run(["git", *args], cwd=root, check=True,
                          text=True, capture_output=True).stdout.strip()

with tempfile.TemporaryDirectory() as temp:
    root = Path(temp)
    git(root, "init", "-q", "-b", "main")
    for i in range(1, 13):
        (root / f"module{i:02d}.py").write_text(f"VALUE = {i}\n", encoding="utf-8")
    chosen = []
    for i in range(1, 6):
        chosen.append(f"module{i:02d}.py")
    git(root, "add", "--", *chosen)
    staged = git(root, "diff", "--cached", "--name-only").splitlines()
    others = git(root, "ls-files", "--others", "--exclude-standard").splitlines()
    print("File:", 12)
    print("Đã stage:", len(staged))
    print("Chưa stage:", len(others))
    print("module06 chưa stage:", "module06.py" in others)
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Chọn stage năm file trong 12 module, giữ bảy file khác chưa theo dõi.
# Dữ liệu: 12 module01.py..module12.py trong repository tạm; chỉ module01..05 được thêm vào index.
# subprocess cho phép chạy lệnh Git CLI từ Python, thay vì mô phỏng phản hồi Git.
import subprocess
# tempfile cấp thư mục tạm để ví dụ không đụng repository thật của người học.
import tempfile
# Path đại diện đường dẫn theo hệ điều hành và hỗ trợ thao tác file với toán tử /.
from pathlib import Path

# Định nghĩa hàm trợ giúp chạy Git; *args thu các phần đối số khác nhau thành tuple, root chỉ định thư mục repository tạm.
def git(root, *args):
    # subprocess.run() chạy chương trình git theo list đối số; không dùng shell=True nên tránh diễn giải chuỗi bởi shell.
    # cwd=root đặt thư mục làm việc của Git đúng repository tạm, không vô tình thao tác trong dự án thật.
    # check=True phát sinh CalledProcessError nếu lệnh Git trả mã lỗi, tránh tiếp tục với kết quả thất bại.
    return subprocess.run(["git", *args], cwd=root, check=True,
                          # text=True giải mã stdout thành chuỗi văn bản, không phải bytes.
                          # capture_output=True thu stdout/stderr để xử lý trong Python thay vì in lẫn lên terminal.
                          # stdout là đầu ra chuẩn của lệnh Git; strip() bỏ khoảng trắng/xuống dòng hai đầu cho dễ so sánh.
                          text=True, capture_output=True).stdout.strip()

# TemporaryDirectory() tạo thư mục tạm và tự dọn toàn bộ repository khi ra khỏi khối with, kể cả khi có lỗi.
with tempfile.TemporaryDirectory() as temp:
    # Đổi chuỗi đường dẫn thư mục tạm thành Path để ghép tên file.
    root = Path(temp)
    # git init -b main tạo repository mới với nhánh chính main; -q giảm thông báo, chỉ trong root tạm.
    git(root, "init", "-q", "-b", "main")
    # Sinh số 1..12 để tạo đủ 12 script, không chứa 13.
    for i in range(1, 13):
        # Path ghép root/tên file, :02d thêm số 0; write_text() ghi UTF-8 và tạo file nếu chưa có.
        (root / f"module{i:02d}.py").write_text(f"VALUE = {i}\n", encoding="utf-8")
    # List tên năm file dự định stage; không stage toàn bộ thư mục.
    chosen = []
    # Tạo số 1..5, đúng năm module được chọn.
    for i in range(1, 6):
        # append() đưa tên file module01..05 vào list.
        chosen.append(f"module{i:02d}.py")
    # git add chuyển file sang staging; '--' kết thúc tùy chọn để tên file lạ không bị hiểu là cờ; *chosen giải nén năm tên thành năm đối số.
    git(root, "add", "--", *chosen)
    # Liệt kê tên các file đã stage trong index, chứ chưa commit.
    staged = git(root, "diff", "--cached", "--name-only").splitlines()
    # ls-files --others liệt kê file chưa theo dõi; --exclude-standard loại file bị ignore theo .gitignore/exclude.
    others = git(root, "ls-files", "--others", "--exclude-standard").splitlines()
    print("File:", 12)
    # Số file trong index phải là năm, khác len(others) là bảy chưa stage.
    print("Đã stage:", len(staged))
    print("Chưa stage:", len(others))
    # in kiểm module06 nằm trong các file chưa theo dõi, trả Boolean.
    print("module06 chưa stage:", "module06.py" in others)
```

**Lệnh Git tương ứng:** Chỉ thực hành trong repository thử, không chạy vào repository đang làm việc.

**No Note — Không chú thích**

```bash
git add -- module01.py module02.py module03.py module04.py module05.py
```

**Code có chú thích — Giải thích từng bước**

```bash
git add -- module01.py module02.py module03.py module04.py module05.py
```

**Kết quả khi chạy:**

```text
File: 12
Đã stage: 5
Chưa stage: 7
module06 chưa stage: True
```

Stage là **lựa chọn nội dung cho commit tiếp theo**, không phải đã commit. Khi sửa file sau stage, cần stage lại phần sửa muốn ghi.

### Tình huống 3 — Cấp 3: Tách nhánh thay đổi ba trong 15 script

**Từ vựng trong mục:** **Branch** — nhánh; **Commit** — bản ghi lịch sử; **Switch** — chuyển nhánh.

**Tình huống thực tế:** Một nhóm có **15 script** đã được ghi trong nhánh `main` với nội dung `VERSION = 1`. Một người muốn thử phiên bản mới cho **ba script đầu**, nhưng đồng đội vẫn cần dùng đúng phiên bản cũ trên `main`. Người đó sẽ tạo nhánh `feature`, sửa và commit riêng ba file rồi chuyển qua lại giữa hai nhánh để kiểm chứng sự khác biệt.

**Vì sao chọn cách này?** **Branch (nhánh)** là tên trỏ tới một chuỗi lịch sử commit, giúp thử thay đổi mà chưa đưa vào nhánh chung. `git switch -c feature` tạo và chuyển sang nhánh mới từ bản `main`; sửa ba script rồi `git add` và `git commit` lưu bản thay đổi **chỉ trên feature**. `git diff --name-only main feature` cho biết những file khác giữa hai đầu nhánh. Khi `switch` về `main`, `lesson01.py` vẫn là `VERSION = 1`; chuyển sang `feature` thì là `VERSION = 2`. Ví dụ này không cần remote, nên không phải kéo code hoặc tạo pull request.

**Quy trình:**
1. Tạo 15 script v1 và commit ban đầu với thông tin tác giả test.
2. Tạo nhánh `feature`, sửa ba script thành v2, commit.
3. Chuyển giữa hai nhánh, kiểm tra nội dung khác nhau và số file diff.

**No Note — Không chú thích**

```python
import subprocess
import tempfile
from pathlib import Path

def git(root, *args):
    return subprocess.run(["git", *args], cwd=root, check=True,
                          text=True, capture_output=True).stdout.strip()

with tempfile.TemporaryDirectory() as temp:
    root = Path(temp)
    git(root, "init", "-q", "-b", "main")
    git(root, "config", "user.name", "Lesson Tester")
    git(root, "config", "user.email", "lesson@example.invalid")
    for i in range(1,16):
        (root / f"lesson{i:02d}.py").write_text("VERSION = 1\n", encoding="utf-8")
    git(root, "add", ".")
    git(root, "commit", "-q", "-m", "base")
    git(root, "switch", "-q", "-c", "feature")
    for i in range(1,4):
        (root / f"lesson{i:02d}.py").write_text("VERSION = 2\n", encoding="utf-8")
    git(root, "add", ".")
    git(root, "commit", "-q", "-m", "update three scripts")
    difference = git(root, "diff", "--name-only", "main", "feature").splitlines()
    git(root, "switch", "-q", "main")
    main_version = (root / "lesson01.py").read_text().strip()
    git(root, "switch", "-q", "feature")
    feature_version = (root / "lesson01.py").read_text().strip()
    print("File ban đầu:", 15)
    print("File thay đổi:", len(difference))
    print("Main:", main_version)
    print("Feature:", feature_version)
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tạo nhánh feature, commit ba file thay đổi và chứng minh main chưa nhận sửa đổi.
# Dữ liệu: 15 script có VERSION=1 ban đầu; feature đổi ba script đầu thành VERSION=2, mỗi nhánh có lịch sử riêng.
# subprocess cho phép chạy lệnh Git CLI từ Python, thay vì mô phỏng phản hồi Git.
import subprocess
# tempfile cấp thư mục tạm để ví dụ không đụng repository thật của người học.
import tempfile
# Path đại diện đường dẫn theo hệ điều hành và hỗ trợ thao tác file với toán tử /.
from pathlib import Path

# Định nghĩa hàm trợ giúp chạy Git; *args thu các phần đối số khác nhau thành tuple, root chỉ định thư mục repository tạm.
def git(root, *args):
    # subprocess.run() chạy chương trình git theo list đối số; không dùng shell=True nên tránh diễn giải chuỗi bởi shell.
    # cwd=root đặt thư mục làm việc của Git đúng repository tạm, không vô tình thao tác trong dự án thật.
    # check=True phát sinh CalledProcessError nếu lệnh Git trả mã lỗi, tránh tiếp tục với kết quả thất bại.
    return subprocess.run(["git", *args], cwd=root, check=True,
                          # text=True giải mã stdout thành chuỗi văn bản, không phải bytes.
                          # capture_output=True thu stdout/stderr để xử lý trong Python thay vì in lẫn lên terminal.
                          # stdout là đầu ra chuẩn của lệnh Git; strip() bỏ khoảng trắng/xuống dòng hai đầu cho dễ so sánh.
                          text=True, capture_output=True).stdout.strip()

# TemporaryDirectory() tạo thư mục tạm và tự dọn toàn bộ repository khi ra khỏi khối with, kể cả khi có lỗi.
with tempfile.TemporaryDirectory() as temp:
    # Đổi chuỗi đường dẫn thư mục tạm thành Path để ghép tên file.
    root = Path(temp)
    # git init -b main tạo repository mới với nhánh chính main; -q giảm thông báo, chỉ trong root tạm.
    git(root, "init", "-q", "-b", "main")
    # git config cài tên tác giả commit CHỈ trong repository tạm, không đổi Git global.
    git(root, "config", "user.name", "Lesson Tester")
    # Đặt email minh họa .invalid cục bộ để Git cho phép tạo commit, không gửi email.
    git(root, "config", "user.email", "lesson@example.invalid")
    # Tạo 15 tên script với chỉ số 1..15.
    for i in range(1,16):
        # write_text() tạo nội dung bản gốc trên tất cả 15 file, encoding='utf-8' giữ mã Unicode.
        (root / f"lesson{i:02d}.py").write_text("VERSION = 1\n", encoding="utf-8")
    # git add . đưa file đang thay đổi trong root vào staging, trước khi commit.
    git(root, "add", ".")
    # commit tạo snapshot từ staging; -q chạy yên lặng, -m truyền thông điệp 'base'.
    git(root, "commit", "-q", "-m", "base")
    # switch -c feature tạo nhánh mới tại commit hiện tại và chuyển sang; -q giảm thông báo.
    git(root, "switch", "-q", "-c", "feature")
    # Chọn chỉ ba file đầu tiên để sửa trên nhánh feature.
    for i in range(1,4):
        # Ghi đè bản feature của ba file thành VERSION=2; không thay đổi ngay commit của main.
        (root / f"lesson{i:02d}.py").write_text("VERSION = 2\n", encoding="utf-8")
    # git add . đưa file đang thay đổi trong root vào staging, trước khi commit.
    git(root, "add", ".")
    # Ghi một commit sửa ba script trên feature.
    git(root, "commit", "-q", "-m", "update three scripts")
    # diff --name-only main feature liệt kê file có nội dung khác nhau giữa hai nhánh, không in toàn bộ patch.
    difference = git(root, "diff", "--name-only", "main", "feature").splitlines()
    # Chuyển về main: working tree phản ánh VERSION=1 từ commit main.
    git(root, "switch", "-q", "main")
    # read_text() đọc nội dung file hiện đang checkout; strip() bỏ dấu xuống dòng cuối, không chỉnh file.
    main_version = (root / "lesson01.py").read_text().strip()
    # Chuyển lại feature: phiên bản working tree của lesson01 là VERSION=2.
    git(root, "switch", "-q", "feature")
    # read_text() đọc nội dung file hiện đang checkout; strip() bỏ dấu xuống dòng cuối, không chỉnh file.
    feature_version = (root / "lesson01.py").read_text().strip()
    print("File ban đầu:", 15)
    # Số tên file khác nhau giữa hai nhánh, đúng ba.
    print("File thay đổi:", len(difference))
    print("Main:", main_version)
    print("Feature:", feature_version)
```

**Lệnh Git tương ứng:** Chỉ thực hành trong repository thử, không chạy vào repository đang làm việc.

**No Note — Không chú thích**

```bash
git switch -c feature
```

**Code có chú thích — Giải thích từng bước**

```bash
git switch -c feature
```

**Kết quả khi chạy:**

```text
File ban đầu: 15
File thay đổi: 3
Main: VERSION = 1
Feature: VERSION = 2
```

Commit lưu ảnh chụp **file đã stage**. Quay về `main` không cần xóa thay đổi ở nhánh feature và cũng không tạo commit trên main.

### Tình huống 4 — Cấp 4: Chia 18 file thành ba commit có thể kiểm tra

**Từ vựng trong mục:** **Commit history** — lịch sử; **Log** — nhật ký commit; **Tracked file** — file đang theo dõi.

**Tình huống thực tế:** Nhóm bảo trì nhận **18 script tool01.py–tool18.py** cần quản lý theo **ba giai đoạn**, mỗi giai đoạn gồm đúng 6 file. Quản lý muốn lịch sử Git có **ba commit có tên dễ hiểu**, mỗi commit đại diện một đợt làm việc, thay vì chỉ có một commit chứa toàn bộ 18 file. Sau cùng, cần xác nhận Git theo dõi đủ file và đọc lại tên các commit gần nhất.

**Vì sao chọn cách này?** **Commit** là mốc lưu lại một nhóm thay đổi đã được stage, kèm **thông điệp mô tả**. Chương trình chia 18 file thành ba đợt sáu file, dùng `git add` đúng tên file mỗi đợt rồi `git commit -m 'batch ...'`. `git rev-list --count HEAD` đếm ba commit đã tạo, `git ls-files` xác nhận 18 script đã được theo dõi. `git log -3 --format=%s` chỉ lấy **tiêu đề** ba commit gần nhất (mới trước, cũ sau), vì mã hash có thể đổi giữa các lần dựng thử nên không phù hợp để viết sẵn đáp án cố định. Chia lịch sử theo công việc giúp review hoặc quay lại từng giai đoạn rõ ràng.

**Quy trình:**
1. Tạo lần lượt ba nhóm, mỗi nhóm sáu file trong repository tạm.
2. Sau mỗi nhóm stage riêng các file và commit với thông điệp riêng.
3. Kiểm số file Git theo dõi, số commit và thứ tự ba thông điệp gần nhất.

**No Note — Không chú thích**

```python
import subprocess
import tempfile
from pathlib import Path

def git(root, *args):
    return subprocess.run(["git", *args], cwd=root, check=True,
                          text=True, capture_output=True).stdout.strip()

with tempfile.TemporaryDirectory() as temp:
    root = Path(temp)
    git(root, "init", "-q", "-b", "main")
    git(root, "config", "user.name", "Lesson Tester")
    git(root, "config", "user.email", "lesson@example.invalid")
    for batch in range(1,4):
        filenames = []
        for i in range((batch-1)*6+1, batch*6+1):
            filename = f"tool{i:02d}.py"
            (root / filename).write_text(f"VALUE = {i}\n", encoding="utf-8")
            filenames.append(filename)
        git(root, "add", "--", *filenames)
        git(root, "commit", "-q", "-m", f"batch {batch}")
    tracked = git(root, "ls-files").splitlines()
    messages = git(root, "log", "-3", "--format=%s").splitlines()
    print("Script:", len(tracked))
    print("Commit:", git(root, "rev-list", "--count", "HEAD"))
    print("Lịch sử gần nhất:", ", ".join(messages))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tạo ba commit nhóm độc lập trên 18 file và đọc lịch sử Git gần nhất.
# Dữ liệu: Ba đợt, mỗi đợt tạo sáu file tool, tổng 18 file trên main của repository tạm.
# subprocess cho phép chạy lệnh Git CLI từ Python, thay vì mô phỏng phản hồi Git.
import subprocess
# tempfile cấp thư mục tạm để ví dụ không đụng repository thật của người học.
import tempfile
# Path đại diện đường dẫn theo hệ điều hành và hỗ trợ thao tác file với toán tử /.
from pathlib import Path

# Định nghĩa hàm trợ giúp chạy Git; *args thu các phần đối số khác nhau thành tuple, root chỉ định thư mục repository tạm.
def git(root, *args):
    # subprocess.run() chạy chương trình git theo list đối số; không dùng shell=True nên tránh diễn giải chuỗi bởi shell.
    # cwd=root đặt thư mục làm việc của Git đúng repository tạm, không vô tình thao tác trong dự án thật.
    # check=True phát sinh CalledProcessError nếu lệnh Git trả mã lỗi, tránh tiếp tục với kết quả thất bại.
    return subprocess.run(["git", *args], cwd=root, check=True,
                          # text=True giải mã stdout thành chuỗi văn bản, không phải bytes.
                          # capture_output=True thu stdout/stderr để xử lý trong Python thay vì in lẫn lên terminal.
                          # stdout là đầu ra chuẩn của lệnh Git; strip() bỏ khoảng trắng/xuống dòng hai đầu cho dễ so sánh.
                          text=True, capture_output=True).stdout.strip()

# TemporaryDirectory() tạo thư mục tạm và tự dọn toàn bộ repository khi ra khỏi khối with, kể cả khi có lỗi.
with tempfile.TemporaryDirectory() as temp:
    # Đổi chuỗi đường dẫn thư mục tạm thành Path để ghép tên file.
    root = Path(temp)
    # git init -b main tạo repository mới với nhánh chính main; -q giảm thông báo, chỉ trong root tạm.
    git(root, "init", "-q", "-b", "main")
    git(root, "config", "user.name", "Lesson Tester")
    git(root, "config", "user.email", "lesson@example.invalid")
    # Ba vòng batch=1,2,3, đúng ba commit riêng biệt.
    for batch in range(1,4):
        # List riêng mỗi batch chứa sáu tên file sẽ stage.
        filenames = []
        # Tính dải chỉ số sáu file liên tiếp cho từng batch: 1..6, 7..12, 13..18.
        for i in range((batch-1)*6+1, batch*6+1):
            # f-string :02d đặt tên tool01.py..tool18.py theo thứ tự.
            filename = f"tool{i:02d}.py"
            # Ghi một script mới theo số i trong thư mục tạm, UTF-8.
            (root / filename).write_text(f"VALUE = {i}\n", encoding="utf-8")
            # Ghi tên file vừa tạo vào list của đúng batch hiện tại.
            filenames.append(filename)
        # Stage CHỈ sáu file của batch hiện tại; '--' ngăn hiểu tên thành cờ, * giải nén list.
        git(root, "add", "--", *filenames)
        # Tạo một commit snapshot per batch, -q ẩn thông báo, -m gắn tên batch.
        git(root, "commit", "-q", "-m", f"batch {batch}")
    # ls-files liệt kê tất cả file đang được Git theo dõi trong index, gồm 18 file sau ba batch.
    tracked = git(root, "ls-files").splitlines()
    # log -3 lấy tối đa ba commit gần nhất; --format=%s chỉ in CHỦ ĐỀ commit, không in hash/body.
    messages = git(root, "log", "-3", "--format=%s").splitlines()
    print("Script:", len(tracked))
    # rev-list --count HEAD đếm số commit có thể đi tới từ HEAD, ở đây ba commit.
    print("Commit:", git(root, "rev-list", "--count", "HEAD"))
    # join() ghép các tiêu đề commit theo thứ tự từ mới tới cũ.
    print("Lịch sử gần nhất:", ", ".join(messages))
```

**Lệnh Git tương ứng:** Chỉ thực hành trong repository thử, không chạy vào repository đang làm việc.

**No Note — Không chú thích**

```bash
git log -3 --format=%s
```

**Code có chú thích — Giải thích từng bước**

```bash
git log -3 --format=%s
```

**Kết quả khi chạy:**

```text
Script: 18
Commit: 3
Lịch sử gần nhất: batch 3, batch 2, batch 1
```

Chỉ có ba commit vì mỗi commit chứa **sáu file**. Số file và số commit trả lời hai câu hỏi khác nhau.

### Tình huống 5 — Cấp 5: Merge nhánh an toàn khi hai người sửa khác file trong 20 script

**Từ vựng trong mục:** **Merge** — hợp nhất lịch sử; **Merge commit** — commit có hai cha; **Clean working tree** — cây làm việc sạch.

**Tình huống thực tế:** Hai lập trình viên cùng làm trên **dự án thử nghiệm 20 file Python**. Từ phiên bản chung, người thứ nhất sửa **tool01 và tool02** trên nhánh `feature`; người thứ hai sửa **tool19 và tool20** trên `main`. Vì họ sửa **những file khác nhau**, nhóm muốn hợp nhất để cả bốn sửa đổi còn nguyên, thấy rõ **merge commit có hai nhánh cha**, và kiểm tra trạng thái làm việc sạch. Không kết nối remote hay đẩy code ra Internet.

**Vì sao chọn cách này?** **Merge** là đưa thay đổi từ hai lịch sử vào cùng một nhánh. Ví dụ tạo commit gốc 20 file, tách `feature` để sửa hai file đầu, rồi quay về `main` sửa hai file cuối, nên hai nhánh đã có **hai commit khác nhau**. `git merge --no-ff feature` yêu cầu Git tạo **merge commit riêng**, kể cả khi có thể gộp nhanh, để nhìn rõ dấu mốc hợp nhất. `git rev-list --parents -n 1 HEAD` cho thấy merge commit và **hai parent**; nội dung tool01/tool20 chứng minh hai phía đều được giữ, còn `status` trống nghĩa là thư mục làm việc sạch. Vì các file sửa không giao nhau, Git có thể tự gộp; nếu cùng sửa một dòng thì cần giải quyết **xung đột (conflict)**, không tự ghi đè theo cảm tính.

**Quy trình:**
1. Tạo 20 file và commit bản gốc.
2. Từ cùng commit gốc, tạo nhánh feature rồi sửa/commit hai file đầu; quay main sửa/commit hai file cuối.
3. Merge không fast-forward, xác minh nội dung bốn file, 20 file tracked và hai parent.

**No Note — Không chú thích**

```python
import subprocess
import tempfile
from pathlib import Path

def git(root, *args):
    return subprocess.run(["git", *args], cwd=root, check=True,
                          text=True, capture_output=True).stdout.strip()

with tempfile.TemporaryDirectory() as temp:
    root = Path(temp)
    git(root, "init", "-q", "-b", "main")
    git(root, "config", "user.name", "Lesson Tester")
    git(root, "config", "user.email", "lesson@example.invalid")
    for i in range(1,21):
        (root / f"tool{i:02d}.py").write_text("VERSION = 1\n", encoding="utf-8")
    git(root, "add", ".")
    git(root, "commit", "-q", "-m", "base")
    git(root, "switch", "-q", "-c", "feature")
    for i in (1,2):
        (root / f"tool{i:02d}.py").write_text("VERSION = 2\n", encoding="utf-8")
    git(root, "add", ".")
    git(root, "commit", "-q", "-m", "feature edits")
    git(root, "switch", "-q", "main")
    for i in (19,20):
        (root / f"tool{i:02d}.py").write_text("VERSION = 3\n", encoding="utf-8")
    git(root, "add", ".")
    git(root, "commit", "-q", "-m", "main edits")
    git(root, "merge", "-q", "--no-ff", "feature", "-m", "merge feature")
    parents = git(root, "rev-list", "--parents", "-n", "1", "HEAD").split()
    print("File:", len(git(root, "ls-files").splitlines()))
    print("Commit trong lịch sử:", git(root, "rev-list", "--count", "HEAD"))
    print("Merge có hai cha:", len(parents) == 3)
    print("Sửa feature giữ lại:", (root / "tool01.py").read_text().strip() == "VERSION = 2")
    print("Sửa main giữ lại:", (root / "tool20.py").read_text().strip() == "VERSION = 3")
    print("Working tree sạch:", git(root, "status", "--porcelain") == "")
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Merge nhánh feature chứa hai sửa đổi vào main cũng có hai sửa đổi KHÁC file, rồi kiểm merge sạch.
# Dữ liệu: 20 file tool01..20; feature sửa 01/02 lên VERSION=2; main sửa 19/20 lên VERSION=3; hai phía không sửa chung file.
# subprocess cho phép chạy lệnh Git CLI từ Python, thay vì mô phỏng phản hồi Git.
import subprocess
# tempfile cấp thư mục tạm để ví dụ không đụng repository thật của người học.
import tempfile
# Path đại diện đường dẫn theo hệ điều hành và hỗ trợ thao tác file với toán tử /.
from pathlib import Path

# Định nghĩa hàm trợ giúp chạy Git; *args thu các phần đối số khác nhau thành tuple, root chỉ định thư mục repository tạm.
def git(root, *args):
    # subprocess.run() chạy chương trình git theo list đối số; không dùng shell=True nên tránh diễn giải chuỗi bởi shell.
    # cwd=root đặt thư mục làm việc của Git đúng repository tạm, không vô tình thao tác trong dự án thật.
    # check=True phát sinh CalledProcessError nếu lệnh Git trả mã lỗi, tránh tiếp tục với kết quả thất bại.
    return subprocess.run(["git", *args], cwd=root, check=True,
                          # text=True giải mã stdout thành chuỗi văn bản, không phải bytes.
                          # capture_output=True thu stdout/stderr để xử lý trong Python thay vì in lẫn lên terminal.
                          # stdout là đầu ra chuẩn của lệnh Git; strip() bỏ khoảng trắng/xuống dòng hai đầu cho dễ so sánh.
                          text=True, capture_output=True).stdout.strip()

# TemporaryDirectory() tạo thư mục tạm và tự dọn toàn bộ repository khi ra khỏi khối with, kể cả khi có lỗi.
with tempfile.TemporaryDirectory() as temp:
    # Đổi chuỗi đường dẫn thư mục tạm thành Path để ghép tên file.
    root = Path(temp)
    # git init -b main tạo repository mới với nhánh chính main; -q giảm thông báo, chỉ trong root tạm.
    git(root, "init", "-q", "-b", "main")
    git(root, "config", "user.name", "Lesson Tester")
    git(root, "config", "user.email", "lesson@example.invalid")
    # Sinh chỉ số 1..20 để tạo 20 script nguồn.
    for i in range(1,21):
        # Mỗi file ban đầu là VERSION=1, chung cho cả hai nhánh.
        (root / f"tool{i:02d}.py").write_text("VERSION = 1\n", encoding="utf-8")
    git(root, "add", ".")
    # Commit cơ sở lưu trạng thái 20 file giống nhau trước khi tách nhánh.
    git(root, "commit", "-q", "-m", "base")
    # Tạo/chuyển nhánh feature từ commit base; -q ẩn thông báo.
    git(root, "switch", "-q", "-c", "feature")
    # Tuple (1,2) chọn đúng hai file sửa trong feature.
    for i in (1,2):
        # Ghi VERSION=2 trong hai file đầu của feature.
        (root / f"tool{i:02d}.py").write_text("VERSION = 2\n", encoding="utf-8")
    git(root, "add", ".")
    # Commit những thay đổi feature đã stage.
    git(root, "commit", "-q", "-m", "feature edits")
    # Chuyển sang main trước khi sửa cặp file khác.
    git(root, "switch", "-q", "main")
    # Chỉ sửa tool19 và tool20 trên main để tránh đụng hai file của feature.
    for i in (19,20):
        # Ghi VERSION=3 vào hai file cuối của nhánh main.
        (root / f"tool{i:02d}.py").write_text("VERSION = 3\n", encoding="utf-8")
    git(root, "add", ".")
    # Tạo commit main độc lập với commit feature.
    git(root, "commit", "-q", "-m", "main edits")
    # merge feature vào main; --no-ff ép tạo MERGE COMMIT kể cả khi có thể fast-forward; -m đặt tiêu đề, -q ẩn log.
    git(root, "merge", "-q", "--no-ff", "feature", "-m", "merge feature")
    # rev-list --parents -n 1 HEAD in commit mới nhất và các hash cha; merge hai nhánh có hai cha.
    parents = git(root, "rev-list", "--parents", "-n", "1", "HEAD").split()
    # ls-files liệt kê 20 file đang được theo dõi sau merge.
    print("File:", len(git(root, "ls-files").splitlines()))
    # Đếm mọi commit trong lịch sử có thể tới từ HEAD, bao gồm base, hai commit nhánh và merge.
    print("Commit trong lịch sử:", git(root, "rev-list", "--count", "HEAD"))
    # List gồm hash merge và HAI hash cha nên tổng ba phần tử; True chứng minh đây là merge commit.
    print("Merge có hai cha:", len(parents) == 3)
    # Kiểm script feature còn VERSION=2 trong main sau merge, strip() chỉ loại ký tự trắng khi đọc.
    print("Sửa feature giữ lại:", (root / "tool01.py").read_text().strip() == "VERSION = 2")
    # Kiểm thay đổi main VERSION=3 cũng còn sau merge.
    print("Sửa main giữ lại:", (root / "tool20.py").read_text().strip() == "VERSION = 3")
    # Trạng thái porcelain rỗng nghĩa không có sửa đổi chưa commit/untracked, working tree sạch.
    print("Working tree sạch:", git(root, "status", "--porcelain") == "")
```

**Lệnh Git tương ứng:** Chỉ thực hành trong repository thử, không chạy vào repository đang làm việc.

**No Note — Không chú thích**

```bash
git merge --no-ff feature
```

**Code có chú thích — Giải thích từng bước**

```bash
git merge --no-ff feature
```

**Kết quả khi chạy:**

```text
File: 20
Commit trong lịch sử: 4
Merge có hai cha: True
Sửa feature giữ lại: True
Sửa main giữ lại: True
Working tree sạch: True
```

Toàn bộ thí nghiệm chạy trong **thư mục tạm có repo Git riêng**; lệnh không thao tác lên repository dự án của người học. Khi merge xảy ra conflict, phải dừng xử lý dựa trên bằng chứng thay vì tự bỏ thay đổi.

## 6. Sai lầm thường gặp

- `git add` chỉ stage, không tạo commit; `git commit` chỉ ghi nội dung đã stage.
- `git diff` xem phần chưa stage, `git diff --cached` xem phần đã stage.
- Tạo nhánh khác không có nghĩa đã đẩy nhánh lên remote; push cần có quyền truy cập.
- Đường dẫn remote có thể tồn tại dù chưa có quyền push hoặc chưa xác thực.
- `git pull --ff-only` từ chối trường hợp phải merge/rebase; không nên `reset --hard` chỉ để bỏ thông báo lệch lịch sử.
- Đầu ra các lệnh Git phụ thuộc repository và trạng thái; không được coi hash ví dụ là kết quả của dự án khác.

## 7. Trắc nghiệm

**Q1. What does a Git repository contain? | Repository Git chứa gì?**

A. Project content and version history metadata | Nội dung dự án và siêu dữ liệu lịch sử phiên bản

B. A recorded snapshot of staged content | Bản ghi trạng thái từ nội dung đã stage

C. A movable reference to a commit | Tham chiếu di chuyển trỏ đến commit

D. A named reference to another repository URL | Tên tham chiếu đến URL repository khác

**Đáp án: A**

**Giải thích:** Git lưu trạng thái và tham chiếu trong `.git`, không chỉ gom file vào thư mục. Nó là phạm vi quản lý lịch sử dự án, không phải một commit hay nhánh riêng lẻ.


**Q2. What is a commit? | Commit là gì?**

A. Project content and version history metadata | Nội dung dự án và siêu dữ liệu lịch sử phiên bản

B. A recorded snapshot of staged content | Bản ghi trạng thái từ nội dung đã stage

C. A movable reference to a commit | Tham chiếu di chuyển trỏ đến commit

D. A named reference to another repository URL | Tên tham chiếu đến URL repository khác

**Đáp án: B**

**Giải thích:** Commit lưu nội dung đã stage cùng mã định danh và thông điệp. Chỉnh file mà chưa stage không tự làm thay đổi nội dung của commit kế.


**Q3. What is a branch? | Nhánh Git là gì?**

A. Project content and version history metadata | Nội dung dự án và siêu dữ liệu lịch sử phiên bản

B. A recorded snapshot of staged content | Bản ghi trạng thái từ nội dung đã stage

C. A movable reference to a commit | Tham chiếu di chuyển trỏ đến commit

D. A named reference to another repository URL | Tên tham chiếu đến URL repository khác

**Đáp án: C**

**Giải thích:** Tạo nhánh không sao chép vật lý toàn bộ file sang thư mục khác. Nhánh dịch chuyển khi có commit mới, còn commit đã tạo là một bản ghi bất biến.


**Q4. What is a remote? | Remote là gì?**

A. Project content and version history metadata | Nội dung dự án và siêu dữ liệu lịch sử phiên bản

B. A recorded snapshot of staged content | Bản ghi trạng thái từ nội dung đã stage

C. A movable reference to a commit | Tham chiếu di chuyển trỏ đến commit

D. A named reference to another repository URL | Tên tham chiếu đến URL repository khác

**Đáp án: D**

**Giải thích:** Remote chỉ định địa chỉ đồng bộ; quyền truy cập được kiểm riêng. Đổi URL origin không tự xác thực người dùng hay tạo commit ở remote.


**Q5. What does `git status` show? | `git status` hiển thị gì?**

A. Untracked, staged and working changes | File chưa theo dõi, đã stage và đang sửa

B. Stages current changes to that path | Stage thay đổi hiện tại của đường dẫn đó

C. Records staged state with a message | Lưu phần đã stage thành commit có thông điệp

D. Compact commit history | Lịch sử commit rút gọn

**Đáp án: A**

**Giải thích:** Lệnh chỉ báo trạng thái, không tạo commit. Hãy xem status trước add/commit để phát hiện file chưa theo dõi hoặc chưa stage.


**Q6. What does `git add file.py` do? | `git add file.py` làm gì?**

A. Untracked, staged and working changes | File chưa theo dõi, đã stage và đang sửa

B. Stages current changes to that path | Stage thay đổi hiện tại của đường dẫn đó

C. Records staged state with a message | Lưu phần đã stage thành commit có thông điệp

D. Compact commit history | Lịch sử commit rút gọn

**Đáp án: B**

**Giải thích:** Stage chuẩn bị cho commit, không phải tải lên remote. Sau `git add`, xem `git diff --cached` để chắc chỉ những phần mong muốn được đưa vào stage.


**Q7. What does `git commit -m ...` do? | `git commit -m ...` làm gì?**

A. Untracked, staged and working changes | File chưa theo dõi, đã stage và đang sửa

B. Stages current changes to that path | Stage thay đổi hiện tại của đường dẫn đó

C. Records staged state with a message | Lưu phần đã stage thành commit có thông điệp

D. Compact commit history | Lịch sử commit rút gọn

**Đáp án: C**

**Giải thích:** Sau commit vẫn có thể còn sửa đổi chưa stage. Sửa đổi không nằm trong index sẽ không thuộc commit cho tới khi stage lại.


**Q8. What does `git log --oneline` show? | `git log --oneline` hiển thị gì?**

A. Untracked, staged and working changes | File chưa theo dõi, đã stage và đang sửa

B. Stages current changes to that path | Stage thay đổi hiện tại của đường dẫn đó

C. Records staged state with a message | Lưu phần đã stage thành commit có thông điệp

D. Compact commit history | Lịch sử commit rút gọn

**Đáp án: D**

**Giải thích:** Hiển thị hash và tiêu đề, không phải diff chi tiết. Muốn xem thay đổi từng dòng phải dùng diff hoặc show, không chỉ đọc tiêu đề log.


**Q9. What does `git switch -c name` do? | `git switch -c name` làm gì?**

A. Creates and checks out a new branch | Tạo và chuyển sang nhánh mới

B. Name of current branch | Tên nhánh hiện tại

C. Unstaged differences for that path | Khác biệt chưa stage của đường dẫn đó

D. Staged differences against last commit | Khác biệt đã stage so với commit gần nhất

**Đáp án: A**

**Giải thích:** Nhánh bắt đầu từ commit hiện tại nếu không chỉ định mốc khác. Nếu tên đã tồn tại thì tạo nhánh mới sẽ báo lỗi; khi đó cần chuyển nhánh thay vì tạo tiếp.


**Q10. What does `git branch --show-current` return? | `git branch --show-current` trả gì?**

A. Creates and checks out a new branch | Tạo và chuyển sang nhánh mới

B. Name of current branch | Tên nhánh hiện tại

C. Unstaged differences for that path | Khác biệt chưa stage của đường dẫn đó

D. Staged differences against last commit | Khác biệt đã stage so với commit gần nhất

**Đáp án: B**

**Giải thích:** Giúp tránh commit trên nhánh không mong muốn. Nếu đang ở detached HEAD, có thể không có tên nhánh hiện tại để in.


**Q11. What does `git diff -- file` show? | `git diff -- file` hiển thị gì?**

A. Creates and checks out a new branch | Tạo và chuyển sang nhánh mới

B. Name of current branch | Tên nhánh hiện tại

C. Unstaged differences for that path | Khác biệt chưa stage của đường dẫn đó

D. Staged differences against last commit | Khác biệt đã stage so với commit gần nhất

**Đáp án: C**

**Giải thích:** diff thường so working tree với staging area. Với nội dung đã stage, `git diff` thường không hiện; phải xem diff cached.


**Q12. What does `git diff --cached` show? | `git diff --cached` hiển thị gì?**

A. Creates and checks out a new branch | Tạo và chuyển sang nhánh mới

B. Name of current branch | Tên nhánh hiện tại

C. Unstaged differences for that path | Khác biệt chưa stage của đường dẫn đó

D. Staged differences against last commit | Khác biệt đã stage so với commit gần nhất

**Đáp án: D**

**Giải thích:** Giúp xem nội dung đã stage trước khi commit. Nó cho biết nội dung sẽ vào commit, khác phần mới chỉ đang sửa ngoài working tree.


**Q13. What does `git fetch` do? | `git fetch` làm gì?**

A. Downloads remote refs and objects without merging | Tải tham chiếu/dữ liệu remote nhưng chưa merge

B. Sends local refs and commits to remote if permitted | Gửi tham chiếu/commit lên remote nếu có quyền

C. To isolate work before integration | Để tách công việc trước khi tích hợp

D. The index of content selected for next commit | Chỉ mục nội dung được chọn cho commit kế

**Đáp án: A**

**Giải thích:** Fetch cập nhật thông tin remote nhưng chưa nhập vào nhánh đang làm. Fetch có thể cập nhật nhánh theo dõi remote nhưng không nhập chúng vào nhánh local đang đứng.


**Q14. What does `git push` do? | `git push` làm gì?**

A. Downloads remote refs and objects without merging | Tải tham chiếu/dữ liệu remote nhưng chưa merge

B. Sends local refs and commits to remote if permitted | Gửi tham chiếu/commit lên remote nếu có quyền

C. To isolate work before integration | Để tách công việc trước khi tích hợp

D. The index of content selected for next commit | Chỉ mục nội dung được chọn cho commit kế

**Đáp án: B**

**Giải thích:** Push không tự stage hoặc commit thay đổi chưa lưu. Các sửa đổi chưa commit phải được ghi vào lịch sử trước khi push chia sẻ bình thường.


**Q15. Why use a feature branch? | Vì sao dùng nhánh tính năng?**

A. Downloads remote refs and objects without merging | Tải tham chiếu/dữ liệu remote nhưng chưa merge

B. Sends local refs and commits to remote if permitted | Gửi tham chiếu/commit lên remote nếu có quyền

C. To isolate work before integration | Để tách công việc trước khi tích hợp

D. The index of content selected for next commit | Chỉ mục nội dung được chọn cho commit kế

**Đáp án: C**

**Giải thích:** Tách nhánh cho phép xem thử trước khi ảnh hưởng main. Chỉ nên merge nhánh tính năng sau khi kiểm tra đúng phần thay đổi dự định.


**Q16. What is staging area? | Staging area là gì?**

A. Downloads remote refs and objects without merging | Tải tham chiếu/dữ liệu remote nhưng chưa merge

B. Sends local refs and commits to remote if permitted | Gửi tham chiếu/commit lên remote nếu có quyền

C. To isolate work before integration | Để tách công việc trước khi tích hợp

D. The index of content selected for next commit | Chỉ mục nội dung được chọn cho commit kế

**Đáp án: D**

**Giải thích:** Nội dung đã stage có thể khác sửa đổi mới trong working tree. Index tách phần được ghi vào commit với những sửa đổi khác vẫn còn ở máy.


**Q17. What does `git pull --ff-only` require? | `git pull --ff-only` đòi hỏi gì?**

A. A fast-forward update without a merge commit | Có thể tiến thẳng lịch sử mà không tạo merge commit

B. No; authentication and permissions are separate | Không; xác thực và quyền là chuyện khác

C. No, they need to be staged again | Không, cần stage lại phần sửa mới

D. Review status and staged diff | Xem status và diff đã stage

**Đáp án: A**

**Giải thích:** Nó từ chối lịch sử cần tích hợp kiểu không fast-forward. Lịch sử đã phân nhánh cần quyết định tích hợp riêng; ff-only không tự xóa commit.


**Q18. Does setting origin grant push permissions? | Đặt origin có tự cấp quyền push không?**

A. A fast-forward update without a merge commit | Có thể tiến thẳng lịch sử mà không tạo merge commit

B. No; authentication and permissions are separate | Không; xác thực và quyền là chuyện khác

C. No, they need to be staged again | Không, cần stage lại phần sửa mới

D. Review status and staged diff | Xem status và diff đã stage

**Đáp án: B**

**Giải thích:** Có thể cấu hình URL dù không có quyền ghi. Quyền do máy chủ và thông tin đăng nhập quyết định, không phải do tên remote trên máy.


**Q19. Can git commit include edits made after the last git add automatically? | git commit có tự chứa sửa đổi sau lần git add cuối không?**

A. A fast-forward update without a merge commit | Có thể tiến thẳng lịch sử mà không tạo merge commit

B. No; authentication and permissions are separate | Không; xác thực và quyền là chuyện khác

C. No, they need to be staged again | Không, cần stage lại phần sửa mới

D. Review status and staged diff | Xem status và diff đã stage

**Đáp án: C**

**Giải thích:** Commit lưu trạng thái index, có thể cũ hơn nội dung đang sửa. Stage lại sẽ chụp phiên bản mới; nếu không commit dùng bản đã stage cũ.


**Q20. How should a developer check changes before committing? | Nên kiểm thay đổi trước commit bằng cách nào?**

A. A fast-forward update without a merge commit | Có thể tiến thẳng lịch sử mà không tạo merge commit

B. No; authentication and permissions are separate | Không; xác thực và quyền là chuyện khác

C. No, they need to be staged again | Không, cần stage lại phần sửa mới

D. Review status and staged diff | Xem status và diff đã stage

**Đáp án: D**

**Giải thích:** Kiểm tra giúp phát hiện file hoặc dòng thay đổi ngoài ý muốn. Nếu diff đã stage có bí mật hoặc file ngoài phạm vi, hãy bỏ stage hoặc sửa trước khi commit.

## 8. Nối sang bài tiếp

`File/Project → git init/add/commit → branch → pull/push → Review`.

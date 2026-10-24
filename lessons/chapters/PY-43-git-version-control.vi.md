# PY-43 — Git: quản lý phiên bản và hợp tác trên mã nguồn


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Repository** — kho mã nguồn; **Commit** — bản ghi thay đổi.

`File/Project → git init/add/commit → branch → pull/push → Review`

Bài này hệ thống hóa kiến thức đã học thành các thao tác thực hành có đầu vào và đầu ra rõ ràng.

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

```bash
git status
```

**Kết quả có thể quan sát:** Trạng thái hiển thị phụ thuộc file đang sửa và các commit hiện có; xem phần Changes not staged, Staged, Untracked.

### 4.2. Commit — Bản chụp các thay đổi đã stage

**Từ vựng trong mục:** **Commit**.

Commit ghi lại một trạng thái của những file đã **stage** vào lịch sử cùng tác giả, thời gian và thông điệp. Quy trình `git add lesson.py` đưa bản đang chọn vào staging area, sau đó `git commit -m ...` tạo commit. Nếu sửa file thêm **sau khi stage**, phần sửa mới chưa tự nằm trong commit. `git log -1 --oneline` xem commit gần nhất; mã hash phụ thuộc repository.

```bash
git log -1 --oneline
```

**Kết quả có thể quan sát:** Lệnh in mã commit rút gọn và thông điệp của bản gần nhất nếu dự án có commit; không có một mã cố định.

### 4.3. Branch — Nhánh để phát triển song song

**Từ vựng trong mục:** **Branch**.

Branch là một **tham chiếu đến commit**, giúp làm tính năng riêng mà không làm thay đổi ngay `main`. `git switch -c feature/score` tạo nhánh mới và chuyển sang nó từ commit hiện tại; code mới chỉ có trên nhánh đó cho tới khi được merge. Để tránh nhầm, kiểm tra `git branch --show-current` trước khi làm; tên nhánh này là ví dụ, không phải chính sách của mọi nhóm.

```bash
git switch -c feature/score
git branch --show-current
```

**Kết quả có thể quan sát:** Sau khi tạo thành công, lệnh sau in `feature/score`; lần chạy tiếp sẽ báo nhánh đã tồn tại.

### 4.4. Remote — Liên kết đến kho Git ở nơi khác

**Từ vựng trong mục:** **Remote**.

Remote là một tên tham chiếu đến địa chỉ repository khác, thường tên `origin` dùng cho kho trên GitHub. `git remote -v` liệt kê địa chỉ fetch/push đang cấu hình; nó không tự chứng minh đã đăng nhập hay có quyền push. `git fetch` tải tham chiếu từ remote, `git pull --ff-only` chỉ nhận thay đổi khi có thể đi thẳng không tạo merge commit, còn `git push` gửi commit nếu có quyền.

```bash
git remote -v
```

**Kết quả có thể quan sát:** Lệnh hiển thị tên và URL remote đã cấu hình; repository không có remote sẽ không in dòng nào.

## 5. Năm tình huống ứng dụng

### Tình huống 1 — Kiểm file trước khi commit

**Từ vựng trong mục:** **Git** — quản lý phiên bản; **Terminal** — cửa sổ lệnh.

**Tình huống thực tế:** Học viên vừa chỉnh `lesson.py` trong repository Git của bài tập và muốn biết file đang thay đổi hay đã được stage. Thao tác phải không sửa file và không tạo commit.

**Vì sao chọn cách giải này?** `git status` chỉ đọc trạng thái làm việc và staging area, an toàn để kiểm trước khi lưu.

**Quy trình giải:**

1. Mở terminal tại root repository.
2. Chạy `git status` và đọc phần Changes not staged / Changes to be committed.
3. Nếu thấy file ngoài dự kiến, kiểm tra trước khi stage.

```bash
git status
```

**Kết quả có thể quan sát:** Thông báo trạng thái phụ thuộc repository; lệnh không tự lưu thay đổi.

### Tình huống 2 — Chỉ lưu script đã sửa

**Từ vựng trong mục:** **Git** — quản lý phiên bản; **Terminal** — cửa sổ lệnh.

**Tình huống thực tế:** Dự án có `lesson.py` mới được chỉnh và các file khác chưa sẵn sàng. Học viên chỉ muốn tạo commit chứa thay đổi của `lesson.py`.

**Vì sao chọn cách giải này?** Stage cụ thể file trước để tránh commit nhầm thay đổi ngoài phạm vi.

**Quy trình giải:**

1. Chạy `git diff -- lesson.py` xem nội dung thay đổi.
2. Stage `lesson.py`, kiểm `git diff --cached -- lesson.py`.
3. Commit với thông điệp ngắn rồi kiểm lịch sử.

```bash
git add lesson.py
git diff --cached -- lesson.py
git commit -m "lesson: update practice"
```

**Kết quả có thể quan sát:** Nếu file có thay đổi staged, commit được tạo; mã hash và thống kê file phụ thuộc repository.

### Tình huống 3 — Tạo nhánh thử thuật toán mới

**Từ vựng trong mục:** **Git** — quản lý phiên bản; **Terminal** — cửa sổ lệnh.

**Tình huống thực tế:** Nhóm thực hành muốn làm bản thử PCA mà vẫn giữ `main` ổn định; dự án hiện đang ở nhánh main và tên `experiment/pca` chưa tồn tại.

**Vì sao chọn cách giải này?** `git switch -c` tạo nhánh riêng từ vị trí hiện tại và chuyển sang nhánh đó.

**Quy trình giải:**

1. Kiểm tra nhánh đang đứng.
2. Tạo và chuyển nhánh thử với tên chưa tồn tại.
3. Kiểm tên nhánh hiện tại trước khi sửa code.

```bash
git switch -c experiment/pca
git branch --show-current
```

**Kết quả có thể quan sát:** Lệnh thứ hai in `experiment/pca` nếu tạo nhánh thành công.

### Tình huống 4 — Đọc năm commit gần nhất

**Từ vựng trong mục:** **Git** — quản lý phiên bản; **Terminal** — cửa sổ lệnh.

**Tình huống thực tế:** Repository bài học đã có ít nhất năm commit. Người phụ trách muốn xem những thay đổi gần nhất để tìm mã commit cần đối chiếu.

**Vì sao chọn cách giải này?** `git log --oneline -5` hiển thị commit rút gọn theo thời gian, không thay đổi code.

**Quy trình giải:**

1. Vào đúng repository.
2. Chạy log tối đa năm commit.
3. Đọc hash và thông điệp để chọn bản cần kiểm tra.

```bash
git log --oneline -5
```

**Kết quả có thể quan sát:** In tối đa năm dòng hash và thông điệp; giá trị thay đổi theo lịch sử thật.

### Tình huống 5 — So nội dung chưa stage

**Từ vựng trong mục:** **Git** — quản lý phiên bản; **Terminal** — cửa sổ lệnh.

**Tình huống thực tế:** Một sinh viên mới sửa `lesson.py` nhưng chưa stage. Trước khi commit cần xem chính xác dòng nào bị thêm hoặc xóa.

**Vì sao chọn cách giải này?** `git diff -- lesson.py` so working tree với phần đã stage, tránh đưa nhầm sửa đổi vào lịch sử.

**Quy trình giải:**

1. Đảm bảo file đang có thay đổi chưa stage.
2. Chạy `git diff` giới hạn theo đường dẫn.
3. Đọc các dòng dấu +/− rồi quyết định có stage không.

```bash
git diff -- lesson.py
```

**Kết quả có thể quan sát:** Hiển thị diff nếu có phần chưa stage; không in gì nếu không có khác biệt tương ứng.

## 6. Sai lầm thường gặp

- `git add` chỉ stage, không tạo commit; `git commit` chỉ ghi nội dung đã stage.
- `git diff` xem phần chưa stage, `git diff --cached` xem phần đã stage.
- Tạo nhánh khác không có nghĩa đã đẩy nhánh lên remote; push cần có quyền truy cập.
- Đường dẫn remote có thể tồn tại dù chưa có quyền push hoặc chưa xác thực.
- `git pull --ff-only` từ chối trường hợp phải merge/rebase; không nên `reset --hard` chỉ để bỏ thông báo lệch lịch sử.
- Đầu ra các lệnh Git phụ thuộc repository và trạng thái; không được coi hash ví dụ là kết quả của dự án khác.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Q1. What does a Git repository contain? — Repository Git chứa gì?**

A. Project content and version history metadata — Nội dung dự án và siêu dữ liệu lịch sử phiên bản

B. A recorded snapshot of staged content — Bản ghi trạng thái từ nội dung đã stage

C. A movable reference to a commit — Tham chiếu di chuyển trỏ đến commit

D. A named reference to another repository URL — Tên tham chiếu đến URL repository khác

**Q2. What is a commit? — Commit là gì?**

A. Project content and version history metadata — Nội dung dự án và siêu dữ liệu lịch sử phiên bản

B. A recorded snapshot of staged content — Bản ghi trạng thái từ nội dung đã stage

C. A movable reference to a commit — Tham chiếu di chuyển trỏ đến commit

D. A named reference to another repository URL — Tên tham chiếu đến URL repository khác

**Q3. What is a branch? — Nhánh Git là gì?**

A. Project content and version history metadata — Nội dung dự án và siêu dữ liệu lịch sử phiên bản

B. A recorded snapshot of staged content — Bản ghi trạng thái từ nội dung đã stage

C. A movable reference to a commit — Tham chiếu di chuyển trỏ đến commit

D. A named reference to another repository URL — Tên tham chiếu đến URL repository khác

**Q4. What is a remote? — Remote là gì?**

A. Project content and version history metadata — Nội dung dự án và siêu dữ liệu lịch sử phiên bản

B. A recorded snapshot of staged content — Bản ghi trạng thái từ nội dung đã stage

C. A movable reference to a commit — Tham chiếu di chuyển trỏ đến commit

D. A named reference to another repository URL — Tên tham chiếu đến URL repository khác

**Q5. What does `git status` show? — `git status` hiển thị gì?**

A. Untracked, staged and working changes — File chưa theo dõi, đã stage và đang sửa

B. Stages current changes to that path — Stage thay đổi hiện tại của đường dẫn đó

C. Records staged state with a message — Lưu phần đã stage thành commit có thông điệp

D. Compact commit history — Lịch sử commit rút gọn

**Q6. What does `git add file.py` do? — `git add file.py` làm gì?**

A. Untracked, staged and working changes — File chưa theo dõi, đã stage và đang sửa

B. Stages current changes to that path — Stage thay đổi hiện tại của đường dẫn đó

C. Records staged state with a message — Lưu phần đã stage thành commit có thông điệp

D. Compact commit history — Lịch sử commit rút gọn

**Q7. What does `git commit -m ...` do? — `git commit -m ...` làm gì?**

A. Untracked, staged and working changes — File chưa theo dõi, đã stage và đang sửa

B. Stages current changes to that path — Stage thay đổi hiện tại của đường dẫn đó

C. Records staged state with a message — Lưu phần đã stage thành commit có thông điệp

D. Compact commit history — Lịch sử commit rút gọn

**Q8. What does `git log --oneline` show? — `git log --oneline` hiển thị gì?**

A. Untracked, staged and working changes — File chưa theo dõi, đã stage và đang sửa

B. Stages current changes to that path — Stage thay đổi hiện tại của đường dẫn đó

C. Records staged state with a message — Lưu phần đã stage thành commit có thông điệp

D. Compact commit history — Lịch sử commit rút gọn

**Q9. What does `git switch -c name` do? — `git switch -c name` làm gì?**

A. Creates and checks out a new branch — Tạo và chuyển sang nhánh mới

B. Name of current branch — Tên nhánh hiện tại

C. Unstaged differences for that path — Khác biệt chưa stage của đường dẫn đó

D. Staged differences against last commit — Khác biệt đã stage so với commit gần nhất

**Q10. What does `git branch --show-current` return? — `git branch --show-current` trả gì?**

A. Creates and checks out a new branch — Tạo và chuyển sang nhánh mới

B. Name of current branch — Tên nhánh hiện tại

C. Unstaged differences for that path — Khác biệt chưa stage của đường dẫn đó

D. Staged differences against last commit — Khác biệt đã stage so với commit gần nhất

**Q11. What does `git diff -- file` show? — `git diff -- file` hiển thị gì?**

A. Creates and checks out a new branch — Tạo và chuyển sang nhánh mới

B. Name of current branch — Tên nhánh hiện tại

C. Unstaged differences for that path — Khác biệt chưa stage của đường dẫn đó

D. Staged differences against last commit — Khác biệt đã stage so với commit gần nhất

**Q12. What does `git diff --cached` show? — `git diff --cached` hiển thị gì?**

A. Creates and checks out a new branch — Tạo và chuyển sang nhánh mới

B. Name of current branch — Tên nhánh hiện tại

C. Unstaged differences for that path — Khác biệt chưa stage của đường dẫn đó

D. Staged differences against last commit — Khác biệt đã stage so với commit gần nhất

**Q13. What does `git fetch` do? — `git fetch` làm gì?**

A. Downloads remote refs and objects without merging — Tải tham chiếu/dữ liệu remote nhưng chưa merge

B. Sends local refs and commits to remote if permitted — Gửi tham chiếu/commit lên remote nếu có quyền

C. To isolate work before integration — Để tách công việc trước khi tích hợp

D. The index of content selected for next commit — Chỉ mục nội dung được chọn cho commit kế

**Q14. What does `git push` do? — `git push` làm gì?**

A. Downloads remote refs and objects without merging — Tải tham chiếu/dữ liệu remote nhưng chưa merge

B. Sends local refs and commits to remote if permitted — Gửi tham chiếu/commit lên remote nếu có quyền

C. To isolate work before integration — Để tách công việc trước khi tích hợp

D. The index of content selected for next commit — Chỉ mục nội dung được chọn cho commit kế

**Q15. Why use a feature branch? — Vì sao dùng nhánh tính năng?**

A. Downloads remote refs and objects without merging — Tải tham chiếu/dữ liệu remote nhưng chưa merge

B. Sends local refs and commits to remote if permitted — Gửi tham chiếu/commit lên remote nếu có quyền

C. To isolate work before integration — Để tách công việc trước khi tích hợp

D. The index of content selected for next commit — Chỉ mục nội dung được chọn cho commit kế

**Q16. What is staging area? — Staging area là gì?**

A. Downloads remote refs and objects without merging — Tải tham chiếu/dữ liệu remote nhưng chưa merge

B. Sends local refs and commits to remote if permitted — Gửi tham chiếu/commit lên remote nếu có quyền

C. To isolate work before integration — Để tách công việc trước khi tích hợp

D. The index of content selected for next commit — Chỉ mục nội dung được chọn cho commit kế

**Q17. What does `git pull --ff-only` require? — `git pull --ff-only` đòi hỏi gì?**

A. A fast-forward update without a merge commit — Có thể tiến thẳng lịch sử mà không tạo merge commit

B. No; authentication and permissions are separate — Không; xác thực và quyền là chuyện khác

C. No, they need to be staged again — Không, cần stage lại phần sửa mới

D. Review status and staged diff — Xem status và diff đã stage

**Q18. Does setting origin grant push permissions? — Đặt origin có tự cấp quyền push không?**

A. A fast-forward update without a merge commit — Có thể tiến thẳng lịch sử mà không tạo merge commit

B. No; authentication and permissions are separate — Không; xác thực và quyền là chuyện khác

C. No, they need to be staged again — Không, cần stage lại phần sửa mới

D. Review status and staged diff — Xem status và diff đã stage

**Q19. Can git commit include edits made after the last git add automatically? — git commit có tự chứa sửa đổi sau lần git add cuối không?**

A. A fast-forward update without a merge commit — Có thể tiến thẳng lịch sử mà không tạo merge commit

B. No; authentication and permissions are separate — Không; xác thực và quyền là chuyện khác

C. No, they need to be staged again — Không, cần stage lại phần sửa mới

D. Review status and staged diff — Xem status và diff đã stage

**Q20. How should a developer check changes before committing? — Nên kiểm thay đổi trước commit bằng cách nào?**

A. A fast-forward update without a merge commit — Có thể tiến thẳng lịch sử mà không tạo merge commit

B. No; authentication and permissions are separate — Không; xác thực và quyền là chuyện khác

C. No, they need to be staged again — Không, cần stage lại phần sửa mới

D. Review status and staged diff — Xem status và diff đã stage

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **A** | Git tracks snapshots and references in `.git`, not merely a folder of files. | Git lưu trạng thái và tham chiếu trong `.git`, không chỉ gom file vào thư mục. |
| Q2 | **B** | A commit represents indexed content and has an identity and message. | Commit lưu nội dung đã stage cùng mã định danh và thông điệp. |
| Q3 | **C** | Creating a branch does not clone all files into a separate physical folder. | Tạo nhánh không sao chép vật lý toàn bộ file sang thư mục khác. |
| Q4 | **D** | Remote configuration tells Git where to fetch/push; rights are separate. | Remote chỉ định địa chỉ đồng bộ; quyền truy cập được kiểm riêng. |
| Q5 | **A** | It reports repository state without creating a commit. | Lệnh chỉ báo trạng thái, không tạo commit. |
| Q6 | **B** | Staging prepares content for the next commit, not remote upload. | Stage chuẩn bị cho commit, không phải tải lên remote. |
| Q7 | **C** | The working tree can still contain unstaged edits. | Sau commit vẫn có thể còn sửa đổi chưa stage. |
| Q8 | **D** | It displays commit identifiers and subjects, not file diffs. | Hiển thị hash và tiêu đề, không phải diff chi tiết. |
| Q9 | **A** | The branch begins at the current commit unless another start point is given. | Nhánh bắt đầu từ commit hiện tại nếu không chỉ định mốc khác. |
| Q10 | **B** | It helps avoid committing on the wrong branch. | Giúp tránh commit trên nhánh không mong muốn. |
| Q11 | **C** | Plain diff compares working content with the index. | diff thường so working tree với staging area. |
| Q12 | **D** | It previews the indexed content likely to enter a commit. | Giúp xem nội dung đã stage trước khi commit. |
| Q13 | **A** | Fetching updates local knowledge of remote history; work branch remains unchanged. | Fetch cập nhật thông tin remote nhưng chưa nhập vào nhánh đang làm. |
| Q14 | **B** | It does not stage or commit working changes automatically. | Push không tự stage hoặc commit thay đổi chưa lưu. |
| Q15 | **C** | Isolation helps review experiments without directly changing main. | Tách nhánh cho phép xem thử trước khi ảnh hưởng main. |
| Q16 | **D** | Staged content can differ from later working-tree edits. | Nội dung đã stage có thể khác sửa đổi mới trong working tree. |
| Q17 | **A** | It refuses histories requiring non-fast-forward integration. | Nó từ chối lịch sử cần tích hợp kiểu không fast-forward. |
| Q18 | **B** | An URL can be configured even without write access. | Có thể cấu hình URL dù không có quyền ghi. |
| Q19 | **C** | The commit records the index, which may be older than working content. | Commit lưu trạng thái index, có thể cũ hơn nội dung đang sửa. |
| Q20 | **D** | Review catches unintended files and content before recording history. | Kiểm tra giúp phát hiện file hoặc dòng thay đổi ngoài ý muốn. |

## 8. Nối sang bài tiếp

`File/Project → git init/add/commit → branch → pull/push → Review`.

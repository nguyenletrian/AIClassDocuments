# PY-43 — Git: quản lý phiên bản và hợp tác trên mã nguồn

## 1. Vị trí trong chuỗi kiến thức

`File/Project → git init/add/commit → branch → pull/push → Review`

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Ý nghĩa |
|---|---|---|
| Repository | kho mã nguồn | Nơi lưu lịch sử phiên bản |
| Commit | bản ghi thay đổi | Điểm lưu thay đổi có thông điệp |
| Branch | nhánh | Hướng phát triển độc lập |
| Remote | kho từ xa | Đường dẫn đến repository cộng tác |

## 3. Hàm và cách sử dụng

| Cú pháp | Mục đích và lựa chọn |
|---|---|
| `git status` | Xem file được sửa và đã stage hay chưa |
| `git add <file> / git commit -m` | Chọn thay đổi và tạo lịch sử có thông điệp |
| `git switch -c <branch>` | Tách nhánh thử nghiệm để không sửa nhánh chính |
| `git pull --ff-only / git push` | Đồng bộ an toàn khi lịch sử cho phép, kiểm tra remote trước |

## 4. Khái niệm liên quan và ví dụ nhỏ

### 4.1. Repository

Nơi lưu lịch sử phiên bản.

```bash
git status
```

### 4.2. Commit

Điểm lưu thay đổi có thông điệp.

```bash
git log -1
```

### 4.3. Branch

Hướng phát triển độc lập.

```bash
git branch
```

### 4.4. Remote

Đường dẫn đến repository cộng tác.

```bash
git remote -v
```

## 5. Năm tình huống thực tế

### Tình huống 1 — Kiểm trạng thái trước lưu

**Bài toán:** Kiểm trạng thái trước lưu.

**Vì sao chọn cách này?** status giúp biết có thay đổi chưa commit

**Dữ liệu:** Một repository đã git init.

```bash
git status
```

### Tình huống 2 — Lưu thay đổi bài tập

**Bài toán:** Lưu thay đổi bài tập.

**Vì sao chọn cách này?** Stage đúng file tránh commit nhầm tài liệu khác

**Dữ liệu:** File script lesson.py mới được sửa.

```bash
git add lesson.py
git commit -m "docs: add practice script"
```

### Tình huống 3 — Tạo nhánh thí nghiệm

**Bài toán:** Tạo nhánh thí nghiệm.

**Vì sao chọn cách này?** Tách công việc mới khỏi main ổn định

**Dữ liệu:** Repo bài học.

```bash
git switch -c experiment/pca
```

### Tình huống 4 — Xem lịch sử

**Bài toán:** Xem lịch sử.

**Vì sao chọn cách này?** Log giúp truy lại lần thay đổi gần nhất

**Dữ liệu:** Repo đã có ít nhất một commit.

```bash
git log --oneline -5
```

### Tình huống 5 — Xem thay đổi chưa stage

**Bài toán:** Xem thay đổi chưa stage.

**Vì sao chọn cách này?** Diff giúp kiểm tra trước khi lưu

**Dữ liệu:** Repo có file đang sửa.

```bash
git diff -- lesson.py
```

## 6. Nhầm lẫn cần tránh

Đừng sao chép lệnh khi chưa hiểu dữ liệu hoặc trạng thái môi trường; kết quả thử nghiệm không chứng minh rằng mọi máy và mọi bộ dữ liệu đều giống nhau.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ


**Q1. What is Repository? — Thuật ngữ Repository là gì?**

A. Another term is Điểm lưu thay đổi có thông điệp — Điểm lưu thay đổi có thông điệp

B. It is Nơi lưu lịch sử phiên bản — Nơi lưu lịch sử phiên bản

C. Another term is Hướng phát triển độc lập — Hướng phát triển độc lập

D. Another term is Đường dẫn đến repository cộng tác — Đường dẫn đến repository cộng tác


**Q2. What is Commit? — Thuật ngữ Commit là gì?**

A. It is Điểm lưu thay đổi có thông điệp — Điểm lưu thay đổi có thông điệp

B. Another term is Hướng phát triển độc lập — Hướng phát triển độc lập

C. Another term is Đường dẫn đến repository cộng tác — Đường dẫn đến repository cộng tác

D. Another term is Nơi lưu lịch sử phiên bản — Nơi lưu lịch sử phiên bản


**Q3. What is Branch? — Thuật ngữ Branch là gì?**

A. Another term is Đường dẫn đến repository cộng tác — Đường dẫn đến repository cộng tác

B. Another term is Nơi lưu lịch sử phiên bản — Nơi lưu lịch sử phiên bản

C. Another term is Điểm lưu thay đổi có thông điệp — Điểm lưu thay đổi có thông điệp

D. It is Hướng phát triển độc lập — Hướng phát triển độc lập


**Q4. What is Remote? — Thuật ngữ Remote là gì?**

A. Another term is Nơi lưu lịch sử phiên bản — Nơi lưu lịch sử phiên bản

B. Another term is Điểm lưu thay đổi có thông điệp — Điểm lưu thay đổi có thông điệp

C. It is Đường dẫn đến repository cộng tác — Đường dẫn đến repository cộng tác

D. Another term is Hướng phát triển độc lập — Hướng phát triển độc lập


**Q5. What is git status used for? — Cú pháp git status dùng để làm gì?**

A. A different function is for Chọn thay đổi và tạo lịch sử có thông điệp — Chọn thay đổi và tạo lịch sử có thông điệp

B. It is for Xem file được sửa và đã stage hay chưa — Xem file được sửa và đã stage hay chưa

C. A different function is for Tách nhánh thử nghiệm để không sửa nhánh chính — Tách nhánh thử nghiệm để không sửa nhánh chính

D. A different function is for Đồng bộ an toàn khi lịch sử cho phép, kiểm tra remote trước — Đồng bộ an toàn khi lịch sử cho phép, kiểm tra remote trước


**Q6. What is git add <file> / git commit -m used for? — Cú pháp git add <file> / git commit -m dùng để làm gì?**

A. It is for Chọn thay đổi và tạo lịch sử có thông điệp — Chọn thay đổi và tạo lịch sử có thông điệp

B. A different function is for Tách nhánh thử nghiệm để không sửa nhánh chính — Tách nhánh thử nghiệm để không sửa nhánh chính

C. A different function is for Đồng bộ an toàn khi lịch sử cho phép, kiểm tra remote trước — Đồng bộ an toàn khi lịch sử cho phép, kiểm tra remote trước

D. A different function is for Xem file được sửa và đã stage hay chưa — Xem file được sửa và đã stage hay chưa


**Q7. What is git switch -c <branch> used for? — Cú pháp git switch -c <branch> dùng để làm gì?**

A. A different function is for Đồng bộ an toàn khi lịch sử cho phép, kiểm tra remote trước — Đồng bộ an toàn khi lịch sử cho phép, kiểm tra remote trước

B. A different function is for Xem file được sửa và đã stage hay chưa — Xem file được sửa và đã stage hay chưa

C. A different function is for Chọn thay đổi và tạo lịch sử có thông điệp — Chọn thay đổi và tạo lịch sử có thông điệp

D. It is for Tách nhánh thử nghiệm để không sửa nhánh chính — Tách nhánh thử nghiệm để không sửa nhánh chính


**Q8. What is git pull --ff-only / git push used for? — Cú pháp git pull --ff-only / git push dùng để làm gì?**

A. A different function is for Xem file được sửa và đã stage hay chưa — Xem file được sửa và đã stage hay chưa

B. A different function is for Chọn thay đổi và tạo lịch sử có thông điệp — Chọn thay đổi và tạo lịch sử có thông điệp

C. It is for Đồng bộ an toàn khi lịch sử cho phép, kiểm tra remote trước — Đồng bộ an toàn khi lịch sử cho phép, kiểm tra remote trước

D. A different function is for Tách nhánh thử nghiệm để không sửa nhánh chính — Tách nhánh thử nghiệm để không sửa nhánh chính


**Q9. Why choose this approach in scenario 1? — Vì sao chọn cách làm trong tình huống 1?**

A. Stage đúng file tránh commit nhầm tài liệu khác — Stage đúng file tránh commit nhầm tài liệu khác

B. status giúp biết có thay đổi chưa commit — status giúp biết có thay đổi chưa commit

C. Tách công việc mới khỏi main ổn định — Tách công việc mới khỏi main ổn định

D. Log giúp truy lại lần thay đổi gần nhất — Log giúp truy lại lần thay đổi gần nhất


**Q10. Why choose this approach in scenario 2? — Vì sao chọn cách làm trong tình huống 2?**

A. Stage đúng file tránh commit nhầm tài liệu khác — Stage đúng file tránh commit nhầm tài liệu khác

B. Tách công việc mới khỏi main ổn định — Tách công việc mới khỏi main ổn định

C. Log giúp truy lại lần thay đổi gần nhất — Log giúp truy lại lần thay đổi gần nhất

D. Diff giúp kiểm tra trước khi lưu — Diff giúp kiểm tra trước khi lưu


**Q11. Why choose this approach in scenario 3? — Vì sao chọn cách làm trong tình huống 3?**

A. Log giúp truy lại lần thay đổi gần nhất — Log giúp truy lại lần thay đổi gần nhất

B. Diff giúp kiểm tra trước khi lưu — Diff giúp kiểm tra trước khi lưu

C. status giúp biết có thay đổi chưa commit — status giúp biết có thay đổi chưa commit

D. Tách công việc mới khỏi main ổn định — Tách công việc mới khỏi main ổn định


**Q12. Why choose this approach in scenario 4? — Vì sao chọn cách làm trong tình huống 4?**

A. Diff giúp kiểm tra trước khi lưu — Diff giúp kiểm tra trước khi lưu

B. status giúp biết có thay đổi chưa commit — status giúp biết có thay đổi chưa commit

C. Log giúp truy lại lần thay đổi gần nhất — Log giúp truy lại lần thay đổi gần nhất

D. Stage đúng file tránh commit nhầm tài liệu khác — Stage đúng file tránh commit nhầm tài liệu khác


**Q13. Why choose this approach in scenario 5? — Vì sao chọn cách làm trong tình huống 5?**

A. status giúp biết có thay đổi chưa commit — status giúp biết có thay đổi chưa commit

B. Diff giúp kiểm tra trước khi lưu — Diff giúp kiểm tra trước khi lưu

C. Stage đúng file tránh commit nhầm tài liệu khác — Stage đúng file tránh commit nhầm tài liệu khác

D. Tách công việc mới khỏi main ổn định — Tách công việc mới khỏi main ổn định


**Q14. What input is used in scenario 1? — Tình huống 1 sử dụng đầu vào nào?**

A. Một repository đã git init — Một repository đã git init

B. File script lesson.py mới được sửa — File script lesson.py mới được sửa

C. Repo bài học — Repo bài học

D. Repo đã có ít nhất một commit — Repo đã có ít nhất một commit


**Q15. What input is used in scenario 2? — Tình huống 2 sử dụng đầu vào nào?**

A. Repo bài học — Repo bài học

B. Repo đã có ít nhất một commit — Repo đã có ít nhất một commit

C. Repo có file đang sửa — Repo có file đang sửa

D. File script lesson.py mới được sửa — File script lesson.py mới được sửa


**Q16. What input is used in scenario 3? — Tình huống 3 sử dụng đầu vào nào?**

A. Repo đã có ít nhất một commit — Repo đã có ít nhất một commit

B. Repo có file đang sửa — Repo có file đang sửa

C. Repo bài học — Repo bài học

D. Một repository đã git init — Một repository đã git init


**Q17. What input is used in scenario 4? — Tình huống 4 sử dụng đầu vào nào?**

A. Repo có file đang sửa — Repo có file đang sửa

B. Repo đã có ít nhất một commit — Repo đã có ít nhất một commit

C. Một repository đã git init — Một repository đã git init

D. File script lesson.py mới được sửa — File script lesson.py mới được sửa


**Q18. What input is used in scenario 5? — Tình huống 5 sử dụng đầu vào nào?**

A. Repo có file đang sửa — Repo có file đang sửa

B. Một repository đã git init — Một repository đã git init

C. File script lesson.py mới được sửa — File script lesson.py mới được sửa

D. Repo bài học — Repo bài học


**Q19. What is important before executing a workflow? — Trước khi chạy workflow cần điều gì?**

A. Only count blank lines — Chỉ đếm dòng trắng

B. Only change editor theme — Chỉ đổi giao diện

C. Ignore credentials — Bỏ qua quản lý tài khoản

D. Understand source, parameters and permissions — Hiểu nguồn, tham số và quyền hạn


**Q20. What should be reported after a test? — Sau khi test cần báo cáo gì?**

A. Only a success claim — Chỉ nói thành công

B. A guess of future results — Đoán kết quả tương lai

C. Observed output, failures and limits — Đầu ra thật, lỗi và giới hạn

D. No evidence — Không cần bằng chứng

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **B** | It is Nơi lưu lịch sử phiên bản | Nơi lưu lịch sử phiên bản |
| Q2 | **A** | It is Điểm lưu thay đổi có thông điệp | Điểm lưu thay đổi có thông điệp |
| Q3 | **D** | It is Hướng phát triển độc lập | Hướng phát triển độc lập |
| Q4 | **C** | It is Đường dẫn đến repository cộng tác | Đường dẫn đến repository cộng tác |
| Q5 | **B** | It is for Xem file được sửa và đã stage hay chưa | Xem file được sửa và đã stage hay chưa |
| Q6 | **A** | It is for Chọn thay đổi và tạo lịch sử có thông điệp | Chọn thay đổi và tạo lịch sử có thông điệp |
| Q7 | **D** | It is for Tách nhánh thử nghiệm để không sửa nhánh chính | Tách nhánh thử nghiệm để không sửa nhánh chính |
| Q8 | **C** | It is for Đồng bộ an toàn khi lịch sử cho phép, kiểm tra remote trước | Đồng bộ an toàn khi lịch sử cho phép, kiểm tra remote trước |
| Q9 | **B** | status giúp biết có thay đổi chưa commit | status giúp biết có thay đổi chưa commit |
| Q10 | **A** | Stage đúng file tránh commit nhầm tài liệu khác | Stage đúng file tránh commit nhầm tài liệu khác |
| Q11 | **D** | Tách công việc mới khỏi main ổn định | Tách công việc mới khỏi main ổn định |
| Q12 | **C** | Log giúp truy lại lần thay đổi gần nhất | Log giúp truy lại lần thay đổi gần nhất |
| Q13 | **B** | Diff giúp kiểm tra trước khi lưu | Diff giúp kiểm tra trước khi lưu |
| Q14 | **A** | Một repository đã git init | Một repository đã git init |
| Q15 | **D** | File script lesson.py mới được sửa | File script lesson.py mới được sửa |
| Q16 | **C** | Repo bài học | Repo bài học |
| Q17 | **B** | Repo đã có ít nhất một commit | Repo đã có ít nhất một commit |
| Q18 | **A** | Repo có file đang sửa | Repo có file đang sửa |
| Q19 | **D** | Understand source, parameters and permissions | Hiểu nguồn, tham số và quyền hạn |
| Q20 | **C** | Observed output, failures and limits | Đầu ra thật, lỗi và giới hạn |

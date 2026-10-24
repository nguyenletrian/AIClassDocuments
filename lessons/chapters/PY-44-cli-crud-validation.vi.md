# PY-44 — Ứng dụng CLI: CRUD, kiểm tra dữ liệu và thống kê hồ sơ


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **CRUD** — tạo/đọc/sửa/xóa; **Validation** — xác minh dữ liệu.

`Dictionary/Function → CRUD → CLI → File/CSV → Data App`

Bài này hệ thống hóa kiến thức đã học thành các thao tác thực hành có đầu vào và đầu ra rõ ràng.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Ý nghĩa |
|---|---|---|
| CRUD | tạo/đọc/sửa/xóa | Bốn thao tác quản lý bản ghi |
| Validation | xác minh dữ liệu | Đảm bảo giá trị đúng giới hạn |
| Lookup | tra cứu | Tìm bản ghi qua khóa |
| Aggregate | tổng hợp | Tính chỉ số từ nhiều hồ sơ |

## 3. Hàm và cách sử dụng

**Từ vựng trong mục:** **Function** — hàm; **Option** — tùy chọn.

| Cú pháp | Mục đích và lựa chọn |
|---|---|
| `dict.get(id)` | Đọc bản ghi và trả mặc định nếu thiếu |
| `dict[id] = record` | Thêm/sửa bản ghi khi đã kiểm tra khóa |
| `dict.pop(id,default)` | Xóa có xử lý mã chưa tồn tại |
| `sum()/max()/min()/sorted()` | Tính thống kê và sắp xếp hồ sơ |

## 4. Khái niệm chính và liên quan

**Mạch kiến thức:** Một CLI nhận yêu cầu người dùng để tạo, đọc, sửa, xóa hồ sơ. Các thao tác CRUD cần Validation trước khi ghi, Lookup để tìm đúng mã và Aggregate để tạo báo cáo. Ví dụ xuyên suốt dùng mã sinh viên làm khóa và điểm trên thang 10 làm trường số.

### 4.1. CRUD — Bốn thao tác trên hồ sơ

**Từ vựng trong mục:** **CRUD — Create/Read/Update/Delete**.

Ứng dụng quản lý sinh viên cần tạo, đọc, sửa và xóa hồ sơ. Với Dictionary, **khóa là mã sinh viên duy nhất**, giá trị là Dictionary trường `name`, `score`. `Create` cần kiểm trùng mã; `Read` tra cứu; `Update` chỉ sửa mã tồn tại; `Delete` xử lý trường hợp mã không tìm thấy. Một CLI dùng lệnh nhập văn bản để thực hiện các thao tác này; đây mới là dữ liệu trong RAM, chưa được lưu bền xuống tệp.

```python
db = {}
db['S1'] = {'name': 'An', 'score': 8}
print(db['S1']['score'])
```

**Kết quả khi chạy:**

```text
8
```

Bản ghi S1 được tạo trong RAM; lấy `score` của S1 cho kết quả 8/10.

### 4.2. Validation — Chặn dữ liệu sai trước khi ghi

**Từ vựng trong mục:** **Validation — kiểm tra hợp lệ**.

Validation phải dựa trên **quy tắc dữ liệu**, ví dụ điểm là số nằm trong `[0,10]`, mã không rỗng, mã sinh viên chưa tồn tại khi thêm mới. Nếu chỉ thử `0 <= score <= 10`, một chuỗi nhập từ CLI phải được đổi sang số có xử lý lỗi trước; không so chuỗi với số. Kiểm tra ràng buộc **trước** khi ghi để tránh ghi sai rồi mới phát hiện.

```python
score = 8
print(isinstance(score, (int, float)) and 0 <= score <= 10)
```

**Kết quả khi chạy:**

```text
True
```

Điểm 8 là kiểu số và nằm trong thang điểm 0 đến 10.

### 4.3. Lookup — Tìm bản ghi theo mã

**Từ vựng trong mục:** **Lookup — tra cứu theo khóa**.

Với Dictionary `db`, `db.get('S1')` trả hồ sơ S1 nếu tồn tại, còn `db.get('S3')` trả `None` theo mặc định. Lệnh `db['S3']` sẽ ném `KeyError` khi thiếu mã. Trong CLI, việc không có hồ sơ cần được phản hồi rõ, không đánh đồng với một hồ sơ thật có điểm 0. Nếu cần thông báo thay vì `None`, truyền đối số mặc định cho `get`.

```python
db = {'S1': {'score': 8}}
print(db.get('S3', 'Not found'))
```

**Kết quả khi chạy:**

```text
Not found
```

Mã S3 không có trong Dictionary nên in thông báo thay vì gây KeyError.

### 4.4. Aggregate — Tóm tắt nhiều bản ghi

**Từ vựng trong mục:** **Aggregate — tổng hợp**.

Tổng hợp biến nhiều hồ sơ thành một con số hay báo cáo: ví dụ mean của ba điểm `[7,8,9]` bằng 8 và điểm cao nhất bằng 9. Trước khi tính cần lấy giá trị số từ trường `score`, không phải mã ID. Với danh sách rỗng, phép `sum(scores)/len(scores)` sẽ chia cho 0; chương trình phải xử lý trường hợp không có hồ sơ.

```python
scores = [7, 8, 9]
print(sum(scores) / len(scores), max(scores))
```

**Kết quả khi chạy:**

```text
8.0 9
```

Điểm trung bình bằng 8/10, điểm cao nhất bằng 9/10 trên ba hồ sơ.

## 5. Năm tình huống ứng dụng

### Tình huống 1 — Thêm sinh viên không ghi đè mã cũ

**Từ vựng trong mục:** **Record** — bản ghi; **ID** — mã định danh.

**Tình huống thực tế:** Trung tâm muốn tạo hồ sơ cho sinh viên S1 tên An, điểm 8/10. Kho hiện rỗng. Chỉ thêm nếu mã chưa tồn tại và điểm thuộc 0–10.

**Vì sao chọn cách giải này?** Kiểm tra cả tính duy nhất của khóa và phạm vi điểm trước khi tạo bản ghi.

**Quy trình giải:**

1. Tạo Dictionary rỗng, mã S1, điểm 8.
2. Kiểm mã chưa có và điểm hợp lệ.
3. Thêm hồ sơ rồi in dữ liệu đã lưu.

```python
db = {}
student_id = 'S1'
score = 8
if student_id not in db and 0 <= score <= 10:
    db[student_id] = {'name': 'An', 'score': score}
print(db)
```

**Kết quả khi chạy:**

```text
{'S1': {'name': 'An', 'score': 8}}
```

Đã thêm một hồ sơ S1, giữ điểm theo thang 10.

### Tình huống 2 — Thông báo khi mã không tồn tại

**Từ vựng trong mục:** **Record** — bản ghi; **ID** — mã định danh.

**Tình huống thực tế:** Danh sách chỉ có S1 điểm 8 và S2 điểm 9; nhân viên tìm mã S3. Chương trình cần báo không tìm thấy thay vì dừng vì lỗi KeyError.

**Vì sao chọn cách giải này?** `dict.get` cho phép định nghĩa giá trị mặc định khi thiếu mã.

**Quy trình giải:**

1. Tạo kho hai sinh viên.
2. Tra khóa S3 bằng `get` kèm thông báo mặc định.
3. In kết quả tra cứu.

```python
db = {'S1': {'score': 8}, 'S2': {'score': 9}}
print(db.get('S3', 'Not found'))
```

**Kết quả khi chạy:**

```text
Not found
```

Hồ sơ S3 không tồn tại; không có bản ghi nào bị thay đổi.

### Tình huống 3 — Sửa điểm sau khi kiểm thang

**Từ vựng trong mục:** **Record** — bản ghi; **ID** — mã định danh.

**Tình huống thực tế:** Hồ sơ S1 có điểm 7/10, người quản lý duyệt sửa lên 9/10. Chỉ cập nhật nếu mã tồn tại và điểm mới hợp lệ.

**Vì sao chọn cách giải này?** Kiểm tra trước khi Update tránh vô tình tạo hồ sơ mới hoặc lưu điểm ngoài phạm vi.

**Quy trình giải:**

1. Tạo bản ghi ban đầu S1 điểm 7.
2. Kiểm S1 đang tồn tại và 9 nằm trong thang.
3. Cập nhật điểm, in bản ghi sau sửa.

```python
db = {'S1': {'score': 7}}
new_score = 9
if 'S1' in db and 0 <= new_score <= 10:
    db['S1']['score'] = new_score
print(db)
```

**Kết quả khi chạy:**

```text
{'S1': {'score': 9}}
```

Điểm đã đổi 7→9/10; đây là Update, không tạo sinh viên thứ hai.

### Tình huống 4 — Xóa mã sinh viên thiếu an toàn

**Từ vựng trong mục:** **Record** — bản ghi; **ID** — mã định danh.

**Tình huống thực tế:** Kho chỉ có S1, nhân viên yêu cầu xóa S2 vốn không tồn tại. Chương trình phải báo không có bản ghi, không ném lỗi hoặc xóa S1.

**Vì sao chọn cách giải này?** `pop(key,default)` xử lý được nhánh không tìm thấy và không xóa khóa khác.

**Quy trình giải:**

1. Khởi tạo kho chỉ có S1.
2. Gọi `pop('S2',None)`.
3. In kết quả và kiểm kho không thay đổi.

```python
db = {'S1': {'score': 8}}
print(db.pop('S2', None))
print(db)
```

**Kết quả khi chạy:**

```text
None
{'S1': {'score': 8}}
```

Không có S2 để xóa nên trả None; S1 được giữ nguyên.

### Tình huống 5 — Tổng hợp kết quả của một lớp

**Từ vựng trong mục:** **Record** — bản ghi; **ID** — mã định danh.

**Tình huống thực tế:** Lớp có ba điểm 7,8,9 theo thang 10; giáo viên muốn in mean và điểm tối đa để báo cáo nội bộ.

**Vì sao chọn cách giải này?** Tính các chỉ số trực tiếp từ điểm số, thay vì lấy trung bình mã sinh viên hoặc chuỗi tên.

**Quy trình giải:**

1. Tạo List gồm ba điểm.
2. Tính mean bằng tổng chia cỡ nhóm và max.
3. In Dictionary báo cáo có hai chỉ số.

```python
scores = [7, 8, 9]
report = {'mean': sum(scores) / len(scores), 'max': max(scores)}
print(report)
```

**Kết quả khi chạy:**

```text
{'mean': 8.0, 'max': 9}
```

Trung bình lớp 8 điểm; cao nhất là 9 điểm.

## 6. Sai lầm thường gặp

- Thêm mã đã có bằng `dict[id]=...` sẽ ghi đè dữ liệu cũ nếu không kiểm trùng.
- Điểm từ CLI có thể là chuỗi; phải parse với xử lý ValueError trước khi so với số.
- `get()` khác `dict[key]` khi thiếu khóa; `pop` có default khác xóa trực tiếp.
- Update cần kiểm mã tồn tại và giới hạn điểm; xóa mã thiếu không được làm mất dữ liệu khác.
- Tính mean cần kiểm List không rỗng và chỉ tính trên trường số thực sự.
- Dictionary tồn tại trong RAM; chương trình thực tế cần lưu file/database và cân nhắc sao lưu/quyền truy cập.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Q1. What are the four CRUD operations? — Bốn thao tác CRUD là gì?**

A. Create, Read, Update, Delete — Tạo, đọc, sửa, xóa

B. Checking constraints before processing or storing — Kiểm ràng buộc trước khi xử lý hoặc lưu

C. A field identifying the desired record — Trường xác định bản ghi cần tìm

D. Computing summaries from multiple records — Tính chỉ số tổng hợp từ nhiều bản ghi

**Q2. What is input validation? — Kiểm tra dữ liệu đầu vào là gì?**

A. Create, Read, Update, Delete — Tạo, đọc, sửa, xóa

B. Checking constraints before processing or storing — Kiểm ràng buộc trước khi xử lý hoặc lưu

C. A field identifying the desired record — Trường xác định bản ghi cần tìm

D. Computing summaries from multiple records — Tính chỉ số tổng hợp từ nhiều bản ghi

**Q3. What is a lookup key? — Khóa tra cứu là gì?**

A. Create, Read, Update, Delete — Tạo, đọc, sửa, xóa

B. Checking constraints before processing or storing — Kiểm ràng buộc trước khi xử lý hoặc lưu

C. A field identifying the desired record — Trường xác định bản ghi cần tìm

D. Computing summaries from multiple records — Tính chỉ số tổng hợp từ nhiều bản ghi

**Q4. What is aggregation? — Aggregate là gì?**

A. Create, Read, Update, Delete — Tạo, đọc, sửa, xóa

B. Checking constraints before processing or storing — Kiểm ràng buộc trước khi xử lý hoặc lưu

C. A field identifying the desired record — Trường xác định bản ghi cần tìm

D. Computing summaries from multiple records — Tính chỉ số tổng hợp từ nhiều bản ghi

**Q5. What does `db.get('S1')` do? — `db.get('S1')` làm gì?**

A. Returns S1 value or None if missing — Trả giá trị S1 hoặc None nếu thiếu

B. Inserts or overwrites the key's value — Thêm hoặc ghi đè giá trị của khóa

C. Removes S2 or returns None if absent — Xóa S2 hoặc trả None nếu thiếu

D. Number of scores in the list — Số điểm trong danh sách

**Q6. What does `db['S1']=record` do? — `db['S1']=record` làm gì?**

A. Returns S1 value or None if missing — Trả giá trị S1 hoặc None nếu thiếu

B. Inserts or overwrites the key's value — Thêm hoặc ghi đè giá trị của khóa

C. Removes S2 or returns None if absent — Xóa S2 hoặc trả None nếu thiếu

D. Number of scores in the list — Số điểm trong danh sách

**Q7. What does `db.pop('S2',None)` do? — `db.pop('S2',None)` làm gì?**

A. Returns S1 value or None if missing — Trả giá trị S1 hoặc None nếu thiếu

B. Inserts or overwrites the key's value — Thêm hoặc ghi đè giá trị của khóa

C. Removes S2 or returns None if absent — Xóa S2 hoặc trả None nếu thiếu

D. Number of scores in the list — Số điểm trong danh sách

**Q8. What does `len(scores)` provide? — `len(scores)` cung cấp gì?**

A. Returns S1 value or None if missing — Trả giá trị S1 hoặc None nếu thiếu

B. Inserts or overwrites the key's value — Thêm hoặc ghi đè giá trị của khóa

C. Removes S2 or returns None if absent — Xóa S2 hoặc trả None nếu thiếu

D. Number of scores in the list — Số điểm trong danh sách

**Q9. What is a safe score validation for integer score 8? — Kiểm tra điểm 8 hợp lệ trên thang 0–10 thế nào?**

A. `0 <= score <= 10` — `0 <= score <= 10`

B. Confirm the key does not exist — Xác nhận khóa chưa tồn tại

C. Confirm the key exists and new values are valid — Xác nhận khóa có và giá trị mới hợp lệ

D. KeyError — Lỗi KeyError

**Q10. What is required before adding a unique student ID? — Trước khi thêm mã sinh viên duy nhất cần gì?**

A. `0 <= score <= 10` — `0 <= score <= 10`

B. Confirm the key does not exist — Xác nhận khóa chưa tồn tại

C. Confirm the key exists and new values are valid — Xác nhận khóa có và giá trị mới hợp lệ

D. KeyError — Lỗi KeyError

**Q11. What is required before updating a student record? — Trước khi sửa hồ sơ cần gì?**

A. `0 <= score <= 10` — `0 <= score <= 10`

B. Confirm the key does not exist — Xác nhận khóa chưa tồn tại

C. Confirm the key exists and new values are valid — Xác nhận khóa có và giá trị mới hợp lệ

D. KeyError — Lỗi KeyError

**Q12. What happens with `db['missing']` for an absent key? — Truy cập `db['missing']` khi thiếu khóa sẽ sao?**

A. `0 <= score <= 10` — `0 <= score <= 10`

B. Confirm the key does not exist — Xác nhận khóa chưa tồn tại

C. Confirm the key exists and new values are valid — Xác nhận khóa có và giá trị mới hợp lệ

D. KeyError — Lỗi KeyError

**Q13. What does `sum([7,8,9])/3` equal? — `sum([7,8,9])/3` bằng gì?**

A. 8.0 — 8.0

B. 9 — 9

C. Check length before dividing — Kiểm số phần tử trước khi chia

D. No, not across process restarts by itself — Không, tự nó không giữ qua lúc khởi động lại

**Q14. What does `max([7,8,9])` return? — `max([7,8,9])` trả gì?**

A. 8.0 — 8.0

B. 9 — 9

C. Check length before dividing — Kiểm số phần tử trước khi chia

D. No, not across process restarts by itself — Không, tự nó không giữ qua lúc khởi động lại

**Q15. How should an empty score list be handled before mean? — Trước khi tính mean với List điểm rỗng cần gì?**

A. 8.0 — 8.0

B. 9 — 9

C. Check length before dividing — Kiểm số phần tử trước khi chia

D. No, not across process restarts by itself — Không, tự nó không giữ qua lúc khởi động lại

**Q16. What does a Python Dictionary persist automatically? — Dictionary Python tự lưu bền dữ liệu không?**

A. 8.0 — 8.0

B. 9 — 9

C. Check length before dividing — Kiểm số phần tử trước khi chia

D. No, not across process restarts by itself — Không, tự nó không giữ qua lúc khởi động lại

**Q17. What is a duplicate ID risk in CRUD? — Nguy cơ mã trùng trong CRUD là gì?**

A. Existing data may be overwritten — Dữ liệu cũ có thể bị ghi đè

B. Reject or safely parse with error handling — Từ chối hoặc đổi kiểu có xử lý lỗi

C. When missing keys are expected and handled — Khi dự kiến thiếu khóa và cần xử lý

D. Numeric score values — Các giá trị điểm dạng số

**Q18. What should CLI do with a non-numeric score input? — CLI nên làm gì với điểm nhập chữ thay vì số?**

A. Existing data may be overwritten — Dữ liệu cũ có thể bị ghi đè

B. Reject or safely parse with error handling — Từ chối hoặc đổi kiểu có xử lý lỗi

C. When missing keys are expected and handled — Khi dự kiến thiếu khóa và cần xử lý

D. Numeric score values — Các giá trị điểm dạng số

**Q19. When is `dict.get` preferable to square indexing? — Khi nào dùng `dict.get` thay `dict[key]`?**

A. Existing data may be overwritten — Dữ liệu cũ có thể bị ghi đè

B. Reject or safely parse with error handling — Từ chối hoặc đổi kiểu có xử lý lỗi

C. When missing keys are expected and handled — Khi dự kiến thiếu khóa và cần xử lý

D. Numeric score values — Các giá trị điểm dạng số

**Q20. Which fields should an average score computation use? — Tính điểm trung bình nên dùng trường nào?**

A. Existing data may be overwritten — Dữ liệu cũ có thể bị ghi đè

B. Reject or safely parse with error handling — Từ chối hoặc đổi kiểu có xử lý lỗi

C. When missing keys are expected and handled — Khi dự kiến thiếu khóa và cần xử lý

D. Numeric score values — Các giá trị điểm dạng số

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **A** | CRUD covers the record lifecycle; it is not a single database command. | CRUD mô tả vòng đời bản ghi, không phải một lệnh cơ sở dữ liệu. |
| Q2 | **B** | Validation prevents invalid scores or duplicate identifiers entering storage. | Validation chặn điểm sai hoặc mã trùng trước khi ghi. |
| Q3 | **C** | Student ID can be a unique key while scores are record values. | Mã sinh viên dùng làm khóa duy nhất, còn điểm là giá trị bản ghi. |
| Q4 | **D** | Average and maximum summarize numeric fields across students. | Trung bình và cực đại tổng hợp trường số qua nhiều học viên. |
| Q5 | **A** | get reads safely without KeyError for a missing key. | get cho phép tra thiếu khóa mà không ném KeyError. |
| Q6 | **B** | Without an existence check, assignment can replace an old record. | Không kiểm khóa tồn tại, phép gán có thể ghi đè hồ sơ. |
| Q7 | **C** | The default suppresses KeyError for a missing key. | Giá trị mặc định tránh lỗi KeyError khi khóa vắng mặt. |
| Q8 | **D** | A mean divides the sum by this count when it is positive. | Mean chia tổng cho số phần tử khi số lượng lớn hơn 0. |
| Q9 | **A** | Both lower and upper bounds must hold. | Cần kiểm cả cận dưới và cận trên. |
| Q10 | **B** | This prevents silently overwriting another student's record. | Nhờ đó tránh ghi đè âm thầm hồ sơ khác. |
| Q11 | **C** | Update should not accidentally create missing records. | Sửa không nên vô tình tạo khóa mới. |
| Q12 | **D** | Direct indexed lookup raises unless the key exists. | Truy cập trực tiếp gây lỗi khi khóa không tồn tại. |
| Q13 | **A** | The total is 24 and there are three scores. | Tổng bằng 24 chia ba bằng 8. |
| Q14 | **B** | max chooses the largest numerical score. | max chọn điểm lớn nhất. |
| Q15 | **C** | Without this guard, dividing by len=0 raises an exception. | Nếu không kiểm, chia cho len=0 sẽ gây lỗi. |
| Q16 | **D** | In-memory records need explicit file or database persistence. | Hồ sơ trong RAM cần lưu ra file hoặc database để tồn tại lâu dài. |
| Q17 | **A** | Unique-key checks prevent accidental replacement. | Kiểm tra khóa duy nhất tránh thay nhầm. |
| Q18 | **B** | A terminal input string cannot be compared with numbers without parsing. | Chuỗi nhập từ terminal cần đổi số trước khi so ngưỡng. |
| Q19 | **C** | get supports an explicit default instead of raising KeyError. | get trả mặc định thay cho ném KeyError. |
| Q20 | **D** | IDs and names identify records but should not enter the numeric average. | ID và tên để nhận diện, không đưa vào phép trung bình. |

## 8. Nối sang bài tiếp

`Dictionary/Function → CRUD → CLI → File/CSV → Data App`.

# PY-07 — Tuple, Set và các phép toán tập hợp


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Tuple** — bộ giá trị; **Set** — tập hợp.

`List → Tuple và Set → Tập hợp/Jaccard`

**Học xong dùng để làm gì?** Giữ cặp tọa độ cố định và lấy các nhãn không trùng nhau, so sánh phần tử chung/riêng của hai nhóm.

**Kết nối kiến thức tiếp theo:** PY-08 dùng Dictionary để liên kết mã hoặc tên với thông tin chi tiết.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Giải thích dễ nhớ |
|---|---|---|
| Tuple | bộ giá trị | Dãy có thứ tự không sửa phần tử được |
| Set | tập hợp | Nhóm phần tử không trùng lặp |
| Union | phép hợp | Mọi phần tử có trong ít nhất một tập |
| Intersection | phép giao | Phần tử chung của hai tập |

## 3. Hàm và cú pháp Python

**Từ vựng trong mục:** **Function** — hàm; **Argument** — đối số.

| Hàm / cú pháp | Mục đích và lựa chọn liên quan |
|---|---|
| `tuple(items)` | Lưu một bộ dữ liệu có thứ tự và cố định |
| `set(items)` | Khử giá trị trùng, không giữ thứ tự đáng tin |
| `a.union(b)`, `a.intersection(b)` | Lấy toàn bộ phần tử của hai tập (hợp), hoặc chỉ phần tử chung (giao); tương đương `a \| b` và `a & b` |
| `a - b, a ^ b` | Tìm phần tử còn thiếu hoặc khác nhau |

## 4. Khái niệm liên quan

Sau List, có hai nhu cầu khác nhau: **giữ một bộ dữ liệu có thứ tự nhưng không sửa trực tiếp** (Tuple), hoặc **chỉ lưu các giá trị không trùng và so sánh hai nhóm** (Set). Hai cấu trúc không thay thế lẫn nhau: tọa độ `(3, 4)` phù hợp với Tuple, còn danh sách kỹ năng không trùng phù hợp với Set. Từ Set, bài học mở rộng sang phép hợp và phép giao.

### 4.1. Tuple — Bộ giá trị cố định

**Từ vựng trong mục:** **Tuple** — bộ giá trị; **Coordinate** — tọa độ.

Tuple chứa các phần tử **có thứ tự**, thường dùng cho một cặp thông tin gắn với nhau như tọa độ `(x, y)`. Với điểm ở vị trí `x = 3`, `y = 4` mét, ta viết `point = (3, 4)`; `point[0]` là x và `point[1]` là y. Không thể gán `point[0] = 5` như List; nếu cần vị trí mới, tạo Tuple mới.

```python
# Mục đích: Bộ giá trị cố định.
point = (3, 4)
print(point)
```

**Kết quả khi chạy:**

```text
(3, 4)
```

Dấu ngoặc tròn biểu thị Tuple gồm hai tọa độ, khác dấu ngoặc vuông của List.

### 4.2. Set — Tập hợp không trùng

**Từ vựng trong mục:** **Set** — tập hợp; **Duplicate** — giá trị lặp.

Set giúp lưu **những giá trị khác nhau** mà không cần ghi cùng một giá trị nhiều lần. Một nhóm học ghi ba nhãn `Python`, `AI`, `Python`; khi chuyển sang Set, nhãn `Python` bị trùng chỉ còn một lần. Set không có chỉ số vị trí như `set[0]` và không đảm bảo thứ tự in. `set()` tạo tập rỗng, còn `{}` tạo Dictionary rỗng.

```python
# Mục đích: Tập hợp không trùng.
skills = set(['Python', 'AI', 'Python'])
print(len(skills))
```

**Kết quả khi chạy:**

```text
2
```

Có hai kỹ năng khác nhau: Python và AI. Ta in **số lượng** để không phụ thuộc thứ tự hiển thị của Set.

### 4.3. Union — Gộp hai nhóm

**Từ vựng trong mục:** **Union** — phép hợp; **Set** — tập hợp.

Giả sử nhóm A học `{Python, AI}`, nhóm B học `{AI, SQL}`. Cửa hàng khóa học muốn biết **tất cả kỹ năng có trong ít nhất một nhóm**. Phép hợp `a | b` giữ Python, AI và SQL nhưng chỉ giữ AI một lần. Với Set, ký hiệu `|` là phép hợp tập hợp, không phải toán tử `or` nối điều kiện Boolean.

```python
# Mục đích: Gộp hai nhóm.
a = {'Python', 'AI'}
b = {'AI', 'SQL'}
print(len(a | b))
```

**Kết quả khi chạy:**

```text
3
```

Phép hợp gồm ba kỹ năng khác nhau; ký hiệu `|` gộp hai Set và tự loại phần trùng.

### 4.4. Intersection — Tìm phần chung

**Từ vựng trong mục:** **Intersection** — phép giao; **Set** — tập hợp.

Vẫn với hai nhóm A có `{Python, AI}` và B có `{AI, SQL}`, ta muốn tìm **kỹ năng cả hai nhóm đều học**. Phép giao `a & b` chỉ giữ AI, vì Python không có ở B và SQL không có ở A. Phép giao khác phép hợp: hợp trả ba kỹ năng, giao chỉ một kỹ năng.

```python
# Mục đích: Tìm phần chung.
a = {'Python', 'AI'}
b = {'AI', 'SQL'}
print(a & b)
```

**Kết quả khi chạy:**

```text
{'AI'}
```

Chỉ có AI xuất hiện trong cả hai nhóm; tập chỉ có một phần tử nên thứ tự hiển thị không gây nhầm lẫn.
### 4.5. Difference — Phần tử còn thiếu trong Set

**Từ vựng trong mục:** **Difference** — hiệu tập hợp; **Set** — tập hợp.

Ngoài phép hợp và phép giao, ta còn cần biết **phần tử chỉ có ở nhóm A nhưng chưa có ở nhóm B**. Ví dụ khóa học yêu cầu `Python`, `SQL`, `AI`, còn học viên đã hoàn thành `Python`; hiệu `required - done` giữ `SQL` và `AI`. Dùng `sorted()` nếu muốn in các kỹ năng theo một thứ tự rõ ràng. Hiệu `a - b` khác **hiệu đối xứng** `a ^ b`, vốn lấy các phần tử chỉ thuộc một trong hai nhóm.

```python
# Mục đích: Phần tử còn thiếu trong Set.
required = {'Python', 'SQL', 'AI'}
done = {'Python'}
print(sorted(required - done))
```

**Kết quả khi chạy:**

```text
['AI', 'SQL']
```

Kết quả là một **List đã sắp xếp**, gồm hai kỹ năng cần học tiếp. Set gốc không bị thay đổi.

## 5. Năm tình huống Tuple/Set — từ bản ghi đến đối chiếu kỹ năng

### Tình huống 1 — Cấp 1: Lưu 10 tọa độ bằng Tuple

**Từ vựng trong mục:** **Tuple** — bộ giá trị; **Unpacking** — tách bộ.

**Tình huống thực tế:** Robot ghi **10 vị trí** trên mặt phẳng (mét), mỗi vị trí là cặp tọa độ `(x, y)` không muốn sửa khi dùng để đối chiếu đường đi. Hãy lưu các cặp bằng tuple, tách tọa độ điểm đầu và đếm những điểm có bình phương khoảng cách tới gốc từ 25 m² trở lên.

**Vì sao chọn cách này?** Tuple giữ cấu trúc cố định của từng cặp số, cho phép tách `x, y = point`. Kiểm tra bình phương khoảng cách tránh cần thêm thư viện tính căn cho bài này.

**Quy trình:**
1. Lưu mười tuple tọa độ, mỗi hàng là một vị trí.
2. Tách `x, y` của từng tuple và đếm điểm đạt ngưỡng.
3. In điểm đầu, số quan sát và số điểm đủ xa.

```python
positions = [(3,4),(0,2),(5,0),(1,1),(2,3),(4,1),(6,0),(1,4),(2,2),(5,5)]
first_x, first_y = positions[0]
far_count = 0
for x, y in positions:
    if x*x + y*y >= 25:
        far_count += 1
if len(positions) != 10:
    raise ValueError("Cần đủ 10 vị trí robot.")
print("Số vị trí:", len(positions))
print("Điểm đầu:", first_x, first_y)
print("Điểm xa:", far_count)
```

**Kết quả khi chạy:**

```text
Số vị trí: 10
Điểm đầu: 3 4
Điểm xa: 4
```

Mỗi tuple là một điểm đo có hai thành phần. Số 25 mang đơn vị m² do chương trình so bình phương khoảng cách, không phải khoảng cách 25 mét.

### Tình huống 2 — Cấp 2: Khử email trùng sau chuẩn hóa 12 bản ghi

**Từ vựng trong mục:** **Set** — tập hợp; **Duplicate** — trùng; **Normalization** — chuẩn hóa.

**Tình huống thực tế:** Một chương trình chuẩn bị gửi thư cho **12 địa chỉ giả lập**, mỗi dòng là một tài khoản. Có email giống nhau nhưng khác chữ hoa/thường và khoảng trắng; cần thống kê số tài khoản duy nhất **sau chuẩn hóa**, không gửi trùng.

**Vì sao chọn cách này?** `set()` chỉ tự loại các chuỗi giống nhau hoàn toàn; cần `strip().lower()` trước để so sánh nhất quán. Tập hợp không bảo đảm thứ tự, nên `sorted()` tạo danh sách hiển thị ổn định.

**Quy trình:**
1. Chuẩn hóa mười hai email sang chữ thường, bỏ khoảng trắng biên.
2. Đưa dữ liệu vào Set để loại các bản ghi giống nhau.
3. Báo số email gốc, số email duy nhất và số lượt thừa.

```python
raw = ["Lan@EXAMPLE.invalid","an@example.invalid"," LAN@example.invalid ","binh@example.invalid","chi@example.invalid","An@Example.INVALID","dung@example.invalid","ha@example.invalid","Minh@example.invalid","lan@example.invalid","trang@example.invalid","ha@example.invalid"]
normalized = []
for email in raw:
    normalized.append(email.strip().lower())
unique = set(normalized)
if len(raw) != 12:
    raise ValueError("Cần đủ 12 dòng email đầu vào.")
print("Dòng nhận:", len(raw))
print("Email duy nhất:", len(unique))
print("Bản ghi trùng:", len(raw) - len(unique))
```

**Kết quả khi chạy:**

```text
Dòng nhận: 12
Email duy nhất: 8
Bản ghi trùng: 4
```

Tên miền `.invalid` chỉ dành cho dữ liệu minh họa. Không dùng số email thô làm số tài khoản duy nhất khi dữ liệu chưa được chuẩn hóa.

### Tình huống 3 — Cấp 3: Tìm học viên học cả hai môn từ 15 lượt đăng ký

**Từ vựng trong mục:** **Intersection** — phép giao; **Union** — phép hợp; **Membership** — thành viên.

**Tình huống thực tế:** Trung tâm nhận **15 lượt đăng ký môn**; mỗi hàng gồm mã học viên và tên môn `Python` hoặc `AI`. Một người có thể xuất hiện trong hai hàng vì đăng ký cả hai môn. Cần biết những ai học **cả hai**, có bao nhiêu học viên riêng biệt và vì sao số lượt không bằng số người.

**Vì sao chọn cách này?** Đưa mã của từng môn vào hai Set. Phép giao `&` tìm người nằm trong cả hai; phép hợp `|` đếm người có ít nhất một môn. Đây là hai yêu cầu khác nhau nên không thể dùng một phép đếm list.

**Quy trình:**
1. Lưu 15 cặp `(mã học viên, môn)` có nghĩa rõ.
2. Tạo Set mã cho từng môn, lấy giao và hợp.
3. Sắp mã trong giao để in ổn định và đếm số người riêng biệt.

```python
registrations = [("SV01","Python"),("SV02","Python"),("SV03","AI"),("SV01","AI"),("SV04","Python"),("SV05","AI"),("SV06","Python"),("SV07","AI"),("SV02","AI"),("SV08","Python"),("SV09","Python"),("SV10","AI"),("SV03","Python"),("SV11","Python"),("SV12","AI")]
python_students = set()
ai_students = set()
for student, subject in registrations:
    if subject == "Python":
        python_students.add(student)
    if subject == "AI":
        ai_students.add(student)
both = sorted(python_students & ai_students)
all_students = python_students | ai_students
if len(registrations) != 15:
    raise ValueError("Cần đúng 15 lượt đăng ký hai môn.")
print("Lượt đăng ký:", len(registrations))
print("Học cả hai:", ", ".join(both))
print("Học viên khác nhau:", len(all_students))
```

**Kết quả khi chạy:**

```text
Lượt đăng ký: 15
Học cả hai: SV01, SV02, SV03
Học viên khác nhau: 12
```

Cùng một mã xuất hiện hai lần là hai lượt đăng ký hợp lệ, không phải nhập trùng nếu môn khác nhau. Phép hợp khử trùng mã để đếm số người.

### Tình huống 4 — Cấp 4: Lọc mã thành viên lỗi và so sánh 18 lượt vào nhóm

**Từ vựng trong mục:** **Difference** — hiệu tập hợp; **Intersection** — phép giao; **Invalid ID** — mã lỗi.

**Tình huống thực tế:** Có **18 lượt ghi danh** vào nhóm A hoặc B, mỗi hàng là `(mã thành viên, nhóm)`; cùng một người được phép vào cả hai nhóm. Lượt thứ 15 bị thiếu ID (`None`), nên không biết thuộc về ai. Cần tách lượt lỗi và tìm người **chỉ ở A** và người ở **cả A lẫn B**.

**Vì sao chọn cách này?** Set chỉ dùng trên các mã hợp lệ; nếu đưa `None` vào tập, đó sẽ bị coi là một thành viên giả. Phép hiệu `A - B` và giao `A & B` trả hai câu trả lời khác nhau.

**Quy trình:**
1. Kiểm tra từng cặp, bỏ lượt có ID None và đếm lỗi.
2. Lập tập thành viên A và B từ 17 lượt hợp lệ.
3. Lấy hiệu/giao rồi in danh sách mã đã sắp xếp.

```python
registrations = [("U01","A"),("U02","A"),("U03","B"),("U04","A"),("U05","B"),("U06","A"),("U07","B"),("U08","A"),("U09","A"),("U10","B"),("U02","B"),("U04","B"),("U11","A"),("U12","B"),(None,"B"),("U13","A"),("U14","B"),("U10","A")]
valid = []
a = set()
b = set()
for code, group in registrations:
    if code is None:
        continue
    valid.append((code, group))
    if group == "A":
        a.add(code)
    if group == "B":
        b.add(code)
if len(registrations) != 18:
    raise ValueError("Cần đúng 18 lượt tham gia nhóm.")
print("Lượt ghi:", len(registrations))
print("Thiếu ID:", len(registrations) - len(valid))
print("Chỉ nhóm A:", ", ".join(sorted(a - b)))
print("Cả hai:", ", ".join(sorted(a & b)))
```

**Kết quả khi chạy:**

```text
Lượt ghi: 18
Thiếu ID: 1
Chỉ nhóm A: U01, U06, U08, U09, U11, U13
Cả hai: U02, U04, U10
```

Không gộp hai lượt của cùng người thành một lỗi: cùng ID ở A/B có nghĩa là người đó tham gia cả hai nhóm.

### Tình huống 5 — Cấp 5: Kiểm kê kỹ năng còn thiếu của 8 học viên qua 20 lượt học

**Từ vựng trong mục:** **Set difference** — hiệu tập hợp; **Data validation** — kiểm dữ liệu; **Tuple** — cặp giá trị.

**Tình huống thực tế:** Khóa học yêu cầu mỗi người hoàn tất **ba kỹ năng Python, SQL và AI**. Hệ thống nhận **20 lượt ghi kết quả**, mỗi hàng là cặp `(mã học viên, kỹ năng đã học)` của 8 người S01…S08. Có một lượt `S06–Python` ghi trùng và một lượt `S06–None` chưa xác định kỹ năng. Cần xác định học viên đủ cả ba, các kỹ năng còn thiếu của S06, số lượt lỗi và số lượt trùng sau chuẩn hóa.

**Vì sao chọn cách này?** Tuple `(người, kỹ năng)` lưu chính xác ý nghĩa của một lượt; dùng set các cặp để khử trùng **cùng người–cùng kỹ năng**, không gộp tất cả kỹ năng theo người mà làm mất thông tin. Hiệu `required - done` tìm từng kỹ năng thiếu.

**Quy trình:**
1. Đọc đủ 20 lượt và tách những lượt chưa biết tên kỹ năng.
2. Dùng Set các tuple `(student, skill)` để loại lượt giống hệt nhau.
3. Với mỗi người, so `required` với tập đã học, tổng hợp người đủ khóa và báo chi tiết S06.

```python
records = [("S01","Python"),("S01","SQL"),("S01","AI"),("S02","Python"),("S02","SQL"),("S03","AI"),("S03","SQL"),("S04","Python"),("S04","AI"),("S05","Python"),("S05","SQL"),("S05","AI"),("S06","Python"),("S06","Python"),("S06",None),("S07","SQL"),("S07","AI"),("S08","Python"),("S08","SQL"),("S08","AI")]
required = {"Python", "SQL", "AI"}
valid = []
all_student_codes = set()
for student, skill in records:
    all_student_codes.add(student)
    if skill is not None:
        valid.append((student, skill))
unique_pairs = set(valid)
all_students = sorted(all_student_codes)
completed = []
missing_s06 = set()
for student in all_students:
    learned = set()
    for user, skill in unique_pairs:
        if user == student:
            learned.add(skill)
    remaining = required - learned
    if not remaining:
        completed.append(student)
    if student == "S06":
        missing_s06 = remaining
if len(records) != 20:
    raise ValueError("Cần kiểm tra đủ 20 lượt kỹ năng.")
print("Lượt ghi:", len(records))
print("Thiếu kỹ năng:", len(records) - len(valid))
print("Lượt trùng:", len(valid) - len(unique_pairs))
print("Hoàn tất:", ", ".join(completed))
print("S06 cần học:", ", ".join(sorted(missing_s06)))
```

**Kết quả khi chạy:**

```text
Lượt ghi: 20
Thiếu kỹ năng: 1
Lượt trùng: 1
Hoàn tất: S01, S05, S08
S06 cần học: AI, SQL
```

Khóa hoàn tất đòi **đủ cả ba kỹ năng**; việc có ba lượt ghi chưa chắc đã là ba kỹ năng khác nhau. Báo riêng lượt thiếu trước khi xét tiến độ học viên.

## 6. Nhầm lẫn dễ gặp

- Tuple không cho gán lại từng phần tử như `point[0] = 5`; nếu cần sửa tọa độ, tạo tuple mới.
- Set không có thứ tự cố định, không dùng `my_set[0]` và không dựa vào thứ tự khi in.
- Set chỉ giữ phần tử có thể băm được (hashable); không thể đặt list trực tiếp làm phần tử của set.
- Phép hợp `|` lấy tất cả phần tử; phép giao `&` chỉ lấy phần tử chung; phép trừ `-` tìm phần tử còn thiếu.

## 7. Trắc nghiệm

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is a tuple? | Tuple là gì?**

A. An ordered mutable sequence | Dãy có thứ tự và có thể sửa

B. An unordered collection of unique items | Tập hợp không thứ tự của phần tử duy nhất

C. A key-to-value mapping | Ánh xạ khóa–giá trị

D. An ordered immutable collection | Tập hợp có thứ tự và bất biến

**Đáp án: D**

**Giải thích:** Tuple là dãy có thứ tự và bất biến: `(2, 3)` giữ tọa độ đầu trước tọa độ sau, nhưng không cho phép gán lại từng phần tử. List cũng có thứ tự nhưng có thể sửa các phần tử.


**Q2. What is a set? | Set là gì?**

A. An ordered collection of key-value entries | Tập hợp có thứ tự các cặp khóa–giá trị

B. A collection that always keeps duplicates | Tập hợp luôn giữ giá trị trùng

C. A collection of unique hashable members | Tập hợp gồm phần tử có thể băm và không trùng

D. A sequence accessed by positional indexes | Dãy truy cập bằng chỉ số vị trí

**Đáp án: C**

**Giải thích:** Set chứa các phần tử có thể băm và không trùng nhau, đồng thời không hỗ trợ truy cập theo chỉ số vị trí. Tạo `set([1, 1, 2])` chỉ còn hai phần tử `1` và `2`, khác List vốn giữ phần tử lặp.


**Q3. What does set union collect? | Phép hợp Set lấy gì?**

A. Only members of the first set not in the second | Chỉ phần tử tập đầu mà không thuộc tập sau

B. Distinct members appearing in either set | Phần tử khác nhau thuộc ít nhất một tập

C. Only members appearing in exactly one set | Chỉ phần tử thuộc đúng một tập

D. Only members common to both sets | Chỉ phần tử chung của hai tập

**Đáp án: B**

**Giải thích:** Phép hợp lấy mỗi phần tử khác nhau xuất hiện trong ít nhất một tập. Với `{1, 2}` và `{2, 3}`, hợp chứa `{1, 2, 3}`; phép giao chỉ giữ phần tử chung `2`.


**Q4. What does set intersection collect? | Phép giao Set lấy gì?**

A. Only members of the first set | Chỉ phần tử tập đầu

B. Members occurring in exactly one set | Phần tử xuất hiện đúng một tập

C. Only members shared by both sets | Chỉ phần tử chung của cả hai tập

D. All distinct members of either set | Mọi phần tử khác nhau thuộc ít nhất một tập

**Đáp án: C**

**Giải thích:** Phép giao chỉ giữ phần tử có mặt ở cả hai tập. Với `{1, 2}` và `{2, 3}`, giao là `{2}`; tập này nhỏ hơn phép hợp `{1, 2, 3}`.


**Q5. Which expression constructs a two-element tuple? | Biểu thức nào tạo Tuple có hai phần tử?**

A. `(2, 3)` | `(2, 3)`

B. `[2, 3]` | `[2, 3]`

C. `{2, 3}` | `{2, 3}`

D. `{2: 3}` | `{2: 3}`

**Đáp án: A**

**Giải thích:** `(2, 3)` là Tuple gồm hai phần tử có thứ tự với các giá trị phân cách bằng dấu phẩy. Ngược lại, `{2, 3}` là Set và `[2, 3]` là List có thể sửa.


**Q6. Which expression constructs a nonempty set? | Biểu thức nào tạo Set không rỗng?**

A. `[2, 3]` | `[2, 3]`

B. `{2: 3}` | `{2: 3}`

C. `(2, 3)` | `(2, 3)`

D. `{2, 3}` | `{2, 3}`

**Đáp án: D**

**Giải thích:** `{2, 3}` tạo Set không rỗng gồm hai số nguyên khác nhau. Dấu ngoặc tròn tạo Tuple và ngoặc vuông tạo List, còn ngoặc nhọn rỗng `{}` tạo Dictionary.


**Q7. Which expression constructs an empty set? | Biểu thức nào tạo Set rỗng?**

A. `[]` | `[]`

B. `set()` | `set()`

C. `()` | `()`

D. `{}` | `{}`

**Đáp án: B**

**Giải thích:** `set()` tạo Set rỗng. Ký hiệu gần giống `{}` lại là Dictionary rỗng, vì vậy không thể dùng cặp ngoặc nhọn trống để tạo Set không có phần tử.


**Q8. Which expression constructs an empty dictionary? | Biểu thức nào tạo Dictionary rỗng?**

A. `set()` | `set()`

B. `[]` | `[]`

C. `()` | `()`

D. `{}` | `{}`

**Đáp án: D**

**Giải thích:** `{}` biểu diễn Dictionary rỗng, tức ánh xạ khóa–giá trị chưa có mục nào. Muốn tạo Set rỗng phải dùng `set()`; List và Tuple rỗng lần lượt là `[]` và `()`.


**Q9. What does `a | b` do for sets? | `a | b` làm gì với hai Set?**

A. Set difference from `a` to `b` | Hiệu Set từ `a` trừ `b`

B. Symmetric difference | Hiệu đối xứng

C. Set union | Phép hợp Set

D. Set intersection | Phép giao Set

**Đáp án: C**

**Giải thích:** Với Set, `a | b` thực hiện phép hợp, giữ phần tử khác nhau thuộc `a`, `b` hoặc cả hai. Nếu `a={1,2}` và `b={2,3}`, kết quả chứa 1, 2, 3, khác giao vốn chỉ giữ 2.


**Q10. What does `a & b` do for sets? | `a & b` làm gì với hai Set?**

A. Set intersection | Phép giao Set

B. Set difference | Phép hiệu Set

C. Symmetric difference | Hiệu đối xứng

D. Set union | Phép hợp Set

**Đáp án: A**

**Giải thích:** `a & b` là phép giao Set, chỉ giữ giá trị xuất hiện ở cả hai tập. Với `{1,2}` và `{2,3}`, kết quả là `{2}`; nó không lấy mọi phần tử khác nhau như phép hợp.


**Q11. What does `a - b` do for sets? | `a - b` làm gì với hai Set?**

A. Members in `a` but not in `b` | Phần tử thuộc `a` nhưng không thuộc `b`

B. Members in exactly one input | Phần tử thuộc đúng một tập

C. Set union | Phép hợp Set

D. Set intersection | Phép giao Set

**Đáp án: A**

**Giải thích:** `a - b` chỉ giữ phần tử thuộc `a` mà không thuộc `b`, nên thứ tự hai vế quan trọng: `{1,2} - {2,3}` cho `{1}`. Đảo hai vế lại được `{3}`, khác hiệu đối xứng giữ cả 1 và 3.


**Q12. What does `a ^ b` do for sets? | `a ^ b` làm gì với hai Set?**

A. Set union | Phép hợp Set

B. Set intersection | Phép giao Set

C. Members of `a` only | Chỉ phần tử của `a`

D. Members in exactly one of the sets | Phần tử thuộc đúng một trong hai tập

**Đáp án: D**

**Giải thích:** `a ^ b` tính hiệu đối xứng: lấy phần tử có mặt đúng ở một trong hai tập. Với `{1,2}` và `{2,3}`, kết quả chứa 1 và 3 nhưng loại phần tử chung 2.


**Q13. What is the length of `set([1,1,2])`? | `set([1,1,2])` có bao nhiêu phần tử?**

A. `2` | `2`

B. `3` | `3`

C. `1` | `1`

D. `ValueError` | `ValueError`

**Đáp án: A**

**Giải thích:** Tạo Set sẽ loại giá trị trùng, vì vậy `set([1,1,2])` chỉ còn phần tử 1 và 2. Độ dài do đó bằng số nguyên `2`, không phải ba vị trí của List gốc.


**Q14. What happens when assigning `t[0] = 9` on a tuple? | Gán `t[0] = 9` trên Tuple sẽ thế nào?**

A. A `TypeError` is raised | Phát sinh `TypeError`

B. A new tuple is created automatically | Tự động tạo Tuple mới

C. An `IndexError` is always raised | Luôn phát sinh `IndexError`

D. The tuple's first item changes to 9 | Phần tử đầu Tuple đổi thành 9

**Đáp án: A**

**Giải thích:** Tuple không cho phép gán lại từng phần tử nên `t[0] = 9` trên Tuple gây `TypeError`. Khác với List, việc gán vào một chỉ số hợp lệ được cho phép.


**Q15. How do you test membership in a set? | Làm sao kiểm tra một giá trị thuộc Set?**

A. `s[x]` | `s[x]`

B. `x in s` | `x in s`

C. `x == s` | `x == s`

D. `s.index(x)` | `s.index(x)`

**Đáp án: B**

**Giải thích:** Dùng `x in s` để kiểm tra phần tử, kết quả là Boolean. Với `s={1,3}`, `3 in s` là `True` và `2 in s` là `False`; Set không có phương thức `.index()` theo vị trí.


**Q16. Is order of printed set elements guaranteed? | Thứ tự phần tử in từ Set có được bảo đảm không?**

A. Always sorted in ascending order | Luôn theo thứ tự tăng dần

B. Always insertion order | Luôn theo thứ tự thêm vào

C. Always a new random permutation | Luôn tạo hoán vị ngẫu nhiên mới

D. No fixed display order is guaranteed | Không bảo đảm thứ tự hiển thị cố định

**Đáp án: D**

**Giải thích:** Set không bảo đảm thứ tự khi hiển thị hay duyệt các phần tử. Dù một lần chạy in `{1, 2, 3}`, không nên phụ thuộc thứ tự đó ở các lần sau; sắp xếp Set là thao tác riêng.


**Q17. Which built-in immutable ordered sequence best represents a fixed coordinate pair `(x, y)`? | Kiểu dãy có thứ tự và bất biến nào phù hợp nhất biểu diễn cặp tọa độ cố định `(x, y)`?**

A. Dictionary | Dictionary

B. Tuple | Tuple

C. List | List

D. Set | Set

**Đáp án: B**

**Giải thích:** Một cặp có thứ tự và bất biến như `(x, y)` phù hợp tọa độ cố định vì vị trí thứ nhất và thứ hai có ý nghĩa riêng. Set không truy cập theo vị trí, còn List cho phép gán lại phần tử.


**Q18. Which built-in collection directly keeps only distinct tags? | Kiểu tập hợp nào trực tiếp chỉ giữ những nhãn khác nhau?**

A. String, which holds one sequence of characters | String lưu dãy ký tự

B. Tuple, which retains duplicates | Tuple giữ nguyên các phần tử trùng

C. Set, which retains distinct tags | Set chỉ giữ nhãn khác nhau

D. List, which retains duplicates | List giữ nguyên các phần tử trùng

**Đáp án: C**

**Giải thích:** Set trực tiếp loại nhãn trùng vì mỗi giá trị chỉ xuất hiện một lần. Với nhãn `['red', 'red', 'blue']`, tạo Set giữ hai nhãn khác nhau `red` và `blue`, nhưng không bảo đảm thứ tự.


**Q19. Which method checks whether sets share no elements? | Phương thức nào kiểm tra hai Set không có phần tử chung?**

A. `union()` | `union()`

B. `isdisjoint()` | `isdisjoint()`

C. `intersection()` | `intersection()`

D. `issubset()` | `issubset()`

**Đáp án: B**

**Giải thích:** `a.isdisjoint(b)` trả `True` khi và chỉ khi hai Set không có phần tử chung. Với `{1,2}` và `{3}`, kết quả là `True`, còn `{1,2}` và `{2,4}` cho `False`.


**Q20. Which function creates a sorted list from a set of comparable numbers? | Hàm nào tạo List đã sắp từ một Set chứa các số có thể so sánh?**

A. `list(s)` without ordering | `list(s)` không sắp xếp

B. `reversed(s)` | `reversed(s)`

C. `sorted(s)` | `sorted(s)`

D. `s.sort()` | `s.sort()`

**Đáp án: C**

**Giải thích:** `sorted(s)` trả về List mới đã sắp xếp, ví dụ `sorted({3,1,2})` cho `[1,2,3]`. Nó không tạo thứ tự cố định cho Set gốc, vốn vẫn là tập không có thứ tự vị trí.

## 8. Nối sang bài tiếp theo

`List → Tuple và Set → Tập hợp/Jaccard`.

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

**No Note — Không chú thích**

```python
point = (3, 4)
print(point)
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tạo tuple tọa độ (x,y) của một điểm.
# Dữ liệu: Tuple gồm 2 tọa độ x=3, y=4, không đổi phần tử sau khi tạo.
# Dấu ngoặc tròn tạo tuple cố định gồm hai phần tử 3 và 4.
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

**No Note — Không chú thích**

```python
skills = set(['Python', 'AI', 'Python'])
print(len(skills))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Dùng set bỏ kỹ năng bị lặp và đếm số loại.
# Dữ liệu: Ba chuỗi kỹ năng có 'Python' lặp.
# set() loại giá trị 'Python' trùng; set không lưu nhiều bản sao cùng kỹ năng.
skills = set(['Python', 'AI', 'Python'])
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
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

**No Note — Không chú thích**

```python
a = {'Python', 'AI'}
b = {'AI', 'SQL'}
print(len(a | b))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Hợp hai tập kỹ năng và đếm kết quả không trùng.
# Dữ liệu: Hai tập không trùng, có một phần tử chung 'AI'.
a = {'Python', 'AI'}
b = {'AI', 'SQL'}
# | hợp hai set: các kỹ năng ở ít nhất một nhóm, không đếm trùng; len() đếm số phần tử.
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

**No Note — Không chú thích**

```python
a = {'Python', 'AI'}
b = {'AI', 'SQL'}
print(a & b)
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Lấy phần giao hai tập: kỹ năng xuất hiện ở cả hai.
# Dữ liệu: Hai tập kỹ năng, thứ tự khi in set không cố định.
a = {'Python', 'AI'}
b = {'AI', 'SQL'}
# & lấy giao: chỉ các kỹ năng thuộc đồng thời hai set; thứ tự in set không đảm bảo.
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

**No Note — Không chú thích**

```python
required = {'Python', 'SQL', 'AI'}
done = {'Python'}
print(sorted(required - done))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Lấy kỹ năng còn thiếu bằng phép trừ tập hợp.
# Dữ liệu: required là bộ kỹ năng phải biết, done là bộ đã học.
required = {'Python', 'SQL', 'AI'}
done = {'Python'}
# - lấy hiệu set: phần tử required chưa có trong done; sorted() tạo danh sách xếp chữ cái để hiển thị ổn định.
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

**Tình huống thực tế:** Một robot di chuyển trên sàn và ghi lại **10 vị trí** theo đơn vị **mét**. Mỗi vị trí gồm hai số `(x, y)`: `x` là khoảng dịch sang ngang, `y` là khoảng dịch theo chiều dọc so với điểm xuất phát `(0, 0)`. Nhóm vận hành muốn lưu nguyên từng cặp tọa độ, đọc cặp đầu tiên và đếm bao nhiêu điểm cách điểm xuất phát ít nhất 5 mét.

**Vì sao chọn cách này?** **Tuple** là cách giữ hai giá trị đi cùng nhau như một cặp tọa độ, ví dụ `(3, 4)` là vị trí sang ngang 3 mét và đi dọc 4 mét. Có thể viết `x, y = point` để lấy hai số ra; bản thân tuple không cho sửa trực tiếp từng phần tử nên phù hợp với việc giữ nguyên tọa độ ghi nhận. Muốn biết một điểm cách gốc ít nhất 5 mét, so tổng **bình phương hai độ dịch chuyển** với 25; ví dụ `(3, 4)` có các phần 9 và 16, cộng thành 25 nên vừa chạm ngưỡng. Cách so này tránh phải tính căn bậc hai nhưng vẫn cho đúng kết quả.

**Quy trình:**
1. Lưu mười tuple tọa độ, mỗi hàng là một vị trí.
2. Tách `x, y` của từng tuple và đếm điểm đạt ngưỡng.
3. In điểm đầu, số quan sát và số điểm đủ xa.

**No Note — Không chú thích**

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

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Đếm trong 10 tọa độ robot có bao nhiêu điểm xa gốc ít nhất 5 đơn vị.
# Dữ liệu: 10 tuple (x,y) vị trí robot, đơn vị tọa độ trong ví dụ.
positions = [(3,4),(0,2),(5,0),(1,1),(2,3),(4,1),(6,0),(1,4),(2,2),(5,5)]
# [0] lấy tọa độ đầu, tách hai phần tuple vào first_x và first_y.
first_x, first_y = positions[0]
far_count = 0
# Tách từng tuple thành x, y để so ngưỡng.
for x, y in positions:
    # Bình phương x,y rồi cộng; >=25 tương đương khoảng cách đến (0,0) ít nhất 5 đơn vị, không cần lấy căn.
    if x*x + y*y >= 25:
        far_count += 1
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
if len(positions) != 10:
    # raise báo lỗi rồi dừng luồng hiện tại nếu dữ liệu không đáp ứng yêu cầu.
    raise ValueError("Cần đủ 10 vị trí robot.")
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
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

**Tình huống thực tế:** Một tổ chức chuẩn bị gửi thông báo cho **12 dòng email thử nghiệm**. Mỗi dòng là email đã được một người điền, nhưng cùng một địa chỉ có thể xuất hiện vài lần hoặc khác chữ hoa/thường và khoảng trắng, chẳng hạn ` Test@Example.INVALID ` với `test@example.invalid`. Trước khi gửi, nhân viên muốn biết có bao nhiêu địa chỉ khác nhau và xem danh sách không lặp, theo thứ tự dễ kiểm tra.

**Vì sao chọn cách này?** `set` là **tập hợp** chỉ giữ mỗi giá trị khác nhau một lần. Tuy nhiên `set` không tự hiểu `Test@Example.INVALID` và `test@example.invalid` là cùng một chuỗi, nên phải làm sạch khoảng trắng bằng `strip()` và thống nhất chữ thường bằng `lower()` trước. Sau đó thêm từng email vào set để xóa bản ghi lặp. Vì set không giữ thứ tự ổn định cho việc in báo cáo, dùng `sorted()` để sắp danh sách. Đây là phép lọc **địa chỉ trùng theo cách viết**, không chứng minh địa chỉ thật sự tồn tại.

**Quy trình:**
1. Chuẩn hóa mười hai email sang chữ thường, bỏ khoảng trắng biên.
2. Đưa dữ liệu vào Set để loại các bản ghi giống nhau.
3. Báo số email gốc, số email duy nhất và số lượt thừa.

**No Note — Không chú thích**

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

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Chuẩn hóa 12 email rồi đếm số địa chỉ khác nhau.
# Dữ liệu: 12 địa chỉ email với chữ hoa và khoảng trắng thừa.
raw = ["Lan@EXAMPLE.invalid","an@example.invalid"," LAN@example.invalid ","binh@example.invalid","chi@example.invalid","An@Example.INVALID","dung@example.invalid","ha@example.invalid","Minh@example.invalid","lan@example.invalid","trang@example.invalid","ha@example.invalid"]
normalized = []
for email in raw:
    # strip() xóa khoảng trắng hai đầu; lower() hạ chữ hoa để cùng email có dạng thống nhất.
    normalized.append(email.strip().lower())
# set() bỏ email trùng sau khi làm sạch, len() của set cho số địa chỉ khác nhau.
unique = set(normalized)
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
if len(raw) != 12:
    # raise báo lỗi rồi dừng luồng hiện tại nếu dữ liệu không đáp ứng yêu cầu.
    raise ValueError("Cần đủ 12 dòng email đầu vào.")
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
print("Dòng nhận:", len(raw))
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
print("Email duy nhất:", len(unique))
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
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

**Tình huống thực tế:** Trung tâm có **15 lượt đăng ký môn**, mỗi dòng chứa mã học viên cùng tên môn **Python** hoặc **AI**. Một học viên đăng ký cả hai môn sẽ có hai dòng, vì thế số dòng không bằng số người. Giáo vụ cần danh sách những người học **cả Python và AI**, cùng tổng số học viên khác nhau đã đăng ký ít nhất một môn.

**Vì sao chọn cách này?** Mỗi môn cần một tập mã học viên: tập Python và tập AI. Với một người H03 có mặt trong cả hai tập, phép **giao** `&` sẽ giữ H03 vì người ấy xuất hiện ở cả hai; phép **hợp** `|` giữ những ai đăng ký ít nhất một môn. Số người khác nhau được đếm từ hợp, chứ không phải đếm 15 lượt vì một người có thể ghi hai lần. Set phù hợp ở đây vì mục tiêu là kiểm tra **sự có mặt của một mã**, không phải đếm số lần học lại cùng môn.

**Quy trình:**
1. Lưu 15 cặp `(mã học viên, môn)` có nghĩa rõ.
2. Tạo Set mã cho từng môn, lấy giao và hợp.
3. Sắp mã trong giao để in ổn định và đếm số người riêng biệt.

**No Note — Không chú thích**

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

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tìm học viên đăng ký cả Python và AI trong 15 lượt.
# Dữ liệu: 15 bộ (mã học viên, tên môn); một học viên có thể đăng ký hai môn.
registrations = [("SV01","Python"),("SV02","Python"),("SV03","AI"),("SV01","AI"),("SV04","Python"),("SV05","AI"),("SV06","Python"),("SV07","AI"),("SV02","AI"),("SV08","Python"),("SV09","Python"),("SV10","AI"),("SV03","Python"),("SV11","Python"),("SV12","AI")]
# set() tạo tập rỗng, mỗi mã học viên xuất hiện tối đa một lần.
python_students = set()
# set() tạo tập rỗng, mỗi mã học viên xuất hiện tối đa một lần.
ai_students = set()
for student, subject in registrations:
    if subject == "Python":
        # add() đưa mã vào tập học Python, tự bỏ trùng.
        python_students.add(student)
    if subject == "AI":
        # add() đưa mã vào tập học AI, tự bỏ trùng.
        ai_students.add(student)
# & lấy học viên có ở cả hai tập; sorted() để in mã theo thứ tự.
both = sorted(python_students & ai_students)
# | lấy tất cả học viên thuộc ít nhất một môn, bỏ trùng.
all_students = python_students | ai_students
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
if len(registrations) != 15:
    # raise báo lỗi rồi dừng luồng hiện tại nếu dữ liệu không đáp ứng yêu cầu.
    raise ValueError("Cần đúng 15 lượt đăng ký hai môn.")
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
print("Lượt đăng ký:", len(registrations))
# join() nối các chuỗi bằng ký tự phân cách, ở đây là dấu phẩy và khoảng trắng.
print("Học cả hai:", ", ".join(both))
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
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

**Tình huống thực tế:** Hai câu lạc bộ A và B nhận **18 lượt đăng ký**, mỗi lượt có mã thành viên và tên câu lạc bộ. Một người có thể tham gia cả hai, nhưng lượt thứ 15 không có mã người (`None`) nên chưa thể xác định ai đăng ký. Người quản lý muốn tách lượt thiếu mã, liệt kê người **chỉ tham gia A**, và người **tham gia cả A lẫn B**.

**Vì sao chọn cách này?** Trước tiên kiểm tra mã thành viên có bị thiếu không. `None` nghĩa là **chưa biết người đăng ký**, nên không thêm vào tập; nếu thêm, hệ thống sẽ xem `None` như một thành viên giả và đếm sai. Từ các mã hợp lệ, tạo tập A và tập B. **Hiệu** `A - B` nghĩa là người có ở A nhưng không có ở B, còn **giao** `A & B` là người có ở cả hai. Hai phép trả lời hai câu hỏi khác nhau; số lượt đăng ký không dùng thay số người vì người có thể đăng ký hai nhóm.

**Quy trình:**
1. Kiểm tra từng cặp, bỏ lượt có ID None và đếm lỗi.
2. Lập tập thành viên A và B từ 17 lượt hợp lệ.
3. Lấy hiệu/giao rồi in danh sách mã đã sắp xếp.

**No Note — Không chú thích**

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

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Lọc mã thiếu trong 18 lượt tham gia, tìm nhóm A-only và tham gia cả hai.
# Dữ liệu: 18 bộ (mã người, nhóm A/B), None là lượt thiếu ID.
registrations = [("U01","A"),("U02","A"),("U03","B"),("U04","A"),("U05","B"),("U06","A"),("U07","B"),("U08","A"),("U09","A"),("U10","B"),("U02","B"),("U04","B"),("U11","A"),("U12","B"),(None,"B"),("U13","A"),("U14","B"),("U10","A")]
valid = []
# set() tạo tập hợp các phần tử không lặp; tập hợp không bảo đảm thứ tự in.
a = set()
# set() tạo tập hợp các phần tử không lặp; tập hợp không bảo đảm thứ tự in.
b = set()
for code, group in registrations:
    # is None nhận lượt không có ID; không đưa vào tập người.
    if code is None:
        # continue bỏ lượt ID thiếu.
        continue
    # append() thêm một phần tử vào cuối danh sách và cập nhật danh sách gốc.
    valid.append((code, group))
    if group == "A":
        # add() thêm mã duy nhất vào nhóm A.
        a.add(code)
    if group == "B":
        # add() thêm mã duy nhất vào nhóm B.
        b.add(code)
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
if len(registrations) != 18:
    # raise báo lỗi rồi dừng luồng hiện tại nếu dữ liệu không đáp ứng yêu cầu.
    raise ValueError("Cần đúng 18 lượt tham gia nhóm.")
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
print("Lượt ghi:", len(registrations))
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
print("Thiếu ID:", len(registrations) - len(valid))
# a - b là người chỉ thuộc nhóm A; sorted() xếp mã để in ổn định.
print("Chỉ nhóm A:", ", ".join(sorted(a - b)))
# a & b là người thuộc cả hai nhóm.
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

**Tình huống thực tế:** Một khóa học theo dõi **8 học viên S01 đến S08** qua **20 lượt ghi nhận kỹ năng**. Mỗi lượt là cặp `(mã học viên, tên kỹ năng)`; khóa học yêu cầu đủ ba kỹ năng **Python, SQL và AI**. Trong các lượt ghi có một lần S06–Python bị lặp và một lần S06 chưa có tên kỹ năng (`None`). Giáo viên muốn biết ai đã học đủ ba kỹ năng, riêng S06 còn thiếu kỹ năng nào, và số lượt ghi trùng hoặc thiếu thông tin.

**Vì sao chọn cách này?** Tuple `(người, kỹ năng)` giúp ghi rõ **ai đã học gì**; hai dòng chỉ là trùng khi **cả người lẫn kỹ năng đều giống nhau**. Set các cặp loại bỏ lần ghi S06–Python bị lặp nhưng vẫn giữ S06–SQL nếu có. `None` là **kỹ năng chưa xác định**, không thể tự coi là một môn đã hoàn thành, nên tách sang nhóm cần bổ sung thông tin. Với từng học viên, so tập kỹ năng đã ghi với tập yêu cầu `{Python, SQL, AI}`: **hiệu** `required - done` chính là các môn còn thiếu. Chỉ học viên có đủ cả ba mới được tính hoàn thành.

**Quy trình:**
1. Đọc đủ 20 lượt và tách những lượt chưa biết tên kỹ năng.
2. Dùng Set các tuple `(student, skill)` để loại lượt giống hệt nhau.
3. Với mỗi người, so `required` với tập đã học, tổng hợp người đủ khóa và báo chi tiết S06.

**No Note — Không chú thích**

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

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Đối chiếu 20 lượt học kỹ năng, gộp trùng và tìm học viên đủ ba môn.
# Dữ liệu: 20 bộ (mã học viên, kỹ năng); None thiếu kỹ năng và có lượt trùng.
records = [("S01","Python"),("S01","SQL"),("S01","AI"),("S02","Python"),("S02","SQL"),("S03","AI"),("S03","SQL"),("S04","Python"),("S04","AI"),("S05","Python"),("S05","SQL"),("S05","AI"),("S06","Python"),("S06","Python"),("S06",None),("S07","SQL"),("S07","AI"),("S08","Python"),("S08","SQL"),("S08","AI")]
required = {"Python", "SQL", "AI"}
valid = []
# set() tạo tập hợp các phần tử không lặp; tập hợp không bảo đảm thứ tự in.
all_student_codes = set()
for student, skill in records:
    # add() lưu toàn bộ mã đã thấy, kể cả khi lượt có kỹ năng None.
    all_student_codes.add(student)
    # is not None chỉ giữ bản ghi có tên kỹ năng, khác bản ghi thiếu.
    if skill is not None:
        # append() thêm một phần tử vào cuối danh sách và cập nhật danh sách gốc.
        valid.append((student, skill))
# set() loại các cặp (học viên, kỹ năng) trùng nhau.
unique_pairs = set(valid)
# sorted() xếp mã học viên để duyệt ổn định.
all_students = sorted(all_student_codes)
completed = []
# set() tạo tập hợp các phần tử không lặp; tập hợp không bảo đảm thứ tự in.
missing_s06 = set()
for student in all_students:
    # set() tạo tập hợp các phần tử không lặp; tập hợp không bảo đảm thứ tự in.
    learned = set()
    for user, skill in unique_pairs:
        if user == student:
            # add() gom kỹ năng khác nhau của cùng học viên.
            learned.add(skill)
    # Hiệu set tìm bộ kỹ năng bắt buộc chưa học.
    remaining = required - learned
    # not kiểm tra set còn thiếu đã rỗng, tức học viên đủ ba kỹ năng.
    if not remaining:
        # append() thêm một phần tử vào cuối danh sách và cập nhật danh sách gốc.
        completed.append(student)
    if student == "S06":
        missing_s06 = remaining
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
if len(records) != 20:
    # raise báo lỗi rồi dừng luồng hiện tại nếu dữ liệu không đáp ứng yêu cầu.
    raise ValueError("Cần kiểm tra đủ 20 lượt kỹ năng.")
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
print("Lượt ghi:", len(records))
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
print("Thiếu kỹ năng:", len(records) - len(valid))
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
print("Lượt trùng:", len(valid) - len(unique_pairs))
# join() nối các chuỗi bằng ký tự phân cách, ở đây là dấu phẩy và khoảng trắng.
print("Hoàn tất:", ", ".join(completed))
# sorted() làm thứ tự tên môn thiếu ổn định khi in.
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

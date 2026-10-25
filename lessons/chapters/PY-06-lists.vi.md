# PY-06 — List, chỉ số, cắt danh sách và sắp xếp


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **List** — danh sách; **Index** — chỉ số.

`Vòng lặp → List → Vector/Array`

**Học xong dùng để làm gì?** Lưu và xử lý danh sách điểm, đơn hàng hoặc sản phẩm theo thứ tự; thêm, xóa, sửa và duyệt từng phần tử.

**Kết nối kiến thức tiếp theo:** PY-07 dùng Tuple cho dữ liệu cố định và Set để bỏ giá trị lặp.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Giải thích dễ nhớ |
|---|---|---|
| List | danh sách | Tập hợp có thứ tự, có thể thay đổi |
| Index | chỉ số | Vị trí tính từ 0 để lấy phần tử |
| Slice | cắt lát | Lấy đoạn phần tử theo start:stop |
| Mutability | khả năng sửa | Có thể cập nhật phần tử của danh sách |

## 3. Hàm và cú pháp Python

**Từ vựng trong mục:** **Function** — hàm; **Argument** — đối số.

| Hàm / cú pháp | Mục đích và lựa chọn liên quan |
|---|---|
| `append(), extend(), insert()` | Thêm từng phần tử hoặc nhiều phần tử vào danh sách |
| `pop(), remove(), del` | Xóa theo vị trí hoặc giá trị |
| `sort(), sorted()` | Sắp xếp tại chỗ hoặc tạo danh sách mới |
| `items[start:stop]` | Lấy vùng con không bao gồm stop |

## 4. Khái niệm liên quan

Một cửa hàng cần ghi các món trong giỏ theo đúng thứ tự khách thêm vào. **List** là cấu trúc Python lưu nhiều giá trị trong một biến, được viết bằng dấu ngoặc vuông `[]`. Từ giỏ hàng này, ta lần lượt học cách tạo danh sách, tìm theo vị trí, lấy một đoạn và thay đổi một món; đó cũng là nền tảng để duyệt dữ liệu bằng vòng `for`.

### 4.1. List — Danh sách

**Từ vựng trong mục:** **List** — danh sách; **Element** — phần tử.

List giữ các phần tử theo thứ tự, và mỗi phần tử có thể là tên món hàng, số hoặc một kiểu dữ liệu khác. Giỏ hàng ban đầu gồm `milk` (sữa) và `bread` (bánh mì); ta đặt cả hai vào biến `basket` để xử lý cùng nhau. Dùng dấu `[]` để tạo danh sách, dấu phẩy ngăn cách các phần tử.

```python
# Mục đích: Danh sách.
basket = ['milk', 'bread']
print(basket)
```

**Kết quả khi chạy:**

```text
['milk', 'bread']
```

Danh sách có hai phần tử theo thứ tự sữa trước, bánh mì sau. Khác với một chuỗi dài, từng món có thể được truy cập và thay đổi riêng.

### 4.2. Index — Vị trí phần tử

**Từ vựng trong mục:** **Index** — chỉ số; **Element** — phần tử.

Khi biết món cần lấy nằm ở vị trí nào, ta dùng **chỉ số**. Python bắt đầu đếm từ `0`: với `['milk', 'bread']`, `basket[0]` là `milk`, còn `basket[1]` là `bread`; `basket[-1]` cũng chỉ phần tử cuối. Chỉ số nằm ngoài giới hạn danh sách sẽ gây `IndexError`.

```python
# Mục đích: Vị trí phần tử.
basket = ['milk', 'bread']
print(basket[0])
```

**Kết quả khi chạy:**

```text
milk
```

Chỉ số `0` lấy đúng món sữa ở vị trí đầu tiên, không phải phần tử thứ hai.

### 4.3. Slice — Lấy một đoạn danh sách

**Từ vựng trong mục:** **Slice** — cắt lát; **Start/stop** — vị trí bắt đầu/kết thúc.

Nếu giỏ có ba món `milk`, `bread`, `rice` và chỉ muốn lấy hai món đầu, ta dùng `basket[:2]`. Với lát cắt `[start:stop]`, vị trí `start` được lấy, còn `stop` **không được lấy**. Bỏ trống `start` nghĩa là bắt đầu từ đầu danh sách. Lát cắt tạo list mới, không xóa phần tử khỏi giỏ gốc.

```python
# Mục đích: Lấy một đoạn danh sách.
basket = ['milk', 'bread', 'rice']
print(basket[:2])
```

**Kết quả khi chạy:**

```text
['milk', 'bread']
```

Kết quả gồm sữa và bánh mì; `rice` ở chỉ số `2` nằm ngoài đoạn được lấy.

### 4.4. Mutability — Thay đổi nội dung danh sách

**Từ vựng trong mục:** **Mutability** — khả năng thay đổi; **Assignment** — phép gán.

Khác với tuple ở bài kế tiếp, **List là kiểu có thể sửa** sau khi tạo. Nếu cửa hàng đổi món thứ hai từ `bread` thành `rice`, ta gán trực tiếp `basket[1] = 'rice'`. Danh sách vẫn có hai phần tử, chỉ giá trị tại vị trí 1 được thay. Muốn thêm món mới vào cuối thì dùng `append()`, không phải phép gán này.

```python
# Mục đích: Thay đổi nội dung danh sách.
basket = ['milk', 'bread']
basket[1] = 'rice'
print(basket)
```

**Kết quả khi chạy:**

```text
['milk', 'rice']
```

Món thứ hai đổi thành gạo; món sữa đầu tiên vẫn giữ nguyên.
### 4.5. Sorting — Sắp xếp List

**Từ vựng trong mục:** **Sorting** — sắp xếp; **Ascending/descending** — tăng dần/giảm dần.

Khi có điểm ưu tiên `[7, 9, 4]`, ta thường muốn xem điểm cao trước. Hàm `sorted(scores, reverse=True)` tạo **List mới** theo thứ tự giảm dần; `reverse=False` (mặc định) cho thứ tự tăng dần. List ban đầu không bị sửa bởi `sorted()`, khác với phương thức `scores.sort()` vốn sắp xếp trực tiếp List gốc. Với ví dụ này, điểm 9 đứng đầu, rồi 7 và 4.

```python
# Mục đích: Sắp xếp List.
scores = [7, 9, 4]
ranked = sorted(scores, reverse=True)
print(ranked)
```

**Kết quả khi chạy:**

```text
[9, 7, 4]
```

Danh sách kết quả được sắp theo điểm giảm dần. Các điểm số không bị thay đổi, chỉ thứ tự của chúng khác đi.

## 5. Năm tình huống List — tăng độ khó từ thao tác đến hàng đợi

### Tình huống 1 — Cấp 1: Chỉnh giỏ hàng 10 sản phẩm

**Từ vựng trong mục:** **List** — danh sách; **Append** — thêm cuối; **Index** — chỉ số.

**Tình huống thực tế:** Giỏ hàng bán lẻ chứa **10 mặt hàng** theo thứ tự quét mã (mỗi phần tử là tên một món), từ `Gạo` đến `Táo`. Khách chọn thêm `Bánh` trước khi thanh toán. Nhân viên cần xem số mặt hàng ban đầu, số mặt hàng sau khi thêm và tên món cuối mà không xóa dữ liệu cũ.

**Vì sao chọn cách này?** `append()` thêm đúng một phần tử vào cuối list; `len()` kiểm tra độ dài trước/sau. Chưa cần lọc hay sắp xếp vì khách muốn giữ nguyên thứ tự đã quét.

**Quy trình:**
1. Lưu đúng 10 tên món trong list.
2. Ghi độ dài ban đầu và thêm sản phẩm bằng `append()`.
3. Đối chiếu độ dài tăng đúng một và đọc phần tử cuối.

```python
basket = ["Gạo", "Sữa", "Trứng", "Dầu", "Muối", "Đường", "Mì", "Cam", "Bơ", "Táo"]
before = len(basket)
basket.append("Bánh")
if before != 10 or len(basket) != before + 1:
    raise ValueError("Danh sách phải bắt đầu với 10 món và tăng đúng một món.")
print("Ban đầu:", before)
print("Sau thêm:", len(basket))
print("Món cuối:", basket[-1])
```

**Kết quả khi chạy:**

```text
Ban đầu: 10
Sau thêm: 11
Món cuối: Bánh
```

Đầu vào có 10 bản ghi sản phẩm; danh sách sau thao tác có 11 món vì khách thêm đúng một mặt hàng.

### Tình huống 2 — Cấp 2: Lấy ba yêu cầu quan trọng nhất từ 12 phiếu

**Từ vựng trong mục:** **Sort** — sắp xếp; **Slice** — cắt lát; **Stable** — ổn định thứ tự.

**Tình huống thực tế:** Đội kỹ thuật tiếp nhận **12 phiếu** T01…T12; mỗi phần tử là mức ưu tiên từ 1 đến 10 (càng lớn càng gấp). Có phiếu bằng điểm nhau. Cần lấy ba phiếu ưu tiên cao nhất, **giữ thứ tự đến trước khi đồng điểm**, và không thay đổi danh sách điểm ban đầu.

**Vì sao chọn cách này?** List cho phép tạo danh sách các cặp `(điểm, thứ tự)`; `sorted()` trả danh sách mới và phép `[:3]` chọn đúng ba phiếu. Kết hợp điểm giảm và vị trí tăng để xử lý hòa điểm một cách minh bạch.

**Quy trình:**
1. Đánh số phiếu theo vị trí list (bắt đầu từ 1).
2. Tạo danh sách `(điểm âm, thứ tự, mã phiếu)` để sắp xếp từ ưu tiên cao xuống.
3. Lấy ba phiếu đầu; kiểm tra list điểm nguồn vẫn giữ thứ tự.

```python
priorities = [4,9,7,9,3,8,6,10,2,10,5,8]
ranked = []
for position, score in enumerate(priorities, 1):
    ranked.append((-score, position, f"T{position:02d}"))
ranked = sorted(ranked)
top_three = []
for row in ranked[:3]:
    top_three.append(row[2])
if len(priorities) != 12:
    raise ValueError("Cần đủ 12 phiếu ưu tiên.")
if priorities[0] != 4:
    raise ValueError("Danh sách gốc đã bị thay đổi ở phiếu T01.")
print("Phiếu:", len(priorities))
print("Ba phiếu trước:", ", ".join(top_three))
print("Điểm gốc T01:", priorities[0])
```

**Kết quả khi chạy:**

```text
Phiếu: 12
Ba phiếu trước: T08, T10, T02
Điểm gốc T01: 4
```

Dùng chỉ số gốc để phân xử hòa điểm giúp kết quả ổn định; không làm mất thông tin phiếu nào có điểm 10.

### Tình huống 3 — Cấp 3: Lọc 15 điểm và chọn nhóm cần hỗ trợ

**Từ vựng trong mục:** **Comprehension** — tạo list ngắn gọn; **Slicing** — cắt lát; **Threshold** — ngưỡng.

**Tình huống thực tế:** Trung tâm có **15 học viên** H01…H15 với điểm cuối kỳ theo thứ tự, thang 10. Điểm từ **5** được tính là đạt. Giáo viên cần danh sách mã đạt, số học viên chưa đạt và ba mã đầu tiên trong nhóm chưa đạt để sắp lịch hỗ trợ.

**Vì sao chọn cách này?** Vòng `for` đọc từng cặp vị trí–điểm; câu lệnh `if` tách nhóm đạt và nhóm chưa đạt. Viết tường minh giúp học viên nhìn thấy cách mỗi phần tử được thêm vào list. Cắt `[:3]` giới hạn số người cần gọi trước mà vẫn giữ thứ tự lớp.

**Quy trình:**
1. Dùng `enumerate(..., 1)` để liên kết điểm với mã học viên.
2. Lọc hai nhóm bằng điều kiện từ 5 trở lên hoặc dưới 5.
3. In số lượng, ba mã cần hỗ trợ và kiểm tra tổng vẫn bằng 15.

```python
grades = [4.5,7,8,3,9,5,7.5,4,6.5,10,8,2,7,5.5,9.5]
passed = []
needs_help = []
for i, grade in enumerate(grades, 1):
    student_code = f"H{i:02d}"
    if grade >= 5:
        passed.append(student_code)
    else:
        needs_help.append(student_code)
if len(grades) != 15:
    raise ValueError("Cần đủ 15 điểm học viên.")
if len(passed) + len(needs_help) != 15:
    raise ValueError("Hai nhóm điểm phải bao phủ đủ 15 học viên.")
print("Số học viên:", len(grades))
print("Đạt:", len(passed))
print("Cần hỗ trợ:", len(needs_help))
print("Gọi trước:", ", ".join(needs_help[:3]))
```

**Kết quả khi chạy:**

```text
Số học viên: 15
Đạt: 11
Cần hỗ trợ: 4
Gọi trước: H01, H04, H08
```

Điểm chính xác bằng 5 thuộc nhóm đạt. Ở cấp này yêu cầu kết hợp lọc, đếm và lấy một lát cắt có ý nghĩa.

### Tình huống 4 — Cấp 4: Sửa tồn kho 18 SKU nhưng bảo toàn bản kiểm kê

**Từ vựng trong mục:** **Mutable** — có thể thay đổi; **Copy** — sao chép; **Missing** — dữ liệu thiếu.

**Tình huống thực tế:** Kho có **18 mã SKU** theo thứ tự K01…K18, mỗi hàng là số món còn trong kho. Sau kiểm kê, K02 phải sửa từ 6 thành 4 và K08 từ 7 thành 5; K18 chưa có số liệu (`None`). Cần sửa trên **bản sao** của list, không làm thay đổi bản chụp cũ; báo hai giá trị đã sửa và số mã chưa có số liệu.

**Vì sao chọn cách này?** Nếu gán `edited = original` thì cả hai tên cùng trỏ vào một list: sửa bản mới sẽ làm hỏng chứng cứ kiểm kê cũ. `copy()` tạo list khác; chỉ số bắt đầu bằng 0 nên K02 là phần tử 1.

**Quy trình:**
1. Tạo list 18 giá trị và sao chép bằng `copy()`.
2. Sửa đúng hai vị trí sau khi kiểm kê và nhận diện dữ liệu thiếu.
3. In dữ liệu trước/sau, số lượt thiếu; xác nhận list cũ chưa bị sửa.

```python
original = [8,6,9,5,11,4,12,7,3,10,6,9,8,5,7,4,0,None]
updated = original.copy()
updated[1] = 4  # K02
updated[7] = 5  # K08
missing = []
for i, value in enumerate(updated, 1):
    if value is None:
        missing.append(f"K{i:02d}")
if len(original) != 18 or len(updated) != 18:
    raise ValueError("Cần đủ 18 mục tồn kho trong cả hai danh sách.")
if original[1] != 6 or original[7] != 7:
    raise ValueError("Sổ kiểm kê gốc không được thay đổi.")
print("SKU:", len(updated))
print("K02 cũ/mới:", original[1], updated[1])
print("K08 cũ/mới:", original[7], updated[7])
print("Chưa kiểm kê:", ", ".join(missing))
```

**Kết quả khi chạy:**

```text
SKU: 18
K02 cũ/mới: 6 4
K08 cũ/mới: 7 5
Chưa kiểm kê: K18
```

`None` không có nghĩa tồn kho bằng 0; cấp này đòi hỏi giữ nguyên chứng cứ, sửa đúng chỉ số và không lặng lẽ thay số đo thiếu.

### Tình huống 5 — Cấp 5: Xây hàng đợi 20 phiếu theo mức độ ưu tiên và FIFO

**Từ vựng trong mục:** **Queue** — hàng đợi; **Stable sort** — sắp xếp ổn định; **Validation** — kiểm tra.

**Tình huống thực tế:** Bàn hỗ trợ nhận **20 phiếu** R01…R20, mỗi hàng chứa mức ưu tiên 1–3 (3 khẩn cấp nhất). R12 chưa được chấm ưu tiên (`None`) nên phải chờ xác nhận. Cần tạo danh sách xử lý phiếu đã đủ dữ liệu: ưu tiên 3 trước 2 trước 1, **nếu cùng điểm thì phiếu đến trước xử lý trước**. In năm mã xử lý đầu tiên và số phiếu đang chờ bổ sung.

**Vì sao chọn cách này?** Danh sách ban đầu giữ thứ tự nhận. Khi sắp xếp, dùng cặp `(-ưu tiên, thứ tự tới)`; không đặt `None` bằng 0 vì đó là phiếu chưa đủ thông tin. Slicing chọn đúng năm việc đầu, không loại bỏ phiếu còn lại.

**Quy trình:**
1. Tạo 20 bản ghi vị trí–mức ưu tiên và xác nhận hàng R12 thiếu điểm.
2. Lọc phiếu có ưu tiên hợp lệ; tạo khóa ưu tiên giảm và vị trí tới tăng.
3. Sắp xếp thành hàng đợi xử lý, đối chiếu số dòng và in năm phiếu đầu.

```python
priorities = [3,1,2,3,2,1,3,2,1,3,2,None,1,3,2,1,3,2,1,2]
queue = []
for i, value in enumerate(priorities, 1):
    queue.append((f"R{i:02d}", value))
missing = []
ready = []
for arrival, (code, level) in enumerate(queue):
    if level is None:
        missing.append(code)
    else:
        ready.append((-level, arrival, code))
ready.sort()
next_five = []
for neg_level, arrival, code in ready[:5]:
    next_five.append(code)
if len(queue) != 20:
    raise ValueError("Cần đủ 20 phiếu hỗ trợ.")
if len(ready) + len(missing) != 20:
    raise ValueError("Các phiếu sẵn sàng và thiếu điểm phải đủ 20.")
print("Tổng phiếu:", len(queue))
print("Sẵn sàng:", len(ready))
print("Thiếu ưu tiên:", ", ".join(missing))
print("Xử lý trước:", ", ".join(next_five))
```

**Kết quả khi chạy:**

```text
Tổng phiếu: 20
Sẵn sàng: 19
Thiếu ưu tiên: R12
Xử lý trước: R01, R04, R07, R10, R14
```

Mỗi vị trí trong list là thời điểm nhận phiếu; dùng thêm vị trí như khóa phụ giúp minh bạch vì sao một phiếu cùng ưu tiên phải được xử lý trước phiếu khác.

## 6. Nhầm lẫn dễ gặp

- Chỉ số list bắt đầu từ `0`; truy cập vượt ngoài list gây `IndexError`.
- `append([3,4])` thêm cả list như một phần tử, còn `extend([3,4])` thêm lần lượt `3` và `4`.
- `list.sort()` sửa list gốc và trả về `None`; `sorted(list)` tạo list mới.
- `pop(0)` sẽ lỗi nếu list rỗng. Với hàng đợi lớn, nên dùng `collections.deque`.
- Cắt list bằng `[:2]` không lấy phần tử có chỉ số `2`.

## 7. Trắc nghiệm

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is a Python List? | List trong Python là gì?**

A. A mapping of keys to values | Ánh xạ từ khóa sang giá trị

B. An ordered, mutable collection | Tập hợp có thứ tự và có thể sửa

C. An unordered collection of unique items | Tập hợp không thứ tự gồm phần tử duy nhất

D. An immutable sequence of items | Dãy phần tử bất biến

**Đáp án: B**

**Giải thích:** List trong Python là tập hợp có thứ tự và có thể thay đổi, nên mỗi phần tử có vị trí và có thể được sửa sau khi tạo. Ví dụ `[10, 20]` chứa hai phần tử theo thứ tự xác định; set không hỗ trợ chỉ số vị trí.


**Q2. What is the index of the first list element? | Chỉ số của phần tử List đầu tiên là gì?**

A. `0` | `0`

B. `-1` | `-1`

C. `len(a)` | `len(a)`

D. `1` | `1`

**Đáp án: A**

**Giải thích:** Chỉ số List bắt đầu từ `0`, vì vậy `a[0]` lấy phần tử đầu và `a[1]` lấy phần tử thứ hai. Chỉ số âm `-1` mang nghĩa khác: phần tử cuối.


**Q3. For a List `a`, what does `a[:2]` return? | Với `a` là một List, `a[:2]` trả về gì?**

A. Items from index 2 to the end | Các phần tử từ chỉ số 2 đến cuối

B. A new list of the first two items | List mới gồm hai phần tử đầu

C. A new list of the last two items | List mới gồm hai phần tử cuối

D. Only item at index 2 | Chỉ phần tử tại chỉ số 2

**Đáp án: B**

**Giải thích:** Lát cắt `a[:2]` mặc định bắt đầu tại chỉ số 0 và dừng trước chỉ số 2, tạo List mới gồm hai phần tử đầu. Với `[4, 5, 6]`, kết quả là `[4, 5]`, không phải phần tử tại chỉ số 2.


**Q4. What does 'mutable' mean for a list? | List có tính mutable nghĩa là gì?**

A. Its contents can be changed after creation | Có thể sửa nội dung sau khi tạo

B. Its elements cannot be changed | Không thể sửa các phần tử

C. Every element must have the same type | Mọi phần tử phải cùng kiểu

D. Its elements sort automatically | Các phần tử được tự động sắp xếp

**Đáp án: A**

**Giải thích:** Mutable nghĩa là có thể thay, thêm hoặc xóa phần tử trên List hiện có. Ví dụ gán `a = [1, 2]` rồi thực hiện `a[0] = 9` làm `a` thành `[9, 2]`; tuple không cho phép gán phần tử như vậy.


**Q5. What does `append(x)` do? | `append(x)` làm gì?**

A. Inserts `x` before the first item | Chèn `x` trước phần tử đầu

B. Removes the final element and returns it | Xóa phần tử cuối và trả về

C. Adds `x` as a single final item | Thêm `x` thành một phần tử cuối

D. Adds every element of `x` separately | Thêm riêng từng phần tử của `x`

**Đáp án: C**

**Giải thích:** `append(x)` thêm toàn bộ `x` thành đúng một phần tử cuối List và sửa List tại chỗ. Vì vậy thêm `[2, 3]` bằng `append` vào `[1]` tạo phần tử List lồng nhau, không thêm từng số; muốn thêm từng số thì dùng `extend()`.


**Q6. What does `extend(items)` do? | `extend(items)` làm gì?**

A. Deletes items matching `items` | Xóa phần tử khớp `items`

B. Appends the iterable as one nested item | Thêm cả iterable thành một phần tử lồng

C. Adds the individual elements from `items` | Thêm từng phần tử từ `items`

D. Replaces the first element with `items` | Thay phần tử đầu bằng `items`

**Đáp án: C**

**Giải thích:** `extend(items)` duyệt đối số và thêm từng phần tử riêng vào List hiện có. Với `a = [1]`, `a.extend([2, 3])` tạo `[1, 2, 3]`, còn `append([2, 3])` sẽ tạo `[1, [2, 3]]`.


**Q7. What does `insert(0, x)` do? | `insert(0, x)` làm gì?**

A. Replaces the first element with `x` | Thay phần tử đầu bằng `x`

B. Inserts `x` at the front, shifting the others | Chèn `x` vào đầu, đẩy các phần tử khác sang phải

C. Removes the first element | Xóa phần tử đầu

D. Adds `x` at the end | Thêm `x` vào cuối

**Đáp án: B**

**Giải thích:** `insert(0, x)` chèn `x` trước phần tử đầu tiên và đẩy các phần tử cũ sang phải. Ví dụ chèn `9` vào đầu `[1, 2]` cho `[9, 1, 2]`, không ghi đè số `1`.


**Q8. What does `pop(0)` do on a nonempty list? | `pop(0)` làm gì với List không rỗng?**

A. Removes and returns the last item | Xóa và trả phần tử cuối

B. Returns the first item without removing it | Trả phần tử đầu nhưng không xóa

C. Deletes the first occurrence of the value zero | Xóa lần xuất hiện đầu của giá trị không

D. Removes and returns the first item | Xóa và trả phần tử đầu

**Đáp án: D**

**Giải thích:** `pop(0)` xóa phần tử đầu của List không rỗng và trả chính phần tử đã xóa. Với `[7, 8]`, kết quả trả về là `7` và List còn `[8]`; chỉ đọc `a[0]` thì không xóa phần tử nào.


**Q9. What does `remove(x)` do? | `remove(x)` dùng để làm gì?**

A. Deletes every matching value | Xóa tất cả giá trị khớp

B. Returns a sorted copy | Trả bản sao đã sắp xếp

C. Deletes the first matching value | Xóa giá trị khớp đầu tiên

D. Deletes the item at index `x` | Xóa phần tử tại chỉ số `x`

**Đáp án: C**

**Giải thích:** `remove(x)` xóa lần xuất hiện đầu tiên có giá trị bằng `x`; nó tìm theo giá trị chứ không xem `x` là chỉ số. Với `[2, 3, 2]`, `remove(2)` còn `[3, 2]`, và giá trị không tồn tại sẽ gây `ValueError`.


**Q10. What does `del a[1]` do? | `del a[1]` có tác dụng gì?**

A. Returns the removed item | Trả về phần tử đã xóa

B. Deletes the item whose value is `1` | Xóa phần tử có giá trị bằng `1`

C. Deletes the item at index one | Xóa phần tử có chỉ số 1

D. Replaces the item at index one with `None` | Thay phần tử chỉ số 1 bằng `None`

**Đáp án: C**

**Giải thích:** `del a[1]` xóa phần tử tại chỉ số 1, tức phần tử thứ hai vì chỉ số bắt đầu từ 0. Khác `remove(1)`, lệnh này dùng vị trí; khác `pop(1)`, câu lệnh `del` không trả về giá trị bị xóa.


**Q11. What does `a.sort()` return? | `a.sort()` trả về gì?**

A. The sorted indexes | Các chỉ số đã sắp xếp

B. A new sorted list | List mới đã sắp xếp

C. The same list as a return value | Trả về chính List đó

D. `None` | `None`

**Đáp án: D**

**Giải thích:** `a.sort()` sắp List tại chỗ và trả về `None`, nên chính List cũ nhận thứ tự mới. Gán `result = a.sort()` sẽ cho `None`, không phải List mới đã sắp; muốn List riêng thì dùng `sorted(a)`.


**Q12. What does `sorted(a)` do? | `sorted(a)` làm gì?**

A. Reverses the original list in place | Đảo List gốc tại chỗ

B. Produces a set of unique items | Tạo Set các phần tử duy nhất

C. Creates a new sorted list | Tạo List mới đã sắp xếp

D. Sorts `a` in place and returns `None` | Sắp `a` tại chỗ và trả `None`

**Đáp án: C**

**Giải thích:** `sorted(a)` trả về List mới đã sắp xếp và không đổi thứ tự List gốc. Nếu `a = [3, 1]`, `sorted(a)` là `[1, 3]` còn `a` vẫn `[3, 1]`, khác `a.sort()`.


**Q13. What does `a[-1]` read from a nonempty list? | `a[-1]` lấy gì từ List không rỗng?**

A. The last element | Phần tử cuối

B. The first element | Phần tử đầu

C. The number of elements | Số phần tử

D. An `IndexError` for every nonempty list | Luôn có `IndexError` với List không rỗng

**Đáp án: A**

**Giải thích:** Chỉ số `-1` chỉ phần tử cuối của List không rỗng, bất kể List dài bao nhiêu. Với `[4, 7, 9]`, `a[-1]` là `9`; còn `len(a)` đếm đủ ba phần tử.


**Q14. What does `len(a)` report? | `len(a)` cho biết gì?**

A. The number of distinct values | Số giá trị khác nhau

B. The list's memory size in bytes | Kích thước List tính theo byte

C. The final valid index | Chỉ số hợp lệ cuối

D. The number of elements | Số phần tử

**Đáp án: D**

**Giải thích:** `len(a)` trả về số phần tử ở cấp ngoài của List; một List lồng trong được tính là một phần tử. Với `[1, [2, 3]]`, độ dài là `2`, không phải `3` và không phải chỉ số cuối `1`.


**Q15. What happens for `a[10]` on a two-item list? | `a[10]` sẽ thế nào nếu List có hai phần tử?**

A. The last list element | Phần tử cuối List

B. `None` | `None`

C. The integer `0` | Số nguyên `0`

D. `IndexError` | `IndexError`

**Đáp án: D**

**Giải thích:** List gồm hai phần tử chỉ có chỉ số dương hợp lệ `0` và `1`; đọc `a[10]` vượt giới hạn nên gây `IndexError`. Python không tự trả `None` hoặc mở rộng List khi đọc chỉ số không có.


**Q16. What does `a[1] = 5` do? | `a[1] = 5` làm gì?**

A. Changes the first item to `5` | Thay phần tử đầu thành `5`

B. Replaces the second element with `5` | Thay phần tử thứ hai bằng `5`

C. Inserts a new element at index 1 | Chèn phần tử mới tại chỉ số 1

D. Adds `5` to the end | Thêm `5` vào cuối

**Đáp án: B**

**Giải thích:** `a[1] = 5` thay phần tử hiện có tại chỉ số 1 thành `5`, miễn chỉ số đó tồn tại. Với `[8, 9]`, kết quả là `[8, 5]`; lệnh không chèn thêm phần tử hay sửa chỉ số 0.


**Q17. Which operation sorts a list in place? | Thao tác nào sắp xếp ngay List gốc?**

A. `a.sort()` | `a.sort()`

B. `sorted(a)` | `sorted(a)`

C. `a.reverse()` | `a.reverse()`

D. `reversed(a)` | `reversed(a)`

**Đáp án: A**

**Giải thích:** `a.sort()` sắp xếp ngay trên List gốc nên đọc `a` sau đó thấy thứ tự mới. `sorted(a)` trả List khác, còn `reverse()` chỉ đảo vị trí hiện có, không tính thứ tự sắp xếp.


**Q18. Which expression sorts without mutating the original? | Biểu thức nào sắp xếp mà không sửa List gốc?**

A. `sorted(a)` | `sorted(a)`

B. `a.reverse()` | `a.reverse()`

C. `a.extend(sorted(a))` | `a.extend(sorted(a))`

D. `a.sort()` | `a.sort()`

**Đáp án: A**

**Giải thích:** `sorted(a)` tạo List mới theo thứ tự sắp xếp và giữ nguyên `a`. Ngược lại `a.sort()` sửa trực tiếp `a` và trả `None`, nên không thể dùng thay nhau khi cần giữ dữ liệu gốc.


**Q19. What does `reverse=True` mean in a numeric sort? | `reverse=True` có ý nghĩa gì khi sắp xếp số?**

A. Reverse each number's digits | Đảo chữ số trong từng số

B. Ascending order | Thứ tự tăng dần

C. Random element order | Thứ tự phần tử ngẫu nhiên

D. Descending numeric order | Thứ tự số giảm dần

**Đáp án: D**

**Giải thích:** Trong phép sắp số mặc định tăng dần, `reverse=True` đảo thứ tự thành giảm dần. Với `[3, 1, 2]`, `sorted(a, reverse=True)` cho `[3, 2, 1]`, không đơn thuần đảo thứ tự vị trí gốc.


**Q20. How do `append([3,4])` and `extend([3,4])` differ? | `append([3,4])` và `extend([3,4])` khác gì?**

A. Both operations sort the existing list | Cả hai đều sắp xếp List

B. `append` adds one nested list; `extend` adds two elements | `append` thêm một List con; `extend` thêm hai phần tử

C. Both operations create the same flat list | Cả hai tạo cùng List phẳng

D. `append` adds both separately and `extend` nests them | `append` thêm riêng còn `extend` lồng List

**Đáp án: B**

**Giải thích:** `append([3, 4])` thêm nguyên List con thành một phần tử, còn `extend([3, 4])` thêm riêng hai số nguyên. Bắt đầu từ `[1, 2]`, hai kết quả lần lượt là `[1, 2, [3, 4]]` và `[1, 2, 3, 4]`.

## 8. Nối sang bài tiếp theo

`Vòng lặp → List → Vector/Array`.

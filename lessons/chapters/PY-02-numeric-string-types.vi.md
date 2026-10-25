# PY-02 — Kiểu số, Boolean và chuỗi


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Integer** — số nguyên; **Float** — số thực.

`Biến → int/float/bool/str → Slicing → Xử lý văn bản`

**Học xong dùng để làm gì?** Phân biệt số và chữ khi đọc dữ liệu, đổi kiểu để tính tiền, số lượng hoặc điểm trung bình mà không ghép nhầm chuỗi.

**Kết nối kiến thức tiếp theo:** Sang PY-03, dùng toán tử tính toán và so sánh các giá trị đã có kiểu phù hợp.

## 2. English vocabulary — Từ vựng

| English | Nghĩa tiếng Việt | Giải thích |
|---|---|---|
| Integer | số nguyên | Giá trị không có phần thập phân |
| Float | số thực | Số có thể có phần lẻ |
| Boolean | giá trị logic | Giá trị True hoặc False |
| String | chuỗi | Dãy ký tự có thể cắt lát |

## 3. Các hàm và tùy chọn Python

**Từ vựng trong mục:** **Function** — hàm; **Argument** — đối số.

| Hàm / cú pháp | Mục đích và ý nghĩa lựa chọn |
|---|---|
| `str()/int()/float()` | Chuyển kiểu phù hợp trước khi xử lý |
| `strip()/lower()/upper()` | Dọn khoảng trắng và chuẩn hóa chữ |
| `split()/replace()` | Tách chuỗi hoặc thay thế đoạn văn bản |
| `s[start:stop]` | Cắt ký tự theo vị trí, không lấy chỉ số stop |


## 4. Khái niệm liên quan

**Kiểu dữ liệu (data type)** cho Python biết một giá trị biểu diễn điều gì và có thể thực hiện những phép toán nào. Số lượng món hàng thường là số nguyên, nhiệt độ có thể là số thực, điều kiện đạt/chưa đạt là Boolean, còn mã sản phẩm phải được giữ như chuỗi.

### 4.1. Integer — Số nguyên

**Từ vựng trong mục:** **Integer** — số nguyên; **Type** — kiểu dữ liệu.

`int` biểu diễn những số không có phần thập phân, ví dụ 5 sản phẩm hoặc 12 học viên. Dùng `int` khi cần đếm hoặc tính toán số lượng nguyên; khác với chuỗi `"5"`, số `5` thực hiện được phép cộng số học. Ở đây biến `n` giữ số 5 và `type(n)` kiểm tra kiểu.

```python
# Mục đích: Số nguyên.
n = 5
print(type(n))
```

**Kết quả khi chạy:**

```text
<class 'int'>
```

Kết quả cho biết `n` là số nguyên, không phải chuỗi.

### 4.2. Float — Số thực

**Từ vựng trong mục:** **Float** — số thực; **Decimal** — phần thập phân.

`float` lưu các số có phần thập phân, như 3,5 kg hàng hoặc nhiệt độ 36,5 °C. Nếu cần tính trên những số đo này, dùng số thực thay vì chữ. Trong ví dụ, `x` nhận `3.5` và `print()` hiển thị giá trị của nó.

```python
# Mục đích: Số thực.
x = 3.5
print(x)
```

**Kết quả khi chạy:**

```text
3.5
```

Dấu chấm trong code biểu diễn phần thập phân; đơn vị đo phải được xác định theo bài toán.

### 4.3. Boolean — Giá trị đúng/sai

**Từ vựng trong mục:** **Boolean** — giá trị logic; **True/False** — đúng/sai.

`bool` chỉ có hai giá trị `True` và `False`, phù hợp với câu hỏi dạng “đã thanh toán chưa?” hoặc “đủ điều kiện chưa?”. Biến `ok = True` ở đây tượng trưng cho trạng thái kiểm tra đã đạt. Đây không phải chữ `"True"`: Python hiểu là giá trị logic.

```python
# Mục đích: Giá trị đúng/sai.
ok = True
print(ok)
```

**Kết quả khi chạy:**

```text
True
```

Đầu ra là giá trị logic `True`, không phải số 1 hoặc một thông báo khác.

### 4.4. String — Chuỗi ký tự

**Từ vựng trong mục:** **String** — chuỗi; **Slice** — cắt chuỗi.

`str` lưu dãy ký tự theo đúng thứ tự, kể cả chữ số nằm trong mã như `AB12` hoặc số điện thoại bắt đầu bằng 0. Với `code = 'AB12'`, các vị trí lần lượt là 0:A, 1:B, 2:1, 3:2. Cú pháp `[:2]` lấy ký tự ở vị trí 0 và 1, không lấy vị trí 2.

```python
# Mục đích: Chuỗi ký tự.
code = 'AB12'
print(code[:2])
```

**Kết quả khi chạy:**

```text
AB
```

Hai ký tự đầu được tách ra mà chuỗi ban đầu vẫn giữ nguyên.
## 5. Năm tình huống ứng dụng — tăng dần mức độ

### Tình huống 1 — Cấp 1: Chuẩn hóa mười địa chỉ liên hệ

**Từ vựng trong mục:** **String** — chuỗi; **Strip** — bỏ khoảng trắng; **Lower** — chữ thường.

**Tình huống thực tế:** Nhóm hỗ trợ tiếp nhận **10 email giả lập** để đăng ký nhận thông báo. Mỗi dòng là email của một tài khoản nội bộ dạng `Member01@Example.INVALID`, có hai khoảng trắng ở đầu/cuối. Hãy trả về số email và địa chỉ đầu/cuối sau chuẩn hóa.

**Vì sao chọn cách này?** Chuỗi phải được xử lý bằng `strip()` và `lower()` theo đúng thứ tự; bước này chuẩn hóa cách so sánh và hiển thị, **không thay thế kiểm tra địa chỉ email hợp lệ**.

**Quy trình:**
1. Lưu mười chuỗi email thử nghiệm.
2. Bỏ khoảng trắng biên rồi chuyển thành chữ thường.
3. In số email và hai email mẫu đã chuẩn hóa.

```python
raw_emails = ["  Member01@Example.INVALID  ","  Member02@Example.INVALID  ","  Member03@Example.INVALID  ","  Member04@Example.INVALID  ","  Member05@Example.INVALID  ","  Member06@Example.INVALID  ","  Member07@Example.INVALID  ","  Member08@Example.INVALID  ","  Member09@Example.INVALID  ","  Member10@Example.INVALID  "]
cleaned = [email.strip().lower() for email in raw_emails]
assert len(cleaned) == 10
print("Số email:", len(cleaned))
print("Đầu:", cleaned[0])
print("Cuối:", cleaned[-1])
```

**Kết quả khi chạy:**

```text
Số email: 10
Đầu: member01@example.invalid
Cuối: member10@example.invalid
```

Toàn bộ 10 email đã được chuyển đổi. Miền `.invalid` được dùng có chủ đích cho dữ liệu minh họa, không phải tài khoản thật.

### Tình huống 2 — Cấp 2: Tách nhãn sản phẩm trong 12 dòng nhập liệu

**Từ vựng trong mục:** **Split** — tách chuỗi; **Delimiter** — dấu phân cách; **Normalization** — chuẩn hóa.

**Tình huống thực tế:** Thư viện lưu **12 thẻ môn học**, mỗi dòng có hai nhãn cách nhau bằng dấu phẩy, chẳng hạn `"python, AI"` và `"SQL, python"`. Nhân viên cần tách nhãn, chuẩn hóa chữ hoa/thường, rồi đếm **mỗi nhãn xuất hiện bao nhiêu lần** trong cả 12 dòng.

**Vì sao chọn cách này?** Không được coi `Python` và `python` là hai nhãn khác nhau; `split(',')` tách đúng dấu ngăn cách, `strip()` bỏ khoảng trắng quanh từng nhãn và `lower()` quy về một cách viết.

**Quy trình:**
1. Duyệt đủ 12 dòng, tách mỗi dòng thành hai nhãn.
2. Chuẩn hóa nhãn trước khi đưa vào bảng đếm.
3. In tổng dòng và số lần xuất hiện của từng nhãn theo thứ tự chữ cái.

```python
raw_labels = ["python, AI","SQL, python","math, data","Python, SQL","AI, data","math, python","data, SQL","AI, Math","python, data","SQL, AI","Math, SQL","Python, AI"]
counts = {}
for text in raw_labels:
    for part in text.split(","):
        label = part.strip().lower()
        counts[label] = counts.get(label, 0) + 1
assert len(raw_labels) == 12
print("Số dòng:", len(raw_labels))
for label in sorted(counts):
    print(label, counts[label])
```

**Kết quả khi chạy:**

```text
Số dòng: 12
ai 5
data 4
math 4
python 6
sql 5
```

Mỗi dòng đóng góp hai nhãn, tổng tất cả số đếm phải bằng 24. Đây là sự khác biệt giữa dữ liệu gốc có nhiều cách viết và từ vựng đã chuẩn hóa.

### Tình huống 3 — Cấp 3: Giữ số 0 ở đầu của 15 mã đơn hàng

**Từ vựng trong mục:** **Identifier** — mã định danh; **Slice** — cắt chuỗi; **Integer** — số nguyên.

**Tình huống thực tế:** Kho nhận **15 mã đơn hàng**, mỗi mã đúng **5 chữ số**, như `00001` đến `00015`, có khoảng trắng khi nhập. Mỗi mã là **định danh**, không phải số lượng hàng. Hãy chuẩn hóa, kiểm tra độ dài và tìm hai mã đầu/cuối mà không làm mất những số 0.

**Vì sao chọn cách này?** Đổi mã sang `int` sẽ loại các số 0 ở đầu; dùng chuỗi giữ nguyên ký tự, `strip()` bỏ khoảng trắng và `len()` xác nhận đúng độ dài. Sau đó có thể dùng slicing để đọc từng phần mã.

**Quy trình:**
1. Lưu 15 mã chuỗi.
2. Bỏ khoảng trắng và kiểm tra mã chỉ có năm chữ số.
3. In các mẫu đầu/cuối cùng ba ký tự đầu của mã đầu.

```python
raw_codes = ["  00001  ","  00002  ","  00003  ","  00004  ","  00005  ","  00006  ","  00007  ","  00008  ","  00009  ","  00010  ","  00011  ","  00012  ","  00013  ","  00014  ","  00015  "]
codes = [code.strip() for code in raw_codes]
valid = all(code.isdigit() and len(code) == 5 for code in codes)
assert len(codes) == 15
print("Số mã:", len(codes))
print("Đều hợp lệ:", valid)
print("Mã đầu:", codes[0], "| đầu mã:", codes[0][:3])
print("Mã cuối:", codes[-1])
```

**Kết quả khi chạy:**

```text
Số mã: 15
Đều hợp lệ: True
Mã đầu: 00001 | đầu mã: 000
Mã cuối: 00015
```

Đủ 15 mã được giữ nguyên 5 ký tự. Nếu dùng phép đổi sang số nguyên, thông tin định danh `00001` sẽ thành `1` và không còn đúng định dạng.

### Tình huống 4 — Cấp 4: Làm sạch 18 giá đọc từ CSV

**Từ vựng trong mục:** **Float** — số thực; **Conversion** — đổi kiểu; **Invalid input** — đầu vào sai.

**Tình huống thực tế:** Nhà cung cấp gửi **18 đơn giá** (nghìn đồng/món), mỗi dòng là một mã giá theo thứ tự P01…P18. Trong đó P03 ghi `bad` và P14 là chuỗi rỗng. Hãy kiểm tra kiểu trước khi cộng tổng các giá hợp lệ, đồng thời nêu hai mã cần sửa.

**Vì sao chọn cách này?** Không gọi `float()` trực tiếp trên toàn bộ chuỗi: dữ liệu `bad` và rỗng sẽ gây lỗi. Ở ví dụ này, giá chỉ nhận số không âm và tối đa một dấu chấm, nên có thể kiểm tra ký tự trước khi đổi.

**Quy trình:**
1. Gán 18 mã giá theo thứ tự.
2. Bỏ khoảng trắng, kiểm tra định dạng số thập phân không âm.
3. Đổi số hợp lệ thành `float`, ghi lại ID không hợp lệ rồi cộng các giá trị hợp lệ.

```python
raw_prices = ["12.5","8.0","bad","7.5","13.0","10.0","19.5","6.5","11.0","15.5","9.0","16.0","20.0","","10.5","14.5","8.5","12.0"]
valid_prices = []
invalid_ids = []
for index, raw in enumerate(raw_prices, 1):
    clean = raw.strip()
    if not clean.replace(".", "", 1).isdigit():
        invalid_ids.append(f"P{index:02d}")
        continue
    valid_prices.append(float(clean))
assert len(raw_prices) == 18
print("Giá hợp lệ:", len(valid_prices))
print("Giá lỗi:", ", ".join(invalid_ids))
print(f"Tổng giá (nghìn đồng): {sum(valid_prices):.1f}")
```

**Kết quả khi chạy:**

```text
Giá hợp lệ: 16
Giá lỗi: P03, P14
Tổng giá (nghìn đồng): 194.0
```

Đây là tổng **16 đơn giá mẫu**, không phải doanh thu; để tính doanh thu còn cần số lượng bán tương ứng. Quy tắc kiểm tra ký tự chỉ phù hợp với định dạng số không âm đơn giản của bài.

### Tình huống 5 — Cấp 5: Chuẩn hóa, kiểm tra và che 20 mã hồ sơ

**Từ vựng trong mục:** **Boolean** — đúng/sai; **String validation** — kiểm tra chuỗi; **Masking** — che thông tin.

**Tình huống thực tế:** Một hệ thống nội bộ nhận **20 mã hồ sơ giả lập**, mỗi dòng phải có mẫu `ID-` theo sau bằng đúng bốn chữ số. Trong dữ liệu có một mã sai tiền tố, một mã thiếu phần số và một mã lặp. Cần chuẩn hóa khoảng trắng, phân loại mã hợp lệ/trùng/sai rồi chỉ hiển thị hai chữ số cuối của mã hợp lệ khi gửi báo cáo.

**Vì sao chọn cách này?** Đây là bài tổng hợp các phép toán chuỗi và Boolean đã học: không thể chỉ dùng `lower()` hoặc chuyển `int` khi mã có tiền tố và ký tự 0. Dùng Set để phát hiện trùng là phần mở rộng của PY-07.

**Quy trình:**
1. Chuẩn hóa 20 chuỗi, tách tiền tố và hậu tố.
2. Xác nhận độ dài và chữ số, kiểm tra mã đã xuất hiện chưa.
3. Chỉ giữ mã hợp lệ, báo mã sai/trùng và in một mã đã che.

```python
raw_ids = [" ID-0001 "," ID-0002 "," ID-0003 "," ID-0004 "," ID-0005 "," ID-0006 ","X-0007"," ID-0008 "," ID-0009 "," ID-0010 "," ID-0011 "," ID-0004 "," ID-0013 "," ID-0014 "," ID-0015 "," ID-0016 "," ID-0017 "," ID- "," ID-0019 "," ID-0020 "]
accepted = []
invalid = []
duplicates = []
seen = set()
for raw in raw_ids:
    code = raw.strip().upper()
    suffix = code[3:]
    if not (code.startswith("ID-") and len(suffix) == 4 and suffix.isdigit()):
        invalid.append(code)
    elif code in seen:
        duplicates.append(code)
    else:
        seen.add(code)
        accepted.append(code)
assert len(raw_ids) == 20
print("Đầu vào:", len(raw_ids))
print("Hợp lệ duy nhất:", len(accepted))
print("Sai định dạng:", len(invalid))
print("Trùng:", duplicates)
print("Mã đầu đã che:", "ID-**" + accepted[0][-2:])
```

**Kết quả khi chạy:**

```text
Đầu vào: 20
Hợp lệ duy nhất: 17
Sai định dạng: 2
Trùng: ['ID-0004']
Mã đầu đã che: ID-**01
```

20 đầu vào được chia thành 17 mã hợp lệ duy nhất, hai mã sai và một bản sao; phép che chỉ giảm khả năng lộ mã trong bản tin, **không phải mã hóa hay biện pháp bảo mật hoàn chỉnh**.

## 6. Những nhầm lẫn thường gặp

- `int("12.5")` gây lỗi vì chuỗi này không viết theo dạng số nguyên; dùng `float("12.5")` nếu cần số có phần thập phân.
- Không chuyển mã đơn hoặc số điện thoại sang `int` nếu cần giữ số `0` ở đầu.
- `strip()` chỉ bỏ khoảng trắng ở hai đầu chuỗi; `lower()` không tự kiểm tra email hợp lệ.
- `s[:3]` lấy ba ký tự đầu (vị trí 0, 1, 2), không lấy ký tự ở vị trí 3.

## 7. Trắc nghiệm

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. Which description best defines an integer in Python? | Mô tả nào đúng nhất về số nguyên trong Python?**

A. An ordered sequence of characters | Dãy ký tự có thứ tự

B. A negative, zero, or positive integer without a fractional part | Số nguyên âm, số 0 hoặc số nguyên dương không có phần lẻ

C. A true/false value | Một giá trị đúng/sai

D. A floating-point number | Số thực dấu phẩy động

**Đáp án: B**

**Giải thích:** Kiểu `int` của Python lưu chính xác các số nguyên âm, số 0 và số nguyên dương như `-3`, `0`, `12`. Không loại số âm khỏi kiểu này; khác với `int`, `float` biểu diễn số dấu phẩy động, kể cả `2.0`.


**Q2. What is a float? | Float là kiểu dữ liệu nào?**

A. A whole number without a fractional part | Số không có phần thập phân

B. A floating-point number | Số thực dấu phẩy động

C. A true/false value | Một giá trị đúng/sai

D. An ordered sequence of characters | Dãy ký tự có thứ tự

**Đáp án: B**

**Giải thích:** `float` là kiểu số dấu phẩy động trong Python, ví dụ `1.5` và `2.0`. Ngay cả `2.0` dù có giá trị toán học nguyên vẫn là `float` chứ không phải `int`.


**Q3. What is a Boolean? | Boolean là gì?**

A. A true/false value | Một giá trị đúng/sai

B. A floating-point number | Số thực dấu phẩy động

C. An ordered sequence of characters | Dãy ký tự có thứ tự

D. A whole number without a fractional part | Số không có phần thập phân

**Đáp án: A**

**Giải thích:** Boolean biểu diễn một trong hai trạng thái `True` hoặc `False`, thường dùng trong điều kiện như `3 > 2`. Vai trò của nó khác việc lưu số hoặc dãy ký tự có thứ tự.


**Q4. What is a string? | Chuỗi là gì?**

A. An ordered sequence of characters | Dãy ký tự có thứ tự

B. A whole number without a fractional part | Số không có phần thập phân

C. A floating-point number | Số thực dấu phẩy động

D. A true/false value | Một giá trị đúng/sai

**Đáp án: A**

**Giải thích:** Chuỗi (`str`) là dãy ký tự Unicode có thứ tự, chẳng hạn `'Python'`. Chuỗi chữ số như `'12'` vẫn là văn bản nên cộng với chuỗi khác sẽ nối chữ, không phải cộng số.


**Q5. What does `strip()` normally remove? | `strip()` thường loại bỏ gì?**

A. Whitespace at both ends | Khoảng trắng ở hai đầu

B. Text converted to lowercase | Văn bản chuyển sang chữ thường

C. Text converted to uppercase | Văn bản chuyển sang chữ hoa

D. Substitutes matching text | Thay các đoạn chữ khớp mẫu

**Đáp án: A**

**Giải thích:** Khi không truyền tham số, `strip()` bỏ khoảng trắng ở đầu và cuối, không xóa khoảng trắng giữa chuỗi. Ví dụ `'  a b  '.strip()` thành `'a b'` và giữ dấu cách giữa `a` và `b`.


**Q6. What does `lower()` return? | `lower()` trả về gì?**

A. Substitutes matching text | Thay các đoạn chữ khớp mẫu

B. Text converted to uppercase | Văn bản chuyển sang chữ hoa

C. Text converted to lowercase | Văn bản chuyển sang chữ thường

D. Whitespace at both ends | Khoảng trắng ở hai đầu

**Đáp án: C**

**Giải thích:** `lower()` trả về bản sao chữ thường, nên `'PyThOn'.lower()` được `'python'`. Hàm không sửa chuỗi gốc tại chỗ vì chuỗi là bất biến.


**Q7. What does `upper()` return? | `upper()` trả về gì?**

A. Whitespace at both ends | Khoảng trắng ở hai đầu

B. Substitutes matching text | Thay các đoạn chữ khớp mẫu

C. Text converted to lowercase | Văn bản chuyển sang chữ thường

D. Text converted to uppercase | Văn bản chuyển sang chữ hoa

**Đáp án: D**

**Giải thích:** `upper()` trả về chữ hoa, ví dụ `'ab'.upper()` là `'AB'`. Khác `lower()`, nó đổi chữ cái về dạng hoa; ký tự như chữ số vẫn giữ nguyên.


**Q8. What does `replace(old, new)` do? | `replace(old, new)` có tác dụng gì?**

A. Whitespace at both ends | Khoảng trắng ở hai đầu

B. Text converted to uppercase | Văn bản chuyển sang chữ hoa

C. Text converted to lowercase | Văn bản chuyển sang chữ thường

D. Substitutes matching text | Thay các đoạn chữ khớp mẫu

**Đáp án: D**

**Giải thích:** `replace(old, new)` trả về chuỗi mới sau khi thay các đoạn khớp; `'aba'.replace('a', 'x')` được `'xbx'`. Hàm không sửa chuỗi gốc và không chỉ đơn thuần đổi hoa/thường.


**Q9. What does `'a,b'.split(',')` return? | `'a,b'.split(',')` trả về gì?**

A. `['a', 'b']` | `['a', 'b']`

B. `'ab'` | `'ab'`

C. `('a', 'b')` | `('a', 'b')`

D. `['a,b']` | `['a,b']`

**Đáp án: A**

**Giải thích:** `split(',')` tách văn bản tại mỗi dấu phẩy và trả về danh sách các chuỗi con: `'a,b'` thành `['a', 'b']`. Dấu phẩy là dấu phân cách nên bị bỏ đi; kết quả là list chứ không phải một chuỗi.


**Q10. What does `'ABCD'[1:3]` yield? | `'ABCD'[1:3]` cho kết quả gì?**

A. `'CD'` | `'CD'`

B. `'AB'` | `'AB'`

C. `'BC'` | `'BC'`

D. `'BCD'` | `'BCD'`

**Đáp án: C**

**Giải thích:** Chỉ số chuỗi bắt đầu từ 0, nên trong `'ABCD'`, vị trí 1 và 2 là `B` và `C`. Lát cắt `[1:3]` lấy vị trí 1 nhưng không lấy mốc dừng 3, cho `'BC'`.


**Q11. What does `len('Python')` yield? | `len('Python')` trả về gì?**

A. `5` | `5`

B. `7` | `7`

C. `'6'` (string) | `'6'` (chuỗi)

D. `6` (integer) | `6` (số nguyên)

**Đáp án: D**

**Giải thích:** `len()` đếm số ký tự trong chuỗi: `P`, `y`, `t`, `h`, `o`, `n` là sáu ký tự. Hàm trả về số nguyên `6`, không phải chuỗi `'6'`; chữ hoa/thường không đổi số lượng.


**Q12. What does `'A'.join(['x','y'])` yield? | `'A'.join(['x','y'])` tạo gì?**

A. `['x', 'A', 'y']` | `['x', 'A', 'y']`

B. `'xyA'` | `'xyA'`

C. `'xAy'` | `'xAy'`

D. `'Axy'` | `'Axy'`

**Đáp án: C**

**Giải thích:** `join()` chèn chuỗi đứng trước dấu chấm vào giữa các phần tử: `'A'.join(['x','y'])` cho `'xAy'`. Nó không thêm `A` ở đầu toàn danh sách hoặc sau phần tử cuối.


**Q13. What does `int('12')` create? | `int('12')` tạo ra gì?**

A. `ValueError` | `ValueError`

B. `12` (integer) | `12` (số nguyên)

C. `12.0` (float) | `12.0` (số thực)

D. `'12'` (string) | `'12'` (chuỗi)

**Đáp án: B**

**Giải thích:** `int('12')` đổi chuỗi số nguyên hợp lệ thành số nguyên `12` để có thể tính toán. Kết quả không còn là văn bản `'12'` và cũng không phải số thực `12.0`.


**Q14. What does `float('1.5')` create? | `float('1.5')` tạo ra gì?**

A. `ValueError` | `ValueError`

B. `1` (integer) | `1` (số nguyên)

C. `'1.5'` (string) | `'1.5'` (chuỗi)

D. `1.5` (float) | `1.5` (số thực)

**Đáp án: D**

**Giải thích:** `float('1.5')` chuyển văn bản số hợp lệ thành số thực `1.5`. Nó giữ phần lẻ thay vì cắt thành số nguyên `1`, và chuỗi hợp lệ này không gây lỗi.


**Q15. What does `str(12)` create? | `str(12)` tạo gì?**

A. `['1', '2']` | `['1', '2']`

B. `'12'` (string) | `'12'` (chuỗi)

C. `12.0` (float) | `12.0` (số thực)

D. `12` (integer) | `12` (số nguyên)

**Đáp án: B**

**Giải thích:** `str(12)` tạo biểu diễn văn bản `'12'`, phù hợp làm nhãn hoặc nối chuỗi. Kết quả không còn là số nguyên `12`: `'12' + '3'` tạo `'123'`, không phải tổng số `15`.


**Q16. What does `bool('False')` return? | `bool('False')` trả về gì?**

A. `True` | `True`

B. `False` | `False`

C. `ValueError` | `ValueError`

D. `'False'` (string) | `'False'` (chuỗi)

**Đáp án: A**

**Giải thích:** `bool()` kiểm tra tính đúng/sai của giá trị, không đọc nghĩa chữ `True` hay `False` trong văn bản. Do chuỗi `'False'` không rỗng nên `bool('False')` bằng `True`; với chuỗi, chỉ chuỗi rỗng được xem là sai.


**Q17. What is true of Python strings? | Điều nào đúng về chuỗi Python?**

A. Strings are unordered collections | Chuỗi là tập hợp không có thứ tự

B. Strings store only numbers | Chuỗi chỉ lưu số

C. Strings are immutable | Chuỗi không thể sửa trực tiếp từng ký tự

D. Strings can be changed in place with `s[0] = 'x'` | Có thể đổi chuỗi tại chỗ bằng `s[0] = 'x'`

**Đáp án: C**

**Giải thích:** Chuỗi là bất biến: gán `s[0] = 'x'` gây `TypeError`, kể cả khi `s` không rỗng. Các phép như `replace()` tạo chuỗi mới thay vì sửa từng ký tự của chuỗi cũ.


**Q18. What does `s[-1]` select for a nonempty string? | `s[-1]` lấy gì khi chuỗi không rỗng?**

A. The first character | Ký tự đầu

B. Always raises `IndexError` | Luôn gây `IndexError`

C. The final two characters | Hai ký tự cuối

D. The last character | Ký tự cuối

**Đáp án: D**

**Giải thích:** Chỉ số `-1` đếm từ cuối và lấy ký tự cuối của chuỗi không rỗng. Với `s = 'cat'`, `s[-1]` là `'t'`, còn `s[0]` lấy `'c'`.


**Q19. What does `'Ab' == 'ab'` evaluate to? | `'Ab' == 'ab'` có giá trị gì?**

A. `'False'` (string) | `'False'` (chuỗi)

B. `True` (Boolean) | `True` (Boolean)

C. `False` (Boolean) | `False` (Boolean)

D. `0` (integer) | `0` (số nguyên)

**Đáp án: C**

**Giải thích:** So sánh chuỗi xét từng ký tự và phân biệt chữ hoa/thường: `'A'` khác `'a'` nên `'Ab' == 'ab'` cho Boolean `False`. Nếu đổi cả hai chuỗi về chữ thường trước khi so sánh thì kết quả sẽ khác.


**Q20. What is the result of `'4' + '2'`? | `'4' + '2'` cho kết quả gì?**

A. `TypeError` | `TypeError`

B. `'42'` (string) | `'42'` (chuỗi)

C. `'6'` (string) | `'6'` (chuỗi)

D. `6` (integer) | `6` (số nguyên)

**Đáp án: B**

**Giải thích:** Cả hai toán hạng đều là chuỗi nên `+` nối theo thứ tự: `'4' + '2'` được `'42'`. Muốn cộng số, cần đổi kiểu trước, ví dụ `int('4') + int('2')` cho số nguyên `6`.

## 8. Nối sang bài kế tiếp

`Biến → int/float/bool/str → Slicing → Xử lý văn bản`.

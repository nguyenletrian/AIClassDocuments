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
## 5. Năm tình huống lập trình thực tế

### Tình huống 1 — Chuẩn hóa email · Cấp 1: Nhận biết dữ liệu

**Từ vựng trong mục:** **String** — chuỗi; **Method** — phương thức.

**Tình huống thực tế:** Một ứng dụng lưu email do khách nhập là `"  Lan@Example.COM "`, trong đó có khoảng trắng thừa ở đầu và cuối, còn chữ hoa và chữ thường được nhập lẫn nhau.

**Yêu cầu:** In email không còn khoảng trắng ở hai đầu và được đổi thành chữ thường.

**Vì sao chọn cách giải này?** `strip()` bỏ khoảng trắng hai đầu; `lower()` đổi chữ thành chữ thường, giúp thống nhất cách hiển thị và hỗ trợ so sánh email. Cách này không kiểm tra email có hợp lệ hay không.

**Quy trình giải:**

1. Lưu chuỗi email ban đầu.
2. Dùng `strip()` bỏ khoảng trắng đầu và cuối.
3. Dùng `lower()` đổi chữ thành chữ thường rồi in kết quả.

```python
# Mục đích: Chuẩn hóa email.
email = "  Lan@Example.COM "
print(email.strip().lower())
```

**Kết quả khi chạy:**

```text
lan@example.com
```

**Kết quả:** `lan@example.com` — email không còn khoảng trắng thừa và đã viết thường.

**Bài thực hành nâng cấp — cấp 1/5:** Trung tâm nhận **10 hồ sơ** gồm mã `id` và `value` (giá trị số, chưa nhập là `None`). Hãy chuẩn hóa một mã liên hệ bằng strip và lower. Mỗi phần tử là một hồ sơ; mã phải được coi là chuỗi để không làm mất ký tự, đặc biệt khi định dạng và che mã.

```python
values = [42, 70, 58, 91, 35, 76, 88, 64, 54, 96]
rows = [{"id": f"U{k:02d}", "value": v} for k, v in enumerate(values, 1)]
result = f"  {rows[0]['id']}@EXAMPLE.COM  ".strip().lower()
assert len(rows) == 10
print("Số hồ sơ:", len(rows))
print("Kết quả:", result)
```

**Đọc kết quả:** In đúng `Số hồ sơ: 10` cùng kết quả biến đổi của cấp 1. Học viên đối chiếu kết quả với từng chuỗi đầu vào; ở cấp 4–5, `None` không đại diện cho số 0.

### Tình huống 2 — Tách nhãn sản phẩm · Cấp 2: Xử lý nhiều bản ghi

**Từ vựng trong mục:** **String** — chuỗi; **Split** — tách.

**Tình huống thực tế:** Một cửa hàng nhận chuỗi nhãn sản phẩm `"AI,Python,Math"`. Ba nhãn được ngăn cách bằng dấu phẩy và cần tách riêng để xử lý từng nhãn.

**Yêu cầu:** Tạo danh sách gồm ba nhãn từ chuỗi này.

**Vì sao chọn cách giải này?** `split(",")` tách chuỗi ở mỗi dấu phẩy thành các phần tử riêng trong một danh sách.

**Quy trình giải:**

1. Lưu chuỗi nhãn vào `labels`.
2. Truyền dấu phẩy vào `split()` để tách các nhãn.
3. In danh sách nhận được.

```python
# Mục đích: Tách nhãn sản phẩm.
labels = "AI,Python,Math"
print(labels.split(","))
```

**Kết quả khi chạy:**

```text
['AI', 'Python', 'Math']
```

**Kết quả:** `['AI', 'Python', 'Math']` — ba nhãn được tách thành ba phần tử.

**Bài thực hành nâng cấp — cấp 2/5:** Trung tâm nhận **12 hồ sơ** gồm mã `id` và `value` (giá trị số, chưa nhập là `None`). Hãy chuẩn hóa 12 chuỗi nhận từ biểu mẫu. Mỗi phần tử là một hồ sơ; mã phải được coi là chuỗi để không làm mất ký tự, đặc biệt khi định dạng và che mã.

```python
values = [42, 70, 58, 91, 35, 76, 88, 64, 54, 96, 47, 82]
rows = [{"id": f"U{k:02d}", "value": v} for k, v in enumerate(values, 1)]
result = [f" {r['id']}@EXAMPLE.COM ".strip().lower() for r in rows]
assert len(rows) == 12
print("Số hồ sơ:", len(rows))
print("Kết quả:", result)
```

**Đọc kết quả:** In đúng `Số hồ sơ: 12` cùng kết quả biến đổi của cấp 2. Học viên đối chiếu kết quả với từng chuỗi đầu vào; ở cấp 4–5, `None` không đại diện cho số 0.

### Tình huống 3 — Giữ mã đầu 0 · Cấp 3: Lọc bằng nhiều tiêu chí

**Từ vựng trong mục:** **String** — chuỗi; **Slice** — cắt chuỗi.

**Tình huống thực tế:** Hệ thống quản lý đơn hàng lưu mã `00045`. Các số `0` đầu mã phải được giữ nguyên vì đây là mã nhận diện, không phải số để tính toán.

**Yêu cầu:** Lưu mã đơn và in ba ký tự đầu của mã để kiểm tra chúng vẫn còn nguyên.

**Vì sao chọn cách giải này?** Chuỗi `str` giữ được các số `0` đứng đầu. Cú pháp `[:3]` lấy ba ký tự đầu, không chuyển mã sang số nguyên.

**Quy trình giải:**

1. Lưu `"00045"` vào `order_id`.
2. Lấy ba ký tự đầu bằng `order_id[:3]`.
3. In kết quả để xem phần đầu của mã.

```python
# Mục đích: Giữ mã đầu 0.
order_id = "00045"
print(order_id[:3])
```

**Kết quả khi chạy:**

```text
000
```

**Kết quả:** `000` — ba ký tự đầu của mã vẫn được giữ nguyên. Chương trình không in cả mã `00045`.

**Bài thực hành nâng cấp — cấp 3/5:** Trung tâm nhận **15 hồ sơ** gồm mã `id` và `value` (giá trị số, chưa nhập là `None`). Hãy lọc đồng thời theo ngưỡng và đuôi mã. Mỗi phần tử là một hồ sơ; mã phải được coi là chuỗi để không làm mất ký tự, đặc biệt khi định dạng và che mã.

```python
values = [42, 70, 58, 91, 35, 76, 88, 64, 54, 96, 47, 82, 69, 73, 61]
rows = [{"id": f"U{k:02d}", "value": v} for k, v in enumerate(values, 1)]
result = [r['id'] for r in rows if r['value']>=70 and r['id'].endswith(('1','3','5'))]
assert len(rows) == 15
print("Số hồ sơ:", len(rows))
print("Kết quả:", result)
```

**Đọc kết quả:** In đúng `Số hồ sơ: 15` cùng kết quả biến đổi của cấp 3. Học viên đối chiếu kết quả với từng chuỗi đầu vào; ở cấp 4–5, `None` không đại diện cho số 0.

### Tình huống 4 — Đổi số từ CSV · Cấp 4: Kiểm tra dữ liệu khuyết

**Từ vựng trong mục:** **Float** — số thực; **Integer** — số nguyên.

**Tình huống thực tế:** Một cửa hàng nhập từ file CSV giá một sản phẩm là chuỗi `"12.5"` và số lượng là chuỗi `"3"`. Giá tính theo cùng đơn vị tiền của hệ thống.

**Yêu cầu:** Đổi hai chuỗi thành số, rồi tính số tiền cho ba sản phẩm.

**Vì sao chọn cách giải này?** Dùng `float()` cho giá có phần thập phân và `int()` cho số lượng nguyên, sau đó nhân hai số để tính tiền.

**Quy trình giải:**

1. Đổi `"12.5"` thành số thực bằng `float()`.
2. Đổi `"3"` thành số nguyên bằng `int()`.
3. Nhân giá và số lượng rồi in kết quả.

```python
# Mục đích: Đổi số từ CSV.
price = float("12.5")
qty = int("3")
print(price * qty)
```

**Kết quả khi chạy:**

```text
37.5
```

**Kết quả:** `37.5` đơn vị tiền — tổng giá của ba sản phẩm.

**Bài thực hành nâng cấp — cấp 4/5:** Trung tâm nhận **18 hồ sơ** gồm mã `id` và `value` (giá trị số, chưa nhập là `None`). Hãy phát hiện ô thiếu, không ép None thành chuỗi số hợp lệ. Mỗi phần tử là một hồ sơ; mã phải được coi là chuỗi để không làm mất ký tự, đặc biệt khi định dạng và che mã.

```python
values = [42, 70, 58, 91, 35, 76, 88, 64, 54, 96, 47, 82, 69, 73, 61, None, 90, 39]
rows = [{"id": f"U{k:02d}", "value": v} for k, v in enumerate(values, 1)]
result = [(r['id'], 'missing' if r['value'] is None else str(r['value'])) for r in rows]
assert len(rows) == 18
print("Số hồ sơ:", len(rows))
print("Kết quả:", result)
```

**Đọc kết quả:** In đúng `Số hồ sơ: 18` cùng kết quả biến đổi của cấp 4. Học viên đối chiếu kết quả với từng chuỗi đầu vào; ở cấp 4–5, `None` không đại diện cho số 0.

### Tình huống 5 — Che số liên lạc · Cấp 5: Tổng hợp an toàn

**Từ vựng trong mục:** **String** — chuỗi; **Slice** — cắt chuỗi.

**Tình huống thực tế:** Ứng dụng chăm sóc khách hàng có số điện thoại mẫu `0900123456`. Khi hiển thị trên màn hình, ứng dụng chỉ được để lộ ba chữ số cuối.

**Yêu cầu:** In số điện thoại dưới dạng dấu `*` che toàn bộ ký tự trừ ba số cuối.

**Vì sao chọn cách giải này?** Lưu số điện thoại dạng chuỗi để giữ số `0` đầu. `phone[-3:]` lấy ba ký tự cuối; `len(phone)-3` tính số dấu `*` cần in.

**Quy trình giải:**

1. Lưu số điện thoại dưới dạng chuỗi.
2. Tạo số dấu `*` bằng độ dài chuỗi trừ ba.
3. Ghép phần che với ba ký tự cuối rồi in.

```python
# Mục đích: Che số liên lạc.
phone = "0900123456"
print("*" * (len(phone)-3) + phone[-3:])
```

**Kết quả khi chạy:**

```text
*******456
```

**Kết quả:** `*******456` — bảy ký tự đầu được che, chỉ còn `456`.

**Bài thực hành nâng cấp — cấp 5/5:** Trung tâm nhận **20 hồ sơ** gồm mã `id` và `value` (giá trị số, chưa nhập là `None`). Hãy chuẩn hóa, che mã và báo riêng những hồ sơ thiếu dữ liệu. Mỗi phần tử là một hồ sơ; mã phải được coi là chuỗi để không làm mất ký tự, đặc biệt khi định dạng và che mã.

```python
values = [42, 70, 58, 91, 35, 76, 88, 64, 54, 96, 47, 82, 69, 73, 61, None, 90, 39, 85, None]
rows = [{"id": f"U{k:02d}", "value": v} for k, v in enumerate(values, 1)]
result = {'valid':sum(r['value'] is not None for r in rows),'masked':['*'*(len(r['id'])-2)+r['id'][-2:] for r in rows],'missing':[r['id'] for r in rows if r['value'] is None]}
assert len(rows) == 20
print("Số hồ sơ:", len(rows))
print("Kết quả:", result)
```

**Đọc kết quả:** In đúng `Số hồ sơ: 20` cùng kết quả biến đổi của cấp 5. Học viên đối chiếu kết quả với từng chuỗi đầu vào; ở cấp 4–5, `None` không đại diện cho số 0.

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

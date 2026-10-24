# PY-02 — Kiểu số, Boolean và chuỗi


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Integer** — số nguyên; **Float** — số thực.

`Biến → int/float/bool/str → Slicing → Xử lý văn bản`

Sau khi biết lưu thông tin vào biến, ta học cách phân biệt số, chữ và giá trị đúng/sai. Nhờ vậy, Python có thể tính tiền, kiểm tra điều kiện và xử lý văn bản đúng cách.

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
code = 'AB12'
print(code[:2])
```

**Kết quả khi chạy:**

```text
AB
```

Hai ký tự đầu được tách ra mà chuỗi ban đầu vẫn giữ nguyên.
## 5. Năm tình huống lập trình thực tế

### Tình huống 1 — Chuẩn hóa email

**Từ vựng trong mục:** **String** — chuỗi; **Method** — phương thức.

**Tình huống thực tế:** Một ứng dụng lưu email do khách nhập là `"  Lan@Example.COM "`, trong đó có khoảng trắng thừa ở đầu và cuối, còn chữ hoa và chữ thường được nhập lẫn nhau.

**Yêu cầu:** In email không còn khoảng trắng ở hai đầu và được đổi thành chữ thường.

**Vì sao chọn cách giải này?** `strip()` bỏ khoảng trắng hai đầu; `lower()` đổi chữ thành chữ thường, giúp thống nhất cách hiển thị và hỗ trợ so sánh email. Cách này không kiểm tra email có hợp lệ hay không.

**Quy trình giải:**

1. Lưu chuỗi email ban đầu.
2. Dùng `strip()` bỏ khoảng trắng đầu và cuối.
3. Dùng `lower()` đổi chữ thành chữ thường rồi in kết quả.

```python
email = "  Lan@Example.COM "
print(email.strip().lower())
```

**Kết quả khi chạy:**

```text
lan@example.com
```

**Kết quả:** `lan@example.com` — email không còn khoảng trắng thừa và đã viết thường.

### Tình huống 2 — Tách nhãn sản phẩm

**Từ vựng trong mục:** **String** — chuỗi; **Split** — tách.

**Tình huống thực tế:** Một cửa hàng nhận chuỗi nhãn sản phẩm `"AI,Python,Math"`. Ba nhãn được ngăn cách bằng dấu phẩy và cần tách riêng để xử lý từng nhãn.

**Yêu cầu:** Tạo danh sách gồm ba nhãn từ chuỗi này.

**Vì sao chọn cách giải này?** `split(",")` tách chuỗi ở mỗi dấu phẩy thành các phần tử riêng trong một danh sách.

**Quy trình giải:**

1. Lưu chuỗi nhãn vào `labels`.
2. Truyền dấu phẩy vào `split()` để tách các nhãn.
3. In danh sách nhận được.

```python
labels = "AI,Python,Math"
print(labels.split(","))
```

**Kết quả khi chạy:**

```text
['AI', 'Python', 'Math']
```

**Kết quả:** `['AI', 'Python', 'Math']` — ba nhãn được tách thành ba phần tử.

### Tình huống 3 — Giữ mã đầu 0

**Từ vựng trong mục:** **String** — chuỗi; **Slice** — cắt chuỗi.

**Tình huống thực tế:** Hệ thống quản lý đơn hàng lưu mã `00045`. Các số `0` đầu mã phải được giữ nguyên vì đây là mã nhận diện, không phải số để tính toán.

**Yêu cầu:** Lưu mã đơn và in ba ký tự đầu của mã để kiểm tra chúng vẫn còn nguyên.

**Vì sao chọn cách giải này?** Chuỗi `str` giữ được các số `0` đứng đầu. Cú pháp `[:3]` lấy ba ký tự đầu, không chuyển mã sang số nguyên.

**Quy trình giải:**

1. Lưu `"00045"` vào `order_id`.
2. Lấy ba ký tự đầu bằng `order_id[:3]`.
3. In kết quả để xem phần đầu của mã.

```python
order_id = "00045"
print(order_id[:3])
```

**Kết quả khi chạy:**

```text
000
```

**Kết quả:** `000` — ba ký tự đầu của mã vẫn được giữ nguyên. Chương trình không in cả mã `00045`.

### Tình huống 4 — Đổi số từ CSV

**Từ vựng trong mục:** **Float** — số thực; **Integer** — số nguyên.

**Tình huống thực tế:** Một cửa hàng nhập từ file CSV giá một sản phẩm là chuỗi `"12.5"` và số lượng là chuỗi `"3"`. Giá tính theo cùng đơn vị tiền của hệ thống.

**Yêu cầu:** Đổi hai chuỗi thành số, rồi tính số tiền cho ba sản phẩm.

**Vì sao chọn cách giải này?** Dùng `float()` cho giá có phần thập phân và `int()` cho số lượng nguyên, sau đó nhân hai số để tính tiền.

**Quy trình giải:**

1. Đổi `"12.5"` thành số thực bằng `float()`.
2. Đổi `"3"` thành số nguyên bằng `int()`.
3. Nhân giá và số lượng rồi in kết quả.

```python
price = float("12.5")
qty = int("3")
print(price * qty)
```

**Kết quả khi chạy:**

```text
37.5
```

**Kết quả:** `37.5` đơn vị tiền — tổng giá của ba sản phẩm.

### Tình huống 5 — Che số liên lạc

**Từ vựng trong mục:** **String** — chuỗi; **Slice** — cắt chuỗi.

**Tình huống thực tế:** Ứng dụng chăm sóc khách hàng có số điện thoại mẫu `0900123456`. Khi hiển thị trên màn hình, ứng dụng chỉ được để lộ ba chữ số cuối.

**Yêu cầu:** In số điện thoại dưới dạng dấu `*` che toàn bộ ký tự trừ ba số cuối.

**Vì sao chọn cách giải này?** Lưu số điện thoại dạng chuỗi để giữ số `0` đầu. `phone[-3:]` lấy ba ký tự cuối; `len(phone)-3` tính số dấu `*` cần in.

**Quy trình giải:**

1. Lưu số điện thoại dưới dạng chuỗi.
2. Tạo số dấu `*` bằng độ dài chuỗi trừ ba.
3. Ghép phần che với ba ký tự cuối rồi in.

```python
phone = "0900123456"
print("*" * (len(phone)-3) + phone[-3:])
```

**Kết quả khi chạy:**

```text
*******456
```

**Kết quả:** `*******456` — bảy ký tự đầu được che, chỉ còn `456`.

## 6. Những nhầm lẫn thường gặp

- `int("12.5")` gây lỗi vì chuỗi này không viết theo dạng số nguyên; dùng `float("12.5")` nếu cần số có phần thập phân.
- Không chuyển mã đơn hoặc số điện thoại sang `int` nếu cần giữ số `0` ở đầu.
- `strip()` chỉ bỏ khoảng trắng ở hai đầu chuỗi; `lower()` không tự kiểm tra email hợp lệ.
- `s[:3]` lấy ba ký tự đầu (vị trí 0, 1, 2), không lấy ký tự ở vị trí 3.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is an integer? — Số nguyên là gì?**

A. A whole number without a fractional part — Số không có phần thập phân

B. A floating-point number — Số thực dấu phẩy động

C. A true/false value — Một giá trị đúng/sai

D. An ordered sequence of characters — Dãy ký tự có thứ tự

**Q2. What is a float? — Float là kiểu dữ liệu nào?**

A. A whole number without a fractional part — Số không có phần thập phân

B. A floating-point number — Số thực dấu phẩy động

C. A true/false value — Một giá trị đúng/sai

D. An ordered sequence of characters — Dãy ký tự có thứ tự

**Q3. What is a Boolean? — Boolean là gì?**

A. A whole number without a fractional part — Số không có phần thập phân

B. A floating-point number — Số thực dấu phẩy động

C. A true/false value — Một giá trị đúng/sai

D. An ordered sequence of characters — Dãy ký tự có thứ tự

**Q4. What is a string? — Chuỗi là gì?**

A. A whole number without a fractional part — Số không có phần thập phân

B. A floating-point number — Số thực dấu phẩy động

C. A true/false value — Một giá trị đúng/sai

D. An ordered sequence of characters — Dãy ký tự có thứ tự

**Q5. What does `strip()` normally remove? — `strip()` thường loại bỏ gì?**

A. Whitespace at both ends — Khoảng trắng ở hai đầu

B. Text converted to lowercase — Văn bản chuyển sang chữ thường

C. Text converted to uppercase — Văn bản chuyển sang chữ hoa

D. Substitutes matching text — Thay các đoạn chữ khớp mẫu

**Q6. What does `lower()` return? — `lower()` trả về gì?**

A. Whitespace at both ends — Khoảng trắng ở hai đầu

B. Text converted to lowercase — Văn bản chuyển sang chữ thường

C. Text converted to uppercase — Văn bản chuyển sang chữ hoa

D. Substitutes matching text — Thay các đoạn chữ khớp mẫu

**Q7. What does `upper()` return? — `upper()` trả về gì?**

A. Whitespace at both ends — Khoảng trắng ở hai đầu

B. Text converted to lowercase — Văn bản chuyển sang chữ thường

C. Text converted to uppercase — Văn bản chuyển sang chữ hoa

D. Substitutes matching text — Thay các đoạn chữ khớp mẫu

**Q8. What does `replace(old, new)` do? — `replace(old, new)` có tác dụng gì?**

A. Whitespace at both ends — Khoảng trắng ở hai đầu

B. Text converted to lowercase — Văn bản chuyển sang chữ thường

C. Text converted to uppercase — Văn bản chuyển sang chữ hoa

D. Substitutes matching text — Thay các đoạn chữ khớp mẫu

**Q9. What does `'a,b'.split(',')` return? — `'a,b'.split(',')` trả về gì?**

A. `['a', 'b']` — `['a', 'b']`

B. `'BC'` — `'BC'`

C. `6` — `6`

D. `'xAy'` — `'xAy'`

**Q10. What does `'ABCD'[1:3]` yield? — `'ABCD'[1:3]` cho kết quả gì?**

A. `['a', 'b']` — `['a', 'b']`

B. `'BC'` — `'BC'`

C. `6` — `6`

D. `'xAy'` — `'xAy'`

**Q11. What does `len('Python')` yield? — `len('Python')` trả về gì?**

A. `['a', 'b']` — `['a', 'b']`

B. `'BC'` — `'BC'`

C. `6` — `6`

D. `'xAy'` — `'xAy'`

**Q12. What does `'A'.join(['x','y'])` yield? — `'A'.join(['x','y'])` tạo gì?**

A. `['a', 'b']` — `['a', 'b']`

B. `'BC'` — `'BC'`

C. `6` — `6`

D. `'xAy'` — `'xAy'`

**Q13. What does `int('12')` create? — `int('12')` tạo ra gì?**

A. The integer 12 — Số nguyên 12

B. The float 1.5 — Số thực 1.5

C. The string `'12'` — Chuỗi `'12'`

D. `True` — `True`

**Q14. What does `float('1.5')` create? — `float('1.5')` tạo ra gì?**

A. The integer 12 — Số nguyên 12

B. The float 1.5 — Số thực 1.5

C. The string `'12'` — Chuỗi `'12'`

D. `True` — `True`

**Q15. What does `str(12)` create? — `str(12)` tạo gì?**

A. The integer 12 — Số nguyên 12

B. The float 1.5 — Số thực 1.5

C. The string `'12'` — Chuỗi `'12'`

D. `True` — `True`

**Q16. What does `bool('False')` return? — `bool('False')` trả về gì?**

A. The integer 12 — Số nguyên 12

B. The float 1.5 — Số thực 1.5

C. The string `'12'` — Chuỗi `'12'`

D. `True` — `True`

**Q17. What is true of Python strings? — Điều nào đúng về chuỗi Python?**

A. Strings are immutable — Chuỗi không thể sửa trực tiếp từng ký tự

B. Strings can be changed in place with `s[0] = 'x'` — Có thể đổi chuỗi tại chỗ bằng `s[0] = 'x'`

C. Strings store only numbers — Chuỗi chỉ lưu số

D. Strings are unordered collections — Chuỗi là tập hợp không có thứ tự

**Q18. What does `s[-1]` select for a nonempty string? — `s[-1]` lấy gì khi chuỗi không rỗng?**

A. Strings are immutable — Chuỗi không thể sửa trực tiếp từng ký tự

B. The last character — Ký tự cuối

C. `False` — `False`

D. `'42'` — `'42'`

**Q19. What does `'Ab' == 'ab'` evaluate to? — `'Ab' == 'ab'` có giá trị gì?**

A. Strings are immutable — Chuỗi không thể sửa trực tiếp từng ký tự

B. The last character — Ký tự cuối

C. `False` — `False`

D. `'42'` — `'42'`

**Q20. What is the result of `'4' + '2'`? — `'4' + '2'` cho kết quả gì?**

A. Strings are immutable — Chuỗi không thể sửa trực tiếp từng ký tự

B. The last character — Ký tự cuối

C. `False` — `False`

D. `'42'` — `'42'`

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **A** | Integers represent whole-number quantities. | Số nguyên biểu diễn những lượng không có phần lẻ. |
| Q2 | **B** | Floats can represent numbers with fractional parts. | Float có thể biểu diễn số có phần thập phân. |
| Q3 | **C** | Boolean values are True and False. | Giá trị Boolean là True và False. |
| Q4 | **D** | str stores textual characters in order. | str lưu các ký tự văn bản theo thứ tự. |
| Q5 | **A** | strip removes leading and trailing whitespace by default. | strip mặc định bỏ khoảng trắng đầu và cuối. |
| Q6 | **B** | lower produces a lowercase string. | lower tạo ra chuỗi chữ thường. |
| Q7 | **C** | upper produces an uppercase string. | upper tạo ra chuỗi chữ hoa. |
| Q8 | **D** | replace returns text with specified substrings replaced. | replace trả chuỗi với đoạn khớp đã được thay. |
| Q9 | **A** | split separates the string at the comma. | split tách chuỗi tại dấu phẩy. |
| Q10 | **B** | Slicing includes index 1 and excludes index 3. | Lát cắt lấy vị trí 1 nhưng không lấy vị trí 3. |
| Q11 | **C** | The word Python contains six characters. | Từ Python có sáu ký tự. |
| Q12 | **D** | join inserts the separator A between items. | join chèn chữ A giữa các phần tử. |
| Q13 | **A** | int parses integer-formatted text. | int chuyển chuỗi biểu diễn số nguyên thành số nguyên. |
| Q14 | **B** | float parses a decimal number in text. | float chuyển chuỗi số thập phân thành số thực. |
| Q15 | **C** | str converts a number to a textual representation. | str chuyển số thành biểu diễn chữ. |
| Q16 | **D** | Any nonempty string is truthy, including the text False. | Chuỗi không rỗng có giá trị logic đúng, kể cả chữ False. |
| Q17 | **A** | Strings cannot have their characters replaced by index: `s[0] = 'x'` raises `TypeError`. Methods such as `replace()` return another string; unlike mutable lists, the original string remains unchanged. | Không thể gán lại ký tự chuỗi theo chỉ số: `s[0] = 'x'` gây `TypeError`. Hàm như `replace()` trả về chuỗi khác; khác với list có thể sửa, chuỗi ban đầu vẫn giữ nguyên. |
| Q18 | **B** | Negative indexing counts from the end. | Chỉ số âm đếm từ cuối chuỗi. |
| Q19 | **C** | String equality is case-sensitive by default. | So sánh chuỗi mặc định phân biệt hoa/thường. |
| Q20 | **D** | The plus sign concatenates strings rather than adding integers. | Dấu cộng nối chuỗi thay vì cộng số nguyên. |

## 8. Nối sang bài kế tiếp

`Biến → int/float/bool/str → Slicing → Xử lý văn bản`.

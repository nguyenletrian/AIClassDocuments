# PY-01 — Biến, đầu vào và đầu ra trong Python


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Variable** — biến; **Input** — đầu vào.

`Chương trình → Biến → Kiểu dữ liệu → Điều kiện`

Một chương trình nhận thông tin, lưu vào biến, xử lý và tạo ra kết quả. Bài này giúp hiểu các bước đó trước khi học kiểu dữ liệu và câu lệnh điều kiện.

## 2. English vocabulary — Từ vựng

| English | Nghĩa tiếng Việt | Giải thích |
|---|---|---|
| Variable | biến | Tên dùng để tham chiếu một giá trị |
| Input | đầu vào | Thông tin đưa vào chương trình |
| Output | đầu ra | Thông tin chương trình tạo ra |
| Type | kiểu dữ liệu | Nhóm giá trị như str, int, float |

## 3. Các hàm và tùy chọn Python

**Từ vựng trong mục:** **Function** — hàm; **Argument** — đối số.

| Hàm / cú pháp | Mục đích và ý nghĩa lựa chọn |
|---|---|
| `print()` | Hiển thị kết quả, nhận nhiều giá trị phân cách bằng dấu phẩy |
| `input()` | Nhận văn bản từ bàn phím; kết quả luôn là chuỗi |
| `int()/float()` | Đổi chuỗi hợp lệ sang số trước khi tính toán |
| `type()` | Kiểm tra kiểu dữ liệu khi chưa rõ đầu vào |


## 4. Khái niệm liên quan

Một chương trình thường đi theo mạch **nhận thông tin → lưu vào biến → xử lý → đưa ra kết quả**. Bài này bắt đầu từ biến và cho thấy đầu vào, đầu ra và kiểu dữ liệu phối hợp ra sao trong mạch đó.

### 4.1. Variable — Biến

**Từ vựng trong mục:** **Variable** — biến; **Assignment** — phép gán.

Biến là tên để chương trình ghi nhớ một giá trị. Khi viết `total = 12`, Python gắn tên `total` với số `12`; dòng tiếp theo đọc lại giá trị qua tên đó. Biến giúp ta dùng lại dữ liệu và thay đổi dữ liệu ở một chỗ thay vì viết số trực tiếp khắp chương trình.

```python
total = 12
print(total)
```

**Kết quả khi chạy:**

```text
12
```

`total` là tên biến, còn `12` là giá trị được in ra.

### 4.2. Input — Đầu vào

**Từ vựng trong mục:** **Input** — đầu vào; **String** — chuỗi.

Đầu vào là dữ liệu chương trình nhận để xử lý: có thể từ bàn phím, biểu mẫu hoặc tệp. Ví dụ, biểu mẫu nhận tên khách `An`, ứng dụng lưu tên đó trong biến `name`. Để ví dụ tự chạy không cần gõ phím, ta mô phỏng dữ liệu đã nhận bằng một phép gán; khi nhận trực tiếp từ bàn phím, có thể dùng `input()`.

```python
name = 'An'
print(name)
```

**Kết quả khi chạy:**

```text
An
```

Chương trình in đúng tên đã nhận. Biến có thể đến từ nhiều nguồn, không chỉ bàn phím.

### 4.3. Output — Đầu ra

**Từ vựng trong mục:** **Output** — đầu ra; **Print** — hiển thị.

Đầu ra là thông tin chương trình gửi ra ngoài sau khi xử lý. Đầu ra có thể xuất hiện trên màn hình, được lưu vào file hoặc gửi đến hệ thống khác. Trong bài căn bản, `print()` giúp nhìn thấy giá trị đang được tạo ra; chuỗi trong dấu nháy là nội dung cần hiển thị.

```python
print('Xin chào')
```

**Kết quả khi chạy:**

```text
Xin chào
```

`print()` hiển thị dòng chữ; dấu nháy chỉ là cú pháp Python, không xuất hiện trong kết quả.

### 4.4. Type — Kiểu dữ liệu

**Từ vựng trong mục:** **Type** — kiểu dữ liệu; **Float** — số thực.

Cùng một biến có thể chứa chữ hoặc số, nhưng **kiểu dữ liệu** quyết định phép xử lý nào phù hợp. Chẳng hạn mã đơn `"0007"` là chuỗi (`str`) cần giữ số 0 đầu; giá trị `2.5` là số thực (`float`) có thể dùng để tính toán. Hàm `type()` cho biết kiểu của một giá trị.

```python
print(type(2.5))
```

**Kết quả khi chạy:**

```text
<class 'float'>
```

`float` báo đây là số thực, không phải chuỗi ký tự `"2.5"`.
## 5. Năm tình huống lập trình thực tế

### Tình huống 1 — Chào khách mới

**Từ vựng trong mục:** **Variable** — biến.

**Tình huống thực tế:** Một cửa hàng muốn gửi lời chào có tên khách. Khách mới tên Lan.

**Yêu cầu:** Viết chương trình in `Xin chào Lan!`.

**Vì sao chọn cách giải này?** Lưu tên trong biến `name` rồi truyền biến vào f-string để tạo lời chào. Khi đổi khách chỉ cần sửa tên.

**Quy trình giải:**

1. Lưu tên khách vào `name`.
2. Chèn tên vào lời chào bằng f-string.
3. In lời chào.

```python
name = "Lan"
# Dùng tên đã lưu, không viết lại tên trong thông báo.
print(f"Xin chào {name}!")
```

**Kết quả khi chạy:**

```text
Xin chào Lan!
```

**Kết quả:** `Xin chào Lan!` — lời chào chứa đúng tên khách.

### Tình huống 2 — Tính tiền hóa đơn

**Từ vựng trong mục:** **Input** — đầu vào.

**Tình huống thực tế:** Một cửa hàng bán 3 sản phẩm, mỗi sản phẩm giá 120.000 đồng. Phần mềm đang lưu giá và số lượng dưới dạng chữ `"120000"` và `"3"`.

**Yêu cầu:** Tính tổng số tiền cần thanh toán.

**Vì sao chọn cách giải này?** `int()` đổi chữ số thành số nguyên để phép nhân giá với số lượng cho ra tổng tiền.

**Quy trình giải:**

1. Đổi chuỗi giá thành số bằng `int()`.
2. Đổi chuỗi số lượng thành số bằng `int()`.
3. Nhân giá với số lượng và in kết quả.

```python
price = int("120000")
quantity = int("3")
print(price * quantity)
```

**Kết quả khi chạy:**

```text
360000
```

**Kết quả:** `360000` — khách phải trả 360.000 đồng.

### Tình huống 3 — Hiển thị điểm

**Từ vựng trong mục:** **Output** — đầu ra.

**Tình huống thực tế:** Trung tâm đào tạo muốn hiển thị điểm của học viên An, đạt 8,5 điểm trên thang 10.

**Yêu cầu:** In tên và điểm theo mẫu `An: 8.5/10`.

**Vì sao chọn cách giải này?** F-string ghép tên, điểm và thang điểm thành một dòng dễ đọc.

**Quy trình giải:**

1. Lưu tên `An` và điểm `8.5`.
2. Dùng f-string ghép thông tin.
3. In kết quả.

```python
name, score = "An", 8.5
print(f"{name}: {score}/10")
```

**Kết quả khi chạy:**

```text
An: 8.5/10
```

**Kết quả:** `An: 8.5/10` — dòng thông tin gồm tên và điểm học viên.

### Tình huống 4 — Ghi nhiệt độ

**Từ vựng trong mục:** **Type** — kiểu dữ liệu.

**Tình huống thực tế:** Một cảm biến báo nhiệt độ 36,5 °C. Nhân viên cần biết số đo được lưu bằng kiểu dữ liệu gì.

**Yêu cầu:** In kiểu dữ liệu và số đo nhiệt độ.

**Vì sao chọn cách giải này?** Số có phần thập phân được lưu dưới dạng `float`; `type()` cho biết kiểu dữ liệu.

**Quy trình giải:**

1. Lưu `36.5` vào biến `temperature`.
2. Dùng `type()` xem kiểu dữ liệu.
3. In kiểu dữ liệu cùng số đo.

```python
temperature = 36.5
print(type(temperature), temperature)
```

**Kết quả khi chạy:**

```text
<class 'float'> 36.5
```

**Kết quả:** `<class 'float'> 36.5` — kiểu số thực và giá trị 36,5; code chưa in đơn vị °C.

### Tình huống 5 — Giữ mã đơn

**Từ vựng trong mục:** **Variable** — biến.

**Tình huống thực tế:** Một cửa hàng dùng mã đơn bốn chữ số, trong đó hai số `0` đầu tiên phải được giữ lại. Mã đơn hiện tại là `0007`.

**Yêu cầu:** Lưu và in mã chính xác là `0007`, kiểm tra mã vẫn bắt đầu bằng `00`.

**Vì sao chọn cách giải này?** Mã đơn là thông tin nhận diện, không phải số để tính toán; dùng chuỗi `str` để không làm mất các số `0` ở đầu.

**Quy trình giải:**

1. Lưu `"0007"` thành chuỗi trong `order_id`.
2. In mã đơn.
3. Dùng `startswith("00")` kiểm tra hai ký tự đầu; `assert` báo lỗi nếu không đúng.

```python
order_id = "0007"
print(order_id)
assert order_id.startswith("00")
```

**Kết quả khi chạy:**

```text
0007
```

**Kết quả:** `0007` — mã được in nguyên vẹn; `assert` không in thêm khi kiểm tra đúng.

## 6. Những nhầm lẫn thường gặp

- `input()` nhận chữ; cần đổi sang `int()` hoặc `float()` khi muốn tính toán với số. Chuỗi không hợp lệ có thể gây `ValueError`.
- Mã đơn `0007` phải lưu dạng chuỗi nếu cần giữ hai số `0` ở đầu.
- `print()` in kết quả, còn `type()` xem kiểu dữ liệu; hai hàm có nhiệm vụ khác nhau.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is a variable in Python? — Biến trong Python là gì?**

A. A name referring to a value — Tên tham chiếu đến một giá trị

B. Data received for processing — Dữ liệu được nhận để xử lý

C. Information produced by a program — Thông tin do chương trình tạo ra

D. How a value is represented and used — Cách biểu diễn và sử dụng một giá trị

**Q2. What is program input? — Đầu vào chương trình là gì?**

A. A name referring to a value — Tên tham chiếu đến một giá trị

B. Data received for processing — Dữ liệu được nhận để xử lý

C. Information produced by a program — Thông tin do chương trình tạo ra

D. How a value is represented and used — Cách biểu diễn và sử dụng một giá trị

**Q3. What is program output? — Đầu ra chương trình là gì?**

A. A name referring to a value — Tên tham chiếu đến một giá trị

B. Data received for processing — Dữ liệu được nhận để xử lý

C. Information produced by a program — Thông tin do chương trình tạo ra

D. How a value is represented and used — Cách biểu diễn và sử dụng một giá trị

**Q4. What does a data type describe? — Kiểu dữ liệu mô tả điều gì?**

A. A name referring to a value — Tên tham chiếu đến một giá trị

B. Data received for processing — Dữ liệu được nhận để xử lý

C. Information produced by a program — Thông tin do chương trình tạo ra

D. How a value is represented and used — Cách biểu diễn và sử dụng một giá trị

**Q5. Which function prints a value? — Hàm nào in một giá trị?**

A. `print()` — `print()`

B. `input()` — `input()`

C. `type()` — `type()`

D. `int()` — `int()`

**Q6. Which function reads keyboard input? — Hàm nào đọc dữ liệu bàn phím?**

A. `print()` — `print()`

B. `input()` — `input()`

C. `type()` — `type()`

D. `int()` — `int()`

**Q7. Which function finds a value's type? — Hàm nào kiểm tra kiểu giá trị?**

A. `print()` — `print()`

B. `input()` — `input()`

C. `type()` — `type()`

D. `int()` — `int()`

**Q8. Which function converts valid decimal digits to an integer? — Hàm nào đổi chuỗi chữ số hợp lệ thành số nguyên?**

A. `print()` — `print()`

B. `input()` — `input()`

C. `type()` — `type()`

D. `int()` — `int()`

**Q9. Which type represents a count of whole items? — Kiểu nào biểu diễn số lượng món nguyên?**

A. `int` — `int`

B. `float` — `float`

C. `str` — `str`

D. `bool` — `bool`

**Q10. Which type suits a measurement with fractions? — Kiểu nào phù hợp với số đo có phần lẻ?**

A. `int` — `int`

B. `float` — `float`

C. `str` — `str`

D. `bool` — `bool`

**Q11. Which type preserves a leading zero in an identifier? — Kiểu nào giữ số 0 đầu mã định danh?**

A. `int` — `int`

B. `float` — `float`

C. `str` — `str`

D. `bool` — `bool`

**Q12. Which type stores a true/false state? — Kiểu nào lưu trạng thái đúng/sai?**

A. `int` — `int`

B. `float` — `float`

C. `str` — `str`

D. `bool` — `bool`

**Q13. What does `x = 5` do? — `x = 5` thực hiện điều gì?**

A. Assigns the value 5 to x — Gán giá trị 5 cho x

B. A string — Một chuỗi

C. The number 2.5 — Số thực 2.5

D. `ValueError` — `ValueError`

**Q14. What is the type of `input()`'s return value? — Giá trị trả về của `input()` có kiểu nào?**

A. Assigns the value 5 to x — Gán giá trị 5 cho x

B. A string — Một chuỗi

C. The number 2.5 — Số thực 2.5

D. `ValueError` — `ValueError`

**Q15. What does `float('2.5')` produce? — `float('2.5')` tạo ra gì?**

A. Assigns the value 5 to x — Gán giá trị 5 cho x

B. A string — Một chuỗi

C. The number 2.5 — Số thực 2.5

D. `ValueError` — `ValueError`

**Q16. What does `int('abc')` raise? — `int('abc')` phát sinh gì?**

A. Assigns the value 5 to x — Gán giá trị 5 cho x

B. A string — Một chuỗi

C. The number 2.5 — Số thực 2.5

D. `ValueError` — `ValueError`

**Q17. What does `print(2, 3)` display by default? — `print(2, 3)` mặc định hiển thị gì?**

A. `2 3` — `2 3`

B. `4` — `4`

C. `float` — `float`

D. `Hi` — `Hi`

**Q18. What does `x = 2; x = 4` leave in x? — Hai phép gán `x = 2; x = 4` khiến x có giá trị gì?**

A. `2 3` — `2 3`

B. `4` — `4`

C. `float` — `float`

D. `Hi` — `Hi`

**Q19. What does `type(2.0)` return? — `type(2.0)` trả về kiểu nào?**

A. `2 3` — `2 3`

B. `4` — `4`

C. `float` — `float`

D. `Hi` — `Hi`

**Q20. What does `print('Hi')` display? — `print('Hi')` hiển thị gì?**

A. `2 3` — `2 3`

B. `4` — `4`

C. `float` — `float`

D. `Hi` — `Hi`

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **A** | A variable lets later code reuse its associated value. | Biến giúp code phía sau dùng lại giá trị đã gán. |
| Q2 | **B** | Input is supplied to a program before or during processing. | Đầu vào là thông tin được cung cấp để chương trình xử lý. |
| Q3 | **C** | Output is what a program sends out or displays. | Đầu ra là thông tin chương trình xuất ra hoặc hiển thị. |
| Q4 | **D** | A type determines valid operations and representation. | Kiểu dữ liệu quyết định phép toán phù hợp và cách biểu diễn. |
| Q5 | **A** | print displays values in the output stream. | print hiển thị giá trị ra đầu ra. |
| Q6 | **B** | input reads a line of text from the user. | input nhận một dòng văn bản từ người dùng. |
| Q7 | **C** | type reveals the Python type of an object. | type cho biết kiểu Python của đối tượng. |
| Q8 | **D** | int parses a valid integer representation. | int chuyển biểu diễn số nguyên hợp lệ thành số nguyên. |
| Q9 | **A** | int represents integer quantities without fractional parts. | int biểu diễn lượng nguyên không có phần thập phân. |
| Q10 | **B** | float represents fractional numerical values. | float lưu số có phần thập phân. |
| Q11 | **C** | An identifier is text, not a quantity to calculate. | Mã định danh là chuỗi, không phải lượng để tính toán. |
| Q12 | **D** | bool represents True or False. | bool biểu diễn True hoặc False. |
| Q13 | **A** | Assignment associates the name x with the number 5. | Phép gán liên kết tên x với số 5. |
| Q14 | **B** | input returns text even when it looks numeric. | input trả về văn bản kể cả khi người dùng gõ chữ số. |
| Q15 | **C** | float converts valid numeric text to a floating-point value. | float chuyển chuỗi số hợp lệ thành số thực. |
| Q16 | **D** | Letters abc are not a valid integer literal. | abc không phải biểu diễn số nguyên hợp lệ. |
| Q17 | **A** | print separates multiple arguments with a space by default. | print mặc định đặt một dấu cách giữa các đối số. |
| Q18 | **B** | The later assignment replaces the earlier binding. | Phép gán sau thay giá trị được gán trước đó. |
| Q19 | **C** | The decimal point makes 2.0 a floating-point literal. | Dấu thập phân khiến 2.0 là số thực. |
| Q20 | **D** | Quotation marks mark a string literal and are not printed. | Dấu nháy là cú pháp chuỗi, không được in ra. |

## 8. Nối sang bài kế tiếp

`Chương trình → Biến → Kiểu dữ liệu → Điều kiện`.

# PY-01 — Biến, đầu vào và đầu ra trong Python


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Variable** — biến; **Input** — đầu vào.

`Chương trình → Biến → Kiểu dữ liệu → Điều kiện`

**Học xong dùng để làm gì?** Nhận tên, tuổi hoặc số lượng từ người dùng, lưu vào biến và in ra kết quả có thể kiểm tra.

**Kết nối kiến thức tiếp theo:** Sang PY-02, dùng kiểu số và chuỗi để dữ liệu trong biến được tính toán đúng thay vì chỉ hiển thị.

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

B. Information produced by a program — Thông tin do chương trình tạo ra

C. Data received for processing — Dữ liệu được nhận để xử lý

D. How a value is represented and used — Cách biểu diễn và sử dụng một giá trị

**Đáp án: A**

**Giải thích:** Biến Python là tên được liên kết với đối tượng, chẳng hạn `age = 20`. Biến khác dữ liệu đầu vào hay kết quả in ra; dùng `age` sau đó sẽ truy cập giá trị đang được gán.


**Q2. What is program input? — Đầu vào chương trình là gì?**

A. Information produced by a program — Thông tin do chương trình tạo ra

B. How a value is represented and used — Cách biểu diễn và sử dụng một giá trị

C. A name referring to a value — Tên tham chiếu đến một giá trị

D. Data received for processing — Dữ liệu được nhận để xử lý

**Đáp án: D**

**Giải thích:** Đầu vào là dữ liệu chương trình nhận, ví dụ văn bản người dùng nhập cho `input()`. Chương trình có thể xử lý văn bản rồi tạo đầu ra; đầu vào không phải kết quả chương trình.


**Q3. What is program output? — Đầu ra chương trình là gì?**

A. How a value is represented and used — Cách biểu diễn và sử dụng một giá trị

B. Information produced by a program — Thông tin do chương trình tạo ra

C. Data received for processing — Dữ liệu được nhận để xử lý

D. A name referring to a value — Tên tham chiếu đến một giá trị

**Đáp án: B**

**Giải thích:** Đầu ra là thông tin chương trình đưa ra ngoài, ví dụ dòng chữ do `print(5)` hiển thị. Nó khác đầu vào do người dùng cung cấp và khác biến dùng để tham chiếu giá trị trong chương trình.


**Q4. What does a data type describe? — Kiểu dữ liệu mô tả điều gì?**

A. Information produced by a program — Thông tin do chương trình tạo ra

B. How a value is represented and used — Cách biểu diễn và sử dụng một giá trị

C. A name referring to a value — Tên tham chiếu đến một giá trị

D. Data received for processing — Dữ liệu được nhận để xử lý

**Đáp án: B**

**Giải thích:** Kiểu dữ liệu quyết định ý nghĩa giá trị và các phép toán phù hợp: `3` thuộc kiểu `int`, còn `'3'` thuộc `str`. Vì vậy `3 + 2` là phép cộng số, còn `'3' + '2'` nối văn bản.


**Q5. Which function prints a value? — Hàm nào in một giá trị?**

A. `int()` — `int()`

B. `type()` — `type()`

C. `input()` — `input()`

D. `print()` — `print()`

**Đáp án: D**

**Giải thích:** `print()` ghi biểu diễn của giá trị ra đầu ra chuẩn; chẳng hạn `print(5)` hiển thị `5`. Hàm này không nhận câu trả lời người dùng như `input()`.


**Q6. Which function reads keyboard input? — Hàm nào đọc dữ liệu bàn phím?**

A. `input()` — `input()`

B. `int()` — `int()`

C. `type()` — `type()`

D. `print()` — `print()`

**Đáp án: A**

**Giải thích:** `input()` nhận một dòng người dùng gõ và trả về văn bản không kèm ký tự xuống dòng cuối. Dù người dùng gõ `12`, kết quả vẫn là chuỗi `'12'`, không tự đổi thành số nguyên `12`.


**Q7. Which function finds a value's type? — Hàm nào kiểm tra kiểu giá trị?**

A. `input()` — `input()`

B. `print()` — `print()`

C. `type()` — `type()`

D. `int()` — `int()`

**Đáp án: C**

**Giải thích:** `type(value)` trả về lớp/kiểu của đối tượng: `type(3)` là `int` còn `type('3')` là `str`. Hàm kiểm tra kiểu chứ không chuyển đổi giá trị.


**Q8. Which function converts valid decimal digits to an integer? — Hàm nào đổi chuỗi chữ số hợp lệ thành số nguyên?**

A. `int()` — `int()`

B. `print()` — `print()`

C. `type()` — `type()`

D. `input()` — `input()`

**Đáp án: A**

**Giải thích:** `int()` phân tích chuỗi biểu diễn số nguyên hợp lệ nên `int('012')` cho số nguyên `12`; số 0 đầu không được giữ lại. Chuỗi `'12.5'` không phải chuỗi số nguyên thập phân hợp lệ và gây `ValueError`.


**Q9. Which type represents a count of whole items? — Kiểu nào biểu diễn số lượng món nguyên?**

A. `str` — `str`

B. `float` — `float`

C. `int` — `int`

D. `bool` — `bool`

**Đáp án: C**

**Giải thích:** `int` biểu diễn số lượng nguyên như 4 vé hoặc 0 lỗi, không có phần lẻ. `float` phù hợp số đo có thể có phần thập phân, không cần thiết cho số đếm các đơn vị nguyên vẹn.


**Q10. Which type suits a measurement with fractions? — Kiểu nào phù hợp với số đo có phần lẻ?**

A. `int` — `int`

B. `float` — `float`

C. `bool` — `bool`

D. `str` — `str`

**Đáp án: B**

**Giải thích:** `float` biểu diễn giá trị số có thể chứa phần lẻ, ví dụ 2,5 mét. Khác số đếm nguyên, số đo có thể nằm giữa hai số nguyên; số thập phân dạng dấu phẩy động đôi khi chỉ là xấp xỉ.


**Q11. Which type preserves a leading zero in an identifier? — Kiểu nào giữ số 0 đầu mã định danh?**

A. `str` — `str`

B. `bool` — `bool`

C. `float` — `float`

D. `int` — `int`

**Đáp án: A**

**Giải thích:** Mã định danh như `'007'` nên lưu bằng `str` vì mọi ký tự, kể cả hai số 0 đầu, đều có ý nghĩa. Đổi sang `int` được `7` và làm mất định dạng mã.


**Q12. Which type stores a true/false state? — Kiểu nào lưu trạng thái đúng/sai?**

A. `bool` — `bool`

B. `int` — `int`

C. `str` — `str`

D. `float` — `float`

**Đáp án: A**

**Giải thích:** `bool` có hai giá trị logic `True` và `False`, thích hợp biểu diễn trạng thái như có được phép truy cập hay không. Đây không phải kiểu đo lường số hay nhãn văn bản.


**Q13. What does `x = 5` do? — `x = 5` thực hiện điều gì?**

A. Tests whether `x` equals `5` — Kiểm tra `x` có bằng `5` không

B. Adds `5` to the old value of `x` — Cộng `5` vào giá trị cũ của `x`

C. Displays `5` without storing it — Hiển thị `5` mà không gán

D. Assigns the integer `5` to `x` — Gán số nguyên `5` cho `x`

**Đáp án: D**

**Giải thích:** Dấu bằng đơn gán tên `x` cho số nguyên `5`, không kiểm tra bằng nhau và cũng không cộng thêm số. Muốn so sánh `x` có bằng `5` thì dùng `x == 5`.


**Q14. What is the type of `input()`'s return value? — Giá trị trả về của `input()` có kiểu nào?**

A. An integer when only digits are typed — Số nguyên nếu chỉ nhập chữ số

B. A floating-point number by default — Số thực theo mặc định

C. A Boolean indicating whether input exists — Boolean cho biết có đầu vào hay không

D. A string, even if it contains digits — Chuỗi, kể cả khi chỉ chứa chữ số

**Đáp án: D**

**Giải thích:** `input()` luôn trả về `str` chứa nội dung được nhập, ví dụ `'42'`. Nếu cần tính toán số, hãy dùng `int(input())` hoặc phép đổi kiểu phù hợp khi đầu vào hợp lệ.


**Q15. What does `float('2.5')` produce? — `float('2.5')` tạo ra gì?**

A. The string `'2.5'` — Chuỗi `'2.5'`

B. The integer `2` — Số nguyên `2`

C. The floating-point number `2.5` — Số thực `2.5`

D. `ValueError` for any decimal point — `ValueError` nếu có dấu thập phân

**Đáp án: C**

**Giải thích:** `float('2.5')` chuyển văn bản `'2.5'` thành giá trị số thực `2.5`. Kết quả không còn là chuỗi có dấu nháy và không cắt phần lẻ thành số nguyên `2`.


**Q16. What does `int('abc')` raise? — `int('abc')` phát sinh gì?**

A. `TypeError` — `TypeError`

B. `ValueError` — `ValueError`

C. The integer `0` — Số nguyên `0`

D. `NameError` — `NameError`

**Đáp án: B**

**Giải thích:** `int('abc')` phát sinh `ValueError` vì các chữ cái không tạo thành số nguyên hệ mười hợp lệ. Hàm vẫn tồn tại và nhận được chuỗi, nên đây là lỗi giá trị chuyển đổi chứ không phải `NameError`.


**Q17. What does `print(2, 3)` display by default? — `print(2, 3)` mặc định hiển thị gì?**

A. `2,3` — `2,3`

B. `2 3` — `2 3`

C. `(2, 3)` — `(2, 3)`

D. `23` — `23`

**Đáp án: B**

**Giải thích:** Mặc định `print` ngăn cách các đối số bằng một dấu cách: `print(2, 3)` hiển thị `2 3`. Nó không dính hai số thành `23` và không in dạng tuple `(2, 3)`.


**Q18. If `x = 2` is followed by `x = 4` on the next line, what is the final value of `x`? — Nếu `x = 2` rồi `x = 4` ở dòng tiếp theo, giá trị cuối của `x` là gì?**

A. `ValueError` — `ValueError`

B. `2` — `2`

C. `4` — `4`

D. `6` — `6`

**Đáp án: C**

**Giải thích:** Lệnh đầu gán `x` bằng `2`, lệnh tiếp theo gán lại chính tên đó bằng `4`. Vì vậy giá trị cuối là `4`, không phải tổng `6` hay giá trị cũ `2`.


**Q19. Which Python type does `type(2.0)` identify? — `type(2.0)` xác định kiểu Python nào?**

A. `int` — `int`

B. `bool` — `bool`

C. `float` — `float`

D. `str` — `str`

**Đáp án: C**

**Giải thích:** Literal `2.0` là đối tượng số thực, nên `type(2.0)` xác định kiểu `float` (hiển thị `<class 'float'>`). Trong khi đó `type(2)` là `int`; dấu thập phân làm thay đổi kiểu literal.


**Q20. What does `print('Hi')` display? — `print('Hi')` hiển thị gì?**

A. `hi` — `hi`

B. `None` — `None`

C. `'Hi'` including the quotes — `'Hi'` gồm cả dấu nháy

D. `Hi` without quotes — `Hi` không có dấu nháy

**Đáp án: D**

**Giải thích:** Dấu nháy dùng để bao chuỗi trong mã nguồn chứ không phải ký tự thuộc nội dung chuỗi. Vì vậy `print('Hi')` hiển thị `Hi` rồi xuống dòng, không in dấu nháy hoặc chữ thường `hi`.

## 8. Nối sang bài kế tiếp

`Chương trình → Biến → Kiểu dữ liệu → Điều kiện`.

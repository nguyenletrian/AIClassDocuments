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

### 4.1. Variable

**Từ vựng trong mục:** **Variable** — biến.

Biến là tên ta đặt cho một giá trị để dùng lại. Ví dụ, `total = 12` lưu số 12 vào biến `total`; `print(total)` in ra 12.

```python
total = 12
print(total)
```


### 4.2. Input

**Từ vựng trong mục:** **Input** — đầu vào.

Đầu vào là thông tin chương trình nhận được, chẳng hạn tên khách do người dùng nhập. `input()` nhận chữ gõ từ bàn phím. Ví dụ dưới đây gán sẵn tên `An` để minh họa cách lưu và dùng thông tin.

```python
name = 'An'
print(name)
```


### 4.3. Output

**Từ vựng trong mục:** **Output** — đầu ra.

Kết quả là thông tin chương trình tạo ra. `print('Xin chào')` hiển thị chữ `Xin chào` trên màn hình.

```python
print('Xin chào')
```


### 4.4. Type

**Từ vựng trong mục:** **Type** — kiểu dữ liệu.

Kiểu dữ liệu cho Python biết một giá trị là chữ hay số. `str` là chuỗi, `int` là số nguyên, còn `float` là số có phần thập phân. `type(2.5)` cho biết `2.5` là số thực.

```python
print(type(2.5))
```


## 5. Năm tình huống lập trình thực tế

### Tình huống 1 — Chào khách mới

**Từ vựng trong mục:** **Variable** — biến.

**Vấn đề thực tế:** Một cửa hàng muốn gửi lời chào có tên khách. Khách mới tên Lan.

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

**Kết quả:** `Xin chào Lan!` — lời chào chứa đúng tên khách.

### Tình huống 2 — Tính tiền hóa đơn

**Từ vựng trong mục:** **Input** — đầu vào.

**Vấn đề thực tế:** Một cửa hàng bán 3 sản phẩm, mỗi sản phẩm giá 120.000 đồng. Phần mềm đang lưu giá và số lượng dưới dạng chữ `"120000"` và `"3"`.

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

**Kết quả:** `360000` — khách phải trả 360.000 đồng.

### Tình huống 3 — Hiển thị điểm

**Từ vựng trong mục:** **Output** — đầu ra.

**Vấn đề thực tế:** Trung tâm đào tạo muốn hiển thị điểm của học viên An, đạt 8,5 điểm trên thang 10.

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

**Kết quả:** `An: 8.5/10` — dòng thông tin gồm tên và điểm học viên.

### Tình huống 4 — Ghi nhiệt độ

**Từ vựng trong mục:** **Type** — kiểu dữ liệu.

**Vấn đề thực tế:** Một cảm biến báo nhiệt độ 36,5 °C. Nhân viên cần biết số đo được lưu bằng kiểu dữ liệu gì.

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

**Kết quả:** `<class 'float'> 36.5` — kiểu số thực và giá trị 36,5; code chưa in đơn vị °C.

### Tình huống 5 — Giữ mã đơn

**Từ vựng trong mục:** **Variable** — biến.

**Vấn đề thực tế:** Một cửa hàng dùng mã đơn bốn chữ số, trong đó hai số `0` đầu tiên phải được giữ lại. Mã đơn hiện tại là `0007`.

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

**Kết quả:** `0007` — mã được in nguyên vẹn; `assert` không in thêm khi kiểm tra đúng.

## 6. Những nhầm lẫn thường gặp

- `input()` nhận chữ; cần đổi sang `int()` hoặc `float()` khi muốn tính toán với số. Chuỗi không hợp lệ có thể gây `ValueError`.
- Mã đơn `0007` phải lưu dạng chuỗi nếu cần giữ hai số `0` ở đầu.
- `print()` in kết quả, còn `type()` xem kiểu dữ liệu; hai hàm có nhiệm vụ khác nhau.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is Variable? — Thuật ngữ Variable có nghĩa gì?**

A. Data given to a program — Thông tin đưa vào chương trình

B. A named reference to a value — Tên dùng để tham chiếu một giá trị

C. Result produced by a program — Thông tin chương trình tạo ra

D. Category of a value — Nhóm giá trị như str, int, float


**Q2. What is Input? — Thuật ngữ Input có nghĩa gì?**

A. Data given to a program — Thông tin đưa vào chương trình

B. Result produced by a program — Thông tin chương trình tạo ra

C. Category of a value — Nhóm giá trị như str, int, float

D. A named reference to a value — Tên dùng để tham chiếu một giá trị


**Q3. What is Output? — Thuật ngữ Output có nghĩa gì?**

A. Category of a value — Nhóm giá trị như str, int, float

B. A named reference to a value — Tên dùng để tham chiếu một giá trị

C. Data given to a program — Thông tin đưa vào chương trình

D. Result produced by a program — Thông tin chương trình tạo ra


**Q4. What is Type? — Thuật ngữ Type có nghĩa gì?**

A. A named reference to a value — Tên dùng để tham chiếu một giá trị

B. Data given to a program — Thông tin đưa vào chương trình

C. Category of a value — Nhóm giá trị như str, int, float

D. Result produced by a program — Thông tin chương trình tạo ra


**Q5. Which use matches print()? — Công dụng nào đúng với print()?**

A. It always creates perfect predictions — Nó luôn dự đoán đúng tuyệt đối

B. This Python operation supports the described task — Hiển thị kết quả, nhận nhiều giá trị phân cách bằng dấu phẩy

C. It automatically trains a neural network — Nó tự huấn luyện mạng nơ-ron

D. It removes the need for input checks — Nó loại bỏ nhu cầu kiểm tra đầu vào


**Q6. Which use matches input()? — Công dụng nào đúng với input()?**

A. This Python operation supports the described task — Nhận văn bản từ bàn phím; kết quả luôn là chuỗi

B. It always creates perfect predictions — Nó luôn dự đoán đúng tuyệt đối

C. It automatically trains a neural network — Nó tự huấn luyện mạng nơ-ron

D. It removes the need for input checks — Nó loại bỏ nhu cầu kiểm tra đầu vào


**Q7. Which use matches int()/float()? — Công dụng nào đúng với int()/float()?**

A. It always creates perfect predictions — Nó luôn dự đoán đúng tuyệt đối

B. It automatically trains a neural network — Nó tự huấn luyện mạng nơ-ron

C. It removes the need for input checks — Nó loại bỏ nhu cầu kiểm tra đầu vào

D. This Python operation supports the described task — Đổi chuỗi hợp lệ sang số trước khi tính toán


**Q8. Which use matches type()? — Công dụng nào đúng với type()?**

A. It always creates perfect predictions — Nó luôn dự đoán đúng tuyệt đối

B. It automatically trains a neural network — Nó tự huấn luyện mạng nơ-ron

C. This Python operation supports the described task — Kiểm tra kiểu dữ liệu khi chưa rõ đầu vào

D. It removes the need for input checks — Nó loại bỏ nhu cầu kiểm tra đầu vào


**Q9. Which reason fits 'Customer greeting'? — Lý do nào phù hợp với 'Chào khách mới'?**

A. Convert numeric text before multiplying — Đổi số từ văn bản thành số trước khi nhân

B. Store a name once for reuse — Lưu tên trong biến để dùng lại trong nhiều thông báo

C. Format a name and score — Format tên và điểm để xuất ra một dòng dễ đọc

D. Store a decimal reading — Giữ kiểu số thực để không mất phần thập phân


**Q10. Which reason fits 'Invoice total'? — Lý do nào phù hợp với 'Tính tiền hóa đơn'?**

A. Convert numeric text before multiplying — Đổi số từ văn bản thành số trước khi nhân

B. Format a name and score — Format tên và điểm để xuất ra một dòng dễ đọc

C. Store a decimal reading — Giữ kiểu số thực để không mất phần thập phân

D. Keep an ID as text — Mã đơn không phải đại lượng nên giữ dạng chuỗi


**Q11. Which reason fits 'Score report'? — Lý do nào phù hợp với 'Hiển thị điểm'?**

A. Store a decimal reading — Giữ kiểu số thực để không mất phần thập phân

B. Keep an ID as text — Mã đơn không phải đại lượng nên giữ dạng chuỗi

C. Store a name once for reuse — Lưu tên trong biến để dùng lại trong nhiều thông báo

D. Format a name and score — Format tên và điểm để xuất ra một dòng dễ đọc


**Q12. Which reason fits 'Sensor reading'? — Lý do nào phù hợp với 'Ghi nhiệt độ'?**

A. Keep an ID as text — Mã đơn không phải đại lượng nên giữ dạng chuỗi

B. Store a name once for reuse — Lưu tên trong biến để dùng lại trong nhiều thông báo

C. Store a decimal reading — Giữ kiểu số thực để không mất phần thập phân

D. Convert numeric text before multiplying — Đổi số từ văn bản thành số trước khi nhân


**Q13. Which reason fits 'Preserve order ID'? — Lý do nào phù hợp với 'Giữ mã đơn'?**

A. Store a name once for reuse — Lưu tên trong biến để dùng lại trong nhiều thông báo

B. Keep an ID as text — Mã đơn không phải đại lượng nên giữ dạng chuỗi

C. Convert numeric text before multiplying — Đổi số từ văn bản thành số trước khi nhân

D. Format a name and score — Format tên và điểm để xuất ra một dòng dễ đọc


**Q14. Which input fits 'Customer greeting'? — Dữ liệu nào được dùng cho 'Chào khách mới'?**

A. The sample described for Customer greeting — Một chuỗi là tên khách

B. Input from Invoice total — Giá 120000 đồng, số lượng 3

C. Input from Score report — Tên An, điểm 8.5/10

D. Input from Sensor reading — Nhiệt độ 36.5 độ C


**Q15. Which input fits 'Invoice total'? — Dữ liệu nào được dùng cho 'Tính tiền hóa đơn'?**

A. Input from Score report — Tên An, điểm 8.5/10

B. Input from Sensor reading — Nhiệt độ 36.5 độ C

C. Input from Preserve order ID — Mã 0007

D. The sample described for Invoice total — Giá 120000 đồng, số lượng 3


**Q16. Which input fits 'Score report'? — Dữ liệu nào được dùng cho 'Hiển thị điểm'?**

A. Input from Sensor reading — Nhiệt độ 36.5 độ C

B. Input from Preserve order ID — Mã 0007

C. The sample described for Score report — Tên An, điểm 8.5/10

D. Input from Customer greeting — Một chuỗi là tên khách


**Q17. Which input fits 'Sensor reading'? — Dữ liệu nào được dùng cho 'Ghi nhiệt độ'?**

A. Input from Preserve order ID — Mã 0007

B. The sample described for Sensor reading — Nhiệt độ 36.5 độ C

C. Input from Customer greeting — Một chuỗi là tên khách

D. Input from Invoice total — Giá 120000 đồng, số lượng 3


**Q18. Which input fits 'Preserve order ID'? — Dữ liệu nào được dùng cho 'Giữ mã đơn'?**

A. The sample described for Preserve order ID — Mã 0007

B. Input from Customer greeting — Một chuỗi là tên khách

C. Input from Invoice total — Giá 120000 đồng, số lượng 3

D. Input from Score report — Tên An, điểm 8.5/10


**Q19. What must be checked before processing input? — Cần xác định gì trước xử lý?**

A. Only text size — Chỉ kích thước chữ

B. Only the file name length — Chỉ độ dài tên file

C. Only program comments — Chỉ phần comment

D. Input meaning, type and units — Ý nghĩa, kiểu và đơn vị đầu vào


**Q20. What should follow a successful example? — Sau khi ví dụ chạy đúng nên làm gì?**

A. Assume all datasets work identically — Cho rằng mọi bộ dữ liệu giống nhau

B. Delete all tests — Xóa toàn bộ kiểm thử

C. Validate output and edge cases — Kiểm tra kết quả và trường hợp biên

D. Ignore input errors — Bỏ qua lỗi nhập liệu

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **B** | A named reference to a value | Tên dùng để tham chiếu một giá trị |
| Q2 | **A** | Data given to a program | Thông tin đưa vào chương trình |
| Q3 | **D** | Result produced by a program | Thông tin chương trình tạo ra |
| Q4 | **C** | Category of a value | Nhóm giá trị như str, int, float |
| Q5 | **B** | This Python operation supports the described task | Hiển thị kết quả, nhận nhiều giá trị phân cách bằng dấu phẩy |
| Q6 | **A** | This Python operation supports the described task | Nhận văn bản từ bàn phím; kết quả luôn là chuỗi |
| Q7 | **D** | This Python operation supports the described task | Đổi chuỗi hợp lệ sang số trước khi tính toán |
| Q8 | **C** | This Python operation supports the described task | Kiểm tra kiểu dữ liệu khi chưa rõ đầu vào |
| Q9 | **B** | Store a name once for reuse | Lưu tên trong biến để dùng lại trong nhiều thông báo |
| Q10 | **A** | Convert numeric text before multiplying | Đổi số từ văn bản thành số trước khi nhân |
| Q11 | **D** | Format a name and score | Format tên và điểm để xuất ra một dòng dễ đọc |
| Q12 | **C** | Store a decimal reading | Giữ kiểu số thực để không mất phần thập phân |
| Q13 | **B** | Keep an ID as text | Mã đơn không phải đại lượng nên giữ dạng chuỗi |
| Q14 | **A** | The sample described for Customer greeting | Một chuỗi là tên khách |
| Q15 | **D** | The sample described for Invoice total | Giá 120000 đồng, số lượng 3 |
| Q16 | **C** | The sample described for Score report | Tên An, điểm 8.5/10 |
| Q17 | **B** | The sample described for Sensor reading | Nhiệt độ 36.5 độ C |
| Q18 | **A** | The sample described for Preserve order ID | Mã 0007 |
| Q19 | **D** | Input meaning, type and units | Ý nghĩa, kiểu và đơn vị đầu vào |
| Q20 | **C** | Validate output and edge cases | Kiểm tra kết quả và trường hợp biên |

## 8. Nối sang bài kế tiếp

`Chương trình → Biến → Kiểu dữ liệu → Điều kiện`.

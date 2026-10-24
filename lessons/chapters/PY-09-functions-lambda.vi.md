# PY-09 — Hàm, return, lambda và phạm vi biến


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Function** — hàm; **Parameter** — tham số.

`Vòng lặp → Hàm → OOP → Pipeline`

Sau khi biết xử lý dữ liệu bằng vòng lặp và danh sách, ta tạo hàm để dùng lại cùng một công việc mà không phải viết code nhiều lần.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Ý nghĩa |
|---|---|---|
| Function | hàm | Khối code tái sử dụng và nhận tham số |
| Parameter | tham số | Tên đầu vào dùng trong định nghĩa hàm |
| Return | trả về | Kết quả gửi từ hàm về nơi gọi |
| Lambda | hàm ẩn danh | Biểu thức hàm ngắn không cần đặt tên |

## 3. Thư viện, hàm và tham số

**Từ vựng trong mục:** **Function** — hàm; **Parameter** — tham số.

| Hàm/cú pháp | Giải thích và lý do dùng |
|---|---|
| `def func(...):` | Định nghĩa một hàm, sử dụng return để trả kết quả |
| `default / keyword arguments` | Dùng tham số mặc định hoặc gọi theo tên cho dễ đọc |
| `lambda x: expr` | Dùng biểu thức ngắn khi hàm không cần nhiều câu lệnh |
| `sorted(..., key=...)` | Chọn tiêu chí để sắp xếp bản ghi |


## 4. Khái niệm liên quan

### 4.1. Function

**Từ vựng trong mục:** **Function** — hàm.

Hàm là một nhóm lệnh có tên, có thể gọi nhiều lần. `twice(x)` nhân giá trị truyền vào với 2; `twice(3)` trả về `6`.

```python
def twice(x): return x*2
print(twice(3))
```

**Kết quả khi chạy:**

```text
6
```

### 4.2. Parameter

**Từ vựng trong mục:** **Parameter** — tham số.

Tham số là tên biến khai báo trong hàm, như `name` của `hello(name)`. Khi gọi `hello('Lan')`, chuỗi `'Lan'` được truyền vào và in ra `Lan`.

```python
def hello(name): return name
print(hello('Lan'))
```

**Kết quả khi chạy:**

```text
Lan
```

### 4.3. Return

**Từ vựng trong mục:** **Return** — trả về.

`return` gửi kết quả về nơi gọi hàm; khác với `print()` chỉ hiển thị ra màn hình. `add(2, 3)` trả về `5`, rồi `print()` hiển thị số đó.

```python
def add(a,b): return a+b
print(add(2,3))
```

**Kết quả khi chạy:**

```text
5
```

### 4.4. Lambda

**Từ vựng trong mục:** **Lambda** — hàm ẩn danh.

`lambda` tạo hàm ngắn chỉ có một biểu thức, phù hợp cho thao tác đơn giản như chọn khóa sắp xếp. `(lambda x: x+1)(5)` cho kết quả `6`.

```python
print((lambda x: x+1)(5))
```

**Kết quả khi chạy:**

```text
6
```

## 5. Năm tình huống lập trình thực tế

### Tình huống 1 — Tính thuế giá trị gia tăng

**Từ vựng trong mục:** **Function** — hàm.

**Tình huống thực tế:** Một cửa hàng bán sản phẩm giá 100.000 đồng chưa có thuế. Để minh họa cách tính, cửa hàng dùng mức VAT giả định 10% cho sản phẩm này.

**Yêu cầu:** Viết hàm tính giá sau thuế và in số tiền cần thanh toán.

**Vì sao chọn cách giải này?** Hàm `with_vat` nhận giá và mức thuế, với `rate=0.10` là mức mặc định. `return` trả tổng tiền đã làm tròn.

**Quy trình giải:**

1. Định nghĩa hàm với tham số giá và thuế mặc định.
2. Nhân giá với `1 + rate`.
3. Gọi hàm bằng giá 100.000 và in kết quả.

```python
def with_vat(price, rate=0.10):
    return round(price*(1+rate))
print(with_vat(100000))
```

**Kết quả khi chạy:**

```text
110000
```

**Kết quả:** `110000` đồng — giá 100.000 đồng cộng 10% thuế.

### Tình huống 2 — Sắp điểm theo thứ hạng

**Từ vựng trong mục:** **Parameter** — tham số.

**Tình huống thực tế:** Trung tâm có hai hồ sơ học viên: A đạt 8 điểm và B đạt 10 điểm trên thang 10. Cần ưu tiên hiển thị người có điểm cao hơn.

**Yêu cầu:** In danh sách hồ sơ theo điểm giảm dần.

**Vì sao chọn cách giải này?** `sorted()` tạo danh sách đã sắp xếp; `lambda r: r['score']` cho biết phải dùng trường điểm để so sánh.

**Quy trình giải:**

1. Tạo hai Dictionary học viên.
2. Dùng `sorted` với `key` lấy điểm và `reverse=True`.
3. In danh sách sau khi sắp xếp.

```python
people=[{"name":"A","score":8},{"name":"B","score":10}]
print(sorted(people,key=lambda r:r["score"],reverse=True))
```

**Kết quả khi chạy:**

```text
[{'name': 'B', 'score': 10}, {'name': 'A', 'score': 8}]
```

**Kết quả:** `[{'name': 'B', 'score': 10}, {'name': 'A', 'score': 8}]` — B đứng trước A.

### Tình huống 3 — Kiểm tra điểm hợp lệ

**Từ vựng trong mục:** **Return** — trả về.

**Tình huống thực tế:** Một trung tâm chỉ chấp nhận điểm kiểm tra từ 0 đến 10. Nhân viên cần kiểm tra điểm nhập vào là 11.

**Yêu cầu:** Viết hàm trả về `True` khi điểm nằm trong khoảng hợp lệ, ngược lại trả về `False`.

**Vì sao chọn cách giải này?** Hàm `valid_score()` kết hợp hai phép so sánh trong một biểu thức, nên có thể gọi lại cho nhiều học viên.

**Quy trình giải:**

1. Định nghĩa hàm nhận điểm `x`.
2. Kiểm tra `0 <= x <= 10`.
3. Truyền điểm 11 vào hàm và in kết quả.

```python
def valid_score(x): return 0<=x<=10
print(valid_score(11))
```

**Kết quả khi chạy:**

```text
False
```

**Kết quả:** `False` — điểm 11 vượt quá thang điểm 10.

### Tình huống 4 — Trả thống kê đơn giản

**Từ vựng trong mục:** **Lambda** — hàm ẩn danh.

**Tình huống thực tế:** Một cửa hàng ghi số lượng sản phẩm bán được trong ba ngày lần lượt là 7, 8 và 9 món.

**Yêu cầu:** Viết hàm trả về cả tổng số món lẫn số món trung bình mỗi ngày.

**Vì sao chọn cách giải này?** `return` có thể gửi về hai kết quả trong một tuple, sau đó dùng hai biến để nhận tổng và trung bình.

**Quy trình giải:**

1. Truyền list `[7, 8, 9]` vào hàm.
2. Dùng `sum()` tính tổng và chia cho số ngày để tính trung bình.
3. Nhận hai kết quả và in ra.

```python
def summary(values):
    return sum(values), sum(values)/len(values)
total,average=summary([7,8,9])
print(total,average)
```

**Kết quả khi chạy:**

```text
24 8.0
```

**Kết quả:** `24 8.0` — bán tổng cộng 24 món, trung bình 8 món/ngày.

### Tình huống 5 — Lọc yêu cầu ưu tiên

**Từ vựng trong mục:** **Function** — hàm.

**Tình huống thực tế:** Bộ phận vận hành có bốn yêu cầu với điểm ưu tiên `[1, 5, 2, 4]`. Chỉ các yêu cầu có điểm từ 4 trở lên cần được xử lý trước.

**Yêu cầu:** In danh sách các điểm ưu tiên đạt ngưỡng.

**Vì sao chọn cách giải này?** `filter()` áp dụng điều kiện do `lambda` định nghĩa cho từng điểm; `list()` chuyển các kết quả được giữ lại thành danh sách.

**Quy trình giải:**

1. Lưu bốn điểm ưu tiên.
2. Lọc từng điểm bằng điều kiện `x >= 4`.
3. Chuyển kết quả lọc thành list rồi in ra.

```python
priorities=[1,5,2,4]
print(list(filter(lambda x:x>=4,priorities)))
```

**Kết quả khi chạy:**

```text
[5, 4]
```

**Kết quả:** `[5, 4]` — chỉ hai yêu cầu đạt ngưỡng ưu tiên.

## 6. Sai lầm thường gặp

- `return` trả giá trị về chỗ gọi hàm; nếu muốn thấy giá trị trên màn hình thì gọi `print()`.
- Tham số mặc định như `rate=0.10` được dùng khi không truyền giá trị khác vào.
- `lambda` phù hợp biểu thức ngắn, còn xử lý nhiều bước nên dùng `def` cho dễ đọc.
- Hàm tính trung bình cần xử lý danh sách rỗng trước khi chia cho `len(values)`.
- Khi sắp xếp bản ghi, phải chọn đúng trường dữ liệu trong `key`.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is a function? — Hàm là gì?**

A. A reusable block of code — Khối code có thể gọi nhiều lần

B. A CSV file — Một file CSV

C. A loop counter — Biến đếm vòng lặp

D. A folder name — Tên thư mục

**Q2. What is a parameter? — Tham số là gì?**

A. A value returned by print — Giá trị print trả về

B. A name used in a function definition — Tên biến trong phần định nghĩa hàm

C. A list index — Chỉ số list

D. A syntax error — Lỗi cú pháp

**Q3. What does return do? — return làm gì?**

A. End the program always — Luôn kết thúc chương trình

B. Display text only — Chỉ hiển thị chữ

C. Send a value back to the caller — Trả giá trị về nơi gọi

D. Sort the list — Sắp xếp list

**Q4. What is lambda? — lambda là gì?**

A. A short anonymous function — Hàm ngắn không cần tên

B. A file format — Định dạng file

C. A Boolean only — Chỉ giá trị Boolean

D. A type of loop — Một loại vòng lặp

**Q5. What does def do? — def làm gì?**

A. It defines a function — Nó định nghĩa hàm

B. It deletes a file — Nó xóa file

C. It opens a browser — Nó mở trình duyệt

D. It creates a set — Nó tạo set

**Q6. What does a default parameter do? — Tham số mặc định dùng để làm gì?**

A. It provides a default argument value — Nó cung cấp giá trị tham số mặc định

B. It changes a string to uppercase — Nó đổi chữ hoa

C. It disables return — Nó vô hiệu return

D. It forces every argument to be a list — Nó bắt buộc tham số là list

**Q7. When is lambda suitable? — Khi nào lambda phù hợp?**

A. A short function expression — Biểu thức hàm ngắn

B. A class definition — Định nghĩa lớp

C. A while loop — Vòng while

D. A dictionary literal — Dictionary

**Q8. What does the key argument of sorted do? — Tham số key của sorted dùng làm gì?**

A. It chooses a sorting criterion — Nó chọn tiêu chí sắp xếp

B. It removes duplicates only — Nó chỉ bỏ trùng

C. It prints without sorting — Nó in mà không sắp xếp

D. It closes a file — Nó đóng file

**Q9. Why define a VAT function? — Vì sao tạo hàm tính thuế?**

A. Reuse the same tax calculation — Dùng lại phép tính thuế

B. Never pay tax — Không bao giờ tính thuế

C. Change the input randomly — Đổi đầu vào ngẫu nhiên

D. Delete prices — Xóa giá

**Q10. Why use a score-based lambda in sorted? — Vì sao dùng lambda theo điểm khi sắp xếp?**

A. Sort by each person's score — Sắp theo điểm mỗi người

B. Sort alphabetically only — Chỉ sắp theo chữ

C. Add all scores — Cộng mọi điểm

D. Filter missing records — Lọc hồ sơ thiếu

**Q11. Why define valid_score()? — Vì sao tạo valid_score()?**

A. Reuse the score validation rule — Dùng lại quy tắc kiểm tra điểm

B. Skip all checks — Bỏ mọi kiểm tra

C. Always return True — Luôn trả True

D. Convert scores to names — Đổi điểm thành tên

**Q12. Why return two summary values? — Vì sao trả hai giá trị thống kê?**

A. Return sum and average together — Trả tổng và trung bình cùng lúc

B. Return a password — Trả mật khẩu

C. Delete input values — Xóa dữ liệu đầu vào

D. Only sort values — Chỉ sắp xếp

**Q13. Why filter priorities? — Vì sao lọc điểm ưu tiên?**

A. Keep priorities of at least four — Giữ điểm ưu tiên từ bốn trở lên

B. Keep all priorities — Giữ mọi điểm

C. Reverse the values — Đảo giá trị

D. Remove every item — Xóa mọi phần tử

**Q14. What input is used for the VAT example? — Ví dụ thuế dùng dữ liệu nào?**

A. A price of 100000 VND with 10% VAT — Giá 100000 đồng thuế 10%

B. A score of 11 — Điểm 11

C. Three daily quantities — Ba số lượng theo ngày

D. Four priorities — Bốn mức ưu tiên

**Q15. What input is used for sorting learners? — Ví dụ xếp hạng dùng dữ liệu nào?**

A. Two people with scores 8 and 10 — Hai người có điểm 8 và 10

B. Three temperatures — Ba nhiệt độ

C. An empty file — File trống

D. Two stock codes — Hai mã hàng

**Q16. What input is checked by valid_score()? — valid_score() kiểm tra dữ liệu nào?**

A. Score 11 compared with the valid 0–10 range — Điểm 11 so với khoảng 0 đến 10

B. A single text line — Một dòng văn bản

C. Two tax rates — Hai mức thuế

D. A phone number — Số điện thoại

**Q17. What data is summarized? — Hàm summary xử lý dữ liệu nào?**

A. Daily counts 7, 8 and 9 — Số lượng ba ngày 7 8 và 9

B. Three student names — Ba tên học viên

C. Only one score — Chỉ một điểm

D. A CSV header — Tiêu đề CSV

**Q18. What values are filtered? — Những giá trị nào được lọc?**

A. Priority values 1, 5, 2 and 4 — Các điểm ưu tiên 1 5 2 và 4

B. Two email addresses — Hai email

C. A product price only — Chỉ giá sản phẩm

D. A tuple of coordinates — Tuple tọa độ

**Q19. What is true about return and print? — Phát biểu nào đúng về return và print?**

A. A function may return a value without printing — Hàm có thể trả giá trị mà không in

B. return always prints — return luôn in

C. print defines a function — print định nghĩa hàm

D. lambda only sorts — lambda chỉ sắp xếp

**Q20. What is necessary before averaging a list? — Cần làm gì trước khi tính trung bình một list?**

A. Check the empty list before dividing by its length — Kiểm tra list rỗng trước khi chia độ dài

B. Always divide by zero — Luôn chia cho 0

C. Ignore missing data always — Luôn bỏ qua dữ liệu thiếu

D. Remove the return statement — Xóa return

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **A** | A reusable block of code | Khối code có thể gọi nhiều lần |
| Q2 | **B** | A name used in a function definition | Tên biến trong phần định nghĩa hàm |
| Q3 | **C** | Send a value back to the caller | Trả giá trị về nơi gọi |
| Q4 | **A** | A short anonymous function | Hàm ngắn không cần tên |
| Q5 | **A** | It defines a function | Nó định nghĩa hàm |
| Q6 | **A** | It provides a default argument value | Nó cung cấp giá trị tham số mặc định |
| Q7 | **A** | A short function expression | Biểu thức hàm ngắn |
| Q8 | **A** | It chooses a sorting criterion | Nó chọn tiêu chí sắp xếp |
| Q9 | **A** | Reuse the same tax calculation | Dùng lại phép tính thuế |
| Q10 | **A** | Sort by each person's score | Sắp theo điểm mỗi người |
| Q11 | **A** | Reuse the score validation rule | Dùng lại quy tắc kiểm tra điểm |
| Q12 | **A** | Return sum and average together | Trả tổng và trung bình cùng lúc |
| Q13 | **A** | Keep priorities of at least four | Giữ điểm ưu tiên từ bốn trở lên |
| Q14 | **A** | A price of 100000 VND with 10% VAT | Giá 100000 đồng thuế 10% |
| Q15 | **A** | Two people with scores 8 and 10 | Hai người có điểm 8 và 10 |
| Q16 | **A** | Score 11 compared with the valid 0–10 range | Điểm 11 so với khoảng 0 đến 10 |
| Q17 | **A** | Daily counts 7, 8 and 9 | Số lượng ba ngày 7 8 và 9 |
| Q18 | **A** | Priority values 1, 5, 2 and 4 | Các điểm ưu tiên 1 5 2 và 4 |
| Q19 | **A** | A function may return a value without printing | Hàm có thể trả giá trị mà không in |
| Q20 | **A** | Check the empty list before dividing by its length | Kiểm tra list rỗng trước khi chia độ dài |

## 8. Nối sang bài tiếp theo

`Vòng lặp → Hàm → OOP → Pipeline`.

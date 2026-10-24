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
| Biến cục bộ trong `def` | Tên tạo trong hàm thường chỉ dùng được trong hàm, không truy cập trực tiếp từ bên ngoài |


## 4. Khái niệm liên quan

Một **hàm (function)** gom nhiều bước xử lý thành một công việc có tên, có thể gọi lại bằng dữ liệu khác nhau. Khi gọi hàm, giá trị đi vào qua **tham số**, kết quả có thể quay lại bằng **`return`**. `lambda` phù hợp cho một biểu thức ngắn, còn **phạm vi biến (scope)** giúp phân biệt biến chỉ dùng bên trong hàm với biến dùng bên ngoài. Ta dùng cùng ý tưởng tính tiền để lần lượt hiểu năm phần này.

### 4.1. Function — Hàm tái sử dụng

**Từ vựng trong mục:** **Function** — hàm; **Call** — lời gọi hàm.

Giả sử cửa hàng cần tính giá của món hàng nhân đôi khi mua hai phần giống nhau. Nếu viết phép nhân tại nhiều chỗ, thay đổi quy tắc sẽ khó. Ta định nghĩa `twice(x)` bằng từ khóa `def`: `x` là đầu vào, phép `x * 2` tạo kết quả. Khi viết `twice(3)`, Python chạy thân hàm với `x = 3`, rồi trả số 6. Dòng `print()` bên ngoài mới đưa số này lên màn hình.

```python
def twice(x):
    return x * 2

print(twice(3))
```

**Kết quả khi chạy:**

```text
6
```

Một định nghĩa hàm có thể dùng lại cho nhiều giá trị như 3, 5 hoặc 10 mà không viết lại phép nhân.

### 4.2. Parameter và Argument — Tham số và đối số

**Từ vựng trong mục:** **Parameter** — tham số; **Argument** — đối số.

**Tham số** là tên xuất hiện trong dòng định nghĩa, ví dụ `name` của `hello(name)`. **Đối số** là giá trị thật được truyền lúc gọi hàm, ví dụ `'Lan'` trong `hello('Lan')`. Trong thân hàm, `name` tạm nhận `'Lan'`, tạo chuỗi lời chào rồi `return` gửi nó về nơi gọi.

```python
def hello(name):
    return f'Xin chào {name}!'

print(hello('Lan'))
```

**Kết quả khi chạy:**

```text
Xin chào Lan!
```

`name` là tham số, còn `'Lan'` là đối số của lời gọi cụ thể. Truyền `'An'` sẽ tạo lời chào khác.

### 4.3. Return — Kết quả trả về

**Từ vựng trong mục:** **Return** — trả về; **Print** — hiển thị.

`return` khác `print()`: `return` **gửi giá trị về nơi gọi hàm** để chương trình có thể lưu hoặc tính tiếp; `print()` chỉ hiển thị. Ví dụ `add(a, b)` tính tổng hai số. Khi gán `total = add(2, 3)`, biến `total` nhận 5; lệnh `print(total)` mới làm số 5 xuất hiện trên màn hình.

```python
def add(a, b):
    return a + b

total = add(2, 3)
print(total)
```

**Kết quả khi chạy:**

```text
5
```

Giá trị trả về có thể lưu trong biến `total`; nếu hàm chỉ `print()` mà không `return`, nơi gọi không nhận được tổng để tính tiếp.

### 4.4. Lambda — Hàm ngắn dùng một biểu thức

**Từ vựng trong mục:** **Lambda** — hàm ẩn danh; **Expression** — biểu thức.

Khi chỉ cần phép biến đổi đơn giản, `lambda x: x + 1` là cách viết ngắn của một hàm nhận `x` và trả về `x + 1`. Chẳng hạn tăng số lượng hiện tại 5 lên thêm một món sẽ ra 6. `lambda` thích hợp làm tiêu chí sắp xếp hay lọc; công việc có nhiều bước nên dùng `def` để dễ đọc.

```python
increase = lambda x: x + 1
print(increase(5))
```

**Kết quả khi chạy:**

```text
6
```

Hàm được tạo bằng `lambda` nhận 5 và cho 6. Đây là một biểu thức, không có thân nhiều câu lệnh như `def`.

### 4.5. Scope — Phạm vi biến

**Từ vựng trong mục:** **Scope** — phạm vi biến; **Local variable** — biến cục bộ.

**Phạm vi biến** xác định nơi một tên biến có thể được dùng. Trong hàm `with_fee(price)`, biến `fee = 5` chỉ được tạo khi hàm chạy và dùng trong hàm; đó là **biến cục bộ (local)**. Bên ngoài hàm, chương trình chỉ dùng giá trị `return`, không truy cập trực tiếp `fee`. Ví dụ đơn hàng giá 100 (nghìn đồng) có phí xử lý 5 (nghìn đồng).

```python
def with_fee(price):
    fee = 5
    return price + fee

final_price = with_fee(100)
print(final_price)
```

**Kết quả khi chạy:**

```text
105
```

Số 105 là tổng giá và phí, đơn vị nghìn đồng. Biến `fee` ở trong hàm; nếu gọi `print(fee)` ở ngoài, Python sẽ báo `NameError`.
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
def valid_score(x):
    return 0<=x<=10
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
- Không dùng trực tiếp biến cục bộ của hàm từ bên ngoài; đưa dữ liệu cần dùng ra ngoài bằng `return`.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is a Python function? — Hàm Python là gì?**

A. A reusable named block of code — Khối code có tên, dùng lại được

B. A name declared in a function definition — Tên khai báo trong định nghĩa hàm

C. A value supplied when calling a function — Giá trị truyền lúc gọi hàm

D. A result sent back to the caller — Kết quả gửi về nơi gọi

**Q2. What is a parameter? — Tham số là gì?**

A. A reusable named block of code — Khối code có tên, dùng lại được

B. A name declared in a function definition — Tên khai báo trong định nghĩa hàm

C. A value supplied when calling a function — Giá trị truyền lúc gọi hàm

D. A result sent back to the caller — Kết quả gửi về nơi gọi

**Q3. What is an argument? — Đối số là gì?**

A. A reusable named block of code — Khối code có tên, dùng lại được

B. A name declared in a function definition — Tên khai báo trong định nghĩa hàm

C. A value supplied when calling a function — Giá trị truyền lúc gọi hàm

D. A result sent back to the caller — Kết quả gửi về nơi gọi

**Q4. What is a return value? — Giá trị trả về là gì?**

A. A reusable named block of code — Khối code có tên, dùng lại được

B. A name declared in a function definition — Tên khai báo trong định nghĩa hàm

C. A value supplied when calling a function — Giá trị truyền lúc gọi hàm

D. A result sent back to the caller — Kết quả gửi về nơi gọi

**Q5. Which keyword defines a normal function? — Từ khóa nào định nghĩa hàm thông thường?**

A. `def` — `def`

B. `return` — `return`

C. `lambda` — `lambda`

D. `if` — `if`

**Q6. Which keyword sends a value back to the caller? — Từ khóa nào trả giá trị về nơi gọi?**

A. `def` — `def`

B. `return` — `return`

C. `lambda` — `lambda`

D. `if` — `if`

**Q7. Which keyword defines a short anonymous function expression? — Từ khóa nào tạo biểu thức hàm ngắn không tên?**

A. `def` — `def`

B. `return` — `return`

C. `lambda` — `lambda`

D. `if` — `if`

**Q8. Which keyword supplies a conditional branch inside a function? — Từ khóa nào tạo nhánh điều kiện bên trong hàm?**

A. `def` — `def`

B. `return` — `return`

C. `lambda` — `lambda`

D. `if` — `if`

**Q9. What does a default parameter provide? — Tham số mặc định có tác dụng gì?**

A. A fallback value when an argument is omitted — Giá trị dùng khi không truyền đối số

B. An argument passed by parameter name — Đối số truyền theo tên tham số

C. Computing a sorting key for each item — Tính khóa sắp xếp cho từng phần tử

D. Items for which test is truthy — Phần tử có điều kiện test đúng

**Q10. What is a keyword argument? — Đối số theo tên là gì?**

A. A fallback value when an argument is omitted — Giá trị dùng khi không truyền đối số

B. An argument passed by parameter name — Đối số truyền theo tên tham số

C. Computing a sorting key for each item — Tính khóa sắp xếp cho từng phần tử

D. Items for which test is truthy — Phần tử có điều kiện test đúng

**Q11. What does `sorted(rows, key=func)` use `func` for? — Trong `sorted(rows, key=func)`, func dùng để làm gì?**

A. A fallback value when an argument is omitted — Giá trị dùng khi không truyền đối số

B. An argument passed by parameter name — Đối số truyền theo tên tham số

C. Computing a sorting key for each item — Tính khóa sắp xếp cho từng phần tử

D. Items for which test is truthy — Phần tử có điều kiện test đúng

**Q12. What does `filter(test, items)` keep? — `filter(test, items)` giữ gì?**

A. A fallback value when an argument is omitted — Giá trị dùng khi không truyền đối số

B. An argument passed by parameter name — Đối số truyền theo tên tham số

C. Computing a sorting key for each item — Tính khóa sắp xếp cho từng phần tử

D. Items for which test is truthy — Phần tử có điều kiện test đúng

**Q13. What is a local variable? — Biến cục bộ là gì?**

A. A name bound within a function's scope — Tên được tạo trong phạm vi hàm

B. A name defined at module level — Tên được định nghĩa ở mức module

C. A single expression — Một biểu thức

D. A function retaining access to enclosing variables — Hàm còn truy cập được biến từ phạm vi bao ngoài

**Q14. What is a global variable? — Biến toàn cục là gì?**

A. A name bound within a function's scope — Tên được tạo trong phạm vi hàm

B. A name defined at module level — Tên được định nghĩa ở mức module

C. A single expression — Một biểu thức

D. A function retaining access to enclosing variables — Hàm còn truy cập được biến từ phạm vi bao ngoài

**Q15. What is a lambda expression limited to? — Nội dung của lambda bị giới hạn như thế nào?**

A. A name bound within a function's scope — Tên được tạo trong phạm vi hàm

B. A name defined at module level — Tên được định nghĩa ở mức module

C. A single expression — Một biểu thức

D. A function retaining access to enclosing variables — Hàm còn truy cập được biến từ phạm vi bao ngoài

**Q16. What is a closure? — Closure là gì?**

A. A name bound within a function's scope — Tên được tạo trong phạm vi hàm

B. A name defined at module level — Tên được định nghĩa ở mức module

C. A single expression — Một biểu thức

D. A function retaining access to enclosing variables — Hàm còn truy cập được biến từ phạm vi bao ngoài

**Q17. What does a function without explicit `return` produce? — Hàm không có `return` rõ ràng trả về gì?**

A. `None` — `None`

B. Displays output — Hiển thị đầu ra

C. A tuple of two values — Một Tuple gồm hai giá trị

D. `NameError` — `NameError`

**Q18. What does `print()` do instead of returning a useful result? — `print()` làm gì thay vì trả một kết quả để tính tiếp?**

A. `None` — `None`

B. Displays output — Hiển thị đầu ra

C. A tuple of two values — Một Tuple gồm hai giá trị

D. `NameError` — `NameError`

**Q19. What does a function's `return a, b` actually return? — `return a, b` thực chất trả gì?**

A. `None` — `None`

B. Displays output — Hiển thị đầu ra

C. A tuple of two values — Một Tuple gồm hai giá trị

D. `NameError` — `NameError`

**Q20. What happens when code outside a function reads an undefined local name? — Đọc biến cục bộ không tồn tại ở ngoài hàm gây gì?**

A. `None` — `None`

B. Displays output — Hiển thị đầu ra

C. A tuple of two values — Một Tuple gồm hai giá trị

D. `NameError` — `NameError`

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **A** | A function packages related operations and may be called repeatedly. | Hàm gom thao tác liên quan và có thể gọi nhiều lần. |
| Q2 | **B** | A parameter acts as a local name for supplied input. | Tham số là tên cục bộ nhận dữ liệu đầu vào. |
| Q3 | **C** | The caller supplies argument values for parameters. | Nơi gọi truyền giá trị đối số vào tham số. |
| Q4 | **D** | return provides a result that calling code can reuse. | return trả kết quả để nơi gọi có thể tiếp tục sử dụng. |
| Q5 | **A** | def introduces a function body with a name. | def mở phần khai báo hàm có tên. |
| Q6 | **B** | return exits the function and optionally sends its value back. | return kết thúc hàm và có thể trả lại giá trị. |
| Q7 | **C** | lambda creates a callable function from one expression. | lambda tạo hàm từ một biểu thức. |
| Q8 | **D** | if chooses a branch while the function executes. | if lựa chọn nhánh khi hàm đang chạy. |
| Q9 | **A** | Default values are used only when the caller omits that argument. | Giá trị mặc định được dùng khi nơi gọi không truyền đối số tương ứng. |
| Q10 | **B** | Keyword arguments explicitly name the parameter being filled. | Đối số theo tên chỉ rõ tham số được gán giá trị. |
| Q11 | **C** | The key function determines comparison values for ordering. | Hàm key xác định giá trị dùng để so sánh khi sắp xếp. |
| Q12 | **D** | filter retains elements that satisfy the predicate. | filter giữ phần tử thỏa điều kiện lọc. |
| Q13 | **A** | A local binding generally exists only for that function execution. | Biến cục bộ thường chỉ tồn tại trong phạm vi thực thi hàm. |
| Q14 | **B** | Module-level names are available for reading from functions unless shadowed. | Tên cấp module có thể được hàm đọc nếu không bị che bởi tên cục bộ. |
| Q15 | **C** | lambda syntax uses one expression, not a normal multi-statement block. | lambda dùng một biểu thức, không có thân nhiều câu lệnh thông thường. |
| Q16 | **D** | A closure can retain references to variables in an enclosing scope. | Closure có thể tiếp tục dùng các biến ở phạm vi hàm bao ngoài. |
| Q17 | **A** | Python implicitly returns None when execution reaches the function end. | Python ngầm trả None khi hàm chạy tới cuối mà không return. |
| Q18 | **B** | print shows data; return is how a function passes a result to its caller. | print hiển thị dữ liệu, còn return truyền kết quả về nơi gọi. |
| Q19 | **C** | Comma-separated return values are packed into a tuple. | Hai giá trị sau return được đóng gói thành Tuple. |
| Q20 | **D** | A local name is not automatically defined in the caller's scope. | Tên cục bộ không tự tồn tại trong phạm vi nơi gọi. |

## 8. Nối sang bài tiếp theo

`Vòng lặp → Hàm → OOP → Pipeline`.

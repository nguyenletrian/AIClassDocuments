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

A. Only a variable declared at module level — Chỉ biến khai báo ở cấp module

B. Only code that prints text — Chỉ mã in văn bản

C. Only a loop executed once — Chỉ vòng lặp chạy một lần

D. Reusable callable code that can accept inputs — Phần mã có thể gọi lại, có thể nhận đầu vào


**Q2. What is a parameter? — Tham số là gì?**

A. A value supplied by the caller — Giá trị truyền từ nơi gọi

B. A name declared in a function's definition — Tên khai báo trong định nghĩa hàm

C. The value printed by a function — Giá trị được hàm in ra

D. A variable always declared global — Biến luôn được khai báo toàn cục


**Q3. What is an argument? — Đối số là gì?**

A. The name in the function definition — Tên trong định nghĩa hàm

B. A keyword beginning a function body — Từ khóa bắt đầu thân hàm

C. A value supplied in a function call — Giá trị truyền khi gọi hàm

D. The result returned by a function — Kết quả hàm trả về


**Q4. What is a return value? — Giá trị trả về là gì?**

A. A result sent back to the caller — Kết quả gửi về nơi gọi

B. A parameter name — Tên tham số

C. The function's source-code text — Văn bản mã nguồn hàm

D. A displayed message from `print` — Thông báo hiển thị bởi `print`


**Q5. Which keyword defines a normal function? — Từ khóa nào định nghĩa hàm thông thường?**

A. `return` — `return`

B. `lambda` — `lambda`

C. `if` — `if`

D. `def` — `def`


**Q6. Which keyword sends a value back to the caller? — Từ khóa nào trả giá trị về nơi gọi?**

A. `lambda` — `lambda`

B. `if` — `if`

C. `def` — `def`

D. `return` — `return`


**Q7. Which keyword defines a short anonymous function expression? — Từ khóa nào tạo biểu thức hàm ngắn không tên?**

A. `def` — `def`

B. `return` — `return`

C. `lambda` — `lambda`

D. `if` — `if`


**Q8. Which keyword supplies a conditional branch inside a function? — Từ khóa nào tạo nhánh điều kiện bên trong hàm?**

A. `lambda` — `lambda`

B. `if` — `if`

C. `def` — `def`

D. `return` — `return`


**Q9. What does a default parameter provide? — Tham số mặc định có tác dụng gì?**

A. A value calculated only after the function returns — Giá trị chỉ tính sau khi hàm trả về

B. A value that must be supplied for every call — Giá trị bắt buộc phải truyền ở mọi lần gọi

C. A fallback value used when the caller omits an argument — Giá trị dự phòng khi nơi gọi không truyền đối số

D. A value that overrides every explicit argument — Giá trị ghi đè mọi đối số truyền vào


**Q10. What is a keyword argument? — Đối số theo tên là gì?**

A. An argument supplied using its parameter's name — Đối số truyền bằng tên tham số

B. A local variable defined outside the function — Biến cục bộ định nghĩa ngoài hàm

C. A function name passed without calling — Tên hàm được truyền mà không gọi

D. An argument always matched only by position — Đối số luôn ghép bằng vị trí

**Q11. What does `sorted(rows, key=func)` use `func` for? — Trong `sorted(rows, key=func)`, func dùng để làm gì?**

A. Filtering out all false-valued items before sorting — Loại mọi phần tử có giá trị sai trước khi sắp

B. Computing a sort key for each item — Tính khóa sắp xếp cho từng phần tử

C. Replacing every row with `None` — Thay mỗi hàng bằng `None`

D. Printing each row during sorting — In từng hàng trong lúc sắp

**Q12. What does `filter(test, items)` keep? — `filter(test, items)` giữ gì?**

A. Only items whose test result is false — Chỉ phần tử có kết quả kiểm tra sai

B. Items in descending order — Phần tử theo thứ tự giảm dần

C. Items for which `test(item)` is truthy — Phần tử mà `test(item)` có giá trị đúng

D. All items, regardless of the test — Mọi phần tử, bất kể phép kiểm tra


**Q13. What is a local variable? — Biến cục bộ là gì?**

A. Any name defined at module level — Bất kỳ tên nào khai báo cấp module

B. A name automatically shared by every function — Tên tự chia sẻ cho mọi hàm

C. A name that can never change value — Tên không bao giờ đổi giá trị

D. A name bound within a function's local scope — Tên được gán trong phạm vi cục bộ hàm


**Q14. What is a global variable? — Biến toàn cục là gì?**

A. A name bound at module level — Tên được gán ở cấp module

B. A name that exists only inside a class — Tên chỉ tồn tại trong class

C. A name inaccessible to all functions — Tên mọi hàm đều không truy cập được

D. A name created only by `lambda` — Tên chỉ do `lambda` tạo


**Q15. What is a lambda expression limited to? — Nội dung của lambda bị giới hạn như thế nào?**

A. A complete `try/except` statement block — Khối câu lệnh `try/except` đầy đủ

B. A single expression — Một biểu thức

C. Only a numeric literal — Chỉ một literal số

D. A series of ordinary statements — Chuỗi các câu lệnh thông thường


**Q16. What is a closure? — Closure là gì?**

A. A function forced to return `None` — Hàm bị buộc trả `None`

B. A function that prints its enclosing scope — Hàm in phạm vi bao ngoài

C. A function that discards all free variables — Hàm loại bỏ mọi biến tự do

D. A function whose enclosing names remain accessible — Hàm vẫn truy cập được tên của phạm vi bao ngoài

**Q17. When a function reaches its end without executing `return`, what value does it return? — Khi hàm chạy đến cuối mà không thực hiện `return`, nó trả giá trị nào?**

A. `None` — `None`

B. An empty string `''` — Chuỗi rỗng `''`

C. The last local variable — Biến cục bộ cuối

D. `NameError` — `NameError`


**Q18. What does `print()` do instead of returning a useful result? — `print()` làm gì thay vì trả một kết quả để tính tiếp?**

A. Displays output while returning `None` — Hiển thị đầu ra và trả `None`

B. Returns a tuple with the printed text — Trả Tuple chứa văn bản đã in

C. Raises `TypeError` whenever called — Mỗi khi gọi đều gây `TypeError`

D. Always returns the printed string — Luôn trả chuỗi đã in


**Q19. What does a function's `return a, b` actually return? — `return a, b` thực chất trả gì?**

A. The result of adding `a` and `b` — Kết quả cộng `a` với `b`

B. A tuple containing both values — Tuple chứa cả hai giá trị

C. A list containing both values — List chứa cả hai giá trị

D. The two values as separate function return objects — Hai giá trị thành hai đối tượng trả về riêng


**Q20. What happens when code outside a function reads an undefined local name? — Đọc biến cục bộ không tồn tại ở ngoài hàm gây gì?**

A. The most recent printed value is used — Dùng giá trị vừa được in

B. The local name is exported automatically — Tên cục bộ tự xuất ra ngoài

C. `NameError` for the undefined name — `NameError` vì tên chưa được định nghĩa

D. `None` is silently substituted — Tự thay bằng `None`

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **D** | A Python function is reusable callable code that can accept inputs and may return a result. A normal function can be defined with `def`, while `lambda` also creates a function from one expression; being named is not a requirement of all functions. | Hàm Python là phần mã có thể gọi lại nhiều lần, có thể nhận đầu vào và trả kết quả. Hàm thường có thể định nghĩa bằng `def`, còn `lambda` cũng tạo hàm từ một biểu thức; không phải mọi hàm đều bắt buộc có tên. |
| Q2 | **B** | A parameter is a name declared in the function definition to receive an input. In `def double(x):`, `x` is a parameter, whereas the `3` in `double(3)` is an argument supplied at call time. | Tham số là tên khai báo trong định nghĩa hàm để nhận đầu vào. Trong `def double(x):`, `x` là tham số, còn số `3` trong `double(3)` là đối số được truyền khi gọi. |
| Q3 | **C** | An argument is the actual value supplied in a function call. For `double(3)`, the integer `3` is the argument bound to parameter `x`; the parameter name appears in the definition. | Đối số là giá trị thực tế được truyền vào khi gọi hàm. Với `double(3)`, số nguyên `3` là đối số gắn vào tham số `x`; tên tham số xuất hiện trong phần định nghĩa. |
| Q4 | **A** | A return value is information passed back to the caller by the function's `return` statement. Unlike `print`, which displays text, `return` lets surrounding code reuse the computed value. | Giá trị trả về là thông tin hàm gửi về nơi gọi qua câu lệnh `return`. Khác `print` dùng để hiển thị, `return` giúp mã gọi hàm tiếp tục sử dụng kết quả tính toán. |
| Q5 | **D** | `def` begins a named function definition followed by parameters, a colon, and an indented body. `lambda` creates a function expression, while `return` is used within the body to send back a result. | `def` mở đầu định nghĩa hàm có tên, tiếp theo là tham số, dấu hai chấm và thân hàm thụt lề. `lambda` tạo biểu thức hàm, còn `return` dùng bên trong thân để trả kết quả. |
| Q6 | **D** | `return` ends the current function call and sends the indicated value to its caller. For `return x * 2`, the caller receives the doubled value; `print(x * 2)` merely displays it and then returns `None`. | `return` kết thúc lần gọi hàm hiện tại và chuyển giá trị đã chỉ ra về nơi gọi. Với `return x * 2`, nơi gọi nhận giá trị gấp đôi; `print(x * 2)` chỉ hiển thị rồi trả `None`. |
| Q7 | **C** | `lambda` creates a function using a single expression, such as `lambda x: x * 2`. The function may be assigned to a name or passed as an argument, unlike `def` which introduces a regular statement-based definition. | `lambda` tạo hàm từ một biểu thức, chẳng hạn `lambda x: x * 2`. Hàm có thể gán cho tên hoặc truyền làm đối số, khác `def` mở định nghĩa hàm theo dạng câu lệnh. |
| Q8 | **B** | `if` introduces a conditional branch inside a function, so the function may execute different paths based on input. It does not by itself create a function or return a value to the caller. | `if` mở nhánh điều kiện bên trong hàm, giúp hàm chọn đường thực thi theo đầu vào. Bản thân `if` không tạo hàm và cũng không trả giá trị về nơi gọi. |
| Q9 | **C** | A default parameter value is used when the caller omits that argument; for `def greet(name='An')`, `greet()` uses `'An'`. Explicitly passing `greet('Binh')` overrides that default, so it is a fallback rather than a forced value. | Giá trị mặc định của tham số được dùng khi nơi gọi bỏ qua đối số đó; với `def greet(name='An')`, `greet()` dùng `'An'`. Nếu gọi `greet('Binh')` thì giá trị truyền vào thay mặc định, vì vậy đây là dự phòng chứ không phải giá trị bắt buộc. |
| Q10 | **A** | A keyword argument names the parameter in the call, such as `greet(name='An')`. This differs from a positional argument such as `greet('An')`, which is matched by its position. | Đối số theo tên nêu rõ tên tham số lúc gọi, ví dụ `greet(name='An')`. Nó khác đối số theo vị trí như `greet('An')`, vốn ghép với tham số dựa trên vị trí truyền vào. |
| Q11 | **B** | In `sorted(rows, key=func)`, `func` computes a comparison key for each item; sorting uses those returned keys. For `key=len`, shorter strings come first by length rather than lexicographic order. | Trong `sorted(rows, key=func)`, `func` tính giá trị khóa so sánh cho từng phần tử; phép sắp xếp dùng các khóa đó. Ví dụ `key=len` sẽ ưu tiên chuỗi ngắn trước theo độ dài thay vì thứ tự chữ cái. |
| Q12 | **C** | `filter(test, items)` selects items for which `test(item)` is truthy, returning an iterator in Python 3. For `filter(lambda x: x > 0, [-1,2])`, converting to `list` gives `[2]`, not all original elements. | `filter(test, items)` chọn phần tử mà `test(item)` có giá trị đúng, trả iterator trong Python 3. Với `filter(lambda x: x > 0, [-1,2])`, chuyển sang `list` được `[2]`, không phải mọi phần tử ban đầu. |
| Q13 | **D** | A local variable is a name bound in a function's local scope, such as `total` assigned inside `def add():`. It is not automatically defined outside the function, unlike a module-level global name. | Biến cục bộ là tên được gán trong phạm vi cục bộ của hàm, như `total` gán trong `def add():`. Nó không tự tồn tại ngoài hàm, khác tên toàn cục khai báo ở cấp module. |
| Q14 | **A** | A global variable is a name bound at module level and is generally readable inside functions unless shadowed. Assigning to the global binding inside a function usually requires a `global` declaration, unlike simply reading it. | Biến toàn cục là tên được gán ở cấp module và thường có thể đọc trong hàm nếu không bị che khuất. Muốn gán lại chính biến toàn cục từ trong hàm thường phải khai báo `global`, khác việc chỉ đọc giá trị. |
| Q15 | **B** | A Python `lambda` body consists of a single expression whose value becomes the function result. It cannot contain ordinary multi-statement bodies like a sequence of `for` statements and assignments; use `def` for those. | Thân `lambda` trong Python chỉ chứa một biểu thức và giá trị biểu thức trở thành kết quả hàm. Nó không chứa khối nhiều câu lệnh thông thường như chuỗi lệnh `for` và gán; cần dùng `def` trong trường hợp đó. |
| Q16 | **D** | A closure is a function that retains access to names from its enclosing lexical scope, even after the outer function returns. It retains references to those bindings, not necessarily frozen snapshots of their values. | Closure là hàm vẫn truy cập được các tên thuộc phạm vi bao ngoài, kể cả sau khi hàm ngoài đã trả về. Nó giữ liên kết tham chiếu tới các tên đó chứ không nhất thiết chụp cố định giá trị tại một thời điểm. |
| Q17 | **A** | If execution reaches the end of a function without an explicit `return`, Python implicitly returns `None`. The function can still print messages, but printing does not turn those messages into its return value. | Nếu hàm chạy đến cuối mà không có `return` tường minh, Python ngầm trả `None`. Hàm vẫn có thể in thông báo nhưng việc in không biến thông báo đó thành giá trị trả về. |
| Q18 | **A** | `print()` sends text to standard output and its return value is `None`. For example `result = print('Hi')` displays `Hi` but stores `None` in `result`; use `return` in a function when later code needs a result. | `print()` đưa văn bản ra đầu ra chuẩn và giá trị trả về là `None`. Ví dụ `result = print('Hi')` hiển thị `Hi` nhưng lưu `None` vào `result`; dùng `return` trong hàm nếu mã phía sau cần kết quả. |
| Q19 | **B** | A comma-separated return expression packs values into a tuple, so `return a, b` returns `(a, b)`. The caller can unpack it into two names, but the function actually returns one tuple object. | Biểu thức trả về có các giá trị cách nhau bằng dấu phẩy đóng gói chúng thành Tuple, nên `return a, b` trả `(a, b)`. Nơi gọi có thể giải nén ra hai tên, nhưng hàm thực tế trả một đối tượng Tuple. |
| Q20 | **C** | A local name assigned only inside a function does not automatically exist in the module's scope. Reading that undefined name outside raises `NameError`; return it explicitly or store it in a separate accessible binding. | Tên cục bộ chỉ được gán bên trong hàm không tự tồn tại ở phạm vi module. Đọc tên chưa được định nghĩa ở ngoài gây `NameError`; cần trả về tường minh hoặc lưu vào liên kết có thể truy cập. |

## 8. Nối sang bài tiếp theo

`Vòng lặp → Hàm → OOP → Pipeline`.

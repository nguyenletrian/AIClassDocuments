# PY-09 — Hàm, return, lambda và phạm vi biến


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Function** — hàm; **Parameter** — tham số.

`Vòng lặp → Hàm → OOP → Pipeline`

**Học xong dùng để làm gì?** Đóng gói phép tính thành hàm nhận dữ liệu, trả kết quả; dùng lambda làm khóa sắp xếp.

**Kết nối kiến thức tiếp theo:** PY-10 tổ chức dữ liệu và thao tác của một đối tượng thành class.

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

**No Note — Không chú thích**

```python
def twice(x):
    return x * 2

print(twice(3))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tạo hàm twice để nhân đôi số theo đối số.
# Dữ liệu: twice nhận số x và trả giá trị gấp đôi, không in trong hàm.
# def tạo hàm có tham số x; chưa thực thi thân hàm cho đến khi gọi.
def twice(x):
    # return trả x nhân 2 về bên gọi; không tự in.
    return x * 2

# Gọi twice với đối số 3, print in kết quả 6.
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

**No Note — Không chú thích**

```python
def hello(name):
    return f'Xin chào {name}!'

print(hello('Lan'))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Phân biệt tham số khi định nghĩa hàm và đối số khi gọi.
# Dữ liệu: hello nhận tên làm tham số, chuỗi kết quả tạo bằng f-string.
# name là tham số nhận chuỗi khi gọi hàm.
def hello(name):
    # f-string chèn giá trị name vào thông điệp và return trả chuỗi.
    return f'Xin chào {name}!'

# Truyền 'Lan' làm đối số thực tế cho tham số name.
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

**No Note — Không chú thích**

```python
def add(a, b):
    return a + b

total = add(2, 3)
print(total)
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Dùng return trả tổng hai đối số cho biến bên ngoài.
# Dữ liệu: Hàm add có hai tham số a, b; return đưa tổng về bên gọi.
# Hai tham số a,b nhận hai số của người gọi.
def add(a, b):
    # return đưa tổng cho bên gọi, kết thúc hàm.
    return a + b

# Gọi hàm với hai đối số 2 và 3, gán kết quả 5 vào total.
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

**No Note — Không chú thích**

```python
increase = lambda x: x + 1
print(increase(5))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tạo hàm lambda một biểu thức cộng 1.
# Dữ liệu: lambda là hàm không đặt tên tạo trực tiếp bằng một biểu thức.
# lambda nhận tham số x và trả x+1 ngay, không cần def/return.
increase = lambda x: x + 1
# Gọi hàm vừa tạo, nhận 6.
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

**No Note — Không chú thích**

```python
def with_fee(price):
    fee = 5
    return price + fee

final_price = with_fee(100)
print(final_price)
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Phân biệt biến fee cục bộ trong hàm và giá bên ngoài.
# Dữ liệu: fee là biến chỉ tồn tại khi chạy with_fee, không phải biến toàn cục.
# price là tham số của hàm, tách khỏi giá trị bên ngoài.
def with_fee(price):
    # fee là biến cục bộ tạo trong hàm mỗi lần gọi.
    fee = 5
    # return cộng phí 5 vào giá và trả lại kết quả.
    return price + fee

# Truyền giá 100, kết quả là 105.
final_price = with_fee(100)
print(final_price)
```

**Kết quả khi chạy:**

```text
105
```

Số 105 là tổng giá và phí, đơn vị nghìn đồng. Biến `fee` ở trong hàm; nếu gọi `print(fee)` ở ngoài, Python sẽ báo `NameError`.
## 5. Năm tình huống hàm — từ return cơ bản đến pipeline 20 đơn

### Tình huống 1 — Cấp 1: Dùng một hàm tính giá đã cộng thuế của 10 món

**Từ vựng trong mục:** **Function** — hàm; **Return** — trả về; **Default argument** — đối số mặc định.

**Tình huống thực tế:** Một cửa hàng văn phòng phẩm có bảng giá trước thuế của **10 mặt hàng**, mỗi giá tính bằng **đồng/món**. Trong ví dụ giả lập, cửa hàng áp dụng mức thuế **10%** đồng đều và khách mua một món mỗi loại. Thu ngân muốn tính giá sau thuế từng món rồi cộng tổng số tiền phải trả, không phải nhập lại cùng cách tính cho cả mười món.

**Vì sao chọn cách này?** **Hàm** là một đoạn xử lý được đặt tên để dùng lại nhiều lần. `def` tạo hàm tính giá một món sau thuế; **tham số** nhận đơn giá của từng mặt hàng. `return` trả số tiền mới về nơi gọi, nên vòng `for` có thể lấy kết quả của 10 món để cộng tổng. Nếu chỉ dùng `print()` trong hàm thì màn hình có thể hiện số nhưng chỗ tính tổng không nhận được giá trị để cộng. Thuế 10% chỉ là giả định cho dữ liệu minh họa, không khẳng định mọi sản phẩm ngoài đời đều chịu mức này.

**Quy trình:**
1. Định nghĩa hàm `with_tax(price, rate=0.10)` có tham số mặc định.
2. Gọi hàm cho mỗi trong 10 đơn giá.
3. Tổng hợp, kiểm tra số lượng và in tổng.

**No Note — Không chú thích**

```python
prices_vnd = [50000,72000,90000,110000,85000,60000,95000,120000,140000,100000]
def with_tax(price, rate=0.10):
    return round(price * (1 + rate))
prices_after_tax = []
for price in prices_vnd:
    prices_after_tax.append(with_tax(price))
if len(prices_after_tax) != 10:
    raise ValueError("Cần tính thuế đủ 10 đơn giá.")
print("Mặt hàng:", len(prices_vnd))
print("Giá món đầu:", prices_after_tax[0])
print("Tổng tiền (đồng):", sum(prices_after_tax))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Viết hàm tính giá có thuế mặc định 10% cho 10 món.
# Dữ liệu: 10 giá đồng Việt Nam; rate=0.10 là thuế suất mặc định 10%.
prices_vnd = [50000,72000,90000,110000,85000,60000,95000,120000,140000,100000]
# rate có giá trị mặc định 0.10: có thể không truyền để dùng thuế 10%.
def with_tax(price, rate=0.10):
    # Nhân đơn giá với 1.10 để cộng thuế, round() làm tròn tới số nguyên đồng.
    return round(price * (1 + rate))
prices_after_tax = []
for price in prices_vnd:
    # append() tích lũy tiền sau thuế từng món.
    prices_after_tax.append(with_tax(price))
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
if len(prices_after_tax) != 10:
    # raise báo lỗi rồi dừng luồng hiện tại nếu dữ liệu không đáp ứng yêu cầu.
    raise ValueError("Cần tính thuế đủ 10 đơn giá.")
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
print("Mặt hàng:", len(prices_vnd))
# [0] chỉ phần tử đầu tiên; Python đánh số vị trí từ 0.
print("Giá món đầu:", prices_after_tax[0])
# sum() cộng tổng mười mức giá đã có thuế.
print("Tổng tiền (đồng):", sum(prices_after_tax))
```

**Kết quả khi chạy:**

```text
Mặt hàng: 10
Giá món đầu: 55000
Tổng tiền (đồng): 1014200
```

Hàm trả về số, không tự in ra; có thể dùng tiếp trong các phép tính khác mà không phải sao chép biểu thức.

### Tình huống 2 — Cấp 2: Dùng lambda sắp 12 học viên giữ thứ tự hòa điểm

**Từ vựng trong mục:** **Lambda** — hàm ngắn; **Key function** — hàm chọn khóa; **Sorted** — sắp xếp.

**Tình huống thực tế:** Trung tâm nhận **12 hồ sơ học viên** theo thứ tự gửi đơn. Mỗi hồ sơ có tên và điểm trên thang **10**; vài học viên có cùng điểm. Người phụ trách muốn xếp học viên theo điểm từ cao xuống thấp để chọn **bốn người phỏng vấn trước**. Khi hai người đồng điểm, ai gửi hồ sơ trước phải đứng trước, không được đảo ngẫu nhiên thứ tự.

**Vì sao chọn cách này?** **Sắp xếp** là thay đổi thứ tự hiển thị, còn **khóa sắp xếp** (`key`) cho Python biết cần nhìn vào thông tin nào. Ở đây khóa là trường `score`, không phải tên. `lambda item: item['score']` là một hàm nhỏ chỉ dùng tại chỗ để lấy điểm của từng hồ sơ; `reverse=True` cho điểm cao đứng trước. `sorted()` tạo danh sách mới; Python giữ thứ tự ban đầu của các phần tử có **khóa bằng nhau**, nên người nộp trước vẫn trước khi hòa điểm. Sau đó chỉ chọn bốn hồ sơ đầu, không dùng thứ tự tên hay thời gian nộp để thay thế điểm.

**Quy trình:**
1. Lưu 12 Dictionary theo thứ tự tiếp nhận.
2. Viết lambda đọc cột `score` làm khóa cho `sorted`.
3. Lấy bốn tên đầu và kiểm tra danh sách nguồn không đổi.

**No Note — Không chú thích**

```python
students = [{"name":"An","score":8},{"name":"Bình","score":9},{"name":"Chi","score":7},{"name":"Dung","score":9},{"name":"Hà","score":6},{"name":"Khánh","score":10},{"name":"Lan","score":8},{"name":"Minh","score":9},{"name":"Nam","score":5},{"name":"Trang","score":10},{"name":"Vy","score":7},{"name":"Yến","score":9}]
ranked = sorted(students, key=lambda item: item["score"], reverse=True)
if len(students) != 12:
    raise ValueError("Cần đủ 12 hồ sơ đăng ký.")
if students[0]["name"] != "An":
    raise ValueError("Danh sách gốc không được đổi thứ tự nộp.")
print("Học viên:", len(students))
interview_names = []
for student in ranked[:4]:
    interview_names.append(student["name"])
print("Phỏng vấn trước:", ", ".join(interview_names))
print("Nguồn đầu:", students[0]["name"])
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Dùng lambda làm khóa xếp 12 học viên theo điểm giảm.
# Dữ liệu: 12 dict hồ sơ gồm name và score, điểm dùng để ưu tiên phỏng vấn.
students = [{"name":"An","score":8},{"name":"Bình","score":9},{"name":"Chi","score":7},{"name":"Dung","score":9},{"name":"Hà","score":6},{"name":"Khánh","score":10},{"name":"Lan","score":8},{"name":"Minh","score":9},{"name":"Nam","score":5},{"name":"Trang","score":10},{"name":"Vy","score":7},{"name":"Yến","score":9}]
# key=lambda item: item['score'] chọn trường điểm làm khóa; reverse=True xếp điểm lớn trước, sorted() không sửa list gốc.
ranked = sorted(students, key=lambda item: item["score"], reverse=True)
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
if len(students) != 12:
    # raise báo lỗi rồi dừng luồng hiện tại nếu dữ liệu không đáp ứng yêu cầu.
    raise ValueError("Cần đủ 12 hồ sơ đăng ký.")
# [0] chỉ phần tử đầu tiên; Python đánh số vị trí từ 0.
if students[0]["name"] != "An":
    # raise báo lỗi rồi dừng luồng hiện tại nếu dữ liệu không đáp ứng yêu cầu.
    raise ValueError("Danh sách gốc không được đổi thứ tự nộp.")
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
print("Học viên:", len(students))
interview_names = []
# [:4] lấy bốn học viên đứng đầu, cận 4 bị loại.
for student in ranked[:4]:
    # append() thêm một phần tử vào cuối danh sách và cập nhật danh sách gốc.
    interview_names.append(student["name"])
# join() nối các chuỗi bằng ký tự phân cách, ở đây là dấu phẩy và khoảng trắng.
print("Phỏng vấn trước:", ", ".join(interview_names))
# [0] chỉ phần tử đầu tiên; Python đánh số vị trí từ 0.
print("Nguồn đầu:", students[0]["name"])
```

**Kết quả khi chạy:**

```text
Học viên: 12
Phỏng vấn trước: Khánh, Trang, Bình, Dung
Nguồn đầu: An
```

Lambda chỉ định trường điểm để so, không làm thay đổi thứ tự ban đầu của hồ sơ khi các điểm bằng nhau.

### Tình huống 3 — Cấp 3: Tách hàm kiểm tra điểm và hàm xét đạt cho 15 lượt

**Từ vựng trong mục:** **Parameter** — tham số; **Boolean return** — trả về đúng/sai; **Composition** — phối hợp hàm.

**Tình huống thực tế:** Giáo vụ có **15 lượt ghi điểm kiểm tra**, mỗi lượt là một giá trị trên thang **0 đến 10** hoặc dữ liệu chưa có. Danh sách có điểm 11 (quá cao), -1 (không hợp lệ) và `None` (chưa nhập). Điểm hợp lệ từ 5 trở lên được tính là đạt. Giáo vụ muốn biết có bao nhiêu điểm hợp lệ, bao nhiêu người đạt và bao nhiêu lượt chưa thể xét.

**Vì sao chọn cách này?** Để tránh xét sai, tách thành **hai câu hỏi**: giá trị này có phải điểm hợp lệ 0–10 không, và nếu hợp lệ thì có đạt mức 5 không. Hàm `valid_score()` trả kết quả đúng/sai cho câu hỏi đầu; hàm `passed()` dùng lại kiểm tra đó trước khi xét ngưỡng. Như vậy 11, -1 và `None` không bị nhầm thành điểm đạt hoặc trượt bình thường. Hàm nhỏ dễ thử bằng nhiều dữ liệu; viết riêng quy tắc ở từng nơi sẽ dễ có chỗ quên kiểm tra số thiếu.

**Quy trình:**
1. Định nghĩa `valid_score()` trả `True/False` trên dữ liệu đầu vào.
2. Định nghĩa `passed()` dùng kết quả kiểm tra để xét ngưỡng 5.
3. Duyệt đủ 15 lượt và báo các nhóm không chồng lấn.

**No Note — Không chú thích**

```python
scores = [4,7,9,10,2,5,11,8,None,6,0,3,7.5,9.5,-1]
def valid_score(value):
    return isinstance(value, (int, float)) and 0 <= value <= 10

def passed(value):
    return valid_score(value) and value >= 5
valid = []
passed_scores = []
for score in scores:
    if valid_score(score):
        valid.append(score)
        if passed(score):
            passed_scores.append(score)
if len(scores) != 15:
    raise ValueError("Cần kiểm tra đủ 15 kết quả điểm.")
print("Lượt nhận:", len(scores))
print("Hợp lệ:", len(valid))
print("Đạt:", len(passed_scores))
print("Không hợp lệ:", len(scores) - len(valid))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tách hàm kiểm tra điểm hợp lệ và hàm kiểm tra điểm đạt cho 15 kết quả.
# Dữ liệu: 15 số điểm gồm None, số âm và số >10 cần lọc.
scores = [4,7,9,10,2,5,11,8,None,6,0,3,7.5,9.5,-1]
# Hàm kiểm tra đầu vào thuộc số nguyên hoặc số thực và trong thang điểm.
def valid_score(value):
    # isinstance() kiểm tra kiểu là int hoặc float trước khi so 0..10, tránh lỗi với None.
    return isinstance(value, (int, float)) and 0 <= value <= 10

# Hàm tái dùng valid_score rồi xét >=5 để tính đạt.
def passed(value):
    # and bảo đảm điểm hợp lệ và từ 5 trở lên mới đạt.
    return valid_score(value) and value >= 5
valid = []
passed_scores = []
for score in scores:
    # Chỉ đưa điểm hợp lệ vào danh sách; tránh dùng None hoặc 11/-1.
    if valid_score(score):
        # append() thêm một phần tử vào cuối danh sách và cập nhật danh sách gốc.
        valid.append(score)
        # Lọc tiếp người đạt trong nhóm đã hợp lệ.
        if passed(score):
            # append() thêm một phần tử vào cuối danh sách và cập nhật danh sách gốc.
            passed_scores.append(score)
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
if len(scores) != 15:
    # raise báo lỗi rồi dừng luồng hiện tại nếu dữ liệu không đáp ứng yêu cầu.
    raise ValueError("Cần kiểm tra đủ 15 kết quả điểm.")
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
print("Lượt nhận:", len(scores))
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
print("Hợp lệ:", len(valid))
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
print("Đạt:", len(passed_scores))
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
print("Không hợp lệ:", len(scores) - len(valid))
```

**Kết quả khi chạy:**

```text
Lượt nhận: 15
Hợp lệ: 12
Đạt: 8
Không hợp lệ: 3
```

Điểm 0 là điểm thật nhưng chưa đạt, không bị hiểu là dữ liệu thiếu. Phân biệt hai bước kiểm tra là trọng tâm của cấp 3.

### Tình huống 4 — Cấp 4: Hàm trả cả thống kê và các dòng lỗi trong 18 giao dịch

**Từ vựng trong mục:** **Return tuple** — trả nhiều giá trị; **Validation** — kiểm tra hợp lệ; **Scope** — phạm vi biến.

**Tình huống thực tế:** Bộ phận kế toán nhận **18 khoản chi** tính bằng **nghìn đồng**. Trong dữ liệu có hai khoản chưa nhập (`None`) và một khoản -20, không hợp lệ vì chi phí của bài này phải là số không âm. Nhân viên muốn một kết quả báo cáo chung: có bao nhiêu dòng đúng, tổng chi phí hợp lệ, chi phí trung bình và mã các khoản cần sửa, trong khi giữ nguyên bảng gốc.

**Vì sao chọn cách này?** **Hàm trả nhiều giá trị** có thể gom thông tin báo cáo thành một tuple, ví dụ `(số khoản hợp lệ, tổng chi, trung bình, danh sách mã lỗi)`. Chương trình lặp qua đủ 18 dòng; `None` là chưa biết chi phí, còn -20 vi phạm quy định không âm, nên đều được ghi vào nhóm cần sửa, không đưa vào tổng. Biến tổng và danh sách lỗi được tạo **bên trong hàm** (biến cục bộ), không làm sửa dữ liệu đầu vào. Trung bình phải được tính từ **số dòng hợp lệ**, nếu lấy cả 18 dòng làm mẫu số thì kết quả sẽ sai.

**Quy trình:**
1. Xác định dữ liệu hợp lệ: là số và không âm.
2. Duyệt trong hàm, tích lũy các số hợp lệ và ghi mã lỗi.
3. Trả tuple chứa thống kê và danh sách lỗi, in kết quả.

**No Note — Không chú thích**

```python
amounts = [120,200,150,300,None,180,220,0,400,350,-20,280,310,130,260,140,None,230]
def summarize(values):
    accepted = []
    bad_ids = []
    for index, amount in enumerate(values, 1):
        if not isinstance(amount, (int, float)) or amount < 0:
            bad_ids.append(f"G{index:02d}")
        else:
            accepted.append(amount)
    total = sum(accepted)
    if accepted:
        average = total / len(accepted)
    else:
        average = None
    return len(accepted), total, average, bad_ids

count, total, average, errors = summarize(amounts)
if len(amounts) != 18:
    raise ValueError("Cần đủ 18 giao dịch để thống kê.")
print("Giao dịch:", len(amounts))
print("Hợp lệ:", count)
print("Tổng (nghìn đồng):", total)
print(f"Trung bình (nghìn đồng): {average:.1f}")
print("Cần sửa:", ", ".join(errors))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Viết hàm trả nhiều kết quả thống kê trên 18 giao dịch có lỗi.
# Dữ liệu: 18 khoản tiền nghìn đồng, None và số âm là không hợp lệ.
amounts = [120,200,150,300,None,180,220,0,400,350,-20,280,310,130,260,140,None,230]
# Hàm nhận một list giao dịch và trả số lượng, tổng, trung bình và mã lỗi.
def summarize(values):
    accepted = []
    bad_ids = []
    # enumerate(...,1) tạo mã giao dịch G01..G18.
    for index, amount in enumerate(values, 1):
        # not isinstance() nhận khoản không phải số; or nhận số âm.
        if not isinstance(amount, (int, float)) or amount < 0:
            # append() thêm một phần tử vào cuối danh sách và cập nhật danh sách gốc.
            # Định dạng f-string :02d cho số thứ tự thành 2 chữ số với số 0 bổ sung.
            bad_ids.append(f"G{index:02d}")
        else:
            # append() thêm một phần tử vào cuối danh sách và cập nhật danh sách gốc.
            accepted.append(amount)
    # sum() cộng tiền hợp lệ, đơn vị nghìn đồng.
    total = sum(accepted)
    # List rỗng là False; kiểm trước chia để tránh chia 0.
    if accepted:
        # len() đếm số giao dịch hợp lệ; chia tổng để lấy trung bình nghìn đồng.
        average = total / len(accepted)
    else:
        # None báo không thể tính trung bình khi không có số hợp lệ.
        average = None
    # return trả một tuple 4 thành phần để tách vào count,total,average,errors.
    return len(accepted), total, average, bad_ids

count, total, average, errors = summarize(amounts)
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
if len(amounts) != 18:
    # raise báo lỗi rồi dừng luồng hiện tại nếu dữ liệu không đáp ứng yêu cầu.
    raise ValueError("Cần đủ 18 giao dịch để thống kê.")
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
print("Giao dịch:", len(amounts))
print("Hợp lệ:", count)
print("Tổng (nghìn đồng):", total)
# f-string :.1f in trung bình một chữ số thập phân (chỉ chạy khi không phải None).
print(f"Trung bình (nghìn đồng): {average:.1f}")
# join() nối các chuỗi bằng ký tự phân cách, ở đây là dấu phẩy và khoảng trắng.
print("Cần sửa:", ", ".join(errors))
```

**Kết quả khi chạy:**

```text
Giao dịch: 18
Hợp lệ: 15
Tổng (nghìn đồng): 3270
Trung bình (nghìn đồng): 218.0
Cần sửa: G05, G11, G17
```

Trường có giá trị 0 vẫn là một chi phí hợp lệ và được tính vào mẫu số. `None` và âm có nguyên nhân khác nhau nhưng đều không được đưa vào tổng của bài toán này.

### Tình huống 5 — Cấp 5: Xây pipeline các hàm xử lý 20 hóa đơn theo vùng

**Từ vựng trong mục:** **Pipeline** — chuỗi xử lý; **Reusable function** — hàm tái sử dụng; **Lambda** — hàm ngắn.

**Tình huống thực tế:** Một doanh nghiệp nhận **20 dòng hóa đơn** thuộc ba vùng **A, B, C**. Mỗi dòng ghi mã hóa đơn, vùng, giá một món tính bằng **nghìn đồng/món** và số món mua. Hóa đơn O07 chưa có giá; O15 có giá -1 nên không được tính. Kế toán muốn doanh thu của từng vùng, danh sách mã cần sửa và xác nhận cả 20 dòng đã được xem xét, kể cả những dòng không thể cộng tiền.

**Vì sao chọn cách này?** **Pipeline** nghĩa là một chuỗi bước xử lý theo thứ tự, giống kế toán nhận phiếu → kiểm tra → tính tiền → cộng báo cáo. Hàm kiểm tra quyết định một dòng có đủ giá, số lượng và thông tin vùng hay chưa. Chỉ khi hợp lệ mới nhân giá với số món để tính tiền, rồi cộng vào vùng tương ứng. Tách các bước thành hàm nhỏ giúp tìm lỗi và kiểm thử từng phần, thay vì một hàm dài vừa kiểm tra vừa tính. O07 thiếu giá và O15 có giá âm phải được ghi là lỗi, không biến thành hóa đơn 0 đồng; dù không cộng doanh thu, cả hai vẫn thuộc **20 dòng đã xét**. `lambda` trong phần sắp tên vùng chỉ hỗ trợ thứ tự in, không được làm đổi tổng doanh thu.

**Quy trình:**
1. Định nghĩa `valid_order` kiểm tra dữ liệu có giá/số lượng hợp lệ.
2. Tạo hàm `amount` tính doanh thu dòng và hàm `report` gom theo vùng.
3. Xử lý 20 hóa đơn, in số hợp lệ, mã lỗi và doanh thu đúng đơn vị.

**No Note — Không chú thích**

```python
orders = [{"id":"O01","area":"A","price":50,"qty":1},{"id":"O02","area":"B","price":60,"qty":2},{"id":"O03","area":"C","price":70,"qty":3},{"id":"O04","area":"A","price":80,"qty":4},{"id":"O05","area":"B","price":90,"qty":1},{"id":"O06","area":"C","price":50,"qty":2},{"id":"O07","area":"A","price":None,"qty":3},{"id":"O08","area":"B","price":70,"qty":4},{"id":"O09","area":"C","price":80,"qty":1},{"id":"O10","area":"A","price":90,"qty":2},{"id":"O11","area":"B","price":50,"qty":3},{"id":"O12","area":"C","price":60,"qty":4},{"id":"O13","area":"A","price":70,"qty":1},{"id":"O14","area":"B","price":80,"qty":2},{"id":"O15","area":"C","price":-1,"qty":3},{"id":"O16","area":"A","price":50,"qty":4},{"id":"O17","area":"B","price":60,"qty":1},{"id":"O18","area":"C","price":70,"qty":2},{"id":"O19","area":"A","price":80,"qty":3},{"id":"O20","area":"B","price":90,"qty":4}]
def valid_order(order):
    return isinstance(order["price"], (int, float)) and order["price"] >= 0 and order["qty"] > 0

def amount(order):
    return order["price"] * order["qty"]

def report(items):
    totals = {"A": 0, "B": 0, "C": 0}
    invalid = []
    for order in items:
        if valid_order(order):
            totals[order["area"]] += amount(order)
        else:
            invalid.append(order["id"])
    return totals, invalid

totals, invalid = report(orders)
if len(orders) != 20:
    raise ValueError("Cần đủ 20 hóa đơn.")
if len(orders) - len(invalid) != 18:
    raise ValueError("Số hóa đơn hợp lệ phải bằng 18.")
print("Số hóa đơn:", len(orders))
print("Hợp lệ:", len(orders) - len(invalid))
print("Cần sửa:", ", ".join(invalid))
for area in sorted(totals, key=lambda name: name):
    print(f"Vùng {area} (nghìn đồng): {totals[area]}")
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tách thành các hàm xác minh đơn, tính tiền và tổng hợp 20 hóa đơn theo vùng.
# Dữ liệu: 20 dict đơn: id, area A/B/C, price (nghìn đồng), qty (món).
orders = [{"id":"O01","area":"A","price":50,"qty":1},{"id":"O02","area":"B","price":60,"qty":2},{"id":"O03","area":"C","price":70,"qty":3},{"id":"O04","area":"A","price":80,"qty":4},{"id":"O05","area":"B","price":90,"qty":1},{"id":"O06","area":"C","price":50,"qty":2},{"id":"O07","area":"A","price":None,"qty":3},{"id":"O08","area":"B","price":70,"qty":4},{"id":"O09","area":"C","price":80,"qty":1},{"id":"O10","area":"A","price":90,"qty":2},{"id":"O11","area":"B","price":50,"qty":3},{"id":"O12","area":"C","price":60,"qty":4},{"id":"O13","area":"A","price":70,"qty":1},{"id":"O14","area":"B","price":80,"qty":2},{"id":"O15","area":"C","price":-1,"qty":3},{"id":"O16","area":"A","price":50,"qty":4},{"id":"O17","area":"B","price":60,"qty":1},{"id":"O18","area":"C","price":70,"qty":2},{"id":"O19","area":"A","price":80,"qty":3},{"id":"O20","area":"B","price":90,"qty":4}]
# Hàm kiểm tra giá là số không âm và số lượng món dương.
def valid_order(order):
    # isinstance() loại giá None; and chỉ xét so sánh số tiền và số lượng khi kiểu đúng.
    return isinstance(order["price"], (int, float)) and order["price"] >= 0 and order["qty"] > 0

# Hàm trả tiền đơn = giá (nghìn đồng) nhân số lượng.
def amount(order):
    # Nhân đơn giá nghìn đồng với số lượng để ra tiền hóa đơn cùng đơn vị.
    return order["price"] * order["qty"]

# Hàm gom tổng tiền từng vùng và danh sách mã lỗi.
def report(items):
    # Dictionary dùng mã vùng A/B/C làm khóa; số tiền ban đầu là 0.
    totals = {"A": 0, "B": 0, "C": 0}
    invalid = []
    for order in items:
        # Chỉ cộng hóa đơn qua được kiểm tra giá/số lượng.
        if valid_order(order):
            # += cộng tiền đơn vào đúng mã vùng.
            totals[order["area"]] += amount(order)
        else:
            # append() lưu mã hóa đơn sai để báo sửa.
            invalid.append(order["id"])
    # Trả hai kết quả cùng lúc bằng tuple để bên ngoài tách.
    return totals, invalid

totals, invalid = report(orders)
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
if len(orders) != 20:
    # raise báo lỗi rồi dừng luồng hiện tại nếu dữ liệu không đáp ứng yêu cầu.
    raise ValueError("Cần đủ 20 hóa đơn.")
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
if len(orders) - len(invalid) != 18:
    # raise báo lỗi rồi dừng luồng hiện tại nếu dữ liệu không đáp ứng yêu cầu.
    raise ValueError("Số hóa đơn hợp lệ phải bằng 18.")
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
print("Số hóa đơn:", len(orders))
# len() trả số phần tử, dùng để đếm hoặc kiểm tra đủ bản ghi.
print("Hợp lệ:", len(orders) - len(invalid))
# join() nối các chuỗi bằng ký tự phân cách, ở đây là dấu phẩy và khoảng trắng.
print("Cần sửa:", ", ".join(invalid))
# sorted() tạo danh sách mã vùng theo thứ tự chữ cái; lambda name:name dùng chính chuỗi làm khóa.
for area in sorted(totals, key=lambda name: name):
    print(f"Vùng {area} (nghìn đồng): {totals[area]}")
```

**Kết quả khi chạy:**

```text
Số hóa đơn: 20
Hợp lệ: 18
Cần sửa: O07, O15
Vùng A (nghìn đồng): 1060
Vùng B (nghìn đồng): 1220
Vùng C (nghìn đồng): 770
```

Đây là ví dụ tích hợp: mỗi hàm làm một việc, phép biến đổi dễ kiểm thử. Giá âm và thiếu được tách riêng trước khi tổng doanh thu theo vùng.

## 6. Sai lầm thường gặp

- `return` trả giá trị về chỗ gọi hàm; nếu muốn thấy giá trị trên màn hình thì gọi `print()`.
- Tham số mặc định như `rate=0.10` được dùng khi không truyền giá trị khác vào.
- `lambda` phù hợp biểu thức ngắn, còn xử lý nhiều bước nên dùng `def` cho dễ đọc.
- Hàm tính trung bình cần xử lý danh sách rỗng trước khi chia cho `len(values)`.
- Khi sắp xếp bản ghi, phải chọn đúng trường dữ liệu trong `key`.
- Không dùng trực tiếp biến cục bộ của hàm từ bên ngoài; đưa dữ liệu cần dùng ra ngoài bằng `return`.

## 7. Trắc nghiệm

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is a Python function? | Hàm Python là gì?**

A. Only a variable declared at module level | Chỉ biến khai báo ở cấp module

B. Only code that prints text | Chỉ mã in văn bản

C. Only a loop executed once | Chỉ vòng lặp chạy một lần

D. Reusable callable code that can accept inputs | Phần mã có thể gọi lại, có thể nhận đầu vào

**Đáp án: D**

**Giải thích:** Hàm Python là phần mã có thể gọi lại nhiều lần, có thể nhận đầu vào và trả kết quả. Hàm thường có thể định nghĩa bằng `def`, còn `lambda` cũng tạo hàm từ một biểu thức; không phải mọi hàm đều bắt buộc có tên.


**Q2. What is a parameter? | Tham số là gì?**

A. A value supplied by the caller | Giá trị truyền từ nơi gọi

B. A name declared in a function's definition | Tên khai báo trong định nghĩa hàm

C. The value printed by a function | Giá trị được hàm in ra

D. A variable always declared global | Biến luôn được khai báo toàn cục

**Đáp án: B**

**Giải thích:** Tham số là tên khai báo trong định nghĩa hàm để nhận đầu vào. Trong `def double(x):`, `x` là tham số, còn số `3` trong `double(3)` là đối số được truyền khi gọi.


**Q3. What is an argument? | Đối số là gì?**

A. The name in the function definition | Tên trong định nghĩa hàm

B. A keyword beginning a function body | Từ khóa bắt đầu thân hàm

C. A value supplied in a function call | Giá trị truyền khi gọi hàm

D. The result returned by a function | Kết quả hàm trả về

**Đáp án: C**

**Giải thích:** Đối số là giá trị thực tế được truyền vào khi gọi hàm. Với `double(3)`, số nguyên `3` là đối số gắn vào tham số `x`; tên tham số xuất hiện trong phần định nghĩa.


**Q4. What is a return value? | Giá trị trả về là gì?**

A. A result sent back to the caller | Kết quả gửi về nơi gọi

B. A parameter name | Tên tham số

C. The function's source-code text | Văn bản mã nguồn hàm

D. A displayed message from `print` | Thông báo hiển thị bởi `print`

**Đáp án: A**

**Giải thích:** Giá trị trả về là thông tin hàm gửi về nơi gọi qua câu lệnh `return`. Khác `print` dùng để hiển thị, `return` giúp mã gọi hàm tiếp tục sử dụng kết quả tính toán.


**Q5. Which keyword defines a normal function? | Từ khóa nào định nghĩa hàm thông thường?**

A. `return` | `return`

B. `lambda` | `lambda`

C. `if` | `if`

D. `def` | `def`

**Đáp án: D**

**Giải thích:** `def` mở đầu định nghĩa hàm có tên, tiếp theo là tham số, dấu hai chấm và thân hàm thụt lề. `lambda` tạo biểu thức hàm, còn `return` dùng bên trong thân để trả kết quả.


**Q6. Which keyword sends a value back to the caller? | Từ khóa nào trả giá trị về nơi gọi?**

A. `lambda` | `lambda`

B. `if` | `if`

C. `def` | `def`

D. `return` | `return`

**Đáp án: D**

**Giải thích:** `return` kết thúc lần gọi hàm hiện tại và chuyển giá trị đã chỉ ra về nơi gọi. Với `return x * 2`, nơi gọi nhận giá trị gấp đôi; `print(x * 2)` chỉ hiển thị rồi trả `None`.


**Q7. Which keyword defines a short anonymous function expression? | Từ khóa nào tạo biểu thức hàm ngắn không tên?**

A. `def` | `def`

B. `return` | `return`

C. `lambda` | `lambda`

D. `if` | `if`

**Đáp án: C**

**Giải thích:** `lambda` tạo hàm từ một biểu thức, chẳng hạn `lambda x: x * 2`. Hàm có thể gán cho tên hoặc truyền làm đối số, khác `def` mở định nghĩa hàm theo dạng câu lệnh.


**Q8. Which keyword supplies a conditional branch inside a function? | Từ khóa nào tạo nhánh điều kiện bên trong hàm?**

A. `lambda` | `lambda`

B. `if` | `if`

C. `def` | `def`

D. `return` | `return`

**Đáp án: B**

**Giải thích:** `if` mở nhánh điều kiện bên trong hàm, giúp hàm chọn đường thực thi theo đầu vào. Bản thân `if` không tạo hàm và cũng không trả giá trị về nơi gọi.


**Q9. What does a default parameter provide? | Tham số mặc định có tác dụng gì?**

A. A value calculated only after the function returns | Giá trị chỉ tính sau khi hàm trả về

B. A value that must be supplied for every call | Giá trị bắt buộc phải truyền ở mọi lần gọi

C. A fallback value used when the caller omits an argument | Giá trị dự phòng khi nơi gọi không truyền đối số

D. A value that overrides every explicit argument | Giá trị ghi đè mọi đối số truyền vào

**Đáp án: C**

**Giải thích:** Giá trị mặc định của tham số được dùng khi nơi gọi bỏ qua đối số đó; với `def greet(name='An')`, `greet()` dùng `'An'`. Nếu gọi `greet('Binh')` thì giá trị truyền vào thay mặc định, vì vậy đây là dự phòng chứ không phải giá trị bắt buộc.


**Q10. What is a keyword argument? | Đối số theo tên là gì?**

A. An argument supplied using its parameter's name | Đối số truyền bằng tên tham số

B. A local variable defined outside the function | Biến cục bộ định nghĩa ngoài hàm

C. A function name passed without calling | Tên hàm được truyền mà không gọi

D. An argument always matched only by position | Đối số luôn ghép bằng vị trí

**Đáp án: A**

**Giải thích:** Đối số theo tên nêu rõ tên tham số lúc gọi, ví dụ `greet(name='An')`. Nó khác đối số theo vị trí như `greet('An')`, vốn ghép với tham số dựa trên vị trí truyền vào.


**Q11. What does `sorted(rows, key=func)` use `func` for? | Trong `sorted(rows, key=func)`, func dùng để làm gì?**

A. Filtering out all false-valued items before sorting | Loại mọi phần tử có giá trị sai trước khi sắp

B. Computing a sort key for each item | Tính khóa sắp xếp cho từng phần tử

C. Replacing every row with `None` | Thay mỗi hàng bằng `None`

D. Printing each row during sorting | In từng hàng trong lúc sắp

**Đáp án: B**

**Giải thích:** Trong `sorted(rows, key=func)`, `func` tính giá trị khóa so sánh cho từng phần tử; phép sắp xếp dùng các khóa đó. Ví dụ `key=len` sẽ ưu tiên chuỗi ngắn trước theo độ dài thay vì thứ tự chữ cái.


**Q12. What does `filter(test, items)` keep? | `filter(test, items)` giữ gì?**

A. Only items whose test result is false | Chỉ phần tử có kết quả kiểm tra sai

B. Items in descending order | Phần tử theo thứ tự giảm dần

C. Items for which `test(item)` is truthy | Phần tử mà `test(item)` có giá trị đúng

D. All items, regardless of the test | Mọi phần tử, bất kể phép kiểm tra

**Đáp án: C**

**Giải thích:** `filter(test, items)` chọn phần tử mà `test(item)` có giá trị đúng, trả iterator trong Python 3. Với `filter(lambda x: x > 0, [-1,2])`, chuyển sang `list` được `[2]`, không phải mọi phần tử ban đầu.


**Q13. What is a local variable? | Biến cục bộ là gì?**

A. Any name defined at module level | Bất kỳ tên nào khai báo cấp module

B. A name automatically shared by every function | Tên tự chia sẻ cho mọi hàm

C. A name that can never change value | Tên không bao giờ đổi giá trị

D. A name bound within a function's local scope | Tên được gán trong phạm vi cục bộ hàm

**Đáp án: D**

**Giải thích:** Biến cục bộ là tên được gán trong phạm vi cục bộ của hàm, như `total` gán trong `def add():`. Nó không tự tồn tại ngoài hàm, khác tên toàn cục khai báo ở cấp module.


**Q14. What is a global variable? | Biến toàn cục là gì?**

A. A name bound at module level | Tên được gán ở cấp module

B. A name that exists only inside a class | Tên chỉ tồn tại trong class

C. A name inaccessible to all functions | Tên mọi hàm đều không truy cập được

D. A name created only by `lambda` | Tên chỉ do `lambda` tạo

**Đáp án: A**

**Giải thích:** Biến toàn cục là tên được gán ở cấp module và thường có thể đọc trong hàm nếu không bị che khuất. Muốn gán lại chính biến toàn cục từ trong hàm thường phải khai báo `global`, khác việc chỉ đọc giá trị.


**Q15. What is a lambda expression limited to? | Nội dung của lambda bị giới hạn như thế nào?**

A. A complete `try/except` statement block | Khối câu lệnh `try/except` đầy đủ

B. A single expression | Một biểu thức

C. Only a numeric literal | Chỉ một literal số

D. A series of ordinary statements | Chuỗi các câu lệnh thông thường

**Đáp án: B**

**Giải thích:** Thân `lambda` trong Python chỉ chứa một biểu thức và giá trị biểu thức trở thành kết quả hàm. Nó không chứa khối nhiều câu lệnh thông thường như chuỗi lệnh `for` và gán; cần dùng `def` trong trường hợp đó.


**Q16. What is a closure? | Closure là gì?**

A. A function forced to return `None` | Hàm bị buộc trả `None`

B. A function that prints its enclosing scope | Hàm in phạm vi bao ngoài

C. A function that discards all free variables | Hàm loại bỏ mọi biến tự do

D. A function whose enclosing names remain accessible | Hàm vẫn truy cập được tên của phạm vi bao ngoài

**Đáp án: D**

**Giải thích:** Closure là hàm vẫn truy cập được các tên thuộc phạm vi bao ngoài, kể cả sau khi hàm ngoài đã trả về. Nó giữ liên kết tham chiếu tới các tên đó chứ không nhất thiết chụp cố định giá trị tại một thời điểm.


**Q17. When a function reaches its end without executing `return`, what value does it return? | Khi hàm chạy đến cuối mà không thực hiện `return`, nó trả giá trị nào?**

A. `None` | `None`

B. An empty string `''` | Chuỗi rỗng `''`

C. The last local variable | Biến cục bộ cuối

D. `NameError` | `NameError`

**Đáp án: A**

**Giải thích:** Nếu hàm chạy đến cuối mà không có `return` tường minh, Python ngầm trả `None`. Hàm vẫn có thể in thông báo nhưng việc in không biến thông báo đó thành giá trị trả về.


**Q18. What does `print()` do instead of returning a useful result? | `print()` làm gì thay vì trả một kết quả để tính tiếp?**

A. Displays output while returning `None` | Hiển thị đầu ra và trả `None`

B. Returns a tuple with the printed text | Trả Tuple chứa văn bản đã in

C. Raises `TypeError` whenever called | Mỗi khi gọi đều gây `TypeError`

D. Always returns the printed string | Luôn trả chuỗi đã in

**Đáp án: A**

**Giải thích:** `print()` đưa văn bản ra đầu ra chuẩn và giá trị trả về là `None`. Ví dụ `result = print('Hi')` hiển thị `Hi` nhưng lưu `None` vào `result`; dùng `return` trong hàm nếu mã phía sau cần kết quả.


**Q19. What does a function's `return a, b` actually return? | `return a, b` thực chất trả gì?**

A. The result of adding `a` and `b` | Kết quả cộng `a` với `b`

B. A tuple containing both values | Tuple chứa cả hai giá trị

C. A list containing both values | List chứa cả hai giá trị

D. The two values as separate function return objects | Hai giá trị thành hai đối tượng trả về riêng

**Đáp án: B**

**Giải thích:** Biểu thức trả về có các giá trị cách nhau bằng dấu phẩy đóng gói chúng thành Tuple, nên `return a, b` trả `(a, b)`. Nơi gọi có thể giải nén ra hai tên, nhưng hàm thực tế trả một đối tượng Tuple.


**Q20. What happens when code outside a function reads an undefined local name? | Đọc biến cục bộ không tồn tại ở ngoài hàm gây gì?**

A. The most recent printed value is used | Dùng giá trị vừa được in

B. The local name is exported automatically | Tên cục bộ tự xuất ra ngoài

C. `NameError` for the undefined name | `NameError` vì tên chưa được định nghĩa

D. `None` is silently substituted | Tự thay bằng `None`

**Đáp án: C**

**Giải thích:** Tên cục bộ chỉ được gán bên trong hàm không tự tồn tại ở phạm vi module. Đọc tên chưa được định nghĩa ở ngoài gây `NameError`; cần trả về tường minh hoặc lưu vào liên kết có thể truy cập.

## 8. Nối sang bài tiếp theo

`Vòng lặp → Hàm → OOP → Pipeline`.

# PY-10 — Class, Object, constructor và đóng gói


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Class** — lớp; **Object** — đối tượng.

`Hàm / Dictionary → OOP → Kế thừa`

**Học xong dùng để làm gì?** Thiết kế đối tượng học viên hoặc tài khoản với thuộc tính, phương thức và kiểm tra đầu vào.

**Kết nối kiến thức tiếp theo:** PY-11 mở rộng các loại đối tượng bằng kế thừa và ghi đè phương thức.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Ý nghĩa |
|---|---|---|
| Class | lớp | Khuôn mô tả dữ liệu và cách xử lý |
| Object | đối tượng | Một thể hiện cụ thể của lớp |
| Constructor | hàm khởi tạo | Thiết lập thuộc tính lúc tạo instance |
| Encapsulation | đóng gói | Đặt dữ liệu và hành vi bên trong đối tượng |

## 3. Thư viện, hàm và tham số

**Từ vựng trong mục:** **Function** — hàm; **Parameter** — tham số.

| Hàm/cú pháp | Giải thích và lý do dùng |
|---|---|
| `class Name:` | Định nghĩa kiểu đối tượng và các phương thức |
| `__init__(self, ...)` | Khởi tạo trạng thái của từng instance |
| `self.attribute` | Truy cập thuộc tính thuộc về chính đối tượng |
| `__str__/set_*/get_*` | Hiển thị và kiểm tra thao tác thay đổi giá trị |


## 4. Khái niệm liên quan

**Lập trình hướng đối tượng (OOP)** giúp gom **dữ liệu của một đối tượng** và **những thao tác dùng dữ liệu ấy** vào cùng một cấu trúc. Ví dụ một học viên có tên, điểm và cách hiển thị hồ sơ; thay vì đặt các biến rời rạc, ta tạo một lớp `Student`. Từ lớp này, bài học lần lượt giải thích class, object, `__init__`, `self` và cách đóng gói thao tác thay đổi dữ liệu.

### 4.1. Class — Khuôn mẫu đối tượng

**Từ vựng trong mục:** **Class** — lớp; **Method** — phương thức.

**Class** giống bản thiết kế: định nghĩa những việc các đối tượng cùng loại có thể thực hiện. Ví dụ lớp `Student` có phương thức `greet()` trả một lời chào. Dòng `class Student:` tạo bản thiết kế, `def greet(self)` định nghĩa hành động; `self` đại diện cho đối tượng cụ thể đang gọi phương thức. Chỉ viết class chưa tạo hồ sơ học viên nào; `Student()` ở cuối mới tạo một đối tượng để gọi `greet()`.

```python
# Mục đích: Khuôn mẫu đối tượng.
class Student:
    def greet(self):
        return 'Xin chào'

student = Student()
print(student.greet())
```

**Kết quả khi chạy:**

```text
Xin chào
```

Đối tượng `student` gọi phương thức được định nghĩa bên trong lớp `Student`.

### 4.2. Object — Mỗi học viên là một đối tượng

**Từ vựng trong mục:** **Object** — đối tượng; **Attribute** — thuộc tính.

**Object** là một thể hiện được tạo từ class. Cùng một mẫu `Student`, ta có thể tạo hai học viên An và Lan, mỗi người có tên riêng. Thuộc tính `self.name` lưu tên **trên từng đối tượng**, vì vậy thay tên của An không tự thay tên của Lan. Ta dùng dấu chấm `student.name` để lấy một thuộc tính.

```python
# Mục đích: Mỗi học viên là một đối tượng.
class Student:
    def __init__(self, name):
        self.name = name

a = Student('An')
b = Student('Lan')
print(a.name, b.name)
```

**Kết quả khi chạy:**

```text
An Lan
```

Cả `a` và `b` đều thuộc lớp Student, nhưng chứa dữ liệu tên riêng.

### 4.3. Constructor và self — Khởi tạo trạng thái

**Từ vựng trong mục:** **Constructor** — bước khởi tạo; **__init__** — phương thức khởi tạo; **self** — chính đối tượng.

Khi tạo `Student('An', 8)`, Python tạo đối tượng mới rồi tự gọi `__init__` để thiết lập tên và điểm ban đầu. Tham số `self` là đối tượng vừa được tạo; `name` và `score` nhận đối số truyền khi gọi. Lệnh `self.score = score` lưu điểm bên trong học viên, không chỉ trong biến tạm của hàm. Điểm ở đây tính trên thang 10.

```python
# Mục đích: Khởi tạo trạng thái.
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

student = Student('An', 8)
print(student.name, student.score)
```

**Kết quả khi chạy:**

```text
An 8
```

Phương thức `__init__` đưa dữ liệu đầu vào thành hai thuộc tính của cùng hồ sơ học viên.

### 4.4. Encapsulation — Đóng gói dữ liệu và quy tắc xử lý

**Từ vựng trong mục:** **Encapsulation** — đóng gói; **Method** — phương thức; **Validation** — kiểm tra hợp lệ.

**Đóng gói** nghĩa là quản lý dữ liệu cùng các thao tác tác động lên nó trong lớp. Ví dụ điểm chỉ được phép trong khoảng 0–10: lớp `Score` lưu số hiện tại tại `self._value` và có phương thức `set_value()` kiểm tra trước khi cập nhật. Dấu `_` là **quy ước** nhắc người lập trình không nên sửa trực tiếp, không phải cơ chế cấm truy cập tuyệt đối. Đọc điểm qua `get_value()` giúp giữ cùng một cách sử dụng.

```python
# Mục đích: Đóng gói dữ liệu và quy tắc xử lý.
class Score:
    def __init__(self):
        self._value = 0

    def set_value(self, x):
        if not 0 <= x <= 10:
            raise ValueError('Điểm ngoài khoảng 0–10')
        self._value = x

    def get_value(self):
        return self._value

score = Score()
score.set_value(9)
print(score.get_value())
```

**Kết quả khi chạy:**

```text
9
```

Điểm 9 hợp lệ nên được lưu và đọc lại. Với điểm 11, `set_value` sẽ báo `ValueError` thay vì ghi dữ liệu sai.
## 5. Năm tình huống OOP — từ đối tượng đến quản lý trạng thái

### Tình huống 1 — Cấp 1: Tạo 10 đối tượng học viên có trạng thái riêng

**Từ vựng trong mục:** **Class** — lớp; **Object** — đối tượng; **Constructor** — hàm khởi tạo.

**Tình huống thực tế:** Một lớp học có **10 học viên** mã S01…S10 với điểm theo thang 10. Giáo viên muốn tạo đối tượng cho từng người, rồi đọc điểm S01 và S10 mà không phải lưu riêng mười biến điểm.

**Vì sao chọn cách này?** Lớp Student gom mã và điểm vào `self`; mỗi lần gọi `Student(...)` tạo một đối tượng riêng. Đây là mức nhập môn OOP, chỉ khởi tạo và đọc thuộc tính.

**Quy trình:**
1. Định nghĩa lớp có hàm `__init__` lưu mã và điểm.
2. Tạo 10 đối tượng từ bảng điểm, mỗi hàng là một người.
3. In số đối tượng và điểm đầu/cuối.

```python
scores = [8,7,9,6,8.5,10,4,7.5,6.5,9.5]
class Student:
    def __init__(self, code, score):
        self.code = code
        self.score = score

students = [Student(f"S{i:02d}", score) for i, score in enumerate(scores, 1)]
assert len(students) == 10
print("Học viên:", len(students))
print("S01:", students[0].score)
print("S10:", students[-1].score)
```

**Kết quả khi chạy:**

```text
Học viên: 10
S01: 8
S10: 9.5
```

Thuộc tính `self.score` thuộc về từng đối tượng, không phải biến dùng chung cho toàn bộ lớp.

### Tình huống 2 — Cấp 2: Giỏ hàng có phương thức add và total cho 12 món

**Từ vựng trong mục:** **Method** — phương thức; **Self** — đối tượng hiện tại; **Encapsulation** — đóng gói.

**Tình huống thực tế:** Một khách chọn **12 mặt hàng**, mỗi dòng là đơn giá (nghìn đồng/món), mua mỗi loại một món. Bộ phận thu ngân cần đối tượng `Cart` tự quản lý danh sách giá và đưa ra tổng tiền, không để bên ngoài phải tự cộng giá.

**Vì sao chọn cách này?** Phương thức `add()` phụ trách thay đổi danh sách của đúng giỏ hàng, `total()` trả kết quả; danh sách giá được tạo **bên trong** `__init__` nên không bị chia sẻ giữa nhiều giỏ.

**Quy trình:**
1. Tạo lớp `Cart` với thuộc tính `prices` khởi tạo riêng.
2. Lần lượt gọi `add()` với 12 đơn giá.
3. Gọi `total()` và kiểm tra một giỏ mới không chứa hàng cũ.

```python
prices = [20,30,10,15,40,25,35,20,30,10,50,45]
class Cart:
    def __init__(self):
        self.prices = []
    def add(self, price):
        self.prices.append(price)
    def total(self):
        return sum(self.prices)

cart = Cart()
for price in prices:
    cart.add(price)
assert len(cart.prices) == 12
assert Cart().total() == 0
print("Mặt hàng:", len(cart.prices))
print("Tổng (nghìn đồng):", cart.total())
print("Giỏ mới (nghìn đồng):", Cart().total())
```

**Kết quả khi chạy:**

```text
Mặt hàng: 12
Tổng (nghìn đồng): 330
Giỏ mới (nghìn đồng): 0
```

Phương thức được gọi trên một đối tượng cụ thể; việc tạo giỏ mới không kéo theo các mặt hàng của giỏ cũ.

### Tình huống 3 — Cấp 3: Đóng gói quy tắc lưu điểm cho 15 hồ sơ

**Từ vựng trong mục:** **Setter** — phương thức gán; **Validation** — kiểm tra; **Exception** — ngoại lệ.

**Tình huống thực tế:** Phòng đào tạo nhận **15 điểm** theo thứ tự học viên S01…S15 (thang 10). Trong đó S06 đạt 11 và S10 đạt -1 là dữ liệu sai. Để tránh vô tình lưu điểm không hợp lệ, mỗi đối tượng `ScoreRecord` phải kiểm tra trong phương thức `set_score()` trước khi cập nhật.

**Vì sao chọn cách này?** Đặt quy tắc kiểm tra trong lớp để mọi lời gọi đều theo cùng ngưỡng. Khi không hợp lệ, `ValueError` ngăn đối tượng giữ điểm sai; chương trình tổng hợp bắt lỗi theo từng mã để tiếp tục xử lý các hồ sơ khác.

**Quy trình:**
1. Tạo lớp với trạng thái điểm ban đầu `None`.
2. Gọi setter với mỗi trong 15 điểm, bắt lỗi cho đúng mã hồ sơ.
3. Đếm số hồ sơ lưu được và mã cần sửa.

```python
raw_scores = [4,8,7,10,6,11,9,5,7.5,-1,0,8.5,3,9,10]
class ScoreRecord:
    def __init__(self, code):
        self.code = code
        self._score = None
    def set_score(self, value):
        if not (0 <= value <= 10):
            raise ValueError("score must be within 0..10")
        self._score = value
    def get_score(self):
        return self._score

records, errors = [], []
for index, score in enumerate(raw_scores, 1):
    record = ScoreRecord(f"S{index:02d}")
    try:
        record.set_score(score)
    except ValueError:
        errors.append(record.code)
    records.append(record)
assert len(records) == 15
print("Hồ sơ:", len(records))
print("Đã lưu điểm:", sum(rec.get_score() is not None for rec in records))
print("Sai:", ", ".join(errors))
```

**Kết quả khi chạy:**

```text
Hồ sơ: 15
Đã lưu điểm: 13
Sai: S06, S10
```

Điểm 0 là hợp lệ, khác với điểm chưa nhập (`None`). Cấp này thêm ràng buộc và xử lý lỗi mà không kết thúc toàn bộ lượt nhập.

### Tình huống 4 — Cấp 4: Định dạng 18 hóa đơn qua __str__ và xử lý tiền thiếu

**Từ vựng trong mục:** **Dunder method** — phương thức đặc biệt; **__str__** — chuỗi hiển thị; **Missing value** — giá trị thiếu.

**Tình huống thực tế:** Ứng dụng nhận **18 hóa đơn** O01…O18; mỗi dòng chứa số tiền thanh toán (đồng). Hai hóa đơn O06 và O15 chưa được nhập số tiền (`None`). Cần định nghĩa cách một đối tượng hóa đơn hiển thị, nhưng **không** hiển thị dòng thiếu như 0 đồng; báo tổng của các hóa đơn đủ tiền và hai mã cần nhập lại.

**Vì sao chọn cách này?** Phương thức `__str__()` đặt quy tắc hiển thị ở chính đối tượng. Phương thức `is_ready()` tách điều kiện được phép tính tổng; lỗi thiếu được xử lý trước khi dùng số học.

**Quy trình:**
1. Tạo đối tượng `Invoice` cho đủ 18 dòng và lưu mã/số tiền.
2. Định nghĩa `is_ready()` và `__str__()` theo trạng thái có/thiếu tiền.
3. In hóa đơn mẫu, thống kê số hợp lệ, số thiếu và tổng giá trị.

```python
amounts = [100000,125000,150000,175000,200000,None,125000,150000,175000,200000,100000,125000,150000,175000,None,100000,125000,150000]
class Invoice:
    def __init__(self, code, amount):
        self.code, self.amount = code, amount
    def is_ready(self):
        return isinstance(self.amount, (int, float)) and self.amount >= 0
    def __str__(self):
        value = f"{self.amount:,} đồng" if self.is_ready() else "Chưa có số tiền"
        return f"{self.code}: {value}"

invoices = [Invoice(f"O{i:02d}", amount) for i, amount in enumerate(amounts, 1)]
ready = [order for order in invoices if order.is_ready()]
missing = [order.code for order in invoices if not order.is_ready()]
assert len(invoices) == 18
print("Số hóa đơn:", len(invoices))
print("Sẵn sàng:", len(ready))
print("Thiếu:", ", ".join(missing))
print("Tổng (đồng):", sum(order.amount for order in ready))
print("Mẫu:", str(invoices[0]))
```

**Kết quả khi chạy:**

```text
Số hóa đơn: 18
Sẵn sàng: 16
Thiếu: O06, O15
Tổng (đồng): 2325000
Mẫu: O01: 100,000 đồng
```

Chỉ tính tổng trên các đối tượng `is_ready() == True`. Giá trị `None` là một trạng thái thiếu cần sửa, không phải số tiền 0.

### Tình huống 5 — Cấp 5: Xây đối tượng tồn kho độc lập và xử lý 20 lượt xuất

**Từ vựng trong mục:** **State** — trạng thái; **Encapsulation** — đóng gói; **Instance method** — phương thức đối tượng.

**Tình huống thực tế:** Kho có **5 sản phẩm** P01…P05 với tồn đầu ngày lần lượt 10, 9, 8, 7, 5 món. Trong ngày phát sinh **20 yêu cầu xuất**, mỗi hàng là mã sản phẩm và số món muốn lấy. Có lượt vượt số tồn, một lượt chưa có số lượng (`None`) và một lượt yêu cầu 0 món. Hãy dùng đối tượng cho từng sản phẩm để **không bao giờ cho tồn âm**, trả danh sách yêu cầu bị từ chối và số tồn cuối từng sản phẩm.

**Vì sao chọn cách này?** Đối tượng `StockItem` giữ số tồn của **một sản phẩm**; phương thức `reserve` quyết định thành công và chỉ thay đổi `self.quantity` khi đủ điều kiện. Tách trạng thái mỗi sản phẩm tránh tình trạng một yêu cầu của P01 làm thay đổi P02. Đây là bước tổng hợp OOP và kiểm tra đầu vào.

**Quy trình:**
1. Khởi tạo 5 đối tượng độc lập từ tồn đầu ngày.
2. Duyệt 20 yêu cầu theo thứ tự; `reserve()` trả True/False thay vì trừ vô điều kiện.
3. Đếm số yêu cầu thành công, ghi mã lỗi và đối chiếu tồn không âm.

```python
initial = {"P01":10,"P02":9,"P03":8,"P04":7,"P05":5}
requests = [("P01",2),("P02",1),("P03",3),("P01",4),("P02",5),("P03",2),("P04",1),("P01",3),("P03",6),("P04",3),("P02",2),("P01",7),("P05",1),("P03",1),("P04",4),("P05",2),("P01",None),("P02",0),("P04",2),("P05",8)]
class StockItem:
    def __init__(self, code, quantity):
        self.code, self.quantity = code, quantity
    def reserve(self, requested):
        if not isinstance(requested, int) or requested <= 0 or requested > self.quantity:
            return False
        self.quantity -= requested
        return True

items = {code: StockItem(code, qty) for code, qty in initial.items()}
rejected = []
for index, (code, requested) in enumerate(requests, 1):
    if not items[code].reserve(requested):
        rejected.append(f"T{index:02d}")
assert len(requests) == 20
assert all(item.quantity >= 0 for item in items.values())
print("Yêu cầu:", len(requests))
print("Chấp nhận:", len(requests) - len(rejected))
print("Từ chối:", ", ".join(rejected))
print("Tồn cuối:", ", ".join(f"{code}={items[code].quantity}" for code in sorted(items)))
```

**Kết quả khi chạy:**

```text
Yêu cầu: 20
Chấp nhận: 14
Từ chối: T09, T12, T15, T17, T18, T20
Tồn cuối: P01=1, P02=1, P03=2, P04=1, P05=2
```

Người học cần theo dõi trạng thái thay đổi **qua 20 yêu cầu nối tiếp**, không chỉ tính một đơn hàng. Khi một yêu cầu bị từ chối, tồn kho phải giữ nguyên trước khi xét yêu cầu tiếp theo.

## 6. Sai lầm thường gặp

- `class` là khuôn mẫu; đối tượng chỉ xuất hiện khi gọi lớp như `Student('An', 8)`.
- `self.name` là thuộc tính của đối tượng, không phải biến dùng chung giữa mọi học viên. Mỗi đối tượng có trạng thái riêng.
- `__init__` chuẩn bị dữ liệu ban đầu, còn `__str__` quy định cách hiển thị; hai phương thức có mục đích khác nhau.
- `self._value` dùng dấu gạch dưới theo quy ước, không tự tạo thuộc tính hoàn toàn riêng tư. Muốn bảo vệ dữ liệu cần kiểm soát cách cập nhật và kiểm tra hợp lệ.
- Điểm vượt 0–10 sẽ phát sinh `ValueError` trong ví dụ `Score`; không bỏ qua xử lý lỗi ở chương trình thực tế.

## 7. Trắc nghiệm

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is a class in Python OOP? | Class trong OOP Python là gì?**

A. Only a built-in Python function | Chỉ một hàm Python có sẵn

B. A template defining object state and behavior | Khuôn mẫu định nghĩa trạng thái và hành vi đối tượng

C. A concrete instance created from a class | Instance cụ thể được tạo từ class

D. A value stored in one object | Giá trị lưu trong một đối tượng

**Đáp án: B**

**Giải thích:** Class định nghĩa cấu trúc dùng chung cho các đối tượng, gồm thuộc tính và phương thức. Ví dụ class `Student` có thể định nghĩa trường tên và phương thức `display()`; từng sinh viên là một instance của class đó.


**Q2. What is an object or instance? | Object hay instance là gì?**

A. A statement defining a new class | Câu lệnh định nghĩa class mới

B. A concrete instance of a class | Instance cụ thể của class

C. An attribute name only | Chỉ tên thuộc tính

D. A block of import statements | Khối lệnh import

**Đáp án: B**

**Giải thích:** Object hay instance là giá trị cụ thể được tạo từ class. Hai instance `Student` có thể chạy cùng các phương thức nhưng có giá trị `name` khác nhau, vì thế class không đồng nghĩa với một đối tượng.


**Q3. What is an attribute? | Attribute là gì?**

A. A method invocation | Lời gọi phương thức

B. Data or a value associated with an object | Dữ liệu hoặc giá trị gắn với đối tượng

C. A syntax token beginning every class | Token cú pháp bắt đầu mọi class

D. A class declaration | Câu lệnh khai báo class

**Đáp án: B**

**Giải thích:** Attribute là dữ liệu hoặc giá trị gắn với đối tượng được truy cập qua tên, như `student.name`. Nó biểu diễn trạng thái hay đặc điểm, còn phương thức được gọi để thực hiện hành vi.


**Q4. What is an instance method? | Phương thức đối tượng là gì?**

A. An object stored in a list | Đối tượng được lưu trong List

B. A value that cannot be called | Giá trị không thể gọi

C. A class-defined function operating on an instance | Hàm định nghĩa trong class thao tác trên instance

D. A class with no methods | Class không có phương thức

**Đáp án: C**

**Giải thích:** Phương thức instance là hàm định nghĩa trong class và nhận đối tượng làm đối số đầu khi gọi qua instance. Với `student.show()`, phương thức có thể đọc `self.name`; thuộc tính như `student.name` là dữ liệu, không phải lời gọi phương thức.


**Q5. Which syntax begins a class definition? | Cú pháp nào mở đầu định nghĩa class?**

A. `__init__` | `__init__`

B. `self` | `self`

C. `class Student:` | `class Student:`

D. `Student()` | `Student()`

**Đáp án: C**

**Giải thích:** `class Student:` mở đầu định nghĩa class; các lệnh thụt lề bên dưới tạo thân class. Gọi `Student()` là thao tác khác: tạo instance sau khi class phù hợp đã được định nghĩa.


**Q6. If `Student` requires no constructor arguments, which expression creates a Student instance? | Nếu `Student` không yêu cầu đối số khởi tạo, biểu thức nào tạo một instance Student?**

A. `Student()` | `Student()`

B. `def Student:` | `def Student:`

C. `self.Student` | `self.Student`

D. `class Student:` | `class Student:`

**Đáp án: A**

**Giải thích:** Gọi `Student()` tạo instance nếu class có thể khởi tạo mà không cần đối số bắt buộc. Nếu `__init__` yêu cầu đầu vào khác thì phải truyền chúng khi gọi, không được cho rằng ngoặc trống luôn hợp lệ.


**Q7. Which special method initializes instance attributes? | Phương thức đặc biệt nào khởi tạo thuộc tính đối tượng?**

A. `__repr__` | `__repr__`

B. `__newstate__` | `__newstate__`

C. `__str__` | `__str__`

D. `__init__` | `__init__`

**Đáp án: D**

**Giải thích:** `__init__` khởi tạo instance vừa được tạo, thường gán thuộc tính như `self.name = name`. Python tạo đối tượng trước rồi mới gọi hàm khởi tạo; bản thân `__init__` không thực hiện cấp phát đối tượng.


**Q8. What does `self` refer to in an instance method? | `self` trong phương thức đối tượng chỉ gì?**

A. The class object, never an instance | Đối tượng class, không bao giờ là instance

B. The first attribute value | Giá trị thuộc tính đầu tiên

C. A newly created unrelated object | Đối tượng khác vừa được tạo

D. The instance receiving the method call | Instance nhận lời gọi phương thức

**Đáp án: D**

**Giải thích:** Trong phương thức instance thông thường, `self` chỉ đối tượng cụ thể nhận lời gọi. Vì vậy `a.show()` và `b.show()` có thể đọc các thuộc tính khác nhau qua `self` dù cùng định nghĩa class.


**Q9. What does `self.name = name` do? | `self.name = name` làm gì?**

A. Stores `name` on the current instance | Lưu `name` trên instance hiện tại

B. Sets the same name on all instances | Đặt cùng tên trên mọi instance

C. Changes the class's name | Đổi tên class

D. Calls a method named `name` | Gọi phương thức tên `name`

**Đáp án: A**

**Giải thích:** `self.name = name` gán giá trị tham số `name` cho thuộc tính của instance hiện tại. Vì vậy mỗi đối tượng có thể mang tên khác nhau; lệnh không tạo một thuộc tính cấp class được dùng chung.


**Q10. What does `__str__` normally customize? | `__str__` thường tùy chỉnh điều gì?**

A. The readable string representation of an object | Biểu diễn chuỗi dễ đọc của đối tượng

B. The list of all class attributes | Danh sách mọi thuộc tính class

C. The class inheritance hierarchy | Hệ phân cấp kế thừa class

D. The instance's constructor arguments | Các đối số khởi tạo instance

**Đáp án: A**

**Giải thích:** `__str__` điều khiển chuỗi dễ đọc trả về từ `str(obj)` và thường được `print(obj)` hiển thị. Phương thức này phải trả một chuỗi thay vì tự in trực tiếp; nó khác `__init__` dùng để khởi tạo trạng thái.


**Q11. What does `raise ValueError(...)` do? | `raise ValueError(...)` làm gì?**

A. Raises an exception for an invalid value | Phát sinh ngoại lệ cho giá trị không hợp lệ

B. Marks an attribute private | Đánh dấu thuộc tính riêng tư

C. Converts invalid values to `None` | Chuyển giá trị sai thành `None`

D. Silently ignores invalid data | Lặng lẽ bỏ qua dữ liệu sai

**Đáp án: A**

**Giải thích:** `raise ValueError(...)` báo giá trị đầu vào không hợp lệ và ngắt luồng bình thường bằng một ngoại lệ. Ví dụ setter có thể từ chối tuổi âm thay vì lặng lẽ lưu trạng thái không hợp lý.


**Q12. What does the prefix `_value` conventionally mean? | Tiền tố `_value` theo quy ước có nghĩa gì?**

A. A constant that cannot be changed | Hằng không thể thay đổi

B. An attribute invisible to external code | Thuộc tính mã ngoài không thể thấy

C. An internal-use detail by convention | Chi tiết sử dụng nội bộ theo quy ước

D. An automatically encrypted value | Giá trị được tự động mã hóa

**Đáp án: C**

**Giải thích:** Một dấu gạch dưới đầu tên như `_value` theo quy ước đánh dấu chi tiết nội bộ. Python không thực thi tính riêng tư chỉ nhờ cách đặt tên này, nên mã bên ngoài vẫn có thể đọc thuộc tính nếu nó tồn tại.


**Q13. What is encapsulation? | Đóng gói trong OOP là gì?**

A. Copying every attribute into a global variable | Sao chép mọi thuộc tính sang biến toàn cục

B. Converting methods into strings | Chuyển phương thức thành chuỗi

C. Creating a new instance on every access | Tạo instance mới mỗi lần truy cập

D. Grouping related data and methods | Gom dữ liệu và phương thức liên quan

**Đáp án: D**

**Giải thích:** Đóng gói gom dữ liệu và các thao tác liên quan vào cùng class hoặc giao diện đối tượng. Ví dụ phương thức của `BankAccount` có thể cập nhật số dư kèm kiểm tra thay vì để mọi nơi gọi tự sửa các biến rời rạc.


**Q14. Why validate values in a setter method? | Vì sao kiểm tra dữ liệu trong setter?**

A. To make every instance share its private data | Buộc mọi instance chia sẻ dữ liệu riêng

B. To prevent all future method calls | Ngăn mọi lời gọi phương thức sau đó

C. To bypass all input validation | Bỏ qua toàn bộ kiểm tra dữ liệu

D. To validate inputs and preserve valid object state | Kiểm tra đầu vào và giữ trạng thái hợp lệ

**Đáp án: D**

**Giải thích:** Setter kiểm tra dữ liệu trước khi thay đổi trạng thái đối tượng, giúp giữ các ràng buộc như tuổi không được âm. Nếu thiếu kiểm tra, nơi gọi có thể lưu giá trị sai khiến phương thức khác hoạt động không đúng.


**Q15. How do two instances of the same class relate? | Hai đối tượng cùng class có quan hệ gì?**

A. They always share all instance attribute values | Chúng luôn dùng chung mọi giá trị thuộc tính instance

B. They cannot invoke the same methods | Chúng không thể gọi cùng phương thức

C. They share class behavior but can have different states | Chúng chia sẻ hành vi class nhưng có trạng thái khác nhau

D. They are the same object in memory | Chúng là cùng một đối tượng trong bộ nhớ

**Đáp án: C**

**Giải thích:** Các instance cùng class dùng chung định nghĩa phương thức nhưng có thể chứa các thuộc tính instance riêng. Nếu `a.name='An'` và `b.name='Binh'`, sửa `a.name` không tự thay đổi `b.name`.


**Q16. What is a class attribute? | Thuộc tính cấp class là gì?**

A. A method's local variable | Biến cục bộ của phương thức

B. An attribute defined on the class and found by lookup | Thuộc tính định nghĩa trên class và được tìm bằng tra cứu

C. An attribute defined on an object instance only | Thuộc tính chỉ định nghĩa trên instance

D. A required parameter of `__init__` | Tham số bắt buộc của `__init__`

**Đáp án: B**

**Giải thích:** Thuộc tính cấp class được khai báo trên class thay vì riêng từng instance và được tìm thấy khi tra cứu qua class hoặc instance. Instance có thể che khuất thuộc tính đó bằng giá trị riêng, nên đây không phải trường luôn đồng bộ vĩnh viễn.


**Q17. What does `obj.method()` do? | `obj.method()` làm gì?**

A. Invokes a method on `obj` | Gọi phương thức trên `obj`

B. Returns the object's class without invoking anything | Trả class của đối tượng mà không gọi gì

C. Always creates a new instance | Luôn tạo instance mới

D. Always deletes an attribute | Luôn xóa thuộc tính

**Đáp án: A**

**Giải thích:** `obj.method()` tìm và gọi phương thức có tên trên `obj`, thông thường truyền instance đó làm `self`. Chỉ đọc `obj.attribute` thì lấy giá trị, không tự gọi phương thức.


**Q18. When the attribute exists, what does `obj.attribute` read? | Khi thuộc tính tồn tại, `obj.attribute` đọc gì?**

A. Creates a new method automatically | Tự tạo phương thức mới

B. Reads the named attribute on `obj` | Đọc thuộc tính có tên trên `obj`

C. Invokes every method of the object | Gọi mọi phương thức của đối tượng

D. Returns `True` only for class attributes | Chỉ trả `True` với thuộc tính cấp class

**Đáp án: B**

**Giải thích:** `obj.attribute` truy cập giá trị của thuộc tính có tên nếu nó tồn tại. Khác `obj.method()`, biểu thức không gọi hàm; nếu thiếu thuộc tính, Python thông thường phát sinh `AttributeError`.


**Q19. What does `isinstance(obj, Student)` check? | `isinstance(obj, Student)` kiểm tra gì?**

A. The object's exact class only, excluding subclasses | Chỉ class chính xác, loại class con

B. Whether the object has a method named `Student` | Đối tượng có phương thức tên `Student` không

C. Whether the object is a `Student` or its subclass | Đối tượng thuộc `Student` hay class con không

D. The class name as a string | Tên class ở dạng chuỗi

**Đáp án: C**

**Giải thích:** `isinstance(obj, Student)` đúng khi `obj` thuộc class `Student` hoặc một class con của nó. Ngược lại, `type(obj) is Student` chỉ kiểm tra class thực tế chính xác và loại các instance của class con.


**Q20. What does `type(obj)` return? | `type(obj)` trả về gì?**

A. Whether a class membership test is true | Phép kiểm tra thuộc class có đúng không

B. The object itself with unchanged type | Chính đối tượng và kiểu không đổi

C. A Boolean checking only its attributes | Boolean chỉ kiểm tra thuộc tính

D. The object's actual runtime class | Class thực tế của đối tượng khi chạy

**Đáp án: D**

**Giải thích:** `type(obj)` trả về class thực tế của đối tượng lúc chạy, chẳng hạn `Student`. `isinstance(obj, Student)` thì trả Boolean về quan hệ thuộc class và có thể chấp nhận instance của class con.

## 8. Nối sang bài tiếp theo

`Hàm / Dictionary → OOP → Kế thừa`.

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
## 5. Năm tình huống lập trình thực tế

### Tình huống 1 — Tạo hồ sơ học viên · Cấp 1: Một đối tượng

**Từ vựng trong mục:** **Class** — lớp.

**Tình huống thực tế:** Trung tâm tạo hồ sơ học viên An, có điểm 8 trên thang 10. In tên và điểm của học viên.

**Vì sao chọn cách giải này?** Dùng class `Student` để gom tên và điểm của một học viên.

**Quy trình giải:**

1. Tạo lớp `Student` với phương thức `__init__` nhận `name` và `score`.
2. Lưu hai đối số vào thuộc tính của đối tượng bằng `self`.
3. Tạo hồ sơ An với điểm 8 rồi in tên và điểm.

```python
# Mục đích: Tạo hồ sơ học viên.
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

s = Student('An', 8)
print(s.name, s.score)
```

**Kết quả khi chạy:**

```text
An 8
```

**Bài thực hành nâng cấp — cấp 1/5:** Trung tâm có **10 học viên**, mỗi hàng là một học viên với mã `id` và điểm `score` trên thang 100. Hãy tạo một đối tượng Student và đọc thuộc tính. Các cấp sau thêm bản ghi, cấp 4–5 có điểm khuyết cần xử lý qua phương thức chứ không so sánh trực tiếp `None` với số.

```python
values = [42, 70, 58, 91, 35, 76, 88, 64, 54, 96]
rows = [{"id":f"S{k:02d}","score":v} for k,v in enumerate(values,1)]
class Student:
    def __init__(self, info):
        self.id, self.score = info["id"], info["score"]
    def passed(self):
        return self.score is not None and self.score >= 60
result = (Student(rows[0]).id,Student(rows[0]).score)
print("Số học viên:",len(rows))
print("Kết quả:",result)
```

**Đọc kết quả:** Kiểm tra số đối tượng (10) và giá trị trả về của phương thức; mỗi đối tượng lưu trạng thái riêng.

### Tình huống 2 — Giỏ hàng có phương thức · Cấp 2: Quản lý nhiều đối tượng

**Từ vựng trong mục:** **Object** — đối tượng.

**Tình huống thực tế:** Một khách đưa hai món giá 100 và 200 đơn vị tiền vào giỏ hàng. Tính tổng tiền trong giỏ.

**Vì sao chọn cách giải này?** Đối tượng `Cart` giữ list giá và có phương thức `add`, `total`.

**Quy trình giải:**

1. Tạo giỏ hàng `Cart` có danh sách `prices` ban đầu rỗng.
2. Dùng phương thức `add` thêm hai giá 100 và 200.
3. Dùng phương thức `total` cộng các giá và in 300.

```python
# Mục đích: Giỏ hàng có phương thức.
class Cart:
    def __init__(self):
        self.prices = []

    def add(self, price):
        self.prices.append(price)

    def total(self):
        return sum(self.prices)

c = Cart()
c.add(100)
c.add(200)
print(c.total())
```

**Kết quả khi chạy:**

```text
300
```

**Bài thực hành nâng cấp — cấp 2/5:** Trung tâm có **12 học viên**, mỗi hàng là một học viên với mã `id` và điểm `score` trên thang 100. Hãy tạo 12 đối tượng tách biệt và kiểm tra số lượng. Các cấp sau thêm bản ghi, cấp 4–5 có điểm khuyết cần xử lý qua phương thức chứ không so sánh trực tiếp `None` với số.

```python
values = [42, 70, 58, 91, 35, 76, 88, 64, 54, 96, 47, 82]
rows = [{"id":f"S{k:02d}","score":v} for k,v in enumerate(values,1)]
class Student:
    def __init__(self, info):
        self.id, self.score = info["id"], info["score"]
    def passed(self):
        return self.score is not None and self.score >= 60
result = len([Student(r) for r in rows])
print("Số học viên:",len(rows))
print("Kết quả:",result)
```

**Đọc kết quả:** Kiểm tra số đối tượng (12) và giá trị trả về của phương thức; mỗi đối tượng lưu trạng thái riêng.

### Tình huống 3 — Ràng buộc điểm nhập · Cấp 3: Gọi phương thức trên tập hợp

**Từ vựng trong mục:** **Constructor** — hàm khởi tạo.

**Tình huống thực tế:** Hệ thống chỉ cho phép lưu điểm trong khoảng 0 đến 10. Một học viên có điểm 9. Lưu và in điểm hợp lệ.

**Vì sao chọn cách giải này?** Phương thức `set` kiểm tra giới hạn trước khi cập nhật.

**Quy trình giải:**

1. Khởi tạo đối tượng `Score` với giá trị ban đầu bằng 0.
2. Gọi `set(9)` để kiểm tra điểm thuộc khoảng 0–10 rồi lưu giá trị.
3. In điểm đã được lưu; nếu truyền 11, phương thức sẽ báo lỗi.

```python
# Mục đích: Ràng buộc điểm nhập.
class Score:
    def __init__(self):
        self.value = 0

    def set(self, x):
        if not 0 <= x <= 10:
            raise ValueError('score')
        self.value = x

s = Score()
s.set(9)
print(s.value)
```

**Kết quả khi chạy:**

```text
9
```

**Bài thực hành nâng cấp — cấp 3/5:** Trung tâm có **15 học viên**, mỗi hàng là một học viên với mã `id` và điểm `score` trên thang 100. Hãy gọi phương thức passed() để lọc hồ sơ đạt. Các cấp sau thêm bản ghi, cấp 4–5 có điểm khuyết cần xử lý qua phương thức chứ không so sánh trực tiếp `None` với số.

```python
values = [42, 70, 58, 91, 35, 76, 88, 64, 54, 96, 47, 82, 69, 73, 61]
rows = [{"id":f"S{k:02d}","score":v} for k,v in enumerate(values,1)]
class Student:
    def __init__(self, info):
        self.id, self.score = info["id"], info["score"]
    def passed(self):
        return self.score is not None and self.score >= 60
result = [s.id for s in [Student(r) for r in rows] if s.passed()]
print("Số học viên:",len(rows))
print("Kết quả:",result)
```

**Đọc kết quả:** Kiểm tra số đối tượng (15) và giá trị trả về của phương thức; mỗi đối tượng lưu trạng thái riêng.

### Tình huống 4 — In hóa đơn dễ đọc · Cấp 4: Kiểm tra thuộc tính thiếu

**Từ vựng trong mục:** **Encapsulation** — đóng gói.

**Tình huống thực tế:** Một hóa đơn có mã O01 và số tiền 150.000 VND. In hóa đơn ở dạng dễ đọc.

**Vì sao chọn cách giải này?** `__str__` quy định cách đối tượng hiển thị khi truyền vào `print`.

**Quy trình giải:**

1. Lưu mã `O01` và số tiền 150000 trong đối tượng `Order`.
2. Định nghĩa `__str__` để tạo chuỗi hiển thị mã đơn và số tiền.
3. Gọi `print(Order(...))` để Python tự dùng `__str__`.

```python
# Mục đích: In hóa đơn dễ đọc.
class Order:
    def __init__(self, code, total):
        self.code = code
        self.total = total

    def __str__(self):
        return f'{self.code}: {self.total} VND'

print(Order('O01', 150000))
```

**Kết quả khi chạy:**

```text
O01: 150000 VND
```

**Bài thực hành nâng cấp — cấp 4/5:** Trung tâm có **18 học viên**, mỗi hàng là một học viên với mã `id` và điểm `score` trên thang 100. Hãy kiểm tra trường hợp score là None trước so sánh. Các cấp sau thêm bản ghi, cấp 4–5 có điểm khuyết cần xử lý qua phương thức chứ không so sánh trực tiếp `None` với số.

```python
values = [42, 70, 58, 91, 35, 76, 88, 64, 54, 96, 47, 82, 69, 73, 61, None, 90, 39]
rows = [{"id":f"S{k:02d}","score":v} for k,v in enumerate(values,1)]
class Student:
    def __init__(self, info):
        self.id, self.score = info["id"], info["score"]
    def passed(self):
        return self.score is not None and self.score >= 60
result = [(s.id,s.passed()) for s in [Student(r) for r in rows]]
print("Số học viên:",len(rows))
print("Kết quả:",result)
```

**Đọc kết quả:** Kiểm tra số đối tượng (18) và giá trị trả về của phương thức; mỗi đối tượng lưu trạng thái riêng.

### Tình huống 5 — Hai cảm biến độc lập · Cấp 5: Báo cáo từ toàn bộ đối tượng

**Từ vựng trong mục:** **Class** — lớp.

**Tình huống thực tế:** Hai cảm biến có giá trị ban đầu lần lượt 20 và 40. Cảm biến đầu được cập nhật thành 25. Kiểm tra hai cảm biến có lưu giá trị độc lập hay không.

**Vì sao chọn cách giải này?** Mỗi lần gọi `Sensor()` tạo một đối tượng có thuộc tính `value` riêng.

**Quy trình giải:**

1. Tạo hai đối tượng `Sensor(20)` và `Sensor(40)` độc lập.
2. Cập nhật `a.value` thành 25, không sửa `b.value`.
3. In giá trị của cả hai để thấy `25 40`.

```python
# Mục đích: Hai cảm biến độc lập.
class Sensor:
    def __init__(self, value):
        self.value = value

a, b = Sensor(20), Sensor(40)
a.value = 25
print(a.value, b.value)
```

**Kết quả khi chạy:**

```text
25 40
```

**Bài thực hành nâng cấp — cấp 5/5:** Trung tâm có **20 học viên**, mỗi hàng là một học viên với mã `id` và điểm `score` trên thang 100. Hãy tổng hợp đủ hồ sơ đạt, chưa đạt và thiếu điểm. Các cấp sau thêm bản ghi, cấp 4–5 có điểm khuyết cần xử lý qua phương thức chứ không so sánh trực tiếp `None` với số.

```python
values = [42, 70, 58, 91, 35, 76, 88, 64, 54, 96, 47, 82, 69, 73, 61, None, 90, 39, 85, None]
rows = [{"id":f"S{k:02d}","score":v} for k,v in enumerate(values,1)]
class Student:
    def __init__(self, info):
        self.id, self.score = info["id"], info["score"]
    def passed(self):
        return self.score is not None and self.score >= 60
result = {'passed':[s.id for s in [Student(r) for r in rows] if s.passed()],'missing':[s.id for s in [Student(r) for r in rows] if s.score is None]}
print("Số học viên:",len(rows))
print("Kết quả:",result)
```

**Đọc kết quả:** Kiểm tra số đối tượng (20) và giá trị trả về của phương thức; mỗi đối tượng lưu trạng thái riêng.

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

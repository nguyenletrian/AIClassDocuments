# PY-10 — Class, Object, constructor và đóng gói


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Class** — lớp; **Object** — đối tượng.

`Hàm / Dictionary → OOP → Kế thừa`

Sau hàm và Dictionary, ta học cách tạo một kiểu đối tượng có thông tin và hành vi riêng, rồi dùng lại kiểu đó cho nhiều đối tượng.

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

### Tình huống 1 — Tạo hồ sơ học viên

**Từ vựng trong mục:** **Class** — lớp.

**Tình huống thực tế:** Trung tâm tạo hồ sơ học viên An, có điểm 8 trên thang 10. In tên và điểm của học viên.

**Vì sao chọn cách giải này?** Dùng class `Student` để gom tên và điểm của một học viên.

**Quy trình giải:**

1. Tạo lớp `Student` với phương thức `__init__` nhận `name` và `score`.
2. Lưu hai đối số vào thuộc tính của đối tượng bằng `self`.
3. Tạo hồ sơ An với điểm 8 rồi in tên và điểm.

```python
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

### Tình huống 2 — Giỏ hàng có phương thức

**Từ vựng trong mục:** **Object** — đối tượng.

**Tình huống thực tế:** Một khách đưa hai món giá 100 và 200 đơn vị tiền vào giỏ hàng. Tính tổng tiền trong giỏ.

**Vì sao chọn cách giải này?** Đối tượng `Cart` giữ list giá và có phương thức `add`, `total`.

**Quy trình giải:**

1. Tạo giỏ hàng `Cart` có danh sách `prices` ban đầu rỗng.
2. Dùng phương thức `add` thêm hai giá 100 và 200.
3. Dùng phương thức `total` cộng các giá và in 300.

```python
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

### Tình huống 3 — Ràng buộc điểm nhập

**Từ vựng trong mục:** **Constructor** — hàm khởi tạo.

**Tình huống thực tế:** Hệ thống chỉ cho phép lưu điểm trong khoảng 0 đến 10. Một học viên có điểm 9. Lưu và in điểm hợp lệ.

**Vì sao chọn cách giải này?** Phương thức `set` kiểm tra giới hạn trước khi cập nhật.

**Quy trình giải:**

1. Khởi tạo đối tượng `Score` với giá trị ban đầu bằng 0.
2. Gọi `set(9)` để kiểm tra điểm thuộc khoảng 0–10 rồi lưu giá trị.
3. In điểm đã được lưu; nếu truyền 11, phương thức sẽ báo lỗi.

```python
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

### Tình huống 4 — In hóa đơn dễ đọc

**Từ vựng trong mục:** **Encapsulation** — đóng gói.

**Tình huống thực tế:** Một hóa đơn có mã O01 và số tiền 150.000 VND. In hóa đơn ở dạng dễ đọc.

**Vì sao chọn cách giải này?** `__str__` quy định cách đối tượng hiển thị khi truyền vào `print`.

**Quy trình giải:**

1. Lưu mã `O01` và số tiền 150000 trong đối tượng `Order`.
2. Định nghĩa `__str__` để tạo chuỗi hiển thị mã đơn và số tiền.
3. Gọi `print(Order(...))` để Python tự dùng `__str__`.

```python
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

### Tình huống 5 — Hai cảm biến độc lập

**Từ vựng trong mục:** **Class** — lớp.

**Tình huống thực tế:** Hai cảm biến có giá trị ban đầu lần lượt 20 và 40. Cảm biến đầu được cập nhật thành 25. Kiểm tra hai cảm biến có lưu giá trị độc lập hay không.

**Vì sao chọn cách giải này?** Mỗi lần gọi `Sensor()` tạo một đối tượng có thuộc tính `value` riêng.

**Quy trình giải:**

1. Tạo hai đối tượng `Sensor(20)` và `Sensor(40)` độc lập.
2. Cập nhật `a.value` thành 25, không sửa `b.value`.
3. In giá trị của cả hai để thấy `25 40`.

```python
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

## 6. Sai lầm thường gặp

- `class` là khuôn mẫu; đối tượng chỉ xuất hiện khi gọi lớp như `Student('An', 8)`.
- `self.name` là thuộc tính của đối tượng, không phải biến dùng chung giữa mọi học viên. Mỗi đối tượng có trạng thái riêng.
- `__init__` chuẩn bị dữ liệu ban đầu, còn `__str__` quy định cách hiển thị; hai phương thức có mục đích khác nhau.
- `self._value` dùng dấu gạch dưới theo quy ước, không tự tạo thuộc tính hoàn toàn riêng tư. Muốn bảo vệ dữ liệu cần kiểm soát cách cập nhật và kiểm tra hợp lệ.
- Điểm vượt 0–10 sẽ phát sinh `ValueError` trong ví dụ `Score`; không bỏ qua xử lý lỗi ở chương trình thực tế.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is a class in Python OOP? — Class trong OOP Python là gì?**

A. A template defining objects' data and behavior — Khuôn mẫu mô tả dữ liệu và hành vi đối tượng

B. A concrete value created from a class — Đối tượng cụ thể được tạo từ một class

C. Data stored on an object — Dữ liệu lưu trên đối tượng

D. A function belonging to a class that works with an instance — Hàm thuộc lớp, làm việc với đối tượng

**Q2. What is an object or instance? — Object hay instance là gì?**

A. A template defining objects' data and behavior — Khuôn mẫu mô tả dữ liệu và hành vi đối tượng

B. A concrete value created from a class — Đối tượng cụ thể được tạo từ một class

C. Data stored on an object — Dữ liệu lưu trên đối tượng

D. A function belonging to a class that works with an instance — Hàm thuộc lớp, làm việc với đối tượng

**Q3. What is an attribute? — Attribute là gì?**

A. A template defining objects' data and behavior — Khuôn mẫu mô tả dữ liệu và hành vi đối tượng

B. A concrete value created from a class — Đối tượng cụ thể được tạo từ một class

C. Data stored on an object — Dữ liệu lưu trên đối tượng

D. A function belonging to a class that works with an instance — Hàm thuộc lớp, làm việc với đối tượng

**Q4. What is an instance method? — Phương thức đối tượng là gì?**

A. A template defining objects' data and behavior — Khuôn mẫu mô tả dữ liệu và hành vi đối tượng

B. A concrete value created from a class — Đối tượng cụ thể được tạo từ một class

C. Data stored on an object — Dữ liệu lưu trên đối tượng

D. A function belonging to a class that works with an instance — Hàm thuộc lớp, làm việc với đối tượng

**Q5. Which syntax begins a class definition? — Cú pháp nào mở đầu định nghĩa class?**

A. `class Student:` — `class Student:`

B. `Student()` — `Student()`

C. `__init__` — `__init__`

D. The object receiving the method call — Đối tượng đang nhận lời gọi

**Q6. Which syntax creates a Student instance? — Cú pháp nào tạo đối tượng Student?**

A. `class Student:` — `class Student:`

B. `Student()` — `Student()`

C. `__init__` — `__init__`

D. The object receiving the method call — Đối tượng đang nhận lời gọi

**Q7. Which special method initializes instance attributes? — Phương thức đặc biệt nào khởi tạo thuộc tính đối tượng?**

A. `class Student:` — `class Student:`

B. `Student()` — `Student()`

C. `__init__` — `__init__`

D. The object receiving the method call — Đối tượng đang nhận lời gọi

**Q8. What does `self` refer to in an instance method? — `self` trong phương thức đối tượng chỉ gì?**

A. `class Student:` — `class Student:`

B. `Student()` — `Student()`

C. `__init__` — `__init__`

D. The object receiving the method call — Đối tượng đang nhận lời gọi

**Q9. What does `self.name = name` do? — `self.name = name` làm gì?**

A. Stores the name on the current object — Lưu name trên đối tượng hiện tại

B. Readable string representation of an object — Chuỗi hiển thị dễ đọc của đối tượng

C. Signals an invalid value by raising an exception — Báo giá trị không hợp lệ bằng ngoại lệ

D. A non-public implementation detail by convention — Thành phần nội bộ theo quy ước

**Q10. What does `__str__` normally customize? — `__str__` thường tùy chỉnh điều gì?**

A. Stores the name on the current object — Lưu name trên đối tượng hiện tại

B. Readable string representation of an object — Chuỗi hiển thị dễ đọc của đối tượng

C. Signals an invalid value by raising an exception — Báo giá trị không hợp lệ bằng ngoại lệ

D. A non-public implementation detail by convention — Thành phần nội bộ theo quy ước

**Q11. What does `raise ValueError(...)` do? — `raise ValueError(...)` làm gì?**

A. Stores the name on the current object — Lưu name trên đối tượng hiện tại

B. Readable string representation of an object — Chuỗi hiển thị dễ đọc của đối tượng

C. Signals an invalid value by raising an exception — Báo giá trị không hợp lệ bằng ngoại lệ

D. A non-public implementation detail by convention — Thành phần nội bộ theo quy ước

**Q12. What does the prefix `_value` conventionally mean? — Tiền tố `_value` theo quy ước có nghĩa gì?**

A. Stores the name on the current object — Lưu name trên đối tượng hiện tại

B. Readable string representation of an object — Chuỗi hiển thị dễ đọc của đối tượng

C. Signals an invalid value by raising an exception — Báo giá trị không hợp lệ bằng ngoại lệ

D. A non-public implementation detail by convention — Thành phần nội bộ theo quy ước

**Q13. What is encapsulation? — Đóng gói trong OOP là gì?**

A. Keeping data and its operations together — Gom dữ liệu và thao tác lên dữ liệu cùng nhau

B. To enforce valid object state — Để giữ trạng thái đối tượng hợp lệ

C. They share class behavior but can hold different state — Cùng hành vi do lớp định nghĩa nhưng có thể khác dữ liệu

D. A value defined on the class and shared in lookup — Giá trị định nghĩa trên lớp và dùng chung khi truy cập

**Q14. Why validate values in a setter method? — Vì sao kiểm tra dữ liệu trong setter?**

A. Keeping data and its operations together — Gom dữ liệu và thao tác lên dữ liệu cùng nhau

B. To enforce valid object state — Để giữ trạng thái đối tượng hợp lệ

C. They share class behavior but can hold different state — Cùng hành vi do lớp định nghĩa nhưng có thể khác dữ liệu

D. A value defined on the class and shared in lookup — Giá trị định nghĩa trên lớp và dùng chung khi truy cập

**Q15. How do two instances of the same class relate? — Hai đối tượng cùng class có quan hệ gì?**

A. Keeping data and its operations together — Gom dữ liệu và thao tác lên dữ liệu cùng nhau

B. To enforce valid object state — Để giữ trạng thái đối tượng hợp lệ

C. They share class behavior but can hold different state — Cùng hành vi do lớp định nghĩa nhưng có thể khác dữ liệu

D. A value defined on the class and shared in lookup — Giá trị định nghĩa trên lớp và dùng chung khi truy cập

**Q16. What is a class attribute? — Thuộc tính cấp class là gì?**

A. Keeping data and its operations together — Gom dữ liệu và thao tác lên dữ liệu cùng nhau

B. To enforce valid object state — Để giữ trạng thái đối tượng hợp lệ

C. They share class behavior but can hold different state — Cùng hành vi do lớp định nghĩa nhưng có thể khác dữ liệu

D. A value defined on the class and shared in lookup — Giá trị định nghĩa trên lớp và dùng chung khi truy cập

**Q17. What does `obj.method()` do? — `obj.method()` làm gì?**

A. Invokes a method on obj — Gọi một phương thức trên obj

B. An attribute associated with obj — Thuộc tính gắn với obj

C. Whether obj is an instance of Student or a subclass — obj có là đối tượng của Student hoặc lớp con không

D. The object's actual class — Class thực tế của đối tượng

**Q18. What does `obj.attribute` read? — `obj.attribute` đọc gì?**

A. Invokes a method on obj — Gọi một phương thức trên obj

B. An attribute associated with obj — Thuộc tính gắn với obj

C. Whether obj is an instance of Student or a subclass — obj có là đối tượng của Student hoặc lớp con không

D. The object's actual class — Class thực tế của đối tượng

**Q19. What does `isinstance(obj, Student)` check? — `isinstance(obj, Student)` kiểm tra gì?**

A. Invokes a method on obj — Gọi một phương thức trên obj

B. An attribute associated with obj — Thuộc tính gắn với obj

C. Whether obj is an instance of Student or a subclass — obj có là đối tượng của Student hoặc lớp con không

D. The object's actual class — Class thực tế của đối tượng

**Q20. What does `type(obj)` return? — `type(obj)` trả về gì?**

A. Invokes a method on obj — Gọi một phương thức trên obj

B. An attribute associated with obj — Thuộc tính gắn với obj

C. Whether obj is an instance of Student or a subclass — obj có là đối tượng của Student hoặc lớp con không

D. The object's actual class — Class thực tế của đối tượng

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **A** | A class groups common attributes and methods for instances. | Class gom thuộc tính và phương thức chung cho đối tượng. |
| Q2 | **B** | Each instance stores its own state as defined by its class. | Mỗi đối tượng có trạng thái riêng theo lớp của nó. |
| Q3 | **C** | Instance attributes hold values such as name or score. | Thuộc tính đối tượng lưu giá trị như tên hoặc điểm. |
| Q4 | **D** | Instance methods access object state via the instance parameter. | Phương thức đối tượng làm việc với trạng thái qua tham số đối tượng. |
| Q5 | **A** | The class keyword declares a new class. | Từ khóa class khai báo một lớp mới. |
| Q6 | **B** | Calling the class creates an instance of that class. | Gọi lớp tạo ra một đối tượng của lớp đó. |
| Q7 | **C** | Python invokes __init__ after creating a new instance. | Python gọi __init__ sau khi tạo đối tượng mới. |
| Q8 | **D** | self refers to the specific instance whose method is executing. | self chỉ đối tượng cụ thể đang thực thi phương thức. |
| Q9 | **A** | Each instance can hold its own name attribute. | Mỗi đối tượng có thể lưu thuộc tính name riêng. |
| Q10 | **B** | str(obj) and print(obj) use __str__ if implemented. | str(obj) và print(obj) dùng __str__ khi có định nghĩa. |
| Q11 | **C** | raise interrupts normal flow with the specified exception. | raise ngắt luồng bình thường bằng ngoại lệ tương ứng. |
| Q12 | **D** | A single leading underscore signals intended internal use, not enforced privacy. | Một gạch dưới đầu tên chỉ quy ước dùng nội bộ, không khóa truy cập tuyệt đối. |
| Q13 | **A** | Encapsulation groups object state with methods that manage it. | Đóng gói kết hợp trạng thái với phương thức quản lý. |
| Q14 | **B** | Setters can reject invalid values before storing them. | Setter có thể từ chối giá trị sai trước khi lưu. |
| Q15 | **C** | Each instance has its own attributes unless explicit shared class state is used. | Mỗi đối tượng có thuộc tính riêng, trừ khi cố ý dùng dữ liệu chung cấp lớp. |
| Q16 | **D** | Class attributes are available through the class and normally through instances. | Thuộc tính cấp lớp có thể truy cập qua lớp và thông thường qua đối tượng. |
| Q17 | **A** | Dot notation resolves the named method for the instance. | Cú pháp dấu chấm lấy phương thức theo tên trên đối tượng. |
| Q18 | **B** | Dot access retrieves the selected attribute on the object. | Dấu chấm truy cập thuộc tính đã chỉ định của đối tượng. |
| Q19 | **C** | isinstance tests the object's class relationship. | isinstance kiểm tra quan hệ lớp của đối tượng. |
| Q20 | **D** | type reveals the runtime class of an instance. | type cho biết lớp thực tế của đối tượng lúc chạy. |

## 8. Nối sang bài tiếp theo

`Hàm / Dictionary → OOP → Kế thừa`.

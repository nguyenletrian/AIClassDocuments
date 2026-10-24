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


**Q1. Which description matches Class? — Mô tả nào đúng với Class?**

A. A different concept described as Một thể hiện cụ thể của lớp — Một thể hiện cụ thể của lớp

B. The concept described as Khuôn mô tả dữ liệu và cách xử lý — Khuôn mô tả dữ liệu và cách xử lý

C. A different concept described as Thiết lập thuộc tính lúc tạo instance — Thiết lập thuộc tính lúc tạo instance

D. A different concept described as Đặt dữ liệu và hành vi bên trong đối tượng — Đặt dữ liệu và hành vi bên trong đối tượng


**Q2. Which description matches Object? — Mô tả nào đúng với Object?**

A. The concept described as Một thể hiện cụ thể của lớp — Một thể hiện cụ thể của lớp

B. A different concept described as Thiết lập thuộc tính lúc tạo instance — Thiết lập thuộc tính lúc tạo instance

C. A different concept described as Đặt dữ liệu và hành vi bên trong đối tượng — Đặt dữ liệu và hành vi bên trong đối tượng

D. A different concept described as Khuôn mô tả dữ liệu và cách xử lý — Khuôn mô tả dữ liệu và cách xử lý


**Q3. Which description matches Constructor? — Mô tả nào đúng với Constructor?**

A. A different concept described as Đặt dữ liệu và hành vi bên trong đối tượng — Đặt dữ liệu và hành vi bên trong đối tượng

B. A different concept described as Khuôn mô tả dữ liệu và cách xử lý — Khuôn mô tả dữ liệu và cách xử lý

C. A different concept described as Một thể hiện cụ thể của lớp — Một thể hiện cụ thể của lớp

D. The concept described as Thiết lập thuộc tính lúc tạo instance — Thiết lập thuộc tính lúc tạo instance


**Q4. Which description matches Encapsulation? — Mô tả nào đúng với Encapsulation?**

A. A different concept described as Khuôn mô tả dữ liệu và cách xử lý — Khuôn mô tả dữ liệu và cách xử lý

B. A different concept described as Một thể hiện cụ thể của lớp — Một thể hiện cụ thể của lớp

C. The concept described as Đặt dữ liệu và hành vi bên trong đối tượng — Đặt dữ liệu và hành vi bên trong đối tượng

D. A different concept described as Thiết lập thuộc tính lúc tạo instance — Thiết lập thuộc tính lúc tạo instance


**Q5. Which use matches class Name:? — Công dụng nào đúng với class Name:?**

A. Use a different operation to Khởi tạo trạng thái của từng instance — Khởi tạo trạng thái của từng instance

B. Use this syntax to Định nghĩa kiểu đối tượng và các phương thức — Định nghĩa kiểu đối tượng và các phương thức

C. Use a different operation to Truy cập thuộc tính thuộc về chính đối tượng — Truy cập thuộc tính thuộc về chính đối tượng

D. Use a different operation to Hiển thị và kiểm tra thao tác thay đổi giá trị — Hiển thị và kiểm tra thao tác thay đổi giá trị


**Q6. Which use matches __init__(self, ...)? — Công dụng nào đúng với __init__(self, ...)?**

A. Use this syntax to Khởi tạo trạng thái của từng instance — Khởi tạo trạng thái của từng instance

B. Use a different operation to Truy cập thuộc tính thuộc về chính đối tượng — Truy cập thuộc tính thuộc về chính đối tượng

C. Use a different operation to Hiển thị và kiểm tra thao tác thay đổi giá trị — Hiển thị và kiểm tra thao tác thay đổi giá trị

D. Use a different operation to Định nghĩa kiểu đối tượng và các phương thức — Định nghĩa kiểu đối tượng và các phương thức


**Q7. Which use matches self.attribute? — Công dụng nào đúng với self.attribute?**

A. Use a different operation to Hiển thị và kiểm tra thao tác thay đổi giá trị — Hiển thị và kiểm tra thao tác thay đổi giá trị

B. Use a different operation to Định nghĩa kiểu đối tượng và các phương thức — Định nghĩa kiểu đối tượng và các phương thức

C. Use a different operation to Khởi tạo trạng thái của từng instance — Khởi tạo trạng thái của từng instance

D. Use this syntax to Truy cập thuộc tính thuộc về chính đối tượng — Truy cập thuộc tính thuộc về chính đối tượng


**Q8. Which use matches __str__/set_*/get_*? — Công dụng nào đúng với __str__/set_*/get_*?**

A. Use a different operation to Định nghĩa kiểu đối tượng và các phương thức — Định nghĩa kiểu đối tượng và các phương thức

B. Use a different operation to Khởi tạo trạng thái của từng instance — Khởi tạo trạng thái của từng instance

C. Use this syntax to Hiển thị và kiểm tra thao tác thay đổi giá trị — Hiển thị và kiểm tra thao tác thay đổi giá trị

D. Use a different operation to Truy cập thuộc tính thuộc về chính đối tượng — Truy cập thuộc tính thuộc về chính đối tượng


**Q9. What solves scenario 1? — Cách nào giải quyết tình huống 1?**

A. Another method is chosen because Đặt add và total cùng nơi lưu giá sản phẩm — Đặt add và total cùng nơi lưu giá sản phẩm

B. Choose the method because Mỗi object giữ tên và điểm riêng, thay vì nhiều list song song — Mỗi object giữ tên và điểm riêng, thay vì nhiều list song song

C. Another method is chosen because Setter chặn điểm ngoài thang 0–10 — Setter chặn điểm ngoài thang 0–10

D. Another method is chosen because __str__ định nghĩa chữ hiện khi in đối tượng — __str__ định nghĩa chữ hiện khi in đối tượng


**Q10. What solves scenario 2? — Cách nào giải quyết tình huống 2?**

A. Choose the method because Đặt add và total cùng nơi lưu giá sản phẩm — Đặt add và total cùng nơi lưu giá sản phẩm

B. Another method is chosen because Setter chặn điểm ngoài thang 0–10 — Setter chặn điểm ngoài thang 0–10

C. Another method is chosen because __str__ định nghĩa chữ hiện khi in đối tượng — __str__ định nghĩa chữ hiện khi in đối tượng

D. Another method is chosen because Instance khác nhau không chia sẻ nhầm dữ liệu đo — Instance khác nhau không chia sẻ nhầm dữ liệu đo


**Q11. What solves scenario 3? — Cách nào giải quyết tình huống 3?**

A. Another method is chosen because __str__ định nghĩa chữ hiện khi in đối tượng — __str__ định nghĩa chữ hiện khi in đối tượng

B. Another method is chosen because Instance khác nhau không chia sẻ nhầm dữ liệu đo — Instance khác nhau không chia sẻ nhầm dữ liệu đo

C. Another method is chosen because Mỗi object giữ tên và điểm riêng, thay vì nhiều list song song — Mỗi object giữ tên và điểm riêng, thay vì nhiều list song song

D. Choose the method because Setter chặn điểm ngoài thang 0–10 — Setter chặn điểm ngoài thang 0–10


**Q12. What solves scenario 4? — Cách nào giải quyết tình huống 4?**

A. Another method is chosen because Instance khác nhau không chia sẻ nhầm dữ liệu đo — Instance khác nhau không chia sẻ nhầm dữ liệu đo

B. Another method is chosen because Mỗi object giữ tên và điểm riêng, thay vì nhiều list song song — Mỗi object giữ tên và điểm riêng, thay vì nhiều list song song

C. Choose the method because __str__ định nghĩa chữ hiện khi in đối tượng — __str__ định nghĩa chữ hiện khi in đối tượng

D. Another method is chosen because Đặt add và total cùng nơi lưu giá sản phẩm — Đặt add và total cùng nơi lưu giá sản phẩm


**Q13. What solves scenario 5? — Cách nào giải quyết tình huống 5?**

A. Another method is chosen because Mỗi object giữ tên và điểm riêng, thay vì nhiều list song song — Mỗi object giữ tên và điểm riêng, thay vì nhiều list song song

B. Choose the method because Instance khác nhau không chia sẻ nhầm dữ liệu đo — Instance khác nhau không chia sẻ nhầm dữ liệu đo

C. Another method is chosen because Đặt add và total cùng nơi lưu giá sản phẩm — Đặt add và total cùng nơi lưu giá sản phẩm

D. Another method is chosen because Setter chặn điểm ngoài thang 0–10 — Setter chặn điểm ngoài thang 0–10


**Q14. Which data is used in scenario 1? — Tình huống 1 dùng dữ liệu nào?**

A. The described input Một sinh viên có tên An, điểm 8 — Một sinh viên có tên An, điểm 8

B. Another input Giá [100,200] nghìn đồng — Giá [100,200] nghìn đồng

C. Another input Một lần nhập 9/10 — Một lần nhập 9/10

D. Another input Đơn O01 trị giá 150000 đồng — Đơn O01 trị giá 150000 đồng


**Q15. Which data is used in scenario 2? — Tình huống 2 dùng dữ liệu nào?**

A. Another input Một lần nhập 9/10 — Một lần nhập 9/10

B. Another input Đơn O01 trị giá 150000 đồng — Đơn O01 trị giá 150000 đồng

C. Another input Cảm biến A=20, B=40 độ C — Cảm biến A=20, B=40 độ C

D. The described input Giá [100,200] nghìn đồng — Giá [100,200] nghìn đồng


**Q16. Which data is used in scenario 3? — Tình huống 3 dùng dữ liệu nào?**

A. Another input Đơn O01 trị giá 150000 đồng — Đơn O01 trị giá 150000 đồng

B. Another input Cảm biến A=20, B=40 độ C — Cảm biến A=20, B=40 độ C

C. The described input Một lần nhập 9/10 — Một lần nhập 9/10

D. Another input Một sinh viên có tên An, điểm 8 — Một sinh viên có tên An, điểm 8


**Q17. Which data is used in scenario 4? — Tình huống 4 dùng dữ liệu nào?**

A. Another input Cảm biến A=20, B=40 độ C — Cảm biến A=20, B=40 độ C

B. The described input Đơn O01 trị giá 150000 đồng — Đơn O01 trị giá 150000 đồng

C. Another input Một sinh viên có tên An, điểm 8 — Một sinh viên có tên An, điểm 8

D. Another input Giá [100,200] nghìn đồng — Giá [100,200] nghìn đồng


**Q18. Which data is used in scenario 5? — Tình huống 5 dùng dữ liệu nào?**

A. The described input Cảm biến A=20, B=40 độ C — Cảm biến A=20, B=40 độ C

B. Another input Một sinh viên có tên An, điểm 8 — Một sinh viên có tên An, điểm 8

C. Another input Giá [100,200] nghìn đồng — Giá [100,200] nghìn đồng

D. Another input Một lần nhập 9/10 — Một lần nhập 9/10


**Q19. What must be clear before computing? — Cần hiểu gì trước khi tính?**

A. Only font color — Chỉ màu chữ

B. Only filename length — Chỉ độ dài tên file

C. Only number of comments — Chỉ số comment

D. Input meaning and units — Ý nghĩa và đơn vị dữ liệu


**Q20. What should follow a successful demo? — Sau khi demo chạy đúng nên làm gì?**

A. Assume it works for all data — Cho rằng luôn đúng với mọi dữ liệu

B. Remove input validation — Xóa kiểm tra đầu vào

C. Verify output and unusual inputs — Kiểm tra đầu ra và giá trị biên

D. Ignore unexpected results — Bỏ qua kết quả bất thường

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **B** | The concept described as Khuôn mô tả dữ liệu và cách xử lý | Khuôn mô tả dữ liệu và cách xử lý |
| Q2 | **A** | The concept described as Một thể hiện cụ thể của lớp | Một thể hiện cụ thể của lớp |
| Q3 | **D** | The concept described as Thiết lập thuộc tính lúc tạo instance | Thiết lập thuộc tính lúc tạo instance |
| Q4 | **C** | The concept described as Đặt dữ liệu và hành vi bên trong đối tượng | Đặt dữ liệu và hành vi bên trong đối tượng |
| Q5 | **B** | Use this syntax to Định nghĩa kiểu đối tượng và các phương thức | Định nghĩa kiểu đối tượng và các phương thức |
| Q6 | **A** | Use this syntax to Khởi tạo trạng thái của từng instance | Khởi tạo trạng thái của từng instance |
| Q7 | **D** | Use this syntax to Truy cập thuộc tính thuộc về chính đối tượng | Truy cập thuộc tính thuộc về chính đối tượng |
| Q8 | **C** | Use this syntax to Hiển thị và kiểm tra thao tác thay đổi giá trị | Hiển thị và kiểm tra thao tác thay đổi giá trị |
| Q9 | **B** | Choose the method because Mỗi object giữ tên và điểm riêng, thay vì nhiều list song song | Mỗi object giữ tên và điểm riêng, thay vì nhiều list song song |
| Q10 | **A** | Choose the method because Đặt add và total cùng nơi lưu giá sản phẩm | Đặt add và total cùng nơi lưu giá sản phẩm |
| Q11 | **D** | Choose the method because Setter chặn điểm ngoài thang 0–10 | Setter chặn điểm ngoài thang 0–10 |
| Q12 | **C** | Choose the method because __str__ định nghĩa chữ hiện khi in đối tượng | __str__ định nghĩa chữ hiện khi in đối tượng |
| Q13 | **B** | Choose the method because Instance khác nhau không chia sẻ nhầm dữ liệu đo | Instance khác nhau không chia sẻ nhầm dữ liệu đo |
| Q14 | **A** | The described input Một sinh viên có tên An, điểm 8 | Một sinh viên có tên An, điểm 8 |
| Q15 | **D** | The described input Giá [100,200] nghìn đồng | Giá [100,200] nghìn đồng |
| Q16 | **C** | The described input Một lần nhập 9/10 | Một lần nhập 9/10 |
| Q17 | **B** | The described input Đơn O01 trị giá 150000 đồng | Đơn O01 trị giá 150000 đồng |
| Q18 | **A** | The described input Cảm biến A=20, B=40 độ C | Cảm biến A=20, B=40 độ C |
| Q19 | **D** | Input meaning and units | Ý nghĩa và đơn vị dữ liệu |
| Q20 | **C** | Verify output and unusual inputs | Kiểm tra đầu ra và giá trị biên |

## 8. Nối sang bài tiếp theo

`Hàm / Dictionary → OOP → Kế thừa`.

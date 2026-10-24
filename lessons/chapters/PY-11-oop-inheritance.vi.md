# PY-11 — Kế thừa, đa hình và lớp trừu tượng ABC


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Inheritance** — kế thừa; **Polymorphism** — đa hình.

`Class/Object → Inheritance → Abstract API → Kiến trúc ứng dụng`

Sau bài Class và Object, ta học cách tạo lớp con tái sử dụng thành phần chung, sau đó thay đổi cách xử lý cho từng loại đối tượng hoặc quy định phương thức bắt buộc.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Ý nghĩa |
|---|---|---|
| Inheritance | kế thừa | Lớp con dùng lại các đặc điểm lớp cha |
| Polymorphism | đa hình | Cùng lời gọi nhưng các lớp có cách đáp khác nhau |
| Abstract class | lớp trừu tượng | Khung lớp ràng buộc phương thức cần cài đặt |
| Override | ghi đè | Lớp con cài lại phương thức của lớp cha |

## 3. Thư viện, hàm và tham số

**Từ vựng trong mục:** **Function** — hàm; **Parameter** — tham số.

| Hàm/cú pháp | Giải thích và lý do dùng |
|---|---|
| `class Child(Parent)` | Kế thừa thông tin chung |
| `super().__init__(...)` | Gọi khởi tạo lớp cha để không lặp code |
| `ABC/@abstractmethod` | Bắt lớp con định nghĩa giao diện bắt buộc |
| `isinstance(obj,Class)` | Xác minh đối tượng thuộc lớp khi cần |

## 4. Khái niệm liên quan

**Kế thừa, đa hình và lớp trừu tượng** giải quyết ba nhu cầu khác nhau trong OOP: dùng lại đặc điểm chung, xử lý cùng thao tác theo cách riêng và đặt ra chức năng bắt buộc cho lớp con. Từ ví dụ sản phẩm đến dịch vụ thông báo, ta xem từng khái niệm tác động lên lớp, đối tượng và phương thức thế nào.

### 4.1. Inheritance — Kế thừa từ lớp cha

**Từ vựng trong mục:** **Inheritance** — kế thừa; **Parent/child class** — lớp cha/lớp con.

Cửa hàng có nhiều loại sản phẩm, nhưng mỗi món đều có tên. Lớp cha `Product` giữ tên chung, còn lớp con `Electronic(Product)` nhận lại cách lưu tên và có thêm thuộc tính riêng `warranty_months` (tháng bảo hành). `super().__init__(name)` gọi phương thức khởi tạo của lớp cha; nhờ vậy không phải viết lại cách lưu tên ở mọi loại sản phẩm. Đây là **kế thừa**: lớp con dùng lại và mở rộng hành vi, thuộc tính từ lớp cha.

```python
class Product:
    def __init__(self, name):
        self.name = name

class Electronic(Product):
    def __init__(self, name, warranty_months):
        super().__init__(name)
        self.warranty_months = warranty_months

phone = Electronic('Phone', 12)
print(phone.name, phone.warranty_months)
```

**Kết quả khi chạy:**

```text
Phone 12
```

`Phone` là tên được lớp cha khởi tạo; `12` là số tháng bảo hành được lớp con bổ sung.

### 4.2. Polymorphism — Đa hình

**Từ vựng trong mục:** **Polymorphism** — đa hình; **Method** — phương thức.

Giả sử ứng dụng có thông báo bằng email và tin nhắn. Cả hai đều có phương thức `send(message)`, nhưng kết quả khác nhau tùy loại. **Đa hình** nghĩa là code gọi cùng một tên phương thức trên các đối tượng khác nhau mà mỗi đối tượng tự quyết định cách xử lý. Vòng `for` phía dưới không cần viết hai nhánh kiểm tra loại thông báo.

```python
class Email:
    def send(self, message):
        return 'Email: ' + message

class SMS:
    def send(self, message):
        return 'SMS: ' + message

for sender in [Email(), SMS()]:
    print(sender.send('Hello'))
```

**Kết quả khi chạy:**

```text
Email: Hello
SMS: Hello
```

Cùng lời gọi `send('Hello')` nhưng hai loại đối tượng trả về hai kết quả khác nhau.

### 4.3. Abstract class — Lớp trừu tượng

**Từ vựng trong mục:** **Abstract class** — lớp trừu tượng; **Abstract method** — phương thức trừu tượng.

Khi mọi bộ gửi thông báo **bắt buộc** phải có `send()`, ta tạo lớp trừu tượng `Notifier(ABC)` và đánh dấu `@abstractmethod`. Lớp này quy định hợp đồng nhưng chưa đưa ra cách gửi cụ thể. Lớp `Console` phải cài đặt `send()` mới tạo đối tượng được. Chỉ kế thừa `ABC` mà **không có phương thức trừu tượng** thì chưa áp đặt yêu cầu đó.

```python
from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, message):
        pass

class Console(Notifier):
    def send(self, message):
        return 'Console: ' + message

print(Console().send('Hello'))
```

**Kết quả khi chạy:**

```text
Console: Hello
```

`Console` đáp ứng hợp đồng `send()`; nếu bỏ phương thức ấy khỏi `Console`, Python sẽ không cho khởi tạo đối tượng.

### 4.4. Override — Ghi đè phương thức

**Từ vựng trong mục:** **Override** — ghi đè; **Inheritance** — kế thừa.

Lớp cha `Shipping` có phí mặc định 0 đồng, nhưng giao hàng nhanh cần phí 35.000 đồng. Lớp con `Express` **ghi đè (override)** phương thức `fee()` bằng định nghĩa mới cùng tên. Khi gọi `Express().fee()`, Python dùng bản của `Express`, không dùng bản của `Shipping`. Đây là một cách để đa hình xuất hiện thông qua quan hệ kế thừa.

```python
class Shipping:
    def fee(self):
        return 0

class Express(Shipping):
    def fee(self):
        return 35000

print(Shipping().fee(), Express().fee())
```

**Kết quả khi chạy:**

```text
0 35000
```

Hai đối tượng gọi cùng `fee()` nhưng phí khác nhau: gói thường 0 đồng, gói nhanh 35.000 đồng.
## 5. Năm tình huống lập trình thực tế

### Tình huống 1 — Các loại sản phẩm

**Từ vựng trong mục:** **Inheritance** — kế thừa; **Method** — phương thức.

**Tình huống thực tế:** Cửa hàng có sản phẩm điện tử `Phone`. Hệ thống dùng lớp `Product` để lưu tên mọi sản phẩm và lớp `Electronic` để xác định nhóm hàng. Hãy in nhóm sản phẩm của chiếc điện thoại.

**Vì sao chọn cách giải này?** Lớp con tái sử dụng phương thức khởi tạo tên từ lớp cha và thêm phương thức phân nhóm.

**Quy trình giải:**

1. Định nghĩa `Product` lưu tên trong `self.name`.
2. Tạo `Electronic(Product)` với phương thức `category()`.
3. Tạo sản phẩm `Phone`, gọi phương thức phân nhóm và in kết quả.

```python
class Product:
    def __init__(self, name):
        self.name = name

class Electronic(Product):
    def category(self):
        return 'electronic'

print(Electronic('Phone').category())
```

**Kết quả khi chạy:**

```text
electronic
```

Điện thoại được xếp vào nhóm `electronic`; tên `Phone` được giữ qua phần khởi tạo của lớp cha.

### Tình huống 2 — Giao diện gửi thông báo

**Từ vựng trong mục:** **Abstract class** — lớp trừu tượng; **Abstract method** — phương thức trừu tượng.

**Tình huống thực tế:** Ứng dụng yêu cầu mọi bộ gửi thông báo phải có phương thức `send()`. Bộ gửi ra màn hình (`Console`) nhận nội dung `Hello`. Hãy dùng lớp trừu tượng để quy định giao diện và in thông điệp đã gửi.

**Vì sao chọn cách giải này?** `ABC` cùng `@abstractmethod` buộc lớp con triển khai phương thức, giúp tránh lớp gửi thông báo thiếu chức năng.

**Quy trình giải:**

1. Định nghĩa `Notifier(ABC)` với phương thức trừu tượng `send()`.
2. Cài đặt `send()` trong `Console` để tạo nội dung trả về.
3. Gọi `Console().send('Hello')` và in kết quả.

```python
from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, message):
        pass

class Console(Notifier):
    def send(self, message):
        return 'Sent:' + message

print(Console().send('Hello'))
```

**Kết quả khi chạy:**

```text
Sent:Hello
```

Phương thức `send()` của `Console` đã được định nghĩa; chương trình trả về chuỗi `Sent:Hello`.

### Tình huống 3 — Tính phí vận chuyển

**Từ vựng trong mục:** **Override** — ghi đè; **Inheritance** — kế thừa.

**Tình huống thực tế:** Một cửa hàng có dịch vụ vận chuyển thường miễn phí và giao nhanh tính 35.000 đồng mỗi đơn. Hãy in phí giao hàng nhanh bằng phương thức của lớp con.

**Vì sao chọn cách giải này?** Ghi đè `fee()` cho loại giao hàng nhanh mà vẫn giữ giao diện chung `fee()` của lớp cha.

**Quy trình giải:**

1. Lớp `Shipping` định nghĩa phí mặc định bằng 0.
2. Lớp `Express` kế thừa và ghi đè phí bằng 35000.
3. Tạo `Express`, gọi `fee()` và in số tiền.

```python
class Shipping:
    def fee(self):
        return 0

class Express(Shipping):
    def fee(self):
        return 35000

print(Express().fee())
```

**Kết quả khi chạy:**

```text
35000
```

Giá trị 35000 tương ứng 35.000 đồng phí giao nhanh; không dùng giá trị 0 của lớp cha.

### Tình huống 4 — Đọc nhiều loại cảm biến

**Từ vựng trong mục:** **Polymorphism** — đa hình; **Override** — ghi đè.

**Tình huống thực tế:** Hệ thống có một cảm biến nhiệt độ đo 26,5 °C và một cảm biến độ ẩm đo 62%. Cả hai phải có phương thức `read()`. Hãy đọc lần lượt hai cảm biến mà không cần kiểm tra loại trong vòng lặp.

**Vì sao chọn cách giải này?** Hai lớp con ghi đè `read()`, cho phép vòng lặp gọi cùng phương thức trên cả hai đối tượng.

**Quy trình giải:**

1. Tạo lớp chung `Sensor` có `read()`.
2. Hai lớp `Temp` và `Humidity` cài đặt kết quả đọc riêng.
3. Duyệt hai đối tượng và in kết quả từng lời gọi `read()`.

```python
class Sensor:
    def read(self):
        return 0

class Temp(Sensor):
    def read(self):
        return 26.5

class Humidity(Sensor):
    def read(self):
        return 62

for sensor in [Temp(), Humidity()]:
    print(sensor.read())
```

**Kết quả khi chạy:**

```text
26.5
62
```

Dòng đầu là 26,5 °C; dòng thứ hai là 62% độ ẩm. Chương trình chỉ in số, đơn vị được giải thích trong bài.

### Tình huống 5 — Chuyển định dạng báo cáo

**Từ vựng trong mục:** **Override** — ghi đè; **Method** — phương thức.

**Tình huống thực tế:** Hệ thống có lớp báo cáo thường trả chữ `plain`. Báo cáo HTML cần tạo chuỗi `<p>report</p>`. Hãy in nội dung báo cáo HTML bằng cùng phương thức `render()`.

**Vì sao chọn cách giải này?** Lớp `HtmlReport` ghi đè `render()` của lớp cha để trả định dạng HTML.

**Quy trình giải:**

1. Lớp cha `Report` định nghĩa `render()` cho văn bản thường.
2. Lớp con `HtmlReport` định nghĩa lại `render()` cho HTML.
3. Tạo `HtmlReport` và in kết quả.

```python
class Report:
    def render(self):
        return 'plain'

class HtmlReport(Report):
    def render(self):
        return '<p>report</p>'

print(HtmlReport().render())
```

**Kết quả khi chạy:**

```text
<p>report</p>
```

Đầu ra là chuỗi thẻ HTML; `print()` không biến chuỗi thành trang web.
## 6. Sai lầm thường gặp

- **Kế thừa** không tự biến mọi phương thức thành đa hình; lớp con có thể dùng lại hoặc ghi đè tùy nhu cầu.
- Kế thừa `ABC` **chưa đủ** để buộc lớp con triển khai phương thức; cần thêm `@abstractmethod`.
- `super().__init__(...)` dùng logic khởi tạo của lớp cha; nếu bỏ khi cần, thuộc tính chung như `name` có thể chưa được tạo.
- Ghi đè phương thức phải dùng đúng tên và cách nhận tham số phù hợp; khác tên sẽ là phương thức mới.
- Ví dụ cảm biến in hai giá trị có **đơn vị khác nhau**: không được cộng trực tiếp 26,5 °C và 62%.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What does class inheritance primarily enable? — Kế thừa lớp chủ yếu giúp gì?**

A. Reuse or extend parent-class behavior — Dùng lại hoặc mở rộng hành vi class cha

B. Create copies of all existing parent instances — Sao chép mọi instance cha đang tồn tại

C. Guarantee all subclasses have identical state — Bắt buộc mọi class con có trạng thái giống hệt

D. Convert the parent class to a function — Chuyển class cha thành hàm

**Q2. What does `class Dog(Animal):` express? — `class Dog(Animal):` thể hiện điều gì?**

A. `Dog` inherits from `Animal` — `Dog` kế thừa `Animal`

B. `Animal` inherits from `Dog` — `Animal` kế thừa `Dog`

C. `Dog` is an instance of `Animal` — `Dog` là instance của `Animal`

D. `Dog` is a method inside `Animal` — `Dog` là phương thức bên trong `Animal`

**Q3. Why call `super().__init__(name)` in a subclass? — Vì sao lớp con gọi `super().__init__(name)`?**

A. Remove parent methods from the subclass — Xóa phương thức cha khỏi class con

B. Make the subclass automatically abstract — Tự biến class con thành class trừu tượng

C. Initialize parent-defined instance state — Khởi tạo trạng thái instance do class cha định nghĩa

D. Create a second, unrelated parent instance — Tạo instance cha thứ hai không liên quan

**Q4. Which statement best describes polymorphism? — Câu nào mô tả đúng đa hình?**

A. Every method must have a distinct name — Mọi phương thức phải có tên khác nhau

B. Only one class can provide a method named `speak` — Chỉ một class được có phương thức tên `speak`

C. Different objects can implement the same expected operation — Các đối tượng khác nhau có thể cài cùng thao tác dự kiến

D. All objects must have identical attribute values — Mọi đối tượng phải có thuộc tính bằng nhau

**Q5. What is method overriding? — Ghi đè phương thức là gì?**

A. Delete all methods from the parent class — Xóa mọi phương thức khỏi class cha

B. Change only a local variable inside a method — Chỉ đổi biến cục bộ bên trong phương thức

C. Define a same-named method in the subclass — Định nghĩa phương thức cùng tên tại class con

D. Call an inherited method without changing it — Chỉ gọi phương thức kế thừa và không đổi gì

**Q6. What does `@abstractmethod` mark? — `@abstractmethod` đánh dấu điều gì?**

A. A method forbidden from containing any code — Phương thức bị cấm chứa mã

B. A static method with no arguments — Phương thức tĩnh không có đối số

C. A method automatically called after `print` — Phương thức được tự gọi sau `print`

D. An abstract method requirement for concrete subclasses — Yêu cầu phương thức phải được class cụ thể đáp ứng

**Q7. Is inheriting from `ABC` alone enough to require an override? — Chỉ kế thừa `ABC` có buộc ghi đè phương thức không?**

A. No; specific methods must be marked abstract — Không; cần đánh dấu phương thức trừu tượng cụ thể

B. Yes; every method becomes abstract by default — Có; mặc định mọi phương thức đều trừu tượng

C. Yes; all subclass instance attributes must be removed — Có; phải xóa mọi thuộc tính instance của class con

D. No; `ABC` cannot be subclassed — Không; không thể kế thừa `ABC`

**Q8. What happens if an abstract method is left unimplemented? — Điều gì xảy ra nếu phương thức trừu tượng chưa được cài đặt?**

A. The missing method is filled with `return None` automatically — Phương thức thiếu được tự thêm `return None`

B. The subclass loses all inherited attributes — Class con mất mọi thuộc tính kế thừa

C. The abstract method is executed once on construction — Phương thức trừu tượng chạy một lần khi khởi tạo

D. The subclass remains abstract and instantiation fails — Class con vẫn trừu tượng và việc tạo instance thất bại

**Q9. What does `isinstance(obj, Parent)` check? — `isinstance(obj, Parent)` kiểm tra gì?**

A. Whether `obj` has exactly the class `Parent` only — `obj` có đúng duy nhất class `Parent` không

B. Whether `Parent` has an empty method body — `Parent` có thân phương thức rỗng không

C. Whether `obj` contains a string attribute — `obj` có thuộc tính chuỗi không

D. Whether `obj` is an instance of `Parent` or a subclass — `obj` có thuộc `Parent` hoặc class con không

**Q10. If a child overrides `fee()`, which version runs on `Child().fee()`? — Nếu lớp con ghi đè `fee()`, `Child().fee()` chạy bản nào?**

A. No method, because overriding causes an error — Không chạy bản nào vì ghi đè gây lỗi

B. The child's overriding implementation — Bản ghi đè của class con

C. The parent's implementation always — Luôn là bản của class cha

D. Both methods automatically in sequence — Tự động chạy cả hai phương thức liên tiếp

**Q11. Can a child access an inherited attribute set in the parent initializer? — Lớp con có thể dùng thuộc tính khởi tạo ở lớp cha không?**

A. Only if the subclass overrides every method — Chỉ nếu class con ghi đè mọi phương thức

B. Yes, when required parent state has been initialized — Có, khi trạng thái cha cần thiết đã được khởi tạo

C. No, subclass methods can never see attributes set by a parent — Không, phương thức con không bao giờ thấy thuộc tính do cha tạo

D. Only if the attribute is an integer — Chỉ nếu thuộc tính là số nguyên

**Q12. Must polymorphic objects share exactly the same class? — Đối tượng đa hình có bắt buộc cùng một class không?**

A. No; different classes may support the same operation — Không; các class khác nhau có thể hỗ trợ cùng thao tác

B. Yes; every polymorphic object must be the same class — Có; mọi đối tượng đa hình phải cùng class

C. Yes; all polymorphic objects must share all attribute values — Có; mọi đối tượng đa hình phải có mọi thuộc tính bằng nhau

D. No; polymorphism means there are no methods at all — Không; đa hình nghĩa là không có phương thức

**Q13. What does `self` refer to inside an instance method? — `self` trong phương thức đối tượng chỉ gì?**

A. The current Python module — Module Python hiện tại

B. The current instance receiving the call — Instance hiện tại đang nhận lời gọi

C. The parent class definition only — Chỉ định nghĩa class cha

D. Every object belonging to that class — Mọi đối tượng thuộc class đó

**Q14. Does overriding a method erase it from the parent class? — Ghi đè phương thức có xóa bản lớp cha không?**

A. Yes; every parent instance loses its methods — Có; mọi instance cha mất phương thức

B. Only if the method uses `print()` — Chỉ khi phương thức dùng `print()`

C. No; the parent's original method remains defined — Không; phương thức gốc của class cha vẫn tồn tại

D. Yes; overriding deletes the method from the parent class — Có; ghi đè xóa phương thức khỏi class cha

**Q15. How can an override call the parent's implementation? — Phương thức ghi đè gọi bản của lớp cha bằng gì?**

A. `None.method()` — `None.method()`

B. `del Parent.method` — `del Parent.method`

C. `print(super)` — `print(super)`

D. `super().method()` — `super().method()`

**Q16. Can an abstract class define ordinary implemented methods? — Lớp trừu tượng có thể có phương thức thông thường đã triển khai không?**

A. Only if the class has no subclasses — Chỉ khi class không có class con

B. Yes; reusable methods can coexist with abstract methods — Có; phương thức dùng chung có thể cùng tồn tại với phương thức trừu tượng

C. No; abstract classes can contain only `pass` — Không; class trừu tượng chỉ được có `pass`

D. No; abstract classes cannot define attributes — Không; class trừu tượng không thể có thuộc tính

**Q17. What is the relation between overriding and polymorphism? — Ghi đè liên quan gì đến đa hình?**

A. Overriding prevents calls on subclasses — Ghi đè ngăn lời gọi trên class con

B. Overriding forces different method names — Ghi đè buộc phương thức có tên khác nhau

C. Polymorphism only applies when no method is overridden — Đa hình chỉ tồn tại khi không ghi đè

D. Overriding can supply different behavior for one method name — Ghi đè cho phép hành vi khác nhau với cùng tên phương thức

**Q18. Which part of `class Child(Parent):` names the superclass? — Trong `class Child(Parent):`, đâu là tên lớp cha?**

A. `:` — `:`

B. `Parent` — `Parent`

C. `Child` — `Child`

D. `class` — `class`

**Q19. What is a good reason to create a shared base class? — Khi nào nên tạo lớp cha chung?**

A. Related subclasses share meaningful state or behavior — Các class con liên quan có trạng thái hoặc hành vi chung

B. The objects have no common behavior at all — Các đối tượng không có hành vi chung nào

C. Every subclass must contain completely unrelated logic — Mỗi class con buộc có logic hoàn toàn không liên quan

D. Every variable must be made global — Mọi biến phải chuyển thành biến toàn cục

**Q20. Which error may follow if a child skips necessary parent initialization? — Nếu lớp con bỏ khởi tạo lớp cha cần thiết, điều gì có thể xảy ra?**

A. Every integer becomes a string — Mọi số nguyên biến thành chuỗi

B. All subclass methods must execute twice — Mọi phương thức class con phải chạy hai lần

C. An expected inherited instance attribute may be missing — Thuộc tính instance kế thừa được mong đợi có thể bị thiếu

D. The entire parent class is automatically deleted — Toàn bộ class cha tự bị xóa

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **A** | Inheritance allows a subclass to reuse or extend code from a parent class, such as shared `name` handling in `Animal` and extra `bark()` behavior in `Dog`. It does not copy every live object; it establishes a relationship between classes. | Kế thừa cho phép class con dùng lại hoặc mở rộng mã của class cha, ví dụ `Animal` quản lý `name` còn `Dog` bổ sung `bark()`. Cơ chế này không sao chép mọi đối tượng đang tồn tại mà thiết lập quan hệ giữa các class. |
| Q2 | **A** | In `class Dog(Animal):`, the class name before parentheses is `Dog` and the parent class named inside is `Animal`. This declares an inheritance relationship; it does not instantiate either class. | Trong `class Dog(Animal):`, `Dog` là class đang được định nghĩa còn `Animal` trong ngoặc là class cha. Đây là khai báo kế thừa, không tự tạo instance của class nào. |
| Q3 | **C** | `super().__init__(name)` delegates initialization to the next initializer in the method resolution order, commonly setting inherited state such as `self.name`. Without that needed initialization, later methods may find the attribute missing. | `super().__init__(name)` chuyển việc khởi tạo tới phương thức tiếp theo trong thứ tự phân giải phương thức, thường thiết lập trạng thái kế thừa như `self.name`. Nếu bỏ bước cần thiết này, các phương thức sau có thể không tìm thấy thuộc tính. |
| Q4 | **C** | Polymorphism means different objects can respond to the same expected operation in their own ways. For example, both `Dog.speak()` and `Cat.speak()` may be called as `animal.speak()` while producing different sounds. | Đa hình nghĩa là các đối tượng khác nhau có thể đáp ứng cùng một thao tác theo cách riêng. Ví dụ `Dog.speak()` và `Cat.speak()` đều có thể được gọi qua `animal.speak()` nhưng tạo âm thanh khác nhau. |
| Q5 | **C** | Overriding occurs when a subclass defines a method with the same name as an inherited method, providing a more specific implementation. A child `speak()` is then chosen for a child instance, without deleting the parent's method. | Ghi đè xảy ra khi class con định nghĩa phương thức cùng tên với phương thức kế thừa để thay cách triển khai. Instance con sẽ chọn `speak()` của class con mà không xóa phương thức của class cha. |
| Q6 | **D** | With Python's `ABC` machinery, `@abstractmethod` marks a method requirement for concrete subclasses. A class with unresolved abstract methods cannot be instantiated, although the abstract method itself may contain reusable code. | Với cơ chế `ABC` của Python, `@abstractmethod` đánh dấu phương thức cần được triển khai để class trở thành cụ thể. Class còn phương thức trừu tượng chưa được đáp ứng thì không khởi tạo được, dù bản thân phương thức trừu tượng vẫn có thể chứa mã. |
| Q7 | **A** | Inheriting `ABC` does not automatically make every method abstract. A requirement exists only when a method is marked appropriately, such as with `@abstractmethod`; ordinary implemented methods may still be inherited as normal. | Kế thừa `ABC` không tự khiến mọi phương thức trở thành trừu tượng. Yêu cầu chỉ hình thành khi phương thức được đánh dấu phù hợp, ví dụ `@abstractmethod`; phương thức thường đã triển khai vẫn được kế thừa như bình thường. |
| Q8 | **D** | A subclass that still has an unimplemented abstract method remains abstract and normally cannot be instantiated. Python raises `TypeError` when attempting to create such an instance; it does not silently skip the requirement. | Class con còn phương thức trừu tượng chưa triển khai thì vẫn trừu tượng và thông thường không thể tạo instance. Python phát sinh `TypeError` khi cố khởi tạo, không tự bỏ qua yêu cầu. |
| Q9 | **D** | `isinstance(obj, Parent)` tests whether the object is an instance of `Parent` or an inherited subclass. A `Child` instance can therefore pass the test, unlike the exact-class comparison `type(obj) is Parent`. | `isinstance(obj, Parent)` kiểm tra đối tượng có là instance của `Parent` hoặc class con kế thừa không. Vì thế instance `Child` cũng có thể thỏa, khác phép so class chính xác `type(obj) is Parent`. |
| Q10 | **B** | When a child overrides `fee()`, method lookup on a `Child` instance selects the child implementation. The parent's method is not automatically run as well; the child can explicitly delegate using `super().fee()` if needed. | Khi class con ghi đè `fee()`, tra cứu phương thức trên instance `Child` sẽ chọn bản của class con. Bản cha không tự chạy cùng lúc; class con có thể chủ động gọi qua `super().fee()` khi cần. |
| Q11 | **B** | An inherited instance attribute exists when suitable initialization creates it, often by calling the parent's `__init__`. A child can then read `self.name`, but merely declaring inheritance does not automatically execute every custom parent initializer. | Thuộc tính instance kế thừa tồn tại khi bước khởi tạo phù hợp đã tạo nó, thường nhờ gọi `__init__` của class cha. Class con có thể đọc `self.name`, nhưng chỉ khai báo kế thừa không tự chạy mọi hàm khởi tạo cha tùy chỉnh. |
| Q12 | **A** | Polymorphism depends on a shared expected interface or operation, not identical concrete classes. Separate classes may both provide `draw()` so client code can call it on either object. | Đa hình phụ thuộc vào giao diện hoặc thao tác dự kiến dùng chung, không bắt buộc class cụ thể giống nhau. Hai class riêng biệt có thể đều cung cấp `draw()` để mã gọi sử dụng được trên cả hai. |
| Q13 | **B** | `self` conventionally refers to the object on which an instance method is called. Reading `self.name` on two different instances may return different values, even when the method code is shared. | `self` theo quy ước chỉ đối tượng mà phương thức instance đang được gọi trên đó. Đọc `self.name` ở hai instance khác nhau có thể cho giá trị khác dù dùng chung mã phương thức. |
| Q14 | **C** | Overriding changes which implementation method lookup selects on a child, not the parent's class definition. A parent instance can still invoke the original method; `super()` can often access it from the child. | Ghi đè thay đổi bản triển khai được chọn khi tra cứu trên class con, không xóa định nghĩa class cha. Instance cha vẫn gọi được phương thức gốc; class con thường có thể truy cập qua `super()`. |
| Q15 | **D** | `super().method()` delegates to the next implementation according to the method resolution order, often the parent method in simple inheritance. This allows a child override to extend parent behavior rather than duplicate it. | `super().method()` chuyển lời gọi tới bản triển khai kế tiếp theo thứ tự phân giải phương thức, thường là class cha trong kế thừa đơn. Nhờ đó phương thức ghi đè có thể mở rộng hành vi của cha thay vì chép lại. |
| Q16 | **B** | An abstract class can provide ordinary implemented methods alongside abstract requirements. For example, a base shape may implement `describe()` but require subclasses to implement `area()`. | Class trừu tượng có thể có phương thức thường đã triển khai cùng với phương thức bắt buộc. Ví dụ class hình học cơ sở cài `describe()` nhưng yêu cầu class con cài `area()`. |
| Q17 | **D** | Overriding is one way to implement polymorphism: a shared call such as `animal.speak()` can execute different subclass implementations. Overriding is not required for all forms of polymorphism, such as duck typing. | Ghi đè là một cách tạo đa hình: lời gọi chung như `animal.speak()` có thể chạy các bản triển khai khác nhau của class con. Tuy nhiên không phải mọi dạng đa hình đều bắt buộc ghi đè, ví dụ duck typing. |
| Q18 | **B** | In `class Child(Parent):`, the name in the parentheses is the superclass, so `Parent` is inherited by `Child`. `Child` is the new subclass name, and `class` is a declaration keyword. | Trong `class Child(Parent):`, tên trong ngoặc là class cha nên `Parent` được `Child` kế thừa. `Child` là tên class con mới, còn `class` là từ khóa khai báo. |
| Q19 | **A** | A shared base class is useful when related subclasses have common state or behavior, such as a common `name` field. It avoids duplicated definitions while allowing each subclass to specialize its own behavior. | Class cha chung có ích khi các class con liên quan dùng chung trạng thái hoặc hành vi, như trường `name`. Cách này giảm định nghĩa lặp và vẫn cho phép mỗi class con triển khai phần riêng. |
| Q20 | **C** | If a subclass skips necessary parent initialization, parent-defined fields such as `self.name` may never be created. Accessing a missing field normally raises `AttributeError`; calling `super().__init__` or properly reproducing the setup prevents that. | Nếu class con bỏ bước khởi tạo cha cần thiết, các trường do cha thiết lập như `self.name` có thể chưa được tạo. Truy cập trường thiếu thường gây `AttributeError`; gọi `super().__init__` hoặc thực hiện khởi tạo tương đương sẽ ngăn lỗi. |

## 8. Nối sang bài tiếp theo

`Class/Object → Inheritance → Abstract API → Kiến trúc ứng dụng`.

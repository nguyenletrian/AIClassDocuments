# PY-11 — Kế thừa, đa hình và lớp trừu tượng ABC


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Inheritance** — kế thừa; **Polymorphism** — đa hình.

`Class/Object → Inheritance → Abstract API → Kiến trúc ứng dụng`

**Học xong dùng để làm gì?** Dùng chung thao tác cho nhiều loại đối tượng, ví dụ các loại phí có công thức khác nhau.

**Kết nối kiến thức tiếp theo:** PY-12 đọc và lưu dữ liệu từ file/CSV, có xử lý lỗi.

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
# Mục đích: Kế thừa từ lớp cha.
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
# Mục đích: Đa hình.
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
# Mục đích: Lớp trừu tượng.
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
# Mục đích: Ghi đè phương thức.
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
# Mục đích: Các loại sản phẩm.
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
# Mục đích: Giao diện gửi thông báo.
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
# Mục đích: Tính phí vận chuyển.
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
# Mục đích: Đọc nhiều loại cảm biến.
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
# Mục đích: Chuyển định dạng báo cáo.
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

## 7. Trắc nghiệm

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What does class inheritance primarily enable? | Kế thừa lớp chủ yếu giúp gì?**

A. Convert a class into a file | Chuyển lớp thành tệp

B. Reuse and extend behavior of a parent class | Dùng lại và mở rộng hành vi của lớp cha

C. Copy every object in memory | Sao chép mọi đối tượng trong bộ nhớ

D. Prevent all method calls | Ngăn mọi lời gọi phương thức

**Đáp án: B**

**Giải thích:** Kế thừa giúp lớp con dùng lại phương thức của lớp cha và bổ sung hành vi riêng. Ví dụ `Dog(Animal)` có thể kế thừa `eat()` rồi thêm `bark()`; kế thừa không sao chép mọi đối tượng đã tạo.


**Q2. What does `class Dog(Animal):` express? | `class Dog(Animal):` thể hiện điều gì?**

A. Dog inherits from Animal | Dog kế thừa Animal

B. Dog is a function inside Animal | Dog là hàm trong Animal

C. Animal inherits from Dog | Animal kế thừa Dog

D. Dog is an instance of Animal | Dog là đối tượng tạo từ Animal

**Đáp án: A**

**Giải thích:** Trong `class Dog(Animal):`, `Dog` là lớp con còn `Animal` là lớp cơ sở. Cú pháp khai báo quan hệ kế thừa, không tạo đối tượng `Dog` mới hay một hàm bên trong `Animal`.


**Q3. Why call `super().__init__(name)` in a subclass? | Vì sao lớp con gọi `super().__init__(name)`?**

A. To delete the parent class | Để xóa lớp cha

B. To replace every attribute with None | Để thay mọi thuộc tính bằng None

C. To make the child an abstract class | Để biến lớp con thành lớp trừu tượng

D. To initialize inherited parent state | Để khởi tạo dữ liệu chung từ lớp cha

**Đáp án: D**

**Giải thích:** `super().__init__(name)` chuyển việc khởi tạo cho lớp kế tiếp trong thứ tự phân giải phương thức, thường là lớp cha. Nếu hàm đó gán `self.name`, lớp con dùng được thuộc tính ấy mà không phải viết lặp phần khởi tạo.


**Q4. Which statement best describes polymorphism? | Câu nào mô tả đúng đa hình?**

A. A child class cannot override methods | Lớp con không thể ghi đè phương thức

B. All methods must have different names | Mọi phương thức phải có tên khác nhau

C. Different objects respond to the same method call | Các đối tượng khác nhau xử lý cùng một lời gọi phương thức

D. All objects must store identical values | Mọi đối tượng phải có giá trị giống nhau

**Đáp án: C**

**Giải thích:** Đa hình cho phép mã gọi cùng một thao tác trên nhiều đối tượng tương thích. Chẳng hạn `dog.sound()` và `cat.sound()` có thể cho âm thanh khác nhau dù đều gọi `sound()`.


**Q5. What is method overriding? | Ghi đè phương thức là gì?**

A. Removing every inherited attribute | Xóa mọi thuộc tính kế thừa

B. Calling the parent method unchanged | Gọi nguyên phương thức lớp cha

C. Defining a same-named method in a subclass | Định nghĩa lại phương thức cùng tên ở lớp con

D. Changing a local variable only | Chỉ thay đổi một biến cục bộ

**Đáp án: C**

**Giải thích:** Ghi đè xảy ra khi lớp con định nghĩa phương thức trùng tên với phương thức kế thừa. Gọi trên đối tượng lớp con thường chọn bản của lớp con, nhưng phương thức gốc của lớp cha vẫn tồn tại.


**Q6. What does `@abstractmethod` mark? | `@abstractmethod` đánh dấu điều gì?**

A. A property unique to integers | Thuộc tính riêng của số nguyên

B. A method that can never be called | Phương thức không bao giờ được gọi

C. A method that prints automatically | Phương thức tự động in

D. A method subclasses must implement to become concrete | Phương thức lớp con phải triển khai để có thể khởi tạo

**Đáp án: D**

**Giải thích:** Khi lớp dùng cơ chế ABC của Python, `@abstractmethod` đánh dấu yêu cầu mà lớp con cụ thể phải đáp ứng. Phương thức trừu tượng vẫn có thể có phần thân; hạn chế nằm ở việc tạo đối tượng từ lớp còn yêu cầu trừu tượng chưa hoàn thành.


**Q7. Is inheriting from `ABC` alone enough to require an override? | Chỉ kế thừa `ABC` có buộc ghi đè phương thức không?**

A. Yes, every method becomes abstract | Có, mọi phương thức đều trừu tượng

B. No, an abstract method must be declared | Không, cần khai báo phương thức trừu tượng

C. Yes, all subclass methods are deleted | Có, mọi phương thức lớp con bị xóa

D. No, ABC forbids inheritance | Không, ABC cấm kế thừa

**Đáp án: B**

**Giải thích:** Kế thừa `ABC` bật cơ chế lớp trừu tượng nhưng không tự khiến mọi phương thức thành trừu tượng. Khai báo `@abstractmethod` phía trên `def area(self):` mới đặt ra yêu cầu trừu tượng cụ thể.


**Q8. What happens if an abstract method is left unimplemented? | Điều gì xảy ra nếu phương thức trừu tượng chưa được cài đặt?**

A. The concrete instance cannot be created | Không thể tạo đối tượng từ lớp còn phương thức trừu tượng

B. The method automatically sends an email | Phương thức tự gửi email

C. The base class is erased | Lớp cha bị xóa

D. Python silently returns zero | Python âm thầm trả về 0

**Đáp án: A**

**Giải thích:** Nếu lớp con vẫn còn phương thức trừu tượng, Python từ chối tạo instance và báo `TypeError`. Cài đặt đầy đủ các phương thức bắt buộc mới giúp lớp có thể khởi tạo; chỉ kế thừa tên phương thức là chưa đủ.


**Q9. What does `isinstance(obj, Parent)` check? | `isinstance(obj, Parent)` kiểm tra gì?**

A. Whether obj is an instance of Parent or its subclasses | obj có thuộc Parent hoặc lớp con hay không

B. Whether obj is a string | obj có phải chuỗi không

C. Whether Parent has no methods | Parent có rỗng phương thức không

D. Whether obj has been printed | obj đã được in hay chưa

**Đáp án: A**

**Giải thích:** `isinstance(obj, Parent)` kiểm tra đối tượng thuộc `Parent` hoặc lớp con tương thích và trả Boolean. Với `Child(Parent)` thông thường, `isinstance(Child(), Parent)` là `True`, khác phép kiểm tra chính xác `type(obj) is Parent`.


**Q10. If a child overrides `fee()`, which version runs on `Child().fee()`? | Nếu lớp con ghi đè `fee()`, `Child().fee()` chạy bản nào?**

A. The parent's version in every case | Luôn bản của lớp cha

B. Neither version | Không chạy bản nào

C. The child's version | Bản của lớp con

D. Both versions automatically | Tự động chạy cả hai bản

**Đáp án: C**

**Giải thích:** Tra cứu phương thức trên instance ưu tiên bản ghi đè ở `Child` trước phương thức cùng tên được kế thừa. Vì vậy `Child().fee()` chạy bản lớp con; bản lớp cha chỉ chạy thêm nếu phương thức ghi đè chủ động gọi nó.


**Q11. Can a child access an inherited attribute set in the parent initializer? | Lớp con có thể dùng thuộc tính khởi tạo ở lớp cha không?**

A. Only if the attribute is named `class` | Chỉ khi tên thuộc tính là class

B. Yes, if the parent initialization is performed | Có, nếu đã thực hiện khởi tạo lớp cha

C. No, inherited fields are always hidden | Không, thuộc tính kế thừa luôn bị ẩn

D. Only for integer attributes | Chỉ với thuộc tính số nguyên

**Đáp án: B**

**Giải thích:** Lớp con đọc được thuộc tính instance đã được phần khởi tạo thích hợp tạo ra. Nếu `Parent.__init__` gán `self.name`, lớp con gọi `super().__init__(name)` sẽ dùng được `self.name`; bỏ bước cần thiết có thể khiến thuộc tính chưa tồn tại.


**Q12. Must polymorphic objects share exactly the same class? | Đối tượng đa hình có bắt buộc cùng một class không?**

A. Yes, they must be identical objects | Có, phải là cùng một đối tượng

B. Yes, inheritance is forbidden | Có, không được kế thừa

C. No, they can provide the same expected method | Không, có thể thuộc các lớp khác nhau nhưng cùng phương thức

D. No, methods must all be absent | Không, không được có phương thức

**Đáp án: C**

**Giải thích:** Đa hình dựa vào giao diện thao tác chung, không yêu cầu các đối tượng cùng lớp cụ thể. Hàm gọi `obj.sound()` có thể làm việc với `Dog` và `Cat` nếu cả hai cung cấp phương thức đó, dù cách triển khai khác nhau.


**Q13. What does `self` refer to inside an instance method? | `self` trong phương thức đối tượng chỉ gì?**

A. Every object in the program | Toàn bộ đối tượng của chương trình

B. The current object receiving the call | Đối tượng hiện tại đang nhận lời gọi

C. Only the parent class definition | Chỉ phần định nghĩa lớp cha

D. The name of the Python module | Tên module Python

**Đáp án: B**

**Giải thích:** Trong phương thức instance thông thường, `self` là đối tượng cụ thể đang nhận lời gọi. Vì vậy `self.name` của `dog1` có thể khác `self.name` của `dog2`; `self` không phải lớp cha hay module.


**Q14. Does overriding a method erase it from the parent class? | Ghi đè phương thức có xóa bản lớp cha không?**

A. Yes, it deletes all parent code | Có, xóa toàn bộ code lớp cha

B. Yes, it deletes the class name | Có, xóa tên lớp

C. Only when `print()` is used | Chỉ khi dùng print

D. No, the parent method still exists | Không, phương thức của lớp cha vẫn tồn tại

**Đáp án: D**

**Giải thích:** Ghi đè ở lớp con thay đổi phương thức được dùng bởi đối tượng lớp con chứ không xóa định nghĩa trên `Parent`. `Parent().fee()` vẫn dùng bản của cha, còn `Child().fee()` có thể dùng bản ghi đè.


**Q15. How can an override call the parent's implementation? | Phương thức ghi đè gọi bản của lớp cha bằng gì?**

A. `super().method()` | `super().method()`

B. `None.method()` | `None.method()`

C. `print(super)` only | Chỉ `print(super)`

D. `del Parent` | `del Parent`

**Đáp án: A**

**Giải thích:** Trong phương thức ghi đè, `super().method()` chuyển lời gọi tới bản kế tiếp trong thứ tự phân giải phương thức, thường là lớp cha. Nó không gọi tùy ý một lớp bất kỳ; với đa kế thừa, lớp kế tiếp có thể khác lớp cha trực tiếp.


**Q16. Can an abstract class define ordinary implemented methods? | Lớp trừu tượng có thể có phương thức thông thường đã triển khai không?**

A. No, it cannot define attributes | Không, không thể có thuộc tính

B. No, it must only contain pass | Không, chỉ được chứa pass

C. Only when it has no subclasses | Chỉ khi không có lớp con

D. Yes, it can provide reusable behavior too | Có, nó vẫn có thể cung cấp hành vi dùng chung

**Đáp án: D**

**Giải thích:** Lớp trừu tượng có thể vừa có hàm hỗ trợ đã cài đặt vừa có yêu cầu trừu tượng. Chẳng hạn lớp cung cấp `describe()` nhưng buộc lớp con triển khai `area()`; trừu tượng không có nghĩa mọi phương thức phải rỗng.


**Q17. What is the relation between overriding and polymorphism? | Ghi đè liên quan gì đến đa hình?**

A. They both mean deleting attributes | Cả hai đều là xóa thuộc tính

B. Overriding can provide distinct behavior for a common call | Ghi đè tạo hành vi khác nhau cho cùng lời gọi

C. They only apply to CSV files | Chúng chỉ áp dụng cho CSV

D. Overriding prevents polymorphism | Ghi đè ngăn đa hình

**Đáp án: B**

**Giải thích:** Ghi đè là một cách thực hiện đa hình: các lớp con cung cấp thân hàm khác nhau cho cùng tên phương thức. Mã có thể gọi `shape.area()` mà không cần tự chọn hàm riêng cho từng loại hình.


**Q18. Which part of `class Child(Parent):` names the superclass? | Trong `class Child(Parent):`, đâu là tên lớp cha?**

A. `class` | `class`

B. `Child` | `Child`

C. `Parent` | `Parent`

D. `:` | `:`

**Đáp án: C**

**Giải thích:** Trong dòng `class Child(Parent):`, tên bên trong ngoặc là lớp cơ sở `Parent`. Lớp mới đang được khai báo là `Child`; dấu hai chấm mở đầu phần thân lớp được thụt lề.


**Q19. What is a good reason to create a shared base class? | Khi nào nên tạo lớp cha chung?**

A. To avoid using any methods | Để không cần phương thức

B. Every object is unrelated | Mọi đối tượng hoàn toàn không liên quan

C. To make all values constant | Để mọi giá trị là hằng số

D. Several subclasses share data or behavior | Nhiều lớp con có chung dữ liệu hoặc hành vi

**Đáp án: D**

**Giải thích:** Lớp cha chung hữu ích khi nhiều lớp con có trạng thái hoặc hành vi giống nhau. Ví dụ `Car` và `Bike` có thể dùng chung giao diện `Vehicle` thay vì lặp định nghĩa cùng hợp đồng phương thức ở từng lớp.


**Q20. Which error may follow if a child skips necessary parent initialization? | Nếu lớp con bỏ khởi tạo lớp cha cần thiết, điều gì có thể xảy ra?**

A. An expected inherited instance attribute may be missing | Một thuộc tính đối tượng cần thiết có thể chưa được tạo

B. All integers turn into strings | Mọi số nguyên biến thành chuỗi

C. Python automatically runs CSV conversion | Python tự chuyển CSV

D. Every method prints twice | Mọi phương thức in hai lần

**Đáp án: A**

**Giải thích:** Nếu lớp con ghi đè `__init__` mà bỏ phần khởi tạo cần thiết của cha, các trường dự kiến có thể chưa được tạo. Đọc `self.name` sau đó có thể gây `AttributeError`; Python không tự gọi hàm khởi tạo cha đã bị ghi đè.

## 8. Nối sang bài tiếp theo

`Class/Object → Inheritance → Abstract API → Kiến trúc ứng dụng`.

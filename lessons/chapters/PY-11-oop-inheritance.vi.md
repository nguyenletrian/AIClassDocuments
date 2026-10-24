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


**Q1. Which description matches Inheritance? — Mô tả nào đúng với Inheritance?**

A. A different concept described as Cùng lời gọi nhưng các lớp có cách đáp khác nhau — Cùng lời gọi nhưng các lớp có cách đáp khác nhau

B. The concept described as Lớp con dùng lại các đặc điểm lớp cha — Lớp con dùng lại các đặc điểm lớp cha

C. A different concept described as Khung lớp ràng buộc phương thức cần cài đặt — Khung lớp ràng buộc phương thức cần cài đặt

D. A different concept described as Lớp con cài lại phương thức của lớp cha — Lớp con cài lại phương thức của lớp cha


**Q2. Which description matches Polymorphism? — Mô tả nào đúng với Polymorphism?**

A. The concept described as Cùng lời gọi nhưng các lớp có cách đáp khác nhau — Cùng lời gọi nhưng các lớp có cách đáp khác nhau

B. A different concept described as Khung lớp ràng buộc phương thức cần cài đặt — Khung lớp ràng buộc phương thức cần cài đặt

C. A different concept described as Lớp con cài lại phương thức của lớp cha — Lớp con cài lại phương thức của lớp cha

D. A different concept described as Lớp con dùng lại các đặc điểm lớp cha — Lớp con dùng lại các đặc điểm lớp cha


**Q3. Which description matches Abstract class? — Mô tả nào đúng với Abstract class?**

A. A different concept described as Lớp con cài lại phương thức của lớp cha — Lớp con cài lại phương thức của lớp cha

B. A different concept described as Lớp con dùng lại các đặc điểm lớp cha — Lớp con dùng lại các đặc điểm lớp cha

C. A different concept described as Cùng lời gọi nhưng các lớp có cách đáp khác nhau — Cùng lời gọi nhưng các lớp có cách đáp khác nhau

D. The concept described as Khung lớp ràng buộc phương thức cần cài đặt — Khung lớp ràng buộc phương thức cần cài đặt


**Q4. Which description matches Override? — Mô tả nào đúng với Override?**

A. A different concept described as Lớp con dùng lại các đặc điểm lớp cha — Lớp con dùng lại các đặc điểm lớp cha

B. A different concept described as Cùng lời gọi nhưng các lớp có cách đáp khác nhau — Cùng lời gọi nhưng các lớp có cách đáp khác nhau

C. The concept described as Lớp con cài lại phương thức của lớp cha — Lớp con cài lại phương thức của lớp cha

D. A different concept described as Khung lớp ràng buộc phương thức cần cài đặt — Khung lớp ràng buộc phương thức cần cài đặt


**Q5. Which use matches class Child(Parent)? — Công dụng nào đúng với class Child(Parent)?**

A. Use a different operation to Gọi khởi tạo lớp cha để không lặp code — Gọi khởi tạo lớp cha để không lặp code

B. Use this syntax to Kế thừa thông tin chung — Kế thừa thông tin chung

C. Use a different operation to Bắt lớp con định nghĩa giao diện bắt buộc — Bắt lớp con định nghĩa giao diện bắt buộc

D. Use a different operation to Xác minh đối tượng thuộc lớp khi cần — Xác minh đối tượng thuộc lớp khi cần


**Q6. Which use matches super().__init__(...)? — Công dụng nào đúng với super().__init__(...)?**

A. Use this syntax to Gọi khởi tạo lớp cha để không lặp code — Gọi khởi tạo lớp cha để không lặp code

B. Use a different operation to Bắt lớp con định nghĩa giao diện bắt buộc — Bắt lớp con định nghĩa giao diện bắt buộc

C. Use a different operation to Xác minh đối tượng thuộc lớp khi cần — Xác minh đối tượng thuộc lớp khi cần

D. Use a different operation to Kế thừa thông tin chung — Kế thừa thông tin chung


**Q7. Which use matches ABC/@abstractmethod? — Công dụng nào đúng với ABC/@abstractmethod?**

A. Use a different operation to Xác minh đối tượng thuộc lớp khi cần — Xác minh đối tượng thuộc lớp khi cần

B. Use a different operation to Kế thừa thông tin chung — Kế thừa thông tin chung

C. Use a different operation to Gọi khởi tạo lớp cha để không lặp code — Gọi khởi tạo lớp cha để không lặp code

D. Use this syntax to Bắt lớp con định nghĩa giao diện bắt buộc — Bắt lớp con định nghĩa giao diện bắt buộc


**Q8. Which use matches isinstance(obj,Class)? — Công dụng nào đúng với isinstance(obj,Class)?**

A. Use a different operation to Kế thừa thông tin chung — Kế thừa thông tin chung

B. Use a different operation to Gọi khởi tạo lớp cha để không lặp code — Gọi khởi tạo lớp cha để không lặp code

C. Use this syntax to Xác minh đối tượng thuộc lớp khi cần — Xác minh đối tượng thuộc lớp khi cần

D. Use a different operation to Bắt lớp con định nghĩa giao diện bắt buộc — Bắt lớp con định nghĩa giao diện bắt buộc


**Q9. What solves scenario 1? — Cách nào giải quyết tình huống 1?**

A. Another method is chosen because ABC bắt buộc các cách gửi cùng có send — ABC bắt buộc các cách gửi cùng có send

B. Choose the method because Điểm chung được đặt ở lớp cha, khác biệt ở lớp con — Điểm chung được đặt ở lớp cha, khác biệt ở lớp con

C. Another method is chosen because Mỗi dịch vụ tự định nghĩa fee nhưng nơi gọi thống nhất — Mỗi dịch vụ tự định nghĩa fee nhưng nơi gọi thống nhất

D. Another method is chosen because Các cảm biến dùng chung read nhưng trả số đo khác nhau — Các cảm biến dùng chung read nhưng trả số đo khác nhau


**Q10. What solves scenario 2? — Cách nào giải quyết tình huống 2?**

A. Choose the method because ABC bắt buộc các cách gửi cùng có send — ABC bắt buộc các cách gửi cùng có send

B. Another method is chosen because Mỗi dịch vụ tự định nghĩa fee nhưng nơi gọi thống nhất — Mỗi dịch vụ tự định nghĩa fee nhưng nơi gọi thống nhất

C. Another method is chosen because Các cảm biến dùng chung read nhưng trả số đo khác nhau — Các cảm biến dùng chung read nhưng trả số đo khác nhau

D. Another method is chosen because Ghi đè render giúp thêm loại xuất mà không sửa lời gọi — Ghi đè render giúp thêm loại xuất mà không sửa lời gọi


**Q11. What solves scenario 3? — Cách nào giải quyết tình huống 3?**

A. Another method is chosen because Các cảm biến dùng chung read nhưng trả số đo khác nhau — Các cảm biến dùng chung read nhưng trả số đo khác nhau

B. Another method is chosen because Ghi đè render giúp thêm loại xuất mà không sửa lời gọi — Ghi đè render giúp thêm loại xuất mà không sửa lời gọi

C. Another method is chosen because Điểm chung được đặt ở lớp cha, khác biệt ở lớp con — Điểm chung được đặt ở lớp cha, khác biệt ở lớp con

D. Choose the method because Mỗi dịch vụ tự định nghĩa fee nhưng nơi gọi thống nhất — Mỗi dịch vụ tự định nghĩa fee nhưng nơi gọi thống nhất


**Q12. What solves scenario 4? — Cách nào giải quyết tình huống 4?**

A. Another method is chosen because Ghi đè render giúp thêm loại xuất mà không sửa lời gọi — Ghi đè render giúp thêm loại xuất mà không sửa lời gọi

B. Another method is chosen because Điểm chung được đặt ở lớp cha, khác biệt ở lớp con — Điểm chung được đặt ở lớp cha, khác biệt ở lớp con

C. Choose the method because Các cảm biến dùng chung read nhưng trả số đo khác nhau — Các cảm biến dùng chung read nhưng trả số đo khác nhau

D. Another method is chosen because ABC bắt buộc các cách gửi cùng có send — ABC bắt buộc các cách gửi cùng có send


**Q13. What solves scenario 5? — Cách nào giải quyết tình huống 5?**

A. Another method is chosen because Điểm chung được đặt ở lớp cha, khác biệt ở lớp con — Điểm chung được đặt ở lớp cha, khác biệt ở lớp con

B. Choose the method because Ghi đè render giúp thêm loại xuất mà không sửa lời gọi — Ghi đè render giúp thêm loại xuất mà không sửa lời gọi

C. Another method is chosen because ABC bắt buộc các cách gửi cùng có send — ABC bắt buộc các cách gửi cùng có send

D. Another method is chosen because Mỗi dịch vụ tự định nghĩa fee nhưng nơi gọi thống nhất — Mỗi dịch vụ tự định nghĩa fee nhưng nơi gọi thống nhất


**Q14. Which data is used in scenario 1? — Tình huống 1 dùng dữ liệu nào?**

A. The described input Một sản phẩm điện tử giả lập — Một sản phẩm điện tử giả lập

B. Another input Tin nhắn Hello — Tin nhắn Hello

C. Another input Dịch vụ Express phí 35000 đồng — Dịch vụ Express phí 35000 đồng

D. Another input Nhiệt độ 26.5 °C, độ ẩm 62% — Nhiệt độ 26.5 °C, độ ẩm 62%


**Q15. Which data is used in scenario 2? — Tình huống 2 dùng dữ liệu nào?**

A. Another input Dịch vụ Express phí 35000 đồng — Dịch vụ Express phí 35000 đồng

B. Another input Nhiệt độ 26.5 °C, độ ẩm 62% — Nhiệt độ 26.5 °C, độ ẩm 62%

C. Another input Báo cáo plain và HTML — Báo cáo plain và HTML

D. The described input Tin nhắn Hello — Tin nhắn Hello


**Q16. Which data is used in scenario 3? — Tình huống 3 dùng dữ liệu nào?**

A. Another input Nhiệt độ 26.5 °C, độ ẩm 62% — Nhiệt độ 26.5 °C, độ ẩm 62%

B. Another input Báo cáo plain và HTML — Báo cáo plain và HTML

C. The described input Dịch vụ Express phí 35000 đồng — Dịch vụ Express phí 35000 đồng

D. Another input Một sản phẩm điện tử giả lập — Một sản phẩm điện tử giả lập


**Q17. Which data is used in scenario 4? — Tình huống 4 dùng dữ liệu nào?**

A. Another input Báo cáo plain và HTML — Báo cáo plain và HTML

B. The described input Nhiệt độ 26.5 °C, độ ẩm 62% — Nhiệt độ 26.5 °C, độ ẩm 62%

C. Another input Một sản phẩm điện tử giả lập — Một sản phẩm điện tử giả lập

D. Another input Tin nhắn Hello — Tin nhắn Hello


**Q18. Which data is used in scenario 5? — Tình huống 5 dùng dữ liệu nào?**

A. The described input Báo cáo plain và HTML — Báo cáo plain và HTML

B. Another input Một sản phẩm điện tử giả lập — Một sản phẩm điện tử giả lập

C. Another input Tin nhắn Hello — Tin nhắn Hello

D. Another input Dịch vụ Express phí 35000 đồng — Dịch vụ Express phí 35000 đồng


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
| Q1 | **B** | The concept described as Lớp con dùng lại các đặc điểm lớp cha | Lớp con dùng lại các đặc điểm lớp cha |
| Q2 | **A** | The concept described as Cùng lời gọi nhưng các lớp có cách đáp khác nhau | Cùng lời gọi nhưng các lớp có cách đáp khác nhau |
| Q3 | **D** | The concept described as Khung lớp ràng buộc phương thức cần cài đặt | Khung lớp ràng buộc phương thức cần cài đặt |
| Q4 | **C** | The concept described as Lớp con cài lại phương thức của lớp cha | Lớp con cài lại phương thức của lớp cha |
| Q5 | **B** | Use this syntax to Kế thừa thông tin chung | Kế thừa thông tin chung |
| Q6 | **A** | Use this syntax to Gọi khởi tạo lớp cha để không lặp code | Gọi khởi tạo lớp cha để không lặp code |
| Q7 | **D** | Use this syntax to Bắt lớp con định nghĩa giao diện bắt buộc | Bắt lớp con định nghĩa giao diện bắt buộc |
| Q8 | **C** | Use this syntax to Xác minh đối tượng thuộc lớp khi cần | Xác minh đối tượng thuộc lớp khi cần |
| Q9 | **B** | Choose the method because Điểm chung được đặt ở lớp cha, khác biệt ở lớp con | Điểm chung được đặt ở lớp cha, khác biệt ở lớp con |
| Q10 | **A** | Choose the method because ABC bắt buộc các cách gửi cùng có send | ABC bắt buộc các cách gửi cùng có send |
| Q11 | **D** | Choose the method because Mỗi dịch vụ tự định nghĩa fee nhưng nơi gọi thống nhất | Mỗi dịch vụ tự định nghĩa fee nhưng nơi gọi thống nhất |
| Q12 | **C** | Choose the method because Các cảm biến dùng chung read nhưng trả số đo khác nhau | Các cảm biến dùng chung read nhưng trả số đo khác nhau |
| Q13 | **B** | Choose the method because Ghi đè render giúp thêm loại xuất mà không sửa lời gọi | Ghi đè render giúp thêm loại xuất mà không sửa lời gọi |
| Q14 | **A** | The described input Một sản phẩm điện tử giả lập | Một sản phẩm điện tử giả lập |
| Q15 | **D** | The described input Tin nhắn Hello | Tin nhắn Hello |
| Q16 | **C** | The described input Dịch vụ Express phí 35000 đồng | Dịch vụ Express phí 35000 đồng |
| Q17 | **B** | The described input Nhiệt độ 26.5 °C, độ ẩm 62% | Nhiệt độ 26.5 °C, độ ẩm 62% |
| Q18 | **A** | The described input Báo cáo plain và HTML | Báo cáo plain và HTML |
| Q19 | **D** | Input meaning and units | Ý nghĩa và đơn vị dữ liệu |
| Q20 | **C** | Verify output and unusual inputs | Kiểm tra đầu ra và giá trị biên |

## 8. Nối sang bài tiếp theo

`Class/Object → Inheritance → Abstract API → Kiến trúc ứng dụng`.

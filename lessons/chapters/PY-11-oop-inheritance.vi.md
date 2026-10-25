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

**No Note — Không chú thích**

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

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Dùng Electronic kế thừa Product để tái sử dụng tên và bổ sung tháng bảo hành.
# Dữ liệu: Object Phone có bảo hành 12 tháng.
# class định nghĩa kiểu object và các phương thức của nó.
class Product:
    # __init__ chạy khi tạo instance; self trỏ đối tượng hiện tại và các tham số sau self là dữ liệu đầu vào.
    def __init__(self, name):
        # self.thuộc_tính lưu trạng thái riêng của object hiện tại.
        self.name = name

# Cú pháp (Product) cho Electronic kế thừa Product.
class Electronic(Product):
    # __init__ chạy khi tạo instance; self trỏ đối tượng hiện tại và các tham số sau self là dữ liệu đầu vào.
    def __init__(self, name, warranty_months):
        # super() gọi hàm __init__ của cha để lưu name.
        super().__init__(name)
        # Thuộc tính warranty_months giữ số tháng bảo hành riêng của object.
        self.warranty_months = warranty_months

phone = Electronic('Phone', 12)
# Truy cập thuộc tính name do lớp cha khởi tạo bằng dấu chấm.
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

**No Note — Không chú thích**

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

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Cùng lời gọi send() trên Email và SMS tạo kết quả theo loại đối tượng.
# Dữ liệu: Chuỗi Hello được chuyển qua hai loại object; không gửi ra mạng.
# Class Email có hành vi gửi dạng chuỗi bắt đầu bằng Email:.
class Email:
    # Phương thức dùng self để truy cập đúng instance, return trả dữ liệu cho bên gọi.
    def send(self, message):
        # return đưa kết quả trở lại nơi gọi và kết thúc method.
        return 'Email: ' + message

# Class SMS có cùng tên method send(), nhưng kết quả có tiền tố SMS:.
class SMS:
    # Phương thức dùng self để truy cập đúng instance, return trả dữ liệu cho bên gọi.
    def send(self, message):
        # return đưa kết quả trở lại nơi gọi và kết thúc method.
        return 'SMS: ' + message

# Lần lượt tạo Email() và SMS(); đa hình tự chọn send của từng object.
for sender in [Email(), SMS()]:
    # Cùng lệnh .send('Hello') cho kết quả theo loại thật của sender, rồi print().
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

**No Note — Không chú thích**

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

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Quy định phương thức send bắt buộc bằng lớp trừu tượng ABC.
# Dữ liệu: Console hiện thực hóa giao diện Notifier.
# Thư viện abc cung cấp ABC (lớp trừu tượng) và abstractmethod (đánh dấu method bắt buộc).
from abc import ABC, abstractmethod

# Kế thừa ABC quy định giao diện không thể tạo nếu còn phương thức trừu tượng.
class Notifier(ABC):
    # Decorator bắt lớp con cụ thể cài send().
    @abstractmethod
    # Phương thức dùng self để truy cập đúng instance, return trả dữ liệu cho bên gọi.
    def send(self, message):
        # pass là chỗ giữ lệnh rỗng, chưa cung cấp cách xử lý.
        pass

# Console hiện thực hóa send() nên tạo object được.
class Console(Notifier):
    # Phương thức dùng self để truy cập đúng instance, return trả dữ liệu cho bên gọi.
    def send(self, message):
        # return đưa kết quả trở lại nơi gọi và kết thúc method.
        return 'Console: ' + message

# Console() tạo object, .send() trả chuỗi, print() hiển thị.
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

**No Note — Không chú thích**

```python
class Shipping:
    def fee(self):
        return 0

class Express(Shipping):
    def fee(self):
        return 35000

print(Shipping().fee(), Express().fee())
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Lớp Express ghi đè phương thức fee của lớp Shipping.
# Dữ liệu: Phí thông thường 0 đồng, express 35.000 đồng.
# class định nghĩa kiểu object và các phương thức của nó.
class Shipping:
    # Phương thức dùng self để truy cập đúng instance, return trả dữ liệu cho bên gọi.
    def fee(self):
        # return đưa kết quả trở lại nơi gọi và kết thúc method.
        return 0

# Express kế thừa Shipping, ghi đè fee() để trả mức phí riêng.
class Express(Shipping):
    # Phương thức dùng self để truy cập đúng instance, return trả dữ liệu cho bên gọi.
    def fee(self):
        # Phí 35.000 đồng thay cho 0 đồng mặc định của lớp cha.
        return 35000

# Gọi fee trên hai instance khác loại, method của mỗi loại quyết định kết quả.
print(Shipping().fee(), Express().fee())
```

**Kết quả khi chạy:**

```text
0 35000
```

Hai đối tượng gọi cùng `fee()` nhưng phí khác nhau: gói thường 0 đồng, gói nhanh 35.000 đồng.
## 5. Năm tình huống kế thừa/đa hình — từ đối tượng tới giao diện thanh toán

### Tình huống 1 — Cấp 1: Hai loại sản phẩm kế thừa tên chung

**Từ vựng trong mục:** **Inheritance** — kế thừa; **Parent class** — lớp cha; **Override** — ghi đè.

**Tình huống thực tế:** Cửa hàng lập danh sách **10 sản phẩm** để giới thiệu trên bảng hàng. Mỗi dòng có tên sản phẩm, chẳng hạn Laptop hoặc Bàn, và nhóm hàng: `digital` nghĩa là thiết bị điện tử, `physical` nghĩa là đồ dùng thông thường. Nhân viên muốn lưu mỗi sản phẩm thành một đối tượng, xem tên và nhóm của sản phẩm đầu tiên, rồi đếm xem có bao nhiêu thiết bị và đồ dùng.

**Vì sao chọn cách này?** **Kế thừa** cho phép lớp con dùng lại phần thông tin chung của lớp cha. Ở đây lớp `Product` giữ tên sản phẩm; lớp `Digital` và `Physical` nhận cách lưu tên ấy mà không viết lại đoạn khởi tạo. **Ghi đè phương thức** nghĩa là cả hai lớp con đều có `category()` nhưng trả nhãn nhóm của chính mình. Chương trình tạo đúng đối tượng theo nhãn của từng dòng, rồi gọi cùng `category()` để đếm; không cần mỗi chỗ xem sản phẩm lại kiểm tra tên Laptop hay Bàn. Cách này có ích khi nhiều nhóm hàng chia sẻ thông tin, nhưng cách phân nhóm vẫn khác nhau.

**Quy trình:**
1. Định nghĩa lớp `Product` giữ tên và có phương thức `category()`.
2. Tạo lớp `Digital` và `Physical` ghi đè tên nhóm.
3. Tạo 10 đối tượng và đếm mỗi kiểu.

**No Note — Không chú thích**

```python
data = [("Laptop","digital"),("Bàn","physical"),("Chuột","digital"),("Ghế","physical"),("Màn hình","digital"),("Sổ","physical"),("Bàn phím","digital"),("Bút","physical"),("Tablet","digital"),("Tủ","physical")]
class Product:
    def __init__(self, name):
        self.name = name
    def category(self):
        return "other"
class Digital(Product):
    def category(self):
        return "digital"
class Physical(Product):
    def category(self):
        return "physical"
items = []
for name, kind in data:
    if kind == "digital":
        product = Digital(name)
    else:
        product = Physical(name)
    items.append(product)
if len(items) != 10:
    raise ValueError("Cần tạo đủ 10 mặt hàng.")
print("Sản phẩm:", len(items))
print("Đầu tiên:", items[0].name, items[0].category())
digital_count = 0
physical_count = 0
for product in items:
    if product.category() == "digital":
        digital_count += 1
    if product.category() == "physical":
        physical_count += 1
print("Thiết bị:", digital_count)
print("Đồ dùng:", physical_count)
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tạo 10 sản phẩm Digital/Physical và đếm qua cùng phương thức category.
# Dữ liệu: 10 tuple (tên hàng, nhãn digital/physical).
# 10 bản ghi gồm tên hàng và loại sản phẩm.
data = [("Laptop","digital"),("Bàn","physical"),("Chuột","digital"),("Ghế","physical"),("Màn hình","digital"),("Sổ","physical"),("Bàn phím","digital"),("Bút","physical"),("Tablet","digital"),("Tủ","physical")]
# class định nghĩa kiểu object và các phương thức của nó.
class Product:
    # __init__ chạy khi tạo instance; self trỏ đối tượng hiện tại và các tham số sau self là dữ liệu đầu vào.
    def __init__(self, name):
        # self.thuộc_tính lưu trạng thái riêng của object hiện tại.
        self.name = name
    # Method đa hình: cùng tên nhưng giá trị trả tùy lớp con.
    def category(self):
        # return đưa kết quả trở lại nơi gọi và kết thúc method.
        return "other"
# Digital kế thừa Product, ghi đè category trả 'digital'.
class Digital(Product):
    # Method đa hình: cùng tên nhưng giá trị trả tùy lớp con.
    def category(self):
        # return đưa kết quả trở lại nơi gọi và kết thúc method.
        return "digital"
# Physical cũng kế thừa Product, category trả 'physical'.
class Physical(Product):
    # Method đa hình: cùng tên nhưng giá trị trả tùy lớp con.
    def category(self):
        # return đưa kết quả trở lại nơi gọi và kết thúc method.
        return "physical"
items = []
# Tách tên và nhãn của từng bản ghi.
for name, kind in data:
    if kind == "digital":
        product = Digital(name)
    else:
        product = Physical(name)
    # append() đưa object vào list.
    items.append(product)
# len() đếm số phần tử, dùng kiểm đủ bản ghi hoặc báo số lượt.
if len(items) != 10:
    # raise ValueError báo đầu vào sai rồi dừng nhánh hiện tại.
    raise ValueError("Cần tạo đủ 10 mặt hàng.")
# len() đếm số phần tử, dùng kiểm đủ bản ghi hoặc báo số lượt.
print("Sản phẩm:", len(items))
# [0] là object đầu; .name là thuộc tính và category() là method.
print("Đầu tiên:", items[0].name, items[0].category())
digital_count = 0
physical_count = 0
for product in items:
    # Gọi category() trên object thực tế, không cần ép kiểu về class con.
    if product.category() == "digital":
        digital_count += 1
    # Gọi category() trên object thực tế, không cần ép kiểu về class con.
    if product.category() == "physical":
        physical_count += 1
print("Thiết bị:", digital_count)
print("Đồ dùng:", physical_count)
```

**Kết quả khi chạy:**

```text
Sản phẩm: 10
Đầu tiên: Laptop digital
Thiết bị: 5
Đồ dùng: 5
```

Lớp con không cần viết lại `__init__()` vì dùng được hành vi khởi tạo của lớp cha. Cùng lời gọi `category()` trả giá trị khác nhau tùy kiểu đối tượng.

### Tình huống 2 — Cấp 2: Áp giao diện gửi thông báo cho 12 yêu cầu

**Từ vựng trong mục:** **ABC** — lớp trừu tượng; **Abstract method** — phương thức bắt buộc; **Polymorphism** — đa hình.

**Tình huống thực tế:** Một ứng dụng quản lý lớp dự định xử lý **12 thông báo N01–N12**. Mỗi thông báo được giao cho một trong hai kênh: `email` (thư điện tử) hoặc `screen` (hiển thị trên màn hình). Đây là chương trình **mô phỏng**, không gửi thư hay hiện thông báo thật. Người quản lý muốn chạy đủ 12 yêu cầu, xem mỗi kênh nhận bao nhiêu thông báo và đọc thử kết quả của thông báo đầu tiên.

**Vì sao chọn cách này?** **ABC** (lớp cơ sở trừu tượng) là bản quy ước cho các lớp xử lý thông báo: bất kỳ kênh nào cũng phải có phương thức `send(message)`. `@abstractmethod` đánh dấu việc lớp con phải tự cài đặt phương thức ấy. `EmailNotifier` trả chuỗi bắt đầu `email:`, `ScreenNotifier` trả `screen:`; không có kết nối mạng. Nhờ cùng tên `send()`, chương trình dùng một vòng `for` để gọi đúng kênh của mỗi thông báo mà không phải tự viết hai quy trình riêng cho mọi yêu cầu. Đếm các tiền tố trong chuỗi trả về giúp xác nhận chương trình đã định tuyến đúng 12 thông báo.

**Quy trình:**
1. Tạo `Notifier(ABC)` yêu cầu phương thức `send`.
2. Tạo hai lớp cài đặt `send()` với tiền tố kết quả riêng.
3. Duyệt 12 yêu cầu, chọn đối tượng và tổng hợp theo kênh.

**No Note — Không chú thích**

```python
from abc import ABC, abstractmethod
channels = ["email","screen","email","screen","screen","email","screen","email","email","screen","email","screen"]
class Notifier(ABC):
    @abstractmethod
    def send(self, message):
        pass
class EmailNotifier(Notifier):
    def send(self, message):
        return "email:" + message
class ScreenNotifier(Notifier):
    def send(self, message):
        return "screen:" + message
notifiers = {"email": EmailNotifier(), "screen": ScreenNotifier()}
results = []
for i, channel in enumerate(channels, 1):
    message = notifiers[channel].send(f"N{i:02d}")
    results.append(message)
if len(results) != 12:
    raise ValueError("Cần xử lý đủ 12 thông báo.")
print("Yêu cầu:", len(results))
email_count = 0
screen_count = 0
for text in results:
    if text.startswith("email:"):
        email_count += 1
    if text.startswith("screen:"):
        screen_count += 1
print("Kênh email:", email_count)
print("Kênh màn hình:", screen_count)
print("Ví dụ:", results[0])
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Dùng giao diện Notifier chung để tạo 12 thông báo email/screen giả lập.
# Dữ liệu: 12 loại kênh email/screen, mã thông báo N01..N12.
# ABC/abstractmethod xác định giao diện send() bắt buộc.
from abc import ABC, abstractmethod
channels = ["email","screen","email","screen","screen","email","screen","email","email","screen","email","screen"]
class Notifier(ABC):
    # Đánh dấu send là method bắt buộc cho lớp con.
    @abstractmethod
    # Phương thức dùng self để truy cập đúng instance, return trả dữ liệu cho bên gọi.
    def send(self, message):
        # pass là chỗ giữ lệnh rỗng, chưa cung cấp cách xử lý.
        pass
class EmailNotifier(Notifier):
    # Phương thức dùng self để truy cập đúng instance, return trả dữ liệu cho bên gọi.
    def send(self, message):
        # return đưa kết quả trở lại nơi gọi và kết thúc method.
        return "email:" + message
# class định nghĩa kiểu object và các phương thức của nó.
class ScreenNotifier(Notifier):
    # Phương thức dùng self để truy cập đúng instance, return trả dữ liệu cho bên gọi.
    def send(self, message):
        # return đưa kết quả trở lại nơi gọi và kết thúc method.
        return "screen:" + message
# Dictionary ánh xạ chuỗi tên kênh tới object gửi tương ứng.
notifiers = {"email": EmailNotifier(), "screen": ScreenNotifier()}
results = []
# enumerate(...,1) đánh số kênh bắt đầu từ 1.
for i, channel in enumerate(channels, 1):
    # Tra dictionary lấy instance, .send() trả chuỗi tương ứng kênh.
    # f-string :02d tạo mã N01..N12, thêm số 0 ở đầu.
    message = notifiers[channel].send(f"N{i:02d}")
    # append() lưu chuỗi đầu ra mô phỏng.
    results.append(message)
# len() đếm số phần tử, dùng kiểm đủ bản ghi hoặc báo số lượt.
if len(results) != 12:
    # raise ValueError báo đầu vào sai rồi dừng nhánh hiện tại.
    raise ValueError("Cần xử lý đủ 12 thông báo.")
# len() đếm số phần tử, dùng kiểm đủ bản ghi hoặc báo số lượt.
print("Yêu cầu:", len(results))
email_count = 0
screen_count = 0
for text in results:
    # startswith(prefix) kiểm chuỗi có bắt đầu bằng tiền tố email:/screen: hay không.
    if text.startswith("email:"):
        email_count += 1
    # startswith(prefix) kiểm chuỗi có bắt đầu bằng tiền tố email:/screen: hay không.
    if text.startswith("screen:"):
        screen_count += 1
print("Kênh email:", email_count)
print("Kênh màn hình:", screen_count)
# [0] lấy dòng thông báo đầu.
print("Ví dụ:", results[0])
```

**Kết quả khi chạy:**

```text
Yêu cầu: 12
Kênh email: 6
Kênh màn hình: 6
Ví dụ: email:N01
```

Có hai lớp con nhưng chỉ một lời gọi `send()`. Trả chuỗi xác nhận để kiểm chứng bài học, không khẳng định đã gửi thông báo đến người thật.

### Tình huống 3 — Cấp 3: Ghi đè cách tính phí của 15 đơn giao

**Từ vựng trong mục:** **Override** — ghi đè; **Method dispatch** — chọn phương thức; **super()** — gọi lớp cha.

**Tình huống thực tế:** Cửa hàng phải tính phí cho **15 đơn vận chuyển**. Mỗi đơn được chọn một trong ba dịch vụ theo quy tắc giả lập: `standard` giao thường miễn phí; `express` giao nhanh tính **35.000 đồng/đơn**; `cold` giao lạnh tính **50.000 đồng/đơn**. Giá không phụ thuộc số km trong bài này. Kế toán cần tổng tiền phí của tất cả đơn và số đơn sử dụng dịch vụ giao lạnh.

**Vì sao chọn cách này?** **Lớp cha** `Shipping` chứa loại dịch vụ và mức phí mặc định 0; hai **lớp con** `Express`, `Cold` có cùng phương thức `fee()` nhưng trả mức phí khác nhau. `super().__init__(...)` gọi phần khởi tạo của lớp cha để lưu tên loại dịch vụ, nên lớp con không phải lặp lại cách lưu. Chương trình tạo đối tượng theo từng loại rồi chỉ cần gọi `order.fee()` cho cả 15 đơn: đây là **đa hình**, cùng một lời gọi nhưng kết quả do loại đối tượng quyết định. Vì bảng phí trong bài cố định theo loại, không thêm phép tính khoảng cách hay thu thêm cho giao thường.

**Quy trình:**
1. Định nghĩa lớp cha `Shipping` với `fee()` mặc định 0.
2. Hai lớp con `Express`/`Cold` ghi đè phí và dùng `super()` để lưu loại.
3. Tạo 15 đối tượng, cộng kết quả gọi cùng một phương thức.

**No Note — Không chú thích**

```python
types = ["standard","express","cold","standard","express","standard","cold","express","express","standard","cold","standard","express","cold","standard"]
class Shipping:
    def __init__(self, kind):
        self.kind = kind
    def fee(self):
        return 0
class Express(Shipping):
    def __init__(self):
        super().__init__("express")
    def fee(self):
        return 35000
class Cold(Shipping):
    def __init__(self):
        super().__init__("cold")
    def fee(self):
        return 50000
def create_standard_shipping():
    return Shipping("standard")

factory = {"standard": create_standard_shipping,
           "express": Express, "cold": Cold}
orders = []
for kind in types:
    orders.append(factory[kind]())
if len(orders) != 15:
    raise ValueError("Cần xử lý đủ 15 đơn vận chuyển.")
print("Đơn:", len(orders))
cold_count = 0
total_fee = 0
for order in orders:
    if order.kind == "cold":
        cold_count += 1
    total_fee += order.fee()
print("Giao lạnh:", cold_count)
print("Tổng phí (đồng):", total_fee)
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tạo 15 kiểu vận chuyển bằng factory và tính phí theo lớp con.
# Dữ liệu: 15 nhãn standard/express/cold; phí lần lượt 0/35.000/50.000 đồng.
types = ["standard","express","cold","standard","express","standard","cold","express","express","standard","cold","standard","express","cold","standard"]
# Lớp cha lưu kind và cung cấp fee() mặc định.
class Shipping:
    # __init__ chạy khi tạo instance; self trỏ đối tượng hiện tại và các tham số sau self là dữ liệu đầu vào.
    def __init__(self, kind):
        # self.thuộc_tính lưu trạng thái riêng của object hiện tại.
        self.kind = kind
    # Phương thức dùng self để truy cập đúng instance, return trả dữ liệu cho bên gọi.
    def fee(self):
        # return đưa kết quả trở lại nơi gọi và kết thúc method.
        return 0
# Express là dịch vụ nhanh, cài phí 35.000 đồng.
class Express(Shipping):
    # __init__ chạy khi tạo instance; self trỏ đối tượng hiện tại và các tham số sau self là dữ liệu đầu vào.
    def __init__(self):
        # super() gọi __init__ của lớp cha để lưu đúng nhãn kind.
        super().__init__("express")
    # Phương thức dùng self để truy cập đúng instance, return trả dữ liệu cho bên gọi.
    def fee(self):
        # return đưa kết quả trở lại nơi gọi và kết thúc method.
        return 35000
# Cold là dịch vụ lạnh, cài phí 50.000 đồng.
class Cold(Shipping):
    # __init__ chạy khi tạo instance; self trỏ đối tượng hiện tại và các tham số sau self là dữ liệu đầu vào.
    def __init__(self):
        # super() gọi __init__ của lớp cha để lưu đúng nhãn kind.
        super().__init__("cold")
    # Phương thức dùng self để truy cập đúng instance, return trả dữ liệu cho bên gọi.
    def fee(self):
        # return đưa kết quả trở lại nơi gọi và kết thúc method.
        return 50000
# Factory tạo Shipping('standard') khi cần.
def create_standard_shipping():
    # return đưa kết quả trở lại nơi gọi và kết thúc method.
    return Shipping("standard")

# Dictionary chứa callable: hàm factory hoặc class có thể gọi để tạo object.
factory = {"standard": create_standard_shipping,
           "express": Express, "cold": Cold}
orders = []
for kind in types:
    # Lấy callable theo nhãn rồi gọi () tạo instance phù hợp.
    orders.append(factory[kind]())
# len() đếm số phần tử, dùng kiểm đủ bản ghi hoặc báo số lượt.
if len(orders) != 15:
    # raise ValueError báo đầu vào sai rồi dừng nhánh hiện tại.
    raise ValueError("Cần xử lý đủ 15 đơn vận chuyển.")
# len() đếm số phần tử, dùng kiểm đủ bản ghi hoặc báo số lượt.
print("Đơn:", len(orders))
cold_count = 0
total_fee = 0
for order in orders:
    if order.kind == "cold":
        cold_count += 1
    # Cùng method fee() nhưng tính phí khác nhau theo object; += cộng tổng đồng.
    total_fee += order.fee()
print("Giao lạnh:", cold_count)
print("Tổng phí (đồng):", total_fee)
```

**Kết quả khi chạy:**

```text
Đơn: 15
Giao lạnh: 4
Tổng phí (đồng): 375000
```

Phí giao lạnh và nhanh cao hơn loại thường vì chính sách giả định của cửa hàng; không lấy bảng giá này làm giá thực tế của đơn vị vận chuyển.

### Tình huống 4 — Cấp 4: Đọc 18 cảm biến nhiều kiểu và tách dữ liệu thiếu

**Từ vựng trong mục:** **Polymorphism** — đa hình; **Instance** — đối tượng; **Validation** — kiểm tra dữ liệu.

**Tình huống thực tế:** Trạm kỹ thuật ghi **18 kết quả cảm biến**, xen kẽ hai loại phép đo: nhiệt độ tính bằng **°C** và độ ẩm tính bằng **%**. Hai lượt không có giá trị nên để `None`; các lượt khác có số như 24 °C hoặc 56%. Nhân viên muốn một danh sách các kết quả được gắn đúng đơn vị, biết bao nhiêu lượt hợp lệ, bao nhiêu lượt thiếu và xem kết quả đầu tiên.

**Vì sao chọn cách này?** **Đa hình** cũng hữu ích khi các đối tượng phải cùng trả kết quả nhưng **đơn vị hiển thị khác nhau**. Lớp `Sensor` giữ giá trị chung; lớp `Temperature` định dạng `°C`, còn `Humidity` định dạng `%` trong phương thức `read()`. Chương trình đọc lần lượt cả 18 đối tượng bằng một lệnh gọi `read()` mà không phải kiểm tra loại sau mỗi lần đọc. Nếu giá trị là `None`, phương thức trả `None` trước khi định dạng, vì không thể in số thập phân từ dữ liệu thiếu. Sau đó đếm riêng kết quả có số và chưa có số; không coi phép đo thiếu là 0.

**Quy trình:**
1. Tạo lớp cha lưu số đo và cung cấp giao diện `read`.
2. Ghi đè `read()` cho nhiệt độ/độ ẩm theo đơn vị.
3. Duyệt 18 đối tượng, loại dòng thiếu và đếm kết quả.

**No Note — Không chú thích**

```python
records = [("temp",24),("humidity",56),("temp",25),("humidity",58),("temp",None),("humidity",60),("temp",27),("humidity",62),("temp",28),("humidity",64),("temp",29),("humidity",66),("temp",30),("humidity",None),("temp",31),("humidity",70),("temp",32),("humidity",72)]
class Sensor:
    def __init__(self, value):
        self.value = value
    def read(self):
        raise NotImplementedError
class Temperature(Sensor):
    def read(self):
        if self.value is None:
            return None
        return f"{self.value:.1f} °C"
class Humidity(Sensor):
    def read(self):
        if self.value is None:
            return None
        return f"{self.value:.1f} %"
sensors = []
for kind, value in records:
    if kind == "temp":
        sensor = Temperature(value)
    else:
        sensor = Humidity(value)
    sensors.append(sensor)
results = []
valid = []
for sensor in sensors:
    text = sensor.read()
    results.append(text)
    if text is not None:
        valid.append(text)
if len(results) != 18:
    raise ValueError("Cần nhận đủ 18 bản ghi cảm biến.")
print("Cảm biến:", len(results))
print("Hợp lệ:", len(valid))
print("Thiếu:", len(results) - len(valid))
print("Mẫu đầu:", results[0])
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Nhận 18 mẫu nhiệt độ/độ ẩm bằng class đa hình, giữ None là dữ liệu thiếu.
# Dữ liệu: 18 bộ (loại temp/humidity, giá trị °C/%), None là mất số đo.
records = [("temp",24),("humidity",56),("temp",25),("humidity",58),("temp",None),("humidity",60),("temp",27),("humidity",62),("temp",28),("humidity",64),("temp",29),("humidity",66),("temp",30),("humidity",None),("temp",31),("humidity",70),("temp",32),("humidity",72)]
# Lớp cha chứa giá trị gốc và khai giao diện read().
class Sensor:
    # __init__ chạy khi tạo instance; self trỏ đối tượng hiện tại và các tham số sau self là dữ liệu đầu vào.
    def __init__(self, value):
        # self.thuộc_tính lưu trạng thái riêng của object hiện tại.
        self.value = value
    # Phương thức dùng self để truy cập đúng instance, return trả dữ liệu cho bên gọi.
    def read(self):
        # Thông báo read của lớp cha chưa cài, buộc class con ghi đè.
        raise NotImplementedError
# Class đọc nhiệt độ theo đơn vị °C.
class Temperature(Sensor):
    # Phương thức dùng self để truy cập đúng instance, return trả dữ liệu cho bên gọi.
    def read(self):
        # is None nhận dữ liệu thiếu, không biến thành 0.
        if self.value is None:
            # return đưa kết quả trở lại nơi gọi và kết thúc method.
            return None
        # f-string :.1f định dạng số với một chữ số thập phân.
        return f"{self.value:.1f} °C"
# Class đọc độ ẩm theo đơn vị %.
class Humidity(Sensor):
    # Phương thức dùng self để truy cập đúng instance, return trả dữ liệu cho bên gọi.
    def read(self):
        # is None nhận dữ liệu thiếu, không biến thành 0.
        if self.value is None:
            # return đưa kết quả trở lại nơi gọi và kết thúc method.
            return None
        # f-string :.1f định dạng số với một chữ số thập phân.
        return f"{self.value:.1f} %"
sensors = []
for kind, value in records:
    if kind == "temp":
        sensor = Temperature(value)
    else:
        sensor = Humidity(value)
    # append() thêm instance của class cảm biến thích hợp.
    sensors.append(sensor)
results = []
valid = []
for sensor in sensors:
    # Đa hình gọi read() theo loại class thực tế.
    text = sensor.read()
    results.append(text)
    # Giữ những dòng read() cho chuỗi hợp lệ; loại None.
    if text is not None:
        valid.append(text)
# len() đếm số phần tử, dùng kiểm đủ bản ghi hoặc báo số lượt.
if len(results) != 18:
    # raise ValueError báo đầu vào sai rồi dừng nhánh hiện tại.
    raise ValueError("Cần nhận đủ 18 bản ghi cảm biến.")
# len() đếm số phần tử, dùng kiểm đủ bản ghi hoặc báo số lượt.
print("Cảm biến:", len(results))
# len() đếm số phần tử, dùng kiểm đủ bản ghi hoặc báo số lượt.
print("Hợp lệ:", len(valid))
# Số thiếu bằng tổng 18 bản ghi trừ số hợp lệ.
print("Thiếu:", len(results) - len(valid))
print("Mẫu đầu:", results[0])
```

**Kết quả khi chạy:**

```text
Cảm biến: 18
Hợp lệ: 16
Thiếu: 2
Mẫu đầu: 24.0 °C
```

Cùng lời gọi `read()` nhưng cách tạo chuỗi khác nhau tùy lớp con; dữ liệu mất tín hiệu phải được đếm riêng, không gán bằng 0 °C hoặc 0%.

### Tình huống 5 — Cấp 5: Thiết kế hai loại giao dịch theo hợp đồng phí chung

**Từ vựng trong mục:** **Abstract class** — lớp trừu tượng; **Override** — ghi đè; **Dispatch** — phân phối phương thức.

**Tình huống thực tế:** Hệ thống thanh toán thử nghiệm nhận **20 giao dịch P01–P20**. Mỗi dòng gồm số tiền tính bằng **đồng** và loại xử lý `bank` (chuyển khoản) hoặc `card` (thẻ). Theo mức phí minh họa, chuyển khoản thu **2.500 đồng** mỗi giao dịch, còn thẻ thu **2% số tiền**. Giao dịch P07 chưa có số tiền (`None`), P16 có tiền âm nên cần sửa. Bộ phận vận hành cần tổng phí của **18 giao dịch hợp lệ** và danh sách hai mã lỗi; không thu tiền thật.

**Vì sao chọn cách này?** **Hợp đồng chung** ở đây là mọi phương thức thanh toán đều phải có `fee()`, được lớp `Payment` khai báo bằng ABC. Lớp `Bank` trả khoản phí cố định 2.500 đồng, lớp `Card` tính 2% trên số tiền giao dịch rồi làm tròn theo code. Phần kiểm tra đầu vào được đặt tại lớp cha `Payment`: chỉ nhận số tiền là số và không âm. Vì thế khi P07 là `None` hoặc P16 âm, chương trình bắt `ValueError` và đưa mã vào danh sách sửa **trước khi tính phí**, không biến lỗi thành 0 đồng. Chỉ đối tượng hợp lệ mới được thêm vào danh sách để cộng phí, nên không cần tự chọn công thức trong từng lần cộng.

**Quy trình:**
1. Tạo giao diện `Payment(ABC)` giữ số tiền hợp lệ và bắt buộc phương thức `fee()`.
2. Tạo `Bank` và `Card` ghi đè `fee()` theo chính sách giả lập.
3. Duyệt 20 giao dịch, ghi mã sai, cộng phí các đối tượng hợp lệ và đối chiếu số bản ghi.

**No Note — Không chú thích**

```python
from abc import ABC, abstractmethod
amounts = [100000,125000,150000,175000,200000,225000,None,100000,125000,150000,175000,200000,225000,250000,100000,-10000,150000,175000,200000,225000]
methods = ["bank","card","card","bank","card","card","bank","card","card","bank","card","card","bank","card","card","bank","card","card","bank","card"]
class Payment(ABC):
    def __init__(self, amount):
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Số tiền không hợp lệ")
        self.amount = amount
    @abstractmethod
    def fee(self):
        pass
class Bank(Payment):
    def fee(self):
        return 2500
class Card(Payment):
    def fee(self):
        return round(self.amount * 0.02)
valid, invalid = [], []
for i, (amount, method) in enumerate(zip(amounts, methods), 1):
    try:
        if method == "bank":
            payment = Bank(amount)
        else:
            payment = Card(amount)
        valid.append(payment)
    except ValueError:
        invalid.append(f"P{i:02d}")
if len(amounts) != 20 or len(valid) + len(invalid) != 20:
    raise ValueError("Cần đối chiếu đủ 20 giao dịch, kể cả giao dịch sai.")
print("Giao dịch:", len(amounts))
print("Hợp lệ:", len(valid))
print("Cần sửa:", ", ".join(invalid))
total_fee = 0
for item in valid:
    total_fee += item.fee()
print("Phí tổng (đồng):", total_fee)
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Xử lý 20 thanh toán, chặn số tiền sai và tính phí Bank/Card.
# Dữ liệu: 20 số tiền đồng ghép vị trí với 20 loại thanh toán bank/card; None, -10.000 là lỗi.
# ABC và abstractmethod thiết lập hợp đồng cho các phương thức phí.
from abc import ABC, abstractmethod
amounts = [100000,125000,150000,175000,200000,225000,None,100000,125000,150000,175000,200000,225000,250000,100000,-10000,150000,175000,200000,225000]
methods = ["bank","card","card","bank","card","card","bank","card","card","bank","card","card","bank","card","card","bank","card","card","bank","card"]
# Class cha trừu tượng kiểm số tiền hợp lệ.
class Payment(ABC):
    # __init__ chạy khi tạo instance; self trỏ đối tượng hiện tại và các tham số sau self là dữ liệu đầu vào.
    def __init__(self, amount):
        # isinstance() xác minh là số; not/or loại None, số âm và tránh so None với 0.
        if not isinstance(amount, (int, float)) or amount < 0:
            # raise ValueError báo đầu vào sai rồi dừng nhánh hiện tại.
            raise ValueError("Số tiền không hợp lệ")
        # self.thuộc_tính lưu trạng thái riêng của object hiện tại.
        self.amount = amount
    # Decorator yêu cầu Bank/Card phải có fee().
    @abstractmethod
    # Phương thức dùng self để truy cập đúng instance, return trả dữ liệu cho bên gọi.
    def fee(self):
        # pass là chỗ giữ lệnh rỗng, chưa cung cấp cách xử lý.
        pass
# Bank có phí cố định 2.500 đồng.
class Bank(Payment):
    # Phương thức dùng self để truy cập đúng instance, return trả dữ liệu cho bên gọi.
    def fee(self):
        # return đưa kết quả trở lại nơi gọi và kết thúc method.
        return 2500
# Card tính phí 2% số tiền giao dịch.
class Card(Payment):
    # Phương thức dùng self để truy cập đúng instance, return trả dữ liệu cho bên gọi.
    def fee(self):
        # 0.02 là 2%, round() làm tròn thành tiền đồng.
        return round(self.amount * 0.02)
valid, invalid = [], []
# zip() ghép tiền và phương thức theo vị trí; enumerate(...,1) đánh thứ tự P01..P20.
for i, (amount, method) in enumerate(zip(amounts, methods), 1):
    # try bao đoạn khởi tạo có thể báo lỗi để except xử lý riêng.
    try:
        if method == "bank":
            payment = Bank(amount)
        else:
            payment = Card(amount)
        valid.append(payment)
    # Bắt ValueError khi tiền sai để tiếp tục xét giao dịch khác.
    except ValueError:
        # append() lưu mã lỗi với f-string :02d.
        invalid.append(f"P{i:02d}")
# len() đếm số phần tử, dùng kiểm đủ bản ghi hoặc báo số lượt.
if len(amounts) != 20 or len(valid) + len(invalid) != 20:
    # raise ValueError báo đầu vào sai rồi dừng nhánh hiện tại.
    raise ValueError("Cần đối chiếu đủ 20 giao dịch, kể cả giao dịch sai.")
# len() đếm số phần tử, dùng kiểm đủ bản ghi hoặc báo số lượt.
print("Giao dịch:", len(amounts))
# len() đếm số phần tử, dùng kiểm đủ bản ghi hoặc báo số lượt.
print("Hợp lệ:", len(valid))
print("Cần sửa:", ", ".join(invalid))
total_fee = 0
for item in valid:
    # Gọi fee theo class Bank/Card rồi cộng dồn phí đồng.
    total_fee += item.fee()
print("Phí tổng (đồng):", total_fee)
```

**Kết quả khi chạy:**

```text
Giao dịch: 20
Hợp lệ: 18
Cần sửa: P07, P16
Phí tổng (đồng): 56500
```

Vì mỗi giao dịch là một đối tượng thanh toán khác loại, chương trình gọi `fee()` thống nhất nhưng nhận kết quả theo đúng lớp con. Không sử dụng số âm và `None` như khoản thu bằng 0.

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

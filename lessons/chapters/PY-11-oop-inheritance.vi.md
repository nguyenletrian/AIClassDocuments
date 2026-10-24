# PY-11 — Kế thừa, đa hình và lớp trừu tượng ABC

## 1. Vị trí trong chuỗi kiến thức

`Class/Object → Inheritance → Abstract API → Kiến trúc ứng dụng`

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Ý nghĩa |
|---|---|---|
| Inheritance | kế thừa | Lớp con dùng lại các đặc điểm lớp cha |
| Polymorphism | đa hình | Cùng lời gọi nhưng các lớp có cách đáp khác nhau |
| Abstract class | lớp trừu tượng | Khung lớp ràng buộc phương thức cần cài đặt |
| Override | ghi đè | Lớp con cài lại phương thức của lớp cha |

## 3. Thư viện, hàm và tham số

| Hàm/cú pháp | Giải thích và lý do dùng |
|---|---|
| `class Child(Parent)` | Kế thừa thông tin chung |
| `super().__init__(...)` | Gọi khởi tạo lớp cha để không lặp code |
| `ABC/@abstractmethod` | Bắt lớp con định nghĩa giao diện bắt buộc |
| `isinstance(obj,Class)` | Xác minh đối tượng thuộc lớp khi cần |

## 4. Khái niệm và ví dụ nhỏ

### 4.1. Inheritance

Lớp con dùng lại các đặc điểm lớp cha.

```python
class P: pass
class C(P): pass
print(isinstance(C(),P))
```

### 4.2. Polymorphism

Cùng lời gọi nhưng các lớp có cách đáp khác nhau.

```python
class A:
    def f(self):return 1
print(A().f())
```

### 4.3. Abstract class

Khung lớp ràng buộc phương thức cần cài đặt.

```python
from abc import ABC
class Base(ABC): pass
print(Base())
```

### 4.4. Override

Lớp con cài lại phương thức của lớp cha.

```python
class A:
    def f(self):return 1
class B(A):
    def f(self):return 2
print(B().f())
```

## 5. Năm tình huống lập trình thực tế

### Tình huống 1 — Các loại sản phẩm

**Vấn đề:** Các loại sản phẩm.

**Vì sao chọn cách giải?** Điểm chung được đặt ở lớp cha, khác biệt ở lớp con.

**Dữ liệu:** Một sản phẩm điện tử giả lập.

```python
class Product:
    def __init__(self,name):self.name=name
class Electronic(Product):
    def category(self):return "electronic"
print(Electronic("Phone").category())
```

### Tình huống 2 — Giao diện gửi thông báo

**Vấn đề:** Giao diện gửi thông báo.

**Vì sao chọn cách giải?** ABC bắt buộc các cách gửi cùng có send.

**Dữ liệu:** Tin nhắn Hello.

```python
from abc import ABC,abstractmethod
class Notifier(ABC):
    @abstractmethod
    def send(self,msg):pass
class Console(Notifier):
    def send(self,msg):return "Sent:"+msg
print(Console().send("Hello"))
```

### Tình huống 3 — Tính phí vận chuyển

**Vấn đề:** Tính phí vận chuyển.

**Vì sao chọn cách giải?** Mỗi dịch vụ tự định nghĩa fee nhưng nơi gọi thống nhất.

**Dữ liệu:** Dịch vụ Express phí 35000 đồng.

```python
class Shipping:
    def fee(self):return 0
class Express(Shipping):
    def fee(self):return 35000
print(Express().fee())
```

### Tình huống 4 — Đọc nhiều loại cảm biến

**Vấn đề:** Đọc nhiều loại cảm biến.

**Vì sao chọn cách giải?** Các cảm biến dùng chung read nhưng trả số đo khác nhau.

**Dữ liệu:** Nhiệt độ 26.5 °C, độ ẩm 62%.

```python
class Sensor:
    def read(self):return 0
class Temp(Sensor):
    def read(self):return 26.5
class Humidity(Sensor):
    def read(self):return 62
for s in [Temp(),Humidity()]:print(s.read())
```

### Tình huống 5 — Chuyển định dạng báo cáo

**Vấn đề:** Chuyển định dạng báo cáo.

**Vì sao chọn cách giải?** Ghi đè render giúp thêm loại xuất mà không sửa lời gọi.

**Dữ liệu:** Báo cáo plain và HTML.

```python
class Report:
    def render(self):return "plain"
class HtmlReport(Report):
    def render(self):return "<p>report</p>"
print(HtmlReport().render())
```

## 6. Sai lầm thường gặp

- Cần chú ý thứ tự xử lý, kiểu dữ liệu và đơn vị đo. Trường hợp rỗng/thiếu dữ liệu phải có cách xử lý rõ ràng.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ


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

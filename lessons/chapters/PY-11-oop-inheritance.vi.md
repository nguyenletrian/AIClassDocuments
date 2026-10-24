# PY-11 — Kế thừa, đa hình và lớp trừu tượng ABC


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Inheritance** — kế thừa; **Polymorphism** — đa hình.

`Class/Object → Inheritance → Abstract API → Kiến trúc ứng dụng`

Bài này nối trực tiếp kiến thức trước với bước xử lý dữ liệu/AI sau đó. Hãy nắm ý nghĩa dữ liệu trước khi chạy code.

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

Các lựa chọn được giải thích cùng hàm; trong ví dụ code chỉ nhắc lý do thao tác, ý nghĩa hàng/cột và đơn vị đo.

## 4. Khái niệm và ví dụ nhỏ

### 4.1. Inheritance

**Từ vựng trong mục:** **Inheritance** — kế thừa.

Lớp con dùng lại các đặc điểm lớp cha. Đây là bước nhỏ của chuỗi kiến thức, không cần chứng minh toán học để hiểu cách tính bằng Python.

```python
class P: pass
class C(P): pass
print(isinstance(C(),P))
```

**Tự kiểm tra:** Inheritance là gì? **Đáp án:** Lớp con dùng lại các đặc điểm lớp cha.

### 4.2. Polymorphism

**Từ vựng trong mục:** **Polymorphism** — đa hình.

Cùng lời gọi nhưng các lớp có cách đáp khác nhau. Đây là bước nhỏ của chuỗi kiến thức, không cần chứng minh toán học để hiểu cách tính bằng Python.

```python
class A:
    def f(self):return 1
print(A().f())
```

**Tự kiểm tra:** Polymorphism là gì? **Đáp án:** Cùng lời gọi nhưng các lớp có cách đáp khác nhau.

### 4.3. Abstract class

**Từ vựng trong mục:** **Abstract class** — lớp trừu tượng.

Khung lớp ràng buộc phương thức cần cài đặt. Đây là bước nhỏ của chuỗi kiến thức, không cần chứng minh toán học để hiểu cách tính bằng Python.

```python
from abc import ABC
class Base(ABC): pass
print(Base())
```

**Tự kiểm tra:** Abstract class là gì? **Đáp án:** Khung lớp ràng buộc phương thức cần cài đặt.

### 4.4. Override

**Từ vựng trong mục:** **Override** — ghi đè.

Lớp con cài lại phương thức của lớp cha. Đây là bước nhỏ của chuỗi kiến thức, không cần chứng minh toán học để hiểu cách tính bằng Python.

```python
class A:
    def f(self):return 1
class B(A):
    def f(self):return 2
print(B().f())
```

**Tự kiểm tra:** Override là gì? **Đáp án:** Lớp con cài lại phương thức của lớp cha.

## 5. Năm tình huống lập trình thực tế

### Tình huống 1 — Các loại sản phẩm

**Từ vựng trong mục:** **Inheritance** — kế thừa.

**Tình huống thực tế:** Một cửa hàng đang cần giải quyết việc các loại sản phẩm. Thông tin đầu vào: Một sản phẩm điện tử giả lập. Dữ liệu minh họa; khi có bảng, mỗi hàng là đối tượng và mỗi cột là một thuộc tính với ý nghĩa rõ. Hãy lập trình thực hiện việc này và in kết quả để nhân viên kiểm tra.

**Vì sao chọn cách giải?** Điểm chung được đặt ở lớp cha, khác biệt ở lớp con. Đây là phương án phù hợp bài toán nhỏ, không tự suy ra đủ an toàn với mọi dữ liệu thật.


**Quy trình:** Nắm dữ liệu → chọn cấu trúc/hàm → tính → in và kiểm tra kết quả.

```python
class Product:
    def __init__(self,name):self.name=name
class Electronic(Product):
    def category(self):return "electronic"
print(Electronic("Phone").category())
```

**Đọc kết quả:** So sánh kết quả với tình huống đầu vào và thử trường hợp ngoại lệ.

### Tình huống 2 — Giao diện gửi thông báo

**Từ vựng trong mục:** **Polymorphism** — đa hình.

**Tình huống thực tế:** Một bộ phận vận hành đang cần giải quyết việc giao diện gửi thông báo. Thông tin đầu vào: Tin nhắn Hello. Dữ liệu minh họa; khi có bảng, mỗi hàng là đối tượng và mỗi cột là một thuộc tính với ý nghĩa rõ. Hãy lập trình thực hiện việc này và in kết quả để nhân viên kiểm tra.

**Vì sao chọn cách giải?** ABC bắt buộc các cách gửi cùng có send. Đây là phương án phù hợp bài toán nhỏ, không tự suy ra đủ an toàn với mọi dữ liệu thật.


**Quy trình:** Nắm dữ liệu → chọn cấu trúc/hàm → tính → in và kiểm tra kết quả.

```python
from abc import ABC,abstractmethod
class Notifier(ABC):
    @abstractmethod
    def send(self,msg):pass
class Console(Notifier):
    def send(self,msg):return "Sent:"+msg
print(Console().send("Hello"))
```

**Đọc kết quả:** So sánh kết quả với tình huống đầu vào và thử trường hợp ngoại lệ.

### Tình huống 3 — Tính phí vận chuyển

**Từ vựng trong mục:** **Abstract class** — lớp trừu tượng.

**Tình huống thực tế:** Một bộ phận vận hành đang cần giải quyết việc tính phí vận chuyển. Thông tin đầu vào: Dịch vụ Express phí 35000 đồng. Dữ liệu minh họa; khi có bảng, mỗi hàng là đối tượng và mỗi cột là một thuộc tính với ý nghĩa rõ. Hãy lập trình thực hiện việc này và in kết quả để nhân viên kiểm tra.

**Vì sao chọn cách giải?** Mỗi dịch vụ tự định nghĩa fee nhưng nơi gọi thống nhất. Đây là phương án phù hợp bài toán nhỏ, không tự suy ra đủ an toàn với mọi dữ liệu thật.


**Quy trình:** Nắm dữ liệu → chọn cấu trúc/hàm → tính → in và kiểm tra kết quả.

```python
class Shipping:
    def fee(self):return 0
class Express(Shipping):
    def fee(self):return 35000
print(Express().fee())
```

**Đọc kết quả:** So sánh kết quả với tình huống đầu vào và thử trường hợp ngoại lệ.

### Tình huống 4 — Đọc nhiều loại cảm biến

**Từ vựng trong mục:** **Override** — ghi đè.

**Tình huống thực tế:** Một hệ thống giám sát đang cần giải quyết việc đọc nhiều loại cảm biến. Thông tin đầu vào: Nhiệt độ 26.5 °C, độ ẩm 62%. Dữ liệu minh họa; khi có bảng, mỗi hàng là đối tượng và mỗi cột là một thuộc tính với ý nghĩa rõ. Hãy lập trình thực hiện việc này và in kết quả để nhân viên kiểm tra.

**Vì sao chọn cách giải?** Các cảm biến dùng chung read nhưng trả số đo khác nhau. Đây là phương án phù hợp bài toán nhỏ, không tự suy ra đủ an toàn với mọi dữ liệu thật.


**Quy trình:** Nắm dữ liệu → chọn cấu trúc/hàm → tính → in và kiểm tra kết quả.

```python
class Sensor:
    def read(self):return 0
class Temp(Sensor):
    def read(self):return 26.5
class Humidity(Sensor):
    def read(self):return 62
for s in [Temp(),Humidity()]:print(s.read())
```

**Đọc kết quả:** So sánh kết quả với tình huống đầu vào và thử trường hợp ngoại lệ.

### Tình huống 5 — Chuyển định dạng báo cáo

**Từ vựng trong mục:** **Inheritance** — kế thừa.

**Tình huống thực tế:** Một nhóm phát triển phần mềm đang cần giải quyết việc chuyển định dạng báo cáo. Thông tin đầu vào: Báo cáo plain và HTML. Dữ liệu minh họa; khi có bảng, mỗi hàng là đối tượng và mỗi cột là một thuộc tính với ý nghĩa rõ. Hãy lập trình thực hiện việc này và in kết quả để nhân viên kiểm tra.

**Vì sao chọn cách giải?** Ghi đè render giúp thêm loại xuất mà không sửa lời gọi. Đây là phương án phù hợp bài toán nhỏ, không tự suy ra đủ an toàn với mọi dữ liệu thật.


**Quy trình:** Nắm dữ liệu → chọn cấu trúc/hàm → tính → in và kiểm tra kết quả.

```python
class Report:
    def render(self):return "plain"
class HtmlReport(Report):
    def render(self):return "<p>report</p>"
print(HtmlReport().render())
```

**Đọc kết quả:** So sánh kết quả với tình huống đầu vào và thử trường hợp ngoại lệ.

## 6. Sai lầm thường gặp

- Không dùng đầu ra mẫu để suy diễn về người thật, hàng hóa thật hoặc kết quả dự đoán AI.
- Cần chú ý thứ tự xử lý, kiểu dữ liệu và đơn vị đo. Trường hợp rỗng/thiếu dữ liệu phải có cách xử lý rõ ràng.

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

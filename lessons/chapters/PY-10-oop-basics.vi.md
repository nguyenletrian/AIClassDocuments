# PY-10 — Class, Object, constructor và đóng gói

## 1. Vị trí trong chuỗi kiến thức

`Hàm / Dictionary → OOP → Kế thừa`

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Ý nghĩa |
|---|---|---|
| Class | lớp | Khuôn mô tả dữ liệu và cách xử lý |
| Object | đối tượng | Một thể hiện cụ thể của lớp |
| Constructor | hàm khởi tạo | Thiết lập thuộc tính lúc tạo instance |
| Encapsulation | đóng gói | Đặt dữ liệu và hành vi bên trong đối tượng |

## 3. Thư viện, hàm và tham số

| Hàm/cú pháp | Giải thích và lý do dùng |
|---|---|
| `class Name:` | Định nghĩa kiểu đối tượng và các phương thức |
| `__init__(self, ...)` | Khởi tạo trạng thái của từng instance |
| `self.attribute` | Truy cập thuộc tính thuộc về chính đối tượng |
| `__str__/set_*/get_*` | Hiển thị và kiểm tra thao tác thay đổi giá trị |

## 4. Khái niệm và ví dụ nhỏ

### 4.1. Class

Khuôn mô tả dữ liệu và cách xử lý.

```python
class P: pass
print(P)
```

### 4.2. Object

Một thể hiện cụ thể của lớp.

```python
class P: pass
print(type(P()))
```

### 4.3. Constructor

Thiết lập thuộc tính lúc tạo instance.

```python
class P:
    def __init__(self,x): self.x=x
print(P(3).x)
```

### 4.4. Encapsulation

Đặt dữ liệu và hành vi bên trong đối tượng.

```python
class Counter:
    def __init__(self): self.n=0
    def add(self): self.n+=1
c=Counter();c.add();print(c.n)
```

## 5. Năm tình huống lập trình thực tế

### Tình huống 1 — Tạo hồ sơ học viên

**Vì sao chọn cách giải?** Mỗi object giữ tên và điểm riêng, thay vì nhiều list song song.

**Dữ liệu:** Một sinh viên có tên An, điểm 8.

```python
class Student:
    def __init__(self,name,score): self.name,self.score=name,score
s=Student("An",8)
print(s.name,s.score)
```

### Tình huống 2 — Giỏ hàng có phương thức

**Vì sao chọn cách giải?** Đặt add và total cùng nơi lưu giá sản phẩm.

**Dữ liệu:** Giá [100,200] nghìn đồng.

```python
class Cart:
    def __init__(self): self.prices=[]
    def add(self,p): self.prices.append(p)
    def total(self): return sum(self.prices)
c=Cart();c.add(100);c.add(200)
print(c.total())
```

### Tình huống 3 — Ràng buộc điểm nhập

**Vì sao chọn cách giải?** Setter chặn điểm ngoài thang 0–10.

**Dữ liệu:** Một lần nhập 9/10.

```python
class Score:
    def __init__(self): self.value=0
    def set(self,x):
        if not 0<=x<=10: raise ValueError("score")
        self.value=x
s=Score();s.set(9);print(s.value)
```

### Tình huống 4 — In hóa đơn dễ đọc

**Vì sao chọn cách giải?** __str__ định nghĩa chữ hiện khi in đối tượng.

**Dữ liệu:** Đơn O01 trị giá 150000 đồng.

```python
class Order:
    def __init__(self,code,total):self.code,self.total=code,total
    def __str__(self):return f"{self.code}: {self.total} VND"
print(Order("O01",150000))
```

### Tình huống 5 — Hai cảm biến độc lập

**Vì sao chọn cách giải?** Instance khác nhau không chia sẻ nhầm dữ liệu đo.

**Dữ liệu:** Cảm biến A=20, B=40 độ C.

```python
class Sensor:
    def __init__(self,value): self.value=value
a,b=Sensor(20),Sensor(40)
a.value=25
print(a.value,b.value)
```

## 6. Sai lầm thường gặp

- Cần chú ý thứ tự xử lý, kiểu dữ liệu và đơn vị đo. Trường hợp rỗng/thiếu dữ liệu phải có cách xử lý rõ ràng.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ


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

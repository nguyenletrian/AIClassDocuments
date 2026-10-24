# PY-31 — Giới hạn, tính liên tục và đạo hàm


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Limit** — giới hạn; **Continuity** — tính liên tục.

`Hàm số → Limit → Derivative → Gradient`

Kiến thức này liên quan đến việc biểu diễn, đánh giá hoặc tối ưu tính toán phục vụ AI. Đọc ví dụ trước khi liên hệ tới mô hình phức tạp.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Ý nghĩa |
|---|---|---|
| Limit | giới hạn | Giá trị hàm tiến gần khi đầu vào tiến đến điểm |
| Continuity | tính liên tục | Giới hạn và giá trị hàm phù hợp tại điểm xét |
| Derivative | đạo hàm | Tốc độ thay đổi cục bộ của hàm theo đầu vào |
| Tangent slope | độ dốc tiếp tuyến | Giá trị đạo hàm tại một điểm |

## 3. Hàm và cách gọi bằng Python

**Từ vựng trong mục:** **Function** — hàm; **Parameter** — tham số.

| Hàm / tham số | Giải thích |
|---|---|
| `sympy.symbols()/limit()` | Tạo biến ký hiệu và tính giới hạn kể cả điểm không xác định |
| `sympy.diff(f,x)` | Đạo hàm theo biến x |
| `expr.subs(x,value)` | Thay giá trị vào công thức symbolic |
| `np.gradient(y,x)` | Ước lượng đạo hàm từ dãy mẫu, phụ thuộc bước lấy mẫu |

## 4. Các khái niệm liên quan

### 4.1. Limit

**Từ vựng trong mục:** **Limit** — giới hạn.

Giá trị hàm tiến gần khi đầu vào tiến đến điểm.

```python
import sympy as sp
x=sp.symbols('x');print(sp.limit((x*x-4)/(x-2),x,2))
```

**Tự kiểm tra:** Limit là gì? **Đáp án:** Giá trị hàm tiến gần khi đầu vào tiến đến điểm.

### 4.2. Continuity

**Từ vựng trong mục:** **Continuity** — tính liên tục.

Giới hạn và giá trị hàm phù hợp tại điểm xét.

```python
import sympy as sp
x=sp.symbols('x');print(sp.limit(x*x,x,2)==4)
```

**Tự kiểm tra:** Continuity là gì? **Đáp án:** Giới hạn và giá trị hàm phù hợp tại điểm xét.

### 4.3. Derivative

**Từ vựng trong mục:** **Derivative** — đạo hàm.

Tốc độ thay đổi cục bộ của hàm theo đầu vào.

```python
import sympy as sp
x=sp.symbols('x');print(sp.diff(x*x,x))
```

**Tự kiểm tra:** Derivative là gì? **Đáp án:** Tốc độ thay đổi cục bộ của hàm theo đầu vào.

### 4.4. Tangent slope

**Từ vựng trong mục:** **Tangent slope** — độ dốc tiếp tuyến.

Giá trị đạo hàm tại một điểm.

```python
import sympy as sp
x=sp.symbols('x');print(sp.diff(x*x,x).subs(x,3))
```

**Tự kiểm tra:** Tangent slope là gì? **Đáp án:** Giá trị đạo hàm tại một điểm.

## 5. Năm tình huống ứng dụng thực tế

### Tình huống 1 — Xem giá trị gần điểm rỗng

**Từ vựng trong mục:** **Limit** — giới hạn.

**Tình huống thực tế:** Một nhóm phân tích đang hỗ trợ quyết định vận hành cần xem giá trị gần điểm rỗng để phục vụ một công việc cụ thể. Đầu vào được cung cấp: (x²-4)/(x-2), khi x→2. Hãy viết chương trình xử lý thông tin trên và giải thích kết quả.

**Vì sao chọn phương án?** Giới hạn cho biết xu hướng dù biểu thức gốc không xác định tại điểm


**Quy trình:** xác định giá trị/hàm → chọn phương pháp → lập trình → quan sát giá trị/shape → thử thêm đầu vào.

```python
import sympy as sp
x=sp.symbols('x')
print(sp.limit((x*x-4)/(x-2),x,2))
```


### Tình huống 2 — Tốc độ tăng quãng đường

**Từ vựng trong mục:** **Continuity** — tính liên tục.

**Tình huống thực tế:** Một nhóm phân tích đang hỗ trợ quyết định vận hành cần tốc độ tăng quãng đường để phục vụ một công việc cụ thể. Đầu vào được cung cấp: Quãng đường s(t)=t², t=3 giây. Hãy viết chương trình xử lý thông tin trên và giải thích kết quả.

**Vì sao chọn phương án?** Đạo hàm quãng đường theo thời gian là vận tốc


**Quy trình:** xác định giá trị/hàm → chọn phương pháp → lập trình → quan sát giá trị/shape → thử thêm đầu vào.

```python
import sympy as sp
t=sp.symbols('t');v=sp.diff(t**2,t)
print(v.subs(t,3))
```


### Tình huống 3 — Độ dốc đường giá

**Từ vựng trong mục:** **Derivative** — đạo hàm.

**Tình huống thực tế:** Một nhóm phân tích đang hỗ trợ quyết định vận hành cần độ dốc đường giá để phục vụ một công việc cụ thể. Đầu vào được cung cấp: Hàm doanh thu f(x)=2x²+3x. Hãy viết chương trình xử lý thông tin trên và giải thích kết quả.

**Vì sao chọn phương án?** Tìm đạo hàm để biết xu hướng ở x=4


**Quy trình:** xác định giá trị/hàm → chọn phương pháp → lập trình → quan sát giá trị/shape → thử thêm đầu vào.

```python
import sympy as sp
x=sp.symbols('x');f=2*x*x+3*x
print(sp.diff(f,x).subs(x,4))
```


### Tình huống 4 — Kiểm liên tục hàm đơn giản

**Từ vựng trong mục:** **Tangent slope** — độ dốc tiếp tuyến.

**Tình huống thực tế:** Một nhóm phát triển AI cần kiểm liên tục hàm đơn giản để phục vụ một công việc cụ thể. Đầu vào được cung cấp: f(x)=x² tại x=2. Hãy viết chương trình xử lý thông tin trên và giải thích kết quả.

**Vì sao chọn phương án?** Đối chiếu limit và f(a)


**Quy trình:** xác định giá trị/hàm → chọn phương pháp → lập trình → quan sát giá trị/shape → thử thêm đầu vào.

```python
import sympy as sp
x=sp.symbols('x');f=x*x
print(sp.limit(f,x,2)==f.subs(x,2))
```


### Tình huống 5 — Ước lượng đạo hàm từ cảm biến

**Từ vựng trong mục:** **Limit** — giới hạn.

**Tình huống thực tế:** Một nhóm phát triển AI cần ước lượng đạo hàm từ cảm biến để phục vụ một công việc cụ thể. Đầu vào được cung cấp: 5 thời điểm cách nhau 1 giây. Hãy viết chương trình xử lý thông tin trên và giải thích kết quả.

**Vì sao chọn phương án?** gradient gần đúng khi dữ liệu chỉ có giá trị mẫu


**Quy trình:** xác định giá trị/hàm → chọn phương pháp → lập trình → quan sát giá trị/shape → thử thêm đầu vào.

```python
import numpy as np
time=np.arange(5.);distance=time**2
print(np.gradient(distance,time))
```


## 6. Các lỗi dễ gặp

Hàm kích hoạt và loss không tự thay thế quy trình huấn luyện; đạo hàm theo một biến không giống gradient nhiều biến. Tránh tràn số mũ, log(0), chia cho 0; luôn để ý learning rate và đơn vị.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.


**Q1. What does Limit mean? — Thuật ngữ Limit có nghĩa gì?**

A. It instead means Giới hạn và giá trị hàm phù hợp tại điểm xét — Giới hạn và giá trị hàm phù hợp tại điểm xét

B. It means Giá trị hàm tiến gần khi đầu vào tiến đến điểm — Giá trị hàm tiến gần khi đầu vào tiến đến điểm

C. It instead means Tốc độ thay đổi cục bộ của hàm theo đầu vào — Tốc độ thay đổi cục bộ của hàm theo đầu vào

D. It instead means Giá trị đạo hàm tại một điểm — Giá trị đạo hàm tại một điểm


**Q2. What does Continuity mean? — Thuật ngữ Continuity có nghĩa gì?**

A. It means Giới hạn và giá trị hàm phù hợp tại điểm xét — Giới hạn và giá trị hàm phù hợp tại điểm xét

B. It instead means Tốc độ thay đổi cục bộ của hàm theo đầu vào — Tốc độ thay đổi cục bộ của hàm theo đầu vào

C. It instead means Giá trị đạo hàm tại một điểm — Giá trị đạo hàm tại một điểm

D. It instead means Giá trị hàm tiến gần khi đầu vào tiến đến điểm — Giá trị hàm tiến gần khi đầu vào tiến đến điểm


**Q3. What does Derivative mean? — Thuật ngữ Derivative có nghĩa gì?**

A. It instead means Giá trị đạo hàm tại một điểm — Giá trị đạo hàm tại một điểm

B. It instead means Giá trị hàm tiến gần khi đầu vào tiến đến điểm — Giá trị hàm tiến gần khi đầu vào tiến đến điểm

C. It instead means Giới hạn và giá trị hàm phù hợp tại điểm xét — Giới hạn và giá trị hàm phù hợp tại điểm xét

D. It means Tốc độ thay đổi cục bộ của hàm theo đầu vào — Tốc độ thay đổi cục bộ của hàm theo đầu vào


**Q4. What does Tangent slope mean? — Thuật ngữ Tangent slope có nghĩa gì?**

A. It instead means Giá trị hàm tiến gần khi đầu vào tiến đến điểm — Giá trị hàm tiến gần khi đầu vào tiến đến điểm

B. It instead means Giới hạn và giá trị hàm phù hợp tại điểm xét — Giới hạn và giá trị hàm phù hợp tại điểm xét

C. It means Giá trị đạo hàm tại một điểm — Giá trị đạo hàm tại một điểm

D. It instead means Tốc độ thay đổi cục bộ của hàm theo đầu vào — Tốc độ thay đổi cục bộ của hàm theo đầu vào


**Q5. What does sympy.symbols()/limit() do? — Mục đích của sympy.symbols()/limit() là gì?**

A. Another operation does Đạo hàm theo biến x — Đạo hàm theo biến x

B. It is used to Tạo biến ký hiệu và tính giới hạn kể cả điểm không xác định — Tạo biến ký hiệu và tính giới hạn kể cả điểm không xác định

C. Another operation does Thay giá trị vào công thức symbolic — Thay giá trị vào công thức symbolic

D. Another operation does Ước lượng đạo hàm từ dãy mẫu, phụ thuộc bước lấy mẫu — Ước lượng đạo hàm từ dãy mẫu, phụ thuộc bước lấy mẫu


**Q6. What does sympy.diff(f,x) do? — Mục đích của sympy.diff(f,x) là gì?**

A. It is used to Đạo hàm theo biến x — Đạo hàm theo biến x

B. Another operation does Thay giá trị vào công thức symbolic — Thay giá trị vào công thức symbolic

C. Another operation does Ước lượng đạo hàm từ dãy mẫu, phụ thuộc bước lấy mẫu — Ước lượng đạo hàm từ dãy mẫu, phụ thuộc bước lấy mẫu

D. Another operation does Tạo biến ký hiệu và tính giới hạn kể cả điểm không xác định — Tạo biến ký hiệu và tính giới hạn kể cả điểm không xác định


**Q7. What does expr.subs(x,value) do? — Mục đích của expr.subs(x,value) là gì?**

A. Another operation does Ước lượng đạo hàm từ dãy mẫu, phụ thuộc bước lấy mẫu — Ước lượng đạo hàm từ dãy mẫu, phụ thuộc bước lấy mẫu

B. Another operation does Tạo biến ký hiệu và tính giới hạn kể cả điểm không xác định — Tạo biến ký hiệu và tính giới hạn kể cả điểm không xác định

C. Another operation does Đạo hàm theo biến x — Đạo hàm theo biến x

D. It is used to Thay giá trị vào công thức symbolic — Thay giá trị vào công thức symbolic


**Q8. What does np.gradient(y,x) do? — Mục đích của np.gradient(y,x) là gì?**

A. Another operation does Tạo biến ký hiệu và tính giới hạn kể cả điểm không xác định — Tạo biến ký hiệu và tính giới hạn kể cả điểm không xác định

B. Another operation does Đạo hàm theo biến x — Đạo hàm theo biến x

C. It is used to Ước lượng đạo hàm từ dãy mẫu, phụ thuộc bước lấy mẫu — Ước lượng đạo hàm từ dãy mẫu, phụ thuộc bước lấy mẫu

D. Another operation does Thay giá trị vào công thức symbolic — Thay giá trị vào công thức symbolic


**Q9. Why use this method in scenario 1? — Vì sao chọn cách giải ở tình huống 1?**

A. Đạo hàm quãng đường theo thời gian là vận tốc — Đạo hàm quãng đường theo thời gian là vận tốc

B. Giới hạn cho biết xu hướng dù biểu thức gốc không xác định tại điểm — Giới hạn cho biết xu hướng dù biểu thức gốc không xác định tại điểm

C. Tìm đạo hàm để biết xu hướng ở x=4 — Tìm đạo hàm để biết xu hướng ở x=4

D. Đối chiếu limit và f(a) — Đối chiếu limit và f(a)


**Q10. Why use this method in scenario 2? — Vì sao chọn cách giải ở tình huống 2?**

A. Đạo hàm quãng đường theo thời gian là vận tốc — Đạo hàm quãng đường theo thời gian là vận tốc

B. Tìm đạo hàm để biết xu hướng ở x=4 — Tìm đạo hàm để biết xu hướng ở x=4

C. Đối chiếu limit và f(a) — Đối chiếu limit và f(a)

D. gradient gần đúng khi dữ liệu chỉ có giá trị mẫu — gradient gần đúng khi dữ liệu chỉ có giá trị mẫu


**Q11. Why use this method in scenario 3? — Vì sao chọn cách giải ở tình huống 3?**

A. Đối chiếu limit và f(a) — Đối chiếu limit và f(a)

B. gradient gần đúng khi dữ liệu chỉ có giá trị mẫu — gradient gần đúng khi dữ liệu chỉ có giá trị mẫu

C. Giới hạn cho biết xu hướng dù biểu thức gốc không xác định tại điểm — Giới hạn cho biết xu hướng dù biểu thức gốc không xác định tại điểm

D. Tìm đạo hàm để biết xu hướng ở x=4 — Tìm đạo hàm để biết xu hướng ở x=4


**Q12. Why use this method in scenario 4? — Vì sao chọn cách giải ở tình huống 4?**

A. gradient gần đúng khi dữ liệu chỉ có giá trị mẫu — gradient gần đúng khi dữ liệu chỉ có giá trị mẫu

B. Giới hạn cho biết xu hướng dù biểu thức gốc không xác định tại điểm — Giới hạn cho biết xu hướng dù biểu thức gốc không xác định tại điểm

C. Đối chiếu limit và f(a) — Đối chiếu limit và f(a)

D. Đạo hàm quãng đường theo thời gian là vận tốc — Đạo hàm quãng đường theo thời gian là vận tốc


**Q13. Why use this method in scenario 5? — Vì sao chọn cách giải ở tình huống 5?**

A. Giới hạn cho biết xu hướng dù biểu thức gốc không xác định tại điểm — Giới hạn cho biết xu hướng dù biểu thức gốc không xác định tại điểm

B. gradient gần đúng khi dữ liệu chỉ có giá trị mẫu — gradient gần đúng khi dữ liệu chỉ có giá trị mẫu

C. Đạo hàm quãng đường theo thời gian là vận tốc — Đạo hàm quãng đường theo thời gian là vận tốc

D. Tìm đạo hàm để biết xu hướng ở x=4 — Tìm đạo hàm để biết xu hướng ở x=4


**Q14. Which input belongs to scenario 1? — Tình huống 1 sử dụng dữ liệu gì?**

A. The input is (x²-4)/(x-2), khi x→2 — (x²-4)/(x-2), khi x→2

B. Another input is Quãng đường s(t)=t², t=3 giây — Quãng đường s(t)=t², t=3 giây

C. Another input is Hàm doanh thu f(x)=2x²+3x — Hàm doanh thu f(x)=2x²+3x

D. Another input is f(x)=x² tại x=2 — f(x)=x² tại x=2


**Q15. Which input belongs to scenario 2? — Tình huống 2 sử dụng dữ liệu gì?**

A. Another input is Hàm doanh thu f(x)=2x²+3x — Hàm doanh thu f(x)=2x²+3x

B. Another input is f(x)=x² tại x=2 — f(x)=x² tại x=2

C. Another input is 5 thời điểm cách nhau 1 giây — 5 thời điểm cách nhau 1 giây

D. The input is Quãng đường s(t)=t², t=3 giây — Quãng đường s(t)=t², t=3 giây


**Q16. Which input belongs to scenario 3? — Tình huống 3 sử dụng dữ liệu gì?**

A. Another input is f(x)=x² tại x=2 — f(x)=x² tại x=2

B. Another input is 5 thời điểm cách nhau 1 giây — 5 thời điểm cách nhau 1 giây

C. The input is Hàm doanh thu f(x)=2x²+3x — Hàm doanh thu f(x)=2x²+3x

D. Another input is (x²-4)/(x-2), khi x→2 — (x²-4)/(x-2), khi x→2


**Q17. Which input belongs to scenario 4? — Tình huống 4 sử dụng dữ liệu gì?**

A. Another input is 5 thời điểm cách nhau 1 giây — 5 thời điểm cách nhau 1 giây

B. The input is f(x)=x² tại x=2 — f(x)=x² tại x=2

C. Another input is (x²-4)/(x-2), khi x→2 — (x²-4)/(x-2), khi x→2

D. Another input is Quãng đường s(t)=t², t=3 giây — Quãng đường s(t)=t², t=3 giây


**Q18. Which input belongs to scenario 5? — Tình huống 5 sử dụng dữ liệu gì?**

A. The input is 5 thời điểm cách nhau 1 giây — 5 thời điểm cách nhau 1 giây

B. Another input is (x²-4)/(x-2), khi x→2 — (x²-4)/(x-2), khi x→2

C. Another input is Quãng đường s(t)=t², t=3 giây — Quãng đường s(t)=t², t=3 giây

D. Another input is Hàm doanh thu f(x)=2x²+3x — Hàm doanh thu f(x)=2x²+3x


**Q19. What must be known before computing? — Trước khi tính phải biết gì?**

A. Only editor color — Chỉ màu giao diện

B. Only filename — Chỉ tên file

C. Only number of comments — Chỉ số lượng comment

D. Input meaning and units — Ý nghĩa và đơn vị đầu vào


**Q20. What makes a calculation trustworthy? — Điều gì giúp phép tính đáng tin?**

A. Assume models never fail — Cho rằng mô hình không bao giờ sai

B. Delete validation — Xóa bước xác minh

C. Verify results and edge cases — Kiểm tra kết quả và trường hợp biên

D. Guess data units — Đoán đơn vị dữ liệu

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **B** | It means Giá trị hàm tiến gần khi đầu vào tiến đến điểm | Giá trị hàm tiến gần khi đầu vào tiến đến điểm |
| Q2 | **A** | It means Giới hạn và giá trị hàm phù hợp tại điểm xét | Giới hạn và giá trị hàm phù hợp tại điểm xét |
| Q3 | **D** | It means Tốc độ thay đổi cục bộ của hàm theo đầu vào | Tốc độ thay đổi cục bộ của hàm theo đầu vào |
| Q4 | **C** | It means Giá trị đạo hàm tại một điểm | Giá trị đạo hàm tại một điểm |
| Q5 | **B** | It is used to Tạo biến ký hiệu và tính giới hạn kể cả điểm không xác định | Tạo biến ký hiệu và tính giới hạn kể cả điểm không xác định |
| Q6 | **A** | It is used to Đạo hàm theo biến x | Đạo hàm theo biến x |
| Q7 | **D** | It is used to Thay giá trị vào công thức symbolic | Thay giá trị vào công thức symbolic |
| Q8 | **C** | It is used to Ước lượng đạo hàm từ dãy mẫu, phụ thuộc bước lấy mẫu | Ước lượng đạo hàm từ dãy mẫu, phụ thuộc bước lấy mẫu |
| Q9 | **B** | Giới hạn cho biết xu hướng dù biểu thức gốc không xác định tại điểm | Giới hạn cho biết xu hướng dù biểu thức gốc không xác định tại điểm |
| Q10 | **A** | Đạo hàm quãng đường theo thời gian là vận tốc | Đạo hàm quãng đường theo thời gian là vận tốc |
| Q11 | **D** | Tìm đạo hàm để biết xu hướng ở x=4 | Tìm đạo hàm để biết xu hướng ở x=4 |
| Q12 | **C** | Đối chiếu limit và f(a) | Đối chiếu limit và f(a) |
| Q13 | **B** | gradient gần đúng khi dữ liệu chỉ có giá trị mẫu | gradient gần đúng khi dữ liệu chỉ có giá trị mẫu |
| Q14 | **A** | The input is (x²-4)/(x-2), khi x→2 | (x²-4)/(x-2), khi x→2 |
| Q15 | **D** | The input is Quãng đường s(t)=t², t=3 giây | Quãng đường s(t)=t², t=3 giây |
| Q16 | **C** | The input is Hàm doanh thu f(x)=2x²+3x | Hàm doanh thu f(x)=2x²+3x |
| Q17 | **B** | The input is f(x)=x² tại x=2 | f(x)=x² tại x=2 |
| Q18 | **A** | The input is 5 thời điểm cách nhau 1 giây | 5 thời điểm cách nhau 1 giây |
| Q19 | **D** | Input meaning and units | Ý nghĩa và đơn vị đầu vào |
| Q20 | **C** | Verify results and edge cases | Kiểm tra kết quả và trường hợp biên |

## 8. Bài tiếp theo

`Hàm số → Limit → Derivative → Gradient`.

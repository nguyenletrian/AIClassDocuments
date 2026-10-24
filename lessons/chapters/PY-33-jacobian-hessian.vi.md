# PY-33 — Jacobian, Hessian và điểm cực trị

## 1. Vị trí trong chuỗi kiến thức

`Gradient → Jacobian → Hessian → Tối ưu mô hình`

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Khái niệm |
|---|---|---|
| Jacobian | ma trận Jacobian | Bảng đạo hàm riêng bậc 1 của hàm nhiều đầu ra |
| Hessian | ma trận Hessian | Bảng đạo hàm riêng bậc hai của hàm vô hướng |
| Critical point | điểm tới hạn | Điểm có gradient bằng 0 hoặc không xác định |
| Curvature | độ cong | Cách độ dốc biến thiên quanh vị trí đang xét |

## 3. Hàm Python và tham số quan trọng

| Hàm / cú pháp | Cách sử dụng |
|---|---|
| `sympy.Matrix([...]).jacobian(vars)` | Đạo hàm riêng hàm vector theo biến |
| `sympy.hessian(f,vars)` | Đạo hàm bậc hai của hàm vô hướng |
| `sympy.solve(equations,vars)` | Tìm điểm thỏa hệ điều kiện |
| `np.linalg.eigvalsh(H)` | Xét dấu eigenvalue Hessian đối xứng tại điểm cực trị |

## 4. Khái niệm liên quan, ví dụ nhỏ

### 4.1. Jacobian

Bảng đạo hàm riêng bậc 1 của hàm nhiều đầu ra.

```python
import sympy as sp
x,y=sp.symbols('x y');F=sp.Matrix([x+y,x*y]);print(F.jacobian([x,y]))
```

### 4.2. Hessian

Bảng đạo hàm riêng bậc hai của hàm vô hướng.

```python
import sympy as sp
x,y=sp.symbols('x y');print(sp.hessian(x*x+y*y,[x,y]))
```

### 4.3. Critical point

Điểm có gradient bằng 0 hoặc không xác định.

```python
import sympy as sp
x=sp.symbols('x');print(sp.solve(sp.diff(x*x,x),x))
```

### 4.4. Curvature

Cách độ dốc biến thiên quanh vị trí đang xét.

```python
import sympy as sp
x=sp.symbols('x');print(sp.diff(x*x,x,2))
```

## 5. Năm tình huống thực tế

### Tình huống 1 — Độ nhạy hai đầu ra cảm biến

**Vấn đề:** Độ nhạy hai đầu ra cảm biến.

**Vì sao chọn phương pháp này?** Jacobian diễn tả hai đầu ra thay đổi theo nhiệt độ và áp suất.

**Dữ liệu:** F1=x+y, F2=x*y.

```python
import sympy as sp
x,y=sp.symbols("x y")
F=sp.Matrix([x+y,x*y])
print(F.jacobian([x,y]).subs({x:3,y:2}))
```

### Tình huống 2 — Độ cong hàm lỗi

**Vấn đề:** Độ cong hàm lỗi.

**Vì sao chọn phương pháp này?** Hessian giúp thấy loss tăng nhanh theo các hướng khác nhau.

**Dữ liệu:** f=x²+2y².

```python
import sympy as sp
x,y=sp.symbols("x y")
print(sp.hessian(x*x+2*y*y,[x,y]))
```

### Tình huống 3 — Tìm tối ưu chi phí

**Vấn đề:** Tìm tối ưu chi phí.

**Vì sao chọn phương pháp này?** Giải gradient=0 cho hàm bậc hai.

**Dữ liệu:** f=(x-3)²+(y-2)².

```python
import sympy as sp
x,y=sp.symbols("x y");f=(x-3)**2+(y-2)**2
print(sp.solve([sp.diff(f,x),sp.diff(f,y)],[x,y]))
```

### Tình huống 4 — Phân biệt cực tiểu và cực đại

**Vấn đề:** Phân biệt cực tiểu và cực đại.

**Vì sao chọn phương pháp này?** Eigenvalue Hessian dương ở điểm tới hạn gợi ý cực tiểu địa phương.

**Dữ liệu:** f=x²+y² tại (0,0).

```python
import sympy as sp,numpy as np
x,y=sp.symbols("x y");H=sp.hessian(x*x+y*y,[x,y])
print(np.linalg.eigvalsh(np.array(H,dtype=float)))
```

### Tình huống 5 — Độ nhạy hàm nhiều đầu ra

**Vấn đề:** Độ nhạy hàm nhiều đầu ra.

**Vì sao chọn phương pháp này?** Kiểm Jacobian đầu ra có shape đúng.

**Dữ liệu:** F gồm hai hàm của 2 biến.

```python
import sympy as sp
x,y=sp.symbols("x y")
J=sp.Matrix([x*x+y,x+y*y]).jacobian([x,y])
print(J.shape)
```

## 6. Những nhầm lẫn thường gặp

Xác suất có điều kiện cần mẫu nền; xác suất của phân phối liên tục tại một điểm không phải PDF; thống kê từ một nhóm nhỏ không tự chứng minh kết quả cho quần thể. Chú ý định nghĩa mean/std và giả định độc lập.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ


**Q1. What is Jacobian? — Thuật ngữ Jacobian là gì?**

A. Another concept means Bảng đạo hàm riêng bậc hai của hàm vô hướng — Bảng đạo hàm riêng bậc hai của hàm vô hướng

B. It means Bảng đạo hàm riêng bậc 1 của hàm nhiều đầu ra — Bảng đạo hàm riêng bậc 1 của hàm nhiều đầu ra

C. Another concept means Điểm có gradient bằng 0 hoặc không xác định — Điểm có gradient bằng 0 hoặc không xác định

D. Another concept means Cách độ dốc biến thiên quanh vị trí đang xét — Cách độ dốc biến thiên quanh vị trí đang xét


**Q2. What is Hessian? — Thuật ngữ Hessian là gì?**

A. It means Bảng đạo hàm riêng bậc hai của hàm vô hướng — Bảng đạo hàm riêng bậc hai của hàm vô hướng

B. Another concept means Điểm có gradient bằng 0 hoặc không xác định — Điểm có gradient bằng 0 hoặc không xác định

C. Another concept means Cách độ dốc biến thiên quanh vị trí đang xét — Cách độ dốc biến thiên quanh vị trí đang xét

D. Another concept means Bảng đạo hàm riêng bậc 1 của hàm nhiều đầu ra — Bảng đạo hàm riêng bậc 1 của hàm nhiều đầu ra


**Q3. What is Critical point? — Thuật ngữ Critical point là gì?**

A. Another concept means Cách độ dốc biến thiên quanh vị trí đang xét — Cách độ dốc biến thiên quanh vị trí đang xét

B. Another concept means Bảng đạo hàm riêng bậc 1 của hàm nhiều đầu ra — Bảng đạo hàm riêng bậc 1 của hàm nhiều đầu ra

C. Another concept means Bảng đạo hàm riêng bậc hai của hàm vô hướng — Bảng đạo hàm riêng bậc hai của hàm vô hướng

D. It means Điểm có gradient bằng 0 hoặc không xác định — Điểm có gradient bằng 0 hoặc không xác định


**Q4. What is Curvature? — Thuật ngữ Curvature là gì?**

A. Another concept means Bảng đạo hàm riêng bậc 1 của hàm nhiều đầu ra — Bảng đạo hàm riêng bậc 1 của hàm nhiều đầu ra

B. Another concept means Bảng đạo hàm riêng bậc hai của hàm vô hướng — Bảng đạo hàm riêng bậc hai của hàm vô hướng

C. It means Cách độ dốc biến thiên quanh vị trí đang xét — Cách độ dốc biến thiên quanh vị trí đang xét

D. Another concept means Điểm có gradient bằng 0 hoặc không xác định — Điểm có gradient bằng 0 hoặc không xác định


**Q5. What does sympy.Matrix([...]).jacobian(vars) calculate? — Hàm sympy.Matrix([...]).jacobian(vars) tính gì?**

A. Another calculation is Đạo hàm bậc hai của hàm vô hướng — Đạo hàm bậc hai của hàm vô hướng

B. It calculates Đạo hàm riêng hàm vector theo biến — Đạo hàm riêng hàm vector theo biến

C. Another calculation is Tìm điểm thỏa hệ điều kiện — Tìm điểm thỏa hệ điều kiện

D. Another calculation is Xét dấu eigenvalue Hessian đối xứng tại điểm cực trị — Xét dấu eigenvalue Hessian đối xứng tại điểm cực trị


**Q6. What does sympy.hessian(f,vars) calculate? — Hàm sympy.hessian(f,vars) tính gì?**

A. It calculates Đạo hàm bậc hai của hàm vô hướng — Đạo hàm bậc hai của hàm vô hướng

B. Another calculation is Tìm điểm thỏa hệ điều kiện — Tìm điểm thỏa hệ điều kiện

C. Another calculation is Xét dấu eigenvalue Hessian đối xứng tại điểm cực trị — Xét dấu eigenvalue Hessian đối xứng tại điểm cực trị

D. Another calculation is Đạo hàm riêng hàm vector theo biến — Đạo hàm riêng hàm vector theo biến


**Q7. What does sympy.solve(equations,vars) calculate? — Hàm sympy.solve(equations,vars) tính gì?**

A. Another calculation is Xét dấu eigenvalue Hessian đối xứng tại điểm cực trị — Xét dấu eigenvalue Hessian đối xứng tại điểm cực trị

B. Another calculation is Đạo hàm riêng hàm vector theo biến — Đạo hàm riêng hàm vector theo biến

C. Another calculation is Đạo hàm bậc hai của hàm vô hướng — Đạo hàm bậc hai của hàm vô hướng

D. It calculates Tìm điểm thỏa hệ điều kiện — Tìm điểm thỏa hệ điều kiện


**Q8. What does np.linalg.eigvalsh(H) calculate? — Hàm np.linalg.eigvalsh(H) tính gì?**

A. Another calculation is Đạo hàm riêng hàm vector theo biến — Đạo hàm riêng hàm vector theo biến

B. Another calculation is Đạo hàm bậc hai của hàm vô hướng — Đạo hàm bậc hai của hàm vô hướng

C. It calculates Xét dấu eigenvalue Hessian đối xứng tại điểm cực trị — Xét dấu eigenvalue Hessian đối xứng tại điểm cực trị

D. Another calculation is Tìm điểm thỏa hệ điều kiện — Tìm điểm thỏa hệ điều kiện


**Q9. Why use this method in scenario 1? — Vì sao chọn phương pháp trong tình huống 1?**

A. Hessian giúp thấy loss tăng nhanh theo các hướng khác nhau — Hessian giúp thấy loss tăng nhanh theo các hướng khác nhau

B. Jacobian diễn tả hai đầu ra thay đổi theo nhiệt độ và áp suất — Jacobian diễn tả hai đầu ra thay đổi theo nhiệt độ và áp suất

C. Giải gradient=0 cho hàm bậc hai — Giải gradient=0 cho hàm bậc hai

D. Eigenvalue Hessian dương ở điểm tới hạn gợi ý cực tiểu địa phương — Eigenvalue Hessian dương ở điểm tới hạn gợi ý cực tiểu địa phương


**Q10. Why use this method in scenario 2? — Vì sao chọn phương pháp trong tình huống 2?**

A. Hessian giúp thấy loss tăng nhanh theo các hướng khác nhau — Hessian giúp thấy loss tăng nhanh theo các hướng khác nhau

B. Giải gradient=0 cho hàm bậc hai — Giải gradient=0 cho hàm bậc hai

C. Eigenvalue Hessian dương ở điểm tới hạn gợi ý cực tiểu địa phương — Eigenvalue Hessian dương ở điểm tới hạn gợi ý cực tiểu địa phương

D. Kiểm Jacobian đầu ra có shape đúng — Kiểm Jacobian đầu ra có shape đúng


**Q11. Why use this method in scenario 3? — Vì sao chọn phương pháp trong tình huống 3?**

A. Eigenvalue Hessian dương ở điểm tới hạn gợi ý cực tiểu địa phương — Eigenvalue Hessian dương ở điểm tới hạn gợi ý cực tiểu địa phương

B. Kiểm Jacobian đầu ra có shape đúng — Kiểm Jacobian đầu ra có shape đúng

C. Jacobian diễn tả hai đầu ra thay đổi theo nhiệt độ và áp suất — Jacobian diễn tả hai đầu ra thay đổi theo nhiệt độ và áp suất

D. Giải gradient=0 cho hàm bậc hai — Giải gradient=0 cho hàm bậc hai


**Q12. Why use this method in scenario 4? — Vì sao chọn phương pháp trong tình huống 4?**

A. Kiểm Jacobian đầu ra có shape đúng — Kiểm Jacobian đầu ra có shape đúng

B. Jacobian diễn tả hai đầu ra thay đổi theo nhiệt độ và áp suất — Jacobian diễn tả hai đầu ra thay đổi theo nhiệt độ và áp suất

C. Eigenvalue Hessian dương ở điểm tới hạn gợi ý cực tiểu địa phương — Eigenvalue Hessian dương ở điểm tới hạn gợi ý cực tiểu địa phương

D. Hessian giúp thấy loss tăng nhanh theo các hướng khác nhau — Hessian giúp thấy loss tăng nhanh theo các hướng khác nhau


**Q13. Why use this method in scenario 5? — Vì sao chọn phương pháp trong tình huống 5?**

A. Jacobian diễn tả hai đầu ra thay đổi theo nhiệt độ và áp suất — Jacobian diễn tả hai đầu ra thay đổi theo nhiệt độ và áp suất

B. Kiểm Jacobian đầu ra có shape đúng — Kiểm Jacobian đầu ra có shape đúng

C. Hessian giúp thấy loss tăng nhanh theo các hướng khác nhau — Hessian giúp thấy loss tăng nhanh theo các hướng khác nhau

D. Giải gradient=0 cho hàm bậc hai — Giải gradient=0 cho hàm bậc hai


**Q14. Which input is from scenario 1? — Dữ liệu nào thuộc tình huống 1?**

A. The input is F1=x+y, F2=x*y — F1=x+y, F2=x*y

B. Another input is f=x²+2y² — f=x²+2y²

C. Another input is f=(x-3)²+(y-2)² — f=(x-3)²+(y-2)²

D. Another input is f=x²+y² tại (0,0) — f=x²+y² tại (0,0)


**Q15. Which input is from scenario 2? — Dữ liệu nào thuộc tình huống 2?**

A. Another input is f=(x-3)²+(y-2)² — f=(x-3)²+(y-2)²

B. Another input is f=x²+y² tại (0,0) — f=x²+y² tại (0,0)

C. Another input is F gồm hai hàm của 2 biến — F gồm hai hàm của 2 biến

D. The input is f=x²+2y² — f=x²+2y²


**Q16. Which input is from scenario 3? — Dữ liệu nào thuộc tình huống 3?**

A. Another input is f=x²+y² tại (0,0) — f=x²+y² tại (0,0)

B. Another input is F gồm hai hàm của 2 biến — F gồm hai hàm của 2 biến

C. The input is f=(x-3)²+(y-2)² — f=(x-3)²+(y-2)²

D. Another input is F1=x+y, F2=x*y — F1=x+y, F2=x*y


**Q17. Which input is from scenario 4? — Dữ liệu nào thuộc tình huống 4?**

A. Another input is F gồm hai hàm của 2 biến — F gồm hai hàm của 2 biến

B. The input is f=x²+y² tại (0,0) — f=x²+y² tại (0,0)

C. Another input is F1=x+y, F2=x*y — F1=x+y, F2=x*y

D. Another input is f=x²+2y² — f=x²+2y²


**Q18. Which input is from scenario 5? — Dữ liệu nào thuộc tình huống 5?**

A. The input is F gồm hai hàm của 2 biến — F gồm hai hàm của 2 biến

B. Another input is F1=x+y, F2=x*y — F1=x+y, F2=x*y

C. Another input is f=x²+2y² — f=x²+2y²

D. Another input is f=(x-3)²+(y-2)² — f=(x-3)²+(y-2)²


**Q19. What must a statistical report mention? — Báo cáo thống kê cần nêu gì?**

A. Only plot colors — Chỉ màu biểu đồ

B. Only a filename — Chỉ tên tệp

C. Only code line count — Chỉ số dòng code

D. Assumptions, units and sample size — Giả định, đơn vị và kích thước mẫu


**Q20. What makes a numerical result reliable? — Điều gì làm kết quả số đáng tin?**

A. Assuming all data independent — Cho rằng mọi dữ liệu độc lập

B. Deleting verification — Xóa bước xác minh

C. Checking assumptions and edge cases — Kiểm tra giả định và trường hợp biên

D. Ignoring missing inputs — Bỏ dữ liệu thiếu mà không đánh giá

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **B** | It means Bảng đạo hàm riêng bậc 1 của hàm nhiều đầu ra | Bảng đạo hàm riêng bậc 1 của hàm nhiều đầu ra |
| Q2 | **A** | It means Bảng đạo hàm riêng bậc hai của hàm vô hướng | Bảng đạo hàm riêng bậc hai của hàm vô hướng |
| Q3 | **D** | It means Điểm có gradient bằng 0 hoặc không xác định | Điểm có gradient bằng 0 hoặc không xác định |
| Q4 | **C** | It means Cách độ dốc biến thiên quanh vị trí đang xét | Cách độ dốc biến thiên quanh vị trí đang xét |
| Q5 | **B** | It calculates Đạo hàm riêng hàm vector theo biến | Đạo hàm riêng hàm vector theo biến |
| Q6 | **A** | It calculates Đạo hàm bậc hai của hàm vô hướng | Đạo hàm bậc hai của hàm vô hướng |
| Q7 | **D** | It calculates Tìm điểm thỏa hệ điều kiện | Tìm điểm thỏa hệ điều kiện |
| Q8 | **C** | It calculates Xét dấu eigenvalue Hessian đối xứng tại điểm cực trị | Xét dấu eigenvalue Hessian đối xứng tại điểm cực trị |
| Q9 | **B** | Jacobian diễn tả hai đầu ra thay đổi theo nhiệt độ và áp suất | Jacobian diễn tả hai đầu ra thay đổi theo nhiệt độ và áp suất |
| Q10 | **A** | Hessian giúp thấy loss tăng nhanh theo các hướng khác nhau | Hessian giúp thấy loss tăng nhanh theo các hướng khác nhau |
| Q11 | **D** | Giải gradient=0 cho hàm bậc hai | Giải gradient=0 cho hàm bậc hai |
| Q12 | **C** | Eigenvalue Hessian dương ở điểm tới hạn gợi ý cực tiểu địa phương | Eigenvalue Hessian dương ở điểm tới hạn gợi ý cực tiểu địa phương |
| Q13 | **B** | Kiểm Jacobian đầu ra có shape đúng | Kiểm Jacobian đầu ra có shape đúng |
| Q14 | **A** | The input is F1=x+y, F2=x*y | F1=x+y, F2=x*y |
| Q15 | **D** | The input is f=x²+2y² | f=x²+2y² |
| Q16 | **C** | The input is f=(x-3)²+(y-2)² | f=(x-3)²+(y-2)² |
| Q17 | **B** | The input is f=x²+y² tại (0,0) | f=x²+y² tại (0,0) |
| Q18 | **A** | The input is F gồm hai hàm của 2 biến | F gồm hai hàm của 2 biến |
| Q19 | **D** | Assumptions, units and sample size | Giả định, đơn vị và kích thước mẫu |
| Q20 | **C** | Checking assumptions and edge cases | Kiểm tra giả định và trường hợp biên |

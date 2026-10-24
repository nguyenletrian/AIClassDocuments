# PY-33 — Jacobian, Hessian và điểm cực trị


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Jacobian** — ma trận Jacobian; **Hessian** — ma trận Hessian.

`Gradient → Jacobian → Hessian → Tối ưu mô hình`

Bài này kết nối dữ liệu thực nghiệm với cách tính xác suất, thống kê và các bước học máy.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Khái niệm |
|---|---|---|
| Jacobian | ma trận Jacobian | Bảng đạo hàm riêng bậc 1 của hàm nhiều đầu ra |
| Hessian | ma trận Hessian | Bảng đạo hàm riêng bậc hai của hàm vô hướng |
| Critical point | điểm tới hạn | Điểm có gradient bằng 0 hoặc không xác định |
| Curvature | độ cong | Cách độ dốc biến thiên quanh vị trí đang xét |

## 3. Hàm Python và tham số quan trọng

**Từ vựng trong mục:** **Function** — hàm; **Parameter** — tham số.

| Hàm / cú pháp | Cách sử dụng |
|---|---|
| `sympy.Matrix([...]).jacobian(vars)` | Đạo hàm riêng hàm vector theo biến |
| `sympy.hessian(f,vars)` | Đạo hàm bậc hai của hàm vô hướng |
| `sympy.solve(equations,vars)` | Tìm điểm thỏa hệ điều kiện |
| `np.linalg.eigvalsh(H)` | Xét dấu eigenvalue Hessian đối xứng tại điểm cực trị |

## 4. Khái niệm liên quan, ví dụ nhỏ

### 4.1. Jacobian

**Từ vựng trong mục:** **Jacobian** — ma trận Jacobian.

Bảng đạo hàm riêng bậc 1 của hàm nhiều đầu ra. Trước khi tính, phân biệt điều kiện áp dụng và ý nghĩa của đầu vào.

```python
import sympy as sp
x,y=sp.symbols('x y');F=sp.Matrix([x+y,x*y]);print(F.jacobian([x,y]))
```

**Tự kiểm tra:** Jacobian là gì? **Đáp án:** Bảng đạo hàm riêng bậc 1 của hàm nhiều đầu ra.

### 4.2. Hessian

**Từ vựng trong mục:** **Hessian** — ma trận Hessian.

Bảng đạo hàm riêng bậc hai của hàm vô hướng. Trước khi tính, phân biệt điều kiện áp dụng và ý nghĩa của đầu vào.

```python
import sympy as sp
x,y=sp.symbols('x y');print(sp.hessian(x*x+y*y,[x,y]))
```

**Tự kiểm tra:** Hessian là gì? **Đáp án:** Bảng đạo hàm riêng bậc hai của hàm vô hướng.

### 4.3. Critical point

**Từ vựng trong mục:** **Critical point** — điểm tới hạn.

Điểm có gradient bằng 0 hoặc không xác định. Trước khi tính, phân biệt điều kiện áp dụng và ý nghĩa của đầu vào.

```python
import sympy as sp
x=sp.symbols('x');print(sp.solve(sp.diff(x*x,x),x))
```

**Tự kiểm tra:** Critical point là gì? **Đáp án:** Điểm có gradient bằng 0 hoặc không xác định.

### 4.4. Curvature

**Từ vựng trong mục:** **Curvature** — độ cong.

Cách độ dốc biến thiên quanh vị trí đang xét. Trước khi tính, phân biệt điều kiện áp dụng và ý nghĩa của đầu vào.

```python
import sympy as sp
x=sp.symbols('x');print(sp.diff(x*x,x,2))
```

**Tự kiểm tra:** Curvature là gì? **Đáp án:** Cách độ dốc biến thiên quanh vị trí đang xét.

## 5. Năm tình huống thực tế

### Tình huống 1 — Độ nhạy hai đầu ra cảm biến

**Từ vựng trong mục:** **Jacobian** — ma trận Jacobian.

**Tình huống thực tế:** Một hệ thống giám sát cần độ nhạy hai đầu ra cảm biến để phục vụ một công việc cụ thể. Đầu vào được cung cấp: F1=x+y, F2=x*y. Các số liệu là giả lập và đơn vị/thứ tự được nêu ngay tại đây; không suy ra kết luận cho người thật. Hãy viết chương trình xử lý thông tin trên và giải thích kết quả.

**Vì sao chọn phương pháp này?** Jacobian diễn tả hai đầu ra thay đổi theo nhiệt độ và áp suất. Không dùng kết quả mô phỏng làm bằng chứng thống kê khi thiếu đủ mẫu và giả định.


**Quy trình:** làm rõ giả định → mô tả biến cố/đặc trưng → chọn hàm → kiểm tra kết quả, giới hạn và độ nhạy.

```python
import sympy as sp
x,y=sp.symbols("x y")
F=sp.Matrix([x+y,x*y])
print(F.jacobian([x,y]).subs({x:3,y:2}))
```

**Đọc kết quả:** Đối chiếu kết quả với ý nghĩa xác suất hoặc đơn vị đo; lưu ý sai số và cách lấy mẫu.

### Tình huống 2 — Độ cong hàm lỗi

**Từ vựng trong mục:** **Hessian** — ma trận Hessian.

**Tình huống thực tế:** Một nhóm phát triển AI cần độ cong hàm lỗi để phục vụ một công việc cụ thể. Đầu vào được cung cấp: f=x²+2y². Các số liệu là giả lập và đơn vị/thứ tự được nêu ngay tại đây; không suy ra kết luận cho người thật. Hãy viết chương trình xử lý thông tin trên và giải thích kết quả.

**Vì sao chọn phương pháp này?** Hessian giúp thấy loss tăng nhanh theo các hướng khác nhau. Không dùng kết quả mô phỏng làm bằng chứng thống kê khi thiếu đủ mẫu và giả định.


**Quy trình:** làm rõ giả định → mô tả biến cố/đặc trưng → chọn hàm → kiểm tra kết quả, giới hạn và độ nhạy.

```python
import sympy as sp
x,y=sp.symbols("x y")
print(sp.hessian(x*x+2*y*y,[x,y]))
```

**Đọc kết quả:** Đối chiếu kết quả với ý nghĩa xác suất hoặc đơn vị đo; lưu ý sai số và cách lấy mẫu.

### Tình huống 3 — Tìm tối ưu chi phí

**Từ vựng trong mục:** **Critical point** — điểm tới hạn.

**Tình huống thực tế:** Một nhóm phát triển AI cần tìm tối ưu chi phí để phục vụ một công việc cụ thể. Đầu vào được cung cấp: f=(x-3)²+(y-2)². Các số liệu là giả lập và đơn vị/thứ tự được nêu ngay tại đây; không suy ra kết luận cho người thật. Hãy viết chương trình xử lý thông tin trên và giải thích kết quả.

**Vì sao chọn phương pháp này?** Giải gradient=0 cho hàm bậc hai. Không dùng kết quả mô phỏng làm bằng chứng thống kê khi thiếu đủ mẫu và giả định.


**Quy trình:** làm rõ giả định → mô tả biến cố/đặc trưng → chọn hàm → kiểm tra kết quả, giới hạn và độ nhạy.

```python
import sympy as sp
x,y=sp.symbols("x y");f=(x-3)**2+(y-2)**2
print(sp.solve([sp.diff(f,x),sp.diff(f,y)],[x,y]))
```

**Đọc kết quả:** Đối chiếu kết quả với ý nghĩa xác suất hoặc đơn vị đo; lưu ý sai số và cách lấy mẫu.

### Tình huống 4 — Phân biệt cực tiểu và cực đại

**Từ vựng trong mục:** **Curvature** — độ cong.

**Tình huống thực tế:** Một nhóm phân tích đang hỗ trợ quyết định vận hành cần phân biệt cực tiểu và cực đại để phục vụ một công việc cụ thể. Đầu vào được cung cấp: f=x²+y² tại (0,0). Các số liệu là giả lập và đơn vị/thứ tự được nêu ngay tại đây; không suy ra kết luận cho người thật. Hãy viết chương trình xử lý thông tin trên và giải thích kết quả.

**Vì sao chọn phương pháp này?** Eigenvalue Hessian dương ở điểm tới hạn gợi ý cực tiểu địa phương. Không dùng kết quả mô phỏng làm bằng chứng thống kê khi thiếu đủ mẫu và giả định.


**Quy trình:** làm rõ giả định → mô tả biến cố/đặc trưng → chọn hàm → kiểm tra kết quả, giới hạn và độ nhạy.

```python
import sympy as sp,numpy as np
x,y=sp.symbols("x y");H=sp.hessian(x*x+y*y,[x,y])
print(np.linalg.eigvalsh(np.array(H,dtype=float)))
```

**Đọc kết quả:** Đối chiếu kết quả với ý nghĩa xác suất hoặc đơn vị đo; lưu ý sai số và cách lấy mẫu.

### Tình huống 5 — Độ nhạy hàm nhiều đầu ra

**Từ vựng trong mục:** **Jacobian** — ma trận Jacobian.

**Tình huống thực tế:** Một nhóm phát triển AI cần độ nhạy hàm nhiều đầu ra để phục vụ một công việc cụ thể. Đầu vào được cung cấp: F gồm hai hàm của 2 biến. Các số liệu là giả lập và đơn vị/thứ tự được nêu ngay tại đây; không suy ra kết luận cho người thật. Hãy viết chương trình xử lý thông tin trên và giải thích kết quả.

**Vì sao chọn phương pháp này?** Kiểm Jacobian đầu ra có shape đúng. Không dùng kết quả mô phỏng làm bằng chứng thống kê khi thiếu đủ mẫu và giả định.


**Quy trình:** làm rõ giả định → mô tả biến cố/đặc trưng → chọn hàm → kiểm tra kết quả, giới hạn và độ nhạy.

```python
import sympy as sp
x,y=sp.symbols("x y")
J=sp.Matrix([x*x+y,x+y*y]).jacobian([x,y])
print(J.shape)
```

**Đọc kết quả:** Đối chiếu kết quả với ý nghĩa xác suất hoặc đơn vị đo; lưu ý sai số và cách lấy mẫu.

## 6. Những nhầm lẫn thường gặp

Xác suất có điều kiện cần mẫu nền; xác suất của phân phối liên tục tại một điểm không phải PDF; thống kê từ một nhóm nhỏ không tự chứng minh kết quả cho quần thể. Chú ý định nghĩa mean/std và giả định độc lập.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.


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

## 8. Liên hệ bài tiếp theo

`Gradient → Jacobian → Hessian → Tối ưu mô hình`.

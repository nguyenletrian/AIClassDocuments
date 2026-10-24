# PY-32 — Đạo hàm riêng, gradient descent và learning rate

*DRAFT · Học qua Python · Cần kiểm tra kết quả và môi trường trước khi phát hành*

## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Partial derivative** — đạo hàm riêng; **Gradient** — vector gradient.

`Derivative → Gradient → Optimization → Training`

Kiến thức này liên quan đến việc biểu diễn, đánh giá hoặc tối ưu tính toán phục vụ AI. Đọc ví dụ trước khi liên hệ tới mô hình phức tạp.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Ý nghĩa |
|---|---|---|
| Partial derivative | đạo hàm riêng | Đạo hàm theo một biến khi các biến khác giữ cố định |
| Gradient | vector gradient | Vector gồm các đạo hàm riêng của hàm nhiều biến |
| Learning rate | tốc độ học | Bước nhân gradient khi cập nhật tham số |
| Epoch | vòng huấn luyện | Một lượt sử dụng hết dữ liệu train để cập nhật mô hình |

## 3. Hàm và cách gọi bằng Python

**Từ vựng trong mục:** **Function** — hàm; **Parameter** — tham số.

| Hàm / tham số | Giải thích |
|---|---|
| `sympy.diff(f,x)` | Đạo hàm riêng của hàm f theo x |
| `grad=[df/dx,df/dy,...]` | Ghép các đạo hàm riêng thành vector |
| `w = w - lr * gradient` | Cập nhật đi ngược hướng tăng loss |
| `np.mean((pred-y)**2)` | Loss MSE mẫu cho tối ưu hồi quy |

## 4. Các khái niệm liên quan

### 4.1. Partial derivative

**Từ vựng trong mục:** **Partial derivative** — đạo hàm riêng.

Đạo hàm theo một biến khi các biến khác giữ cố định. Thử mã nhỏ để nhìn thấy giá trị trước khi làm bài toán phức tạp hơn.

```python
import sympy as sp
x,y=sp.symbols('x y');print(sp.diff(x*x+3*x*y,x))
```

**Tự kiểm tra:** Partial derivative là gì? **Đáp án:** Đạo hàm theo một biến khi các biến khác giữ cố định.

### 4.2. Gradient

**Từ vựng trong mục:** **Gradient** — vector gradient.

Vector gồm các đạo hàm riêng của hàm nhiều biến. Thử mã nhỏ để nhìn thấy giá trị trước khi làm bài toán phức tạp hơn.

```python
import numpy as np
print(np.array([2*3.,2*4.]))
```

**Tự kiểm tra:** Gradient là gì? **Đáp án:** Vector gồm các đạo hàm riêng của hàm nhiều biến.

### 4.3. Learning rate

**Từ vựng trong mục:** **Learning rate** — tốc độ học.

Bước nhân gradient khi cập nhật tham số. Thử mã nhỏ để nhìn thấy giá trị trước khi làm bài toán phức tạp hơn.

```python
lr=.1;w=3.;print(w-lr*2*w)
```

**Tự kiểm tra:** Learning rate là gì? **Đáp án:** Bước nhân gradient khi cập nhật tham số.

### 4.4. Epoch

**Từ vựng trong mục:** **Epoch** — vòng huấn luyện.

Một lượt sử dụng hết dữ liệu train để cập nhật mô hình. Thử mã nhỏ để nhìn thấy giá trị trước khi làm bài toán phức tạp hơn.

```python
for epoch in range(3): print(epoch)
```

**Tự kiểm tra:** Epoch là gì? **Đáp án:** Một lượt sử dụng hết dữ liệu train để cập nhật mô hình.

## 5. Năm tình huống ứng dụng thực tế

### Tình huống 1 — Giảm chi phí một biến

**Từ vựng trong mục:** **Partial derivative** — đạo hàm riêng.

**Vấn đề:** Giảm chi phí một biến.

**Vì sao chọn phương án?** Cập nhật w theo độ dốc của hàm w²; không dùng công thức hoặc mô hình phức tạp hơn khi các giả định chưa được kiểm tra.

**Dữ liệu:** Bắt đầu w=4, lr=0.1, 10 bước. Các đơn vị và phép tính đã ghi trong đoạn mô tả; dữ liệu minh họa không dùng làm kết luận thực.

**Quy trình:** xác định giá trị/hàm → chọn phương pháp → lập trình → quan sát giá trị/shape → thử thêm đầu vào.

```python
w=4.;lr=.1
for step in range(10):
    w-=lr*2*w
print(round(w,4))
```

**Đọc kết quả:** So sánh số in ra với công thức trong bài. Nếu dữ liệu thực có nhiễu, phải kiểm tra điều kiện và giới hạn trước khi ứng dụng vào AI.

### Tình huống 2 — Đạo hàm riêng chi phí

**Từ vựng trong mục:** **Gradient** — vector gradient.

**Vấn đề:** Đạo hàm riêng chi phí.

**Vì sao chọn phương án?** Hàm hai biến f=x²+3xy+y² cần đạo hàm từng biến; không dùng công thức hoặc mô hình phức tạp hơn khi các giả định chưa được kiểm tra.

**Dữ liệu:** Hàm tại x=1,y=2. Các đơn vị và phép tính đã ghi trong đoạn mô tả; dữ liệu minh họa không dùng làm kết luận thực.

**Quy trình:** xác định giá trị/hàm → chọn phương pháp → lập trình → quan sát giá trị/shape → thử thêm đầu vào.

```python
import sympy as sp
x,y=sp.symbols('x y');f=x*x+3*x*y+y*y
print(sp.diff(f,x).subs({x:1,y:2}))
```

**Đọc kết quả:** So sánh số in ra với công thức trong bài. Nếu dữ liệu thực có nhiễu, phải kiểm tra điều kiện và giới hạn trước khi ứng dụng vào AI.

### Tình huống 3 — Theo dõi lịch sử loss

**Từ vựng trong mục:** **Learning rate** — tốc độ học.

**Vấn đề:** Theo dõi lịch sử loss.

**Vì sao chọn phương án?** Lưu loss sau từng bước để xem có giảm; không dùng công thức hoặc mô hình phức tạp hơn khi các giả định chưa được kiểm tra.

**Dữ liệu:** Hàm loss w² với w=3. Các đơn vị và phép tính đã ghi trong đoạn mô tả; dữ liệu minh họa không dùng làm kết luận thực.

**Quy trình:** xác định giá trị/hàm → chọn phương pháp → lập trình → quan sát giá trị/shape → thử thêm đầu vào.

```python
w=3.;history=[]
for step in range(5):
    history.append(w*w)
    w-=.1*2*w
print(history)
```

**Đọc kết quả:** So sánh số in ra với công thức trong bài. Nếu dữ liệu thực có nhiễu, phải kiểm tra điều kiện và giới hạn trước khi ứng dụng vào AI.

### Tình huống 4 — So tốc độ học

**Từ vựng trong mục:** **Epoch** — vòng huấn luyện.

**Vấn đề:** So tốc độ học.

**Vì sao chọn phương án?** Learning rate quá cao có thể làm mất ổn định; không dùng công thức hoặc mô hình phức tạp hơn khi các giả định chưa được kiểm tra.

**Dữ liệu:** w=4, lr 0.1 và 1.1. Các đơn vị và phép tính đã ghi trong đoạn mô tả; dữ liệu minh họa không dùng làm kết luận thực.

**Quy trình:** xác định giá trị/hàm → chọn phương pháp → lập trình → quan sát giá trị/shape → thử thêm đầu vào.

```python
for lr in [.1,1.1]:
    w=4.
    for _ in range(5):w-=lr*2*w
    print(lr,round(w*w,3))
```

**Đọc kết quả:** So sánh số in ra với công thức trong bài. Nếu dữ liệu thực có nhiễu, phải kiểm tra điều kiện và giới hạn trước khi ứng dụng vào AI.

### Tình huống 5 — Fit giá nhà bằng gradient

**Từ vựng trong mục:** **Partial derivative** — đạo hàm riêng.

**Vấn đề:** Fit giá nhà bằng gradient.

**Vì sao chọn phương án?** Tính dMSE/dw rồi cập nhật hệ số hồi quy tuyến tính; không dùng công thức hoặc mô hình phức tạp hơn khi các giả định chưa được kiểm tra.

**Dữ liệu:** X=[1,2,3], y=[2,4,6], 100 bước. Các đơn vị và phép tính đã ghi trong đoạn mô tả; dữ liệu minh họa không dùng làm kết luận thực.

**Quy trình:** xác định giá trị/hàm → chọn phương pháp → lập trình → quan sát giá trị/shape → thử thêm đầu vào.

```python
import numpy as np
x=np.array([1.,2.,3.]);y=np.array([2.,4.,6.])
w=0.;lr=.1
for _ in range(100):
    w-=lr*2*np.mean(x*(w*x-y))
print(round(w,3))
```

**Đọc kết quả:** So sánh số in ra với công thức trong bài. Nếu dữ liệu thực có nhiễu, phải kiểm tra điều kiện và giới hạn trước khi ứng dụng vào AI.

## 6. Các lỗi dễ gặp

Hàm kích hoạt và loss không tự thay thế quy trình huấn luyện; đạo hàm theo một biến không giống gradient nhiều biến. Tránh tràn số mũ, log(0), chia cho 0; luôn để ý learning rate và đơn vị.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.


**Q1. What does Partial derivative mean? — Thuật ngữ Partial derivative có nghĩa gì?**

A. It instead means Vector gồm các đạo hàm riêng của hàm nhiều biến — Vector gồm các đạo hàm riêng của hàm nhiều biến

B. It means Đạo hàm theo một biến khi các biến khác giữ cố định — Đạo hàm theo một biến khi các biến khác giữ cố định

C. It instead means Bước nhân gradient khi cập nhật tham số — Bước nhân gradient khi cập nhật tham số

D. It instead means Một lượt sử dụng hết dữ liệu train để cập nhật mô hình — Một lượt sử dụng hết dữ liệu train để cập nhật mô hình


**Q2. What does Gradient mean? — Thuật ngữ Gradient có nghĩa gì?**

A. It means Vector gồm các đạo hàm riêng của hàm nhiều biến — Vector gồm các đạo hàm riêng của hàm nhiều biến

B. It instead means Bước nhân gradient khi cập nhật tham số — Bước nhân gradient khi cập nhật tham số

C. It instead means Một lượt sử dụng hết dữ liệu train để cập nhật mô hình — Một lượt sử dụng hết dữ liệu train để cập nhật mô hình

D. It instead means Đạo hàm theo một biến khi các biến khác giữ cố định — Đạo hàm theo một biến khi các biến khác giữ cố định


**Q3. What does Learning rate mean? — Thuật ngữ Learning rate có nghĩa gì?**

A. It instead means Một lượt sử dụng hết dữ liệu train để cập nhật mô hình — Một lượt sử dụng hết dữ liệu train để cập nhật mô hình

B. It instead means Đạo hàm theo một biến khi các biến khác giữ cố định — Đạo hàm theo một biến khi các biến khác giữ cố định

C. It instead means Vector gồm các đạo hàm riêng của hàm nhiều biến — Vector gồm các đạo hàm riêng của hàm nhiều biến

D. It means Bước nhân gradient khi cập nhật tham số — Bước nhân gradient khi cập nhật tham số


**Q4. What does Epoch mean? — Thuật ngữ Epoch có nghĩa gì?**

A. It instead means Đạo hàm theo một biến khi các biến khác giữ cố định — Đạo hàm theo một biến khi các biến khác giữ cố định

B. It instead means Vector gồm các đạo hàm riêng của hàm nhiều biến — Vector gồm các đạo hàm riêng của hàm nhiều biến

C. It means Một lượt sử dụng hết dữ liệu train để cập nhật mô hình — Một lượt sử dụng hết dữ liệu train để cập nhật mô hình

D. It instead means Bước nhân gradient khi cập nhật tham số — Bước nhân gradient khi cập nhật tham số


**Q5. What does sympy.diff(f,x) do? — Mục đích của sympy.diff(f,x) là gì?**

A. Another operation does Ghép các đạo hàm riêng thành vector — Ghép các đạo hàm riêng thành vector

B. It is used to Đạo hàm riêng của hàm f theo x — Đạo hàm riêng của hàm f theo x

C. Another operation does Cập nhật đi ngược hướng tăng loss — Cập nhật đi ngược hướng tăng loss

D. Another operation does Loss MSE mẫu cho tối ưu hồi quy — Loss MSE mẫu cho tối ưu hồi quy


**Q6. What does grad=[df/dx,df/dy,...] do? — Mục đích của grad=[df/dx,df/dy,...] là gì?**

A. It is used to Ghép các đạo hàm riêng thành vector — Ghép các đạo hàm riêng thành vector

B. Another operation does Cập nhật đi ngược hướng tăng loss — Cập nhật đi ngược hướng tăng loss

C. Another operation does Loss MSE mẫu cho tối ưu hồi quy — Loss MSE mẫu cho tối ưu hồi quy

D. Another operation does Đạo hàm riêng của hàm f theo x — Đạo hàm riêng của hàm f theo x


**Q7. What does w = w - lr * gradient do? — Mục đích của w = w - lr * gradient là gì?**

A. Another operation does Loss MSE mẫu cho tối ưu hồi quy — Loss MSE mẫu cho tối ưu hồi quy

B. Another operation does Đạo hàm riêng của hàm f theo x — Đạo hàm riêng của hàm f theo x

C. Another operation does Ghép các đạo hàm riêng thành vector — Ghép các đạo hàm riêng thành vector

D. It is used to Cập nhật đi ngược hướng tăng loss — Cập nhật đi ngược hướng tăng loss


**Q8. What does np.mean((pred-y)**2) do? — Mục đích của np.mean((pred-y)**2) là gì?**

A. Another operation does Đạo hàm riêng của hàm f theo x — Đạo hàm riêng của hàm f theo x

B. Another operation does Ghép các đạo hàm riêng thành vector — Ghép các đạo hàm riêng thành vector

C. It is used to Loss MSE mẫu cho tối ưu hồi quy — Loss MSE mẫu cho tối ưu hồi quy

D. Another operation does Cập nhật đi ngược hướng tăng loss — Cập nhật đi ngược hướng tăng loss


**Q9. Why use this method in scenario 1? — Vì sao chọn cách giải ở tình huống 1?**

A. Hàm hai biến f=x²+3xy+y² cần đạo hàm từng biến — Hàm hai biến f=x²+3xy+y² cần đạo hàm từng biến

B. Cập nhật w theo độ dốc của hàm w² — Cập nhật w theo độ dốc của hàm w²

C. Lưu loss sau từng bước để xem có giảm — Lưu loss sau từng bước để xem có giảm

D. Learning rate quá cao có thể làm mất ổn định — Learning rate quá cao có thể làm mất ổn định


**Q10. Why use this method in scenario 2? — Vì sao chọn cách giải ở tình huống 2?**

A. Hàm hai biến f=x²+3xy+y² cần đạo hàm từng biến — Hàm hai biến f=x²+3xy+y² cần đạo hàm từng biến

B. Lưu loss sau từng bước để xem có giảm — Lưu loss sau từng bước để xem có giảm

C. Learning rate quá cao có thể làm mất ổn định — Learning rate quá cao có thể làm mất ổn định

D. Tính dMSE/dw rồi cập nhật hệ số hồi quy tuyến tính — Tính dMSE/dw rồi cập nhật hệ số hồi quy tuyến tính


**Q11. Why use this method in scenario 3? — Vì sao chọn cách giải ở tình huống 3?**

A. Learning rate quá cao có thể làm mất ổn định — Learning rate quá cao có thể làm mất ổn định

B. Tính dMSE/dw rồi cập nhật hệ số hồi quy tuyến tính — Tính dMSE/dw rồi cập nhật hệ số hồi quy tuyến tính

C. Cập nhật w theo độ dốc của hàm w² — Cập nhật w theo độ dốc của hàm w²

D. Lưu loss sau từng bước để xem có giảm — Lưu loss sau từng bước để xem có giảm


**Q12. Why use this method in scenario 4? — Vì sao chọn cách giải ở tình huống 4?**

A. Tính dMSE/dw rồi cập nhật hệ số hồi quy tuyến tính — Tính dMSE/dw rồi cập nhật hệ số hồi quy tuyến tính

B. Cập nhật w theo độ dốc của hàm w² — Cập nhật w theo độ dốc của hàm w²

C. Learning rate quá cao có thể làm mất ổn định — Learning rate quá cao có thể làm mất ổn định

D. Hàm hai biến f=x²+3xy+y² cần đạo hàm từng biến — Hàm hai biến f=x²+3xy+y² cần đạo hàm từng biến


**Q13. Why use this method in scenario 5? — Vì sao chọn cách giải ở tình huống 5?**

A. Cập nhật w theo độ dốc của hàm w² — Cập nhật w theo độ dốc của hàm w²

B. Tính dMSE/dw rồi cập nhật hệ số hồi quy tuyến tính — Tính dMSE/dw rồi cập nhật hệ số hồi quy tuyến tính

C. Hàm hai biến f=x²+3xy+y² cần đạo hàm từng biến — Hàm hai biến f=x²+3xy+y² cần đạo hàm từng biến

D. Lưu loss sau từng bước để xem có giảm — Lưu loss sau từng bước để xem có giảm


**Q14. Which input belongs to scenario 1? — Tình huống 1 sử dụng dữ liệu gì?**

A. The input is Bắt đầu w=4, lr=0.1, 10 bước — Bắt đầu w=4, lr=0.1, 10 bước

B. Another input is Hàm tại x=1,y=2 — Hàm tại x=1,y=2

C. Another input is Hàm loss w² với w=3 — Hàm loss w² với w=3

D. Another input is w=4, lr 0.1 và 1.1 — w=4, lr 0.1 và 1.1


**Q15. Which input belongs to scenario 2? — Tình huống 2 sử dụng dữ liệu gì?**

A. Another input is Hàm loss w² với w=3 — Hàm loss w² với w=3

B. Another input is w=4, lr 0.1 và 1.1 — w=4, lr 0.1 và 1.1

C. Another input is X=[1,2,3], y=[2,4,6], 100 bước — X=[1,2,3], y=[2,4,6], 100 bước

D. The input is Hàm tại x=1,y=2 — Hàm tại x=1,y=2


**Q16. Which input belongs to scenario 3? — Tình huống 3 sử dụng dữ liệu gì?**

A. Another input is w=4, lr 0.1 và 1.1 — w=4, lr 0.1 và 1.1

B. Another input is X=[1,2,3], y=[2,4,6], 100 bước — X=[1,2,3], y=[2,4,6], 100 bước

C. The input is Hàm loss w² với w=3 — Hàm loss w² với w=3

D. Another input is Bắt đầu w=4, lr=0.1, 10 bước — Bắt đầu w=4, lr=0.1, 10 bước


**Q17. Which input belongs to scenario 4? — Tình huống 4 sử dụng dữ liệu gì?**

A. Another input is X=[1,2,3], y=[2,4,6], 100 bước — X=[1,2,3], y=[2,4,6], 100 bước

B. The input is w=4, lr 0.1 và 1.1 — w=4, lr 0.1 và 1.1

C. Another input is Bắt đầu w=4, lr=0.1, 10 bước — Bắt đầu w=4, lr=0.1, 10 bước

D. Another input is Hàm tại x=1,y=2 — Hàm tại x=1,y=2


**Q18. Which input belongs to scenario 5? — Tình huống 5 sử dụng dữ liệu gì?**

A. The input is X=[1,2,3], y=[2,4,6], 100 bước — X=[1,2,3], y=[2,4,6], 100 bước

B. Another input is Bắt đầu w=4, lr=0.1, 10 bước — Bắt đầu w=4, lr=0.1, 10 bước

C. Another input is Hàm tại x=1,y=2 — Hàm tại x=1,y=2

D. Another input is Hàm loss w² với w=3 — Hàm loss w² với w=3


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
| Q1 | **B** | It means Đạo hàm theo một biến khi các biến khác giữ cố định | Đạo hàm theo một biến khi các biến khác giữ cố định |
| Q2 | **A** | It means Vector gồm các đạo hàm riêng của hàm nhiều biến | Vector gồm các đạo hàm riêng của hàm nhiều biến |
| Q3 | **D** | It means Bước nhân gradient khi cập nhật tham số | Bước nhân gradient khi cập nhật tham số |
| Q4 | **C** | It means Một lượt sử dụng hết dữ liệu train để cập nhật mô hình | Một lượt sử dụng hết dữ liệu train để cập nhật mô hình |
| Q5 | **B** | It is used to Đạo hàm riêng của hàm f theo x | Đạo hàm riêng của hàm f theo x |
| Q6 | **A** | It is used to Ghép các đạo hàm riêng thành vector | Ghép các đạo hàm riêng thành vector |
| Q7 | **D** | It is used to Cập nhật đi ngược hướng tăng loss | Cập nhật đi ngược hướng tăng loss |
| Q8 | **C** | It is used to Loss MSE mẫu cho tối ưu hồi quy | Loss MSE mẫu cho tối ưu hồi quy |
| Q9 | **B** | Cập nhật w theo độ dốc của hàm w² | Cập nhật w theo độ dốc của hàm w² |
| Q10 | **A** | Hàm hai biến f=x²+3xy+y² cần đạo hàm từng biến | Hàm hai biến f=x²+3xy+y² cần đạo hàm từng biến |
| Q11 | **D** | Lưu loss sau từng bước để xem có giảm | Lưu loss sau từng bước để xem có giảm |
| Q12 | **C** | Learning rate quá cao có thể làm mất ổn định | Learning rate quá cao có thể làm mất ổn định |
| Q13 | **B** | Tính dMSE/dw rồi cập nhật hệ số hồi quy tuyến tính | Tính dMSE/dw rồi cập nhật hệ số hồi quy tuyến tính |
| Q14 | **A** | The input is Bắt đầu w=4, lr=0.1, 10 bước | Bắt đầu w=4, lr=0.1, 10 bước |
| Q15 | **D** | The input is Hàm tại x=1,y=2 | Hàm tại x=1,y=2 |
| Q16 | **C** | The input is Hàm loss w² với w=3 | Hàm loss w² với w=3 |
| Q17 | **B** | The input is w=4, lr 0.1 và 1.1 | w=4, lr 0.1 và 1.1 |
| Q18 | **A** | The input is X=[1,2,3], y=[2,4,6], 100 bước | X=[1,2,3], y=[2,4,6], 100 bước |
| Q19 | **D** | Input meaning and units | Ý nghĩa và đơn vị đầu vào |
| Q20 | **C** | Verify results and edge cases | Kiểm tra kết quả và trường hợp biên |

## 8. Bài tiếp theo

`Derivative → Gradient → Optimization → Training`.

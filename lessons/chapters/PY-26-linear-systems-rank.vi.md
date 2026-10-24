# PY-26 — Hệ phương trình tuyến tính, rank và nghiệm


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Linear system** — hệ tuyến tính; **Rank** — hạng ma trận.

`Ma trận → Rank/Solve → Regression → AI`

Nắm liên hệ giữa cấu trúc toán học và mảng dữ liệu Python trước khi sử dụng vào học máy.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Giải thích |
|---|---|---|
| Linear system | hệ tuyến tính | Nhiều phương trình chứa cùng các ẩn số |
| Rank | hạng ma trận | Số hàng/cột độc lập tuyến tính |
| Coefficient matrix | ma trận hệ số | Các hệ số của ẩn trong Ax=b |
| Residual | sai số dư | Độ sai khác giữa dự đoán Ax và b |

## 3. NumPy và các hàm liên quan

**Từ vựng trong mục:** **Function** — hàm; **Shape** — kích thước mảng.

| Hàm / tham số | Dùng làm gì |
|---|---|
| `np.linalg.solve(A,b)` | Giải Ax=b khi ma trận A vuông không suy biến |
| `np.linalg.matrix_rank(A)` | Kiểm tra số chiều độc lập tuyến tính |
| `np.column_stack((A,b))` | Ghép ma trận hệ số và vế phải thành augmented matrix |
| `np.linalg.lstsq(A,b,rcond=None)` | Tìm nghiệm bình phương tối thiểu khi quá nhiều phương trình |

## 4. Khái niệm kèm ví dụ nhỏ

### 4.1. Linear system

**Từ vựng trong mục:** **Linear system** — hệ tuyến tính.

Nhiều phương trình chứa cùng các ẩn số. Trước khi sử dụng biểu thức hãy xem phần tử, hàng/cột và đơn vị đầu vào.

```python
import numpy as np
print(np.linalg.solve([[1,1],[2,1]],[5,8]))
```

**Tự kiểm tra:** Linear system có nghĩa gì? **Đáp án:** Nhiều phương trình chứa cùng các ẩn số.

### 4.2. Rank

**Từ vựng trong mục:** **Rank** — hạng ma trận.

Số hàng/cột độc lập tuyến tính. Trước khi sử dụng biểu thức hãy xem phần tử, hàng/cột và đơn vị đầu vào.

```python
import numpy as np
print(np.linalg.matrix_rank([[1,2],[2,4]]))
```

**Tự kiểm tra:** Rank có nghĩa gì? **Đáp án:** Số hàng/cột độc lập tuyến tính.

### 4.3. Coefficient matrix

**Từ vựng trong mục:** **Coefficient matrix** — ma trận hệ số.

Các hệ số của ẩn trong Ax=b. Trước khi sử dụng biểu thức hãy xem phần tử, hàng/cột và đơn vị đầu vào.

```python
import numpy as np
print(np.array([[1,1],[2,1]]))
```

**Tự kiểm tra:** Coefficient matrix có nghĩa gì? **Đáp án:** Các hệ số của ẩn trong Ax=b.

### 4.4. Residual

**Từ vựng trong mục:** **Residual** — sai số dư.

Độ sai khác giữa dự đoán Ax và b. Trước khi sử dụng biểu thức hãy xem phần tử, hàng/cột và đơn vị đầu vào.

```python
import numpy as np
A=np.eye(2);x=np.array([2,3]);b=np.array([2,3]);print(A@x-b)
```

**Tự kiểm tra:** Residual có nghĩa gì? **Đáp án:** Độ sai khác giữa dự đoán Ax và b.

## 5. Năm tình huống ứng dụng

### Tình huống 1 — Tính giá hai loại hàng

**Từ vựng trong mục:** **Linear system** — hệ tuyến tính.

**Vấn đề:** Tính giá hai loại hàng.

**Vì sao chọn phương án?** Solve tìm giá mỗi loại từ hai hóa đơn độc lập; điều kiện tiên quyết là dữ liệu có shape và ý nghĩa từng giá trị rõ ràng.

**Dữ liệu:** x+y=5, 2x+y=8 (nghìn đồng). Mỗi hàng là một đối tượng, mỗi cột là feature trong bài toán (nếu đầu vào là ma trận). Những con số ở đây là minh họa, không phải kết luận thực tế.

**Quy trình:** mô tả dữ liệu → xác định phép tính/shape → tính bằng Python → kiểm tra kết quả.

```python
import numpy as np
A=np.array([[1,1],[2,1]],dtype=float);b=np.array([5,8])
print(np.linalg.solve(A,b))
```

**Đọc kết quả:** Chú ý kích thước và đơn vị kết quả, thử thêm ca biên nếu đưa vào ứng dụng thực tế.

### Tình huống 2 — Xem cột dữ liệu trùng

**Từ vựng trong mục:** **Rank** — hạng ma trận.

**Vấn đề:** Xem cột dữ liệu trùng.

**Vì sao chọn phương án?** Rank thấp phát hiện một feature tuyến tính phụ thuộc feature khác; điều kiện tiên quyết là dữ liệu có shape và ý nghĩa từng giá trị rõ ràng.

**Dữ liệu:** Ma trận [1,2];[2,4]. Mỗi hàng là một đối tượng, mỗi cột là feature trong bài toán (nếu đầu vào là ma trận). Những con số ở đây là minh họa, không phải kết luận thực tế.

**Quy trình:** mô tả dữ liệu → xác định phép tính/shape → tính bằng Python → kiểm tra kết quả.

```python
import numpy as np
A=np.array([[1,2],[2,4]])
print(np.linalg.matrix_rank(A))
```

**Đọc kết quả:** Chú ý kích thước và đơn vị kết quả, thử thêm ca biên nếu đưa vào ứng dụng thực tế.

### Tình huống 3 — Kiểm chứng nghiệm

**Từ vựng trong mục:** **Coefficient matrix** — ma trận hệ số.

**Vấn đề:** Kiểm chứng nghiệm.

**Vì sao chọn phương án?** Nhân A@x rồi so b để phát hiện sai phép giải; điều kiện tiên quyết là dữ liệu có shape và ý nghĩa từng giá trị rõ ràng.

**Dữ liệu:** Hệ x+y=5, 2x+y=8. Mỗi hàng là một đối tượng, mỗi cột là feature trong bài toán (nếu đầu vào là ma trận). Những con số ở đây là minh họa, không phải kết luận thực tế.

**Quy trình:** mô tả dữ liệu → xác định phép tính/shape → tính bằng Python → kiểm tra kết quả.

```python
import numpy as np
A=np.array([[1,1],[2,1]]);b=np.array([5,8]);x=np.array([3,2])
print(np.allclose(A@x,b))
```

**Đọc kết quả:** Chú ý kích thước và đơn vị kết quả, thử thêm ca biên nếu đưa vào ứng dụng thực tế.

### Tình huống 4 — Ước lượng từ số đo nhiễu

**Từ vựng trong mục:** **Residual** — sai số dư.

**Vấn đề:** Ước lượng từ số đo nhiễu.

**Vì sao chọn phương án?** lstsq phù hợp khi số phương trình lớn hơn số ẩn; điều kiện tiên quyết là dữ liệu có shape và ý nghĩa từng giá trị rõ ràng.

**Dữ liệu:** Ba điểm để fit đường y=ax+b. Mỗi hàng là một đối tượng, mỗi cột là feature trong bài toán (nếu đầu vào là ma trận). Những con số ở đây là minh họa, không phải kết luận thực tế.

**Quy trình:** mô tả dữ liệu → xác định phép tính/shape → tính bằng Python → kiểm tra kết quả.

```python
import numpy as np
x=np.array([1,2,3]);y=np.array([2,4,6])
A=np.column_stack([x,np.ones_like(x)])
print(np.linalg.lstsq(A,y,rcond=None)[0])
```

**Đọc kết quả:** Chú ý kích thước và đơn vị kết quả, thử thêm ca biên nếu đưa vào ứng dụng thực tế.

### Tình huống 5 — Tìm sai số dư

**Từ vựng trong mục:** **Linear system** — hệ tuyến tính.

**Vấn đề:** Tìm sai số dư.

**Vì sao chọn phương án?** Residual cho biết hệ có tái tạo đúng mục tiêu không; điều kiện tiên quyết là dữ liệu có shape và ý nghĩa từng giá trị rõ ràng.

**Dữ liệu:** A=I, x=[2,3], b=[2,4]. Mỗi hàng là một đối tượng, mỗi cột là feature trong bài toán (nếu đầu vào là ma trận). Những con số ở đây là minh họa, không phải kết luận thực tế.

**Quy trình:** mô tả dữ liệu → xác định phép tính/shape → tính bằng Python → kiểm tra kết quả.

```python
import numpy as np
A=np.eye(2);x=np.array([2,3]);b=np.array([2,4])
print(A@x-b)
```

**Đọc kết quả:** Chú ý kích thước và đơn vị kết quả, thử thêm ca biên nếu đưa vào ứng dụng thực tế.

## 6. Sai lầm cần tránh

Phân biệt vector một chiều với ma trận hai chiều, tránh nhân ma trận sai shape; covariance và eigenvalue không phải độ chính xác mô hình. Các ví dụ số không có ý nghĩa dự đoán nếu thiếu bước đánh giá.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.


**Q1. What is Linear system? — Thuật ngữ Linear system có nghĩa gì?**

A. It instead means Số hàng/cột độc lập tuyến tính — Số hàng/cột độc lập tuyến tính

B. It means Nhiều phương trình chứa cùng các ẩn số — Nhiều phương trình chứa cùng các ẩn số

C. It instead means Các hệ số của ẩn trong Ax=b — Các hệ số của ẩn trong Ax=b

D. It instead means Độ sai khác giữa dự đoán Ax và b — Độ sai khác giữa dự đoán Ax và b


**Q2. What is Rank? — Thuật ngữ Rank có nghĩa gì?**

A. It means Số hàng/cột độc lập tuyến tính — Số hàng/cột độc lập tuyến tính

B. It instead means Các hệ số của ẩn trong Ax=b — Các hệ số của ẩn trong Ax=b

C. It instead means Độ sai khác giữa dự đoán Ax và b — Độ sai khác giữa dự đoán Ax và b

D. It instead means Nhiều phương trình chứa cùng các ẩn số — Nhiều phương trình chứa cùng các ẩn số


**Q3. What is Coefficient matrix? — Thuật ngữ Coefficient matrix có nghĩa gì?**

A. It instead means Độ sai khác giữa dự đoán Ax và b — Độ sai khác giữa dự đoán Ax và b

B. It instead means Nhiều phương trình chứa cùng các ẩn số — Nhiều phương trình chứa cùng các ẩn số

C. It instead means Số hàng/cột độc lập tuyến tính — Số hàng/cột độc lập tuyến tính

D. It means Các hệ số của ẩn trong Ax=b — Các hệ số của ẩn trong Ax=b


**Q4. What is Residual? — Thuật ngữ Residual có nghĩa gì?**

A. It instead means Nhiều phương trình chứa cùng các ẩn số — Nhiều phương trình chứa cùng các ẩn số

B. It instead means Số hàng/cột độc lập tuyến tính — Số hàng/cột độc lập tuyến tính

C. It means Độ sai khác giữa dự đoán Ax và b — Độ sai khác giữa dự đoán Ax và b

D. It instead means Các hệ số của ẩn trong Ax=b — Các hệ số của ẩn trong Ax=b


**Q5. What does np.linalg.solve(A,b) help with? — Hàm np.linalg.solve(A,b) giúp làm gì?**

A. Another function helps to Kiểm tra số chiều độc lập tuyến tính — Kiểm tra số chiều độc lập tuyến tính

B. It helps to Giải Ax=b khi ma trận A vuông không suy biến — Giải Ax=b khi ma trận A vuông không suy biến

C. Another function helps to Ghép ma trận hệ số và vế phải thành augmented matrix — Ghép ma trận hệ số và vế phải thành augmented matrix

D. Another function helps to Tìm nghiệm bình phương tối thiểu khi quá nhiều phương trình — Tìm nghiệm bình phương tối thiểu khi quá nhiều phương trình


**Q6. What does np.linalg.matrix_rank(A) help with? — Hàm np.linalg.matrix_rank(A) giúp làm gì?**

A. It helps to Kiểm tra số chiều độc lập tuyến tính — Kiểm tra số chiều độc lập tuyến tính

B. Another function helps to Ghép ma trận hệ số và vế phải thành augmented matrix — Ghép ma trận hệ số và vế phải thành augmented matrix

C. Another function helps to Tìm nghiệm bình phương tối thiểu khi quá nhiều phương trình — Tìm nghiệm bình phương tối thiểu khi quá nhiều phương trình

D. Another function helps to Giải Ax=b khi ma trận A vuông không suy biến — Giải Ax=b khi ma trận A vuông không suy biến


**Q7. What does np.column_stack((A,b)) help with? — Hàm np.column_stack((A,b)) giúp làm gì?**

A. Another function helps to Tìm nghiệm bình phương tối thiểu khi quá nhiều phương trình — Tìm nghiệm bình phương tối thiểu khi quá nhiều phương trình

B. Another function helps to Giải Ax=b khi ma trận A vuông không suy biến — Giải Ax=b khi ma trận A vuông không suy biến

C. Another function helps to Kiểm tra số chiều độc lập tuyến tính — Kiểm tra số chiều độc lập tuyến tính

D. It helps to Ghép ma trận hệ số và vế phải thành augmented matrix — Ghép ma trận hệ số và vế phải thành augmented matrix


**Q8. What does np.linalg.lstsq(A,b,rcond=None) help with? — Hàm np.linalg.lstsq(A,b,rcond=None) giúp làm gì?**

A. Another function helps to Giải Ax=b khi ma trận A vuông không suy biến — Giải Ax=b khi ma trận A vuông không suy biến

B. Another function helps to Kiểm tra số chiều độc lập tuyến tính — Kiểm tra số chiều độc lập tuyến tính

C. It helps to Tìm nghiệm bình phương tối thiểu khi quá nhiều phương trình — Tìm nghiệm bình phương tối thiểu khi quá nhiều phương trình

D. Another function helps to Ghép ma trận hệ số và vế phải thành augmented matrix — Ghép ma trận hệ số và vế phải thành augmented matrix


**Q9. Why choose this method for scenario 1? — Vì sao chọn cách làm tình huống 1?**

A. Rank thấp phát hiện một feature tuyến tính phụ thuộc feature khác — Rank thấp phát hiện một feature tuyến tính phụ thuộc feature khác

B. Solve tìm giá mỗi loại từ hai hóa đơn độc lập — Solve tìm giá mỗi loại từ hai hóa đơn độc lập

C. Nhân A@x rồi so b để phát hiện sai phép giải — Nhân A@x rồi so b để phát hiện sai phép giải

D. lstsq phù hợp khi số phương trình lớn hơn số ẩn — lstsq phù hợp khi số phương trình lớn hơn số ẩn


**Q10. Why choose this method for scenario 2? — Vì sao chọn cách làm tình huống 2?**

A. Rank thấp phát hiện một feature tuyến tính phụ thuộc feature khác — Rank thấp phát hiện một feature tuyến tính phụ thuộc feature khác

B. Nhân A@x rồi so b để phát hiện sai phép giải — Nhân A@x rồi so b để phát hiện sai phép giải

C. lstsq phù hợp khi số phương trình lớn hơn số ẩn — lstsq phù hợp khi số phương trình lớn hơn số ẩn

D. Residual cho biết hệ có tái tạo đúng mục tiêu không — Residual cho biết hệ có tái tạo đúng mục tiêu không


**Q11. Why choose this method for scenario 3? — Vì sao chọn cách làm tình huống 3?**

A. lstsq phù hợp khi số phương trình lớn hơn số ẩn — lstsq phù hợp khi số phương trình lớn hơn số ẩn

B. Residual cho biết hệ có tái tạo đúng mục tiêu không — Residual cho biết hệ có tái tạo đúng mục tiêu không

C. Solve tìm giá mỗi loại từ hai hóa đơn độc lập — Solve tìm giá mỗi loại từ hai hóa đơn độc lập

D. Nhân A@x rồi so b để phát hiện sai phép giải — Nhân A@x rồi so b để phát hiện sai phép giải


**Q12. Why choose this method for scenario 4? — Vì sao chọn cách làm tình huống 4?**

A. Residual cho biết hệ có tái tạo đúng mục tiêu không — Residual cho biết hệ có tái tạo đúng mục tiêu không

B. Solve tìm giá mỗi loại từ hai hóa đơn độc lập — Solve tìm giá mỗi loại từ hai hóa đơn độc lập

C. lstsq phù hợp khi số phương trình lớn hơn số ẩn — lstsq phù hợp khi số phương trình lớn hơn số ẩn

D. Rank thấp phát hiện một feature tuyến tính phụ thuộc feature khác — Rank thấp phát hiện một feature tuyến tính phụ thuộc feature khác


**Q13. Why choose this method for scenario 5? — Vì sao chọn cách làm tình huống 5?**

A. Solve tìm giá mỗi loại từ hai hóa đơn độc lập — Solve tìm giá mỗi loại từ hai hóa đơn độc lập

B. Residual cho biết hệ có tái tạo đúng mục tiêu không — Residual cho biết hệ có tái tạo đúng mục tiêu không

C. Rank thấp phát hiện một feature tuyến tính phụ thuộc feature khác — Rank thấp phát hiện một feature tuyến tính phụ thuộc feature khác

D. Nhân A@x rồi so b để phát hiện sai phép giải — Nhân A@x rồi so b để phát hiện sai phép giải


**Q14. What input is relevant to scenario 1? — Dữ liệu nào của tình huống 1?**

A. The input is x+y=5, 2x+y=8 (nghìn đồng) — x+y=5, 2x+y=8 (nghìn đồng)

B. Different data: Ma trận [1,2];[2,4] — Ma trận [1,2];[2,4]

C. Different data: Hệ x+y=5, 2x+y=8 — Hệ x+y=5, 2x+y=8

D. Different data: Ba điểm để fit đường y=ax+b — Ba điểm để fit đường y=ax+b


**Q15. What input is relevant to scenario 2? — Dữ liệu nào của tình huống 2?**

A. Different data: Hệ x+y=5, 2x+y=8 — Hệ x+y=5, 2x+y=8

B. Different data: Ba điểm để fit đường y=ax+b — Ba điểm để fit đường y=ax+b

C. Different data: A=I, x=[2,3], b=[2,4] — A=I, x=[2,3], b=[2,4]

D. The input is Ma trận [1,2];[2,4] — Ma trận [1,2];[2,4]


**Q16. What input is relevant to scenario 3? — Dữ liệu nào của tình huống 3?**

A. Different data: Ba điểm để fit đường y=ax+b — Ba điểm để fit đường y=ax+b

B. Different data: A=I, x=[2,3], b=[2,4] — A=I, x=[2,3], b=[2,4]

C. The input is Hệ x+y=5, 2x+y=8 — Hệ x+y=5, 2x+y=8

D. Different data: x+y=5, 2x+y=8 (nghìn đồng) — x+y=5, 2x+y=8 (nghìn đồng)


**Q17. What input is relevant to scenario 4? — Dữ liệu nào của tình huống 4?**

A. Different data: A=I, x=[2,3], b=[2,4] — A=I, x=[2,3], b=[2,4]

B. The input is Ba điểm để fit đường y=ax+b — Ba điểm để fit đường y=ax+b

C. Different data: x+y=5, 2x+y=8 (nghìn đồng) — x+y=5, 2x+y=8 (nghìn đồng)

D. Different data: Ma trận [1,2];[2,4] — Ma trận [1,2];[2,4]


**Q18. What input is relevant to scenario 5? — Dữ liệu nào của tình huống 5?**

A. The input is A=I, x=[2,3], b=[2,4] — A=I, x=[2,3], b=[2,4]

B. Different data: x+y=5, 2x+y=8 (nghìn đồng) — x+y=5, 2x+y=8 (nghìn đồng)

C. Different data: Ma trận [1,2];[2,4] — Ma trận [1,2];[2,4]

D. Different data: Hệ x+y=5, 2x+y=8 — Hệ x+y=5, 2x+y=8


**Q19. What should be checked for matrix operations? — Phép toán ma trận phải kiểm tra gì?**

A. Only line spacing — Chỉ khoảng cách dòng

B. Only file suffix — Chỉ phần mở rộng file

C. Only terminal width — Chỉ độ rộng terminal

D. Shapes and data units — Shape và đơn vị dữ liệu


**Q20. Why is one numeric example not enough for AI? — Vì sao một ví dụ số chưa đủ đánh giá AI?**

A. It always proves generalization — Nó luôn chứng minh khả năng tổng quát

B. It removes the need for test data — Nó bỏ được tập kiểm tra

C. It does not establish predictive performance — Nó không đo chất lượng dự đoán

D. It guarantees no leakage — Nó bảo đảm không rò rỉ dữ liệu

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **B** | It means Nhiều phương trình chứa cùng các ẩn số | Nhiều phương trình chứa cùng các ẩn số |
| Q2 | **A** | It means Số hàng/cột độc lập tuyến tính | Số hàng/cột độc lập tuyến tính |
| Q3 | **D** | It means Các hệ số của ẩn trong Ax=b | Các hệ số của ẩn trong Ax=b |
| Q4 | **C** | It means Độ sai khác giữa dự đoán Ax và b | Độ sai khác giữa dự đoán Ax và b |
| Q5 | **B** | It helps to Giải Ax=b khi ma trận A vuông không suy biến | Giải Ax=b khi ma trận A vuông không suy biến |
| Q6 | **A** | It helps to Kiểm tra số chiều độc lập tuyến tính | Kiểm tra số chiều độc lập tuyến tính |
| Q7 | **D** | It helps to Ghép ma trận hệ số và vế phải thành augmented matrix | Ghép ma trận hệ số và vế phải thành augmented matrix |
| Q8 | **C** | It helps to Tìm nghiệm bình phương tối thiểu khi quá nhiều phương trình | Tìm nghiệm bình phương tối thiểu khi quá nhiều phương trình |
| Q9 | **B** | Solve tìm giá mỗi loại từ hai hóa đơn độc lập | Solve tìm giá mỗi loại từ hai hóa đơn độc lập |
| Q10 | **A** | Rank thấp phát hiện một feature tuyến tính phụ thuộc feature khác | Rank thấp phát hiện một feature tuyến tính phụ thuộc feature khác |
| Q11 | **D** | Nhân A@x rồi so b để phát hiện sai phép giải | Nhân A@x rồi so b để phát hiện sai phép giải |
| Q12 | **C** | lstsq phù hợp khi số phương trình lớn hơn số ẩn | lstsq phù hợp khi số phương trình lớn hơn số ẩn |
| Q13 | **B** | Residual cho biết hệ có tái tạo đúng mục tiêu không | Residual cho biết hệ có tái tạo đúng mục tiêu không |
| Q14 | **A** | The input is x+y=5, 2x+y=8 (nghìn đồng) | x+y=5, 2x+y=8 (nghìn đồng) |
| Q15 | **D** | The input is Ma trận [1,2];[2,4] | Ma trận [1,2];[2,4] |
| Q16 | **C** | The input is Hệ x+y=5, 2x+y=8 | Hệ x+y=5, 2x+y=8 |
| Q17 | **B** | The input is Ba điểm để fit đường y=ax+b | Ba điểm để fit đường y=ax+b |
| Q18 | **A** | The input is A=I, x=[2,3], b=[2,4] | A=I, x=[2,3], b=[2,4] |
| Q19 | **D** | Shapes and data units | Shape và đơn vị dữ liệu |
| Q20 | **C** | It does not establish predictive performance | Nó không đo chất lượng dự đoán |

## 8. Nối sang bài kế tiếp

`Ma trận → Rank/Solve → Regression → AI`.

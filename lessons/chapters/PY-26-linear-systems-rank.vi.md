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

## 4. Khái niệm liên quan

### 4.1. Linear system

**Từ vựng trong mục:** **Linear system** — hệ tuyến tính.

Một **hệ phương trình tuyến tính** gồm nhiều phương trình bậc nhất dùng chung các ẩn cần tìm. Ví dụ, cửa hàng chưa biết giá hai sản phẩm là `x` và `y` (nghìn đồng). Mua mỗi loại một món hết 5 nghìn đồng nên `x + y = 5`; mua hai món loại thứ nhất và một món loại thứ hai hết 8 nghìn đồng nên `2x + y = 8`. Hai phương trình phải cùng đúng. Viết gọn thành `A @ [x, y] = b`, với `A = [[1, 1], [2, 1]]` và `b = [5, 8]`. **Mỗi hàng của A là một giao dịch/phương trình; mỗi cột tương ứng số lượng sản phẩm x hoặc y; mỗi phần tử là hệ số của ẩn tương ứng.** Mảng `b` chứa tổng tiền từng giao dịch theo nghìn đồng. Hàm `solve()` tìm được `x=3` và `y=2` nghìn đồng.

```python
import numpy as np
print(np.linalg.solve([[1,1],[2,1]],[5,8]))
```

**Kết quả khi chạy:**

```text
[3. 2.]
```

### 4.2. Rank

**Từ vựng trong mục:** **Rank** — hạng ma trận.

**Rank (hạng ma trận)** là số hàng hoặc cột độc lập tuyến tính tối đa: không thể tạo một hàng độc lập bằng cách nhân/cộng các hàng còn lại. Chẳng hạn `[[1, 2], [2, 4]]` có hàng thứ hai bằng hai lần hàng đầu, nên chỉ cung cấp một thông tin độc lập và có rank bằng `1`, không phải `2`. Với hệ hai ẩn, thiếu phương trình độc lập có thể khiến ta không xác định được một nghiệm duy nhất. Trong ví dụ giá hàng ở mục 4.1, hai hàng `[1, 1]` và `[2, 1]` không là bội của nhau nên đủ hai điều kiện độc lập.

```python
import numpy as np
print(np.linalg.matrix_rank([[1,2],[2,4]]))
```

**Kết quả khi chạy:**

```text
1
```

### 4.3. Coefficient matrix

**Từ vựng trong mục:** **Coefficient matrix** — ma trận hệ số.

**Ma trận hệ số** gom các hệ số đứng trước các ẩn vào một bảng số. Ở bài toán giá hai sản phẩm, `A = [[1, 1], [2, 1]]` có kích thước `2 × 2`: **hàng 0** ứng với giao dịch một món mỗi loại, **hàng 1** ứng với giao dịch hai món loại x và một món loại y; **cột 0** là số lượng loại x, **cột 1** là số lượng loại y. Vector ẩn `[x, y]` có hai phần tử là giá mỗi loại, đơn vị nghìn đồng; vector vế phải `[5, 8]` là tổng tiền hai giao dịch. Phép nhân `A @ [x, y]` tái tạo hai tổng tiền.

```python
import numpy as np
print(np.array([[1,1],[2,1]]))
```

**Kết quả khi chạy:**

```text
[[1 1]
 [2 1]]
```

### 4.4. Residual

**Từ vựng trong mục:** **Residual** — sai số dư.

**Residual (sai số dư)** là hiệu giữa giá trị tính từ nghiệm và giá trị quan sát: `r = A @ x - b`. Nếu mọi phương trình được thỏa đúng thì residual bằng 0 (hoặc gần 0 do sai số tính toán). Ví dụ đơn giản trong code dưới dùng ma trận đơn vị `A = [[1, 0], [0, 1]]`, nghiệm thử `[2, 3]` và vế phải `[2, 3]`, nên residual là `[0, 0]`. Trong bài toán giá hàng ở trên, khi `x=3`, `y=2` thì hai tổng tiền tính lại là `[5, 8]`, sai số dư cũng bằng 0.

```python
import numpy as np
A=np.eye(2)
x=np.array([2,3])
b=np.array([2,3])
print(A@x-b)
```

**Kết quả khi chạy:**

```text
[0. 0.]
```

## 5. Năm tình huống ứng dụng

### Tình huống 1 — Tính giá hai loại hàng

**Từ vựng trong mục:** **Linear system** — hệ tuyến tính.

**Tình huống thực tế:** Cửa hàng bán hai loại sản phẩm: mua mỗi loại một món hết 5 đơn vị tiền, mua hai món loại đầu và một món loại sau hết 8. Tìm giá từng loại.

**Vì sao chọn phương án?** Solve tìm giá mỗi loại từ hai hóa đơn độc lập; điều kiện tiên quyết là dữ liệu có shape và ý nghĩa từng giá trị rõ ràng.


**Quy trình giải:** Lưu đầu vào đã nêu, dùng công thức hoặc hàm trong code rồi đối chiếu kết quả in ra.

```python
import numpy as np
A=np.array([[1,1],[2,1]],dtype=float)
b=np.array([5,8])
print(np.linalg.solve(A,b))
```

**Kết quả khi chạy:**

```text
[3. 2.]
```


### Tình huống 2 — Xem cột dữ liệu trùng

**Từ vựng trong mục:** **Rank** — hạng ma trận.

**Tình huống thực tế:** Bảng hai cột dữ liệu có hàng [1,2] và [2,4]; cột thứ hai gấp đôi cột đầu. Kiểm tra rank để nhận biết phụ thuộc.

**Vì sao chọn phương án?** Rank thấp phát hiện một feature tuyến tính phụ thuộc feature khác; điều kiện tiên quyết là dữ liệu có shape và ý nghĩa từng giá trị rõ ràng.


**Quy trình giải:** Lưu đầu vào đã nêu, dùng công thức hoặc hàm trong code rồi đối chiếu kết quả in ra.

```python
import numpy as np
A=np.array([[1,2],[2,4]])
print(np.linalg.matrix_rank(A))
```

**Kết quả khi chạy:**

```text
1
```


### Tình huống 3 — Kiểm chứng nghiệm

**Từ vựng trong mục:** **Coefficient matrix** — ma trận hệ số.

**Tình huống thực tế:** Một hệ có ma trận [[1,1],[2,1]] và kết quả [5,8]. Xác nhận nghiệm [3,2] có thỏa cả hai phương trình.

**Vì sao chọn phương án?** Nhân A@x rồi so b để phát hiện sai phép giải; điều kiện tiên quyết là dữ liệu có shape và ý nghĩa từng giá trị rõ ràng.


**Quy trình giải:** Lưu đầu vào đã nêu, dùng công thức hoặc hàm trong code rồi đối chiếu kết quả in ra.

```python
import numpy as np
A=np.array([[1,1],[2,1]])
b=np.array([5,8])
x=np.array([3,2])
print(np.allclose(A@x,b))
```

**Kết quả khi chạy:**

```text
True
```


### Tình huống 4 — Ước lượng từ số đo nhiễu

**Từ vựng trong mục:** **Residual** — sai số dư.

**Tình huống thực tế:** Ba số đo x=[1,2,3] và y=[2,4,6] có quan hệ gần tuyến tính. Dùng bình phương tối thiểu tìm hệ số góc và hệ số chặn.

**Vì sao chọn phương án?** lstsq phù hợp khi số phương trình lớn hơn số ẩn; điều kiện tiên quyết là dữ liệu có shape và ý nghĩa từng giá trị rõ ràng.


**Quy trình giải:** Lưu đầu vào đã nêu, dùng công thức hoặc hàm trong code rồi đối chiếu kết quả in ra.

```python
import numpy as np
x=np.array([1,2,3])
y=np.array([2,4,6])
A=np.column_stack([x,np.ones_like(x)])
print(np.linalg.lstsq(A,y,rcond=None)[0])
```

**Kết quả khi chạy (tham khảo):**

```text
[2.00000000e+00 2.32610211e-15]
```

*Hệ số thứ hai rất gần 0; các chữ số cuối có thể thay đổi theo phiên bản NumPy và môi trường tính toán.*


### Tình huống 5 — Tìm sai số dư

**Từ vựng trong mục:** **Linear system** — hệ tuyến tính.

**Tình huống thực tế:** Một mô hình dự báo vector [2,3] nhưng giá trị thật là [2,4]. Tính vector sai số dự báo trừ thực tế.

**Vì sao chọn phương án?** Residual cho biết hệ có tái tạo đúng mục tiêu không; điều kiện tiên quyết là dữ liệu có shape và ý nghĩa từng giá trị rõ ràng.


**Quy trình giải:** Lưu đầu vào đã nêu, dùng công thức hoặc hàm trong code rồi đối chiếu kết quả in ra.

```python
import numpy as np
A=np.eye(2)
x=np.array([2,3])
b=np.array([2,4])
print(A@x-b)
```

**Kết quả khi chạy:**

```text
[ 0. -1.]
```


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

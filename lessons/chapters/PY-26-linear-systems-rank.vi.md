# PY-26 — Hệ phương trình tuyến tính, rank và nghiệm


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Linear system** — hệ tuyến tính; **Rank** — hạng ma trận.

`Ma trận → Rank/Solve → Regression → AI`

**Học xong dùng để làm gì?** Kiểm tra hệ ràng buộc có đủ thông tin để giải hay có phương trình trùng, thiếu hoặc mâu thuẫn.

**Kết nối kiến thức tiếp theo:** PY-27 xác định hướng đặc biệt của phép biến đổi ma trận qua trị riêng/vector riêng.

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

**Nội dung chính:** một hệ tuyến tính liên kết nhiều phương trình qua cùng các ẩn. Ta xác định đúng **hàng = phương trình**, **cột = ẩn**, **vế phải = giá trị đã biết**, sau đó kiểm tra tính độc lập và độ khớp của nghiệm.

### 4.1. Linear system — Một hệ phương trình chung các ẩn

**Từ vựng trong mục:** **Linear system** — hệ tuyến tính; **Equation** — phương trình.

Hệ tuyến tính là **nhiều phương trình cùng chứa các ẩn cần tìm**. Cửa hàng bán loại A giá `x` và loại B giá `y` (đơn vị nghìn đồng): mua một A và một B hết 5; mua hai A và một B hết 8. Ta có `x+y=5` và `2x+y=8`. Để viết `Ax=b`, mỗi **hàng của A là một phương trình**, mỗi **cột là hệ số của một ẩn**, `b` chứa tổng tiền từng hóa đơn. Giải hệ tìm được x=3, y=2.

```python
import numpy as np

A = np.array([[1, 1], [2, 1]], dtype=float)
b = np.array([5, 8], dtype=float)
print(np.linalg.solve(A, b))
```

**Kết quả khi chạy:**

```text
[3. 2.]
```

Loại A giá 3 nghìn và loại B giá 2 nghìn đồng; nghiệm đồng thời thỏa hai hóa đơn.

### 4.2. Rank — Số thông tin độc lập

**Từ vựng trong mục:** **Rank** — hạng; **Linear dependence** — phụ thuộc tuyến tính.

**Rank** cho biết có bao nhiêu hàng/cột độc lập tuyến tính trong một ma trận. Ví dụ hai hàng `[1,2]` và `[2,4]`: hàng sau chỉ bằng hai lần hàng đầu nên không đưa thêm thông tin độc lập. Rank bằng 1 dù bảng có hai hàng và hai cột. Với một hệ 2 ẩn, nếu rank(A)=2 và A vuông thì nghiệm duy nhất khi hệ có vế phải b phù hợp (ở đây ma trận khả nghịch); nếu rank thấp cần kiểm tra cả ma trận mở rộng để biết vô nghiệm hay vô số nghiệm.

```python
import numpy as np

A = np.array([[1, 2], [2, 4]])
print(np.linalg.matrix_rank(A))
```

**Kết quả khi chạy:**

```text
1
```

Hai hàng phụ thuộc nhau nên số chiều thông tin độc lập chỉ là một.

### 4.3. Coefficient matrix — Bảng hệ số và vế phải

**Từ vựng trong mục:** **Coefficient matrix** — ma trận hệ số; **Augmented matrix** — ma trận mở rộng.

Trong `Ax=b`, **A chỉ chứa hệ số của các ẩn**, còn b chứa **giá trị đích của từng phương trình**. Ví dụ hệ `x+y=5`, `2x+y=8` có A hai hàng × hai cột, b dài hai phần tử. Ghép b thành một cột cuối bằng `np.column_stack((A,b))` cho ma trận mở rộng 2×3. Cột cuối này **không phải một ẩn mới**. Khi giải, số hàng A phải bằng số phần tử b.

```python
import numpy as np

A = np.array([[1, 1], [2, 1]])
b = np.array([5, 8])
print(np.column_stack((A, b)))
```

**Kết quả khi chạy:**

```text
[[1 1 5]
 [2 1 8]]
```

Hai cột đầu là hệ số của x, y; cột cuối là tổng tiền hóa đơn.

### 4.4. Residual — Sai lệch và nghiệm bình phương tối thiểu

**Từ vựng trong mục:** **Residual** — sai số dư; **Least squares** — bình phương tối thiểu.

Khi thử nghiệm x cho hệ `Ax=b`, **sai số dư** `r=Ax-b` đo mỗi phương trình lệch bao nhiêu so với vế phải. Nếu `r=0` thì nghiệm thỏa chính xác; dữ liệu đo thực tế thường có nhiễu nên không tìm được nghiệm thỏa mọi hàng. Khi số phương trình nhiều hơn số ẩn, `np.linalg.lstsq` tìm x làm **tổng bình phương các sai số dư nhỏ nhất**. Ví dụ ba số đo có x=1,2,3 và giá trị y=2,4,6.1; fit đường `y=m*x+c` không khớp hoàn toàn và cho gần `m=2.05`, `c=-0.067`.

```python
import numpy as np

x = np.array([1, 2, 3])
y = np.array([2, 4, 6.1])
A = np.column_stack((x, np.ones_like(x)))
coeff = np.linalg.lstsq(A, y, rcond=None)[0]
print(np.round(coeff, 3))
```

**Kết quả khi chạy:**

```text
[ 2.05  -0.067]
```

Hệ số góc xấp xỉ 2,05 và hệ số chặn xấp xỉ −0,067; đây là nghiệm xấp xỉ do số đo có nhiễu.

## 5. Năm tình huống ứng dụng

### Tình huống 1 — Tính giá hai loại hàng

**Tình huống thực tế:** Một hóa đơn gồm một món A và một món B giá tổng cộng 5 nghìn đồng; hóa đơn khác gồm hai A và một B hết 8 nghìn đồng. Hai đơn giá chưa biết, ký hiệu x,y. Tìm giá từng món.

**Vì sao chọn cách giải này?** Hệ hai phương trình độc lập và hai ẩn có ma trận hệ số vuông, khả nghịch; dùng `solve` tìm nghiệm chính xác.

**Quy trình giải:**

1. Đặt hai ẩn x, y là giá A, B, cùng đơn vị nghìn đồng.
2. Đưa hệ số từ hai hóa đơn vào hai hàng ma trận A và tổng tiền vào b.
3. Dùng `np.linalg.solve` rồi in hai đơn giá.

```python
import numpy as np

A = np.array([[1, 1], [2, 1]], dtype=float)
b = np.array([5, 8], dtype=float)
print(np.linalg.solve(A, b))
```

**Kết quả khi chạy:**

```text
[3. 2.]
```

Giá món A là 3 nghìn, món B là 2 nghìn đồng.

### Tình huống 2 — Phát hiện hai cột dữ liệu phụ thuộc

**Tình huống thực tế:** Bảng đặc trưng của hai mẫu có hàng `[1,2]`, `[2,4]`. Cột hai luôn gấp đôi cột một, nên đội phân tích muốn biết bảng có hai hướng thông tin độc lập hay không.

**Vì sao chọn cách giải này?** Rank phản ánh số chiều độc lập; với hai cột tỷ lệ nhau, hạng chỉ bằng một.

**Quy trình giải:**

1. Tạo ma trận hai hàng × hai cột, mỗi hàng là một mẫu.
2. Dùng `matrix_rank` tính số chiều độc lập.
3. In rank để đối chiếu với hai cột đầu vào.

```python
import numpy as np

A = np.array([[1, 2], [2, 4]])
print(np.linalg.matrix_rank(A))
```

**Kết quả khi chạy:**

```text
1
```

Chỉ có một hướng thông tin độc lập, không phải hai.

### Tình huống 3 — Kiểm tra nghiệm của hệ

**Tình huống thực tế:** Một hệ có A=`[[1,1],[2,1]]` và b=`[5,8]`. Người học đề xuất nghiệm x=`[3,2]`. Kiểm tra nghiệm này có tái tạo được cả hai vế phải không.

**Vì sao chọn cách giải này?** Tính `A@x` rồi dùng `np.allclose` so b, tránh lệ thuộc vào việc tự nhìn từng phương trình.

**Quy trình giải:**

1. Nhập ma trận hai phương trình và hai giá trị ở vế phải.
2. Nhập nghiệm thử `[3,2]`.
3. So `A @ x` với b và in kết quả Boolean.

```python
import numpy as np

A = np.array([[1, 1], [2, 1]])
b = np.array([5, 8])
x = np.array([3, 2])
print(np.allclose(A @ x, b))
```

**Kết quả khi chạy:**

```text
True
```

Nghiệm đã cho thỏa đồng thời cả hai phương trình.

### Tình huống 4 — Ước lượng đường thẳng từ số đo có nhiễu

**Tình huống thực tế:** Thiết bị ghi x lần lượt 1,2,3 và y lần lượt 2,4,6.1, cùng đơn vị đo phù hợp. Cần ước lượng đường y=m*x+c dù ba điểm không nằm chính xác trên một đường.

**Vì sao chọn cách giải này?** `lstsq` tối thiểu hóa tổng bình phương sai số khi ba phương trình chỉ có hai ẩn m,c.

**Quy trình giải:**

1. Đặt mỗi hàng của A là `[x_i,1]`, tương ứng hệ số m và c.
2. Đưa ba giá trị y vào vế phải và giải bằng `lstsq`.
3. Làm tròn hệ số để đầu ra minh họa ổn định.

```python
import numpy as np

x = np.array([1, 2, 3])
y = np.array([2, 4, 6.1])
A = np.column_stack((x, np.ones_like(x)))
coeff = np.linalg.lstsq(A, y, rcond=None)[0]
print(np.round(coeff, 3))
```

**Kết quả khi chạy:**

```text
[ 2.05  -0.067]
```

Đường khớp xấp xỉ `y=2.05x−0.067`, không phải một đường đi qua chính xác cả ba số đo.

### Tình huống 5 — Đo sai số dư của một dự báo

**Tình huống thực tế:** Một mô hình trả dự báo `[2,3]` cho hai giá trị mục tiêu `[2,4]` cùng đơn vị. Cần biết mô hình chênh bao nhiêu ở từng quan sát, quy ước dư = dự báo − thực tế.

**Vì sao chọn cách giải này?** Vector `Ax-b` mô tả độ lệch có dấu cho từng hàng; số âm nghĩa là dự báo thấp hơn thực tế.

**Quy trình giải:**

1. Dùng ma trận đơn vị để `A@x` chính là hai dự báo.
2. Trừ vector b của hai giá trị thực tế.
3. In vector sai số dư theo thứ tự hai quan sát.

```python
import numpy as np

A = np.eye(2)
x = np.array([2, 3])
b = np.array([2, 4])
print(A @ x - b)
```

**Kết quả khi chạy:**

```text
[ 0. -1.]
```

Quan sát đầu đúng hoàn toàn; quan sát thứ hai dự báo thấp hơn thực tế một đơn vị.

## 6. Sai lầm thường gặp

- Một hàng của A là một phương trình; một cột là hệ số của một ẩn. Không được đảo hai chiều khi đọc dữ liệu.
- b là giá trị đã biết ở vế phải, không phải cột hệ số của một ẩn mới.
- Hệ phụ thuộc hàng có thể vô nghiệm hoặc vô số nghiệm; xét cả rank(A) và rank([A, b]), không kết luận chỉ từ rank(A).
- `solve` dành cho ma trận vuông khả nghịch; `lstsq` giải gần đúng được cả hệ có nhiều số đo.
- Residual có dấu; bình phương tối thiểu tối ưu tổng **bình phương** dư chứ không tối ưu tổng dư có dấu.
- Chỉ dùng `np.allclose` để kiểm nghiệm trong sai số số học, không coi đó là bằng nhau tuyệt đối.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Các câu hỏi chỉ kiểm tra khái niệm và cách áp dụng kiến thức, không yêu cầu nhớ tình huống thực hành.**

**Q1. What is a linear system? — Hệ tuyến tính là gì?**

A. Several linear equations sharing unknowns — Nhiều phương trình tuyến tính chung các ẩn

B. The number of linearly independent rows or columns — Số hàng hoặc cột độc lập tuyến tính

C. The coefficients multiplying the unknowns — Các hệ số nhân với từng ẩn

D. `A @ x - b` — `A @ x - b`

**Đáp án: A**

**Giải thích:** Các phương trình cùng chứa các ẩn cần giải.


**Q2. What does the rank of a matrix measure? — Rank của ma trận đo gì?**

A. Several linear equations sharing unknowns — Nhiều phương trình tuyến tính chung các ẩn

B. The number of linearly independent rows or columns — Số hàng hoặc cột độc lập tuyến tính

C. The coefficients multiplying the unknowns — Các hệ số nhân với từng ẩn

D. `A @ x - b` — `A @ x - b`

**Đáp án: B**

**Giải thích:** Rank đếm hướng độc lập, không chỉ số hàng.


**Q3. What does a coefficient matrix contain? — Ma trận hệ số chứa gì?**

A. Several linear equations sharing unknowns — Nhiều phương trình tuyến tính chung các ẩn

B. The number of linearly independent rows or columns — Số hàng hoặc cột độc lập tuyến tính

C. The coefficients multiplying the unknowns — Các hệ số nhân với từng ẩn

D. `A @ x - b` — `A @ x - b`

**Đáp án: C**

**Giải thích:** Ma trận chứa hệ số số học của từng ẩn.


**Q4. What is the residual vector for Ax=b? — Vector sai số dư của Ax=b là gì?**

A. Several linear equations sharing unknowns — Nhiều phương trình tuyến tính chung các ẩn

B. The number of linearly independent rows or columns — Số hàng hoặc cột độc lập tuyến tính

C. The coefficients multiplying the unknowns — Các hệ số nhân với từng ẩn

D. `A @ x - b` — `A @ x - b`

**Đáp án: D**

**Giải thích:** Lấy Ax trừ b cho độ lệch từng phương trình.


**Q5. Which tool solves a nonsingular square system? — Hàm nào giải hệ vuông không suy biến?**

A. `np.linalg.solve(A,b)` — `np.linalg.solve(A,b)`

B. `np.linalg.matrix_rank(A)` — `np.linalg.matrix_rank(A)`

C. `np.column_stack((A,b))` — `np.column_stack((A,b))`

D. `np.linalg.lstsq(A,b,rcond=None)` — `np.linalg.lstsq(A,b,rcond=None)`

**Đáp án: A**

**Giải thích:** solve dùng cho ma trận hệ số vuông, không suy biến.


**Q6. Which tool determines matrix rank? — Hàm nào tính hạng ma trận?**

A. `np.linalg.solve(A,b)` — `np.linalg.solve(A,b)`

B. `np.linalg.matrix_rank(A)` — `np.linalg.matrix_rank(A)`

C. `np.column_stack((A,b))` — `np.column_stack((A,b))`

D. `np.linalg.lstsq(A,b,rcond=None)` — `np.linalg.lstsq(A,b,rcond=None)`

**Đáp án: B**

**Giải thích:** matrix_rank đo số chiều độc lập.


**Q7. Which tool builds an augmented matrix? — Hàm nào ghép ma trận mở rộng?**

A. `np.linalg.solve(A,b)` — `np.linalg.solve(A,b)`

B. `np.linalg.matrix_rank(A)` — `np.linalg.matrix_rank(A)`

C. `np.column_stack((A,b))` — `np.column_stack((A,b))`

D. `np.linalg.lstsq(A,b,rcond=None)` — `np.linalg.lstsq(A,b,rcond=None)`

**Đáp án: C**

**Giải thích:** column_stack ghép b thành cột bên cạnh A.


**Q8. Which tool computes a least-squares solution? — Hàm nào tìm nghiệm bình phương tối thiểu?**

A. `np.linalg.solve(A,b)` — `np.linalg.solve(A,b)`

B. `np.linalg.matrix_rank(A)` — `np.linalg.matrix_rank(A)`

C. `np.column_stack((A,b))` — `np.column_stack((A,b))`

D. `np.linalg.lstsq(A,b,rcond=None)` — `np.linalg.lstsq(A,b,rcond=None)`

**Đáp án: D**

**Giải thích:** lstsq tối thiểu hóa bình phương độ dài Ax−b.


**Q9. For Ax=b with A shape (3,2), what do the rows represent? — Với A shape (3,2), các hàng biểu diễn gì?**

A. Three equations or observations — Ba phương trình hoặc quan sát

B. Coefficients of two unknowns — Hệ số của hai ẩn

C. The right-hand-side values — Các giá trị vế phải

D. It cannot have a unique solution for every b — Không thể có nghiệm duy nhất với mọi b

**Đáp án: A**

**Giải thích:** Ba hàng tương ứng ba quan sát hoặc phương trình.


**Q10. For Ax=b with A shape (3,2), what do the columns represent? — Với A shape (3,2), các cột biểu diễn gì?**

A. Three equations or observations — Ba phương trình hoặc quan sát

B. Coefficients of two unknowns — Hệ số của hai ẩn

C. The right-hand-side values — Các giá trị vế phải

D. It cannot have a unique solution for every b — Không thể có nghiệm duy nhất với mọi b

**Đáp án: B**

**Giải thích:** Hai cột là hệ số của hai ẩn ở từng phương trình.


**Q11. What does the final column of an augmented matrix represent? — Cột cuối của ma trận mở rộng biểu diễn gì?**

A. Three equations or observations — Ba phương trình hoặc quan sát

B. Coefficients of two unknowns — Hệ số của hai ẩn

C. The right-hand-side values — Các giá trị vế phải

D. It cannot have a unique solution for every b — Không thể có nghiệm duy nhất với mọi b

**Đáp án: C**

**Giải thích:** Ma trận mở rộng ghi các vế phải ở cột cuối.


**Q12. What does a rank-deficient square matrix imply? — Ma trận vuông thiếu hạng gợi ý điều gì?**

A. Three equations or observations — Ba phương trình hoặc quan sát

B. Coefficients of two unknowns — Hệ số của hai ẩn

C. The right-hand-side values — Các giá trị vế phải

D. It cannot have a unique solution for every b — Không thể có nghiệm duy nhất với mọi b

**Đáp án: D**

**Giải thích:** Thiếu hạng đầy đủ khiến không bảo đảm nghiệm duy nhất.


**Q13. If the residual is exactly zero, what is true? — Nếu sai số dư bằng 0 thì điều gì đúng?**

A. Every equation is satisfied — Mọi phương trình đều được thỏa

B. The sum of squared residuals — Tổng bình phương sai số dư

C. Whether a candidate solution approximately satisfies the system — Nghiệm thử có thỏa hệ gần đúng hay không

D. Ranks of A and its augmented matrix — Hạng của A và ma trận mở rộng

**Đáp án: A**

**Giải thích:** Sai số dư bằng 0 nghĩa là Ax=b.


**Q14. What does least squares minimize? — Bình phương tối thiểu làm nhỏ nhất gì?**

A. Every equation is satisfied — Mọi phương trình đều được thỏa

B. The sum of squared residuals — Tổng bình phương sai số dư

C. Whether a candidate solution approximately satisfies the system — Nghiệm thử có thỏa hệ gần đúng hay không

D. Ranks of A and its augmented matrix — Hạng của A và ma trận mở rộng

**Đáp án: B**

**Giải thích:** Bình phương sai lệch làm lỗi lớn bị phạt mạnh.


**Q15. What does `np.allclose(A@x,b)` check? — `np.allclose(A@x,b)` kiểm tra gì?**

A. Every equation is satisfied — Mọi phương trình đều được thỏa

B. The sum of squared residuals — Tổng bình phương sai số dư

C. Whether a candidate solution approximately satisfies the system — Nghiệm thử có thỏa hệ gần đúng hay không

D. Ranks of A and its augmented matrix — Hạng của A và ma trận mở rộng

**Đáp án: C**

**Giải thích:** allclose so kết quả trong ngưỡng sai số số học.


**Q16. What should be compared to diagnose inconsistency of a system? — Để xét hệ vô nghiệm cần so sánh gì?**

A. Every equation is satisfied — Mọi phương trình đều được thỏa

B. The sum of squared residuals — Tổng bình phương sai số dư

C. Whether a candidate solution approximately satisfies the system — Nghiệm thử có thỏa hệ gần đúng hay không

D. Ranks of A and its augmented matrix — Hạng của A và ma trận mở rộng

**Đáp án: D**

**Giải thích:** Hạng A khác hạng [A, b] cho biết hệ vô nghiệm.


**Q17. Why isn't the right-hand side b another unknown? — Vì sao b không phải một ẩn mới?**

A. It contains known target values — Nó chứa giá trị mục tiêu đã biết

B. They add no new independent direction — Chúng không bổ sung hướng độc lập mới

C. When observations outnumber unknowns or do not fit exactly — Khi nhiều quan sát hơn ẩn hoặc không khớp chính xác

D. Prediction is lower than actual — Dự báo thấp hơn thực tế

**Đáp án: A**

**Giải thích:** b là dữ liệu đã biết, x mới là biến chưa biết.


**Q18. What happens when rows of A are multiples of each other? — Nếu các hàng A là bội nhau thì sao?**

A. It contains known target values — Nó chứa giá trị mục tiêu đã biết

B. They add no new independent direction — Chúng không bổ sung hướng độc lập mới

C. When observations outnumber unknowns or do not fit exactly — Khi nhiều quan sát hơn ẩn hoặc không khớp chính xác

D. Prediction is lower than actual — Dự báo thấp hơn thực tế

**Đáp án: B**

**Giải thích:** Hàng tỷ lệ chỉ lặp thông tin tuyến tính.


**Q19. When is `lstsq` useful? — Khi nào `lstsq` hữu ích?**

A. It contains known target values — Nó chứa giá trị mục tiêu đã biết

B. They add no new independent direction — Chúng không bổ sung hướng độc lập mới

C. When observations outnumber unknowns or do not fit exactly — Khi nhiều quan sát hơn ẩn hoặc không khớp chính xác

D. Prediction is lower than actual — Dự báo thấp hơn thực tế

**Đáp án: C**

**Giải thích:** Bình phương tối thiểu tìm cách khớp tốt nhất khi hệ không thỏa hết.


**Q20. What does a negative residual mean under r=prediction−actual? — Sai số dư âm theo r=dự báo−thực tế nghĩa là gì?**

A. It contains known target values — Nó chứa giá trị mục tiêu đã biết

B. They add no new independent direction — Chúng không bổ sung hướng độc lập mới

C. When observations outnumber unknowns or do not fit exactly — Khi nhiều quan sát hơn ẩn hoặc không khớp chính xác

D. Prediction is lower than actual — Dự báo thấp hơn thực tế

**Đáp án: D**

**Giải thích:** Dự báo trừ thực tế là số âm khi dự báo thiếu.

## 8. Nối sang bài kế tiếp

`Ma trận → Rank/Solve → Regression → AI`.

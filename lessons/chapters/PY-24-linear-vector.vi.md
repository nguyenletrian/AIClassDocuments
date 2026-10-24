# PY-24 — Scalar, vector, norm, đơn vị và dot product


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Scalar** — đại lượng vô hướng; **Vector** — véc-tơ.

`NumPy → Scalar/Vector → Matrix → PCA`

Nắm liên hệ giữa cấu trúc toán học và mảng dữ liệu Python trước khi sử dụng vào học máy.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Giải thích |
|---|---|---|
| Scalar | đại lượng vô hướng | Một số đơn lẻ có thể đo độ lớn |
| Vector | véc-tơ | Dãy số mô tả nhiều thành phần của một đối tượng |
| Norm | độ lớn véc-tơ | Độ dài theo chuẩn đã chọn |
| Dot product | tích vô hướng | Nhân từng cặp tọa độ tương ứng rồi cộng |

## 3. NumPy và các hàm liên quan

**Từ vựng trong mục:** **Function** — hàm; **Shape** — kích thước mảng.

| Hàm / tham số | Dùng làm gì |
|---|---|
| `np.array([...],dtype=float)` | Tạo véc-tơ kiểu thực khi phép tính tạo phần thập phân |
| `np.linalg.norm(v)` | Độ lớn Euclidean của véc-tơ |
| `v/np.linalg.norm(v)` | Chuẩn hóa về độ dài 1, phải tránh norm bằng 0 |
| `a @ b / np.dot(a,b)` | Tích vô hướng nếu hai vector một chiều cùng độ dài |

## 4. Khái niệm liên quan

Bài học nối bốn ý: **scalar** là số đơn lẻ, **vector** chứa tọa độ, **norm** đo độ dài, **dot product** kết hợp các thành phần. Robot dịch chuyển `(3,4)` mét có vector hai chiều nhưng quãng đường thẳng chỉ là một số bằng 5 mét.

### 4.1. Scalar — Số đơn lẻ và đơn vị

Scalar là một giá trị số như vận tốc 2,5 mét/giây. Python lưu số, còn ý nghĩa và đơn vị phải do người lập trình nêu. Scalar khác vector vì không chứa nhiều thành phần tọa độ.

```python
speed = 2.5
print(speed)
```

**Kết quả khi chạy:**

```text
2.5
```

Số 2.5 đại diện vận tốc m/s, không phải tọa độ.

### 4.2. Vector — Các tọa độ có thứ tự

Vector là dãy tọa độ theo một hệ trục. Robot đi 3 m theo x và 4 m theo y nên dùng vector `[3,4]`. Phần tử đầu là x, phần tử sau là y. Đổi `[3,4]` thành `[4,3]` sẽ đổi ý nghĩa hai trục.

```python
import numpy as np

movement = np.array([3, 4])
print(movement)
```

**Kết quả khi chạy:**

```text
[3 4]
```

Hai phần tử lần lượt là độ dịch chuyển theo x và y (mét).

### 4.3. Norm — Độ dài vector

Chuẩn Euclid là độ dài `sqrt(x²+y²)`. Với vector `(3,4)`, độ dài bằng `sqrt(9+16)=5` m. Vector đơn vị giữ hướng và có norm bằng 1; muốn chuẩn hóa phải chia các thành phần cho norm, trừ trường hợp norm bằng 0.

```python
import numpy as np

movement = np.array([3.0, 4.0])
print(np.linalg.norm(movement))
```

**Kết quả khi chạy:**

```text
5.0
```

Robot cách gốc tọa độ 5 mét theo đường thẳng.

### 4.4. Dot product — Nhân và cộng cùng vị trí

Tích vô hướng của hai vector cùng số chiều bằng tổng các tích từng thành phần: `(1,2)·(3,4)=1×3+2×4=11`. Dùng để tính điểm có trọng số hoặc kiểm tra hai vector khác không vuông góc (khi tích vô hướng bằng 0).

```python
import numpy as np

a = np.array([1, 2])
b = np.array([3, 4])
print(a @ b)
```

**Kết quả khi chạy:**

```text
11
```

Tích vô hướng trả một scalar bằng 11.

## 5. Năm tình huống ứng dụng

### Tình huống 1 — Tính khoảng cách 2D

**Từ vựng trong mục:** **Scalar** — đại lượng vô hướng.

**Tình huống thực tế:** Robot di chuyển từ (0,0) tới (3,4) mét. Tính khoảng cách theo đường thẳng.

**Vì sao chọn cách giải này?** Norm của vector dịch chuyển là khoảng cách tới gốc.


**Quy trình giải:**

1. Tạo vector từ (0,0) đến (3,4) mét.
2. Tính norm Euclid.
3. In khoảng cách 5 mét.

```python
import numpy as np
v=np.array([3,4],dtype=float)
print(np.linalg.norm(v))
```

**Kết quả khi chạy:**

```text
5.0
```


### Tình huống 2 — Chuẩn hóa hướng di chuyển

**Từ vựng trong mục:** **Vector** — véc-tơ.

**Tình huống thực tế:** Robot nhận vector hướng (3,4). Chuẩn hóa thành vector đơn vị để chỉ biểu thị hướng.

**Vì sao chọn cách giải này?** Chia vector cho norm tạo hướng có độ dài bằng 1.


**Quy trình giải:**

1. Tạo vector hướng (3,4) dạng float.
2. Tính norm và chia nếu norm khác 0.
3. In vector đơn vị [0.6,0.8].

```python
import numpy as np
v=np.array([3.,4.])
norm=np.linalg.norm(v)
u=v/norm if norm else v
print(u)
```

**Kết quả khi chạy:**

```text
[0.6 0.8]
```


### Tình huống 3 — Điểm tổng kết có trọng số

**Từ vựng trong mục:** **Dot product** — tích vô hướng.

**Tình huống thực tế:** Điểm ba môn của học viên là [8,7,9] theo trọng số [20%,30%,50%]. Tính điểm tổng kết.

**Vì sao chọn cách giải này?** Tích vô hướng kết hợp điểm số và trọng số từng môn.


**Quy trình giải:**

1. Lưu ba điểm và ba trọng số theo cùng thứ tự môn.
2. Nhân bằng `@` để tính tổng có trọng số.
3. In 8.2 điểm trên thang 10.

```python
import numpy as np
scores=np.array([8,7,9])
weights=np.array([.2,.3,.5])
print(scores@weights)
```

**Kết quả khi chạy:**

```text
8.2
```


### Tình huống 4 — Tìm hai hướng vuông góc

**Từ vựng trong mục:** **Dot product** — tích vô hướng.

**Tình huống thực tế:** Hai hướng [1,0] và [0,1] cần kiểm tra vuông góc bằng tích vô hướng.

**Vì sao chọn cách giải này?** Tích vô hướng bằng 0 với hai vector khác không chứng tỏ vuông góc.


**Quy trình giải:**

1. Tạo hai vector khác không [1,0] và [0,1].
2. Tính tích vô hướng.
3. In 0 và xác định hai vector vuông góc.

```python
import numpy as np
a=np.array([1,0])
b=np.array([0,1])
print(a@b)
```

**Kết quả khi chạy:**

```text
0
```


### Tình huống 5 — Tính sai khác cảm biến

**Từ vựng trong mục:** **Scalar** — đại lượng vô hướng.

**Tình huống thực tế:** Hai lần đo cảm biến theo cặp cùng đơn vị là (20,30) và (23,34). Tính độ lệch Euclid.

**Vì sao chọn cách giải này?** Norm của hiệu vector đo khoảng cách giữa hai lần đo.


**Quy trình giải:**

1. Lưu hai cặp đo cùng đơn vị.
2. Tính hiệu vector và norm của hiệu.
3. In chênh lệch Euclid là 5.

```python
import numpy as np
a=np.array([20,30])
b=np.array([23,34])
print(np.linalg.norm(a-b))
```

**Kết quả khi chạy:**

```text
5.0
```


## 6. Sai lầm thường gặp

- Scalar là số đơn; vector là dãy các thành phần có thứ tự.
- Khi tính khoảng cách, các thành phần phải cùng hệ trục và đơn vị phù hợp.
- Không chuẩn hóa vector không vì norm bằng 0.
- Dấu `*` NumPy nhân từng phần tử; `@` với hai vector 1-D tính tích vô hướng.
- Khi kiểm tra vuông góc với dữ liệu float, nên so với một ngưỡng sai số nhỏ.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.


**Q1. What is Scalar? — Thuật ngữ Scalar có nghĩa gì?**

A. It instead means Dãy số mô tả nhiều thành phần của một đối tượng — Dãy số mô tả nhiều thành phần của một đối tượng

B. It means Một số đơn lẻ có thể đo độ lớn — Một số đơn lẻ có thể đo độ lớn

C. It instead means Độ dài theo chuẩn đã chọn — Độ dài theo chuẩn đã chọn

D. It instead means Nhân từng cặp tọa độ tương ứng rồi cộng — Nhân từng cặp tọa độ tương ứng rồi cộng


**Q2. What is Vector? — Thuật ngữ Vector có nghĩa gì?**

A. It means Dãy số mô tả nhiều thành phần của một đối tượng — Dãy số mô tả nhiều thành phần của một đối tượng

B. It instead means Độ dài theo chuẩn đã chọn — Độ dài theo chuẩn đã chọn

C. It instead means Nhân từng cặp tọa độ tương ứng rồi cộng — Nhân từng cặp tọa độ tương ứng rồi cộng

D. It instead means Một số đơn lẻ có thể đo độ lớn — Một số đơn lẻ có thể đo độ lớn


**Q3. What is Norm? — Thuật ngữ Norm có nghĩa gì?**

A. It instead means Nhân từng cặp tọa độ tương ứng rồi cộng — Nhân từng cặp tọa độ tương ứng rồi cộng

B. It instead means Một số đơn lẻ có thể đo độ lớn — Một số đơn lẻ có thể đo độ lớn

C. It instead means Dãy số mô tả nhiều thành phần của một đối tượng — Dãy số mô tả nhiều thành phần của một đối tượng

D. It means Độ dài theo chuẩn đã chọn — Độ dài theo chuẩn đã chọn


**Q4. What is Dot product? — Thuật ngữ Dot product có nghĩa gì?**

A. It instead means Một số đơn lẻ có thể đo độ lớn — Một số đơn lẻ có thể đo độ lớn

B. It instead means Dãy số mô tả nhiều thành phần của một đối tượng — Dãy số mô tả nhiều thành phần của một đối tượng

C. It means Nhân từng cặp tọa độ tương ứng rồi cộng — Nhân từng cặp tọa độ tương ứng rồi cộng

D. It instead means Độ dài theo chuẩn đã chọn — Độ dài theo chuẩn đã chọn


**Q5. What does np.array([...],dtype=float) help with? — Hàm np.array([...],dtype=float) giúp làm gì?**

A. Another function helps to Độ lớn Euclidean của véc-tơ — Độ lớn Euclidean của véc-tơ

B. It helps to Tạo véc-tơ kiểu thực khi phép tính tạo phần thập phân — Tạo véc-tơ kiểu thực khi phép tính tạo phần thập phân

C. Another function helps to Chuẩn hóa về độ dài 1, phải tránh norm bằng 0 — Chuẩn hóa về độ dài 1, phải tránh norm bằng 0

D. Another function helps to Tích vô hướng nếu hai vector một chiều cùng độ dài — Tích vô hướng nếu hai vector một chiều cùng độ dài


**Q6. What does np.linalg.norm(v) help with? — Hàm np.linalg.norm(v) giúp làm gì?**

A. It helps to Độ lớn Euclidean của véc-tơ — Độ lớn Euclidean của véc-tơ

B. Another function helps to Chuẩn hóa về độ dài 1, phải tránh norm bằng 0 — Chuẩn hóa về độ dài 1, phải tránh norm bằng 0

C. Another function helps to Tích vô hướng nếu hai vector một chiều cùng độ dài — Tích vô hướng nếu hai vector một chiều cùng độ dài

D. Another function helps to Tạo véc-tơ kiểu thực khi phép tính tạo phần thập phân — Tạo véc-tơ kiểu thực khi phép tính tạo phần thập phân


**Q7. What does v/np.linalg.norm(v) help with? — Hàm v/np.linalg.norm(v) giúp làm gì?**

A. Another function helps to Tích vô hướng nếu hai vector một chiều cùng độ dài — Tích vô hướng nếu hai vector một chiều cùng độ dài

B. Another function helps to Tạo véc-tơ kiểu thực khi phép tính tạo phần thập phân — Tạo véc-tơ kiểu thực khi phép tính tạo phần thập phân

C. Another function helps to Độ lớn Euclidean của véc-tơ — Độ lớn Euclidean của véc-tơ

D. It helps to Chuẩn hóa về độ dài 1, phải tránh norm bằng 0 — Chuẩn hóa về độ dài 1, phải tránh norm bằng 0


**Q8. What does a @ b / np.dot(a,b) help with? — Hàm a @ b / np.dot(a,b) giúp làm gì?**

A. Another function helps to Tạo véc-tơ kiểu thực khi phép tính tạo phần thập phân — Tạo véc-tơ kiểu thực khi phép tính tạo phần thập phân

B. Another function helps to Độ lớn Euclidean của véc-tơ — Độ lớn Euclidean của véc-tơ

C. It helps to Tích vô hướng nếu hai vector một chiều cùng độ dài — Tích vô hướng nếu hai vector một chiều cùng độ dài

D. Another function helps to Chuẩn hóa về độ dài 1, phải tránh norm bằng 0 — Chuẩn hóa về độ dài 1, phải tránh norm bằng 0


**Q9. Why choose this method for scenario 1? — Vì sao chọn cách làm tình huống 1?**

A. Chia norm giúp hướng có độ dài 1 trước điều khiển tốc độ — Chia norm giúp hướng có độ dài 1 trước điều khiển tốc độ

B. Norm từ véc-tơ độ lệch giúp tính khoảng cách đến gốc — Norm từ véc-tơ độ lệch giúp tính khoảng cách đến gốc

C. Dot product của điểm và trọng số tạo điểm tổng — Dot product của điểm và trọng số tạo điểm tổng

D. Dot bằng 0 cho hai vector khác 0 biểu thị trực giao — Dot bằng 0 cho hai vector khác 0 biểu thị trực giao


**Q10. Why choose this method for scenario 2? — Vì sao chọn cách làm tình huống 2?**

A. Chia norm giúp hướng có độ dài 1 trước điều khiển tốc độ — Chia norm giúp hướng có độ dài 1 trước điều khiển tốc độ

B. Dot product của điểm và trọng số tạo điểm tổng — Dot product của điểm và trọng số tạo điểm tổng

C. Dot bằng 0 cho hai vector khác 0 biểu thị trực giao — Dot bằng 0 cho hai vector khác 0 biểu thị trực giao

D. Norm của hiệu vector đo mức sai khác tổng hợp — Norm của hiệu vector đo mức sai khác tổng hợp


**Q11. Why choose this method for scenario 3? — Vì sao chọn cách làm tình huống 3?**

A. Dot bằng 0 cho hai vector khác 0 biểu thị trực giao — Dot bằng 0 cho hai vector khác 0 biểu thị trực giao

B. Norm của hiệu vector đo mức sai khác tổng hợp — Norm của hiệu vector đo mức sai khác tổng hợp

C. Norm từ véc-tơ độ lệch giúp tính khoảng cách đến gốc — Norm từ véc-tơ độ lệch giúp tính khoảng cách đến gốc

D. Dot product của điểm và trọng số tạo điểm tổng — Dot product của điểm và trọng số tạo điểm tổng


**Q12. Why choose this method for scenario 4? — Vì sao chọn cách làm tình huống 4?**

A. Norm của hiệu vector đo mức sai khác tổng hợp — Norm của hiệu vector đo mức sai khác tổng hợp

B. Norm từ véc-tơ độ lệch giúp tính khoảng cách đến gốc — Norm từ véc-tơ độ lệch giúp tính khoảng cách đến gốc

C. Dot bằng 0 cho hai vector khác 0 biểu thị trực giao — Dot bằng 0 cho hai vector khác 0 biểu thị trực giao

D. Chia norm giúp hướng có độ dài 1 trước điều khiển tốc độ — Chia norm giúp hướng có độ dài 1 trước điều khiển tốc độ


**Q13. Why choose this method for scenario 5? — Vì sao chọn cách làm tình huống 5?**

A. Norm từ véc-tơ độ lệch giúp tính khoảng cách đến gốc — Norm từ véc-tơ độ lệch giúp tính khoảng cách đến gốc

B. Norm của hiệu vector đo mức sai khác tổng hợp — Norm của hiệu vector đo mức sai khác tổng hợp

C. Chia norm giúp hướng có độ dài 1 trước điều khiển tốc độ — Chia norm giúp hướng có độ dài 1 trước điều khiển tốc độ

D. Dot product của điểm và trọng số tạo điểm tổng — Dot product của điểm và trọng số tạo điểm tổng


**Q14. What input is relevant to scenario 1? — Dữ liệu nào của tình huống 1?**

A. The input is Vị trí điểm [3,4] mét — Vị trí điểm [3,4] mét

B. Different data: Véc-tơ [3,4] mét — Véc-tơ [3,4] mét

C. Different data: Điểm 8 7 9; trọng số 0.2,0.3,0.5 — Điểm 8 7 9; trọng số 0.2,0.3,0.5

D. Different data: a=[1,0], b=[0,1] — a=[1,0], b=[0,1]


**Q15. What input is relevant to scenario 2? — Dữ liệu nào của tình huống 2?**

A. Different data: Điểm 8 7 9; trọng số 0.2,0.3,0.5 — Điểm 8 7 9; trọng số 0.2,0.3,0.5

B. Different data: a=[1,0], b=[0,1] — a=[1,0], b=[0,1]

C. Different data: Hai kênh cảm biến trên cùng đơn vị — Hai kênh cảm biến trên cùng đơn vị

D. The input is Véc-tơ [3,4] mét — Véc-tơ [3,4] mét


**Q16. What input is relevant to scenario 3? — Dữ liệu nào của tình huống 3?**

A. Different data: a=[1,0], b=[0,1] — a=[1,0], b=[0,1]

B. Different data: Hai kênh cảm biến trên cùng đơn vị — Hai kênh cảm biến trên cùng đơn vị

C. The input is Điểm 8 7 9; trọng số 0.2,0.3,0.5 — Điểm 8 7 9; trọng số 0.2,0.3,0.5

D. Different data: Vị trí điểm [3,4] mét — Vị trí điểm [3,4] mét


**Q17. What input is relevant to scenario 4? — Dữ liệu nào của tình huống 4?**

A. Different data: Hai kênh cảm biến trên cùng đơn vị — Hai kênh cảm biến trên cùng đơn vị

B. The input is a=[1,0], b=[0,1] — a=[1,0], b=[0,1]

C. Different data: Vị trí điểm [3,4] mét — Vị trí điểm [3,4] mét

D. Different data: Véc-tơ [3,4] mét — Véc-tơ [3,4] mét


**Q18. What input is relevant to scenario 5? — Dữ liệu nào của tình huống 5?**

A. The input is Hai kênh cảm biến trên cùng đơn vị — Hai kênh cảm biến trên cùng đơn vị

B. Different data: Vị trí điểm [3,4] mét — Vị trí điểm [3,4] mét

C. Different data: Véc-tơ [3,4] mét — Véc-tơ [3,4] mét

D. Different data: Điểm 8 7 9; trọng số 0.2,0.3,0.5 — Điểm 8 7 9; trọng số 0.2,0.3,0.5


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
| Q1 | **B** | It means Một số đơn lẻ có thể đo độ lớn | Một số đơn lẻ có thể đo độ lớn |
| Q2 | **A** | It means Dãy số mô tả nhiều thành phần của một đối tượng | Dãy số mô tả nhiều thành phần của một đối tượng |
| Q3 | **D** | It means Độ dài theo chuẩn đã chọn | Độ dài theo chuẩn đã chọn |
| Q4 | **C** | It means Nhân từng cặp tọa độ tương ứng rồi cộng | Nhân từng cặp tọa độ tương ứng rồi cộng |
| Q5 | **B** | It helps to Tạo véc-tơ kiểu thực khi phép tính tạo phần thập phân | Tạo véc-tơ kiểu thực khi phép tính tạo phần thập phân |
| Q6 | **A** | It helps to Độ lớn Euclidean của véc-tơ | Độ lớn Euclidean của véc-tơ |
| Q7 | **D** | It helps to Chuẩn hóa về độ dài 1, phải tránh norm bằng 0 | Chuẩn hóa về độ dài 1, phải tránh norm bằng 0 |
| Q8 | **C** | It helps to Tích vô hướng nếu hai vector một chiều cùng độ dài | Tích vô hướng nếu hai vector một chiều cùng độ dài |
| Q9 | **B** | Norm từ véc-tơ độ lệch giúp tính khoảng cách đến gốc | Norm từ véc-tơ độ lệch giúp tính khoảng cách đến gốc |
| Q10 | **A** | Chia norm giúp hướng có độ dài 1 trước điều khiển tốc độ | Chia norm giúp hướng có độ dài 1 trước điều khiển tốc độ |
| Q11 | **D** | Dot product của điểm và trọng số tạo điểm tổng | Dot product của điểm và trọng số tạo điểm tổng |
| Q12 | **C** | Dot bằng 0 cho hai vector khác 0 biểu thị trực giao | Dot bằng 0 cho hai vector khác 0 biểu thị trực giao |
| Q13 | **B** | Norm của hiệu vector đo mức sai khác tổng hợp | Norm của hiệu vector đo mức sai khác tổng hợp |
| Q14 | **A** | The input is Vị trí điểm [3,4] mét | Vị trí điểm [3,4] mét |
| Q15 | **D** | The input is Véc-tơ [3,4] mét | Véc-tơ [3,4] mét |
| Q16 | **C** | The input is Điểm 8 7 9; trọng số 0.2,0.3,0.5 | Điểm 8 7 9; trọng số 0.2,0.3,0.5 |
| Q17 | **B** | The input is a=[1,0], b=[0,1] | a=[1,0], b=[0,1] |
| Q18 | **A** | The input is Hai kênh cảm biến trên cùng đơn vị | Hai kênh cảm biến trên cùng đơn vị |
| Q19 | **D** | Shapes and data units | Shape và đơn vị dữ liệu |
| Q20 | **C** | It does not establish predictive performance | Nó không đo chất lượng dự đoán |

## 8. Nối sang bài kế tiếp

`NumPy → Scalar/Vector → Matrix → PCA`.

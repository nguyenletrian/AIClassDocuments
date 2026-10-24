# PY-16 — NumPy reshape, transpose, ma trận và lưu file


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Reshape** — đổi hình dạng; **Transpose** — chuyển vị.

`ndarray → Reshape/Transpose → Matrix → Model Input`

Nắm khái niệm của bài này giúp xử lý đúng dữ liệu có nhiều đối tượng và đặc trưng trước khi dùng trong AI.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Dùng khi nào |
|---|---|---|
| Reshape | đổi hình dạng | Đổi shape nhưng giữ số phần tử |
| Transpose | chuyển vị | Đổi trục hàng và cột |
| Matrix multiply | nhân ma trận | Tạo kết quả bằng phép nhân tuyến tính |
| Serialization | lưu dữ liệu | Ghi mảng vào tệp để đọc lại |

## 3. Thư viện, hàm và lựa chọn

**Từ vựng trong mục:** **Function** — hàm; **Argument** — đối số.

| Hàm / tham số | Giải thích ngay theo hàm |
|---|---|
| `reshape(rows,cols)` | Số phần tử trước/sau phải bằng nhau |
| `X.T / np.transpose(X)` | Đổi trục từ hàng thành cột |
| `A @ B / np.dot(A,B)` | Nhân tuyến tính yêu cầu kích thước tương thích |
| `np.save()/np.load()` | Lưu và đọc định dạng NPY, chỉ tải từ nguồn tin cậy |


## 4. Khái niệm liên quan

Từ một dãy nhiệt độ hoặc bảng điểm, ta cần biết **bố trí lại dữ liệu**, **đổi chiều quan sát**, **tính điểm tổng hợp** và **lưu để sử dụng lại**. Bốn khái niệm này nối nhau: `reshape` bố trí hàng/cột, `.T` chuyển vị, `@` kết hợp các chiều đúng quy tắc, còn `np.save`/`np.load` lưu và phục hồi mảng.

### 4.1. Reshape — Đổi hình dạng mảng

**Từ vựng trong mục:** **Reshape** — đổi hình dạng; **Shape** — kích thước.

**Reshape** đổi cách sắp xếp một dãy phần tử thành các hàng/cột mới **mà không đổi số phần tử**. Ví dụ máy đo có 6 nhiệt độ theo thứ tự thời gian `[20,21,22,23,24,25]` °C. Nếu mỗi hàng đại diện một ngày và mỗi cột là một giờ đo, `reshape(2,3)` tạo bảng **2 ngày × 3 giờ**. Ngày đầu chứa ba số đầu, ngày hai chứa ba số sau. Không thể reshape 6 số thành `(4,2)` vì cần 8 số.

```python
import numpy as np

temperatures = np.array([20, 21, 22, 23, 24, 25])
print(temperatures.reshape(2, 3))
```

**Kết quả khi chạy:**

```text
[[20 21 22]
 [23 24 25]]
```

Mỗi hàng là một ngày, mỗi cột là một giờ đo theo thứ tự. Shape đổi từ `(6,)` thành `(2,3)`, còn thứ tự giá trị không đổi.

### 4.2. Transpose — Hoán đổi ý nghĩa hàng và cột

**Từ vựng trong mục:** **Transpose** — chuyển vị; **Row/column** — hàng/cột.

**Transpose** (`.T`) tráo hai trục của bảng hai chiều. Ví dụ bảng `scores` có **2 hàng học viên** An, Bình và **3 cột môn** Toán, Văn, Python: `[8,7,9]` và `[6,5,8]`. Sau `.T`, bảng thành **3 hàng môn** và **2 cột học viên**. Các điểm giữ nguyên nhưng cách trình bày đổi, giúp thống kê theo môn dễ nhìn hơn. Khác `reshape`, chuyển vị đổi vị trí của các ô theo trục.

```python
import numpy as np

scores = np.array([[8, 7, 9], [6, 5, 8]])
print(scores.T)
```

**Kết quả khi chạy:**

```text
[[8 6]
 [7 5]
 [9 8]]
```

Hàng đầu chứa điểm Toán của An và Bình, hàng hai là Văn, hàng ba là Python. Shape chuyển từ `(2,3)` thành `(3,2)`.

### 4.3. Matrix multiplication — Nhân ma trận

**Từ vựng trong mục:** **Matrix multiplication** — nhân ma trận; **Dot product** — tích vô hướng.

Toán tử `@` thực hiện **phép nhân ma trận**, không phải nhân từng ô như `*`. Với một học viên có điểm `[8,7,9]` cho ba môn và trọng số `[0.2,0.3,0.5]`, `scores @ weights` tính `8×0.2 + 7×0.3 + 9×0.5 = 8.2`. Với bảng nhiều học viên, các hàng là người và các cột là môn; ma trận trọng số phải có số hàng bằng số cột của bảng điểm, ví dụ `(2,3) @ (3,1) → (2,1)`.

```python
import numpy as np

scores = np.array([8, 7, 9])
weights = np.array([0.2, 0.3, 0.5])
print(scores @ weights)
```

**Kết quả khi chạy:**

```text
8.2
```

Điểm có trọng số là 8,2 trên thang 10. `@` nhân các thành phần tương ứng rồi cộng thành một điểm tổng kết.

### 4.4. Serialization — Lưu và đọc lại mảng

**Từ vựng trong mục:** **Serialization** — tuần tự hóa; **NPY** — định dạng lưu mảng NumPy.

**Tuần tự hóa (serialization)** là lưu dữ liệu trong bộ nhớ thành định dạng có thể đọc lại. NumPy dùng `np.save` ghi mảng thành tệp `.npy`, chứa cả **giá trị, shape và dtype**; `np.load` phục hồi dữ liệu. Ví dụ lưu ba điểm `[3,5,7]` vào thư mục tạm rồi đọc lại để kiểm tra. `allow_pickle=False` phù hợp khi chỉ cần dữ liệu số, tránh đọc đối tượng Python được pickle hóa từ nguồn không tin cậy. `tolist()` chỉ đổi mảng thành List, **không lưu file**.

```python
import numpy as np
from pathlib import Path
from tempfile import TemporaryDirectory

scores = np.array([3, 5, 7])
with TemporaryDirectory() as folder:
    file_path = Path(folder) / 'scores.npy'
    np.save(file_path, scores)
    restored = np.load(file_path, allow_pickle=False)
    print(restored)
```

**Kết quả khi chạy:**

```text
[3 5 7]
```

Mảng được ghi ra tệp `.npy` rồi đọc lại đủ ba phần tử. Thư mục tạm tự được dọn sau khi thoát khỏi `with`.

## 5. Năm tình huống thực tế

### Tình huống 1 — Tổ chức dữ liệu đo theo giờ

**Từ vựng trong mục:** **Reshape** — đổi hình dạng.

**Tình huống thực tế:** Thiết bị ghi sáu mức nhiệt độ 20, 21, 22, 23, 24, 25 °C theo thứ tự. Sắp dữ liệu thành bảng hai hàng, ba cột.

**Vì sao chọn cách giải này?** `reshape(2,3)` giữ nguyên 6 số nhưng đổi hình dạng.

**Quy trình giải:**

1. Ghi sáu giá trị nhiệt độ theo thứ tự giờ đo.
2. Đổi thành bảng hai ngày × ba giờ bằng `reshape(2, 3)`.
3. In bảng và kiểm tra ngày đầu chứa ba số đầu, ngày sau chứa ba số cuối.

```python
import numpy as np
values = np.array([20, 21, 22, 23, 24, 25])
print(values.reshape(2, 3))
```

**Kết quả khi chạy:**

```text
[[20 21 22]
 [23 24 25]]
```

### Tình huống 2 — Đổi hàng cột báo cáo

**Từ vựng trong mục:** **Transpose** — chuyển vị.

**Tình huống thực tế:** Trung tâm có bảng điểm hai học viên, ba môn: `(8,7,9)` và `(6,5,8)`. Chuyển hàng thành cột và in kích thước kết quả.

**Vì sao chọn cách giải này?** `.T` chuyển từ bảng 2×3 thành 3×2.

**Quy trình giải:**

1. Tạo bảng điểm gồm hai hàng học viên và ba cột môn.
2. Dùng `.T` đổi thành ba hàng môn × hai cột học viên.
3. In `scores.T.shape` để xác minh `(3, 2)`.

```python
import numpy as np
scores = np.array([[8, 7, 9], [6, 5, 8]])
print(scores.T.shape)
```

**Kết quả khi chạy:**

```text
(3, 2)
```

### Tình huống 3 — Điểm tổng kết có trọng số

**Từ vựng trong mục:** **Matrix multiply** — nhân ma trận.

**Tình huống thực tế:** Một học viên có điểm ba thành phần `[8,7,9]`, trọng số tương ứng `[0.2,0.3,0.5]`. Tính điểm tổng kết theo trọng số.

**Vì sao chọn cách giải này?** Tích vô hướng `@` nhân từng điểm với trọng số rồi cộng.

**Quy trình giải:**

1. Lưu ba điểm môn và ba trọng số theo đúng thứ tự.
2. Nhân tích vô hướng bằng toán tử `@`.
3. In điểm tổng kết, tính bằng `8×0.2 + 7×0.3 + 9×0.5`.

```python
import numpy as np
scores = np.array([8, 7, 9])
w = np.array([.2, .3, .5])
print(scores@w)
```

**Kết quả khi chạy:**

```text
8.2
```

### Tình huống 4 — Tạo đặc trưng tổng hợp

**Từ vựng trong mục:** **Matrix multiplication** — nhân ma trận.

**Tình huống thực tế:** Hai học viên có ba điểm `(8,7,9)` và `(6,5,8)`, cần tạo hai điểm tổng hợp theo ma trận trọng số trong code. In bảng điểm tổng hợp của hai học viên.

**Vì sao chọn cách giải này?** Phép `X @ W` nhân mảng dữ liệu 2×3 với trọng số 3×2, cho bảng 2×2.

**Quy trình giải:**

1. Tạo bảng điểm 2×3 và ma trận trọng số 3×2.
2. Nhân `X @ W` để tạo hai đặc trưng tổng hợp trên mỗi học viên.
3. In bảng 2×2 và xác định từng hàng vẫn tương ứng một học viên.

```python
import numpy as np
X = np.array([[8, 7, 9], [6, 5, 8]])
W = np.array([[.5, 0], [.5, .5], [0, .5]])
print(X@W)
```

**Kết quả khi chạy:**

```text
[[7.5 8. ]
 [5.5 6.5]]
```

### Tình huống 5 — Lưu và đọc mảng an toàn

**Từ vựng trong mục:** **Serialization** — lưu dữ liệu.

**Tình huống thực tế:** Nhà phân tích có dãy số `[3,5,7]` cần lưu để đọc lại. Ghi vào file tạm `.npy`, tải lại và in đúng các số.

**Vì sao chọn cách giải này?** `np.save` và `np.load(..., allow_pickle=False)` dùng định dạng mảng NumPy.

**Quy trình giải:**

1. Tạo mảng số và thư mục tạm làm nơi lưu.
2. Dùng `np.save` ghi `.npy`, `np.load(..., allow_pickle=False)` đọc lại.
3. In mảng đã khôi phục, đối chiếu với dữ liệu gốc.

```python
import numpy as np
from pathlib import Path
from tempfile import TemporaryDirectory
with TemporaryDirectory() as folder:
    p = Path(folder)/"data.npy"
    np.save(p, np.array([3, 5, 7]))
    print(np.load(p, allow_pickle=False))
```

**Kết quả khi chạy:**

```text
[3 5 7]
```

## 6. Sai lầm thường gặp

- `reshape` chỉ thành công khi **tích các kích thước mới bằng số phần tử ban đầu**. Sáu giá trị tạo được bảng 2×3, không phải 4×2.
- `reshape` và `.T` không tương đương: reshape nhóm lại các phần tử theo thứ tự, transpose tráo vị trí theo trục.
- `A * B` nhân từng ô khi broadcast được; `A @ B` nhân ma trận theo chiều tương thích. Với ma trận 2×3, bên phải cần có 3 hàng.
- Phải xác định rõ hàng là học viên/ngày, cột là môn/giờ đo trước khi đọc kết quả.
- `np.save` tạo file thực; `array.tolist()` chỉ chuyển sang List, không ghi file. Không bật `allow_pickle=True` với dữ liệu không đáng tin.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What does `reshape()` change? — `reshape()` thay đổi điều gì?**

A. The array's shape without changing its total element count — Hình dạng mảng mà không đổi số phần tử

B. Swaps rows and columns — Hoán đổi hàng và cột

C. Matrix multiplication — Phép nhân ma trận

D. Writes an array to an NPY file — Ghi mảng vào tệp NPY

**Q2. What does `.T` do to a 2-D array? — `.T` làm gì với mảng 2-D?**

A. The array's shape without changing its total element count — Hình dạng mảng mà không đổi số phần tử

B. Swaps rows and columns — Hoán đổi hàng và cột

C. Matrix multiplication — Phép nhân ma trận

D. Writes an array to an NPY file — Ghi mảng vào tệp NPY

**Q3. What does `A @ B` mean for compatible matrices? — `A @ B` nghĩa là gì với các ma trận tương thích?**

A. The array's shape without changing its total element count — Hình dạng mảng mà không đổi số phần tử

B. Swaps rows and columns — Hoán đổi hàng và cột

C. Matrix multiplication — Phép nhân ma trận

D. Writes an array to an NPY file — Ghi mảng vào tệp NPY

**Q4. What does `np.save()` do? — `np.save()` làm gì?**

A. The array's shape without changing its total element count — Hình dạng mảng mà không đổi số phần tử

B. Swaps rows and columns — Hoán đổi hàng và cột

C. Matrix multiplication — Phép nhân ma trận

D. Writes an array to an NPY file — Ghi mảng vào tệp NPY

**Q5. Which shape specifically has two rows and three columns? — Shape nào có đúng hai hàng và ba cột?**

A. `(2, 3)` — `(2, 3)`

B. `(3, 2)` — `(3, 2)`

C. `(2, 4)` — `(2, 4)`

D. `(6,)` — `(6,)`

**Q6. What is the transpose shape of a `(2, 3)` matrix? — Chuyển vị ma trận `(2, 3)` có shape nào?**

A. `(2, 3)` — `(2, 3)`

B. `(3, 2)` — `(3, 2)`

C. `(2, 4)` — `(2, 4)`

D. `(6,)` — `(6,)`

**Q7. What is the shape of `(2, 3) @ (3, 4)`? — Phép `(2, 3) @ (3, 4)` cho shape gì?**

A. `(2, 3)` — `(2, 3)`

B. `(3, 2)` — `(3, 2)`

C. `(2, 4)` — `(2, 4)`

D. `(6,)` — `(6,)`

**Q8. What shape has a one-dimensional array of six values? — Mảng một chiều có sáu giá trị có shape nào?**

A. `(2, 3)` — `(2, 3)`

B. `(3, 2)` — `(3, 2)`

C. `(2, 4)` — `(2, 4)`

D. `(6,)` — `(6,)`

**Q9. How does `reshape` differ from transpose? — reshape khác transpose ở đâu?**

A. Reshape regroups positions; transpose exchanges axes — Reshape nhóm lại vị trí; transpose đổi trục

B. `*` multiplies element-wise; `@` performs matrix multiplication — `*` nhân từng phần tử; `@` nhân ma trận

C. Reads the saved array — Đọc lại mảng đã lưu

D. Converts the array into Python lists or scalars — Chuyển mảng thành List hoặc số Python

**Q10. How does `*` differ from `@` for numeric ndarrays? — `*` khác `@` thế nào với ndarray số?**

A. Reshape regroups positions; transpose exchanges axes — Reshape nhóm lại vị trí; transpose đổi trục

B. `*` multiplies element-wise; `@` performs matrix multiplication — `*` nhân từng phần tử; `@` nhân ma trận

C. Reads the saved array — Đọc lại mảng đã lưu

D. Converts the array into Python lists or scalars — Chuyển mảng thành List hoặc số Python

**Q11. What does `np.load()` normally do for an NPY file? — `np.load()` làm gì với tệp NPY?**

A. Reshape regroups positions; transpose exchanges axes — Reshape nhóm lại vị trí; transpose đổi trục

B. `*` multiplies element-wise; `@` performs matrix multiplication — `*` nhân từng phần tử; `@` nhân ma trận

C. Reads the saved array — Đọc lại mảng đã lưu

D. Converts the array into Python lists or scalars — Chuyển mảng thành List hoặc số Python

**Q12. What does `array.tolist()` do? — `array.tolist()` làm gì?**

A. Reshape regroups positions; transpose exchanges axes — Reshape nhóm lại vị trí; transpose đổi trục

B. `*` multiplies element-wise; `@` performs matrix multiplication — `*` nhân từng phần tử; `@` nhân ma trận

C. Reads the saved array — Đọc lại mảng đã lưu

D. Converts the array into Python lists or scalars — Chuyển mảng thành List hoặc số Python

**Q13. What happens if you reshape six elements to `(4, 2)`? — Điều gì xảy ra nếu reshape sáu phần tử thành `(4, 2)`?**

A. A ValueError due to incompatible element counts — Phát sinh ValueError vì số phần tử không khớp

B. Left columns and right rows — Số cột bên trái và số hàng bên phải

C. `allow_pickle=False` — `allow_pickle=False`

D. Shape and dtype — Shape và dtype

**Q14. What must match to multiply two matrices with `@`? — Muốn nhân hai ma trận bằng `@`, chiều nào phải khớp?**

A. A ValueError due to incompatible element counts — Phát sinh ValueError vì số phần tử không khớp

B. Left columns and right rows — Số cột bên trái và số hàng bên phải

C. `allow_pickle=False` — `allow_pickle=False`

D. Shape and dtype — Shape và dtype

**Q15. Which option avoids loading pickled objects from an NPY file? — Tùy chọn nào tránh đọc đối tượng pickle trong file NPY?**

A. A ValueError due to incompatible element counts — Phát sinh ValueError vì số phần tử không khớp

B. Left columns and right rows — Số cột bên trái và số hàng bên phải

C. `allow_pickle=False` — `allow_pickle=False`

D. Shape and dtype — Shape và dtype

**Q16. What does NPY preserve in addition to array values? — NPY lưu thêm gì ngoài các giá trị?**

A. A ValueError due to incompatible element counts — Phát sinh ValueError vì số phần tử không khớp

B. Left columns and right rows — Số cột bên trái và số hàng bên phải

C. `allow_pickle=False` — `allow_pickle=False`

D. Shape and dtype — Shape và dtype

**Q17. What is a 1-D dot product of two equal-length numeric vectors? — Tích vô hướng của hai vector một chiều bằng nhau độ dài là gì?**

A. The sum of pairwise products — Tổng các tích của từng cặp phần tử

B. A 3-by-3 identity matrix — Ma trận đơn vị 3×3

C. `shape` — `shape`

D. `dtype` — `dtype`

**Q18. What does `np.eye(3)` create? — `np.eye(3)` tạo gì?**

A. The sum of pairwise products — Tổng các tích của từng cặp phần tử

B. A 3-by-3 identity matrix — Ma trận đơn vị 3×3

C. `shape` — `shape`

D. `dtype` — `dtype`

**Q19. Which property reports the array dimensions? — Thuộc tính nào cho biết kích thước các chiều?**

A. The sum of pairwise products — Tổng các tích của từng cặp phần tử

B. A 3-by-3 identity matrix — Ma trận đơn vị 3×3

C. `shape` — `shape`

D. `dtype` — `dtype`

**Q20. Which property reports element data type? — Thuộc tính nào cho biết kiểu phần tử?**

A. The sum of pairwise products — Tổng các tích của từng cặp phần tử

B. A 3-by-3 identity matrix — Ma trận đơn vị 3×3

C. `shape` — `shape`

D. `dtype` — `dtype`

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **A** | reshape rearranges the same elements into new dimensions. For six elements, reshaping from `(2,3)` to `(3,2)` is valid, but reshaping to `(4,2)` is not. | reshape bố trí lại cùng các phần tử theo kích thước mới. Với sáu phần tử, đổi `(2,3)` thành `(3,2)` hợp lệ, nhưng đổi thành `(4,2)` thì không. |
| Q2 | **B** | A transpose exchanges the two axes of a matrix. For `[[1,2,3],[4,5,6]]`, the transpose has three rows containing `[1,4]`, `[2,5]`, `[3,6]`. | Chuyển vị tráo hai trục của ma trận. Với `[[1,2,3],[4,5,6]]`, chuyển vị tạo ba hàng lần lượt là `[1,4]`, `[2,5]`, `[3,6]`. |
| Q3 | **C** | The @ operator follows matrix multiplication rather than per-cell multiplication. If `A` has shape `(2,3)` and `B` has shape `(3,4)`, then `A @ B` produces shape `(2,4)`; `*` is element-wise instead. | Toán tử @ tuân theo quy tắc nhân ma trận chứ không nhân riêng từng ô. Nếu `A` có shape `(2,3)` và `B` là `(3,4)`, thì `A @ B` có shape `(2,4)`; dấu `*` lại nhân từng phần tử. |
| Q4 | **D** | NumPy saves array values, shape and dtype in NPY format. Unlike a plain CSV export, an NPY file retains NumPy-specific information used to reconstruct the array. | NumPy lưu giá trị, shape và dtype ở định dạng NPY. Khác CSV văn bản, tệp NPY giữ thông tin riêng của NumPy để khôi phục đúng mảng. |
| Q5 | **A** | The first dimension counts rows and the second counts columns: (2,3). The `(2,3)` shape has six total cells, whereas `(3,2)` has the row and column counts reversed. | Chiều thứ nhất là số hàng và chiều thứ hai là số cột: (2,3). Shape `(2,3)` có tổng sáu ô; `(3,2)` cũng sáu ô nhưng số hàng và cột đảo vị trí. |
| Q6 | **B** | A transpose swaps row and column dimensions. A `(2,3)` matrix becomes `(3,2)` after `.T` because each original column becomes a row. | Chuyển vị đảo kích thước hàng và cột. Ma trận `(2,3)` trở thành `(3,2)` sau `.T` vì mỗi cột cũ trở thành một hàng. |
| Q7 | **C** | Matching inner dimensions 3 leave outer dimensions 2 and 4. The shared dimension 3 is contracted, while the outer dimensions 2 and 4 remain in the product. | Hai chiều trong cùng bằng 3, còn hai chiều ngoài là 2 và 4. Chiều chung bằng 3 được kết hợp khi nhân, còn hai chiều ngoài 2 và 4 được giữ trong kết quả. |
| Q8 | **D** | A flat six-element array has one dimension of length six. The trailing comma in `(6,)` denotes a one-dimensional shape; `(1,6)` would have two dimensions. | Mảng phẳng sáu phần tử có một chiều độ dài sáu. Dấu phẩy trong `(6,)` biểu diễn shape một chiều; `(1,6)` mới có hai chiều. |
| Q9 | **A** | Reshape and transpose can yield the same shape but different values at positions. For `[[1,2,3],[4,5,6]]`, `reshape(3,2)` groups `[1,2]`, `[3,4]`, `[5,6]`, whereas `.T` groups `[1,4]`, `[2,5]`, `[3,6]`. | reshape và transpose có thể cho cùng shape nhưng giá trị ở vị trí khác. Với `[[1,2,3],[4,5,6]]`, `reshape(3,2)` tạo các hàng `[1,2]`, `[3,4]`, `[5,6]`, còn `.T` cho `[1,4]`, `[2,5]`, `[3,6]`. |
| Q10 | **B** | Star uses broadcasting element-wise, while at follows matrix rules. For two 2×2 arrays of ones, `A * B` stays all ones while `A @ B` contains twos because it sums pairwise products. | Dấu sao nhân theo phần tử, @ tuân quy tắc nhân ma trận. Với hai ma trận 2×2 toàn số một, `A * B` vẫn toàn số một, còn `A @ B` toàn số hai do cộng các tích theo hàng–cột. |
| Q11 | **C** | load restores the stored NumPy array. For a trusted NPY file, `np.load(path)` reconstructs an array; avoid enabling pickle for untrusted object data. | load phục hồi mảng NumPy đã ghi. Với tệp NPY đáng tin cậy, `np.load(path)` khôi phục mảng; tránh bật pickle cho dữ liệu đối tượng chưa tin cậy. |
| Q12 | **D** | tolist converts the in-memory representation without saving a file. A two-dimensional array becomes nested Python lists, while a zero-dimensional array becomes a Python scalar. | tolist chuyển biểu diễn dữ liệu trong bộ nhớ chứ không ghi tệp. Mảng hai chiều chuyển thành List lồng nhau, còn mảng không chiều chuyển thành giá trị vô hướng Python. |
| Q13 | **A** | A 4×2 shape needs eight values, not six. Shape `(4,2)` requires `4 × 2 = 8` cells, so NumPy cannot fit exactly six existing elements into it. | Bảng 4×2 cần tám giá trị, không phải sáu. Shape `(4,2)` cần `4 × 2 = 8` ô, nên NumPy không thể phân bố đúng sáu phần tử hiện có vào shape này. |
| Q14 | **B** | Matrix multiplication contracts the common inner dimension. If `A` is `(m,n)` and `B` is `(n,p)`, multiplication is defined and produces `(m,p)`. | Nhân ma trận yêu cầu hai chiều trong bằng nhau. Nếu `A` là `(m,n)` và `B` là `(n,p)`, phép nhân hợp lệ và trả shape `(m,p)`. |
| Q15 | **C** | Disabling pickle is safer for untrusted numeric data. With `np.load(path, allow_pickle=False)`, an object array requiring pickle cannot be loaded, reducing code-execution risk from untrusted files. | Tắt pickle an toàn hơn khi đọc dữ liệu số chưa tin cậy. Với `np.load(path, allow_pickle=False)`, mảng object cần pickle sẽ không được đọc, giúp giảm rủi ro chạy mã từ tệp không tin cậy. |
| Q16 | **D** | NPY stores NumPy metadata needed to restore the array. Unlike plain-text rows, shape and dtype are serialized so a `(2,3)` numeric array can be reconstructed with its structure. | NPY lưu thông tin để khôi phục cấu trúc và kiểu phần tử. Khác các dòng văn bản thường, shape và dtype được lưu để mảng số `(2,3)` khôi phục đúng cấu trúc. |
| Q17 | **A** | The dot product multiplies matching positions and adds the products. For `[1,2]` and `[3,4]`, the dot product is `1×3 + 2×4 = 11`, a scalar rather than a list. | Tích vô hướng nhân các vị trí tương ứng rồi cộng kết quả. Với `[1,2]` và `[3,4]`, tích vô hướng bằng `1×3 + 2×4 = 11`, là một số đơn chứ không phải List. |
| Q18 | **B** | The identity matrix has ones on its diagonal and zeros elsewhere. Its diagonal is `[1,1,1]`, and its six off-diagonal entries are zero; it is not a matrix of all ones. | Ma trận đơn vị có 1 ở đường chéo và 0 ở vị trí khác. Đường chéo chính là `[1,1,1]`, còn sáu ô ngoài chéo đều bằng không; nó không phải ma trận toàn số một. |
| Q19 | **C** | shape lists the length of each array axis. For a 2-D array with three rows and two columns, `X.shape` is `(3,2)` rather than a data type. | shape liệt kê độ dài của từng trục mảng. Với mảng 2D ba hàng hai cột, `X.shape` là `(3,2)` chứ không phải kiểu dữ liệu. |
| Q20 | **D** | dtype records the stored numeric or other element type. For example, an integer array may report an integer dtype whereas a decimal array reports a floating dtype; `shape` reports dimensions instead. | dtype ghi kiểu số hoặc kiểu dữ liệu khác của phần tử. Ví dụ mảng số nguyên có dtype nguyên, mảng số thập phân có dtype thực; `shape` mới cho kích thước các chiều. |

## 8. Nối bài tiếp theo

`ndarray → Reshape/Transpose → Matrix → Model Input`.

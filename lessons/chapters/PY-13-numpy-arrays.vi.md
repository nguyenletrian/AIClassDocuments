# PY-13 — NumPy ndarray, shape, dtype và axis


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **ndarray** — mảng NumPy; **Shape** — kích thước mảng.

`List → NumPy Array → Matrix → PCA`

Bài này nối trực tiếp kiến thức trước với bước xử lý dữ liệu/AI sau đó. Hãy nắm ý nghĩa dữ liệu trước khi chạy code.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Ý nghĩa |
|---|---|---|
| ndarray | mảng NumPy | Một mảng đồng nhất về kiểu phần tử |
| Shape | kích thước mảng | Số phần tử trên từng chiều |
| dtype | kiểu phần tử | Kiểu dữ liệu của giá trị trong mảng |
| Axis | trục tính toán | Chiều dọc theo phép tổng hợp |

## 3. Thư viện, hàm và tham số

**Từ vựng trong mục:** **Function** — hàm; **Parameter** — tham số.

| Hàm/cú pháp | Giải thích và lý do dùng |
|---|---|
| `np.array(data,dtype=float)` | Tạo mảng số thực, dtype=float cho phép lưu phần thập phân |
| `X.shape/X.ndim/X.size` | Xem hàng/cột, số chiều, số phần tử |
| `X.mean(axis=0)` | Tính trung bình của từng CỘT từ các hàng |
| `np.zeros()/np.ones()` | Tạo dữ liệu số được khởi tạo rõ hình dạng |

Các lựa chọn được giải thích cùng hàm; trong ví dụ code chỉ nhắc lý do thao tác, ý nghĩa hàng/cột và đơn vị đo.

## 4. Khái niệm liên quan

### 4.1. ndarray

**Từ vựng trong mục:** **ndarray** — mảng NumPy.

`ndarray` là mảng NumPy để lưu dữ liệu có kiểu nhất quán và tính trên nhiều phần tử.

```python
import numpy as np
print(np.array([1,2]))
```

**Kết quả khi chạy:**

```text
[1 2]
```

### 4.2. Shape

**Từ vựng trong mục:** **Shape** — kích thước mảng.

`shape` cho biết mảng có bao nhiêu phần tử ở mỗi chiều; `(2, 3)` là hai hàng, ba cột.

```python
import numpy as np
print(np.zeros((2,3)).shape)
```

**Kết quả khi chạy:**

```text
(2, 3)
```

### 4.3. dtype

**Từ vựng trong mục:** **dtype** — kiểu phần tử.

`dtype` cho biết kiểu dữ liệu của các phần tử, ví dụ `float64` thường dùng cho số thập phân.

```python
import numpy as np
print(np.array([1.5]).dtype)
```

**Kết quả khi chạy:**

```text
float64
```

### 4.4. Axis

**Từ vựng trong mục:** **Axis** — trục tính toán.

`axis=0` thường tính theo cột trong mảng hai chiều, `axis=1` thường tính theo từng hàng.

```python
import numpy as np
print(np.array([[1,2],[3,4]]).sum(axis=0))
```

**Kết quả khi chạy:**

```text
[4 6]
```

## 5. Năm tình huống lập trình thực tế

### Tình huống 1 — Gom điểm học sinh

**Từ vựng trong mục:** **ndarray** — mảng NumPy.

**Tình huống thực tế:** Trung tâm có điểm hai môn của ba học viên lần lượt là (8,9), (6,7), (9,8). Xác định bảng có bao nhiêu hàng và cột.

**Vì sao chọn cách giải này?** `np.array` ghép mỗi học viên thành một hàng, hai môn là hai cột.

**Quy trình giải:** Lưu dữ liệu đúng thứ tự hàng/cột → dùng phép NumPy phù hợp → in và giải thích kết quả.

```python
import numpy as np
scores=np.array([[8,9],[6,7],[9,8]],dtype=float)
print(scores.shape)
```

**Kết quả khi chạy:**

```text
(3, 2)
```

### Tình huống 2 — Trung bình từng môn

**Từ vựng trong mục:** **Shape** — kích thước mảng.

**Tình huống thực tế:** Với bảng điểm ba học viên hai môn (8,9), (6,7), (9,8), trung tâm cần trung bình mỗi môn. Tính hai điểm trung bình theo cột.

**Vì sao chọn cách giải này?** `mean(axis=0)` lấy trung bình của từng môn qua các học viên.

**Quy trình giải:** Lưu dữ liệu đúng thứ tự hàng/cột → dùng phép NumPy phù hợp → in và giải thích kết quả.

```python
import numpy as np
scores=np.array([[8,9],[6,7],[9,8]],dtype=float)
print(scores.mean(axis=0))
```

**Kết quả khi chạy:**

```text
[7.66666667 8.        ]
```

### Tình huống 3 — Tính tổng doanh thu theo cửa hàng

**Từ vựng trong mục:** **dtype** — kiểu phần tử.

**Tình huống thực tế:** Hai cửa hàng có doanh thu ba ngày: cửa hàng A `[10,20,30]`, cửa hàng B `[8,12,16]` (triệu đồng). Tính tổng doanh thu của mỗi cửa hàng.

**Vì sao chọn cách giải này?** Mỗi hàng là một cửa hàng nên `sum(axis=1)` tính theo hàng.

**Quy trình giải:** Lưu dữ liệu đúng thứ tự hàng/cột → dùng phép NumPy phù hợp → in và giải thích kết quả.

```python
import numpy as np
sales=np.array([[10,20,30],[8,12,16]])
print(sales.sum(axis=1))
```

**Kết quả khi chạy:**

```text
[60 36]
```

### Tình huống 4 — Tạo bảng dự báo ban đầu

**Từ vựng trong mục:** **Axis** — trục tính toán.

**Tình huống thực tế:** Đội phân tích cần khởi tạo bảng dự báo rỗng cho hai cửa hàng, mỗi cửa hàng có ba ngày. Tạo bảng ban đầu toàn số 0 và in số hàng/cột.

**Vì sao chọn cách giải này?** `zeros((2,3))` tạo mảng hai hàng ba cột với giá trị khởi tạo bằng 0.

**Quy trình giải:** Lưu dữ liệu đúng thứ tự hàng/cột → dùng phép NumPy phù hợp → in và giải thích kết quả.

```python
import numpy as np
forecast=np.zeros((2,3))
print(forecast.shape)
```

**Kết quả khi chạy:**

```text
(2, 3)
```

### Tình huống 5 — Kiểm kiểu điểm đầu vào

**Từ vựng trong mục:** **ndarray** — mảng NumPy.

**Tình huống thực tế:** Trung tâm có hai điểm kiểm tra 7.5 và 8.0 trên thang 10. Kiểm tra kiểu dữ liệu và số lượng điểm.

**Vì sao chọn cách giải này?** Đặt `dtype=float` giữ điểm thập phân; `size` đếm số phần tử.

**Quy trình giải:** Lưu dữ liệu đúng thứ tự hàng/cột → dùng phép NumPy phù hợp → in và giải thích kết quả.

```python
import numpy as np
scores=np.array([7.5,8],dtype=float)
print(scores.dtype,scores.size)
```

**Kết quả khi chạy:**

```text
float64 2
```

## 6. Sai lầm thường gặp

- Không dùng đầu ra mẫu để suy diễn về người thật, hàng hóa thật hoặc kết quả dự đoán AI.
- Cần chú ý thứ tự xử lý, kiểu dữ liệu và đơn vị đo. Trường hợp rỗng/thiếu dữ liệu phải có cách xử lý rõ ràng.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.


**Q1. Which description matches ndarray? — Mô tả nào đúng với ndarray?**

A. A different concept described as Số phần tử trên từng chiều — Số phần tử trên từng chiều

B. The concept described as Một mảng đồng nhất về kiểu phần tử — Một mảng đồng nhất về kiểu phần tử

C. A different concept described as Kiểu dữ liệu của giá trị trong mảng — Kiểu dữ liệu của giá trị trong mảng

D. A different concept described as Chiều dọc theo phép tổng hợp — Chiều dọc theo phép tổng hợp


**Q2. Which description matches Shape? — Mô tả nào đúng với Shape?**

A. The concept described as Số phần tử trên từng chiều — Số phần tử trên từng chiều

B. A different concept described as Kiểu dữ liệu của giá trị trong mảng — Kiểu dữ liệu của giá trị trong mảng

C. A different concept described as Chiều dọc theo phép tổng hợp — Chiều dọc theo phép tổng hợp

D. A different concept described as Một mảng đồng nhất về kiểu phần tử — Một mảng đồng nhất về kiểu phần tử


**Q3. Which description matches dtype? — Mô tả nào đúng với dtype?**

A. A different concept described as Chiều dọc theo phép tổng hợp — Chiều dọc theo phép tổng hợp

B. A different concept described as Một mảng đồng nhất về kiểu phần tử — Một mảng đồng nhất về kiểu phần tử

C. A different concept described as Số phần tử trên từng chiều — Số phần tử trên từng chiều

D. The concept described as Kiểu dữ liệu của giá trị trong mảng — Kiểu dữ liệu của giá trị trong mảng


**Q4. Which description matches Axis? — Mô tả nào đúng với Axis?**

A. A different concept described as Một mảng đồng nhất về kiểu phần tử — Một mảng đồng nhất về kiểu phần tử

B. A different concept described as Số phần tử trên từng chiều — Số phần tử trên từng chiều

C. The concept described as Chiều dọc theo phép tổng hợp — Chiều dọc theo phép tổng hợp

D. A different concept described as Kiểu dữ liệu của giá trị trong mảng — Kiểu dữ liệu của giá trị trong mảng


**Q5. Which use matches np.array(data,dtype=float)? — Công dụng nào đúng với np.array(data,dtype=float)?**

A. Use a different operation to Xem hàng/cột, số chiều, số phần tử — Xem hàng/cột, số chiều, số phần tử

B. Use this syntax to Tạo mảng số thực, dtype=float cho phép lưu phần thập phân — Tạo mảng số thực, dtype=float cho phép lưu phần thập phân

C. Use a different operation to Tính trung bình của từng CỘT từ các hàng — Tính trung bình của từng CỘT từ các hàng

D. Use a different operation to Tạo dữ liệu số được khởi tạo rõ hình dạng — Tạo dữ liệu số được khởi tạo rõ hình dạng


**Q6. Which use matches X.shape/X.ndim/X.size? — Công dụng nào đúng với X.shape/X.ndim/X.size?**

A. Use this syntax to Xem hàng/cột, số chiều, số phần tử — Xem hàng/cột, số chiều, số phần tử

B. Use a different operation to Tính trung bình của từng CỘT từ các hàng — Tính trung bình của từng CỘT từ các hàng

C. Use a different operation to Tạo dữ liệu số được khởi tạo rõ hình dạng — Tạo dữ liệu số được khởi tạo rõ hình dạng

D. Use a different operation to Tạo mảng số thực, dtype=float cho phép lưu phần thập phân — Tạo mảng số thực, dtype=float cho phép lưu phần thập phân


**Q7. Which use matches X.mean(axis=0)? — Công dụng nào đúng với X.mean(axis=0)?**

A. Use a different operation to Tạo dữ liệu số được khởi tạo rõ hình dạng — Tạo dữ liệu số được khởi tạo rõ hình dạng

B. Use a different operation to Tạo mảng số thực, dtype=float cho phép lưu phần thập phân — Tạo mảng số thực, dtype=float cho phép lưu phần thập phân

C. Use a different operation to Xem hàng/cột, số chiều, số phần tử — Xem hàng/cột, số chiều, số phần tử

D. Use this syntax to Tính trung bình của từng CỘT từ các hàng — Tính trung bình của từng CỘT từ các hàng


**Q8. Which use matches np.zeros()/np.ones()? — Công dụng nào đúng với np.zeros()/np.ones()?**

A. Use a different operation to Tạo mảng số thực, dtype=float cho phép lưu phần thập phân — Tạo mảng số thực, dtype=float cho phép lưu phần thập phân

B. Use a different operation to Xem hàng/cột, số chiều, số phần tử — Xem hàng/cột, số chiều, số phần tử

C. Use this syntax to Tạo dữ liệu số được khởi tạo rõ hình dạng — Tạo dữ liệu số được khởi tạo rõ hình dạng

D. Use a different operation to Tính trung bình của từng CỘT từ các hàng — Tính trung bình của từng CỘT từ các hàng


**Q9. What solves scenario 1? — Cách nào giải quyết tình huống 1?**

A. Another method is chosen because axis=0 cho phép tính trung bình theo cột môn học — axis=0 cho phép tính trung bình theo cột môn học

B. Choose the method because Dùng ma trận một hàng mỗi SV và cột mỗi môn — Dùng ma trận một hàng mỗi SV và cột mỗi môn

C. Another method is chosen because axis=1 gom giá trị theo từng HÀNG/cửa hàng — axis=1 gom giá trị theo từng HÀNG/cửa hàng

D. Another method is chosen because zeros cấp đúng kích thước chờ ghi kết quả — zeros cấp đúng kích thước chờ ghi kết quả


**Q10. What solves scenario 2? — Cách nào giải quyết tình huống 2?**

A. Choose the method because axis=0 cho phép tính trung bình theo cột môn học — axis=0 cho phép tính trung bình theo cột môn học

B. Another method is chosen because axis=1 gom giá trị theo từng HÀNG/cửa hàng — axis=1 gom giá trị theo từng HÀNG/cửa hàng

C. Another method is chosen because zeros cấp đúng kích thước chờ ghi kết quả — zeros cấp đúng kích thước chờ ghi kết quả

D. Another method is chosen because Mảng float giữ điểm có phần thập phân — Mảng float giữ điểm có phần thập phân


**Q11. What solves scenario 3? — Cách nào giải quyết tình huống 3?**

A. Another method is chosen because zeros cấp đúng kích thước chờ ghi kết quả — zeros cấp đúng kích thước chờ ghi kết quả

B. Another method is chosen because Mảng float giữ điểm có phần thập phân — Mảng float giữ điểm có phần thập phân

C. Another method is chosen because Dùng ma trận một hàng mỗi SV và cột mỗi môn — Dùng ma trận một hàng mỗi SV và cột mỗi môn

D. Choose the method because axis=1 gom giá trị theo từng HÀNG/cửa hàng — axis=1 gom giá trị theo từng HÀNG/cửa hàng


**Q12. What solves scenario 4? — Cách nào giải quyết tình huống 4?**

A. Another method is chosen because Mảng float giữ điểm có phần thập phân — Mảng float giữ điểm có phần thập phân

B. Another method is chosen because Dùng ma trận một hàng mỗi SV và cột mỗi môn — Dùng ma trận một hàng mỗi SV và cột mỗi môn

C. Choose the method because zeros cấp đúng kích thước chờ ghi kết quả — zeros cấp đúng kích thước chờ ghi kết quả

D. Another method is chosen because axis=0 cho phép tính trung bình theo cột môn học — axis=0 cho phép tính trung bình theo cột môn học


**Q13. What solves scenario 5? — Cách nào giải quyết tình huống 5?**

A. Another method is chosen because Dùng ma trận một hàng mỗi SV và cột mỗi môn — Dùng ma trận một hàng mỗi SV và cột mỗi môn

B. Choose the method because Mảng float giữ điểm có phần thập phân — Mảng float giữ điểm có phần thập phân

C. Another method is chosen because axis=0 cho phép tính trung bình theo cột môn học — axis=0 cho phép tính trung bình theo cột môn học

D. Another method is chosen because axis=1 gom giá trị theo từng HÀNG/cửa hàng — axis=1 gom giá trị theo từng HÀNG/cửa hàng


**Q14. Which data is used in scenario 1? — Tình huống 1 dùng dữ liệu nào?**

A. The described input 3 học sinh × 2 môn, điểm thang 10 — 3 học sinh × 2 môn, điểm thang 10

B. Another input 3 học sinh, 2 môn — 3 học sinh, 2 môn

C. Another input 2 cửa hàng × 3 ngày, đơn vị nghìn đồng — 2 cửa hàng × 3 ngày, đơn vị nghìn đồng

D. Another input 2 ngày × 3 kênh cảm biến — 2 ngày × 3 kênh cảm biến


**Q15. Which data is used in scenario 2? — Tình huống 2 dùng dữ liệu nào?**

A. Another input 2 cửa hàng × 3 ngày, đơn vị nghìn đồng — 2 cửa hàng × 3 ngày, đơn vị nghìn đồng

B. Another input 2 ngày × 3 kênh cảm biến — 2 ngày × 3 kênh cảm biến

C. Another input Điểm 7.5, 8.0 — Điểm 7.5, 8.0

D. The described input 3 học sinh, 2 môn — 3 học sinh, 2 môn


**Q16. Which data is used in scenario 3? — Tình huống 3 dùng dữ liệu nào?**

A. Another input 2 ngày × 3 kênh cảm biến — 2 ngày × 3 kênh cảm biến

B. Another input Điểm 7.5, 8.0 — Điểm 7.5, 8.0

C. The described input 2 cửa hàng × 3 ngày, đơn vị nghìn đồng — 2 cửa hàng × 3 ngày, đơn vị nghìn đồng

D. Another input 3 học sinh × 2 môn, điểm thang 10 — 3 học sinh × 2 môn, điểm thang 10


**Q17. Which data is used in scenario 4? — Tình huống 4 dùng dữ liệu nào?**

A. Another input Điểm 7.5, 8.0 — Điểm 7.5, 8.0

B. The described input 2 ngày × 3 kênh cảm biến — 2 ngày × 3 kênh cảm biến

C. Another input 3 học sinh × 2 môn, điểm thang 10 — 3 học sinh × 2 môn, điểm thang 10

D. Another input 3 học sinh, 2 môn — 3 học sinh, 2 môn


**Q18. Which data is used in scenario 5? — Tình huống 5 dùng dữ liệu nào?**

A. The described input Điểm 7.5, 8.0 — Điểm 7.5, 8.0

B. Another input 3 học sinh × 2 môn, điểm thang 10 — 3 học sinh × 2 môn, điểm thang 10

C. Another input 3 học sinh, 2 môn — 3 học sinh, 2 môn

D. Another input 2 cửa hàng × 3 ngày, đơn vị nghìn đồng — 2 cửa hàng × 3 ngày, đơn vị nghìn đồng


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
| Q1 | **B** | The concept described as Một mảng đồng nhất về kiểu phần tử | Một mảng đồng nhất về kiểu phần tử |
| Q2 | **A** | The concept described as Số phần tử trên từng chiều | Số phần tử trên từng chiều |
| Q3 | **D** | The concept described as Kiểu dữ liệu của giá trị trong mảng | Kiểu dữ liệu của giá trị trong mảng |
| Q4 | **C** | The concept described as Chiều dọc theo phép tổng hợp | Chiều dọc theo phép tổng hợp |
| Q5 | **B** | Use this syntax to Tạo mảng số thực, dtype=float cho phép lưu phần thập phân | Tạo mảng số thực, dtype=float cho phép lưu phần thập phân |
| Q6 | **A** | Use this syntax to Xem hàng/cột, số chiều, số phần tử | Xem hàng/cột, số chiều, số phần tử |
| Q7 | **D** | Use this syntax to Tính trung bình của từng CỘT từ các hàng | Tính trung bình của từng CỘT từ các hàng |
| Q8 | **C** | Use this syntax to Tạo dữ liệu số được khởi tạo rõ hình dạng | Tạo dữ liệu số được khởi tạo rõ hình dạng |
| Q9 | **B** | Choose the method because Dùng ma trận một hàng mỗi SV và cột mỗi môn | Dùng ma trận một hàng mỗi SV và cột mỗi môn |
| Q10 | **A** | Choose the method because axis=0 cho phép tính trung bình theo cột môn học | axis=0 cho phép tính trung bình theo cột môn học |
| Q11 | **D** | Choose the method because axis=1 gom giá trị theo từng HÀNG/cửa hàng | axis=1 gom giá trị theo từng HÀNG/cửa hàng |
| Q12 | **C** | Choose the method because zeros cấp đúng kích thước chờ ghi kết quả | zeros cấp đúng kích thước chờ ghi kết quả |
| Q13 | **B** | Choose the method because Mảng float giữ điểm có phần thập phân | Mảng float giữ điểm có phần thập phân |
| Q14 | **A** | The described input 3 học sinh × 2 môn, điểm thang 10 | 3 học sinh × 2 môn, điểm thang 10 |
| Q15 | **D** | The described input 3 học sinh, 2 môn | 3 học sinh, 2 môn |
| Q16 | **C** | The described input 2 cửa hàng × 3 ngày, đơn vị nghìn đồng | 2 cửa hàng × 3 ngày, đơn vị nghìn đồng |
| Q17 | **B** | The described input 2 ngày × 3 kênh cảm biến | 2 ngày × 3 kênh cảm biến |
| Q18 | **A** | The described input Điểm 7.5, 8.0 | Điểm 7.5, 8.0 |
| Q19 | **D** | Input meaning and units | Ý nghĩa và đơn vị dữ liệu |
| Q20 | **C** | Verify output and unusual inputs | Kiểm tra đầu ra và giá trị biên |

## 8. Nối sang bài tiếp theo

`List → NumPy Array → Matrix → PCA`.

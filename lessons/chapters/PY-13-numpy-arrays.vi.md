# PY-13 — NumPy ndarray, shape, dtype và axis


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **ndarray** — mảng NumPy; **Shape** — kích thước mảng.

`List → NumPy Array → Matrix → PCA`

Sau List, ta chuyển sang NumPy để xử lý nhiều điểm hoặc số đo trong một mảng. Bài này giải thích cách đọc hàng, cột, kích thước, kiểu phần tử và trục tính toán trước khi dùng các phép xử lý dữ liệu cho AI.

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

## 4. Khái niệm liên quan

**NumPy ndarray** là công cụ lưu số liệu có cấu trúc. Một bảng có 3 học viên × 2 môn sẽ xuyên suốt phần khái niệm: từ tạo bảng, xem kích thước, hiểu kiểu phần tử cho tới tính toán theo cột. Nhờ giữ nguyên ý nghĩa hàng và cột, kết quả thống kê sẽ không bị hiểu nhầm.

### 4.1. ndarray — Mảng số cho nhiều học viên

**Từ vựng trong mục:** **ndarray** — mảng NumPy; **Element** — phần tử.

**NumPy** là thư viện hỗ trợ tính toán trên nhiều số cùng lúc. Kiểu dữ liệu chính là `ndarray` — một **mảng nhiều chiều**. Ví dụ trung tâm có ba học viên An, Bình, Lan (theo thứ tự ba hàng) và hai môn Toán, Python (theo thứ tự hai cột). Các điểm `[8,9]`, `[6,7]`, `[9,8]` nằm cùng một bảng. **Mỗi hàng** là một người, **mỗi cột** là một môn, **mỗi ô** là điểm của người đó ở môn đó trên thang 10.

```python
import numpy as np

scores = np.array([
    [8, 9],
    [6, 7],
    [9, 8],
])
print(scores)
```

**Kết quả khi chạy:**

```text
[[8 9]
 [6 7]
 [9 8]]
```

Hàng đầu là điểm của An, hàng thứ hai của Bình, hàng thứ ba của Lan; hai số trên một hàng lần lượt thuộc hai môn.

### 4.2. Shape — Kích thước của mảng

**Từ vựng trong mục:** **Shape** — kích thước; **Row/column** — hàng/cột.

Thuộc tính `shape` cho biết **số phần tử ở từng chiều** của mảng. Với bảng điểm ba học viên, hai môn, `shape == (3, 2)`: con số 3 là **số hàng/học viên**, con số 2 là **số cột/môn**. Thuộc tính `size` là số ô dữ liệu (3 × 2 = 6), còn `ndim` là số chiều (2). Không nhầm mảng `(3,2)` với ba môn của hai học viên.

```python
import numpy as np

scores = np.array([[8, 9], [6, 7], [9, 8]])
print(scores.shape, scores.size)
```

**Kết quả khi chạy:**

```text
(3, 2) 6
```

Bảng có 3 người × 2 môn = 6 giá trị điểm; đây là mảng hai chiều.

### 4.3. dtype — Kiểu của các phần tử

**Từ vựng trong mục:** **dtype** — kiểu dữ liệu phần tử; **Float** — số thực.

Một `ndarray` thông thường lưu các phần tử bằng một kiểu dữ liệu chung (`dtype`). Với điểm có phần thập phân như 8,5, ta dùng `dtype=float` khi tạo mảng để giữ phần lẻ và thuận tiện tính trung bình. NumPy trên môi trường thông dụng dùng `float64` cho lựa chọn `float`. Ngược lại, nếu ép điểm thập phân thành số nguyên, phần lẻ có thể mất.

```python
import numpy as np

scores = np.array([8.5, 7.0], dtype=float)
print(scores.dtype, scores.size)
```

**Kết quả khi chạy:**

```text
float64 2
```

Mảng có hai điểm dạng số thực; `8.5` được giữ chứ không bị cắt thành `8`.

### 4.4. Axis — Tính theo hàng hoặc cột

**Từ vựng trong mục:** **Axis** — trục tính toán; **Mean** — trung bình.

Khi tổng hợp dữ liệu hai chiều, **`axis=0` gom các hàng để cho ra một kết quả trên mỗi cột**; **`axis=1` gom các cột để cho ra một kết quả trên mỗi hàng**. Trong bảng ba học viên × hai môn, `scores.mean(axis=0)` tính điểm trung bình **từng môn**: môn Toán `(8+6+9)/3 ≈ 7,67`, môn Python `(9+7+8)/3 = 8`. Nếu đổi sang `axis=1`, sẽ ra ba điểm trung bình tương ứng ba học viên.

```python
import numpy as np

scores = np.array([[8, 9], [6, 7], [9, 8]], dtype=float)
print(scores.mean(axis=0))
```

**Kết quả khi chạy:**

```text
[7.66666667 8.        ]
```

Mảng đầu ra có hai số vì bảng có hai **cột/môn**; kết quả lần lượt là trung bình Toán và Python.

## 5. Năm tình huống lập trình thực tế

### Tình huống 1 — Gom bảng điểm học viên

**Từ vựng trong mục:** **ndarray** — mảng NumPy; **Shape** — kích thước.

**Tình huống thực tế:** Trung tâm ghi điểm hai môn Toán và Python của ba học viên theo thứ tự An (8,9), Bình (6,7), Lan (9,8), thang điểm 10. Hãy tạo mảng và in số hàng, số cột.

**Vì sao chọn cách giải này?** `np.array` gom điểm thành bảng, `shape` cho biết đúng 3 học viên và 2 môn.

**Quy trình giải:**

1. Tạo mảng hai chiều, mỗi hàng ứng với một học viên.
2. Giữ thứ tự cột Toán rồi Python.
3. In `scores.shape` để xác minh số người và môn.

```python
import numpy as np

scores = np.array([[8, 9], [6, 7], [9, 8]], dtype=float)
print(scores.shape)
```

**Kết quả khi chạy:**

```text
(3, 2)
```

Kết quả cho biết 3 hàng học viên và 2 cột môn học.

### Tình huống 2 — Trung bình theo từng môn

**Từ vựng trong mục:** **Axis** — trục tính toán; **Mean** — trung bình.

**Tình huống thực tế:** Với cùng bảng ba học viên, hai môn Toán và Python, trung tâm cần điểm trung bình của **mỗi môn** trên thang 10. Hãy in hai số trung bình theo thứ tự cột.

**Vì sao chọn cách giải này?** `mean(axis=0)` gom các học viên cùng cột môn và tính trung bình.

**Quy trình giải:**

1. Tạo mảng 3 hàng × 2 cột theo thứ tự Toán, Python.
2. Tính `scores.mean(axis=0)`.
3. Đối chiếu hai số với phép tính trung bình ở từng cột.

```python
import numpy as np

scores = np.array([[8, 9], [6, 7], [9, 8]], dtype=float)
print(scores.mean(axis=0))
```

**Kết quả khi chạy:**

```text
[7.66666667 8.        ]
```

Toán trung bình khoảng 7,67; Python trung bình 8,00 điểm.

### Tình huống 3 — Tính tổng doanh thu mỗi cửa hàng

**Từ vựng trong mục:** **Axis** — trục tính toán; **Sum** — phép cộng tổng.

**Tình huống thực tế:** Cửa hàng A có doanh thu ba ngày `[10,20,30]`, cửa hàng B có `[8,12,16]`, đơn vị triệu đồng. Bảng có **hai hàng cửa hàng** và **ba cột ngày**. Hãy tính tổng doanh thu riêng của từng cửa hàng.

**Vì sao chọn cách giải này?** Vì cửa hàng nằm trên hàng, `sum(axis=1)` cộng ba cột ngày cho mỗi hàng.

**Quy trình giải:**

1. Tạo `sales` với hàng đầu là cửa hàng A và hàng sau là B.
2. Cộng theo `axis=1`, tức theo từng hàng.
3. In hai tổng theo thứ tự A rồi B.

```python
import numpy as np

sales = np.array([[10, 20, 30], [8, 12, 16]])
print(sales.sum(axis=1))
```

**Kết quả khi chạy:**

```text
[60 36]
```

Cửa hàng A thu 60 triệu đồng; cửa hàng B thu 36 triệu đồng.

### Tình huống 4 — Tạo bảng dự báo khởi tạo

**Từ vựng trong mục:** **Shape** — kích thước; **Zero array** — mảng số 0.

**Tình huống thực tế:** Đội phân tích chuẩn bị một bảng dự báo cho 2 cửa hàng và 3 ngày, chưa tính giá trị. Hãy tạo mảng toàn số 0 và in hình dạng bảng.

**Vì sao chọn cách giải này?** `np.zeros((2, 3))` khởi tạo đúng số hàng cửa hàng và số cột ngày; số 0 mới là giá trị ban đầu, không phải doanh thu dự báo đã xác minh.

**Quy trình giải:**

1. Gọi `np.zeros` với hình dạng `(2, 3)`.
2. Mỗi hàng dành cho một cửa hàng, mỗi cột dành cho một ngày.
3. In `forecast.shape` để kiểm tra cấu trúc.

```python
import numpy as np

forecast = np.zeros((2, 3))
print(forecast.shape)
```

**Kết quả khi chạy:**

```text
(2, 3)
```

Bảng dành cho hai cửa hàng, ba ngày, tổng cộng sáu vị trí chưa có dự báo thực.

### Tình huống 5 — Kiểm tra kiểu và số lượng điểm

**Từ vựng trong mục:** **dtype** — kiểu phần tử; **size** — số phần tử.

**Tình huống thực tế:** Trung tâm nhập hai điểm kiểm tra 7,5 và 8,0 của một học viên. Hãy dùng mảng số thực để giữ phần thập phân rồi in kiểu và số lượng điểm.

**Vì sao chọn cách giải này?** `dtype=float` tránh mất phần thập phân; `size` đếm đúng hai số được lưu.

**Quy trình giải:**

1. Tạo mảng chứa `7.5` và `8.0` với `dtype=float`.
2. Truy cập thuộc tính `dtype` và `size`.
3. In tên kiểu và số phần tử.

```python
import numpy as np

scores = np.array([7.5, 8.0], dtype=float)
print(scores.dtype, scores.size)
```

**Kết quả khi chạy:**

```text
float64 2
```

Dữ liệu gồm hai điểm kiểu `float64`, không phải chuỗi.

## 6. Sai lầm thường gặp

- `shape=(3,2)` là **3 hàng và 2 cột**, không phải ngược lại; phải ghi rõ mỗi hàng/cột đại diện điều gì.
- `axis=0` tổng hợp theo từng cột trong mảng hai chiều; `axis=1` tổng hợp theo từng hàng. Chọn nhầm trục khiến ý nghĩa kết quả khác đi.
- `dtype=float` giữ phần thập phân, còn kiểu số nguyên có thể cắt phần lẻ nếu ép dữ liệu không phù hợp.
- Kết quả trung bình là số thực; các chữ số cuối có thể phụ thuộc biểu diễn dấu phẩy động, nên giải thích bằng giá trị gần đúng khi cần.
- `np.zeros()` chỉ tạo giá trị khởi tạo 0; không được diễn giải là dự báo thực tế đã được mô hình tính.

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

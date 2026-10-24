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
values=np.array([20,21,22,23,24,25])
print(values.reshape(2,3))
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
scores=np.array([[8,7,9],[6,5,8]])
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
scores=np.array([8,7,9])
w=np.array([.2,.3,.5])
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
X=np.array([[8,7,9],[6,5,8]])
W=np.array([[.5,0],[.5,.5],[0,.5]])
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
    p=Path(folder)/"data.npy"
    np.save(p,np.array([3,5,7]))
    print(np.load(p,allow_pickle=False))
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


**Q1. What does Reshape mean? — Ý nghĩa của Reshape là gì?**

A. It instead describes Đổi trục hàng và cột — Đổi trục hàng và cột

B. The concept is Đổi shape nhưng giữ số phần tử — Đổi shape nhưng giữ số phần tử

C. It instead describes Tạo kết quả bằng phép nhân tuyến tính — Tạo kết quả bằng phép nhân tuyến tính

D. It instead describes Ghi mảng vào tệp để đọc lại — Ghi mảng vào tệp để đọc lại


**Q2. What does Transpose mean? — Ý nghĩa của Transpose là gì?**

A. The concept is Đổi trục hàng và cột — Đổi trục hàng và cột

B. It instead describes Tạo kết quả bằng phép nhân tuyến tính — Tạo kết quả bằng phép nhân tuyến tính

C. It instead describes Ghi mảng vào tệp để đọc lại — Ghi mảng vào tệp để đọc lại

D. It instead describes Đổi shape nhưng giữ số phần tử — Đổi shape nhưng giữ số phần tử


**Q3. What does Matrix multiply mean? — Ý nghĩa của Matrix multiply là gì?**

A. It instead describes Ghi mảng vào tệp để đọc lại — Ghi mảng vào tệp để đọc lại

B. It instead describes Đổi shape nhưng giữ số phần tử — Đổi shape nhưng giữ số phần tử

C. It instead describes Đổi trục hàng và cột — Đổi trục hàng và cột

D. The concept is Tạo kết quả bằng phép nhân tuyến tính — Tạo kết quả bằng phép nhân tuyến tính


**Q4. What does Serialization mean? — Ý nghĩa của Serialization là gì?**

A. It instead describes Đổi shape nhưng giữ số phần tử — Đổi shape nhưng giữ số phần tử

B. It instead describes Đổi trục hàng và cột — Đổi trục hàng và cột

C. The concept is Ghi mảng vào tệp để đọc lại — Ghi mảng vào tệp để đọc lại

D. It instead describes Tạo kết quả bằng phép nhân tuyến tính — Tạo kết quả bằng phép nhân tuyến tính


**Q5. What is the role of reshape(rows,cols)? — Vai trò của reshape(rows,cols) là gì?**

A. Another operation would Đổi trục từ hàng thành cột — Đổi trục từ hàng thành cột

B. It is used to Số phần tử trước/sau phải bằng nhau — Số phần tử trước/sau phải bằng nhau

C. Another operation would Nhân tuyến tính yêu cầu kích thước tương thích — Nhân tuyến tính yêu cầu kích thước tương thích

D. Another operation would Lưu và đọc định dạng NPY, chỉ tải từ nguồn tin cậy — Lưu và đọc định dạng NPY, chỉ tải từ nguồn tin cậy


**Q6. What is the role of X.T / np.transpose(X)? — Vai trò của X.T / np.transpose(X) là gì?**

A. It is used to Đổi trục từ hàng thành cột — Đổi trục từ hàng thành cột

B. Another operation would Nhân tuyến tính yêu cầu kích thước tương thích — Nhân tuyến tính yêu cầu kích thước tương thích

C. Another operation would Lưu và đọc định dạng NPY, chỉ tải từ nguồn tin cậy — Lưu và đọc định dạng NPY, chỉ tải từ nguồn tin cậy

D. Another operation would Số phần tử trước/sau phải bằng nhau — Số phần tử trước/sau phải bằng nhau


**Q7. What is the role of A @ B / np.dot(A,B)? — Vai trò của A @ B / np.dot(A,B) là gì?**

A. Another operation would Lưu và đọc định dạng NPY, chỉ tải từ nguồn tin cậy — Lưu và đọc định dạng NPY, chỉ tải từ nguồn tin cậy

B. Another operation would Số phần tử trước/sau phải bằng nhau — Số phần tử trước/sau phải bằng nhau

C. Another operation would Đổi trục từ hàng thành cột — Đổi trục từ hàng thành cột

D. It is used to Nhân tuyến tính yêu cầu kích thước tương thích — Nhân tuyến tính yêu cầu kích thước tương thích


**Q8. What is the role of np.save()/np.load()? — Vai trò của np.save()/np.load() là gì?**

A. Another operation would Số phần tử trước/sau phải bằng nhau — Số phần tử trước/sau phải bằng nhau

B. Another operation would Đổi trục từ hàng thành cột — Đổi trục từ hàng thành cột

C. It is used to Lưu và đọc định dạng NPY, chỉ tải từ nguồn tin cậy — Lưu và đọc định dạng NPY, chỉ tải từ nguồn tin cậy

D. Another operation would Nhân tuyến tính yêu cầu kích thước tương thích — Nhân tuyến tính yêu cầu kích thước tương thích


**Q9. Which reason fits example 1? — Lý do nào phù hợp ví dụ 1?**

A. Transpose làm môn thành hàng, học sinh thành cột — Transpose làm môn thành hàng, học sinh thành cột

B. reshape đổi 6 giá trị thành 2 ngày × 3 giờ — reshape đổi 6 giá trị thành 2 ngày × 3 giờ

C. Nhân vector điểm với vector trọng số — Nhân vector điểm với vector trọng số

D. Nhân matrix học sinh × matrix trọng số — Nhân matrix học sinh × matrix trọng số


**Q10. Which reason fits example 2? — Lý do nào phù hợp ví dụ 2?**

A. Transpose làm môn thành hàng, học sinh thành cột — Transpose làm môn thành hàng, học sinh thành cột

B. Nhân vector điểm với vector trọng số — Nhân vector điểm với vector trọng số

C. Nhân matrix học sinh × matrix trọng số — Nhân matrix học sinh × matrix trọng số

D. Lưu trong thư mục tạm và load chỉ từ dữ liệu tự tạo — Lưu trong thư mục tạm và load chỉ từ dữ liệu tự tạo


**Q11. Which reason fits example 3? — Lý do nào phù hợp ví dụ 3?**

A. Nhân matrix học sinh × matrix trọng số — Nhân matrix học sinh × matrix trọng số

B. Lưu trong thư mục tạm và load chỉ từ dữ liệu tự tạo — Lưu trong thư mục tạm và load chỉ từ dữ liệu tự tạo

C. reshape đổi 6 giá trị thành 2 ngày × 3 giờ — reshape đổi 6 giá trị thành 2 ngày × 3 giờ

D. Nhân vector điểm với vector trọng số — Nhân vector điểm với vector trọng số


**Q12. Which reason fits example 4? — Lý do nào phù hợp ví dụ 4?**

A. Lưu trong thư mục tạm và load chỉ từ dữ liệu tự tạo — Lưu trong thư mục tạm và load chỉ từ dữ liệu tự tạo

B. reshape đổi 6 giá trị thành 2 ngày × 3 giờ — reshape đổi 6 giá trị thành 2 ngày × 3 giờ

C. Nhân matrix học sinh × matrix trọng số — Nhân matrix học sinh × matrix trọng số

D. Transpose làm môn thành hàng, học sinh thành cột — Transpose làm môn thành hàng, học sinh thành cột


**Q13. Which reason fits example 5? — Lý do nào phù hợp ví dụ 5?**

A. reshape đổi 6 giá trị thành 2 ngày × 3 giờ — reshape đổi 6 giá trị thành 2 ngày × 3 giờ

B. Lưu trong thư mục tạm và load chỉ từ dữ liệu tự tạo — Lưu trong thư mục tạm và load chỉ từ dữ liệu tự tạo

C. Transpose làm môn thành hàng, học sinh thành cột — Transpose làm môn thành hàng, học sinh thành cột

D. Nhân vector điểm với vector trọng số — Nhân vector điểm với vector trọng số


**Q14. Which input matches example 1? — Dữ liệu nào phù hợp ví dụ 1?**

A. The stated data are 6 số đo nhiệt độ giờ — 6 số đo nhiệt độ giờ

B. Other data: 2 SV × 3 môn — 2 SV × 3 môn

C. Other data: 3 môn, trọng số cộng bằng 1 — 3 môn, trọng số cộng bằng 1

D. Other data: 2 SV × 3 môn, tạo 2 đặc trưng — 2 SV × 3 môn, tạo 2 đặc trưng


**Q15. Which input matches example 2? — Dữ liệu nào phù hợp ví dụ 2?**

A. Other data: 3 môn, trọng số cộng bằng 1 — 3 môn, trọng số cộng bằng 1

B. Other data: 2 SV × 3 môn, tạo 2 đặc trưng — 2 SV × 3 môn, tạo 2 đặc trưng

C. Other data: Mảng [3,5,7] — Mảng [3,5,7]

D. The stated data are 2 SV × 3 môn — 2 SV × 3 môn


**Q16. Which input matches example 3? — Dữ liệu nào phù hợp ví dụ 3?**

A. Other data: 2 SV × 3 môn, tạo 2 đặc trưng — 2 SV × 3 môn, tạo 2 đặc trưng

B. Other data: Mảng [3,5,7] — Mảng [3,5,7]

C. The stated data are 3 môn, trọng số cộng bằng 1 — 3 môn, trọng số cộng bằng 1

D. Other data: 6 số đo nhiệt độ giờ — 6 số đo nhiệt độ giờ


**Q17. Which input matches example 4? — Dữ liệu nào phù hợp ví dụ 4?**

A. Other data: Mảng [3,5,7] — Mảng [3,5,7]

B. The stated data are 2 SV × 3 môn, tạo 2 đặc trưng — 2 SV × 3 môn, tạo 2 đặc trưng

C. Other data: 6 số đo nhiệt độ giờ — 6 số đo nhiệt độ giờ

D. Other data: 2 SV × 3 môn — 2 SV × 3 môn


**Q18. Which input matches example 5? — Dữ liệu nào phù hợp ví dụ 5?**

A. The stated data are Mảng [3,5,7] — Mảng [3,5,7]

B. Other data: 6 số đo nhiệt độ giờ — 6 số đo nhiệt độ giờ

C. Other data: 2 SV × 3 môn — 2 SV × 3 môn

D. Other data: 3 môn, trọng số cộng bằng 1 — 3 môn, trọng số cộng bằng 1


**Q19. What must every table clarify? — Bảng dữ liệu cần nêu rõ gì?**

A. Only editor color — Chỉ màu trình soạn

B. Only variable length — Chỉ độ dài tên biến

C. Only number of blank lines — Chỉ số dòng trống

D. Rows, columns and units — Hàng, cột và đơn vị


**Q20. Why test with different inputs? — Tại sao cần thử đầu vào khác?**

A. To guarantee machine learning accuracy — Để bảo đảm AI luôn đúng

B. To remove input validation — Để bỏ kiểm tra dữ liệu

C. To check limitations and edge cases — Để thấy giới hạn và trường hợp biên

D. To change column meanings — Để thay đổi nghĩa các cột

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **B** | The concept is Đổi shape nhưng giữ số phần tử | Đổi shape nhưng giữ số phần tử |
| Q2 | **A** | The concept is Đổi trục hàng và cột | Đổi trục hàng và cột |
| Q3 | **D** | The concept is Tạo kết quả bằng phép nhân tuyến tính | Tạo kết quả bằng phép nhân tuyến tính |
| Q4 | **C** | The concept is Ghi mảng vào tệp để đọc lại | Ghi mảng vào tệp để đọc lại |
| Q5 | **B** | It is used to Số phần tử trước/sau phải bằng nhau | Số phần tử trước/sau phải bằng nhau |
| Q6 | **A** | It is used to Đổi trục từ hàng thành cột | Đổi trục từ hàng thành cột |
| Q7 | **D** | It is used to Nhân tuyến tính yêu cầu kích thước tương thích | Nhân tuyến tính yêu cầu kích thước tương thích |
| Q8 | **C** | It is used to Lưu và đọc định dạng NPY, chỉ tải từ nguồn tin cậy | Lưu và đọc định dạng NPY, chỉ tải từ nguồn tin cậy |
| Q9 | **B** | reshape đổi 6 giá trị thành 2 ngày × 3 giờ | reshape đổi 6 giá trị thành 2 ngày × 3 giờ |
| Q10 | **A** | Transpose làm môn thành hàng, học sinh thành cột | Transpose làm môn thành hàng, học sinh thành cột |
| Q11 | **D** | Nhân vector điểm với vector trọng số | Nhân vector điểm với vector trọng số |
| Q12 | **C** | Nhân matrix học sinh × matrix trọng số | Nhân matrix học sinh × matrix trọng số |
| Q13 | **B** | Lưu trong thư mục tạm và load chỉ từ dữ liệu tự tạo | Lưu trong thư mục tạm và load chỉ từ dữ liệu tự tạo |
| Q14 | **A** | The stated data are 6 số đo nhiệt độ giờ | 6 số đo nhiệt độ giờ |
| Q15 | **D** | The stated data are 2 SV × 3 môn | 2 SV × 3 môn |
| Q16 | **C** | The stated data are 3 môn, trọng số cộng bằng 1 | 3 môn, trọng số cộng bằng 1 |
| Q17 | **B** | The stated data are 2 SV × 3 môn, tạo 2 đặc trưng | 2 SV × 3 môn, tạo 2 đặc trưng |
| Q18 | **A** | The stated data are Mảng [3,5,7] | Mảng [3,5,7] |
| Q19 | **D** | Rows, columns and units | Hàng, cột và đơn vị |
| Q20 | **C** | To check limitations and edge cases | Để thấy giới hạn và trường hợp biên |

## 8. Nối bài tiếp theo

`ndarray → Reshape/Transpose → Matrix → Model Input`.

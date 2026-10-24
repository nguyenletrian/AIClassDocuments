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


## 4. Khái niệm liên quan và ví dụ nhỏ

### 4.1. Reshape

**Từ vựng trong mục:** **Reshape** — đổi hình dạng.

Đổi shape nhưng giữ số phần tử. Hãy xem ví dụ nhỏ trước khi đưa ý tưởng này vào một bảng dữ liệu lớn hơn.

```python
import numpy as np
print(np.arange(6).reshape(2,3))
```

**Tự kiểm tra:** Reshape có nghĩa gì? **Đáp án:** Đổi shape nhưng giữ số phần tử.

### 4.2. Transpose

**Từ vựng trong mục:** **Transpose** — chuyển vị.

Đổi trục hàng và cột. Hãy xem ví dụ nhỏ trước khi đưa ý tưởng này vào một bảng dữ liệu lớn hơn.

```python
import numpy as np
print(np.ones((2,3)).T.shape)
```

**Tự kiểm tra:** Transpose có nghĩa gì? **Đáp án:** Đổi trục hàng và cột.

### 4.3. Matrix multiply

**Từ vựng trong mục:** **Matrix multiply** — nhân ma trận.

Tạo kết quả bằng phép nhân tuyến tính. Hãy xem ví dụ nhỏ trước khi đưa ý tưởng này vào một bảng dữ liệu lớn hơn.

```python
import numpy as np
print(np.eye(2)@np.ones(2))
```

**Tự kiểm tra:** Matrix multiply có nghĩa gì? **Đáp án:** Tạo kết quả bằng phép nhân tuyến tính.

### 4.4. Serialization

**Từ vựng trong mục:** **Serialization** — lưu dữ liệu.

Ghi mảng vào tệp để đọc lại. Hãy xem ví dụ nhỏ trước khi đưa ý tưởng này vào một bảng dữ liệu lớn hơn.

```python
import numpy as np
print(np.array([1,2]).tolist())
```

**Tự kiểm tra:** Serialization có nghĩa gì? **Đáp án:** Ghi mảng vào tệp để đọc lại.

## 5. Năm tình huống thực tế

### Tình huống 1 — Tổ chức dữ liệu đo theo giờ

**Từ vựng trong mục:** **Reshape** — đổi hình dạng.

**Vấn đề:** Tổ chức dữ liệu đo theo giờ.

**Vì sao chọn cách giải này?** reshape đổi 6 giá trị thành 2 ngày × 3 giờ.

**Dữ liệu:** 6 số đo nhiệt độ giờ.

**Quy trình:** hiểu hàng/cột → chọn hàm → chạy phép tính → so sánh trước/sau → kiểm tra trường hợp biên.

```python
import numpy as np
values=np.array([20,21,22,23,24,25])
print(values.reshape(2,3))
```


### Tình huống 2 — Đổi hàng cột báo cáo

**Từ vựng trong mục:** **Transpose** — chuyển vị.

**Vấn đề:** Đổi hàng cột báo cáo.

**Vì sao chọn cách giải này?** Transpose làm môn thành hàng, học sinh thành cột.

**Dữ liệu:** 2 SV × 3 môn.

**Quy trình:** hiểu hàng/cột → chọn hàm → chạy phép tính → so sánh trước/sau → kiểm tra trường hợp biên.

```python
import numpy as np
scores=np.array([[8,7,9],[6,5,8]])
print(scores.T.shape)
```


### Tình huống 3 — Điểm tổng kết có trọng số

**Từ vựng trong mục:** **Matrix multiply** — nhân ma trận.

**Vấn đề:** Điểm tổng kết có trọng số.

**Vì sao chọn cách giải này?** Nhân vector điểm với vector trọng số.

**Dữ liệu:** 3 môn, trọng số cộng bằng 1.

**Quy trình:** hiểu hàng/cột → chọn hàm → chạy phép tính → so sánh trước/sau → kiểm tra trường hợp biên.

```python
import numpy as np
scores=np.array([8,7,9]);w=np.array([.2,.3,.5])
print(scores@w)
```


### Tình huống 4 — Tạo đặc trưng tổng hợp

**Từ vựng trong mục:** **Serialization** — lưu dữ liệu.

**Vấn đề:** Tạo đặc trưng tổng hợp.

**Vì sao chọn cách giải này?** Nhân matrix học sinh × matrix trọng số.

**Dữ liệu:** 2 SV × 3 môn, tạo 2 đặc trưng.

**Quy trình:** hiểu hàng/cột → chọn hàm → chạy phép tính → so sánh trước/sau → kiểm tra trường hợp biên.

```python
import numpy as np
X=np.array([[8,7,9],[6,5,8]])
W=np.array([[.5,0],[.5,.5],[0,.5]])
print(X@W)
```


### Tình huống 5 — Lưu và đọc mảng an toàn

**Từ vựng trong mục:** **Reshape** — đổi hình dạng.

**Vấn đề:** Lưu và đọc mảng an toàn.

**Vì sao chọn cách giải này?** Lưu trong thư mục tạm và load chỉ từ dữ liệu tự tạo.

**Dữ liệu:** Mảng [3,5,7].

**Quy trình:** hiểu hàng/cột → chọn hàm → chạy phép tính → so sánh trước/sau → kiểm tra trường hợp biên.

```python
import numpy as np
from pathlib import Path
from tempfile import TemporaryDirectory
with TemporaryDirectory() as folder:
    p=Path(folder)/"data.npy"
    np.save(p,np.array([3,5,7]))
    print(np.load(p,allow_pickle=False))
```


## 6. Sai lầm thường gặp

Các tham số như axis, shape, dtype hoặc cách xử lý giá trị thiếu có thể thay đổi kết quả. Trước khi xử lý phải biết số hàng, số cột, đơn vị và mục đích của từng phép biến đổi.

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

# PY-14 — NumPy indexing, slicing, boolean và fancy indexing


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Index** — chỉ số; **Slice** — cắt lát.

`NumPy ndarray → Chọn hàng/cột → DataFrame/PCA`

Nắm khái niệm của bài này giúp xử lý đúng dữ liệu có nhiều đối tượng và đặc trưng trước khi dùng trong AI.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Dùng khi nào |
|---|---|---|
| Index | chỉ số | Địa chỉ phần tử của mảng |
| Slice | cắt lát | Lấy một đoạn theo start:stop |
| Boolean mask | mặt nạ logic | Mảng True/False để lọc phần tử |
| Fancy indexing | chỉ số nâng cao | Chọn nhiều vị trí theo danh sách chỉ số |

## 3. Thư viện, hàm và lựa chọn

**Từ vựng trong mục:** **Function** — hàm; **Argument** — đối số.

| Hàm / tham số | Giải thích ngay theo hàm |
|---|---|
| `X[row,col]` | Chọn một ô theo hàng/cột, đếm từ 0 |
| `X[:,j] / X[i,:]` | Lấy cả cột j hoặc hàng i |
| `X[condition]` | Giữ các phần tử thỏa điều kiện logic |
| `X[:,[0,2]]` | Chọn các cột không liền nhau |


## 4. Khái niệm liên quan

### 4.1. Index

**Từ vựng trong mục:** **Index** — chỉ số.

Chỉ số NumPy bắt đầu từ 0; với bảng hai chiều, `a[row, col]` lấy ô theo hàng và cột.

```python
import numpy as np
print(np.array([8,9])[0])
```

**Kết quả khi chạy:**

```text
8
```

### 4.2. Slice

**Từ vựng trong mục:** **Slice** — cắt lát.

Cắt mảng bằng `[start:stop]` lấy các vị trí từ start tới trước stop.

```python
import numpy as np
print(np.arange(5)[1:3])
```

**Kết quả khi chạy:**

```text
[1 2]
```

### 4.3. Boolean mask

**Từ vựng trong mục:** **Boolean mask** — mặt nạ logic.

Mặt nạ Boolean lọc những phần tử hoặc hàng thỏa điều kiện so sánh.

```python
import numpy as np
x=np.array([4,7,9]);print(x[x>=7])
```

**Kết quả khi chạy:**

```text
[7 9]
```

### 4.4. Fancy indexing

**Từ vựng trong mục:** **Fancy indexing** — chỉ số nâng cao.

Fancy indexing dùng danh sách chỉ số để chọn nhiều vị trí không liền nhau.

```python
import numpy as np
x=np.array([3,5,7]);print(x[[0,2]])
```

**Kết quả khi chạy:**

```text
[3 7]
```

## 5. Năm tình huống thực tế

### Tình huống 1 — Tra điểm một sinh viên

**Từ vựng trong mục:** **Index** — chỉ số.

**Tình huống thực tế:** Trung tâm lưu điểm ba học viên, hai môn: `(8,9)`, `(6,7)`, `(9,8)` trên thang 10. Lấy điểm môn thứ nhất của học viên thứ hai.

**Vì sao chọn cách giải này?** Chỉ số hàng 1, cột 0 trỏ vào giá trị 6.

**Quy trình giải:** Lưu dữ liệu đúng thứ tự hàng/cột → dùng phép NumPy phù hợp → in và giải thích kết quả.

```python
import numpy as np
scores=np.array([[8,9],[6,7],[9,8]])
print(scores[1,0])
```

**Kết quả khi chạy:**

```text
6
```

**Kết quả:** Xem ngay giá trị bên dưới đoạn code để biết phép tính đã thực hiện gì.

### Tình huống 2 — Báo danh sách điểm cao

**Từ vựng trong mục:** **Slice** — cắt lát.

**Tình huống thực tế:** Trung tâm có bảng điểm ba học viên như trên và muốn xem người đạt ít nhất 8 điểm ở môn thứ nhất. In những hàng có điểm môn thứ nhất từ 8 trở lên.

**Vì sao chọn cách giải này?** `X[:,0] >= 8` tạo mặt nạ theo cột đầu, sau đó lọc cả hàng.

**Quy trình giải:** Lưu dữ liệu đúng thứ tự hàng/cột → dùng phép NumPy phù hợp → in và giải thích kết quả.

```python
import numpy as np
X=np.array([[8,9],[6,7],[9,8]])
print(X[X[:,0]>=8])
```

**Kết quả khi chạy:**

```text
[[8 9]
 [9 8]]
```

**Kết quả:** Xem ngay giá trị bên dưới đoạn code để biết phép tính đã thực hiện gì.

### Tình huống 3 — Lấy hai môn cần kiểm

**Từ vựng trong mục:** **Boolean mask** — mặt nạ logic.

**Tình huống thực tế:** Bảng điểm hai học viên gồm ba môn: `(8,7,9)` và `(6,5,8)`. Chỉ cần kiểm tra môn thứ nhất và thứ ba. In hai cột môn được chọn.

**Vì sao chọn cách giải này?** `X[:,[0,2]]` lấy mọi hàng và hai cột ở chỉ số 0, 2.

**Quy trình giải:** Lưu dữ liệu đúng thứ tự hàng/cột → dùng phép NumPy phù hợp → in và giải thích kết quả.

```python
import numpy as np
X=np.array([[8,7,9],[6,5,8]])
print(X[:,[0,2]])
```

**Kết quả khi chạy:**

```text
[[8 9]
 [6 8]]
```

**Kết quả:** Xem ngay giá trị bên dưới đoạn code để biết phép tính đã thực hiện gì.

### Tình huống 4 — Lấy ba khách đầu tiên

**Từ vựng trong mục:** **Fancy indexing** — chỉ số nâng cao.

**Tình huống thực tế:** Năm khách có mức chi tiêu lần lượt 100, 200, 50, 300, 120 nghìn đồng. In ba mức chi tiêu đầu tiên.

**Vì sao chọn cách giải này?** `[:3]` cắt ba phần tử đầu, không lấy phần tử thứ tư.

**Quy trình giải:** Lưu dữ liệu đúng thứ tự hàng/cột → dùng phép NumPy phù hợp → in và giải thích kết quả.

```python
import numpy as np
spend=np.array([100,200,50,300,120])
print(spend[:3])
```

**Kết quả khi chạy:**

```text
[100 200  50]
```

**Kết quả:** Xem ngay giá trị bên dưới đoạn code để biết phép tính đã thực hiện gì.

### Tình huống 5 — Sửa số đo bất thường

**Từ vựng trong mục:** **Index** — chỉ số.

**Tình huống thực tế:** Cảm biến ghi các số đo `[20,-1,23,24]` °C, trong đó -1 là mã báo lỗi. Tạo bản sao và thay mã lỗi âm bằng 0 nhưng giữ nguyên dữ liệu ban đầu.

**Vì sao chọn cách giải này?** `copy()` tránh sửa mảng gốc; điều kiện `<0` chỉ chọn giá trị âm.

**Quy trình giải:** Lưu dữ liệu đúng thứ tự hàng/cột → dùng phép NumPy phù hợp → in và giải thích kết quả.

```python
import numpy as np
values=np.array([20,-1,23,24])
clean=values.copy();clean[clean<0]=0
print(values,clean)
```

**Kết quả khi chạy:**

```text
[20 -1 23 24] [20  0 23 24]
```

**Kết quả:** Xem ngay giá trị bên dưới đoạn code để biết phép tính đã thực hiện gì.

## 6. Sai lầm thường gặp

Các tham số như axis, shape, dtype hoặc cách xử lý giá trị thiếu có thể thay đổi kết quả. Trước khi xử lý phải biết số hàng, số cột, đơn vị và mục đích của từng phép biến đổi.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.


**Q1. What does Index mean? — Ý nghĩa của Index là gì?**

A. It instead describes Lấy một đoạn theo start:stop — Lấy một đoạn theo start:stop

B. The concept is Địa chỉ phần tử của mảng — Địa chỉ phần tử của mảng

C. It instead describes Mảng True/False để lọc phần tử — Mảng True/False để lọc phần tử

D. It instead describes Chọn nhiều vị trí theo danh sách chỉ số — Chọn nhiều vị trí theo danh sách chỉ số


**Q2. What does Slice mean? — Ý nghĩa của Slice là gì?**

A. The concept is Lấy một đoạn theo start:stop — Lấy một đoạn theo start:stop

B. It instead describes Mảng True/False để lọc phần tử — Mảng True/False để lọc phần tử

C. It instead describes Chọn nhiều vị trí theo danh sách chỉ số — Chọn nhiều vị trí theo danh sách chỉ số

D. It instead describes Địa chỉ phần tử của mảng — Địa chỉ phần tử của mảng


**Q3. What does Boolean mask mean? — Ý nghĩa của Boolean mask là gì?**

A. It instead describes Chọn nhiều vị trí theo danh sách chỉ số — Chọn nhiều vị trí theo danh sách chỉ số

B. It instead describes Địa chỉ phần tử của mảng — Địa chỉ phần tử của mảng

C. It instead describes Lấy một đoạn theo start:stop — Lấy một đoạn theo start:stop

D. The concept is Mảng True/False để lọc phần tử — Mảng True/False để lọc phần tử


**Q4. What does Fancy indexing mean? — Ý nghĩa của Fancy indexing là gì?**

A. It instead describes Địa chỉ phần tử của mảng — Địa chỉ phần tử của mảng

B. It instead describes Lấy một đoạn theo start:stop — Lấy một đoạn theo start:stop

C. The concept is Chọn nhiều vị trí theo danh sách chỉ số — Chọn nhiều vị trí theo danh sách chỉ số

D. It instead describes Mảng True/False để lọc phần tử — Mảng True/False để lọc phần tử


**Q5. What is the role of X[row,col]? — Vai trò của X[row,col] là gì?**

A. Another operation would Lấy cả cột j hoặc hàng i — Lấy cả cột j hoặc hàng i

B. It is used to Chọn một ô theo hàng/cột, đếm từ 0 — Chọn một ô theo hàng/cột, đếm từ 0

C. Another operation would Giữ các phần tử thỏa điều kiện logic — Giữ các phần tử thỏa điều kiện logic

D. Another operation would Chọn các cột không liền nhau — Chọn các cột không liền nhau


**Q6. What is the role of X[:,j] / X[i,:]? — Vai trò của X[:,j] / X[i,:] là gì?**

A. It is used to Lấy cả cột j hoặc hàng i — Lấy cả cột j hoặc hàng i

B. Another operation would Giữ các phần tử thỏa điều kiện logic — Giữ các phần tử thỏa điều kiện logic

C. Another operation would Chọn các cột không liền nhau — Chọn các cột không liền nhau

D. Another operation would Chọn một ô theo hàng/cột, đếm từ 0 — Chọn một ô theo hàng/cột, đếm từ 0


**Q7. What is the role of X[condition]? — Vai trò của X[condition] là gì?**

A. Another operation would Chọn các cột không liền nhau — Chọn các cột không liền nhau

B. Another operation would Chọn một ô theo hàng/cột, đếm từ 0 — Chọn một ô theo hàng/cột, đếm từ 0

C. Another operation would Lấy cả cột j hoặc hàng i — Lấy cả cột j hoặc hàng i

D. It is used to Giữ các phần tử thỏa điều kiện logic — Giữ các phần tử thỏa điều kiện logic


**Q8. What is the role of X[:,[0,2]]? — Vai trò của X[:,[0,2]] là gì?**

A. Another operation would Chọn một ô theo hàng/cột, đếm từ 0 — Chọn một ô theo hàng/cột, đếm từ 0

B. Another operation would Lấy cả cột j hoặc hàng i — Lấy cả cột j hoặc hàng i

C. It is used to Chọn các cột không liền nhau — Chọn các cột không liền nhau

D. Another operation would Giữ các phần tử thỏa điều kiện logic — Giữ các phần tử thỏa điều kiện logic


**Q9. Which reason fits example 1? — Lý do nào phù hợp ví dụ 1?**

A. Mask lọc hàng điểm Python>=8 — Mask lọc hàng điểm Python>=8

B. Lấy đúng hàng sinh viên và cột môn học — Lấy đúng hàng sinh viên và cột môn học

C. Fancy indexing chọn cột không cần liền nhau — Fancy indexing chọn cột không cần liền nhau

D. Slice theo chiều hàng để xem mẫu báo cáo — Slice theo chiều hàng để xem mẫu báo cáo


**Q10. Which reason fits example 2? — Lý do nào phù hợp ví dụ 2?**

A. Mask lọc hàng điểm Python>=8 — Mask lọc hàng điểm Python>=8

B. Fancy indexing chọn cột không cần liền nhau — Fancy indexing chọn cột không cần liền nhau

C. Slice theo chiều hàng để xem mẫu báo cáo — Slice theo chiều hàng để xem mẫu báo cáo

D. Thao tác mask trên bản sao để không đổi mảng gốc — Thao tác mask trên bản sao để không đổi mảng gốc


**Q11. Which reason fits example 3? — Lý do nào phù hợp ví dụ 3?**

A. Slice theo chiều hàng để xem mẫu báo cáo — Slice theo chiều hàng để xem mẫu báo cáo

B. Thao tác mask trên bản sao để không đổi mảng gốc — Thao tác mask trên bản sao để không đổi mảng gốc

C. Lấy đúng hàng sinh viên và cột môn học — Lấy đúng hàng sinh viên và cột môn học

D. Fancy indexing chọn cột không cần liền nhau — Fancy indexing chọn cột không cần liền nhau


**Q12. Which reason fits example 4? — Lý do nào phù hợp ví dụ 4?**

A. Thao tác mask trên bản sao để không đổi mảng gốc — Thao tác mask trên bản sao để không đổi mảng gốc

B. Lấy đúng hàng sinh viên và cột môn học — Lấy đúng hàng sinh viên và cột môn học

C. Slice theo chiều hàng để xem mẫu báo cáo — Slice theo chiều hàng để xem mẫu báo cáo

D. Mask lọc hàng điểm Python>=8 — Mask lọc hàng điểm Python>=8


**Q13. Which reason fits example 5? — Lý do nào phù hợp ví dụ 5?**

A. Lấy đúng hàng sinh viên và cột môn học — Lấy đúng hàng sinh viên và cột môn học

B. Thao tác mask trên bản sao để không đổi mảng gốc — Thao tác mask trên bản sao để không đổi mảng gốc

C. Mask lọc hàng điểm Python>=8 — Mask lọc hàng điểm Python>=8

D. Fancy indexing chọn cột không cần liền nhau — Fancy indexing chọn cột không cần liền nhau


**Q14. Which input matches example 1? — Dữ liệu nào phù hợp ví dụ 1?**

A. The stated data are 3 học sinh × 2 môn, điểm thang 10 — 3 học sinh × 2 môn, điểm thang 10

B. Other data: 3 học sinh × 2 môn — 3 học sinh × 2 môn

C. Other data: 2 sinh viên × 3 môn — 2 sinh viên × 3 môn

D. Other data: 5 khách với điểm chi tiêu — 5 khách với điểm chi tiêu


**Q15. Which input matches example 2? — Dữ liệu nào phù hợp ví dụ 2?**

A. Other data: 2 sinh viên × 3 môn — 2 sinh viên × 3 môn

B. Other data: 5 khách với điểm chi tiêu — 5 khách với điểm chi tiêu

C. Other data: 4 nhiệt độ có một giá trị âm lỗi — 4 nhiệt độ có một giá trị âm lỗi

D. The stated data are 3 học sinh × 2 môn — 3 học sinh × 2 môn


**Q16. Which input matches example 3? — Dữ liệu nào phù hợp ví dụ 3?**

A. Other data: 5 khách với điểm chi tiêu — 5 khách với điểm chi tiêu

B. Other data: 4 nhiệt độ có một giá trị âm lỗi — 4 nhiệt độ có một giá trị âm lỗi

C. The stated data are 2 sinh viên × 3 môn — 2 sinh viên × 3 môn

D. Other data: 3 học sinh × 2 môn, điểm thang 10 — 3 học sinh × 2 môn, điểm thang 10


**Q17. Which input matches example 4? — Dữ liệu nào phù hợp ví dụ 4?**

A. Other data: 4 nhiệt độ có một giá trị âm lỗi — 4 nhiệt độ có một giá trị âm lỗi

B. The stated data are 5 khách với điểm chi tiêu — 5 khách với điểm chi tiêu

C. Other data: 3 học sinh × 2 môn, điểm thang 10 — 3 học sinh × 2 môn, điểm thang 10

D. Other data: 3 học sinh × 2 môn — 3 học sinh × 2 môn


**Q18. Which input matches example 5? — Dữ liệu nào phù hợp ví dụ 5?**

A. The stated data are 4 nhiệt độ có một giá trị âm lỗi — 4 nhiệt độ có một giá trị âm lỗi

B. Other data: 3 học sinh × 2 môn, điểm thang 10 — 3 học sinh × 2 môn, điểm thang 10

C. Other data: 3 học sinh × 2 môn — 3 học sinh × 2 môn

D. Other data: 2 sinh viên × 3 môn — 2 sinh viên × 3 môn


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
| Q1 | **B** | The concept is Địa chỉ phần tử của mảng | Địa chỉ phần tử của mảng |
| Q2 | **A** | The concept is Lấy một đoạn theo start:stop | Lấy một đoạn theo start:stop |
| Q3 | **D** | The concept is Mảng True/False để lọc phần tử | Mảng True/False để lọc phần tử |
| Q4 | **C** | The concept is Chọn nhiều vị trí theo danh sách chỉ số | Chọn nhiều vị trí theo danh sách chỉ số |
| Q5 | **B** | It is used to Chọn một ô theo hàng/cột, đếm từ 0 | Chọn một ô theo hàng/cột, đếm từ 0 |
| Q6 | **A** | It is used to Lấy cả cột j hoặc hàng i | Lấy cả cột j hoặc hàng i |
| Q7 | **D** | It is used to Giữ các phần tử thỏa điều kiện logic | Giữ các phần tử thỏa điều kiện logic |
| Q8 | **C** | It is used to Chọn các cột không liền nhau | Chọn các cột không liền nhau |
| Q9 | **B** | Lấy đúng hàng sinh viên và cột môn học | Lấy đúng hàng sinh viên và cột môn học |
| Q10 | **A** | Mask lọc hàng điểm Python>=8 | Mask lọc hàng điểm Python>=8 |
| Q11 | **D** | Fancy indexing chọn cột không cần liền nhau | Fancy indexing chọn cột không cần liền nhau |
| Q12 | **C** | Slice theo chiều hàng để xem mẫu báo cáo | Slice theo chiều hàng để xem mẫu báo cáo |
| Q13 | **B** | Thao tác mask trên bản sao để không đổi mảng gốc | Thao tác mask trên bản sao để không đổi mảng gốc |
| Q14 | **A** | The stated data are 3 học sinh × 2 môn, điểm thang 10 | 3 học sinh × 2 môn, điểm thang 10 |
| Q15 | **D** | The stated data are 3 học sinh × 2 môn | 3 học sinh × 2 môn |
| Q16 | **C** | The stated data are 2 sinh viên × 3 môn | 2 sinh viên × 3 môn |
| Q17 | **B** | The stated data are 5 khách với điểm chi tiêu | 5 khách với điểm chi tiêu |
| Q18 | **A** | The stated data are 4 nhiệt độ có một giá trị âm lỗi | 4 nhiệt độ có một giá trị âm lỗi |
| Q19 | **D** | Rows, columns and units | Hàng, cột và đơn vị |
| Q20 | **C** | To check limitations and edge cases | Để thấy giới hạn và trường hợp biên |

## 8. Nối bài tiếp theo

`NumPy ndarray → Chọn hàng/cột → DataFrame/PCA`.

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

Trong code demo, chú thích dữ liệu và lý do xử lý; các flags đã được giải thích ngay tại bảng hàm này.

## 4. Khái niệm liên quan và ví dụ nhỏ

### 4.1. Index

**Từ vựng trong mục:** **Index** — chỉ số.

Địa chỉ phần tử của mảng. Hãy xem ví dụ nhỏ trước khi đưa ý tưởng này vào một bảng dữ liệu lớn hơn.

```python
import numpy as np
print(np.array([8,9])[0])
```

**Tự kiểm tra:** Index có nghĩa gì? **Đáp án:** Địa chỉ phần tử của mảng.

### 4.2. Slice

**Từ vựng trong mục:** **Slice** — cắt lát.

Lấy một đoạn theo start:stop. Hãy xem ví dụ nhỏ trước khi đưa ý tưởng này vào một bảng dữ liệu lớn hơn.

```python
import numpy as np
print(np.arange(5)[1:3])
```

**Tự kiểm tra:** Slice có nghĩa gì? **Đáp án:** Lấy một đoạn theo start:stop.

### 4.3. Boolean mask

**Từ vựng trong mục:** **Boolean mask** — mặt nạ logic.

Mảng True/False để lọc phần tử. Hãy xem ví dụ nhỏ trước khi đưa ý tưởng này vào một bảng dữ liệu lớn hơn.

```python
import numpy as np
x=np.array([4,7,9]);print(x[x>=7])
```

**Tự kiểm tra:** Boolean mask có nghĩa gì? **Đáp án:** Mảng True/False để lọc phần tử.

### 4.4. Fancy indexing

**Từ vựng trong mục:** **Fancy indexing** — chỉ số nâng cao.

Chọn nhiều vị trí theo danh sách chỉ số. Hãy xem ví dụ nhỏ trước khi đưa ý tưởng này vào một bảng dữ liệu lớn hơn.

```python
import numpy as np
x=np.array([3,5,7]);print(x[[0,2]])
```

**Tự kiểm tra:** Fancy indexing có nghĩa gì? **Đáp án:** Chọn nhiều vị trí theo danh sách chỉ số.

## 5. Năm tình huống thực tế

### Tình huống 1 — Tra điểm một sinh viên

**Từ vựng trong mục:** **Index** — chỉ số.

**Vấn đề:** Tra điểm một sinh viên.

**Vì sao chọn cách giải này?** Lấy đúng hàng sinh viên và cột môn học. Đây là lựa chọn đơn giản, có thể chạy thử độc lập trước khi dùng trên dữ liệu lớn.

**Dữ liệu:** 3 học sinh × 2 môn, điểm thang 10; mỗi hàng của bảng là một mẫu, mỗi cột là một thuộc tính theo đơn vị trong mô tả. Các số là dữ liệu minh họa.

**Quy trình:** hiểu hàng/cột → chọn hàm → chạy phép tính → so sánh trước/sau → kiểm tra trường hợp biên.

```python
import numpy as np
scores=np.array([[8,9],[6,7],[9,8]])
print(scores[1,0])
```

**Đọc kết quả:** Kiểm tra shape và giá trị in ra. Không suy diễn độ chính xác một mô hình AI từ dữ liệu demo.

### Tình huống 2 — Báo danh sách điểm cao

**Từ vựng trong mục:** **Slice** — cắt lát.

**Vấn đề:** Báo danh sách điểm cao.

**Vì sao chọn cách giải này?** Mask lọc hàng điểm Python>=8. Đây là lựa chọn đơn giản, có thể chạy thử độc lập trước khi dùng trên dữ liệu lớn.

**Dữ liệu:** 3 học sinh × 2 môn; mỗi hàng của bảng là một mẫu, mỗi cột là một thuộc tính theo đơn vị trong mô tả. Các số là dữ liệu minh họa.

**Quy trình:** hiểu hàng/cột → chọn hàm → chạy phép tính → so sánh trước/sau → kiểm tra trường hợp biên.

```python
import numpy as np
X=np.array([[8,9],[6,7],[9,8]])
print(X[X[:,0]>=8])
```

**Đọc kết quả:** Kiểm tra shape và giá trị in ra. Không suy diễn độ chính xác một mô hình AI từ dữ liệu demo.

### Tình huống 3 — Lấy hai môn cần kiểm

**Từ vựng trong mục:** **Boolean mask** — mặt nạ logic.

**Vấn đề:** Lấy hai môn cần kiểm.

**Vì sao chọn cách giải này?** Fancy indexing chọn cột không cần liền nhau. Đây là lựa chọn đơn giản, có thể chạy thử độc lập trước khi dùng trên dữ liệu lớn.

**Dữ liệu:** 2 sinh viên × 3 môn; mỗi hàng của bảng là một mẫu, mỗi cột là một thuộc tính theo đơn vị trong mô tả. Các số là dữ liệu minh họa.

**Quy trình:** hiểu hàng/cột → chọn hàm → chạy phép tính → so sánh trước/sau → kiểm tra trường hợp biên.

```python
import numpy as np
X=np.array([[8,7,9],[6,5,8]])
print(X[:,[0,2]])
```

**Đọc kết quả:** Kiểm tra shape và giá trị in ra. Không suy diễn độ chính xác một mô hình AI từ dữ liệu demo.

### Tình huống 4 — Lấy ba khách đầu tiên

**Từ vựng trong mục:** **Fancy indexing** — chỉ số nâng cao.

**Vấn đề:** Lấy ba khách đầu tiên.

**Vì sao chọn cách giải này?** Slice theo chiều hàng để xem mẫu báo cáo. Đây là lựa chọn đơn giản, có thể chạy thử độc lập trước khi dùng trên dữ liệu lớn.

**Dữ liệu:** 5 khách với điểm chi tiêu; mỗi hàng của bảng là một mẫu, mỗi cột là một thuộc tính theo đơn vị trong mô tả. Các số là dữ liệu minh họa.

**Quy trình:** hiểu hàng/cột → chọn hàm → chạy phép tính → so sánh trước/sau → kiểm tra trường hợp biên.

```python
import numpy as np
spend=np.array([100,200,50,300,120])
print(spend[:3])
```

**Đọc kết quả:** Kiểm tra shape và giá trị in ra. Không suy diễn độ chính xác một mô hình AI từ dữ liệu demo.

### Tình huống 5 — Sửa số đo bất thường

**Từ vựng trong mục:** **Index** — chỉ số.

**Vấn đề:** Sửa số đo bất thường.

**Vì sao chọn cách giải này?** Thao tác mask trên bản sao để không đổi mảng gốc. Đây là lựa chọn đơn giản, có thể chạy thử độc lập trước khi dùng trên dữ liệu lớn.

**Dữ liệu:** 4 nhiệt độ có một giá trị âm lỗi; mỗi hàng của bảng là một mẫu, mỗi cột là một thuộc tính theo đơn vị trong mô tả. Các số là dữ liệu minh họa.

**Quy trình:** hiểu hàng/cột → chọn hàm → chạy phép tính → so sánh trước/sau → kiểm tra trường hợp biên.

```python
import numpy as np
values=np.array([20,-1,23,24])
clean=values.copy();clean[clean<0]=0
print(values,clean)
```

**Đọc kết quả:** Kiểm tra shape và giá trị in ra. Không suy diễn độ chính xác một mô hình AI từ dữ liệu demo.

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

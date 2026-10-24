# PY-22 — Hoán vị, tổ hợp và tam giác Pascal

*DRAFT · Dữ liệu giả lập · Cần kiểm chứng code trước khi phát hành*

## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Permutation** — hoán vị; **Combination** — tổ hợp.

`Nguyên lý đếm → hoán vị/tổ hợp → phân phối nhị thức`

Bài học giúp sinh viên nhìn rõ quan hệ giữa kiến thức trước và cách xử lý dữ liệu để ứng dụng AI sau này.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Giải thích |
|---|---|---|
| Permutation | hoán vị | Chọn có phân biệt thứ tự |
| Combination | tổ hợp | Chọn nhóm không xét thứ tự |
| Factorial | giai thừa | Tích các số từ 1 đến n |
| Binomial coefficient | hệ số nhị thức | Số cách chọn k từ n |

## 3. Hàm Python và tham số

**Từ vựng trong mục:** **Function** — hàm; **Parameter** — tham số.

| Hàm / cú pháp | Vì sao dùng |
|---|---|
| `math.factorial(n)` | Tính n!, n không âm |
| `math.perm(n,k)` | Đếm cách chọn có thứ tự k từ n |
| `math.comb(n,k)` | Đếm cách chọn không thứ tự |
| `itertools.combinations/permutations` | Liệt kê kết quả khi n nhỏ |

## 4. Các khái niệm liên quan

### 4.1. Permutation

**Từ vựng trong mục:** **Permutation** — hoán vị.

Chọn có phân biệt thứ tự. Đọc khái niệm trước rồi kiểm tra bằng ví dụ Python nhỏ.

```python
import math
print(math.perm(5,2))
```

**Tự kiểm tra nhanh:** Permutation là gì? **Đáp án:** Chọn có phân biệt thứ tự.

### 4.2. Combination

**Từ vựng trong mục:** **Combination** — tổ hợp.

Chọn nhóm không xét thứ tự. Đọc khái niệm trước rồi kiểm tra bằng ví dụ Python nhỏ.

```python
import math
print(math.comb(5,2))
```

**Tự kiểm tra nhanh:** Combination là gì? **Đáp án:** Chọn nhóm không xét thứ tự.

### 4.3. Factorial

**Từ vựng trong mục:** **Factorial** — giai thừa.

Tích các số từ 1 đến n. Đọc khái niệm trước rồi kiểm tra bằng ví dụ Python nhỏ.

```python
import math
print(math.factorial(4))
```

**Tự kiểm tra nhanh:** Factorial là gì? **Đáp án:** Tích các số từ 1 đến n.

### 4.4. Binomial coefficient

**Từ vựng trong mục:** **Binomial coefficient** — hệ số nhị thức.

Số cách chọn k từ n. Đọc khái niệm trước rồi kiểm tra bằng ví dụ Python nhỏ.

```python
import math
print(math.comb(6,3))
```

**Tự kiểm tra nhanh:** Binomial coefficient là gì? **Đáp án:** Số cách chọn k từ n.

## 5. Năm vấn đề thực tế

### Tình huống 1 — Chọn trưởng và phó nhóm

**Từ vựng trong mục:** **Permutation** — hoán vị.

**Vấn đề:** Chọn trưởng và phó nhóm.

**Vì sao chọn phương án này?** Vị trí trưởng và phó khác nhau nên dùng hoán vị. Đừng chọn thuật toán AI khi chỉ cần thống kê hay quy tắc rõ ràng.

**Dữ liệu:** 5 ứng viên, 2 vai trò. Đầu vào minh họa; nếu dùng bảng, mỗi hàng là một đối tượng và cột là đặc trưng cụ thể.

**Quy trình:** Đọc dữ liệu → chọn phương pháp → triển khai → đọc kết quả → kiểm tra trường hợp biên.

```python
import math
print(math.perm(5,2))
```

**Đọc kết quả:** Giải thích ý nghĩa đầu ra và thử thay một dữ liệu để quan sát kết quả.

### Tình huống 2 — Chọn đội thi

**Từ vựng trong mục:** **Combination** — tổ hợp.

**Vấn đề:** Chọn đội thi.

**Vì sao chọn phương án này?** Các thành viên không phân vai trò nên dùng tổ hợp. Đừng chọn thuật toán AI khi chỉ cần thống kê hay quy tắc rõ ràng.

**Dữ liệu:** 12 người, chọn 5. Đầu vào minh họa; nếu dùng bảng, mỗi hàng là một đối tượng và cột là đặc trưng cụ thể.

**Quy trình:** Đọc dữ liệu → chọn phương pháp → triển khai → đọc kết quả → kiểm tra trường hợp biên.

```python
import math
print(math.comb(12,5))
```

**Đọc kết quả:** Giải thích ý nghĩa đầu ra và thử thay một dữ liệu để quan sát kết quả.

### Tình huống 3 — Sắp thứ tự kiểm thử

**Từ vựng trong mục:** **Factorial** — giai thừa.

**Vấn đề:** Sắp thứ tự kiểm thử.

**Vì sao chọn phương án này?** Thứ tự thực hiện làm kết quả khác nhau. Đừng chọn thuật toán AI khi chỉ cần thống kê hay quy tắc rõ ràng.

**Dữ liệu:** 3 bài test A B C. Đầu vào minh họa; nếu dùng bảng, mỗi hàng là một đối tượng và cột là đặc trưng cụ thể.

**Quy trình:** Đọc dữ liệu → chọn phương pháp → triển khai → đọc kết quả → kiểm tra trường hợp biên.

```python
from itertools import permutations
print(list(permutations(["A","B","C"])))
```

**Đọc kết quả:** Giải thích ý nghĩa đầu ra và thử thay một dữ liệu để quan sát kết quả.

### Tình huống 4 — Đề xuất cặp môn học

**Từ vựng trong mục:** **Binomial coefficient** — hệ số nhị thức.

**Vấn đề:** Đề xuất cặp môn học.

**Vì sao chọn phương án này?** Mỗi cặp môn học không cần phân biệt thứ tự. Đừng chọn thuật toán AI khi chỉ cần thống kê hay quy tắc rõ ràng.

**Dữ liệu:** Ba môn Python AI SQL. Đầu vào minh họa; nếu dùng bảng, mỗi hàng là một đối tượng và cột là đặc trưng cụ thể.

**Quy trình:** Đọc dữ liệu → chọn phương pháp → triển khai → đọc kết quả → kiểm tra trường hợp biên.

```python
from itertools import combinations
print(list(combinations(["Python","AI","SQL"],2)))
```

**Đọc kết quả:** Giải thích ý nghĩa đầu ra và thử thay một dữ liệu để quan sát kết quả.

### Tình huống 5 — Tính hàng Pascal

**Từ vựng trong mục:** **Permutation** — hoán vị.

**Vấn đề:** Tính hàng Pascal.

**Vì sao chọn phương án này?** Hệ số comb cho từng vị trí hàng n. Đừng chọn thuật toán AI khi chỉ cần thống kê hay quy tắc rõ ràng.

**Dữ liệu:** Hàng n=4. Đầu vào minh họa; nếu dùng bảng, mỗi hàng là một đối tượng và cột là đặc trưng cụ thể.

**Quy trình:** Đọc dữ liệu → chọn phương pháp → triển khai → đọc kết quả → kiểm tra trường hợp biên.

```python
import math
print([math.comb(4,k) for k in range(5)])
```

**Đọc kết quả:** Giải thích ý nghĩa đầu ra và thử thay một dữ liệu để quan sát kết quả.

## 6. Các lỗi dễ mắc

Cần phân biệt khi nào thứ tự quan trọng, khi nào phần tử trùng được tính lại, và khi nào dữ liệu thật không có đủ điều kiện như ví dụ. Xem kỹ kiểu dữ liệu và đầu vào trống.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.


**Q1. What best describes Permutation? — Mô tả nào đúng với Permutation?**

A. A different idea is Chọn nhóm không xét thứ tự — Chọn nhóm không xét thứ tự

B. It is Chọn có phân biệt thứ tự — Chọn có phân biệt thứ tự

C. A different idea is Tích các số từ 1 đến n — Tích các số từ 1 đến n

D. A different idea is Số cách chọn k từ n — Số cách chọn k từ n


**Q2. What best describes Combination? — Mô tả nào đúng với Combination?**

A. It is Chọn nhóm không xét thứ tự — Chọn nhóm không xét thứ tự

B. A different idea is Tích các số từ 1 đến n — Tích các số từ 1 đến n

C. A different idea is Số cách chọn k từ n — Số cách chọn k từ n

D. A different idea is Chọn có phân biệt thứ tự — Chọn có phân biệt thứ tự


**Q3. What best describes Factorial? — Mô tả nào đúng với Factorial?**

A. A different idea is Số cách chọn k từ n — Số cách chọn k từ n

B. A different idea is Chọn có phân biệt thứ tự — Chọn có phân biệt thứ tự

C. A different idea is Chọn nhóm không xét thứ tự — Chọn nhóm không xét thứ tự

D. It is Tích các số từ 1 đến n — Tích các số từ 1 đến n


**Q4. What best describes Binomial coefficient? — Mô tả nào đúng với Binomial coefficient?**

A. A different idea is Chọn có phân biệt thứ tự — Chọn có phân biệt thứ tự

B. A different idea is Chọn nhóm không xét thứ tự — Chọn nhóm không xét thứ tự

C. It is Số cách chọn k từ n — Số cách chọn k từ n

D. A different idea is Tích các số từ 1 đến n — Tích các số từ 1 đến n


**Q5. Which operation matches math.factorial(n)? — Mục đích của math.factorial(n) là gì?**

A. Another operation is used to Đếm cách chọn có thứ tự k từ n — Đếm cách chọn có thứ tự k từ n

B. It is used to Tính n!, n không âm — Tính n!, n không âm

C. Another operation is used to Đếm cách chọn không thứ tự — Đếm cách chọn không thứ tự

D. Another operation is used to Liệt kê kết quả khi n nhỏ — Liệt kê kết quả khi n nhỏ


**Q6. Which operation matches math.perm(n,k)? — Mục đích của math.perm(n,k) là gì?**

A. It is used to Đếm cách chọn có thứ tự k từ n — Đếm cách chọn có thứ tự k từ n

B. Another operation is used to Đếm cách chọn không thứ tự — Đếm cách chọn không thứ tự

C. Another operation is used to Liệt kê kết quả khi n nhỏ — Liệt kê kết quả khi n nhỏ

D. Another operation is used to Tính n!, n không âm — Tính n!, n không âm


**Q7. Which operation matches math.comb(n,k)? — Mục đích của math.comb(n,k) là gì?**

A. Another operation is used to Liệt kê kết quả khi n nhỏ — Liệt kê kết quả khi n nhỏ

B. Another operation is used to Tính n!, n không âm — Tính n!, n không âm

C. Another operation is used to Đếm cách chọn có thứ tự k từ n — Đếm cách chọn có thứ tự k từ n

D. It is used to Đếm cách chọn không thứ tự — Đếm cách chọn không thứ tự


**Q8. Which operation matches itertools.combinations/permutations? — Mục đích của itertools.combinations/permutations là gì?**

A. Another operation is used to Tính n!, n không âm — Tính n!, n không âm

B. Another operation is used to Đếm cách chọn có thứ tự k từ n — Đếm cách chọn có thứ tự k từ n

C. It is used to Liệt kê kết quả khi n nhỏ — Liệt kê kết quả khi n nhỏ

D. Another operation is used to Đếm cách chọn không thứ tự — Đếm cách chọn không thứ tự


**Q9. Why was the method chosen for scenario 1? — Vì sao chọn cách giải của tình huống 1?**

A. Another reason is Các thành viên không phân vai trò nên dùng tổ hợp — Các thành viên không phân vai trò nên dùng tổ hợp

B. Because Vị trí trưởng và phó khác nhau nên dùng hoán vị — Vị trí trưởng và phó khác nhau nên dùng hoán vị

C. Another reason is Thứ tự thực hiện làm kết quả khác nhau — Thứ tự thực hiện làm kết quả khác nhau

D. Another reason is Mỗi cặp môn học không cần phân biệt thứ tự — Mỗi cặp môn học không cần phân biệt thứ tự


**Q10. Why was the method chosen for scenario 2? — Vì sao chọn cách giải của tình huống 2?**

A. Because Các thành viên không phân vai trò nên dùng tổ hợp — Các thành viên không phân vai trò nên dùng tổ hợp

B. Another reason is Thứ tự thực hiện làm kết quả khác nhau — Thứ tự thực hiện làm kết quả khác nhau

C. Another reason is Mỗi cặp môn học không cần phân biệt thứ tự — Mỗi cặp môn học không cần phân biệt thứ tự

D. Another reason is Hệ số comb cho từng vị trí hàng n — Hệ số comb cho từng vị trí hàng n


**Q11. Why was the method chosen for scenario 3? — Vì sao chọn cách giải của tình huống 3?**

A. Another reason is Mỗi cặp môn học không cần phân biệt thứ tự — Mỗi cặp môn học không cần phân biệt thứ tự

B. Another reason is Hệ số comb cho từng vị trí hàng n — Hệ số comb cho từng vị trí hàng n

C. Another reason is Vị trí trưởng và phó khác nhau nên dùng hoán vị — Vị trí trưởng và phó khác nhau nên dùng hoán vị

D. Because Thứ tự thực hiện làm kết quả khác nhau — Thứ tự thực hiện làm kết quả khác nhau


**Q12. Why was the method chosen for scenario 4? — Vì sao chọn cách giải của tình huống 4?**

A. Another reason is Hệ số comb cho từng vị trí hàng n — Hệ số comb cho từng vị trí hàng n

B. Another reason is Vị trí trưởng và phó khác nhau nên dùng hoán vị — Vị trí trưởng và phó khác nhau nên dùng hoán vị

C. Because Mỗi cặp môn học không cần phân biệt thứ tự — Mỗi cặp môn học không cần phân biệt thứ tự

D. Another reason is Các thành viên không phân vai trò nên dùng tổ hợp — Các thành viên không phân vai trò nên dùng tổ hợp


**Q13. Why was the method chosen for scenario 5? — Vì sao chọn cách giải của tình huống 5?**

A. Another reason is Vị trí trưởng và phó khác nhau nên dùng hoán vị — Vị trí trưởng và phó khác nhau nên dùng hoán vị

B. Because Hệ số comb cho từng vị trí hàng n — Hệ số comb cho từng vị trí hàng n

C. Another reason is Các thành viên không phân vai trò nên dùng tổ hợp — Các thành viên không phân vai trò nên dùng tổ hợp

D. Another reason is Thứ tự thực hiện làm kết quả khác nhau — Thứ tự thực hiện làm kết quả khác nhau


**Q14. What input is used in scenario 1? — Tình huống 1 dùng dữ liệu gì?**

A. The data are 5 ứng viên, 2 vai trò — 5 ứng viên, 2 vai trò

B. Other data are 12 người, chọn 5 — 12 người, chọn 5

C. Other data are 3 bài test A B C — 3 bài test A B C

D. Other data are Ba môn Python AI SQL — Ba môn Python AI SQL


**Q15. What input is used in scenario 2? — Tình huống 2 dùng dữ liệu gì?**

A. Other data are 3 bài test A B C — 3 bài test A B C

B. Other data are Ba môn Python AI SQL — Ba môn Python AI SQL

C. Other data are Hàng n=4 — Hàng n=4

D. The data are 12 người, chọn 5 — 12 người, chọn 5


**Q16. What input is used in scenario 3? — Tình huống 3 dùng dữ liệu gì?**

A. Other data are Ba môn Python AI SQL — Ba môn Python AI SQL

B. Other data are Hàng n=4 — Hàng n=4

C. The data are 3 bài test A B C — 3 bài test A B C

D. Other data are 5 ứng viên, 2 vai trò — 5 ứng viên, 2 vai trò


**Q17. What input is used in scenario 4? — Tình huống 4 dùng dữ liệu gì?**

A. Other data are Hàng n=4 — Hàng n=4

B. The data are Ba môn Python AI SQL — Ba môn Python AI SQL

C. Other data are 5 ứng viên, 2 vai trò — 5 ứng viên, 2 vai trò

D. Other data are 12 người, chọn 5 — 12 người, chọn 5


**Q18. What input is used in scenario 5? — Tình huống 5 dùng dữ liệu gì?**

A. The data are Hàng n=4 — Hàng n=4

B. Other data are 5 ứng viên, 2 vai trò — 5 ứng viên, 2 vai trò

C. Other data are 12 người, chọn 5 — 12 người, chọn 5

D. Other data are 3 bài test A B C — 3 bài test A B C


**Q19. What information should a dataset have? — Dataset cần thông tin gì?**

A. Only a filename — Chỉ tên file

B. Only an editor font — Chỉ font soạn code

C. Only a line count — Chỉ số dòng

D. Meaning of rows, columns and units — Ý nghĩa hàng, cột và đơn vị


**Q20. After the program works, what comes next? — Sau khi code chạy đúng thì làm gì?**

A. Assume every input works — Cho rằng mọi đầu vào đều đúng

B. Erase validation — Xóa kiểm tra dữ liệu

C. Check the result and limitations — Kiểm tra kết quả và giới hạn

D. Ignore edge cases — Bỏ qua trường hợp biên

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **B** | It is Chọn có phân biệt thứ tự | Chọn có phân biệt thứ tự |
| Q2 | **A** | It is Chọn nhóm không xét thứ tự | Chọn nhóm không xét thứ tự |
| Q3 | **D** | It is Tích các số từ 1 đến n | Tích các số từ 1 đến n |
| Q4 | **C** | It is Số cách chọn k từ n | Số cách chọn k từ n |
| Q5 | **B** | It is used to Tính n!, n không âm | Tính n!, n không âm |
| Q6 | **A** | It is used to Đếm cách chọn có thứ tự k từ n | Đếm cách chọn có thứ tự k từ n |
| Q7 | **D** | It is used to Đếm cách chọn không thứ tự | Đếm cách chọn không thứ tự |
| Q8 | **C** | It is used to Liệt kê kết quả khi n nhỏ | Liệt kê kết quả khi n nhỏ |
| Q9 | **B** | Because Vị trí trưởng và phó khác nhau nên dùng hoán vị | Vị trí trưởng và phó khác nhau nên dùng hoán vị |
| Q10 | **A** | Because Các thành viên không phân vai trò nên dùng tổ hợp | Các thành viên không phân vai trò nên dùng tổ hợp |
| Q11 | **D** | Because Thứ tự thực hiện làm kết quả khác nhau | Thứ tự thực hiện làm kết quả khác nhau |
| Q12 | **C** | Because Mỗi cặp môn học không cần phân biệt thứ tự | Mỗi cặp môn học không cần phân biệt thứ tự |
| Q13 | **B** | Because Hệ số comb cho từng vị trí hàng n | Hệ số comb cho từng vị trí hàng n |
| Q14 | **A** | The data are 5 ứng viên, 2 vai trò | 5 ứng viên, 2 vai trò |
| Q15 | **D** | The data are 12 người, chọn 5 | 12 người, chọn 5 |
| Q16 | **C** | The data are 3 bài test A B C | 3 bài test A B C |
| Q17 | **B** | The data are Ba môn Python AI SQL | Ba môn Python AI SQL |
| Q18 | **A** | The data are Hàng n=4 | Hàng n=4 |
| Q19 | **D** | Meaning of rows, columns and units | Ý nghĩa hàng, cột và đơn vị |
| Q20 | **C** | Check the result and limitations | Kiểm tra kết quả và giới hạn |

## 8. Nối sang bài tiếp

`Nguyên lý đếm → hoán vị/tổ hợp → phân phối nhị thức`.

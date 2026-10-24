# PY-22 — Hoán vị, tổ hợp và tam giác Pascal


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

## 4. Khái niệm liên quan

Khi chọn người hoặc sắp xếp công việc, câu hỏi đầu tiên là **đổi thứ tự có tạo ra kết quả khác không?** Nếu có, ta đếm các cách sắp xếp bằng **hoán vị**; nếu không, ta đếm **tổ hợp**. **Giai thừa** là phép nhân nền tảng để tính những số cách đó, còn **hệ số nhị thức** tạo nên các hàng của tam giác Pascal.

### 4.1. Permutation — Chọn và phân vai có thứ tự

**Từ vựng trong mục:** **Permutation** — chỉnh hợp/hoán vị có thứ tự; **Order** — thứ tự.

Có năm ứng viên và hai vị trí **khác nhau** là trưởng nhóm, phó nhóm. Chọn trưởng có 5 cách; sau đó chọn phó còn 4 cách, nên có `5 × 4 = 20` phương án. Đảo vai trò hai người tạo phương án khác. `math.perm(n,k)` đếm cách lấy **k người khác nhau từ n người** và phân thứ tự, với `0 ≤ k ≤ n`. Nếu dùng hết n người, kết quả là `n!`.

```python
import math

print(math.perm(5, 2))
```

**Kết quả khi chạy:**

```text
20
```

Có 20 cách phân vai trưởng/phó; đổi thứ tự hai người được tính là cách khác.

### 4.2. Combination — Chọn nhóm không phân vai

**Từ vựng trong mục:** **Combination** — tổ hợp; **Order-independent** — không xét thứ tự.

Nếu năm ứng viên chỉ cần chọn **hai người cùng một đội**, cặp An–Bình và Bình–An là **một** đội, không phải hai. Công thức `C(n,k) = n! / (k!(n-k)!)`; với 5 chọn 2 có 10 nhóm. `math.comb(n,k)` tính trực tiếp số nhóm mà không cần liệt kê từng cặp. Trong thực tế cần xác nhận có được chọn một người nhiều lần hay không; ở đây mỗi ứng viên chỉ chọn tối đa một lần.

```python
import math

print(math.comb(5, 2))
```

**Kết quả khi chạy:**

```text
10
```

Số nhóm bằng nửa số cách phân vai hai người vì hoán đổi hai vai không tạo đội mới.

### 4.3. Factorial — Sắp xếp tất cả phần tử

**Từ vựng trong mục:** **Factorial** — giai thừa; **Arrangement** — thứ tự sắp xếp.

Với bốn nhiệm vụ **khác nhau**, có 4 cách chọn việc đầu, 3 cách chọn việc thứ hai, rồi 2 và 1. Tổng số cách sắp xếp là `4! = 4×3×2×1 = 24`. Đây là **giai thừa**. Quy ước `0! = 1` vì có đúng một cách sắp xếp dãy rỗng. `math.factorial` áp dụng cho số nguyên không âm.

```python
import math

print(math.factorial(4))
```

**Kết quả khi chạy:**

```text
24
```

Bốn nhiệm vụ khác nhau có 24 thứ tự thực hiện nếu mỗi nhiệm vụ xuất hiện đúng một lần.

### 4.4. Binomial coefficient và tam giác Pascal

**Từ vựng trong mục:** **Binomial coefficient** — hệ số nhị thức; **Pascal triangle** — tam giác Pascal.

**Hệ số nhị thức** `C(n,k)` là số cách chọn k phần tử không xét thứ tự, đồng thời là hệ số của `a^(n-k)b^k` trong khai triển `(a+b)^n`. Các giá trị `C(n,0)` đến `C(n,n)` tạo thành **hàng n của tam giác Pascal** (đếm từ hàng 0). Với n = 4, hàng có năm hệ số `1,4,6,4,1`; hai cạnh bằng 1 và mỗi ô trong bằng tổng hai ô ngay phía trên.

```python
import math

print([math.comb(4, k) for k in range(5)])
```

**Kết quả khi chạy:**

```text
[1, 4, 6, 4, 1]
```

Hàng thứ tư tính từ 0 có năm hệ số, ứng với k từ 0 đến 4.
## 5. Năm vấn đề thực tế

### Tình huống 1 — Chọn trưởng và phó nhóm

**Từ vựng trong mục:** **Permutation** — hoán vị.

**Tình huống thực tế:** Ban tổ chức có 5 ứng viên và cần chọn một trưởng nhóm, một phó nhóm, hai vị trí khác nhau. Có bao nhiêu cách chọn?

**Vì sao chọn cách giải này?** Hai vai trò khác nhau nên phải tính số cách có thứ tự, dùng `perm`.


**Quy trình giải:**

1. Xác định trưởng nhóm và phó nhóm là hai vị trí khác nhau.
2. Chọn trưởng trong năm người rồi phó trong bốn người còn lại.
3. Nhân 5×4 hoặc gọi `math.perm(5,2)` để đếm.

```python
import math
print(math.perm(5,2))
```

**Kết quả khi chạy:**

```text
20
```

### Tình huống 2 — Chọn đội thi

**Từ vựng trong mục:** **Combination** — tổ hợp.

**Tình huống thực tế:** Một đội thi cần chọn 5 người từ 12 ứng viên; vai trò của người được chọn không phân biệt. Có bao nhiêu đội?

**Vì sao chọn cách giải này?** Không phân vai nên mỗi nhóm năm người chỉ được đếm một lần, dùng `comb`.


**Quy trình giải:**

1. Ghi nhận đội có năm thành viên và có 12 ứng viên.
2. Xác định thứ tự thành viên không quan trọng.
3. Gọi `math.comb(12,5)` để đếm các đội khác nhau.

```python
import math
print(math.comb(12,5))
```

**Kết quả khi chạy:**

```text
792
```

### Tình huống 3 — Sắp thứ tự kiểm thử

**Từ vựng trong mục:** **Factorial** — giai thừa.

**Tình huống thực tế:** Bộ kiểm thử có ba tác vụ A, B, C; cần thử mọi thứ tự thực hiện. Liệt kê các thứ tự.

**Vì sao chọn cách giải này?** Đề yêu cầu toàn bộ thứ tự của ba tác vụ, nên cần hoán vị độ dài ba và nhận `3!` kết quả.


**Quy trình giải:**

1. Tạo ba tác vụ A, B, C, mỗi tác vụ phải xuất hiện một lần.
2. Dùng `itertools.permutations(tasks)` không truyền độ dài để lấy đủ ba tác vụ.
3. In sáu thứ tự; đối chiếu `3! = 6`.

```python
from itertools import permutations
print(list(permutations(['A', 'B', 'C'])))
```

**Kết quả khi chạy:**

```text
[('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
```

### Tình huống 4 — Đề xuất cặp môn học

**Từ vựng trong mục:** **Binomial coefficient** — hệ số nhị thức.

**Tình huống thực tế:** Nhóm học chọn hai môn trong ba môn Python, AI, SQL; thứ tự không quan trọng. Liệt kê các cặp môn.

**Vì sao chọn cách giải này?** Cặp môn không có thứ tự, vì vậy `combinations` không nhân đôi những cặp đảo chiều.


**Quy trình giải:**

1. Lưu ba môn Python, AI, SQL vào List.
2. Dùng `combinations(subjects,2)` vì không phân biệt hai thứ tự trong cùng cặp.
3. In ba cặp môn có thể chọn.

```python
from itertools import combinations
print(list(combinations(["Python","AI","SQL"],2)))
```

**Kết quả khi chạy:**

```text
[('Python', 'AI'), ('Python', 'SQL'), ('AI', 'SQL')]
```

### Tình huống 5 — Tính hàng Pascal

**Từ vựng trong mục:** **Permutation** — hoán vị.

**Tình huống thực tế:** Giáo viên cần viết hàng n=4 của tam giác Pascal bằng C(4,k), k từ 0 đến 4.

**Vì sao chọn cách giải này?** Các giá trị của tam giác Pascal chính là các hệ số nhị thức `C(n,k)`.


**Quy trình giải:**

1. Chọn hàng n=4 của tam giác Pascal.
2. Tính các hệ số `math.comb(4,k)` với k=0..4.
3. In năm giá trị và kiểm tra tính đối xứng.

```python
import math
print([math.comb(4,k) for k in range(5)])
```

**Kết quả khi chạy:**

```text
[1, 4, 6, 4, 1]
```

## 6. Sai lầm thường gặp

- Phân biệt bài toán **có thứ tự** (`perm`) với **không xét thứ tự** (`comb`).
- `itertools.permutations(items,2)` chỉ tạo các cặp có thứ tự, không phải sắp xếp toàn bộ ba phần tử; không truyền k để lấy toàn bộ.
- Cả `math.perm` và `math.comb` giả định các phần tử phân biệt và không chọn trùng một phần tử.
- `math.factorial` cần số nguyên không âm; `0! = 1`.
- `itertools` để **liệt kê** các phương án; `math` giúp **đếm** khi số phương án quá lớn không nên liệt kê.

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

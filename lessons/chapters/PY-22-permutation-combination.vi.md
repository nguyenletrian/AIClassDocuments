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

**Q1. When should permutations be used? — Khi nào dùng hoán vị/chỉnh hợp?**

A. When order matters — Khi thứ tự quan trọng

B. When order does not matter — Khi thứ tự không quan trọng

C. The product 1×2×…×n — Tích 1×2×…×n

D. The number of unordered k-subsets from n distinct items — Số nhóm k phần tử không xét thứ tự từ n phần tử khác nhau

**Q2. When should combinations be used? — Khi nào dùng tổ hợp?**

A. When order matters — Khi thứ tự quan trọng

B. When order does not matter — Khi thứ tự không quan trọng

C. The product 1×2×…×n — Tích 1×2×…×n

D. The number of unordered k-subsets from n distinct items — Số nhóm k phần tử không xét thứ tự từ n phần tử khác nhau

**Q3. What is factorial n!? — Giai thừa n! là gì?**

A. When order matters — Khi thứ tự quan trọng

B. When order does not matter — Khi thứ tự không quan trọng

C. The product 1×2×…×n — Tích 1×2×…×n

D. The number of unordered k-subsets from n distinct items — Số nhóm k phần tử không xét thứ tự từ n phần tử khác nhau

**Q4. What is a binomial coefficient C(n,k)? — Hệ số nhị thức C(n,k) là gì?**

A. When order matters — Khi thứ tự quan trọng

B. When order does not matter — Khi thứ tự không quan trọng

C. The product 1×2×…×n — Tích 1×2×…×n

D. The number of unordered k-subsets from n distinct items — Số nhóm k phần tử không xét thứ tự từ n phần tử khác nhau

**Q5. Which function counts ordered selections? — Hàm nào đếm cách chọn có thứ tự?**

A. `math.perm(n, k)` — `math.perm(n, k)`

B. `math.comb(n, k)` — `math.comb(n, k)`

C. `math.factorial(n)` — `math.factorial(n)`

D. `itertools.permutations(items)` — `itertools.permutations(items)`

**Q6. Which function counts unordered selections? — Hàm nào đếm cách chọn không thứ tự?**

A. `math.perm(n, k)` — `math.perm(n, k)`

B. `math.comb(n, k)` — `math.comb(n, k)`

C. `math.factorial(n)` — `math.factorial(n)`

D. `itertools.permutations(items)` — `itertools.permutations(items)`

**Q7. Which function calculates n!? — Hàm nào tính n!?**

A. `math.perm(n, k)` — `math.perm(n, k)`

B. `math.comb(n, k)` — `math.comb(n, k)`

C. `math.factorial(n)` — `math.factorial(n)`

D. `itertools.permutations(items)` — `itertools.permutations(items)`

**Q8. Which function lists all ordered arrangements? — Hàm nào liệt kê các cách sắp xếp có thứ tự?**

A. `math.perm(n, k)` — `math.perm(n, k)`

B. `math.comb(n, k)` — `math.comb(n, k)`

C. `math.factorial(n)` — `math.factorial(n)`

D. `itertools.permutations(items)` — `itertools.permutations(items)`

**Q9. What is the value of 0!? — 0! bằng bao nhiêu?**

A. 1 — 1

B. 6 — 6

C. 6 pairs — 6 cặp

D. 12 pairs — 12 cặp

**Q10. How many full orderings of three distinct items exist? — Ba phần tử phân biệt có bao nhiêu thứ tự đầy đủ?**

A. 1 — 1

B. 6 — 6

C. 6 pairs — 6 cặp

D. 12 pairs — 12 cặp

**Q11. How many unordered pairs can be chosen from four distinct items? — Chọn cặp không thứ tự từ bốn phần tử có bao nhiêu cách?**

A. 1 — 1

B. 6 — 6

C. 6 pairs — 6 cặp

D. 12 pairs — 12 cặp

**Q12. How many ordered pairs can be formed from four distinct items without repetition? — Từ bốn phần tử phân biệt có bao nhiêu cặp có thứ tự không lặp?**

A. 1 — 1

B. 6 — 6

C. 6 pairs — 6 cặp

D. 12 pairs — 12 cặp

**Q13. What identity relates combinations and permutations? — Công thức nào liên hệ tổ hợp và chỉnh hợp?**

A. P(n,k)=C(n,k)×k! — P(n,k)=C(n,k)×k!

B. 1 — 1

C. 1 — 1

D. Each inner entry sums two entries directly above — Mỗi ô bên trong bằng tổng hai ô ngay phía trên

**Q14. What is C(n,0)? — C(n,0) bằng gì?**

A. P(n,k)=C(n,k)×k! — P(n,k)=C(n,k)×k!

B. 1 — 1

C. 1 — 1

D. Each inner entry sums two entries directly above — Mỗi ô bên trong bằng tổng hai ô ngay phía trên

**Q15. What is C(n,n)? — C(n,n) bằng gì?**

A. P(n,k)=C(n,k)×k! — P(n,k)=C(n,k)×k!

B. 1 — 1

C. 1 — 1

D. Each inner entry sums two entries directly above — Mỗi ô bên trong bằng tổng hai ô ngay phía trên

**Q16. How are entries in Pascal's triangle obtained? — Các ô trong tam giác Pascal được tạo ra sao?**

A. P(n,k)=C(n,k)×k! — P(n,k)=C(n,k)×k!

B. 1 — 1

C. 1 — 1

D. Each inner entry sums two entries directly above — Mỗi ô bên trong bằng tổng hai ô ngay phía trên

**Q17. What does `itertools.combinations(items,2)` list? — `itertools.combinations(items,2)` liệt kê gì?**

A. Unordered two-item groups — Nhóm hai phần tử không xét thứ tự

B. Ordered two-item arrangements — Cặp hai phần tử có thứ tự

C. It returns zero — Hàm trả về 0

D. The number grows factorially — Số cách tăng theo giai thừa

**Q18. What does `itertools.permutations(items,2)` list? — `itertools.permutations(items,2)` liệt kê gì?**

A. Unordered two-item groups — Nhóm hai phần tử không xét thứ tự

B. Ordered two-item arrangements — Cặp hai phần tử có thứ tự

C. It returns zero — Hàm trả về 0

D. The number grows factorially — Số cách tăng theo giai thừa

**Q19. What happens if k>n in `math.comb(n,k)` for nonnegative integers? — Nếu k>n trong math.comb với số nguyên không âm thì sao?**

A. Unordered two-item groups — Nhóm hai phần tử không xét thứ tự

B. Ordered two-item arrangements — Cặp hai phần tử có thứ tự

C. It returns zero — Hàm trả về 0

D. The number grows factorially — Số cách tăng theo giai thừa

**Q20. Why avoid materializing all permutations for large n? — Vì sao tránh liệt kê toàn bộ hoán vị khi n lớn?**

A. Unordered two-item groups — Nhóm hai phần tử không xét thứ tự

B. Ordered two-item arrangements — Cặp hai phần tử có thứ tự

C. It returns zero — Hàm trả về 0

D. The number grows factorially — Số cách tăng theo giai thừa

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **A** | Reordering selected people produces a different arrangement. | Đổi thứ tự người được chọn tạo cách sắp khác. |
| Q2 | **B** | A group remains the same after members swap positions. | Nhóm không đổi khi thành viên đổi chỗ. |
| Q3 | **C** | Factorial counts arrangements of n distinct items. | Giai thừa đếm cách sắp xếp n phần tử phân biệt. |
| Q4 | **D** | C(n,k) is also a coefficient in (a+b)^n. | C(n,k) còn là hệ số trong khai triển (a+b)^n. |
| Q5 | **A** | perm counts arrangements without replacement. | perm đếm cách chọn có thứ tự không lặp. |
| Q6 | **B** | comb counts distinct groups rather than arrangements. | comb đếm các nhóm khác nhau, không xét sắp xếp. |
| Q7 | **C** | factorial multiplies integers from one through n. | factorial nhân các số nguyên từ một tới n. |
| Q8 | **D** | Without r, permutations enumerates complete orderings. | Không truyền r, permutations liệt kê toàn bộ thứ tự. |
| Q9 | **A** | The empty arrangement has exactly one possible order. | Dãy rỗng có một cách sắp xếp. |
| Q10 | **B** | 3! = 3×2×1 = 6. | 3! = 3×2×1 = 6. |
| Q11 | **C** | C(4,2)=6. | C(4,2)=6. |
| Q12 | **D** | 4×3 = 12. | 4×3 = 12. |
| Q13 | **A** | Each chosen group can be arranged in k! orders. | Mỗi nhóm k người có k! cách sắp. |
| Q14 | **B** | There is one way to choose nobody. | Có một cách chọn tập rỗng. |
| Q15 | **C** | There is one way to select every available item. | Có một cách lấy toàn bộ n phần tử. |
| Q16 | **D** | Pascal's identity is C(n,k)=C(n−1,k−1)+C(n−1,k). | Hệ thức Pascal cộng hai hệ số ở hàng trước. |
| Q17 | **A** | It emits each distinct pair once. | Hàm tạo mỗi cặp khác nhau đúng một lần. |
| Q18 | **B** | Reversing a pair yields a different result. | Đổi thứ tự hai phần tử tạo kết quả khác. |
| Q19 | **C** | No k-subset exists when fewer than k items are available. | Không thể chọn k phần tử nếu tổng phần tử ít hơn k. |
| Q20 | **D** | n! quickly becomes too large to store or display. | n! tăng nhanh khiến không thể lưu hoặc in hết. |

## 8. Nối sang bài tiếp

`Nguyên lý đếm → hoán vị/tổ hợp → phân phối nhị thức`.

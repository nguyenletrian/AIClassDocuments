# PY-20 — Logic mệnh đề, bảng chân trị và quy tắc đếm


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Proposition** — mệnh đề; **Truth table** — bảng chân trị.

`Boolean → logic mệnh đề → tổ hợp → xác suất`

Sau các điều kiện `if`, ta tìm hiểu vì sao phép `and`, `or`, `not` cho kết quả đúng hoặc sai và cách đếm số lựa chọn có thể xảy ra.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Giải thích |
|---|---|---|
| Proposition | mệnh đề | Câu có giá trị True hoặc False |
| Truth table | bảng chân trị | Liệt kê kết quả ứng với mọi tổ hợp logic |
| Implication | kéo theo | Quan hệ P⇒Q tương đương (not P) or Q |
| Counting | nguyên lý đếm | Đếm số khả năng khi ghép lựa chọn |

## 3. Hàm Python và tham số

**Từ vựng trong mục:** **Function** — hàm; **Parameter** — tham số.

| Hàm / cú pháp | Vì sao dùng |
|---|---|
| `and/or/not` | Ghép điều kiện, chọn ít nhất một hoặc phủ định |
| `(not p) or q` | Biểu diễn phép kéo theo P⇒Q |
| `itertools.product(A,B)` | Tạo tích Descartes của hai tập tùy chọn |
| `math.prod(counts)` | Nhân số lựa chọn từng bước độc lập |

## 4. Khái niệm liên quan

**Logic mệnh đề** giúp chương trình quyết định đúng/sai theo quy tắc rõ ràng; **bảng chân trị** giúp kiểm tra tất cả trường hợp của nhiều điều kiện; **phép kéo theo** biểu diễn quy định “nếu… thì…”. Khi phải đếm các lựa chọn có thể xảy ra, **nguyên lý cộng và nhân** cho kết quả mà không cần thử bằng tay từng cách.

### 4.1. Proposition — Phát biểu đúng hoặc sai

**Từ vựng trong mục:** **Proposition** — mệnh đề; **Boolean** — đúng/sai.

**Mệnh đề** là một phát biểu có giá trị đúng hoặc sai xác định. Chẳng hạn `3 > 1` là đúng, còn `3 < 1` là sai; trong Python, hai kết quả được biểu diễn bằng `True` và `False`. Không phải mọi câu đều là mệnh đề: câu hỏi “Bạn khỏe không?” chưa mang một giá trị đúng/sai để tính toán. Ta dùng mệnh đề khi viết điều kiện kiểm tra truy cập hoặc quy tắc vận hành.

```python
print(3 > 1)
```

**Kết quả khi chạy:**

```text
True
```

Mệnh đề `3 > 1` đúng vì số 3 lớn hơn 1; `print` hiển thị Boolean `True`.

### 4.2. Truth table — Bảng chân trị

**Từ vựng trong mục:** **Truth table** — bảng chân trị; **AND/OR/NOT** — và/hoặc/phủ định.

**Bảng chân trị** liệt kê mọi kết hợp đúng/sai có thể có của các điều kiện. Với hai biến p, q, mỗi biến có hai trạng thái nên có `2×2 = 4` cặp. `p and q` chỉ đúng khi cả hai đúng; `p or q` đúng nếu **ít nhất một** đúng; `not p` đảo đúng thành sai và ngược lại. Bảng giúp kiểm tra quy tắc ngay cả ở trường hợp khó nhận ra bằng trực giác.

```python
for p in [True, False]:
    for q in [True, False]:
        print(p, q, p and q, p or q)
```

**Kết quả khi chạy:**

```text
True True True True
True False False True
False True False True
False False False False
```

Hai cột đầu là đầu vào p, q; cột thứ ba là AND; cột cuối là OR. Bốn dòng bao phủ mọi trường hợp.

### 4.3. Implication — Nếu p thì q

**Từ vựng trong mục:** **Implication** — kéo theo; **Premise/conclusion** — tiền đề/kết luận.

**Mệnh đề kéo theo** `p ⇒ q` diễn đạt “nếu p thì q”, trong đó p là tiền đề và q là kết luận. Nó **chỉ sai** khi p đúng mà q sai. Ví dụ quy định “nếu đơn được phê duyệt (p), đơn phải có chữ ký (q)”: phê duyệt `True` nhưng có chữ ký `False` là vi phạm. Trong Python ta viết `(not p) or q`. Lưu ý đây là cách kiểm tra logic, không tự chứng minh quan hệ nguyên nhân.

```python
approved = True
signed = False
print((not approved) or signed)
```

**Kết quả khi chạy:**

```text
False
```

Đã phê duyệt nhưng chưa ký nên quy tắc kéo theo không được thỏa mãn.

### 4.4. Counting — Nguyên lý cộng và nhân

**Từ vựng trong mục:** **Counting** — quy tắc đếm; **Product** — tích Descartes.

**Nguyên lý nhân**: nếu có 3 cách chọn màu và mỗi màu đều có 4 cỡ, số cặp (màu, cỡ) là `3×4 = 12`. **Nguyên lý cộng** áp dụng cho lựa chọn thuộc **một trong các nhóm không trùng nhau**: có 3 mẫu áo hoặc 4 mẫu quần để chọn **một món**, tổng cộng 7 cách. Nếu các nhóm có phần giao, phải trừ phần bị đếm lặp; bài tiếp theo sẽ học kỹ phép bao hàm–loại trừ. `itertools.product` liệt kê từng cặp thay vì chỉ đếm.

```python
colors = 3
sizes = 4
print(colors * sizes)
```

**Kết quả khi chạy:**

```text
12
```

Có 12 cách chọn một màu và một cỡ khi mọi màu đều có đủ bốn cỡ.

## 5. Năm tình huống lập trình thực tế

### Tình huống 1 — Điều kiện đăng nhập

**Từ vựng trong mục:** **Proposition** — mệnh đề; **AND** — và.

**Tình huống thực tế:** Một cổng học tập chỉ cho mở nội dung khi người dùng đã đăng nhập và xác minh tài khoản. Trong lần kiểm tra này `logged_in=True`, `verified=False`. In kết quả người dùng có được quyền truy cập hay không.

**Vì sao chọn cách giải này?** Toán tử `and` chỉ cho `True` khi cả hai điều kiện đều đúng.

**Quy trình giải:** Đặt hai trạng thái Boolean → nối chúng bằng `and` → in kết quả.

```python
logged_in, verified = True, False
print(logged_in and verified)
```

**Kết quả khi chạy:**

```text
False
```

**Giải thích kết quả:** `False` — tài khoản đã đăng nhập nhưng chưa xác minh.

### Tình huống 2 — Bảng chân trị

**Từ vựng trong mục:** **Truth table** — bảng chân trị; **OR** — hoặc.

**Tình huống thực tế:** Nhân viên kiểm thử muốn lập bảng chân trị cho `p and q` và `p or q`, trong đó `p`, `q` đều có thể là `True` hoặc `False`. In tất cả bốn tổ hợp của p và q cùng kết quả của hai phép logic.

**Vì sao chọn cách giải này?** Hai vòng `for` lồng nhau tạo đủ 2 × 2 tổ hợp.

**Quy trình giải:** Duyệt p theo hai trạng thái → với mỗi p duyệt q → in p, q, p and q, p or q.

```python
for p in [True, False]:
    for q in [True, False]:
        print(p, q, p and q, p or q)
```

**Kết quả khi chạy:**

```text
True True True True
True False False True
False True False True
False False False False
```

**Giải thích kết quả:** Bốn dòng cho đủ các trường hợp; `and` chỉ đúng khi cả hai đúng, `or` đúng khi ít nhất một đúng.

### Tình huống 3 — Kiểm quy tắc kéo theo

**Từ vựng trong mục:** **Implication** — kéo theo; **Premise** — tiền đề.

**Tình huống thực tế:** Một quy định nội bộ phát biểu: “Nếu đã được phê duyệt (p) thì phải có chứng nhận (q)”. Có trường hợp `p=True` nhưng `q=False`. Kiểm tra quy tắc kéo theo có được đáp ứng không.

**Vì sao chọn cách giải này?** `(not p) or q` tương đương phép kéo theo và nhận `False` khi tiền đề đúng nhưng kết luận sai.

**Quy trình giải:** Gán p=True, q=False → tính `(not p) or q` → in kết quả.

```python
p, q = True, False
print((not p) or q)
```

**Kết quả khi chạy:**

```text
False
```

**Giải thích kết quả:** `False` — trường hợp này vi phạm quy tắc.

### Tình huống 4 — Cấu hình áo

**Từ vựng trong mục:** **Counting** — nguyên lý đếm; **Combination** — cách kết hợp.

**Tình huống thực tế:** Cửa hàng cho khách chọn 1 trong 3 màu áo và 1 trong 4 cỡ; mọi màu đều có đủ bốn cỡ. Tính số cách chọn một màu và một cỡ.

**Vì sao chọn cách giải này?** Nguyên lý nhân phù hợp khi mỗi lựa chọn màu kết hợp được với mọi lựa chọn cỡ.

**Quy trình giải:** Lấy số màu nhân số cỡ: 3 × 4 → in tổng số kết hợp.

```python
print(3 * 4)
```

**Kết quả khi chạy:**

```text
12
```

**Giải thích kết quả:** `12` cách chọn.

### Tình huống 5 — Ghép các tùy chọn

**Từ vựng trong mục:** **Cartesian product** — tích Descartes; **Option** — lựa chọn.

**Tình huống thực tế:** Cửa hàng bán áo có hai màu `red`, `blue` và hai cỡ `S`, `M`, mọi màu đều có đủ hai cỡ. In danh sách cụ thể tất cả cặp (màu, cỡ).

**Vì sao chọn cách giải này?** `itertools.product` liệt kê tích Descartes, khác với chỉ đếm bằng phép nhân.

**Quy trình giải:** Tạo list hai màu và hai cỡ → dùng `product` → chuyển sang list và in.

```python
from itertools import product
print(list(product(["red", "blue"], ["S", "M"])))
```

**Kết quả khi chạy:**

```text
[('red', 'S'), ('red', 'M'), ('blue', 'S'), ('blue', 'M')]
```

**Giải thích kết quả:** Bốn cặp: `(red,S)`, `(red,M)`, `(blue,S)`, `(blue,M)`.

## 6. Sai lầm thường gặp

- Không nhầm `and` (cả hai đúng) với `or` (ít nhất một đúng); `not` đảo giá trị Boolean.
- Phép kéo theo `p ⇒ q` chỉ sai khi `p=True`, `q=False`; tiền đề sai không tự chứng minh kết luận đúng.
- Bảng chân trị hai biến có bốn tổ hợp; nếu thiếu một tổ hợp, kiểm tra logic có thể bỏ sót lỗi.
- Nguyên lý **nhân** đếm lựa chọn theo nhiều bước kết hợp được với nhau; nguyên lý **cộng** đếm các phương án thay thế không trùng. Nếu trùng phải điều chỉnh số đếm.
- Set không bảo đảm thứ tự in, còn kết quả `itertools.product` gồm các tuple theo thứ tự nguồn đã đưa vào.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is a proposition? — Mệnh đề là gì?**

A. A statement that is either true or false — Phát biểu có thể xác định đúng hoặc sai

B. A table of all input truth-value combinations — Bảng các tổ hợp giá trị đúng/sai đầu vào

C. The logical conditional 'if p then q' — Điều kiện logic 'nếu p thì q'

D. Multiply choice counts across sequential stages when each earlier choice permits the stated number of later choices — Nhân số cách chọn qua các bước khi mỗi lựa chọn trước cho phép đúng số cách ở bước sau

**Q2. What is a truth table? — Bảng chân trị là gì?**

A. A statement that is either true or false — Phát biểu có thể xác định đúng hoặc sai

B. A table of all input truth-value combinations — Bảng các tổ hợp giá trị đúng/sai đầu vào

C. The logical conditional 'if p then q' — Điều kiện logic 'nếu p thì q'

D. Multiply the numbers of sequential independent choices — Nhân số lựa chọn qua các bước kết hợp đầy đủ

**Q3. What is logical implication `p ⇒ q`? — Phép kéo theo `p ⇒ q` là gì?**

A. A statement that is either true or false — Phát biểu có thể xác định đúng hoặc sai

B. A table of all input truth-value combinations — Bảng các tổ hợp giá trị đúng/sai đầu vào

C. The logical conditional 'if p then q' — Điều kiện logic 'nếu p thì q'

D. Multiply the numbers of sequential independent choices — Nhân số lựa chọn qua các bước kết hợp đầy đủ

**Q4. What is the multiplication counting principle? — Nguyên lý nhân trong đếm là gì?**

A. A statement that is either true or false — Phát biểu có thể xác định đúng hoặc sai

B. A table of all input truth-value combinations — Bảng các tổ hợp giá trị đúng/sai đầu vào

C. The logical conditional 'if p then q' — Điều kiện logic 'nếu p thì q'

D. Multiply the numbers of sequential independent choices — Nhân số lựa chọn qua các bước kết hợp đầy đủ

**Q5. When is `p and q` true? — Khi nào `p and q` đúng?**

A. When both p and q are true — Khi p và q đều đúng

B. When at least one of p or q is true — Khi có ít nhất một trong p hoặc q đúng

C. Reverses the truth value of p — Đảo giá trị đúng/sai của p

D. When p is true and q is false — Khi p đúng và q sai

**Q6. When is `p or q` true? — Khi nào `p or q` đúng?**

A. When both p and q are true — Khi p và q đều đúng

B. When at least one of p or q is true — Khi có ít nhất một trong p hoặc q đúng

C. Reverses the truth value of p — Đảo giá trị đúng/sai của p

D. When p is true and q is false — Khi p đúng và q sai

**Q7. What does `not p` do? — `not p` làm gì?**

A. When both p and q are true — Khi p và q đều đúng

B. When at least one of p or q is true — Khi có ít nhất một trong p hoặc q đúng

C. Reverses the truth value of p — Đảo giá trị đúng/sai của p

D. When p is true and q is false — Khi p đúng và q sai

**Q8. When is `p ⇒ q` false? — Khi nào `p ⇒ q` sai?**

A. When both p and q are true — Khi p và q đều đúng

B. When at least one of p or q is true — Khi có ít nhất một trong p hoặc q đúng

C. Reverses the truth value of p — Đảo giá trị đúng/sai của p

D. When p is true and q is false — Khi p đúng và q sai

**Q9. How many rows does a truth table with two variables have? — Bảng chân trị hai biến có mấy hàng?**

A. 4 — 4

B. 8 — 8

C. 2 — 2

D. 16 — 16

**Q10. How many rows does a truth table with three variables have? — Bảng chân trị ba biến có mấy hàng?**

A. 4 — 4

B. 8 — 8

C. 2 — 2

D. 16 — 16

**Q11. How many rows does a truth table with one variable have? — Bảng chân trị một biến có mấy hàng?**

A. 4 — 4

B. 8 — 8

C. 2 — 2

D. 16 — 16

**Q12. How many rows does a truth table with four variables have? — Bảng chân trị bốn biến có mấy hàng?**

A. 4 — 4

B. 8 — 8

C. 2 — 2

D. 16 — 16

**Q13. Which expression is equivalent to implication `p ⇒ q`? — Biểu thức nào tương đương `p ⇒ q`?**

A. `(not p) or q` — `(not p) or q`

B. `(True, False)` — `(True, False)`

C. `False` — `False`

D. `True` — `True`

**Q14. Which input pair makes `p ⇒ q` false? — Cặp p, q nào làm `p ⇒ q` sai?**

A. `(not p) or q` — `(not p) or q`

B. `(True, False)` — `(True, False)`

C. `False` — `False`

D. `True` — `True`

**Q15. What is `True and False`? — `True and False` bằng gì?**

A. `(not p) or q` — `(not p) or q`

B. `(True, False)` — `(True, False)`

C. `False` — `False`

D. `True` — `True`

**Q16. What is `False or True`? — `False or True` bằng gì?**

A. `(not p) or q` — `(not p) or q`

B. `(True, False)` — `(True, False)`

C. `False` — `False`

D. `True` — `True`

**Q17. When does the addition counting principle apply directly? — Khi nào có thể áp dụng trực tiếp nguyên lý cộng?**

A. When alternatives are disjoint — Khi các phương án thay thế không trùng nhau

B. When each step has the stated choices for every earlier selection — Khi mỗi bước có đủ số lựa chọn với mọi lựa chọn trước đó

C. All ordered pairs taking one element from each input — Mọi cặp có thứ tự gồm một phần tử từ mỗi nguồn

D. When some outcomes belong to more than one counted group — Khi một kết quả nằm trong nhiều nhóm được đếm

**Q18. When can choices be counted by multiplying options? — Khi nào có thể đếm bằng phép nhân?**

A. When alternatives are disjoint — Khi các phương án thay thế không trùng nhau

B. When each step has the stated choices for every earlier selection — Khi mỗi bước có đủ số lựa chọn với mọi lựa chọn trước đó

C. All ordered pairs taking one element from each input — Mọi cặp có thứ tự gồm một phần tử từ mỗi nguồn

D. When some outcomes belong to more than one counted group — Khi một kết quả nằm trong nhiều nhóm được đếm

**Q19. What does `itertools.product(A, B)` generate? — `itertools.product(A, B)` tạo gì?**

A. When alternatives are disjoint — Khi các phương án thay thế không trùng nhau

B. When each step has the stated choices for every earlier selection — Khi mỗi bước có đủ số lựa chọn với mọi lựa chọn trước đó

C. All ordered pairs taking one element from each input — Mọi cặp có thứ tự gồm một phần tử từ mỗi nguồn

D. When some outcomes belong to more than one counted group — Khi một kết quả nằm trong nhiều nhóm được đếm

**Q20. When should overlapping alternatives be adjusted during counting? — Khi nào cần điều chỉnh phần giao khi đếm?**

A. When alternatives are disjoint — Khi các phương án thay thế không trùng nhau

B. When each step has the stated choices for every earlier selection — Khi mỗi bước có đủ số lựa chọn với mọi lựa chọn trước đó

C. All ordered pairs taking one element from each input — Mọi cặp có thứ tự gồm một phần tử từ mỗi nguồn

D. When some outcomes belong to more than one counted group — Khi một kết quả nằm trong nhiều nhóm được đếm

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **A** | A proposition has a definite truth value. | Mệnh đề có một giá trị đúng/sai xác định. |
| Q2 | **B** | Truth tables enumerate Boolean possibilities. | Bảng chân trị liệt kê các khả năng Boolean. |
| Q3 | **C** | Implication only fails with a true premise and false conclusion. | Kéo theo chỉ sai khi tiền đề đúng, kết luận sai. |
| Q4 | **D** | If stage one has m options and each has exactly n possible continuations, there are m×n complete outcomes. This counting principle requires stage-wise choices, not probabilistic independence. | Nếu bước đầu có m cách và mỗi cách có đúng n lựa chọn nối tiếp thì có m×n kết quả hoàn chỉnh. Quy tắc đếm theo từng bước này không đòi các biến cố độc lập về xác suất. |
| Q5 | **A** | AND requires both conditions. | AND cần cả hai điều kiện đúng. |
| Q6 | **B** | Inclusive OR accepts either or both true conditions. | OR bao hàm chấp nhận một hoặc cả hai điều kiện đúng. |
| Q7 | **C** | NOT negates its Boolean operand. | NOT phủ định giá trị Boolean. |
| Q8 | **D** | A true premise with a false conclusion violates implication. | Tiền đề đúng nhưng kết luận sai làm phép kéo theo sai. |
| Q9 | **A** | Two variables each have two states, giving 2² cases. | Hai biến có hai trạng thái mỗi biến, tạo 2² trường hợp. |
| Q10 | **B** | Three binary choices give 2³ combinations. | Ba lựa chọn nhị phân tạo 2³ tổ hợp. |
| Q11 | **C** | One Boolean has True and False. | Một biến Boolean có True và False. |
| Q12 | **D** | Four Boolean variables give 2⁴ possibilities. | Bốn biến Boolean tạo 2⁴ khả năng. |
| Q13 | **A** | The expression is false exactly for p=True, q=False. | Biểu thức chỉ sai khi p=True, q=False. |
| Q14 | **B** | A true premise with a false conclusion is the only false implication case. | Tiền đề đúng và kết luận sai là trường hợp duy nhất làm phép kéo theo sai. |
| Q15 | **C** | AND is false if any operand is false. | AND sai nếu có một vế sai. |
| Q16 | **D** | OR is true when one operand is true. | OR đúng khi có một vế đúng. |
| Q17 | **A** | Disjoint alternatives are added without double counting. | Các nhóm không trùng có thể cộng mà không đếm lặp. |
| Q18 | **B** | Multiplication requires consistent branching counts. | Nguyên lý nhân yêu cầu số nhánh lựa chọn phù hợp ở từng bước. |
| Q19 | **C** | product enumerates the Cartesian product. | product liệt kê tích Descartes. |
| Q20 | **D** | Overlapping groups must not be counted twice. | Nhóm có giao nhau không được đếm trùng. |

## 8. Nối sang bài tiếp

`Boolean → logic mệnh đề → tổ hợp → xác suất`.

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

### 4.1. Proposition

**Từ vựng trong mục:** **Proposition** — mệnh đề.

Mệnh đề là phát biểu có thể xác định đúng (`True`) hoặc sai (`False`). Ví dụ `3 > 1` là một mệnh đề đúng.

```python
print(3 > 1)
```

**Kết quả khi chạy:**

```text
True
```

### 4.2. Truth table

**Từ vựng trong mục:** **Truth table** — bảng chân trị.

Bảng chân trị liệt kê mọi khả năng của các biến Boolean. Với một biến `p`, có hai trường hợp: `True` hoặc `False`; phủ định `not p` đảo giá trị đó.

```python
for p in [True, False]:
        print(p, not p)
```

**Kết quả khi chạy:**

```text
True False
False True
```

### 4.3. Implication

**Từ vựng trong mục:** **Implication** — kéo theo.

Mệnh đề kéo theo `p ⇒ q` chỉ sai khi `p` đúng nhưng `q` sai. Trong Python ta viết `(not p) or q`. Đây là quy tắc logic, không khẳng định quan hệ nhân quả.

```python
p, q = True, False
print((not p) or q)
```

**Kết quả khi chạy:**

```text
False
```

### 4.4. Counting

**Từ vựng trong mục:** **Counting** — nguyên lý đếm.

Nguyên lý nhân: nếu chọn một trong 3 màu và một trong 4 cỡ độc lập thì có `3 * 4 = 12` kiểu kết hợp.

```python
print(3 * 4)
```

**Kết quả khi chạy:**

```text
12
```

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

## 6. Các lỗi dễ mắc

- `and` chỉ đúng khi cả hai điều kiện đúng, `or` đúng khi ít nhất một điều kiện đúng; `not` đảo Boolean.
- Với mệnh đề kéo theo `p ⇒ q`, trường hợp `p=False` không chứng minh rằng `q=True`.
- Nguyên lý nhân chỉ áp dụng trực tiếp khi mỗi lựa chọn ở bước trước đều có đủ lựa chọn tiếp theo.
- Tích Descartes liệt kê các cặp có thứ tự theo hai nguồn; đừng nhầm với phép hợp của Set.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is a proposition? — Mệnh đề là gì?**

A. A statement with a truth value — Phát biểu có giá trị đúng sai

B. A Python folder — Thư mục Python

C. An image format — Định dạng ảnh

D. A list length — Độ dài list

**Q2. What does not True evaluate to? — not True bằng gì?**

A. True — True

B. False — False

C. None — None

D. 1 — 1

**Q3. When is p and q true? — Khi nào p and q đúng?**

A. When p is false — Khi p sai

B. When at least one is true — Khi có ít nhất một đúng

C. When both are true — Khi cả hai đúng

D. Always — Luôn đúng

**Q4. When is p or q false? — Khi nào p or q sai?**

A. When both true — Khi cả hai đúng

B. When exactly one true — Khi chỉ một đúng

C. When p true — Khi p đúng

D. When both false — Khi cả hai sai

**Q5. How many cases are in a truth table for two Booleans? — Bảng chân trị hai biến Boolean có bao nhiêu trường hợp?**

A. 4 — 4

B. 2 — 2

C. 6 — 6

D. 8 — 8

**Q6. What is implication p ⇒ q equivalent to? — p kéo theo q tương đương biểu thức nào?**

A. p and q — p and q

B. (not p) or q — (not p) or q

C. p or (not q) — p or (not q)

D. not p and q — not p and q

**Q7. When is p ⇒ q false? — Khi nào p kéo theo q sai?**

A. p false and q true — p sai q đúng

B. Both false — Cả hai sai

C. p true and q false — p đúng q sai

D. Both true — Cả hai đúng

**Q8. What does itertools.product produce? — itertools.product tạo gì?**

A. A sum only — Chỉ một tổng

B. A dictionary key — Khóa Dictionary

C. A random option — Một lựa chọn ngẫu nhiên

D. All cross-product tuples — Tất cả bộ kết hợp giữa các nguồn

**Q9. Why is login access denied in the example? — Vì sao ví dụ đăng nhập bị từ chối?**

A. The account is not verified — Tài khoản chưa xác minh

B. The account is logged out — Tài khoản chưa đăng nhập

C. Both flags are true — Cả hai cờ đúng

D. There is no condition — Không có điều kiện

**Q10. What does True and False print? — True and False in gì?**

A. True — True

B. False — False

C. 0 — 0

D. None — None

**Q11. What does True or False print? — True or False in gì?**

A. False — False

B. None — None

C. True — True

D. Error — Lỗi

**Q12. What does implication print for p=True, q=False? — Phép kéo theo in gì khi p=True q=False?**

A. True — True

B. None — None

C. 1 — 1

D. False — False

**Q13. How many combinations arise from 3 colors and 4 sizes? — 3 màu và 4 cỡ có bao nhiêu kết hợp?**

A. 12 — 12

B. 7 — 7

C. 3 — 3

D. 4 — 4

**Q14. What must hold for simple multiplication counting? — Điều kiện dùng nguyên lý nhân trực tiếp là gì?**

A. Only one choice exists — Chỉ có một lựa chọn

B. Each option has the stated number of following choices — Mỗi lựa chọn có đủ số lựa chọn bước tiếp

C. No options can combine — Không có lựa chọn nào kết hợp

D. Every option is identical — Mọi lựa chọn giống nhau

**Q15. How many pairs result from 2 colors and 2 sizes? — 2 màu và 2 cỡ tạo mấy cặp?**

A. 2 — 2

B. 8 — 8

C. 4 — 4

D. 6 — 6

**Q16. What does the truth table enumerate? — Bảng chân trị liệt kê gì?**

A. Only true outcomes — Chỉ kết quả đúng

B. Only false outcomes — Chỉ kết quả sai

C. Random inputs — Đầu vào ngẫu nhiên

D. All logical input combinations — Mọi tổ hợp đầu vào logic

**Q17. Which expression negates a Boolean p? — Biểu thức phủ định p là gì?**

A. not p — not p

B. p and p — p and p

C. p or p — p or p

D. p == p — p == p

**Q18. What is False ⇒ False? — False kéo theo False có giá trị gì?**

A. False — False

B. True — True

C. None — None

D. Error — Lỗi

**Q19. How many outputs does the nested truth-table loop print? — Vòng lặp bảng chân trị in bao nhiêu dòng?**

A. 2 — 2

B. 3 — 3

C. 4 — 4

D. 8 — 8

**Q20. What is the difference between counting and product()? — Khác biệt giữa đếm và product() là gì?**

A. Both always return only a number — Cả hai luôn chỉ trả về số

B. product ignores pairings — product bỏ qua các cặp

C. Counting always prints strings — Đếm luôn in chuỗi

D. Counting gives quantity; product lists pairs — Đếm cho số lượng còn product liệt kê cặp

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **A** | A statement with a truth value | Phát biểu có giá trị đúng sai |
| Q2 | **B** | False | False |
| Q3 | **C** | When both are true | Khi cả hai đúng |
| Q4 | **D** | When both false | Khi cả hai sai |
| Q5 | **A** | 4 | 4 |
| Q6 | **B** | (not p) or q | (not p) or q |
| Q7 | **C** | p true and q false | p đúng q sai |
| Q8 | **D** | All cross-product tuples | Tất cả bộ kết hợp giữa các nguồn |
| Q9 | **A** | The account is not verified | Tài khoản chưa xác minh |
| Q10 | **B** | False | False |
| Q11 | **C** | True | True |
| Q12 | **D** | False | False |
| Q13 | **A** | 12 | 12 |
| Q14 | **B** | Each option has the stated number of following choices | Mỗi lựa chọn có đủ số lựa chọn bước tiếp |
| Q15 | **C** | 4 | 4 |
| Q16 | **D** | All logical input combinations | Mọi tổ hợp đầu vào logic |
| Q17 | **A** | not p | not p |
| Q18 | **B** | True | True |
| Q19 | **C** | 4 | 4 |
| Q20 | **D** | Counting gives quantity; product lists pairs | Đếm cho số lượng còn product liệt kê cặp |

## 8. Nối sang bài tiếp

`Boolean → logic mệnh đề → tổ hợp → xác suất`.

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


**Q1. What best describes Proposition? — Mô tả nào đúng với Proposition?**

A. A different idea is Liệt kê kết quả ứng với mọi tổ hợp logic — Liệt kê kết quả ứng với mọi tổ hợp logic

B. It is Câu có giá trị True hoặc False — Câu có giá trị True hoặc False

C. A different idea is Quan hệ P⇒Q tương đương (not P) or Q — Quan hệ P⇒Q tương đương (not P) or Q

D. A different idea is Đếm số khả năng khi ghép lựa chọn — Đếm số khả năng khi ghép lựa chọn


**Q2. What best describes Truth table? — Mô tả nào đúng với Truth table?**

A. It is Liệt kê kết quả ứng với mọi tổ hợp logic — Liệt kê kết quả ứng với mọi tổ hợp logic

B. A different idea is Quan hệ P⇒Q tương đương (not P) or Q — Quan hệ P⇒Q tương đương (not P) or Q

C. A different idea is Đếm số khả năng khi ghép lựa chọn — Đếm số khả năng khi ghép lựa chọn

D. A different idea is Câu có giá trị True hoặc False — Câu có giá trị True hoặc False


**Q3. What best describes Implication? — Mô tả nào đúng với Implication?**

A. A different idea is Đếm số khả năng khi ghép lựa chọn — Đếm số khả năng khi ghép lựa chọn

B. A different idea is Câu có giá trị True hoặc False — Câu có giá trị True hoặc False

C. A different idea is Liệt kê kết quả ứng với mọi tổ hợp logic — Liệt kê kết quả ứng với mọi tổ hợp logic

D. It is Quan hệ P⇒Q tương đương (not P) or Q — Quan hệ P⇒Q tương đương (not P) or Q


**Q4. What best describes Counting? — Mô tả nào đúng với Counting?**

A. A different idea is Câu có giá trị True hoặc False — Câu có giá trị True hoặc False

B. A different idea is Liệt kê kết quả ứng với mọi tổ hợp logic — Liệt kê kết quả ứng với mọi tổ hợp logic

C. It is Đếm số khả năng khi ghép lựa chọn — Đếm số khả năng khi ghép lựa chọn

D. A different idea is Quan hệ P⇒Q tương đương (not P) or Q — Quan hệ P⇒Q tương đương (not P) or Q


**Q5. Which operation matches and/or/not? — Mục đích của and/or/not là gì?**

A. Another operation is used to Biểu diễn phép kéo theo P⇒Q — Biểu diễn phép kéo theo P⇒Q

B. It is used to Ghép điều kiện, chọn ít nhất một hoặc phủ định — Ghép điều kiện, chọn ít nhất một hoặc phủ định

C. Another operation is used to Tạo tích Descartes của hai tập tùy chọn — Tạo tích Descartes của hai tập tùy chọn

D. Another operation is used to Nhân số lựa chọn từng bước độc lập — Nhân số lựa chọn từng bước độc lập


**Q6. Which operation matches (not p) or q? — Mục đích của (not p) or q là gì?**

A. It is used to Biểu diễn phép kéo theo P⇒Q — Biểu diễn phép kéo theo P⇒Q

B. Another operation is used to Tạo tích Descartes của hai tập tùy chọn — Tạo tích Descartes của hai tập tùy chọn

C. Another operation is used to Nhân số lựa chọn từng bước độc lập — Nhân số lựa chọn từng bước độc lập

D. Another operation is used to Ghép điều kiện, chọn ít nhất một hoặc phủ định — Ghép điều kiện, chọn ít nhất một hoặc phủ định


**Q7. Which operation matches itertools.product(A,B)? — Mục đích của itertools.product(A,B) là gì?**

A. Another operation is used to Nhân số lựa chọn từng bước độc lập — Nhân số lựa chọn từng bước độc lập

B. Another operation is used to Ghép điều kiện, chọn ít nhất một hoặc phủ định — Ghép điều kiện, chọn ít nhất một hoặc phủ định

C. Another operation is used to Biểu diễn phép kéo theo P⇒Q — Biểu diễn phép kéo theo P⇒Q

D. It is used to Tạo tích Descartes của hai tập tùy chọn — Tạo tích Descartes của hai tập tùy chọn


**Q8. Which operation matches math.prod(counts)? — Mục đích của math.prod(counts) là gì?**

A. Another operation is used to Ghép điều kiện, chọn ít nhất một hoặc phủ định — Ghép điều kiện, chọn ít nhất một hoặc phủ định

B. Another operation is used to Biểu diễn phép kéo theo P⇒Q — Biểu diễn phép kéo theo P⇒Q

C. It is used to Nhân số lựa chọn từng bước độc lập — Nhân số lựa chọn từng bước độc lập

D. Another operation is used to Tạo tích Descartes của hai tập tùy chọn — Tạo tích Descartes của hai tập tùy chọn


**Q9. Why was the method chosen for scenario 1? — Vì sao chọn cách giải của tình huống 1?**

A. Another reason is Quét bốn tổ hợp của hai mệnh đề — Quét bốn tổ hợp của hai mệnh đề

B. Because Dùng and để đòi cả đăng nhập và xác minh — Dùng and để đòi cả đăng nhập và xác minh

C. Another reason is Phép kéo theo chỉ sai khi P đúng nhưng Q sai — Phép kéo theo chỉ sai khi P đúng nhưng Q sai

D. Another reason is Nguyên lý nhân đếm số tổ hợp — Nguyên lý nhân đếm số tổ hợp


**Q10. Why was the method chosen for scenario 2? — Vì sao chọn cách giải của tình huống 2?**

A. Because Quét bốn tổ hợp của hai mệnh đề — Quét bốn tổ hợp của hai mệnh đề

B. Another reason is Phép kéo theo chỉ sai khi P đúng nhưng Q sai — Phép kéo theo chỉ sai khi P đúng nhưng Q sai

C. Another reason is Nguyên lý nhân đếm số tổ hợp — Nguyên lý nhân đếm số tổ hợp

D. Another reason is product liệt kê từng cặp màu và size — product liệt kê từng cặp màu và size


**Q11. Why was the method chosen for scenario 3? — Vì sao chọn cách giải của tình huống 3?**

A. Another reason is Nguyên lý nhân đếm số tổ hợp — Nguyên lý nhân đếm số tổ hợp

B. Another reason is product liệt kê từng cặp màu và size — product liệt kê từng cặp màu và size

C. Another reason is Dùng and để đòi cả đăng nhập và xác minh — Dùng and để đòi cả đăng nhập và xác minh

D. Because Phép kéo theo chỉ sai khi P đúng nhưng Q sai — Phép kéo theo chỉ sai khi P đúng nhưng Q sai


**Q12. Why was the method chosen for scenario 4? — Vì sao chọn cách giải của tình huống 4?**

A. Another reason is product liệt kê từng cặp màu và size — product liệt kê từng cặp màu và size

B. Another reason is Dùng and để đòi cả đăng nhập và xác minh — Dùng and để đòi cả đăng nhập và xác minh

C. Because Nguyên lý nhân đếm số tổ hợp — Nguyên lý nhân đếm số tổ hợp

D. Another reason is Quét bốn tổ hợp của hai mệnh đề — Quét bốn tổ hợp của hai mệnh đề


**Q13. Why was the method chosen for scenario 5? — Vì sao chọn cách giải của tình huống 5?**

A. Another reason is Dùng and để đòi cả đăng nhập và xác minh — Dùng and để đòi cả đăng nhập và xác minh

B. Because product liệt kê từng cặp màu và size — product liệt kê từng cặp màu và size

C. Another reason is Quét bốn tổ hợp của hai mệnh đề — Quét bốn tổ hợp của hai mệnh đề

D. Another reason is Phép kéo theo chỉ sai khi P đúng nhưng Q sai — Phép kéo theo chỉ sai khi P đúng nhưng Q sai


**Q14. What input is used in scenario 1? — Tình huống 1 dùng dữ liệu gì?**

A. The data are Hai cờ Boolean — Hai cờ Boolean

B. Other data are P và Q nhận True/False — P và Q nhận True/False

C. Other data are P đúng, Q sai — P đúng, Q sai

D. Other data are 3 màu và 4 cỡ áo — 3 màu và 4 cỡ áo


**Q15. What input is used in scenario 2? — Tình huống 2 dùng dữ liệu gì?**

A. Other data are P đúng, Q sai — P đúng, Q sai

B. Other data are 3 màu và 4 cỡ áo — 3 màu và 4 cỡ áo

C. Other data are 2 màu và 2 size — 2 màu và 2 size

D. The data are P và Q nhận True/False — P và Q nhận True/False


**Q16. What input is used in scenario 3? — Tình huống 3 dùng dữ liệu gì?**

A. Other data are 3 màu và 4 cỡ áo — 3 màu và 4 cỡ áo

B. Other data are 2 màu và 2 size — 2 màu và 2 size

C. The data are P đúng, Q sai — P đúng, Q sai

D. Other data are Hai cờ Boolean — Hai cờ Boolean


**Q17. What input is used in scenario 4? — Tình huống 4 dùng dữ liệu gì?**

A. Other data are 2 màu và 2 size — 2 màu và 2 size

B. The data are 3 màu và 4 cỡ áo — 3 màu và 4 cỡ áo

C. Other data are Hai cờ Boolean — Hai cờ Boolean

D. Other data are P và Q nhận True/False — P và Q nhận True/False


**Q18. What input is used in scenario 5? — Tình huống 5 dùng dữ liệu gì?**

A. The data are 2 màu và 2 size — 2 màu và 2 size

B. Other data are Hai cờ Boolean — Hai cờ Boolean

C. Other data are P và Q nhận True/False — P và Q nhận True/False

D. Other data are P đúng, Q sai — P đúng, Q sai


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
| Q1 | **B** | It is Câu có giá trị True hoặc False | Câu có giá trị True hoặc False |
| Q2 | **A** | It is Liệt kê kết quả ứng với mọi tổ hợp logic | Liệt kê kết quả ứng với mọi tổ hợp logic |
| Q3 | **D** | It is Quan hệ P⇒Q tương đương (not P) or Q | Quan hệ P⇒Q tương đương (not P) or Q |
| Q4 | **C** | It is Đếm số khả năng khi ghép lựa chọn | Đếm số khả năng khi ghép lựa chọn |
| Q5 | **B** | It is used to Ghép điều kiện, chọn ít nhất một hoặc phủ định | Ghép điều kiện, chọn ít nhất một hoặc phủ định |
| Q6 | **A** | It is used to Biểu diễn phép kéo theo P⇒Q | Biểu diễn phép kéo theo P⇒Q |
| Q7 | **D** | It is used to Tạo tích Descartes của hai tập tùy chọn | Tạo tích Descartes của hai tập tùy chọn |
| Q8 | **C** | It is used to Nhân số lựa chọn từng bước độc lập | Nhân số lựa chọn từng bước độc lập |
| Q9 | **B** | Because Dùng and để đòi cả đăng nhập và xác minh | Dùng and để đòi cả đăng nhập và xác minh |
| Q10 | **A** | Because Quét bốn tổ hợp của hai mệnh đề | Quét bốn tổ hợp của hai mệnh đề |
| Q11 | **D** | Because Phép kéo theo chỉ sai khi P đúng nhưng Q sai | Phép kéo theo chỉ sai khi P đúng nhưng Q sai |
| Q12 | **C** | Because Nguyên lý nhân đếm số tổ hợp | Nguyên lý nhân đếm số tổ hợp |
| Q13 | **B** | Because product liệt kê từng cặp màu và size | product liệt kê từng cặp màu và size |
| Q14 | **A** | The data are Hai cờ Boolean | Hai cờ Boolean |
| Q15 | **D** | The data are P và Q nhận True/False | P và Q nhận True/False |
| Q16 | **C** | The data are P đúng, Q sai | P đúng, Q sai |
| Q17 | **B** | The data are 3 màu và 4 cỡ áo | 3 màu và 4 cỡ áo |
| Q18 | **A** | The data are 2 màu và 2 size | 2 màu và 2 size |
| Q19 | **D** | Meaning of rows, columns and units | Ý nghĩa hàng, cột và đơn vị |
| Q20 | **C** | Check the result and limitations | Kiểm tra kết quả và giới hạn |

## 8. Nối sang bài tiếp

`Boolean → logic mệnh đề → tổ hợp → xác suất`.

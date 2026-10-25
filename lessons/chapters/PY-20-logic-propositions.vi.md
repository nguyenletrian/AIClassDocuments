# PY-20 — Logic mệnh đề, bảng chân trị và quy tắc đếm


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Proposition** — mệnh đề; **Truth table** — bảng chân trị.

`Boolean → logic mệnh đề → tổ hợp → xác suất`

**Học xong dùng để làm gì?** Lập bảng đúng/sai của quy tắc và đếm tổ hợp lựa chọn, ví dụ điều kiện xét duyệt.

**Kết nối kiến thức tiếp theo:** PY-21 dùng tập hợp và bao hàm–loại trừ để xử lý nhóm bị chồng lấn.

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
# Mục đích: Phát biểu đúng hoặc sai.
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
# Mục đích: Bảng chân trị.
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
# Mục đích: Nếu p thì q.
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
# Mục đích: Nguyên lý cộng và nhân.
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

### Tình huống 1 — Điều kiện đăng nhập · Cấp 1: Phép đơn

**Từ vựng trong mục:** **Proposition** — mệnh đề; **AND** — và.

**Tình huống thực tế:** Một cổng học tập chỉ cho mở nội dung khi người dùng đã đăng nhập và xác minh tài khoản. Trong lần kiểm tra này `logged_in=True`, `verified=False`. In kết quả người dùng có được quyền truy cập hay không.

**Vì sao chọn cách giải này?** Toán tử `and` chỉ cho `True` khi cả hai điều kiện đều đúng.

**Quy trình giải:** Đặt hai trạng thái Boolean → nối chúng bằng `and` → in kết quả.

```python
# Mục đích: Điều kiện đăng nhập.
logged_in, verified = True, False
print(logged_in and verified)
```

**Kết quả khi chạy:**

```text
False
```

**Giải thích kết quả:** `False` — tài khoản đã đăng nhập nhưng chưa xác minh.

**Bài thực hành nâng cấp — cấp 1/5:** Hệ thống có **10 hồ sơ học viên/đăng nhập** với mã riêng, trạng thái và nhóm. Hãy đánh giá một yêu cầu đăng nhập bằng AND. Các bài tiến từ phép đơn lẻ đến phối hợp nhiều điều kiện; cấp 4–5 phân biệt thông tin chưa có với điều kiện sai.

```python
values = [42, 70, 58, 91, 35, 76, 88, 64, 54, 96]
rows = [{"id":f"U{k:02d}","approved":(x is not None and x>=60),"verified":None if x is None else k%3!=0} for k,x in enumerate(values,1)]
result = rows[0]['approved'] and rows[0]['verified']
print("Số hồ sơ:",len(rows))
print("Kết quả:",result)
```

**Đọc kết quả:** Đối chiếu đủ 10 hồ sơ, tập hợp không chứa phần tử trùng, trạng thái chưa biết phải có nhánh xử lý riêng.

### Tình huống 2 — Bảng chân trị · Cấp 2: Tập dữ liệu

**Từ vựng trong mục:** **Truth table** — bảng chân trị; **OR** — hoặc.

**Tình huống thực tế:** Nhân viên kiểm thử muốn lập bảng chân trị cho `p and q` và `p or q`, trong đó `p`, `q` đều có thể là `True` hoặc `False`. In tất cả bốn tổ hợp của p và q cùng kết quả của hai phép logic.

**Vì sao chọn cách giải này?** Hai vòng `for` lồng nhau tạo đủ 2 × 2 tổ hợp.

**Quy trình giải:** Duyệt p theo hai trạng thái → với mỗi p duyệt q → in p, q, p and q, p or q.

```python
# Mục đích: Bảng chân trị.
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

**Bài thực hành nâng cấp — cấp 2/5:** Hệ thống có **12 hồ sơ học viên/đăng nhập** với mã riêng, trạng thái và nhóm. Hãy lập bảng hai điều kiện trên 12 hồ sơ. Các bài tiến từ phép đơn lẻ đến phối hợp nhiều điều kiện; cấp 4–5 phân biệt thông tin chưa có với điều kiện sai.

```python
values = [42, 70, 58, 91, 35, 76, 88, 64, 54, 96, 47, 82]
rows = [{"id":f"U{k:02d}","approved":(x is not None and x>=60),"verified":None if x is None else k%3!=0} for k,x in enumerate(values,1)]
result = sum(r['approved'] and r['verified'] for r in rows)
print("Số hồ sơ:",len(rows))
print("Kết quả:",result)
```

**Đọc kết quả:** Đối chiếu đủ 12 hồ sơ, tập hợp không chứa phần tử trùng, trạng thái chưa biết phải có nhánh xử lý riêng.

### Tình huống 3 — Kiểm quy tắc kéo theo · Cấp 3: Kết hợp điều kiện

**Từ vựng trong mục:** **Implication** — kéo theo; **Premise** — tiền đề.

**Tình huống thực tế:** Một quy định nội bộ phát biểu: “Nếu đã được phê duyệt (p) thì phải có chứng nhận (q)”. Có trường hợp `p=True` nhưng `q=False`. Kiểm tra quy tắc kéo theo có được đáp ứng không.

**Vì sao chọn cách giải này?** `(not p) or q` tương đương phép kéo theo và nhận `False` khi tiền đề đúng nhưng kết luận sai.

**Quy trình giải:** Gán p=True, q=False → tính `(not p) or q` → in kết quả.

```python
# Mục đích: Kiểm quy tắc kéo theo.
p, q = True, False
print((not p) or q)
```

**Kết quả khi chạy:**

```text
False
```

**Giải thích kết quả:** `False` — trường hợp này vi phạm quy tắc.

**Bài thực hành nâng cấp — cấp 3/5:** Hệ thống có **15 hồ sơ học viên/đăng nhập** với mã riêng, trạng thái và nhóm. Hãy đếm hồ sơ vi phạm quy tắc kéo theo p ⇒ q. Các bài tiến từ phép đơn lẻ đến phối hợp nhiều điều kiện; cấp 4–5 phân biệt thông tin chưa có với điều kiện sai.

```python
values = [42, 70, 58, 91, 35, 76, 88, 64, 54, 96, 47, 82, 69, 73, 61]
rows = [{"id":f"U{k:02d}","approved":(x is not None and x>=60),"verified":None if x is None else k%3!=0} for k,x in enumerate(values,1)]
result = [r['id'] for r in rows if r['approved'] and not r['verified']]
print("Số hồ sơ:",len(rows))
print("Kết quả:",result)
```

**Đọc kết quả:** Đối chiếu đủ 15 hồ sơ, tập hợp không chứa phần tử trùng, trạng thái chưa biết phải có nhánh xử lý riêng.

### Tình huống 4 — Cấu hình áo · Cấp 4: Trường hợp chưa xác định

**Từ vựng trong mục:** **Counting** — nguyên lý đếm; **Combination** — cách kết hợp.

**Tình huống thực tế:** Cửa hàng cho khách chọn 1 trong 3 màu áo và 1 trong 4 cỡ; mọi màu đều có đủ bốn cỡ. Tính số cách chọn một màu và một cỡ.

**Vì sao chọn cách giải này?** Nguyên lý nhân phù hợp khi mỗi lựa chọn màu kết hợp được với mọi lựa chọn cỡ.

**Quy trình giải:** Lấy số màu nhân số cỡ: 3 × 4 → in tổng số kết hợp.

```python
# Mục đích: Cấu hình áo.
print(3 * 4)
```

**Kết quả khi chạy:**

```text
12
```

**Giải thích kết quả:** `12` cách chọn.

**Bài thực hành nâng cấp — cấp 4/5:** Hệ thống có **18 hồ sơ học viên/đăng nhập** với mã riêng, trạng thái và nhóm. Hãy tách hồ sơ chưa xác minh khỏi trường hợp False. Các bài tiến từ phép đơn lẻ đến phối hợp nhiều điều kiện; cấp 4–5 phân biệt thông tin chưa có với điều kiện sai.

```python
values = [42, 70, 58, 91, 35, 76, 88, 64, 54, 96, 47, 82, 69, 73, 61, None, 90, 39]
rows = [{"id":f"U{k:02d}","approved":(x is not None and x>=60),"verified":None if x is None else k%3!=0} for k,x in enumerate(values,1)]
result = [r['id'] for r in rows if r['verified'] is None]
print("Số hồ sơ:",len(rows))
print("Kết quả:",result)
```

**Đọc kết quả:** Đối chiếu đủ 18 hồ sơ, tập hợp không chứa phần tử trùng, trạng thái chưa biết phải có nhánh xử lý riêng.

### Tình huống 5 — Ghép các tùy chọn · Cấp 5: Tổng hợp có phân loại

**Từ vựng trong mục:** **Cartesian product** — tích Descartes; **Option** — lựa chọn.

**Tình huống thực tế:** Cửa hàng bán áo có hai màu `red`, `blue` và hai cỡ `S`, `M`, mọi màu đều có đủ hai cỡ. In danh sách cụ thể tất cả cặp (màu, cỡ).

**Vì sao chọn cách giải này?** `itertools.product` liệt kê tích Descartes, khác với chỉ đếm bằng phép nhân.

**Quy trình giải:** Tạo list hai màu và hai cỡ → dùng `product` → chuyển sang list và in.

```python
# Mục đích: Ghép các tùy chọn.
from itertools import product
print(list(product(["red", "blue"], ["S", "M"])))
```

**Kết quả khi chạy:**

```text
[('red', 'S'), ('red', 'M'), ('blue', 'S'), ('blue', 'M')]
```

**Giải thích kết quả:** Bốn cặp: `(red,S)`, `(red,M)`, `(blue,S)`, `(blue,M)`.

**Bài thực hành nâng cấp — cấp 5/5:** Hệ thống có **20 hồ sơ học viên/đăng nhập** với mã riêng, trạng thái và nhóm. Hãy báo số hồ sơ được truy cập, bị từ chối và thiếu thông tin. Các bài tiến từ phép đơn lẻ đến phối hợp nhiều điều kiện; cấp 4–5 phân biệt thông tin chưa có với điều kiện sai.

```python
values = [42, 70, 58, 91, 35, 76, 88, 64, 54, 96, 47, 82, 69, 73, 61, None, 90, 39, 85, None]
rows = [{"id":f"U{k:02d}","approved":(x is not None and x>=60),"verified":None if x is None else k%3!=0} for k,x in enumerate(values,1)]
result = {'allowed':sum(r['approved'] and r['verified'] is True for r in rows),'denied':sum(r['verified'] is False or not r['approved'] for r in rows),'unknown':[r['id'] for r in rows if r['verified'] is None]}
print("Số hồ sơ:",len(rows))
print("Kết quả:",result)
```

**Đọc kết quả:** Đối chiếu đủ 20 hồ sơ, tập hợp không chứa phần tử trùng, trạng thái chưa biết phải có nhánh xử lý riêng.

## 6. Sai lầm thường gặp

- Không nhầm `and` (cả hai đúng) với `or` (ít nhất một đúng); `not` đảo giá trị Boolean.
- Phép kéo theo `p ⇒ q` chỉ sai khi `p=True`, `q=False`; tiền đề sai không tự chứng minh kết luận đúng.
- Bảng chân trị hai biến có bốn tổ hợp; nếu thiếu một tổ hợp, kiểm tra logic có thể bỏ sót lỗi.
- Nguyên lý **nhân** đếm lựa chọn theo nhiều bước kết hợp được với nhau; nguyên lý **cộng** đếm các phương án thay thế không trùng. Nếu trùng phải điều chỉnh số đếm.
- Set không bảo đảm thứ tự in, còn kết quả `itertools.product` gồm các tuple theo thứ tự nguồn đã đưa vào.

## 7. Trắc nghiệm

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is a proposition? | Mệnh đề là gì?**

A. A table of all input truth-value combinations | Bảng các tổ hợp giá trị đúng/sai đầu vào

B. The logical conditional 'if p then q' | Điều kiện logic 'nếu p thì q'

C. A statement that is either true or false | Phát biểu có thể xác định đúng hoặc sai

D. Multiply choice counts across sequential stages when each earlier choice permits the stated number of later choices | Nhân số cách chọn qua các bước khi mỗi lựa chọn trước cho phép đúng số cách ở bước sau

**Đáp án: C**

**Giải thích:** Mệnh đề có một giá trị đúng/sai xác định. Ví dụ `2 + 2 = 4` là mệnh đề đúng, còn câu hỏi như `Mấy giờ rồi?` không tự khẳng định một giá trị đúng hay sai.


**Q2. What is a truth table? | Bảng chân trị là gì?**

A. Multiply the numbers of sequential independent choices | Nhân số lựa chọn qua các bước kết hợp đầy đủ

B. A statement that is either true or false | Phát biểu có thể xác định đúng hoặc sai

C. A table of all input truth-value combinations | Bảng các tổ hợp giá trị đúng/sai đầu vào

D. The logical conditional 'if p then q' | Điều kiện logic 'nếu p thì q'

**Đáp án: C**

**Giải thích:** Bảng chân trị liệt kê các khả năng Boolean. Với hai mệnh đề p và q, bốn hàng là (T,T), (T,F), (F,T), (F,F); bảng xét mọi cách gán giá trị.


**Q3. What is logical implication `p ⇒ q`? | Phép kéo theo `p ⇒ q` là gì?**

A. The logical conditional 'if p then q' | Điều kiện logic 'nếu p thì q'

B. A statement that is either true or false | Phát biểu có thể xác định đúng hoặc sai

C. Multiply the numbers of sequential independent choices | Nhân số lựa chọn qua các bước kết hợp đầy đủ

D. A table of all input truth-value combinations | Bảng các tổ hợp giá trị đúng/sai đầu vào

**Đáp án: A**

**Giải thích:** Kéo theo chỉ sai khi tiền đề đúng, kết luận sai. Phép kéo theo đòi khi tiền đề p đúng thì kết luận q không được sai; khi p sai, kéo theo vật chất vẫn đúng bất kể q.


**Q4. What is the multiplication counting principle? | Nguyên lý nhân trong đếm là gì?**

A. A statement that is either true or false | Phát biểu có thể xác định đúng hoặc sai

B. A table of all input truth-value combinations | Bảng các tổ hợp giá trị đúng/sai đầu vào

C. The logical conditional 'if p then q' | Điều kiện logic 'nếu p thì q'

D. Multiply stage-choice counts when each earlier choice permits the same stated number of valid continuations | Nhân số cách chọn mỗi bước khi mọi lựa chọn trước đều cho phép cùng số cách đi tiếp hợp lệ

**Đáp án: D**

**Giải thích:** Nếu bước đầu có m cách và mỗi cách có đúng n lựa chọn nối tiếp thì có m×n kết quả hoàn chỉnh. Quy tắc đếm theo từng bước này không đòi các biến cố độc lập về xác suất. Nếu có hai cách chọn áo và mỗi áo đều ghép được với ba quần, tổng cộng `2 × 3 = 6` bộ; không cần giả thiết độc lập xác suất.


**Q5. When is `p and q` true? | Khi nào `p and q` đúng?**

A. Reverses the truth value of p | Đảo giá trị đúng/sai của p

B. When p is true and q is false | Khi p đúng và q sai

C. When at least one of p or q is true | Khi có ít nhất một trong p hoặc q đúng

D. When both p and q are true | Khi p và q đều đúng

**Đáp án: D**

**Giải thích:** AND cần cả hai điều kiện đúng. Nếu p đúng nhưng q sai thì `p and q` sai; một điều kiện đúng chưa đủ cho phép AND.


**Q6. When is `p or q` true? | Khi nào `p or q` đúng?**

A. Reverses the truth value of p | Đảo giá trị đúng/sai của p

B. When p is true and q is false | Khi p đúng và q sai

C. When at least one of p or q is true | Khi có ít nhất một trong p hoặc q đúng

D. When both p and q are true | Khi p và q đều đúng

**Đáp án: C**

**Giải thích:** OR bao hàm chấp nhận một hoặc cả hai điều kiện đúng. Đây là OR bao hàm: p và q có thể cùng đúng, khác XOR chỉ đúng khi đúng một vế.


**Q7. What does `not p` do? | `not p` làm gì?**

A. When p is true and q is false | Khi p đúng và q sai

B. Reverses the truth value of p | Đảo giá trị đúng/sai của p

C. When both p and q are true | Khi p và q đều đúng

D. When at least one of p or q is true | Khi có ít nhất một trong p hoặc q đúng

**Đáp án: B**

**Giải thích:** NOT phủ định giá trị Boolean. Nếu p=True thì `not p=False`; nếu p=False thì phủ định trở thành True.


**Q8. When is `p ⇒ q` false? | Khi nào `p ⇒ q` sai?**

A. When both p and q are true | Khi p và q đều đúng

B. When at least one of p or q is true | Khi có ít nhất một trong p hoặc q đúng

C. When p is true and q is false | Khi p đúng và q sai

D. Reverses the truth value of p | Đảo giá trị đúng/sai của p

**Đáp án: C**

**Giải thích:** Tiền đề đúng nhưng kết luận sai làm phép kéo theo sai. Với p=True và q=False, `(not p) or q` thành `(False or False)`, nên phép kéo theo sai.


**Q9. How many rows does a truth table with two variables have? | Bảng chân trị hai biến có mấy hàng?**

A. 8 | 8

B. 16 | 16

C. 2 | 2

D. 4 | 4

**Đáp án: D**

**Giải thích:** Hai biến có hai trạng thái mỗi biến, tạo 2² trường hợp. Mỗi biến Boolean có hai giá trị, tạo `2 × 2 = 4` tổ hợp chứ không chỉ hai tổ hợp.


**Q10. How many rows does a truth table with three variables have? | Bảng chân trị ba biến có mấy hàng?**

A. 2 | 2

B. 4 | 4

C. 16 | 16

D. 8 | 8

**Đáp án: D**

**Giải thích:** Ba lựa chọn nhị phân tạo 2³ tổ hợp. Ba biến Boolean tạo `2 × 2 × 2 = 8` cách gán đầu vào cho bảng chân trị.


**Q11. How many rows does a truth table with one variable have? | Bảng chân trị một biến có mấy hàng?**

A. 4 | 4

B. 8 | 8

C. 2 | 2

D. 16 | 16

**Đáp án: C**

**Giải thích:** Một biến Boolean có True và False. Hai hàng ứng với biến duy nhất nhận True và False; bảng có `2^1 = 2` hàng.


**Q12. How many rows does a truth table with four variables have? | Bảng chân trị bốn biến có mấy hàng?**

A. 16 | 16

B. 4 | 4

C. 2 | 2

D. 8 | 8

**Đáp án: A**

**Giải thích:** Bốn biến Boolean tạo 2⁴ khả năng. Mỗi biến Boolean thêm vào nhân đôi số hàng, nên bốn biến cần `2^4 = 16` tổ hợp.


**Q13. Which expression is equivalent to implication `p ⇒ q`? | Biểu thức nào tương đương `p ⇒ q`?**

A. `False` | `False`

B. `(not p) or q` | `(not p) or q`

C. `(True, False)` | `(True, False)`

D. `True` | `True`

**Đáp án: B**

**Giải thích:** Biểu thức chỉ sai khi p=True, q=False. Cả `p ⇒ q` và `(not p) or q` chỉ sai khi p=True, q=False nên bảng chân trị của chúng trùng nhau.


**Q14. Which input pair makes `p ⇒ q` false? | Cặp p, q nào làm `p ⇒ q` sai?**

A. `(True, False)` | `(True, False)`

B. `(not p) or q` | `(not p) or q`

C. `True` | `True`

D. `False` | `False`

**Đáp án: A**

**Giải thích:** Tiền đề đúng và kết luận sai là trường hợp duy nhất làm phép kéo theo sai. Thứ tự cặp là `(p, q)`, nên `(True, False)` có tiền đề đúng và kết luận sai như yêu cầu.


**Q15. What is `True and False`? | `True and False` bằng gì?**

A. `True` | `True`

B. `False` | `False`

C. `(not p) or q` | `(not p) or q`

D. `(True, False)` | `(True, False)`

**Đáp án: B**

**Giải thích:** AND sai nếu có một vế sai. Kết quả là Boolean `False`, không phải số nguyên 0; vế thứ hai sai trong khi AND cần cả hai đúng.


**Q16. What is `False or True`? | `False or True` bằng gì?**

A. `True` | `True`

B. `(True, False)` | `(True, False)`

C. `False` | `False`

D. `(not p) or q` | `(not p) or q`

**Đáp án: A**

**Giải thích:** OR đúng khi có một vế đúng. Vì có một vế đúng, OR bao hàm trả Boolean `True`; `False and True` thì lại sai.


**Q17. When does the addition counting principle apply directly? | Khi nào có thể áp dụng trực tiếp nguyên lý cộng?**

A. All ordered pairs taking one element from each input | Mọi cặp có thứ tự gồm một phần tử từ mỗi nguồn

B. When alternatives are disjoint | Khi các phương án thay thế không trùng nhau

C. When some outcomes belong to more than one counted group | Khi một kết quả nằm trong nhiều nhóm được đếm

D. When each step has the stated choices for every earlier selection | Khi mỗi bước có đủ số lựa chọn với mọi lựa chọn trước đó

**Đáp án: B**

**Giải thích:** Các nhóm không trùng có thể cộng mà không đếm lặp. Nếu năm kết quả chỉ thuộc nhóm A và ba kết quả chỉ thuộc nhóm B, tổng có `5 + 3 = 8` phương án không đếm trùng.


**Q18. When can choices be counted by multiplying options? | Khi nào có thể đếm bằng phép nhân?**

A. When each step has the stated choices for every earlier selection | Khi mỗi bước có đủ số lựa chọn với mọi lựa chọn trước đó

B. When alternatives are disjoint | Khi các phương án thay thế không trùng nhau

C. All ordered pairs taking one element from each input | Mọi cặp có thứ tự gồm một phần tử từ mỗi nguồn

D. When some outcomes belong to more than one counted group | Khi một kết quả nằm trong nhiều nhóm được đếm

**Đáp án: A**

**Giải thích:** Nguyên lý nhân yêu cầu số nhánh lựa chọn phù hợp ở từng bước. Nếu mỗi lựa chọn bước đầu đều có đúng ba cách đi tiếp thì nhân số cách mỗi bước; khi số nhánh thay đổi phải cộng số cách theo từng nhánh cẩn thận.


**Q19. What does `itertools.product(A, B)` generate? | `itertools.product(A, B)` tạo gì?**

A. When each step has the stated choices for every earlier selection | Khi mỗi bước có đủ số lựa chọn với mọi lựa chọn trước đó

B. All ordered pairs taking one element from each input | Mọi cặp có thứ tự gồm một phần tử từ mỗi nguồn

C. When alternatives are disjoint | Khi các phương án thay thế không trùng nhau

D. When some outcomes belong to more than one counted group | Khi một kết quả nằm trong nhiều nhóm được đếm

**Đáp án: B**

**Giải thích:** product liệt kê tích Descartes. Với `A=[1,2]` và `B=['x','y']`, product tạo `(1,'x')`, `(1,'y')`, `(2,'x')`, `(2,'y')`, không chỉ ghép vị trí tương ứng.


**Q20. When should overlapping alternatives be adjusted during counting? | Khi nào cần điều chỉnh phần giao khi đếm?**

A. All ordered pairs taking one element from each input | Mọi cặp có thứ tự gồm một phần tử từ mỗi nguồn

B. When each step has the stated choices for every earlier selection | Khi mỗi bước có đủ số lựa chọn với mọi lựa chọn trước đó

C. When alternatives are disjoint | Khi các phương án thay thế không trùng nhau

D. When some outcomes belong to more than one counted group | Khi một kết quả nằm trong nhiều nhóm được đếm

**Đáp án: D**

**Giải thích:** Nhóm có giao nhau không được đếm trùng. Với hai nhóm có giao, công thức `&#124;A ∪ B&#124; = &#124;A&#124; + &#124;B&#124; − &#124;A ∩ B&#124;` trừ phần được tính hai lần.

## 8. Nối sang bài tiếp

`Boolean → logic mệnh đề → tổ hợp → xác suất`.

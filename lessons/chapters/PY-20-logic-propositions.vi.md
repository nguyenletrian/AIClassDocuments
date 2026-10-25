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

## 5. Năm tình huống logic — từ hai mệnh đề đến kiểm thử quy tắc phức hợp

### Tình huống 1 — Cấp 1: Kiểm tra hai điều kiện truy cập của 10 tài khoản

**Từ vựng trong mục:** **Proposition** — mệnh đề; **AND** — và; **Boolean** — đúng/sai.

**Tình huống thực tế:** Cổng tài liệu có **10 tài khoản** U01…U10; mỗi dòng gồm trạng thái đã đăng nhập và đã xác minh (`True`/`False`). Chính sách chỉ cho phép truy cập nếu **cả hai** điều kiện đều đúng. Cần đếm số tài khoản được phép và mã bị từ chối, không sử dụng trạng thái giả định.

**Vì sao chọn cách này?** Toán tử `and` chỉ trả True khi cả hai mệnh đề đúng; nhóm còn lại là người chưa đáp ứng đủ. Đây là kiểm tra quy tắc Boolean đơn giản, không phải hệ thống xác thực thật.

**Quy trình:**
1. Lưu hai trạng thái theo cùng thứ tự 10 tài khoản.
2. Dùng `logged_in and verified` trên từng tài khoản.
3. Báo số được phép và số từ chối, đối chiếu tổng là 10.

```python
logged_in = [True,True,False,True,False,True,True,False,True,True]
verified = [True,False,True,True,False,False,True,True,True,False]
allowed = [a and b for a, b in zip(logged_in, verified)]
assert len(allowed) == 10
print("Tài khoản:", len(allowed))
print("Cho phép:", sum(allowed))
print("Từ chối:", len(allowed) - sum(allowed))
```

**Kết quả khi chạy:**

```text
Tài khoản: 10
Cho phép: 4
Từ chối: 6
```

Tài khoản chỉ đăng nhập nhưng chưa xác minh bị từ chối, vì một điều kiện đúng chưa đủ thỏa phép `and`.

### Tình huống 2 — Cấp 2: Kiểm thử đầy đủ bảng chân trị trên 12 lượt kiểm tra

**Từ vựng trong mục:** **Truth table** — bảng chân trị; **OR** — hoặc; **NOT** — phủ định.

**Tình huống thực tế:** Đội QA chạy **12 lượt kiểm tra**, gồm **4 tổ hợp** hai cờ `có đăng nhập` (p) và `đã xác minh` (q), lặp lại ở ba ngày khác nhau. Mỗi hàng là một cặp cờ của một ngày. Cần chứng minh các tổ hợp đã được bao phủ đủ, đếm số lượt có `p and q` và số lượt có `p or q`; không nhầm một tổ hợp lặp lại thành một tổ hợp mới.

**Vì sao chọn cách này?** Hai Boolean có đúng bốn trường hợp. Dùng `itertools.product` sinh bảng chân trị 4 trường hợp, gắn với 3 ngày thành 12 dòng, sau đó đếm hai phép logic khác nhau.

**Quy trình:**
1. Sinh bốn tổ hợp p/q từ `product` và gắn với ba ngày kiểm thử.
2. Kiểm tra mỗi tổ hợp xuất hiện ba lần.
3. Đếm số lần hai phép AND/OR nhận True và báo độ phủ bảng chân trị.

```python
from itertools import product
truth_table = list(product([True, False], repeat=2))
checks = [(day, p, q) for day in range(1, 4) for p, q in truth_table]
assert len(checks) == 12 and len(set((p, q) for day, p, q in checks)) == 4
print("Lượt kiểm tra:", len(checks))
print("Tổ hợp logic:", len(truth_table))
print("AND đúng:", sum(p and q for day, p, q in checks))
print("OR đúng:", sum(p or q for day, p, q in checks))
```

**Kết quả khi chạy:**

```text
Lượt kiểm tra: 12
Tổ hợp logic: 4
AND đúng: 3
OR đúng: 9
```

Bảng chân trị chỉ có bốn tổ hợp **khác nhau**; 12 là số lượt chạy có lặp theo ngày để kiểm tra tính nhất quán.

### Tình huống 3 — Cấp 3: Kiểm phép kéo theo trên 15 hồ sơ phê duyệt

**Từ vựng trong mục:** **Implication** — kéo theo; **Premise** — tiền đề; **Counterexample** — phản ví dụ.

**Tình huống thực tế:** Một tổ chức kiểm tra **15 hồ sơ** R01…R15, mỗi hàng có trạng thái đã phê duyệt (p) và đã có chứng chỉ (q). Quy định là: “**Nếu được phê duyệt thì phải có chứng chỉ**”. Cần tìm các hồ sơ vi phạm và giải thích vì sao hồ sơ **chưa phê duyệt** không tự động là vi phạm dù chưa có chứng chỉ.

**Vì sao chọn cách này?** Phép kéo theo `p ⇒ q` tương đương `(not p) or q`, chỉ sai khi `p=True` và `q=False`. Không nhầm với `p and q` vì như thế sẽ kết tội cả hồ sơ không thuộc đối tượng quy định.

**Quy trình:**
1. Lưu 15 cặp Boolean đúng theo ID.
2. Tính điều kiện tuân thủ bằng `(not p) or q`.
3. Liệt kê phản ví dụ và số hồ sơ tuân thủ.

```python
approved = [True,False,True,True,False,True,False,True,True,False,True,False,True,True,True]
certified = [True,False,False,True,False,True,True,False,True,True,True,False,True,False,True]
compliant = [(not p) or q for p, q in zip(approved, certified)]
violations = [f"R{i:02d}" for i, ok in enumerate(compliant, 1) if not ok]
assert len(compliant) == 15
print("Hồ sơ:", len(compliant))
print("Tuân thủ:", sum(compliant))
print("Vi phạm:", ", ".join(violations))
```

**Kết quả khi chạy:**

```text
Hồ sơ: 15
Tuân thủ: 12
Vi phạm: R03, R08, R14
```

Việc chưa phê duyệt khiến tiền đề sai; với một phép kéo theo, trường hợp đó không làm hỏng chính sách đang được kiểm tra.

### Tình huống 4 — Cấp 4: Đếm 18 cấu hình sản phẩm và lọc ràng buộc

**Từ vựng trong mục:** **Cartesian product** — tích Descartes; **Counting rule** — quy tắc nhân; **NOT** — phủ định.

**Tình huống thực tế:** Cửa hàng muốn bán áo với **3 màu**, **3 cỡ** và **2 chất liệu**; mỗi tổ hợp màu–cỡ–chất liệu là một cấu hình. Hệ thống tạo đúng **18 cấu hình**, nhưng chính sách mẫu **không cho màu Đỏ dùng chất liệu Poly**, bất kể cỡ. Cần đếm cấu hình hợp lệ, bị loại và kiểm tra kết quả bằng cả việc tạo tổ hợp lẫn quy tắc đếm.

**Vì sao chọn cách này?** `itertools.product` tạo mọi kết hợp từ ba nhóm lựa chọn, tương ứng nguyên lý nhân. Một điều kiện Boolean loại cấu hình xung đột; không xóa toàn bộ màu Đỏ hay toàn bộ Poly.

**Quy trình:**
1. Tạo 18 tuple từ màu, cỡ, chất liệu.
2. Lọc những tuple có đồng thời Đỏ và Poly.
3. Đối chiếu số hợp lệ + số loại = 18 và in kết quả.

```python
from itertools import product
colors = ["Đỏ", "Xanh", "Trắng"]
sizes = ["S", "M", "L"]
materials = ["Cotton", "Poly"]
options = list(product(colors, sizes, materials))
valid = [item for item in options if not (item[0] == "Đỏ" and item[2] == "Poly")]
assert len(options) == len(colors) * len(sizes) * len(materials) == 18
print("Cấu hình:", len(options))
print("Hợp lệ:", len(valid))
print("Loại:", len(options) - len(valid))
print("Ví dụ đầu:", " - ".join(valid[0]))
```

**Kết quả khi chạy:**

```text
Cấu hình: 18
Hợp lệ: 15
Loại: 3
Ví dụ đầu: Đỏ - S - Cotton
```

Tích Descartes liệt kê **toàn bộ cấu hình**; trong bài này ràng buộc giảm số cấu hình từ 18 còn 15, chứ không tạo thêm cấu hình mới.

### Tình huống 5 — Cấp 5: Thử 20 yêu cầu truy cập với quy tắc nhiều điều kiện và ngoại lệ

**Từ vựng trong mục:** **Compound logic** — logic phối hợp; **Precedence** — độ ưu tiên; **Invariant** — điều kiện bất biến.

**Tình huống thực tế:** Cổng tài liệu học tập nhận **20 yêu cầu giả lập** U01…U20. Mỗi hàng có tuổi (năm), sự đồng ý của người giám hộ, xác minh tài khoản và cờ đã khóa. **Quy tắc minh họa**: cho phép khi (**đủ 18 tuổi hoặc có đồng ý**) **và** đã xác minh **và không bị khóa**. Cần báo số được phép, số bị từ chối và xác nhận không có yêu cầu đã khóa nào được phép; đây không phải chính sách truy cập thực tế của một dịch vụ.

**Vì sao chọn cách này?** Nhóm điều kiện `or` trong ngoặc thể hiện một trong hai cơ sở truy cập; các điều kiện `and` khác là bắt buộc. `not blocked` ngăn trường hợp đã khóa nhưng vẫn đủ tuổi/xác minh được mở quyền; kiểm chứng bằng `assert` phát hiện sai lệch quy tắc.

**Quy trình:**
1. Tạo 20 bản ghi đầy đủ bốn thuộc tính.
2. Dùng một biểu thức Boolean có ngoặc cho mọi bản ghi.
3. Đếm kết quả, kiểm tra tổng 20 và khẳng định mọi yêu cầu bị khóa đều bị từ chối.

```python
requests = [{"age":16,"consent":False,"verified":True,"blocked":False},{"age":17,"consent":True,"verified":True,"blocked":False},{"age":18,"consent":True,"verified":False,"blocked":False},{"age":19,"consent":True,"verified":True,"blocked":False},{"age":20,"consent":True,"verified":True,"blocked":False},{"age":21,"consent":False,"verified":True,"blocked":False},{"age":22,"consent":True,"verified":False,"blocked":False},{"age":23,"consent":True,"verified":True,"blocked":True},{"age":16,"consent":True,"verified":True,"blocked":False},{"age":17,"consent":True,"verified":True,"blocked":False},{"age":18,"consent":False,"verified":False,"blocked":False},{"age":19,"consent":True,"verified":True,"blocked":False},{"age":20,"consent":True,"verified":True,"blocked":False},{"age":21,"consent":True,"verified":True,"blocked":False},{"age":22,"consent":True,"verified":False,"blocked":False},{"age":23,"consent":False,"verified":True,"blocked":False},{"age":16,"consent":True,"verified":True,"blocked":False},{"age":17,"consent":True,"verified":True,"blocked":False},{"age":18,"consent":True,"verified":False,"blocked":True},{"age":19,"consent":True,"verified":True,"blocked":False}]
allowed = [((item["age"] >= 18 or item["consent"])
            and item["verified"] and not item["blocked"])
           for item in requests]
assert len(requests) == len(allowed) == 20
assert all(not allowed[i] for i, item in enumerate(requests) if item["blocked"])
print("Yêu cầu:", len(requests))
print("Cho phép:", sum(allowed))
print("Từ chối:", len(allowed) - sum(allowed))
print("Yêu cầu bị khóa:", sum(item["blocked"] for item in requests))
```

**Kết quả khi chạy:**

```text
Yêu cầu: 20
Cho phép: 13
Từ chối: 7
Yêu cầu bị khóa: 2
```

Từng yêu cầu là một hàng gồm nhiều mệnh đề, không phải một phần tử đơn. Quy tắc là ví dụ học thuật; hệ thống thực phải dựa trên chính sách xác thực và bảo vệ dữ liệu được phê duyệt.

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

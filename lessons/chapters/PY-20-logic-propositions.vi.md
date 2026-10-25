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
# Mục đích: Kiểm một phát biểu logic bằng phép so sánh lớn hơn.
# Dữ liệu: Phát biểu 3 lớn hơn 1 là đúng (True), không phải phép gán.
# Toán tử > so sánh 3 với 1 và trả giá trị Boolean True; print() hiển thị kết quả.
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
# Mục đích: Liệt kê bảng chân trị đủ bốn cặp p/q và kết quả AND, OR.
# Dữ liệu: Hai mệnh đề p và q, mỗi mệnh đề có hai giá trị True/False.
# Vòng ngoài lần lượt đặt p=True rồi p=False.
for p in [True, False]:
    # Vòng trong thử q=True và q=False cho MỖI p, tạo 2×2=4 cặp.
    for q in [True, False]:
        # and chỉ True khi CẢ p và q đều đúng; or True nếu ÍT NHẤT một trong hai đúng.
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
# Mục đích: Biểu diễn quy tắc nếu được duyệt thì phải ký bằng (not p) or q.
# Dữ liệu: p là approved (đã duyệt), q là signed (đã ký); p=True, q=False vi phạm điều kiện.
# Giả định hồ sơ đã được duyệt (p đúng).
approved = True
# Giả định hồ sơ chưa ký (q sai).
signed = False
# Mệnh đề kéo theo p→q tương đương (not p) or q: chỉ False khi p đúng mà q sai.
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
# Mục đích: Áp dụng nguyên lý nhân: số kết hợp màu sắc và kích cỡ sản phẩm.
# Dữ liệu: Có 3 màu và 4 cỡ độc lập; mỗi màu kết hợp được với từng cỡ.
# Có ba lựa chọn màu, không phải ba sản phẩm đã sản xuất.
colors = 3
# Có bốn lựa chọn kích cỡ cho mỗi màu.
sizes = 4
# Nguyên lý nhân cho 3×4=12 cặp cấu hình, giả sử mọi cặp đều hợp lệ.
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

**Tình huống thực tế:** Cổng tài liệu học tập có **10 tài khoản U01–U10**. Với mỗi tài khoản, hệ thống ghi hai thông tin **đã đăng nhập** và **đã xác minh**, mỗi thông tin là `True` (đúng) hoặc `False` (chưa đúng). Quy tắc giả lập: chỉ người **đã đăng nhập và đã xác minh** mới được truy cập. Nhân viên cần đếm số tài khoản được phép và bị từ chối; một tài khoản chỉ đạt một trong hai yêu cầu thì vẫn phải bị từ chối.

**Vì sao chọn cách này?** **Boolean** là kiểu thông tin chỉ có hai trạng thái: đúng (`True`) hoặc sai (`False`). `and` có nghĩa là **cả hai điều kiện đều phải đúng**: đã đăng nhập nhưng chưa xác minh vẫn trả `False`. Chương trình duyệt đồng thời hai danh sách, kiểm từng cặp của **cùng tài khoản**, rồi lưu một kết quả cho mỗi người. `sum(allowed)` đếm số `True` (trong phép cộng, `True` được tính như 1), còn số bị từ chối là số tài khoản trừ số được phép. Không dùng `or`, vì `or` chỉ đòi **một** điều kiện, sẽ mở quyền quá sớm.

**Quy trình:**
1. Lưu hai trạng thái theo cùng thứ tự 10 tài khoản.
2. Dùng `logged_in and verified` trên từng tài khoản.
3. Báo số được phép và số từ chối, đối chiếu tổng là 10.

```python
# Mục đích: Kiểm quyền 10 tài khoản: chỉ tài khoản vừa đăng nhập vừa xác minh mới được phép.
# Dữ liệu: 10 trạng thái logged_in True/False và 10 verified True/False cùng vị trí tài khoản.
# List 10 cờ đăng nhập theo thứ tự tài khoản.
logged_in = [True,True,False,True,False,True,True,False,True,True]
# List 10 cờ xác minh khớp từng vị trí với logged_in.
verified = [True,False,True,True,False,False,True,True,True,False]
# List rỗng lưu kết quả cho phép True/False của từng tài khoản.
allowed = []
# zip() ghép hai cờ ở CÙNG vị trí thành một tài khoản, không tạo mọi tổ hợp.
for logged, verified_status in zip(logged_in, verified):
    # and chỉ True nếu đăng nhập và xác minh đều True; append() giữ đúng một kết quả mỗi tài khoản.
    allowed.append(logged and verified_status)
# len() đếm đủ 10 tài khoản đã kiểm.
if len(allowed) != 10:
    # ValueError dừng khi số lượng hoặc quy tắc logic không nhất quán với dữ liệu đầu vào.
    raise ValueError("Cần kiểm tra đủ 10 tài khoản.")
# len() đếm đủ 10 tài khoản đã kiểm.
print("Tài khoản:", len(allowed))
# Trong Python True đếm như 1 và False như 0; sum() đếm tài khoản được phép.
print("Cho phép:", sum(allowed))
# len() đếm đủ 10 tài khoản đã kiểm.
# Trong Python True đếm như 1 và False như 0; sum() đếm tài khoản được phép.
# Tổng trừ được phép ra số tài khoản bị từ chối.
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

**Tình huống thực tế:** Đội kiểm thử phần mềm muốn xem quy tắc truy cập hoạt động ra sao với **hai trạng thái đúng/sai**: `p` là đã đăng nhập, `q` là đã xác minh. Hai trạng thái này tạo **4 cách kết hợp**, từ cả hai đúng đến cả hai sai. Nhân viên chạy lại cả bốn cách trong **3 ngày**, tổng cộng **12 lượt kiểm tra**, và muốn xác nhận không thiếu trường hợp nào, đồng thời đếm `p and q` và `p or q` đúng bao nhiêu lượt.

**Vì sao chọn cách này?** **Bảng chân trị** là cách liệt kê **tất cả các trường hợp đúng/sai có thể có** để kiểm tra một quy tắc, thay vì chỉ thử trường hợp thuận lợi. `itertools.product([True, False], repeat=2)` sinh bốn cặp `p, q` có thể có. Vòng lặp bên ngoài lặp các cặp ấy trong 3 ngày thành 12 lượt; **lượt thử** là số lần chạy, còn **tổ hợp khác nhau** vẫn chỉ có bốn. Với `and`, chỉ cặp **cả hai đúng** mới cho kết quả đúng; với `or`, mọi cặp có **ít nhất một trạng thái đúng** đều đúng. Dùng set các cặp kiểm tra đã bao phủ đủ bốn trường hợp, không nhầm ba lần thử lặp là ba trường hợp mới.

**Quy trình:**
1. Sinh bốn tổ hợp p/q từ `product` và gắn với ba ngày kiểm thử.
2. Kiểm tra mỗi tổ hợp xuất hiện ba lần.
3. Đếm số lần hai phép AND/OR nhận True và báo độ phủ bảng chân trị.

```python
# Mục đích: Dùng itertools.product sinh bảng chân trị bốn cặp, lặp ba ngày tạo 12 lượt kiểm.
# Dữ liệu: p,q là hai mệnh đề Boolean; đủ 4 tổ hợp mỗi ngày × 3 ngày.
# product() của itertools tạo tích Descartes: mọi tổ hợp từ các nhóm lựa chọn.
from itertools import product
# repeat=2 dùng cùng tập hai giá trị cho p và q, sinh 4 cặp; list() lưu lại.
truth_table = list(product([True, False], repeat=2))
checks = []
# range(1,4) sinh ngày 1,2,3, không lấy 4.
for day in range(1, 4):
    # Tách mỗi tuple (p,q) của bảng chân trị cho từng ngày.
    for p, q in truth_table:
        # append() thêm bộ (ngày,p,q) vào list, tổng 12 bộ.
        checks.append((day, p, q))
# set() tập rỗng chỉ lưu cặp logic không trùng, bỏ thông tin ngày.
pairs = set()
for day, p, q in checks:
    # add() tự loại cặp trùng giữa ba ngày để còn bốn tổ hợp duy nhất.
    pairs.add((p, q))
# Kiểm đúng 12 lượt và đủ bốn cặp logic trước khi kết luận.
if len(checks) != 12 or len(pairs) != 4:
    # ValueError dừng khi số lượng hoặc quy tắc logic không nhất quán với dữ liệu đầu vào.
    raise ValueError("Cần có 12 lượt kiểm tra với đủ bốn tổ hợp logic.")
print("Lượt kiểm tra:", len(checks))
print("Tổ hợp logic:", len(truth_table))
and_count = 0
or_count = 0
for day, p, q in checks:
    # AND chỉ đúng khi cả p và q cùng True; += 1 đếm lượt thỏa.
    if p and q:
        and_count += 1
    # OR đúng khi ít nhất một mệnh đề đúng; += 1 đếm lượt thỏa.
    if p or q:
        or_count += 1
print("AND đúng:", and_count)
print("OR đúng:", or_count)
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

**Tình huống thực tế:** Một tổ chức kiểm tra **15 hồ sơ phê duyệt R01–R15**. Mỗi dòng ghi hai trạng thái đúng/sai: hồ sơ **đã được phê duyệt** (`p`) và **đã có chứng chỉ** (`q`). Nội quy giả lập nói: **nếu đã được phê duyệt thì phải có chứng chỉ**. Nhân viên cần tìm đúng những hồ sơ được phê duyệt nhưng chưa có chứng chỉ, không gắn nhãn vi phạm cho một hồ sơ chưa phê duyệt chỉ vì người đó cũng chưa có chứng chỉ.

**Vì sao chọn cách này?** **Kéo theo** là cách diễn đạt quy định kiểu '**nếu p thì q**'. Quy định này **chỉ bị vi phạm** khi điều kiện đầu đã xảy ra (`p=True`: được phê duyệt) nhưng yêu cầu sau **không được đáp ứng** (`q=False`: thiếu chứng chỉ). Biểu thức `(not p) or q` diễn tả chính xác điều đó: `not` đảo đúng thành sai và ngược lại; `or` chỉ cần một vế đúng. Người chưa được phê duyệt chưa phải đối tượng bắt buộc của quy định này nên không tự động vi phạm, dù chưa có chứng chỉ. Nếu thay bằng `p and q`, chương trình sẽ đánh dấu sai cả nhóm chưa phê duyệt.

**Quy trình:**
1. Lưu 15 cặp Boolean đúng theo ID.
2. Tính điều kiện tuân thủ bằng `(not p) or q`.
3. Liệt kê phản ví dụ và số hồ sơ tuân thủ.

```python
# Mục đích: Kiểm 15 hồ sơ tuân thủ mệnh đề 'nếu duyệt thì phải có chứng nhận'.
# Dữ liệu: 15 cờ approved/certified theo cùng vị trí, quy tắc p→q chỉ sai khi p=True và q=False.
# 15 cờ hồ sơ đã duyệt; True nghĩa điều kiện tiền đề p đúng.
approved = [True,False,True,True,False,True,False,True,True,False,True,False,True,True,True]
# 15 cờ có chứng nhận tương ứng từng hồ sơ; True nghĩa hệ quả q đúng.
certified = [True,False,False,True,False,True,True,False,True,True,True,False,True,False,True]
compliant = []
# zip() ghép cờ duyệt và chứng nhận của chính một hồ sơ theo vị trí.
for approved_status, certificate_status in zip(approved, certified):
    # Quy tắc p→q: khi không duyệt thì không vi phạm; nếu đã duyệt phải có chứng nhận.
    # append() lưu Boolean tuân thủ của mỗi hồ sơ theo thứ tự.
    compliant.append((not approved_status) or certificate_status)
violations = []
# enumerate(...,1) đánh số hồ sơ R01..R15 (không dùng chỉ số 0 làm mã).
for i, ok in enumerate(compliant, 1):
    # not tìm những kết quả tuân thủ bằng False.
    if not ok:
        # append() lưu mã vi phạm; f-string :02d tạo số thứ tự hai chữ số.
        violations.append(f"R{i:02d}")
if len(compliant) != 15:
    # ValueError dừng khi số lượng hoặc quy tắc logic không nhất quán với dữ liệu đầu vào.
    raise ValueError("Cần kiểm tra đủ 15 hồ sơ.")
print("Hồ sơ:", len(compliant))
# sum() đếm số True (tuân thủ) trong list Boolean.
print("Tuân thủ:", sum(compliant))
# join() ghép mã vi phạm bằng dấu phẩy và khoảng trắng.
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

**Tình huống thực tế:** Nhà bán hàng thiết kế áo với **3 màu** (Đỏ, Xanh, Trắng), **3 cỡ** (S, M, L) và **2 chất liệu** (Cotton, Poly). Một cấu hình áo là một lựa chọn từ **mỗi nhóm**, ví dụ Đỏ–M–Cotton. Theo quy định minh họa, áo **màu Đỏ không được làm bằng Poly** ở bất kỳ cỡ nào. Người quản lý muốn liệt kê đủ **18 cấu hình ban đầu**, rồi đếm bao nhiêu cấu hình hợp lệ và bao nhiêu cấu hình phải loại.

**Vì sao chọn cách này?** **Tổ hợp sản phẩm** là cách chọn **một màu, một cỡ và một chất liệu** cùng lúc. `itertools.product` sinh lần lượt mọi bộ ba mà không bỏ sót: ba màu, ba cỡ và hai chất liệu tạo 18 cấu hình. Sau đó kiểm riêng từng cấu hình: chỉ loại khi **đồng thời** màu là Đỏ **và** chất liệu là Poly; cỡ S, M hay L không làm thay đổi quy tắc này. Dùng `not (...)` nghĩa là **giữ lại những bộ không rơi vào trường hợp bị cấm**. Không xóa tất cả áo Đỏ hoặc tất cả chất liệu Poly, vì nhiều cách phối khác vẫn hợp lệ.

**Quy trình:**
1. Tạo 18 tuple từ màu, cỡ, chất liệu.
2. Lọc những tuple có đồng thời Đỏ và Poly.
3. Đối chiếu số hợp lệ + số loại = 18 và in kết quả.

```python
# Mục đích: Sinh 18 cấu hình màu/cỡ/chất liệu, loại mọi cấu hình Đỏ + Poly.
# Dữ liệu: 3 màu Đỏ/Xanh/Trắng × 3 cỡ S/M/L × 2 chất liệu Cotton/Poly = 18 cấu hình.
# itertools.product sinh tất cả tổ hợp giữa nhiều danh sách độc lập.
from itertools import product
# Ba màu là ba lựa chọn của thành phần thứ nhất.
colors = ["Đỏ", "Xanh", "Trắng"]
# Ba cỡ là ba lựa chọn thành phần thứ hai.
sizes = ["S", "M", "L"]
# Hai chất liệu tạo chiều lựa chọn thứ ba.
materials = ["Cotton", "Poly"]
# product() tạo 3×3×2=18 tuple (màu,cỡ,chất liệu), list() giữ toàn bộ.
options = list(product(colors, sizes, materials))
valid = []
# Duyệt từng tuple cấu hình.
for item in options:
    # [0] là màu, [2] chất liệu; and nhận tổ hợp Đỏ cùng Poly, not đảo để chỉ giữ tổ hợp KHÔNG bị cấm.
    if not (item[0] == "Đỏ" and item[2] == "Poly"):
        # append() lưu tuple hợp lệ; không sửa list gốc options.
        valid.append(item)
# Nguyên lý nhân xác minh phải có 18 tổ hợp trước khi lọc.
if len(options) != 18 or len(colors) * len(sizes) * len(materials) != 18:
    # ValueError dừng khi số lượng hoặc quy tắc logic không nhất quán với dữ liệu đầu vào.
    raise ValueError("Cần liệt kê đúng 18 tổ hợp sản phẩm.")
print("Cấu hình:", len(options))
print("Hợp lệ:", len(valid))
print("Loại:", len(options) - len(valid))
# valid[0] là tuple cấu hình hợp lệ đầu; join() nối ba trường thành chuỗi dễ đọc.
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

**Tình huống thực tế:** Cổng tài liệu nhận **20 yêu cầu truy cập giả lập**. Mỗi yêu cầu ghi tuổi (**năm**), có được người giám hộ đồng ý hay không, tài khoản đã xác minh hay chưa và tài khoản có đang bị khóa hay không. Quy tắc minh họa: người **từ 18 tuổi hoặc đã có sự đồng ý** được xét tiếp; sau đó bắt buộc phải **đã xác minh** và **không bị khóa**. Người quản lý cần đếm số yêu cầu được phép, bị từ chối và số tài khoản bị khóa, đồng thời xác nhận mọi yêu cầu đã khóa đều không thể được cho phép.

**Vì sao chọn cách này?** Quy tắc gồm **ba phần**, cần đặt ngoặc để người học nhìn thấy rõ: (1) **tuổi từ 18 hoặc có đồng ý** — chỉ cần một điều kiện; (2) **đã xác minh** — bắt buộc; (3) **không bị khóa** — bắt buộc. `or` kết nối hai cách đáp ứng phần (1), còn `and` kết nối kết quả ấy với hai phần bắt buộc. `not blocked` đổi cờ bị khóa thành điều kiện **không bị khóa**; vì thế yêu cầu đã khóa luôn không đủ điều kiện, kể cả người lớn đã xác minh. Chương trình kiểm tra lại từng yêu cầu bị khóa và **báo lỗi nếu có trường hợp được phép**, giúp phát hiện sai quy tắc. Đây chỉ là chính sách **mô phỏng** của bài tập, không mô tả luật hay điều kiện truy cập thật của dịch vụ.

**Quy trình:**
1. Tạo 20 bản ghi đầy đủ bốn thuộc tính.
2. Dùng một biểu thức Boolean có ngoặc cho mọi bản ghi.
3. Đếm kết quả, kiểm tra tổng 20 và khẳng định mọi yêu cầu bị khóa đều bị từ chối.

```python
# Mục đích: Kiểm 20 yêu cầu truy cập theo tuổi hoặc đồng ý, đồng thời đã xác minh và không bị khóa.
# Dữ liệu: 20 dict gồm age năm, consent/verified/blocked là cờ Boolean; quy tắc chỉ mang tính ví dụ, không phải chính sách pháp luật.
# Mỗi dict là một yêu cầu: tuổi (năm), cờ đồng ý, cờ xác minh và cờ bị khóa.
requests = [{"age":16,"consent":False,"verified":True,"blocked":False},{"age":17,"consent":True,"verified":True,"blocked":False},{"age":18,"consent":True,"verified":False,"blocked":False},{"age":19,"consent":True,"verified":True,"blocked":False},{"age":20,"consent":True,"verified":True,"blocked":False},{"age":21,"consent":False,"verified":True,"blocked":False},{"age":22,"consent":True,"verified":False,"blocked":False},{"age":23,"consent":True,"verified":True,"blocked":True},{"age":16,"consent":True,"verified":True,"blocked":False},{"age":17,"consent":True,"verified":True,"blocked":False},{"age":18,"consent":False,"verified":False,"blocked":False},{"age":19,"consent":True,"verified":True,"blocked":False},{"age":20,"consent":True,"verified":True,"blocked":False},{"age":21,"consent":True,"verified":True,"blocked":False},{"age":22,"consent":True,"verified":False,"blocked":False},{"age":23,"consent":False,"verified":True,"blocked":False},{"age":16,"consent":True,"verified":True,"blocked":False},{"age":17,"consent":True,"verified":True,"blocked":False},{"age":18,"consent":True,"verified":False,"blocked":True},{"age":19,"consent":True,"verified":True,"blocked":False}]
# List kết quả giữ một giá trị cho phép True/False trên mỗi yêu cầu.
allowed = []
# Duyệt từng dict, lấy trường qua item['tên_trường'].
for item in requests:
    # or chỉ đòi từ 18 tuổi HOẶC đã có đồng ý; đây là giả định bài học, không phải quy định truy cập thực tế.
    age_or_consent_ok = item["age"] >= 18 or item["consent"]
    # and yêu cầu đủ ba điều kiện: tuổi/đồng ý đạt, đã xác minh, không bị khóa; not đảo cờ blocked.
    can_access = age_or_consent_ok and item["verified"] and not item["blocked"]
    # append() lưu kết quả của đúng một yêu cầu sau kiểm.
    allowed.append(can_access)
# Kiểm đủ 20 yêu cầu và 20 kết quả tương ứng để không bỏ bản ghi.
if len(requests) != 20 or len(allowed) != 20:
    # ValueError dừng khi số lượng hoặc quy tắc logic không nhất quán với dữ liệu đầu vào.
    raise ValueError("Cần kiểm tra đủ 20 yêu cầu truy cập.")
# enumerate() không có start mặc định đánh số từ 0 để cùng index với allowed[i].
for i, item in enumerate(requests):
    # Phát hiện lỗi logic nếu bất kỳ yêu cầu đã khóa nào lại được cho phép.
    if item["blocked"] and allowed[i]:
        # ValueError dừng khi số lượng hoặc quy tắc logic không nhất quán với dữ liệu đầu vào.
        raise ValueError("Yêu cầu bị khóa không được phép truy cập.")
print("Yêu cầu:", len(requests))
# sum() trên Boolean đếm số True (cho phép); số từ chối = tổng - True.
print("Cho phép:", sum(allowed))
# sum() trên Boolean đếm số True (cho phép); số từ chối = tổng - True.
print("Từ chối:", len(allowed) - sum(allowed))
blocked_count = 0
# Duyệt từng dict, lấy trường qua item['tên_trường'].
for item in requests:
    if item["blocked"]:
        # += 1 đếm riêng các yêu cầu có cờ bị khóa, không đồng nhất với mọi lý do từ chối.
        blocked_count += 1
print("Yêu cầu bị khóa:", blocked_count)
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

**Giải thích:** Nhóm có giao nhau không được đếm trùng. Với hai nhóm có giao, công thức `|A ∪ B| = |A| + |B| − |A ∩ B|` trừ phần được tính hai lần.

## 8. Nối sang bài tiếp

`Boolean → logic mệnh đề → tổ hợp → xác suất`.

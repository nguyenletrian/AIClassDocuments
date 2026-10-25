# PY-22 — Hoán vị, tổ hợp và tam giác Pascal


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Permutation** — hoán vị; **Combination** — tổ hợp.

`Nguyên lý đếm → hoán vị/tổ hợp → phân phối nhị thức`

**Học xong dùng để làm gì?** Tính số cách chọn người, chia vai hoặc sắp lịch, phân biệt có và không xét thứ tự.

**Kết nối kiến thức tiếp theo:** PY-23 mô hình hóa quan hệ và độ tương đồng giữa đối tượng bằng đồ thị/Jaccard.

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
# Mục đích: Chọn và phân vai có thứ tự.
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
# Mục đích: Chọn nhóm không phân vai.
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
# Mục đích: Sắp xếp tất cả phần tử.
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
# Mục đích: Binomial coefficient và tam giác Pascal.
import math

counts = []
for k in range(5):
    counts.append(math.comb(4, k))
print(counts)
```

**Kết quả khi chạy:**

```text
[1, 4, 6, 4, 1]
```

Hàng thứ tư tính từ 0 có năm hệ số, ứng với k từ 0 đến 4.
## 5. Năm tình huống hoán vị và tổ hợp — từ phân vai đến chọn nhóm có ràng buộc

### Tình huống 1 — Cấp 1: Phân vai trưởng và phó từ 10 ứng viên

**Từ vựng trong mục:** **Permutation** — chọn có thứ tự; **Role** — vai trò.

**Tình huống thực tế:** Câu lạc bộ có **10 ứng viên U01–U10** đã đủ điều kiện. Cần chọn **một trưởng nhóm** và **một phó nhóm** từ hai người khác nhau. Nếu U01 làm trưởng và U02 làm phó thì đó là phương án khác với U02 làm trưởng, U01 làm phó. Người phụ trách muốn biết tổng số cách phân vai và xem một phương án đầu tiên từ chương trình.

**Vì sao chọn cách này?** **Chỉnh hợp** phù hợp khi **vị trí, vai trò hoặc thứ tự có ý nghĩa**. Trưởng và phó không giống nhau, nên đổi hai người tạo phương án mới. `math.perm(len(candidates), 2)` đếm cách điền lần lượt hai vai bằng hai người khác nhau; `itertools.permutations(candidates, 2)` có thể liệt kê các cặp để kiểm tra. Vòng `for` lấy cặp đầu và `break` vì bài chỉ cần **một ví dụ**, không phải in toàn bộ các phương án. Nếu dùng tổ hợp không xét thứ tự thì sẽ gộp nhầm hai cách giao chức danh khác nhau.

**Quy trình:**
1. Lưu đúng 10 ID ứng viên.
2. Đếm phương án có thứ tự bằng `math.perm`.
3. Liệt kê kết quả đầu tiên để xác minh vai trò khác nhau.

```python
import math
from itertools import permutations
candidates = ["U01","U02","U03","U04","U05","U06","U07","U08","U09","U10"]
first = None
for pair in permutations(candidates, 2):
    first = pair
    break
if first is None:
    raise ValueError("Cần ít nhất hai ứng viên để phân vai.")
if len(candidates) != 10:
    raise ValueError("Cần đúng 10 ứng viên.")
print("Ứng viên:", len(candidates))
print("Cách phân vai:", math.perm(len(candidates), 2))
print("Phân vai đầu:", first[0], first[1])
```

**Kết quả khi chạy:**

```text
Ứng viên: 10
Cách phân vai: 90
Phân vai đầu: U01 U02
```

Người U01 làm trưởng và U02 làm phó khác cách đảo vai; không cho phép một ứng viên bị chọn hai lần.

### Tình huống 2 — Cấp 2: Chọn nhóm 3 người từ 12 tình nguyện viên

**Từ vựng trong mục:** **Combination** — chọn không xét thứ tự; **Distinct** — không trùng người.

**Tình huống thực tế:** Ban tổ chức sự kiện có **12 tình nguyện viên S01–S12**. Mỗi đội trực chỉ cần **3 người ngang vai**, không có vai trò trưởng hay phó; một người không được xuất hiện hai lần trong một đội. Đội gồm S01, S02, S03 vẫn là cùng một đội khi đọc tên theo thứ tự S03, S02, S01. Người quản lý muốn đếm các đội khác nhau và liệt kê một đội đầu tiên.

**Vì sao chọn cách này?** **Tổ hợp** dùng khi chỉ quan tâm **ai được chọn**, không quan tâm tên nào được viết trước. Đội S01–S02–S03 và S03–S01–S02 là một đội, vì cả ba người ngang vai. `math.comb(12, 3)` tính số đội khác nhau; `itertools.combinations(volunteers, 3)` liệt kê mỗi bộ ba đúng một lần để chương trình có thể đối chiếu kết quả. Không dùng chỉnh hợp, vì chỉnh hợp tính riêng các thứ tự của cùng ba người nên số đội sẽ lớn hơn thực tế.

**Quy trình:**
1. Lưu 12 mã thành viên.
2. Dùng tổ hợp chọn ba mã, không xét thứ tự.
3. So số tổ với danh sách liệt kê để xác nhận.

```python
import math
from itertools import combinations
volunteers = ["S01","S02","S03","S04","S05","S06","S07","S08","S09","S10","S11","S12"]
groups = list(combinations(volunteers, 3))
if len(volunteers) != 12:
    raise ValueError("Cần đủ 12 tình nguyện viên.")
if len(groups) != math.comb(12, 3):
    raise ValueError("Số nhóm ba người phải khớp số tổ hợp lý thuyết.")
print("Tình nguyện viên:", len(volunteers))
print("Số nhóm:", len(groups))
print("Nhóm đầu:", ", ".join(groups[0]))
```

**Kết quả khi chạy:**

```text
Tình nguyện viên: 12
Số nhóm: 220
Nhóm đầu: S01, S02, S03
```

Bài này khác cấp 1 ở chỗ đổi vị trí ba người **không** tạo nhóm mới; nhận biết thứ tự quan trọng hay không quyết định phép đếm.

### Tình huống 3 — Cấp 3: Lọc 15 ứng viên trước khi chọn hai vai kiểm thử

**Từ vựng trong mục:** **Eligibility** — đủ điều kiện; **Permutation** — phân vai; **Combination** — chọn nhóm.

**Tình huống thực tế:** Đội kiểm thử phần mềm có **15 hồ sơ nhân sự T01–T15**. Mỗi hồ sơ ghi kỹ năng Python, AI hoặc SQL và cờ `available` cho biết người đó có sẵn sàng hay không. Dự án cần **hai người có vai trò khác nhau**, một người viết kiểm thử và một người duyệt; chỉ người sẵn sàng và có kỹ năng **Python hoặc AI** được chọn. Nhân sự muốn đếm người đủ chuẩn, số đội hai người không phân vai và số cách giao hai vai thực tế.

**Vì sao chọn cách này?** Đầu tiên phải **lọc người đủ điều kiện** theo `available` và kỹ năng; số 15 là tổng hồ sơ, **không phải tổng người được chọn**. Sau lọc, nếu chỉ hỏi chọn hai đồng đội thì dùng `math.comb` vì hai người ngang vai. Nếu hỏi ai viết và ai duyệt thì dùng `math.perm` vì đổi vai tạo cách giao nhiệm vụ khác. Như vậy cùng một danh sách hợp lệ có thể trả hai con số khác nhau vì **câu hỏi kinh doanh khác nhau**, chứ không phải hai thuật toán mâu thuẫn.

**Quy trình:**
1. Kiểm tra từng hồ sơ trong 15 dòng để lọc kỹ năng và cờ sẵn sàng.
2. Đếm số cặp không phân vai bằng `comb`.
3. Đếm số phương án gán hai vai bằng `perm`, xác nhận mỗi cặp có hai cách phân vai.

```python
import math
people = [{"id":"T01","skill":"Python","available":True},{"id":"T02","skill":"AI","available":True},{"id":"T03","skill":"SQL","available":True},{"id":"T04","skill":"Python","available":True},{"id":"T05","skill":"AI","available":False},{"id":"T06","skill":"SQL","available":True},{"id":"T07","skill":"Python","available":True},{"id":"T08","skill":"AI","available":True},{"id":"T09","skill":"SQL","available":True},{"id":"T10","skill":"Python","available":False},{"id":"T11","skill":"AI","available":True},{"id":"T12","skill":"SQL","available":True},{"id":"T13","skill":"Python","available":True},{"id":"T14","skill":"AI","available":True},{"id":"T15","skill":"SQL","available":False}]
eligible = []
for person in people:
    if person["available"] and person["skill"] in ("Python", "AI"):
        eligible.append(person["id"])
if len(people) != 15:
    raise ValueError("Cần kiểm tra 15 hồ sơ nhân sự.")
print("Hồ sơ:", len(people))
print("Đủ điều kiện:", len(eligible))
print("Chọn đội hai người:", math.comb(len(eligible), 2))
print("Phân hai vai:", math.perm(len(eligible), 2))
```

**Kết quả khi chạy:**

```text
Hồ sơ: 15
Đủ điều kiện: 8
Chọn đội hai người: 28
Phân hai vai: 56
```

Khác hai cấp đầu, phải lọc dữ liệu trước khi đếm. Không được chọn người không sẵn sàng hoặc thiếu kỹ năng phù hợp.

### Tình huống 4 — Cấp 4: Lập lịch ba lượt xử lý từ 18 ca lỗi có mức khẩn cấp

**Từ vựng trong mục:** **Ordered selection** — chọn có thứ tự; **Factorial** — giai thừa; **Constraint** — ràng buộc.

**Tình huống thực tế:** Đội trực vận hành có **18 phiếu sự cố C01–C18**; mỗi phiếu ghi mức `blocker` (ngăn hệ thống hoạt động), `high` (nghiêm trọng) hoặc `normal` (thông thường), cùng cờ `ready` về mức đầy đủ thông tin. Ca trực cần chọn **ba sự cố khác nhau xử lý theo thứ tự**. Chỉ các phiếu `blocker` hoặc `high` có `ready=True` được dùng; chẳng hạn C12 chưa sẵn sàng và cũng thuộc loại thông thường. Điều phối viên cần số lịch ba vị trí hợp lệ và một lịch đầu để đối chiếu.

**Vì sao chọn cách này?** **Lịch xử lý** gồm ba vị trí đầu–giữa–cuối, nên thứ tự C01 rồi C04 rồi C07 khác C07 rồi C04 rồi C01, dù chọn cùng ba sự cố. Chương trình duyệt 18 hồ sơ, giữ các dòng vừa **đủ thông tin (`ready`)** vừa ở mức `blocker` hoặc `high`; không mặc định mọi phiếu là hợp lệ. `permutations(eligible, 3)` liệt kê các lịch gồm ba sự cố **không lặp**; `math.perm` đếm để kiểm tra. Cách này mới chỉ liệt kê **phương án thứ tự** theo tiêu chí đã cho, chưa tính thời lượng xử lý hay ưu tiên `blocker` đứng trước `high` vì ví dụ không đặt thêm quy định ấy.

**Quy trình:**
1. Duyệt 18 hồ sơ, chỉ giữ ca khẩn cấp có cờ sẵn sàng.
2. Đếm các lịch có thứ tự gồm ba ca không lặp.
3. Liệt kê lịch đầu, kiểm số lịch với `math.perm`.

```python
import math
from itertools import permutations
incidents = [{"id":"C01","severity":"blocker","ready":True},{"id":"C02","severity":"normal","ready":True},{"id":"C03","severity":"normal","ready":True},{"id":"C04","severity":"high","ready":True},{"id":"C05","severity":"normal","ready":True},{"id":"C06","severity":"normal","ready":True},{"id":"C07","severity":"blocker","ready":True},{"id":"C08","severity":"normal","ready":True},{"id":"C09","severity":"normal","ready":True},{"id":"C10","severity":"high","ready":True},{"id":"C11","severity":"normal","ready":True},{"id":"C12","severity":"normal","ready":False},{"id":"C13","severity":"blocker","ready":True},{"id":"C14","severity":"normal","ready":True},{"id":"C15","severity":"normal","ready":True},{"id":"C16","severity":"high","ready":True},{"id":"C17","severity":"normal","ready":True},{"id":"C18","severity":"normal","ready":True}]
eligible = []
for row in incidents:
    if row["ready"] and row["severity"] in ("blocker", "high"):
        eligible.append(row["id"])
schedules = list(permutations(eligible, 3))
if len(incidents) != 18:
    raise ValueError("Cần đủ 18 sự cố đã ghi nhận.")
if len(schedules) != math.perm(len(eligible), 3):
    raise ValueError("Số lịch ba ca phải khớp số cách xếp có thứ tự.")
print("Sự cố:", len(incidents))
print("Đủ tiêu chí:", len(eligible))
print("Lịch 3 ca:", len(schedules))
print("Lịch đầu:", ", ".join(schedules[0]))
```

**Kết quả khi chạy:**

```text
Sự cố: 18
Đủ tiêu chí: 6
Lịch 3 ca: 120
Lịch đầu: C01, C04, C07
```

Ba vị trí là ba lượt thực hiện khác nhau nên dùng hoán vị; nhân viên không được đưa ca chưa có dữ liệu vào danh sách xử lý.

### Tình huống 5 — Cấp 5: Chọn ban phản biện 3 nhóm từ 20 người có ràng buộc

**Từ vựng trong mục:** **Constrained combination** — tổ hợp có ràng buộc; **Cross-check** — kiểm tra chéo.

**Tình huống thực tế:** Ban chuyên môn có **20 hồ sơ U01–U20**, mỗi người thuộc một nhóm **A, B hoặc C** và có cờ `ready`. U06 và U15 chưa sẵn sàng. Ban cần chọn **đúng ba người ngang vai**, gồm **một người nhóm A, một người nhóm B và một người nhóm C**; không được chọn hai người cùng nhóm hay đếm ba người đó nhiều lần do đổi thứ tự. Người điều phối muốn biết số ứng viên đủ điều kiện từng nhóm và tổng số ban hợp lệ.

**Vì sao chọn cách này?** Trước tiên bỏ người `ready=False` vì chưa thể tham gia. Sau đó, **một ban hợp lệ** phải có tập tên nhóm đúng bằng `{A, B, C}`: điều này bắt buộc đủ ba nhóm, không có hai người cùng nhóm. `combinations(ready, 3)` liệt kê các nhóm ba người **không xét thứ tự** rồi kiểm tra điều kiện; chương trình còn đếm số người sẵn sàng của từng nhóm. Nếu chọn độc lập đúng **một người từ mỗi nhóm**, số cách là tích số lựa chọn của A, B và C, dùng để đối chiếu kết quả liệt kê. Chỉ dùng tổ hợp của tất cả người sẵn sàng sẽ tính cả ban có hai người nhóm A, nên sai yêu cầu.

**Quy trình:**
1. Tách 20 hồ sơ theo nhóm A/B/C và trạng thái sẵn sàng.
2. Liệt kê mọi tổ ba người **không thứ tự** và chỉ giữ đội đủ ba nhóm.
3. So số ban hợp lệ với số lựa chọn từ mỗi nhóm, xác minh không chứa ứng viên chưa sẵn sàng.

```python
from itertools import combinations
people = [{"id":"U01","team":"A","ready":True},{"id":"U02","team":"B","ready":True},{"id":"U03","team":"C","ready":True},{"id":"U04","team":"A","ready":True},{"id":"U05","team":"B","ready":True},{"id":"U06","team":"C","ready":False},{"id":"U07","team":"A","ready":True},{"id":"U08","team":"B","ready":True},{"id":"U09","team":"C","ready":True},{"id":"U10","team":"A","ready":True},{"id":"U11","team":"B","ready":True},{"id":"U12","team":"C","ready":True},{"id":"U13","team":"A","ready":True},{"id":"U14","team":"B","ready":True},{"id":"U15","team":"C","ready":False},{"id":"U16","team":"A","ready":True},{"id":"U17","team":"B","ready":True},{"id":"U18","team":"C","ready":True},{"id":"U19","team":"A","ready":True},{"id":"U20","team":"B","ready":True}]
ready = []
for person in people:
    if person["ready"]:
        ready.append(person)
valid = []
for team in combinations(ready, 3):
    team_names = set()
    for person in team:
        team_names.add(person["team"])
    if team_names == {"A", "B", "C"}:
        valid.append(team)
counts = {"A": 0, "B": 0, "C": 0}
for person in ready:
    counts[person["team"]] += 1
if len(people) != 20:
    raise ValueError("Cần đủ 20 hồ sơ ban đầu.")
if len(valid) != counts["A"] * counts["B"] * counts["C"]:
    raise ValueError("Số ban ba nhóm phải bằng số cách chọn một người mỗi nhóm.")
print("Hồ sơ:", len(people))
print("Sẵn sàng:", len(ready))
print("Người theo nhóm:", counts["A"], counts["B"], counts["C"])
print("Ban ba nhóm:", len(valid))
```

**Kết quả khi chạy:**

```text
Hồ sơ: 20
Sẵn sàng: 18
Người theo nhóm: 7 7 4
Ban ba nhóm: 196
```

Ở cấp này, không thể chỉ gọi `comb(20,3)`: hai điều kiện **sẵn sàng** và **mỗi nhóm đúng một người** quyết định số đội thực sự khả thi.

## 6. Sai lầm thường gặp

- Phân biệt bài toán **có thứ tự** (`perm`) với **không xét thứ tự** (`comb`).
- `itertools.permutations(items,2)` chỉ tạo các cặp có thứ tự, không phải sắp xếp toàn bộ ba phần tử; không truyền k để lấy toàn bộ.
- Cả `math.perm` và `math.comb` giả định các phần tử phân biệt và không chọn trùng một phần tử.
- `math.factorial` cần số nguyên không âm; `0! = 1`.
- `itertools` để **liệt kê** các phương án; `math` giúp **đếm** khi số phương án quá lớn không nên liệt kê.

## 7. Trắc nghiệm

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. When should permutations be used? | Khi nào dùng hoán vị/chỉnh hợp?**

A. When order matters | Khi thứ tự quan trọng

B. When order does not matter | Khi thứ tự không quan trọng

C. The product 1×2×…×n | Tích 1×2×…×n

D. The number of unordered k-subsets from n distinct items | Số nhóm k phần tử không xét thứ tự từ n phần tử khác nhau

**Đáp án: A**

**Giải thích:** Đổi thứ tự người được chọn tạo cách sắp khác.


**Q2. When should combinations be used? | Khi nào dùng tổ hợp?**

A. When order matters | Khi thứ tự quan trọng

B. When order does not matter | Khi thứ tự không quan trọng

C. The product 1×2×…×n | Tích 1×2×…×n

D. The number of unordered k-subsets from n distinct items | Số nhóm k phần tử không xét thứ tự từ n phần tử khác nhau

**Đáp án: B**

**Giải thích:** Nhóm không đổi khi thành viên đổi chỗ.


**Q3. What is factorial n!? | Giai thừa n! là gì?**

A. When order matters | Khi thứ tự quan trọng

B. When order does not matter | Khi thứ tự không quan trọng

C. The product 1×2×…×n | Tích 1×2×…×n

D. The number of unordered k-subsets from n distinct items | Số nhóm k phần tử không xét thứ tự từ n phần tử khác nhau

**Đáp án: C**

**Giải thích:** Giai thừa đếm cách sắp xếp n phần tử phân biệt.


**Q4. What is a binomial coefficient C(n,k)? | Hệ số nhị thức C(n,k) là gì?**

A. When order matters | Khi thứ tự quan trọng

B. When order does not matter | Khi thứ tự không quan trọng

C. The product 1×2×…×n | Tích 1×2×…×n

D. The number of unordered k-subsets from n distinct items | Số nhóm k phần tử không xét thứ tự từ n phần tử khác nhau

**Đáp án: D**

**Giải thích:** C(n,k) còn là hệ số trong khai triển (a+b)^n.


**Q5. Which function counts ordered selections? | Hàm nào đếm cách chọn có thứ tự?**

A. `math.perm(n, k)` | `math.perm(n, k)`

B. `math.comb(n, k)` | `math.comb(n, k)`

C. `math.factorial(n)` | `math.factorial(n)`

D. `itertools.permutations(items)` | `itertools.permutations(items)`

**Đáp án: A**

**Giải thích:** perm đếm cách chọn có thứ tự không lặp.


**Q6. Which function counts unordered selections? | Hàm nào đếm cách chọn không thứ tự?**

A. `math.perm(n, k)` | `math.perm(n, k)`

B. `math.comb(n, k)` | `math.comb(n, k)`

C. `math.factorial(n)` | `math.factorial(n)`

D. `itertools.permutations(items)` | `itertools.permutations(items)`

**Đáp án: B**

**Giải thích:** comb đếm các nhóm khác nhau, không xét sắp xếp.


**Q7. Which function calculates n!? | Hàm nào tính n!?**

A. `math.perm(n, k)` | `math.perm(n, k)`

B. `math.comb(n, k)` | `math.comb(n, k)`

C. `math.factorial(n)` | `math.factorial(n)`

D. `itertools.permutations(items)` | `itertools.permutations(items)`

**Đáp án: C**

**Giải thích:** factorial nhân các số nguyên từ một tới n.


**Q8. Which function lists all ordered arrangements? | Hàm nào liệt kê các cách sắp xếp có thứ tự?**

A. `math.perm(n, k)` | `math.perm(n, k)`

B. `math.comb(n, k)` | `math.comb(n, k)`

C. `math.factorial(n)` | `math.factorial(n)`

D. `itertools.permutations(items)` | `itertools.permutations(items)`

**Đáp án: D**

**Giải thích:** Không truyền r, permutations liệt kê toàn bộ thứ tự.


**Q9. What is the value of 0!? | 0! bằng bao nhiêu?**

A. 1 | 1

B. 6 | 6

C. 10 pairs | 10 cặp

D. 12 pairs | 12 cặp

**Đáp án: A**

**Giải thích:** Dãy rỗng có một cách sắp xếp.


**Q10. How many full orderings of three distinct items exist? | Ba phần tử phân biệt có bao nhiêu thứ tự đầy đủ?**

A. 1 | 1

B. 6 | 6

C. 10 pairs | 10 cặp

D. 12 pairs | 12 cặp

**Đáp án: B**

**Giải thích:** 3! = 3×2×1 = 6.


**Q11. How many unordered pairs can be chosen from five distinct items? | Chọn cặp không thứ tự từ năm phần tử có bao nhiêu cách?**

A. 1 | 1

B. 6 | 6

C. 10 pairs | 10 cặp

D. 12 pairs | 12 cặp

**Đáp án: C**

**Giải thích:** Chọn hai từ năm không xét thứ tự có C(5,2)=10 cặp.


**Q12. How many ordered pairs can be formed from four distinct items without repetition? | Từ bốn phần tử phân biệt có bao nhiêu cặp có thứ tự không lặp?**

A. 1 | 1

B. 6 | 6

C. 10 pairs | 10 cặp

D. 12 pairs | 12 cặp

**Đáp án: D**

**Giải thích:** 4×3 = 12.


**Q13. What identity relates combinations and permutations? | Công thức nào liên hệ tổ hợp và chỉnh hợp?**

A. P(n,k)=C(n,k)×k! | P(n,k)=C(n,k)×k!

B. 1 | 1

C. n | n

D. Each inner entry sums two entries directly above | Mỗi ô bên trong bằng tổng hai ô ngay phía trên

**Đáp án: A**

**Giải thích:** Mỗi nhóm k người có k! cách sắp.


**Q14. What is C(n,0)? | C(n,0) bằng gì?**

A. P(n,k)=C(n,k)×k! | P(n,k)=C(n,k)×k!

B. 1 | 1

C. n | n

D. Each inner entry sums two entries directly above | Mỗi ô bên trong bằng tổng hai ô ngay phía trên

**Đáp án: B**

**Giải thích:** Có một cách chọn tập rỗng.


**Q15. What is C(n,n−1)? | C(n,n−1) bằng gì?**

A. P(n,k)=C(n,k)×k! | P(n,k)=C(n,k)×k!

B. 1 | 1

C. n | n

D. Each inner entry sums two entries directly above | Mỗi ô bên trong bằng tổng hai ô ngay phía trên

**Đáp án: C**

**Giải thích:** Chọn n−1 từ n tương đương chọn một phần tử bỏ lại nên có n cách.


**Q16. How are entries in Pascal's triangle obtained? | Các ô trong tam giác Pascal được tạo ra sao?**

A. P(n,k)=C(n,k)×k! | P(n,k)=C(n,k)×k!

B. 1 | 1

C. n | n

D. Each inner entry sums two entries directly above | Mỗi ô bên trong bằng tổng hai ô ngay phía trên

**Đáp án: D**

**Giải thích:** Hệ thức Pascal cộng hai hệ số ở hàng trước.


**Q17. What does `itertools.combinations(items,2)` list? | `itertools.combinations(items,2)` liệt kê gì?**

A. Unordered two-item groups | Nhóm hai phần tử không xét thứ tự

B. Ordered two-item arrangements | Cặp hai phần tử có thứ tự

C. It returns zero | Hàm trả về 0

D. The number grows factorially | Số cách tăng theo giai thừa

**Đáp án: A**

**Giải thích:** Hàm tạo mỗi cặp khác nhau đúng một lần.


**Q18. What does `itertools.permutations(items,2)` list? | `itertools.permutations(items,2)` liệt kê gì?**

A. Unordered two-item groups | Nhóm hai phần tử không xét thứ tự

B. Ordered two-item arrangements | Cặp hai phần tử có thứ tự

C. It returns zero | Hàm trả về 0

D. The number grows factorially | Số cách tăng theo giai thừa

**Đáp án: B**

**Giải thích:** Đổi thứ tự hai phần tử tạo kết quả khác.


**Q19. What happens if k>n in `math.comb(n,k)` for nonnegative integers? | Nếu k>n trong math.comb với số nguyên không âm thì sao?**

A. Unordered two-item groups | Nhóm hai phần tử không xét thứ tự

B. Ordered two-item arrangements | Cặp hai phần tử có thứ tự

C. It returns zero | Hàm trả về 0

D. The number grows factorially | Số cách tăng theo giai thừa

**Đáp án: C**

**Giải thích:** Không thể chọn k phần tử nếu tổng phần tử ít hơn k.


**Q20. Why avoid materializing all permutations for large n? | Vì sao tránh liệt kê toàn bộ hoán vị khi n lớn?**

A. Unordered two-item groups | Nhóm hai phần tử không xét thứ tự

B. Ordered two-item arrangements | Cặp hai phần tử có thứ tự

C. It returns zero | Hàm trả về 0

D. The number grows factorially | Số cách tăng theo giai thừa

**Đáp án: D**

**Giải thích:** n! tăng nhanh khiến không thể lưu hoặc in hết.

## 8. Nối sang bài tiếp

`Nguyên lý đếm → hoán vị/tổ hợp → phân phối nhị thức`.

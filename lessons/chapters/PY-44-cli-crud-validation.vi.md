# PY-44 — Ứng dụng CLI: CRUD, kiểm tra dữ liệu và thống kê hồ sơ


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **CRUD** — tạo/đọc/sửa/xóa; **Validation** — xác minh dữ liệu.

`Dictionary/Function → CRUD → CLI → File/CSV → Data App`

**Học xong dùng để làm gì?** Tạo công cụ thêm/đọc/sửa/xóa dữ liệu từ terminal, từ chối đầu vào sai và báo lỗi rõ ràng.

**Kết nối kiến thức tiếp theo:** PY-45 trực quan hóa dữ liệu đầu vào và kết quả để người dùng kiểm tra.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Ý nghĩa |
|---|---|---|
| CRUD | tạo/đọc/sửa/xóa | Bốn thao tác quản lý bản ghi |
| Validation | xác minh dữ liệu | Đảm bảo giá trị đúng giới hạn |
| Lookup | tra cứu | Tìm bản ghi qua khóa |
| Aggregate | tổng hợp | Tính chỉ số từ nhiều hồ sơ |

## 3. Hàm và cách sử dụng

**Từ vựng trong mục:** **Function** — hàm; **Option** — tùy chọn.

| Cú pháp | Mục đích và lựa chọn |
|---|---|
| `dict.get(id)` | Đọc bản ghi và trả mặc định nếu thiếu |
| `dict[id] = record` | Thêm/sửa bản ghi khi đã kiểm tra khóa |
| `dict.pop(id,default)` | Xóa có xử lý mã chưa tồn tại |
| `sum()/max()/min()/sorted()` | Tính thống kê và sắp xếp hồ sơ |

## 4. Khái niệm chính và liên quan

**Mạch kiến thức:** Một CLI nhận yêu cầu người dùng để tạo, đọc, sửa, xóa hồ sơ. Các thao tác CRUD cần Validation trước khi ghi, Lookup để tìm đúng mã và Aggregate để tạo báo cáo. Ví dụ xuyên suốt dùng mã sinh viên làm khóa và điểm trên thang 10 làm trường số.

### 4.1. CRUD — Bốn thao tác trên hồ sơ

**Từ vựng trong mục:** **CRUD — Create/Read/Update/Delete**.

Ứng dụng quản lý sinh viên cần tạo, đọc, sửa và xóa hồ sơ. Với Dictionary, **khóa là mã sinh viên duy nhất**, giá trị là Dictionary trường `name`, `score`. `Create` cần kiểm trùng mã; `Read` tra cứu; `Update` chỉ sửa mã tồn tại; `Delete` xử lý trường hợp mã không tìm thấy. Một CLI dùng lệnh nhập văn bản để thực hiện các thao tác này; đây mới là dữ liệu trong RAM, chưa được lưu bền xuống tệp.

**No Note — Không chú thích**

```python
db = {}
db['S1'] = {'name': 'An', 'score': 8}
print(db['S1']['score'])
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Minh họa tạo rồi đọc một hồ sơ trong database giả lập dạng dictionary.
# Dữ liệu: Hồ sơ S1 có name=An và score=8; dữ liệu chỉ tồn tại trong bộ nhớ Python.
# {} tạo dictionary rỗng làm database IN-MEMORY; không có file hay SQL.
db = {}
# CREATE: gán key 'S1' cho dictionary con chứa tên và điểm; cùng key gán lần nữa sẽ ghi đè.
db['S1'] = {'name': 'An', 'score': 8}
# READ: tra lần lượt mã S1 và trường score qua hai cặp dấu []; thiếu key sẽ gây KeyError.
print(db['S1']['score'])
```

**Kết quả khi chạy:**

```text
8
```

Bản ghi S1 được tạo trong RAM; lấy `score` của S1 cho kết quả 8/10.

### 4.2. Validation — Chặn dữ liệu sai trước khi ghi

**Từ vựng trong mục:** **Validation — kiểm tra hợp lệ**.

Validation phải dựa trên **quy tắc dữ liệu**, ví dụ điểm là số nằm trong `[0,10]`, mã không rỗng, mã sinh viên chưa tồn tại khi thêm mới. Nếu chỉ thử `0 <= score <= 10`, một chuỗi nhập từ CLI phải được đổi sang số có xử lý lỗi trước; không so chuỗi với số. Kiểm tra ràng buộc **trước** khi ghi để tránh ghi sai rồi mới phát hiện.

**No Note — Không chú thích**

```python
score = 8
print(isinstance(score, (int, float)) and 0 <= score <= 10)
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Kiểm loại dữ liệu và giới hạn điểm số trước khi chấp nhận.
# Dữ liệu: Điểm ví dụ 8 phải là int/float và nằm trong đoạn [0,10].
# Đầu vào một điểm số nguyên minh họa.
score = 8
# isinstance(x,(int,float)) True nếu x thuộc một trong hai kiểu số; tuple trong ngoặc là các kiểu được chấp nhận.
# Phép so sánh chuỗi đòi score từ 0 đến 10, bao gồm hai đầu mút; and yêu cầu cả kiểm kiểu và khoảng đúng.
print(isinstance(score, (int, float)) and 0 <= score <= 10)
```

**Kết quả khi chạy:**

```text
True
```

Điểm 8 là kiểu số và nằm trong thang điểm 0 đến 10.

### 4.3. Lookup — Tìm bản ghi theo mã

**Từ vựng trong mục:** **Lookup — tra cứu theo khóa**.

Với Dictionary `db`, `db.get('S1')` trả hồ sơ S1 nếu tồn tại, còn `db.get('S3')` trả `None` theo mặc định. Lệnh `db['S3']` sẽ ném `KeyError` khi thiếu mã. Trong CLI, việc không có hồ sơ cần được phản hồi rõ, không đánh đồng với một hồ sơ thật có điểm 0. Nếu cần thông báo thay vì `None`, truyền đối số mặc định cho `get`.

**No Note — Không chú thích**

```python
db = {'S1': {'score': 8}}
print(db.get('S3', 'Not found'))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tra một mã hồ sơ không tồn tại mà không gây KeyError.
# Dữ liệu: Database chỉ có S1, nhưng cần đọc mã S3.
# Dictionary lưu khóa S1 có điểm 8.
db = {'S1': {'score': 8}}
# get(key,default) trả giá trị dự phòng 'Not found' nếu không có S3, thay vì ném KeyError như db['S3'].
print(db.get('S3', 'Not found'))
```

**Kết quả khi chạy:**

```text
Not found
```

Mã S3 không có trong Dictionary nên in thông báo thay vì gây KeyError.

### 4.4. Aggregate — Tóm tắt nhiều bản ghi

**Từ vựng trong mục:** **Aggregate — tổng hợp**.

Tổng hợp biến nhiều hồ sơ thành một con số hay báo cáo: ví dụ mean của ba điểm `[7,8,9]` bằng 8 và điểm cao nhất bằng 9. Trước khi tính cần lấy giá trị số từ trường `score`, không phải mã ID. Với danh sách rỗng, phép `sum(scores)/len(scores)` sẽ chia cho 0; chương trình phải xử lý trường hợp không có hồ sơ.

**No Note — Không chú thích**

```python
scores = [7, 8, 9]
print(sum(scores) / len(scores), max(scores))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tạo báo cáo điểm trung bình và điểm cao nhất từ ba hồ sơ.
# Dữ liệu: Ba điểm 7,8,9 trên thang 0–10, mỗi số là một người.
# List điểm của ba người, không có thông tin ID.
scores = [7, 8, 9]
# sum() cộng tổng điểm, len() đếm số người, phép chia cho mean; cần list không rỗng để tránh chia 0.
# max() trả điểm cao nhất, khác với tổng/mean và sẽ lỗi trên list rỗng.
print(sum(scores) / len(scores), max(scores))
```

**Kết quả khi chạy:**

```text
8.0 9
```

Điểm trung bình bằng 8/10, điểm cao nhất bằng 9/10 trên ba hồ sơ.

## 5. Năm tình huống CLI/CRUD — từ kiểm mã đến 20 lệnh có audit

### Tình huống 1 — Cấp 1: Tạo hồ sơ từ 10 yêu cầu, từ chối ID trùng

**Từ vựng trong mục:** **Create** — tạo hồ sơ; **Unique key** — khóa duy nhất.

**Tình huống thực tế:** Phòng đào tạo nhận **10 yêu cầu tạo hồ sơ học viên**, mỗi yêu cầu ghi **mã S01…S09**, tên và điểm kiểm tra **trên thang 10**. Yêu cầu thứ 10 dùng lại **mã S03** với tên khác. Giáo vụ muốn tạo đúng **9 hồ sơ hợp lệ**, giữ nguyên điểm đã lưu của S03 và báo mã bị từ chối, không để người nhập sau vô tình ghi đè hồ sơ trước.

**Vì sao chọn cách này?** **CRUD** là bốn thao tác cơ bản với dữ liệu: **Create** (tạo), **Read** (đọc), **Update** (sửa), **Delete** (xóa). Bài đầu chỉ thực hiện **Create** trong `dictionary`: khóa là **mã học viên duy nhất**, giá trị là tên và điểm của người đó. Trước khi thêm, `if row['id'] in db` kiểm mã đã tồn tại hay chưa; nếu trùng thì ghi mã vào `rejected` và dùng `continue` bỏ riêng lượt này. Nếu cứ gán thẳng `db[id] = ...`, hồ sơ S03 ban đầu sẽ bị ghi đè không cảnh báo. Sau 10 yêu cầu, chương trình đối chiếu số hồ sơ và điểm S03, chứ không tự tính yêu cầu bị từ chối là một người mới.

**Quy trình:**
1. Tạo 10 yêu cầu có một mã lặp và điểm hợp lệ.
2. Kiểm mã tồn tại trước mỗi lệnh ADD rồi lưu hồ sơ.
3. Đếm kết quả, xác nhận điểm S03 gốc không bị thay.

**No Note — Không chú thích**

```python
requests = [{"id":"S01","name":"Student01","score":5},{"id":"S02","name":"Student02","score":6},{"id":"S03","name":"Student03","score":7},{"id":"S04","name":"Student04","score":8},{"id":"S05","name":"Student05","score":9},{"id":"S06","name":"Student06","score":10},{"id":"S07","name":"Student07","score":5},{"id":"S08","name":"Student08","score":6},{"id":"S09","name":"Student09","score":7},{"id":"S03","name":"Student10","score":8}]
db = {}
rejected = []
for row in requests:
    if row["id"] in db:
        rejected.append(row["id"])
        continue
    db[row["id"]] = {"name":row["name"],"score":row["score"]}
if len(requests) != 10:
    raise ValueError("Cần đủ 10 yêu cầu tạo hồ sơ.")
print("Yêu cầu:", len(requests))
print("Đã tạo:", len(db))
print("Trùng mã:", ", ".join(rejected))
print("Điểm S03:", db["S03"]["score"])
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Xử lý 10 yêu cầu CREATE, từ chối mã S03 bị trùng mà không ghi đè hồ sơ đã có.
# Dữ liệu: 10 yêu cầu thêm hồ sơ, ID S03 xuất hiện hai lần với điểm khác nhau; database chỉ giữ lần tạo đầu.
# Mười dict yêu cầu có id/name/score; số yêu cầu khác số hồ sơ hợp lệ vì mã có thể trùng.
requests = [{"id":"S01","name":"Student01","score":5},{"id":"S02","name":"Student02","score":6},{"id":"S03","name":"Student03","score":7},{"id":"S04","name":"Student04","score":8},{"id":"S05","name":"Student05","score":9},{"id":"S06","name":"Student06","score":10},{"id":"S07","name":"Student07","score":5},{"id":"S08","name":"Student08","score":6},{"id":"S09","name":"Student09","score":7},{"id":"S03","name":"Student10","score":8}]
# Dictionary lưu hồ sơ theo ID duy nhất; tránh ghi đè yêu cầu trước.
db = {}
# List mã bị từ chối để xuất báo cáo.
rejected = []
# Duyệt từng yêu cầu thêm mới theo thứ tự xuất hiện.
for row in requests:
    # in kiểm ID đã là khóa trong db; nếu có thì bị trùng, không được tạo lại.
    if row["id"] in db:
        # append() ghi mã trùng vào list từ chối.
        rejected.append(row["id"])
        # continue bỏ phần còn lại của vòng hiện tại, bảo vệ hồ sơ gốc khỏi ghi đè.
        continue
    # CREATE hợp lệ: ghi dictionary con name/score theo ID chưa có.
    db[row["id"]] = {"name":row["name"],"score":row["score"]}
# Đòi đúng 10 yêu cầu nguồn; đếm cả yêu cầu bị từ chối.
if len(requests) != 10:
    # ValueError báo đầu vào không đúng số lượng, tránh công bố kết quả thiếu.
    raise ValueError("Cần đủ 10 yêu cầu tạo hồ sơ.")
print("Yêu cầu:", len(requests))
# len() đếm hồ sơ được tạo với mã duy nhất, không phải 10 yêu cầu.
print("Đã tạo:", len(db))
# join() ghép mã trùng trong list bằng dấu phẩy và khoảng trắng.
print("Trùng mã:", ", ".join(rejected))
# Tra điểm S03 sau xử lý để xác nhận điểm lần tạo đầu vẫn còn, không bị cập nhật bởi yêu cầu trùng.
print("Điểm S03:", db["S03"]["score"])
```

**Kết quả khi chạy:**

```text
Yêu cầu: 10
Đã tạo: 9
Trùng mã: S03
Điểm S03: 7
```

9 hồ sơ cuối là **9 mã khác nhau**; dòng nhập trùng phải được báo lại cho người dùng thay vì tự sửa hồ sơ cũ.

### Tình huống 2 — Cấp 2: Tra cứu 12 mã và phân biệt ID vắng với điểm 0

**Từ vựng trong mục:** **Read** — đọc hồ sơ; **Lookup** — tra theo khóa; **Missing key** — mã không có.

**Tình huống thực tế:** Phòng học đang lưu **10 học viên S01–S10 trong bộ nhớ RAM**; mỗi người có mã và điểm, riêng **S01 có điểm 0 hợp lệ**. Nhân viên gửi **12 lượt yêu cầu đọc hồ sơ**, gồm cả 10 mã có thật và hai mã lạ **S99, S88**. Họ cần đếm bao nhiêu lượt tìm thấy và bao nhiêu lượt không thấy, nhưng không được coi học viên đạt 0 điểm là người chưa có hồ sơ.

**Vì sao chọn cách này?** **Read** là tra thông tin mà **không sửa** dữ liệu. `db.get(sid)` trả bản ghi cho mã có trong dictionary và trả `None` khi mã **không tồn tại**. Cần kiểm `record is None` chứ không kiểm giá trị điểm bằng `if not score`: trong Python số **0 được xem là False** khi dùng như điều kiện, nhưng ở đây **0 điểm vẫn là một điểm hợp lệ**. Chương trình duyệt đủ 12 yêu cầu rồi đưa mã vào nhóm tìm thấy hoặc nhóm thiếu, bảo đảm đọc S01 không bị nhầm với S99/S88. Đây là dữ liệu trong RAM, chưa có file hay máy chủ cơ sở dữ liệu.

**Quy trình:**
1. Tạo 10 hồ sơ với mã khác nhau và 12 lượt tra ID.
2. Dùng `get` nhận hồ sơ hoặc None, đếm lượt tìm thấy/thất bại.
3. Kiểm riêng điểm 0 của S01 vẫn được trả về đúng.

**No Note — Không chú thích**

```python
db = {}
for i in range(1, 11):
    db[f"S{i:02d}"] = {"score": i - 1}
requests = ["S01","S02","S03","S04","S05","S06","S07","S08","S09","S10","S99","S88"]
found, missing = [], []
for sid in requests:
    record = db.get(sid)
    if record is None:
        missing.append(sid)
    else:
        found.append(sid)
if len(requests) != 12:
    raise ValueError("Cần đủ 12 yêu cầu tra cứu.")
print("Lượt tra cứu:", len(requests))
print("Tìm thấy:", len(found))
print("Không thấy:", ", ".join(missing))
print("S01 có điểm 0:", db["S01"]["score"] == 0)
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Đọc 12 yêu cầu GET trên cơ sở mười hồ sơ, phân biệt điểm 0 với không tìm thấy.
# Dữ liệu: Có hồ sơ S01..S10 (S01 có score=0) và hai yêu cầu S99/S88 không tồn tại.
# Database in-memory lưu điểm theo mã hồ sơ.
db = {}
# Tạo 10 mã S01..S10, cận trên 11 không được lấy.
for i in range(1, 11):
    # f-string :02d định dạng mã hồ sơ có hai chữ số.
    # S01 có score=0, giá trị 0 vẫn là dữ liệu hợp lệ chứ không phải chưa tìm thấy.
    db[f"S{i:02d}"] = {"score": i - 1}
# List 12 mã cần tra; gồm hai mã không tồn tại.
requests = ["S01","S02","S03","S04","S05","S06","S07","S08","S09","S10","S99","S88"]
# Hai list phân biệt mã tìm được và mã không có.
found, missing = [], []
# Duyệt từng yêu cầu tra cứu.
for sid in requests:
    # get() trả dict hồ sơ nếu có, hoặc None khi không có khóa; không phát sinh KeyError.
    record = db.get(sid)
    # is None kiểm ĐÚNG dấu hiệu không tìm thấy, không kiểm `if not record` hay `if not score` vì điểm 0 hợp lệ.
    if record is None:
        # Ghi mã không tồn tại để thông báo.
        missing.append(sid)
    else:
        # Ghi mã tìm được mà không sửa hồ sơ.
        found.append(sid)
# Kiểm có đủ 12 lượt GET.
if len(requests) != 12:
    # Dừng nếu số yêu cầu nguồn sai.
    raise ValueError("Cần đủ 12 yêu cầu tra cứu.")
print("Lượt tra cứu:", len(requests))
# Đếm các yêu cầu tra tìm được.
print("Tìm thấy:", len(found))
# Nối các mã không tìm thấy thành dòng thông báo.
print("Không thấy:", ", ".join(missing))
# So điểm thực lưu với số 0 để xác nhận GET không nhầm điểm 0 thành missing.
print("S01 có điểm 0:", db["S01"]["score"] == 0)
```

**Kết quả khi chạy:**

```text
Lượt tra cứu: 12
Tìm thấy: 10
Không thấy: S99, S88
S01 có điểm 0: True
```

Không tìm thấy mã là **vấn đề khóa**, khác với việc tìm thấy mã nhưng giá trị điểm bằng 0.

### Tình huống 3 — Cấp 3: Kiểm dữ liệu trước khi sửa điểm qua 15 yêu cầu

**Từ vựng trong mục:** **Update** — sửa hồ sơ; **Validation** — kiểm dữ liệu; **Finite number** — số hữu hạn.

**Tình huống thực tế:** Trung tâm có **10 hồ sơ điểm S01–S10** và tiếp nhận **15 yêu cầu sửa điểm**, mỗi yêu cầu gồm mã và điểm nhập dưới dạng **chuỗi văn bản**. Mười yêu cầu đầu nhập điểm trong khoảng **0–10**; năm yêu cầu còn lại có điểm âm, điểm 11, chữ `bad`, chữ `nan` hoặc mã **S99** không tồn tại. Giáo vụ cần cập nhật đúng dữ liệu hợp lệ và ghi số yêu cầu bị từ chối mà không sinh thêm người học ngoài danh sách.

**Vì sao chọn cách này?** **Update** là thay giá trị của **mã đã tồn tại**, nên phải kiểm `sid in db` trước khi lưu. Vì CLI nhận đầu vào dạng chữ, `float(raw_score)` được gọi bên trong `try` để chuyển các chuỗi số thành điểm; `except ValueError` xử lý chuỗi như `bad` mà không làm dừng toàn bộ 15 lượt. Nhưng `float('nan')` vẫn chuyển được thành **số dấu phẩy động đặc biệt**, nên cần `math.isfinite` để loại **NaN hoặc vô cực**, cùng quy tắc điểm phải từ 0 đến 10. Khi một yêu cầu sai, chương trình tăng `rejected` và **giữ nguyên điểm cũ**. Chỉ 10 yêu cầu hợp lệ được ghi, không tự thêm S99.

**Quy trình:**
1. Tạo 10 mã ban đầu và 15 yêu cầu chứa điểm ở dạng chuỗi.
2. Kiểm mã có sẵn, thử đổi điểm, chặn số ngoài thang và NaN.
3. Đếm cập nhật/thất bại, đối chiếu số hồ sơ và điểm mới S03.

**No Note — Không chú thích**

```python
import math
db = {}
for i in range(1, 11):
    db[f"S{i:02d}"] = {"score": 5.0}
updates = [["S01","6.5"],["S02","7.5"],["S03","8.5"],["S04","9.5"],["S05","6.5"],["S06","6.5"],["S07","7.5"],["S08","8.5"],["S09","9.5"],["S10","6.5"],["S03","-1"],["S02","11"],["S04","bad"],["S05","nan"],["S99","7.5"]]
accepted, rejected = 0, 0
for sid, raw_score in updates:
    if sid not in db:
        rejected += 1
        continue
    try:
        score = float(raw_score)
    except ValueError:
        rejected += 1
        continue
    if not math.isfinite(score) or not (0 <= score <= 10):
        rejected += 1
        continue
    db[sid]["score"] = score
    accepted += 1
if len(updates) != 15:
    raise ValueError("Cần đủ 15 yêu cầu cập nhật.")
print("Yêu cầu:", len(updates))
print("Cập nhật:", accepted)
print("Từ chối:", rejected)
print("Hồ sơ còn:", len(db))
print("Điểm S03:", db["S03"]["score"])
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Xử lý 15 yêu cầu UPDATE, loại mã lạ, chuỗi không đổi được sang số, NaN và điểm ngoài 0–10.
# Dữ liệu: Có 10 hồ sơ S01..S10; 15 yêu cầu cập nhật điểm dạng chuỗi có các trường hợp -1,11,bad,nan,S99.
# Thư viện chuẩn math cho isfinite() để loại NaN và số vô cực.
import math
# Lưu mười hồ sơ đã tồn tại trước khi UPDATE.
db = {}
# Tạo 10 mã duy nhất S01..S10.
for i in range(1, 11):
    # Mã có hai chữ số bằng f-string :02d.
    db[f"S{i:02d}"] = {"score": 5.0}
# 15 cặp (ID, chuỗi điểm), gồm cả yêu cầu hợp lệ và không hợp lệ.
updates = [["S01","6.5"],["S02","7.5"],["S03","8.5"],["S04","9.5"],["S05","6.5"],["S06","6.5"],["S07","7.5"],["S08","8.5"],["S09","9.5"],["S10","6.5"],["S03","-1"],["S02","11"],["S04","bad"],["S05","nan"],["S99","7.5"]]
# Hai bộ đếm phân biệt cập nhật thành công và từ chối.
accepted, rejected = 0, 0
# Unpack một yêu cầu thành ID và chuỗi điểm thô.
for sid, raw_score in updates:
    # Không có hồ sơ đích thì không được tạo mới bằng UPDATE.
    if sid not in db:
        # Tăng số yêu cầu thất bại, kể cả sai mã hoặc giá trị.
        rejected += 1
        # Bỏ qua yêu cầu hiện tại sau khi bị từ chối, không chỉnh DB.
        continue
    # Thử chuyển chuỗi thành số; cú pháp try/except chỉ bắt lỗi mà nhánh except khai báo.
    try:
        # Chuyển chuỗi như '6.5' sang float; 'bad' ném ValueError nhưng 'nan' tạo NaN hợp lệ về cú pháp.
        score = float(raw_score)
    # Bắt lỗi chuyển chuỗi không hợp lệ để từ chối thay vì dừng toàn chương trình.
    except ValueError:
        # Tăng số yêu cầu thất bại, kể cả sai mã hoặc giá trị.
        rejected += 1
        # Bỏ qua yêu cầu hiện tại sau khi bị từ chối, không chỉnh DB.
        continue
    # isfinite() kiểm số hữu hạn, loại NaN/+inf/-inf vốn có thể vượt qua bước float().
    # Giới hạn điểm trong khoảng đóng [0,10]; and/ not kết hợp cả kiểm hữu hạn và khoảng.
    if not math.isfinite(score) or not (0 <= score <= 10):
        # Tăng số yêu cầu thất bại, kể cả sai mã hoặc giá trị.
        rejected += 1
        # Bỏ qua yêu cầu hiện tại sau khi bị từ chối, không chỉnh DB.
        continue
    # UPDATE đúng mã/điểm: chỉ sửa trường score của hồ sơ hiện có.
    db[sid]["score"] = score
    # Tăng số lần cập nhật thành công, không phải số người khác nhau.
    accepted += 1
# Kiểm đủ 15 yêu cầu, không bỏ những yêu cầu bị từ chối.
if len(updates) != 15:
    # Dừng khi dữ liệu số yêu cầu không đúng.
    raise ValueError("Cần đủ 15 yêu cầu cập nhật.")
print("Yêu cầu:", len(updates))
print("Cập nhật:", accepted)
print("Từ chối:", rejected)
# Số hồ sơ sau UPDATE vẫn là 10, vì UPDATE không tạo/xóa hồ sơ.
print("Hồ sơ còn:", len(db))
# Tra S03 sau các yêu cầu để kiểm trạng thái điểm cuối đã được cập nhật hợp lệ.
print("Điểm S03:", db["S03"]["score"])
```

**Kết quả khi chạy:**

```text
Yêu cầu: 15
Cập nhật: 10
Từ chối: 5
Hồ sơ còn: 10
Điểm S03: 8.5
```

NaN phải bị chặn **trước khi ghi**; nếu để NaN trong dữ liệu, tổng hợp điểm và so sánh ngưỡng về sau có thể bị sai.

### Tình huống 4 — Cấp 4: Xóa an toàn từ 18 lệnh với mã lặp và mã lạ

**Từ vựng trong mục:** **Delete** — xóa; **Idempotence** — gọi lại không làm sai dữ liệu; **Audit** — đối soát.

**Tình huống thực tế:** Ứng dụng quản lý có **10 hồ sơ S01–S10** và nhận **18 lệnh xóa** theo thứ tự. Mười lệnh đầu gọi đúng mười mã, nhưng tám lệnh sau có mã **đã bị xóa** hoặc **chưa từng tồn tại**. Nhân viên cần biết có bao nhiêu hồ sơ thực sự đã mất, bao nhiêu lệnh không làm thay đổi dữ liệu và xác nhận cuối cùng không còn hồ sơ nào.

**Vì sao chọn cách này?** **Delete** là xóa một bản ghi khi **mã đang tồn tại**. `db.pop(sid, None)` vừa lấy vừa xóa khi thấy mã, còn nếu mã vắng thì trả `None` thay vì báo `KeyError` làm gián đoạn vòng lặp. Chương trình kiểm giá trị trả về để tách **xóa thành công** và **mã không còn trong DB**. Sau khi mười hồ sơ đầu đã xóa, gọi xóa lại S01 không thể được tính là thành công lần nữa, vì dữ liệu không thay đổi. Tổng số thành công và thất bại phải bằng **18 lệnh**, còn `len(db)` xác nhận danh sách cuối đã rỗng.

**Quy trình:**
1. Tạo 10 ID trong Dictionary và 18 mã được yêu cầu xóa.
2. Dùng `pop(..., None)`, đếm thành công khi trả hồ sơ thật.
3. Báo số lệnh lỗi/không thay đổi và số hồ sơ còn lại.

**No Note — Không chú thích**

```python
db = {}
for i in range(1, 11):
    db[f"S{i:02d}"] = {"score": i}
requests = ["S01","S02","S03","S04","S05","S06","S07","S08","S09","S10","S01","S02","S03","S99","S98","S97","S05","S100"]
deleted, missing = 0, 0
for sid in requests:
    value = db.pop(sid, None)
    if value is None:
        missing += 1
    else:
        deleted += 1
if len(requests) != 18:
    raise ValueError("Cần đủ 18 yêu cầu xóa.")
print("Lệnh xóa:", len(requests))
print("Xóa thật:", deleted)
print("Mã không còn:", missing)
print("Hồ sơ còn:", len(db))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Xử lý 18 yêu cầu DELETE có mã trùng và mã lạ, bảo đảm xóa một lần mỗi hồ sơ.
# Dữ liệu: Bắt đầu 10 hồ sơ S01..S10; 18 lượt DELETE gồm mã lặp lại, S99/S98/S97/S100 không tồn tại.
# Database in-memory ban đầu rỗng.
db = {}
# Tạo 10 mã có số thứ tự 1..10.
for i in range(1, 11):
    # f-string :02d thêm số 0 ở đầu mã S01..S10.
    # Điểm ban đầu của một hồ sơ để có dữ liệu kiểm xóa.
    db[f"S{i:02d}"] = {"score": i}
# 18 lệnh xóa, gồm cả mã trùng và mã không tồn tại.
requests = ["S01","S02","S03","S04","S05","S06","S07","S08","S09","S10","S01","S02","S03","S99","S98","S97","S05","S100"]
# Hai bộ đếm lệnh xóa thật và lệnh không tìm thấy hồ sơ.
deleted, missing = 0, 0
# Lần lượt xử lý từng yêu cầu, trạng thái db thay đổi sau mỗi xóa.
for sid in requests:
    # pop(key,default) vừa lấy VỪA XÓA hồ sơ nếu tồn tại; nếu thiếu khóa trả None thay vì KeyError.
    value = db.pop(sid, None)
    # Chỉ khi pop trả None mới tính lệnh không tìm thấy; xóa cùng ID lần hai không xóa thêm.
    if value is None:
        # Đếm yêu cầu xóa vào ID không còn tồn tại.
        missing += 1
    else:
        # Đếm số hồ sơ thực sự xóa, không phải tổng yêu cầu.
        deleted += 1
# Xác minh đủ 18 lệnh nguồn.
if len(requests) != 18:
    # Dừng nếu thiếu lệnh.
    raise ValueError("Cần đủ 18 yêu cầu xóa.")
print("Lệnh xóa:", len(requests))
print("Xóa thật:", deleted)
print("Mã không còn:", missing)
# Đếm hồ sơ còn lại trong database sau xóa.
print("Hồ sơ còn:", len(db))
```

**Kết quả khi chạy:**

```text
Lệnh xóa: 18
Xóa thật: 10
Mã không còn: 8
Hồ sơ còn: 0
```

Xóa không tìm thấy được ghi nhận rõ trong **audit**; không được ngầm tạo lại hồ sơ trong quá trình xóa.

### Tình huống 5 — Cấp 5: Chạy 20 câu lệnh CLI CRUD có kiểm tra và báo cáo cuối

**Từ vựng trong mục:** **CLI command** — lệnh văn bản; **CRUD** — tạo/đọc/sửa/xóa; **Audit trail** — lịch sử thao tác.

**Tình huống thực tế:** Trung tâm đào tạo xây **CLI (chương trình nhận lệnh văn bản)** để quản lý điểm học viên. Có **20 lệnh theo thứ tự**, gồm `ADD` (thêm), `GET` (xem), `UPDATE` (sửa), `DELETE` (xóa) và `REPORT` (báo cáo). Trong đó có lệnh hợp lệ, thêm trùng mã, điểm không phải số, điểm vượt 10, tìm mã chưa có và xóa lần thứ hai. Nhóm muốn xử lý đủ 20 lệnh, đếm số thao tác thành công/thất bại và xem **số hồ sơ cùng điểm trung bình cuối** mà không làm hỏng cơ sở dữ liệu trong RAM.

**Vì sao chọn cách này?** **CLI** là giao diện để nhập lệnh bằng chữ thay vì bấm nút; ở ví dụ này **20 lệnh được chuẩn bị sẵn**, không yêu cầu người học gõ tương tác. `shlex.split` chia chữ thành các thành phần an toàn hơn cách chạy nội dung bằng `eval`; chương trình kiểm **tên lệnh và số đối số** trước khi làm. `parse_score` đổi điểm thành số và kiểm **hữu hạn, từ 0 đến 10**; thêm phải chưa có mã, sửa/xóa/tra phải có mã phù hợp. `audit` ghi các lượt thành công theo loại hoặc `REJECT` cho lệnh không đạt điều kiện; lệnh `REPORT` chỉ **đọc và tổng hợp**, không sửa hồ sơ. Vì các lệnh chạy **theo thứ tự**, xóa một mã ảnh hưởng lệnh tới sau, và điểm trung bình cuối chỉ được tính từ **những hồ sơ còn lại**.

**Quy trình:**
1. Lưu 20 dòng lệnh để chạy tự động, không cần người nhập bàn phím.
2. Phân tích từng lệnh theo tên và số đối số, kiểm khóa và giá trị điểm.
3. Đếm CREATE/UPDATE/DELETE/thất bại; tính số hồ sơ và mean cuối, xác nhận báo cáo không ghi dữ liệu.

**No Note — Không chú thích**

```python
import math
import shlex
commands = ["ADD S01 7","ADD S02 8","ADD S03 9","ADD S04 6","ADD S05 5","ADD S06 10","ADD S07 7","ADD S08 8","ADD S09 9","ADD S10 6","ADD S01 9","UPDATE S03 9.5","UPDATE S05 bad","GET S03","GET S99","DELETE S02","DELETE S02","ADD S11 11","UPDATE S08 8.5","REPORT"]
db = {}
audit = {"ADD":0,"UPDATE":0,"DELETE":0,"GET":0,"REPORT":0,"REJECT":0}
def parse_score(raw):
    try:
        value = float(raw)
    except ValueError:
        return None
    if math.isfinite(value) and 0 <= value <= 10:
        return value
    return None
for command in commands:
    parts = shlex.split(command)
    verb = parts[0]
    ok = False
    if verb == "ADD" and len(parts) == 3:
        sid, raw = parts[1:]
        score = parse_score(raw)
        if sid not in db and score is not None:
            db[sid] = score
            ok = True
    elif verb == "UPDATE" and len(parts) == 3:
        sid, raw = parts[1:]
        score = parse_score(raw)
        if sid in db and score is not None:
            db[sid] = score
            ok = True
    elif verb == "GET" and len(parts) == 2:
        ok = parts[1] in db
    elif verb == "DELETE" and len(parts) == 2:
        ok = db.pop(parts[1], None) is not None
    elif verb == "REPORT" and len(parts) == 1:
        ok = bool(db)
    if ok:
        audit[verb] += 1
    else:
        audit["REJECT"] += 1
if len(commands) != 20 or sum(audit.values()) != 20:
    raise ValueError("Cần đối chiếu đủ 20 lệnh CLI được xử lý.")
print("Lệnh:", len(commands))
print("Thêm/sửa/xóa:", audit["ADD"], audit["UPDATE"], audit["DELETE"])
print("Lệnh từ chối:", audit["REJECT"])
print("Hồ sơ cuối:", len(db))
print(f"Điểm TB cuối: {sum(db.values())/len(db):.2f}")
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Mô phỏng CLI CRUD với 20 lệnh ADD/UPDATE/GET/DELETE/REPORT, kiểm dữ liệu và thống kê audit.
# Dữ liệu: 20 chuỗi lệnh nhập sẵn; database là dictionary tạm, có lệnh trùng mã, điểm bad/11 và xóa hai lần.
# math.isfinite() xác nhận điểm số thật sự là số hữu hạn.
import math
# shlex.split() phân tích chuỗi lệnh theo cú pháp dấu nháy/khoảng trắng giống shell, KHÔNG thực thi shell.
import shlex
# 20 dòng lệnh mô phỏng đầu vào người dùng, không mở terminal tương tác thật.
commands = ["ADD S01 7","ADD S02 8","ADD S03 9","ADD S04 6","ADD S05 5","ADD S06 10","ADD S07 7","ADD S08 8","ADD S09 9","ADD S10 6","ADD S01 9","UPDATE S03 9.5","UPDATE S05 bad","GET S03","GET S99","DELETE S02","DELETE S02","ADD S11 11","UPDATE S08 8.5","REPORT"]
# Dictionary lưu ID→điểm trong RAM, không có SQL hoặc file.
db = {}
# Dictionary bộ đếm kết quả từng loại lệnh thành công và REJECT; tổng đếm phải bằng 20.
audit = {"ADD":0,"UPDATE":0,"DELETE":0,"GET":0,"REPORT":0,"REJECT":0}
# Hàm nhận chuỗi điểm và trả float hợp lệ hoặc None để gọi xử lý từ chối.
# Kiểm kiểu, tính hữu hạn và phạm vi điểm trước khi ghi.
def parse_score(raw):
    # Bắt đầu đoạn có thể lỗi khi ép chuỗi sang số.
    try:
        # float() chuyển chuỗi điểm, có thể sinh ValueError nếu 'bad'; 'nan' sẽ chuyển được nên cần isfinite().
        value = float(raw)
    # Bắt lỗi chuỗi không thể chuyển thành số.
    except ValueError:
        # None là dấu hiệu không hợp lệ; điểm 0 vẫn hợp lệ nên không dùng if not score.
        return None
    # isfinite() loại NaN, +inf/-inf; đồng thời yêu cầu điểm trong [0,10].
    # Chặn mọi điểm âm hoặc >10.
    if math.isfinite(value) and 0 <= value <= 10:
        # Trả float hợp lệ cho thao tác ADD/UPDATE.
        return value
    # None là dấu hiệu không hợp lệ; điểm 0 vẫn hợp lệ nên không dùng if not score.
    return None
# Duyệt từng lệnh đúng thứ tự, vì UPDATE/DELETE phụ thuộc trạng thái trước đó.
for command in commands:
    # Tách command thành list token, xử lý khoảng trắng và chuỗi có dấu nháy, không thực thi nội dung.
    parts = shlex.split(command)
    # [0] lấy động từ lệnh; với lệnh rỗng sẽ IndexError, nhưng dữ liệu mẫu không có lệnh rỗng.
    verb = parts[0]
    # Mặc định lệnh bị từ chối cho tới khi một nhánh thỏa điều kiện.
    ok = False
    # Lệnh ADD cần đúng ba token (ADD ID điểm), tránh thiếu/dư tham số.
    if verb == "ADD" and len(parts) == 3:
        # Slice [1:] bỏ động từ, lấy hai tham số mã và điểm.
        sid, raw = parts[1:]
        # Kiểm kiểu, tính hữu hạn và phạm vi điểm trước khi ghi.
        score = parse_score(raw)
        # CREATE chỉ khi ID chưa có và điểm hợp lệ; phân biệt None với score=0.
        if sid not in db and score is not None:
            # Lưu điểm theo ID khi ADD/UPDATE hợp lệ; thao tác UPDATE kiểm tồn tại trước.
            db[sid] = score
            ok = True
    # UPDATE cần đúng ba token, không tự tạo hồ sơ mới.
    elif verb == "UPDATE" and len(parts) == 3:
        # Slice [1:] bỏ động từ, lấy hai tham số mã và điểm.
        sid, raw = parts[1:]
        # Kiểm kiểu, tính hữu hạn và phạm vi điểm trước khi ghi.
        score = parse_score(raw)
        # UPDATE chỉ cho phép sửa ID đã tồn tại với điểm được validate.
        if sid in db and score is not None:
            # Lưu điểm theo ID khi ADD/UPDATE hợp lệ; thao tác UPDATE kiểm tồn tại trước.
            db[sid] = score
            ok = True
    # GET chỉ nhận một tham số ID; trạng thái thành công khi ID có trong db.
    elif verb == "GET" and len(parts) == 2:
        # Tra ID trong dict không thay đổi hồ sơ.
        ok = parts[1] in db
    # DELETE chỉ nhận ID, không cần điểm.
    elif verb == "DELETE" and len(parts) == 2:
        # pop() xóa và trả giá trị hoặc None; xóa lần hai bị REJECT, không tạo KeyError.
        ok = db.pop(parts[1], None) is not None
    # REPORT không có tham số, chỉ hợp lệ nếu db có ít nhất một hồ sơ.
    elif verb == "REPORT" and len(parts) == 1:
        # bool(dictionary) là True khi database không rỗng.
        ok = bool(db)
    # Lệnh hợp lệ đóng góp đúng một bộ đếm theo verb.
    if ok:
        # Tăng đếm loại lệnh thành công; các verb hợp lệ đều có key trong audit.
        audit[verb] += 1
    else:
        # Mọi lệnh thất bại đi vào bộ đếm chung REJECT.
        audit["REJECT"] += 1
# Kiểm đủ 20 dòng lệnh.
# values() lấy số đếm từng loại; sum() phải bằng tổng lệnh để không bỏ/trùng thống kê.
if len(commands) != 20 or sum(audit.values()) != 20:
    # Dừng khi số yêu cầu và tổng audit không khớp.
    raise ValueError("Cần đối chiếu đủ 20 lệnh CLI được xử lý.")
print("Lệnh:", len(commands))
print("Thêm/sửa/xóa:", audit["ADD"], audit["UPDATE"], audit["DELETE"])
print("Lệnh từ chối:", audit["REJECT"])
print("Hồ sơ cuối:", len(db))
# values() lấy điểm hồ sơ còn; sum()/len() tính điểm trung bình, cần db không rỗng (kịch bản bảo đảm).
# f-string :.2f chỉ định hiển thị điểm trung bình với hai chữ số sau dấu thập phân.
print(f"Điểm TB cuối: {sum(db.values())/len(db):.2f}")
```

**Kết quả khi chạy:**

```text
Lệnh: 20
Thêm/sửa/xóa: 10 2 1
Lệnh từ chối: 5
Hồ sơ cuối: 9
Điểm TB cuối: 7.56
```

Ứng dụng hiện chỉ lưu trạng thái **trong RAM**: khi tắt chương trình dữ liệu biến mất. Triển khai thật phải bổ sung lưu bền, phân quyền và kiểm thử xử lý lỗi.

## 6. Sai lầm thường gặp

- Thêm mã đã có bằng `dict[id]=...` sẽ ghi đè dữ liệu cũ nếu không kiểm trùng.
- Điểm từ CLI có thể là chuỗi; phải parse với xử lý ValueError trước khi so với số.
- `get()` khác `dict[key]` khi thiếu khóa; `pop` có default khác xóa trực tiếp.
- Update cần kiểm mã tồn tại và giới hạn điểm; xóa mã thiếu không được làm mất dữ liệu khác.
- Tính mean cần kiểm List không rỗng và chỉ tính trên trường số thực sự.
- Dictionary tồn tại trong RAM; chương trình thực tế cần lưu file/database và cân nhắc sao lưu/quyền truy cập.

## 7. Trắc nghiệm

**Q1. What are the four CRUD operations? | Bốn thao tác CRUD là gì?**

A. Create, Read, Update, Delete | Tạo, đọc, sửa, xóa

B. Checking constraints before processing or storing | Kiểm ràng buộc trước khi xử lý hoặc lưu

C. A field identifying the desired record | Trường xác định bản ghi cần tìm

D. Computing summaries from multiple records | Tính chỉ số tổng hợp từ nhiều bản ghi

**Đáp án: A**

**Giải thích:** CRUD mô tả vòng đời bản ghi, không phải một lệnh cơ sở dữ liệu. Nếu coi thêm mới như ghi đè mà không có chính sách, dữ liệu sinh viên cũ có thể bị mất.


**Q2. What is input validation? | Kiểm tra dữ liệu đầu vào là gì?**

A. Create, Read, Update, Delete | Tạo, đọc, sửa, xóa

B. Checking constraints before processing or storing | Kiểm ràng buộc trước khi xử lý hoặc lưu

C. A field identifying the desired record | Trường xác định bản ghi cần tìm

D. Computing summaries from multiple records | Tính chỉ số tổng hợp từ nhiều bản ghi

**Đáp án: B**

**Giải thích:** Validation chặn điểm sai hoặc mã trùng trước khi ghi. Validation kiểm cả kiểu dữ liệu và giới hạn nghiệp vụ, không chỉ kiểm code chạy được.


**Q3. What is a lookup key? | Khóa tra cứu là gì?**

A. Create, Read, Update, Delete | Tạo, đọc, sửa, xóa

B. Checking constraints before processing or storing | Kiểm ràng buộc trước khi xử lý hoặc lưu

C. A field identifying the desired record | Trường xác định bản ghi cần tìm

D. Computing summaries from multiple records | Tính chỉ số tổng hợp từ nhiều bản ghi

**Đáp án: C**

**Giải thích:** Mã sinh viên dùng làm khóa duy nhất, còn điểm là giá trị bản ghi. Nên dùng mã sinh viên duy nhất và ổn định làm khóa, không dùng điểm có thể thay đổi.


**Q4. What is aggregation? | Aggregate là gì?**

A. Create, Read, Update, Delete | Tạo, đọc, sửa, xóa

B. Checking constraints before processing or storing | Kiểm ràng buộc trước khi xử lý hoặc lưu

C. A field identifying the desired record | Trường xác định bản ghi cần tìm

D. Computing summaries from multiple records | Tính chỉ số tổng hợp từ nhiều bản ghi

**Đáp án: D**

**Giải thích:** Trung bình và cực đại tổng hợp trường số qua nhiều học viên. Với lớp rỗng, cần quy định kết quả 'không có dữ liệu' trước khi tính thống kê số.


**Q5. What does `db.get('S1')` do? | `db.get('S1')` làm gì?**

A. Returns S1 value or None if missing | Trả giá trị S1 hoặc None nếu thiếu

B. Inserts or overwrites the key's value | Thêm hoặc ghi đè giá trị của khóa

C. Removes S2 or returns None if absent | Xóa S2 hoặc trả None nếu thiếu

D. Number of scores in the list | Số điểm trong danh sách

**Đáp án: A**

**Giải thích:** get cho phép tra thiếu khóa mà không ném KeyError. `get` chỉ đọc; việc nhận giá trị mặc định không làm tạo hồ sơ còn thiếu.


**Q6. What does `db['S1']=record` do? | `db['S1']=record` làm gì?**

A. Returns S1 value or None if missing | Trả giá trị S1 hoặc None nếu thiếu

B. Inserts or overwrites the key's value | Thêm hoặc ghi đè giá trị của khóa

C. Removes S2 or returns None if absent | Xóa S2 hoặc trả None nếu thiếu

D. Number of scores in the list | Số điểm trong danh sách

**Đáp án: B**

**Giải thích:** Không kiểm khóa tồn tại, phép gán có thể ghi đè hồ sơ. Hàm thêm mới nên từ chối mã đã tồn tại, không chỉ dùng phép gán.


**Q7. What does `db.pop('S2',None)` do? | `db.pop('S2',None)` làm gì?**

A. Returns S1 value or None if missing | Trả giá trị S1 hoặc None nếu thiếu

B. Inserts or overwrites the key's value | Thêm hoặc ghi đè giá trị của khóa

C. Removes S2 or returns None if absent | Xóa S2 hoặc trả None nếu thiếu

D. Number of scores in the list | Số điểm trong danh sách

**Đáp án: C**

**Giải thích:** Giá trị mặc định tránh lỗi KeyError khi khóa vắng mặt. Nếu không có giá trị mặc định, pop khóa S2 còn thiếu sẽ ném KeyError.


**Q8. What does `len(scores)` provide? | `len(scores)` cung cấp gì?**

A. Returns S1 value or None if missing | Trả giá trị S1 hoặc None nếu thiếu

B. Inserts or overwrites the key's value | Thêm hoặc ghi đè giá trị của khóa

C. Removes S2 or returns None if absent | Xóa S2 hoặc trả None nếu thiếu

D. Number of scores in the list | Số điểm trong danh sách

**Đáp án: D**

**Giải thích:** Mean chia tổng cho số phần tử khi số lượng lớn hơn 0. Số lượng bằng 0 là ca biên, cần kiểm trước khi chia tổng.


**Q9. What is a safe score validation for integer score 8? | Kiểm tra điểm 8 hợp lệ trên thang 0–10 thế nào?**

A. `0 <= score <= 10` | `0 <= score <= 10`

B. Confirm the key does not exist | Xác nhận khóa chưa tồn tại

C. Confirm the key exists and new values are valid | Xác nhận khóa có và giá trị mới hợp lệ

D. KeyError | Lỗi KeyError

**Đáp án: A**

**Giải thích:** Cần kiểm cả cận dưới và cận trên. Nếu điểm đến từ chuỗi CLI bất kỳ, cần xác minh/đổi kiểu trước khi so sánh.


**Q10. What is required before adding a unique student ID? | Trước khi thêm mã sinh viên duy nhất cần gì?**

A. `0 <= score <= 10` | `0 <= score <= 10`

B. Confirm the key does not exist | Xác nhận khóa chưa tồn tại

C. Confirm the key exists and new values are valid | Xác nhận khóa có và giá trị mới hợp lệ

D. KeyError | Lỗi KeyError

**Đáp án: B**

**Giải thích:** Nhờ đó tránh ghi đè âm thầm hồ sơ khác. Kiểm khóa trước khi ghi; ghi đè rồi mới phát hiện có thể không khôi phục tự động được.


**Q11. What is required before updating a student record? | Trước khi sửa hồ sơ cần gì?**

A. `0 <= score <= 10` | `0 <= score <= 10`

B. Confirm the key does not exist | Xác nhận khóa chưa tồn tại

C. Confirm the key exists and new values are valid | Xác nhận khóa có và giá trị mới hợp lệ

D. KeyError | Lỗi KeyError

**Đáp án: C**

**Giải thích:** Sửa không nên vô tình tạo khóa mới. Nhờ đó vừa cập nhật đúng người vừa giữ điểm trong thang hợp lệ.


**Q12. What happens with `db['missing']` for an absent key? | Truy cập `db['missing']` khi thiếu khóa sẽ sao?**

A. `0 <= score <= 10` | `0 <= score <= 10`

B. Confirm the key does not exist | Xác nhận khóa chưa tồn tại

C. Confirm the key exists and new values are valid | Xác nhận khóa có và giá trị mới hợp lệ

D. KeyError | Lỗi KeyError

**Đáp án: D**

**Giải thích:** Truy cập trực tiếp gây lỗi khi khóa không tồn tại. Cần phân biệt khóa không tồn tại với học viên tồn tại nhưng điểm bằng 0.


**Q13. What does `sum([7,8,9])/3` equal? | `sum([7,8,9])/3` bằng gì?**

A. 8.0 | 8.0

B. 9 | 9

C. Check length before dividing | Kiểm số phần tử trước khi chia

D. No, not across process restarts by itself | Không, tự nó không giữ qua lúc khởi động lại

**Đáp án: A**

**Giải thích:** Tổng bằng 24 chia ba bằng 8. Cả ba điểm có trọng số bằng nhau; kết quả không phải điểm cao nhất hay tổng điểm.


**Q14. What does `max([7,8,9])` return? | `max([7,8,9])` trả gì?**

A. 8.0 | 8.0

B. 9 | 9

C. Check length before dividing | Kiểm số phần tử trước khi chia

D. No, not across process restarts by itself | Không, tự nó không giữ qua lúc khởi động lại

**Đáp án: B**

**Giải thích:** max chọn điểm lớn nhất. Phép này chọn điểm cao nhất, chưa tự xác định mã sinh viên nếu không giữ liên hệ bản ghi.


**Q15. How should an empty score list be handled before mean? | Trước khi tính mean với List điểm rỗng cần gì?**

A. 8.0 | 8.0

B. 9 | 9

C. Check length before dividing | Kiểm số phần tử trước khi chia

D. No, not across process restarts by itself | Không, tự nó không giữ qua lúc khởi động lại

**Đáp án: C**

**Giải thích:** Nếu không kiểm, chia cho len=0 sẽ gây lỗi. Chương trình cần nêu cách xử lý lớp rỗng, không bịa ra một điểm trung bình.


**Q16. What does a Python Dictionary persist automatically? | Dictionary Python tự lưu bền dữ liệu không?**

A. 8.0 | 8.0

B. 9 | 9

C. Check length before dividing | Kiểm số phần tử trước khi chia

D. No, not across process restarts by itself | Không, tự nó không giữ qua lúc khởi động lại

**Đáp án: D**

**Giải thích:** Hồ sơ trong RAM cần lưu ra file hoặc database để tồn tại lâu dài. Muốn dữ liệu còn sau khi mở lại, phải lưu bằng JSON, SQLite hoặc cơ chế lưu bền khác.


**Q17. What is a duplicate ID risk in CRUD? | Nguy cơ mã trùng trong CRUD là gì?**

A. Existing data may be overwritten | Dữ liệu cũ có thể bị ghi đè

B. Reject or safely parse with error handling | Từ chối hoặc đổi kiểu có xử lý lỗi

C. When missing keys are expected and handled | Khi dự kiến thiếu khóa và cần xử lý

D. Numeric score values | Các giá trị điểm dạng số

**Đáp án: A**

**Giải thích:** Kiểm tra khóa duy nhất tránh thay nhầm. Nên từ chối mã trùng hoặc dùng lệnh Update riêng nếu chủ ý sửa.


**Q18. What should CLI do with a non-numeric score input? | CLI nên làm gì với điểm nhập chữ thay vì số?**

A. Existing data may be overwritten | Dữ liệu cũ có thể bị ghi đè

B. Reject or safely parse with error handling | Từ chối hoặc đổi kiểu có xử lý lỗi

C. When missing keys are expected and handled | Khi dự kiến thiếu khóa và cần xử lý

D. Numeric score values | Các giá trị điểm dạng số

**Đáp án: B**

**Giải thích:** Chuỗi nhập từ terminal cần đổi số trước khi so ngưỡng. Hãy đổi kiểu an toàn, xử lý ValueError rồi mới kiểm tra thang điểm.


**Q19. When is `dict.get` preferable to square indexing? | Khi nào dùng `dict.get` thay `dict[key]`?**

A. Existing data may be overwritten | Dữ liệu cũ có thể bị ghi đè

B. Reject or safely parse with error handling | Từ chối hoặc đổi kiểu có xử lý lỗi

C. When missing keys are expected and handled | Khi dự kiến thiếu khóa và cần xử lý

D. Numeric score values | Các giá trị điểm dạng số

**Đáp án: C**

**Giải thích:** get trả mặc định thay cho ném KeyError. Khi chắc chắn mọi khóa đều có, truy cập [] phù hợp; nếu có thể thiếu thì `get` an toàn hơn.


**Q20. Which fields should an average score computation use? | Tính điểm trung bình nên dùng trường nào?**

A. Existing data may be overwritten | Dữ liệu cũ có thể bị ghi đè

B. Reject or safely parse with error handling | Từ chối hoặc đổi kiểu có xử lý lỗi

C. When missing keys are expected and handled | Khi dự kiến thiếu khóa và cần xử lý

D. Numeric score values | Các giá trị điểm dạng số

**Đáp án: D**

**Giải thích:** ID và tên để nhận diện, không đưa vào phép trung bình. Chỉ tổng hợp trường điểm dạng số, thống nhất thang đo và cách xử lý ô thiếu.

## 8. Nối sang bài tiếp

`Dictionary/Function → CRUD → CLI → File/CSV → Data App`.

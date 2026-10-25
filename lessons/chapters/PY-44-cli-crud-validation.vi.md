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

```python
# Mục đích: Bốn thao tác trên hồ sơ.
db = {}
db['S1'] = {'name': 'An', 'score': 8}
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

```python
# Mục đích: Chặn dữ liệu sai trước khi ghi.
score = 8
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

```python
# Mục đích: Tìm bản ghi theo mã.
db = {'S1': {'score': 8}}
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

```python
# Mục đích: Tóm tắt nhiều bản ghi.
scores = [7, 8, 9]
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

**Tình huống thực tế:** Phòng đào tạo nhận **10 yêu cầu thêm học viên**; mỗi yêu cầu gồm mã S01…, tên và điểm thang 10. Yêu cầu cuối cố nhập lại mã S03 với tên khác, nên cần lưu được 9 hồ sơ và từ chối thao tác có nguy cơ ghi đè điểm thật.

**Vì sao chọn cách này?** Dictionary chỉ cho phép một giá trị cho một khóa; nếu gán thẳng `db[id]=...` mà không kiểm tra, yêu cầu trùng sẽ **âm thầm ghi đè**. Kiểm trước khi ghi, lưu số thành công/thất bại để dễ đối soát.

**Quy trình:**
1. Tạo 10 yêu cầu có một mã lặp và điểm hợp lệ.
2. Kiểm mã tồn tại trước mỗi lệnh ADD rồi lưu hồ sơ.
3. Đếm kết quả, xác nhận điểm S03 gốc không bị thay.

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

**Tình huống thực tế:** Phòng học có **10 học viên** S01–S10 trong RAM; S01 có điểm **0/10 hợp lệ**. Nhân viên thực hiện **12 lượt tra cứu**, gồm đủ 10 mã và hai mã không tồn tại S99/S88. Cần trả lời số mã tìm thấy, số mã thiếu và xác nhận S01 không bị coi là hồ sơ không tồn tại vì có điểm 0.

**Vì sao chọn cách này?** `dict.get(id)` trả None khi thiếu khóa; kiểm đối tượng hồ sơ bằng `is None`, không dùng `if not record['score']` vì điểm 0 là số hợp lệ.

**Quy trình:**
1. Tạo 10 hồ sơ với mã khác nhau và 12 lượt tra ID.
2. Dùng `get` nhận hồ sơ hoặc None, đếm lượt tìm thấy/thất bại.
3. Kiểm riêng điểm 0 của S01 vẫn được trả về đúng.

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

**Tình huống thực tế:** Một lớp có **10 hồ sơ** S01–S10 và nhận **15 yêu cầu sửa điểm**; 10 yêu cầu đầu hợp lệ (điểm trong 0–10), năm yêu cầu sau gồm điểm âm, vượt 10, chuỗi không phải số, NaN và mã không tồn tại. Cần cập nhật chỉ các yêu cầu hợp lệ, không ghi giá trị giả hoặc tạo mã mới.

**Vì sao chọn cách này?** Chuỗi từ CLI phải đổi sang `float` trong `try/except`, tiếp tục kiểm `math.isfinite` vì `float('nan')` là số dấu phẩy động nhưng **không phải điểm hợp lệ**. Kiểm khóa trước thao tác Update.

**Quy trình:**
1. Tạo 10 mã ban đầu và 15 yêu cầu chứa điểm ở dạng chuỗi.
2. Kiểm mã có sẵn, thử đổi điểm, chặn số ngoài thang và NaN.
3. Đếm cập nhật/thất bại, đối chiếu số hồ sơ và điểm mới S03.

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

**Tình huống thực tế:** Một ứng dụng CLI ban đầu có **10 hồ sơ** S01–S10 và nhận **18 lệnh xóa**; 10 lệnh đầu xóa đúng mã một lần, 8 lệnh cuối lặp hoặc chứa mã chưa có. Cần biết có bao nhiêu hồ sơ thực sự bị xóa, bao nhiêu lệnh không thay đổi dữ liệu và kiểm tra DB rỗng sau cùng.

**Vì sao chọn cách này?** `dict.pop(id, None)` tránh ném KeyError khi mã vắng. Nhưng CLI vẫn cần **thông báo không tìm thấy**, không coi lần xóa thứ hai là thành công.

**Quy trình:**
1. Tạo 10 ID trong Dictionary và 18 mã được yêu cầu xóa.
2. Dùng `pop(..., None)`, đếm thành công khi trả hồ sơ thật.
3. Báo số lệnh lỗi/không thay đổi và số hồ sơ còn lại.

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

**Tình huống thực tế:** Trung tâm mô phỏng một ứng dụng CLI nhận **20 lệnh văn bản** gồm ADD, GET, UPDATE, DELETE, REPORT. Mỗi lệnh là một dòng sự kiện có thứ tự; 10 lệnh đầu thêm học viên, các lệnh sau có sửa hợp lệ, thêm trùng, điểm `bad`, tra mã không có, xóa lặp và điểm vượt 10. Cần **không làm hỏng dữ liệu khi nhập lỗi**, đếm số lệnh từ chối và in mean điểm trên hồ sơ còn lại.

**Vì sao chọn cách này?** Dùng `shlex.split` tách cú pháp đơn giản thay vì `eval`, kiểm số trường từng loại lệnh, kiểm trùng mã/số hữu hạn/thang điểm trước khi sửa. Một lệnh báo cáo chỉ **đọc**, không thay đổi Dictionary.

**Quy trình:**
1. Lưu 20 dòng lệnh để chạy tự động, không cần người nhập bàn phím.
2. Phân tích từng lệnh theo tên và số đối số, kiểm khóa và giá trị điểm.
3. Đếm CREATE/UPDATE/DELETE/thất bại; tính số hồ sơ và mean cuối, xác nhận báo cáo không ghi dữ liệu.

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

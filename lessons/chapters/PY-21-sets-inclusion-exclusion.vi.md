# PY-21 — Tập hợp, bao hàm–loại trừ và phân hoạch


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Union** — phép hợp; **Intersection** — phép giao.

`Set → hợp/giao/hiệu → bao hàm–loại trừ → train/test`

**Học xong dùng để làm gì?** Đếm số người thuộc nhiều nhóm mà không tính trùng, phân hoạch đối tượng thành các tập không giao nhau.

**Kết nối kiến thức tiếp theo:** PY-22 đếm số cách chọn nhóm và xếp thứ tự từ tập phần tử.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Giải thích |
|---|---|---|
| Union | phép hợp | Lấy tất cả phần tử thuộc ít nhất một tập |
| Intersection | phép giao | Lấy phần tử có trong cả hai tập |
| Inclusion–exclusion | bao hàm–loại trừ | Cộng từng tập rồi trừ phần giao bị đếm hai lần |
| Partition | phân hoạch | Chia thành các nhóm rời nhau phủ đủ tập gốc |

## 3. Hàm Python và tham số

**Từ vựng trong mục:** **Function** — hàm; **Parameter** — tham số.

| Hàm / cú pháp | Vì sao dùng |
|---|---|
| `a \| b, a & b` | Hợp và giao các tập hợp |
| `a - b, a ^ b` | Hiệu và hiệu đối xứng |
| `len(a \| b)` | Đếm phần tử khác nhau |
| `a.isdisjoint(b)` | Kiểm tra hai nhóm có trùng phần tử không |

## 4. Khái niệm liên quan

**Tập hợp** giúp lưu các đối tượng **khác nhau** rồi so sánh thành viên giữa các nhóm. Ta dùng hai lớp học Python và AI làm ví dụ xuyên suốt: phép hợp tìm tất cả học viên, phép giao tìm người học cả hai, quy tắc bao hàm–loại trừ giúp đếm không trùng, còn phân hoạch giúp chia bộ dữ liệu thành các phần rời nhau.

### 4.1. Set và phép hợp — Ai tham gia ít nhất một nhóm?

**Từ vựng trong mục:** **Set** — tập hợp; **Union** — phép hợp.

Set không giữ phần tử trùng. Lớp Python gồm SV1, SV2; lớp AI gồm SV2, SV3. Phép **hợp** `python | ai` chứa tất cả người có mặt trong **ít nhất một** lớp. SV2 nằm ở cả hai nhưng chỉ xuất hiện một lần. Khi cần đầu ra ổn định, dùng `sorted()` vì Set không bảo đảm thứ tự hiển thị.

**No Note — Không chú thích**

```python
python = {'SV1', 'SV2'}
ai = {'SV2', 'SV3'}
print(sorted(python | ai))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tìm danh sách sinh viên thuộc ít nhất một trong hai nhóm Python/AI bằng phép hợp tập hợp.
# Dữ liệu: Mã SV1, SV2 thuộc Python; SV2, SV3 thuộc AI; SV2 có mặt ở cả hai nhưng chỉ đếm một lần.
# Tập set lưu mã không trùng; dấu ngoặc nhọn tạo tập hợp sinh viên Python.
python = {'SV1', 'SV2'}
# Tập AI chứa SV2 chung với Python và SV3 riêng.
ai = {'SV2', 'SV3'}
# | là hợp hai set, lấy người thuộc ít nhất một nhóm và bỏ SV2 trùng; sorted() xếp mã để in ổn định vì set không có thứ tự bảo đảm.
print(sorted(python | ai))
```

**Kết quả khi chạy:**

```text
['SV1', 'SV2', 'SV3']
```

Ba mã học viên khác nhau thuộc ít nhất một lớp; `sorted` tạo List để hiển thị theo thứ tự rõ ràng.

### 4.2. Intersection và Difference — Phần chung và phần riêng

**Từ vựng trong mục:** **Intersection** — phép giao; **Difference** — hiệu tập hợp.

**Giao** `a & b` chỉ lấy phần tử thuộc cả hai nhóm; với lớp Python {SV1,SV2} và AI {SV2,SV3}, phần chung là SV2. **Hiệu** `a - b` chỉ lấy phần tử thuộc a nhưng không thuộc b, tức SV1 trong ví dụ. Hiệu khác hiệu đối xứng `a ^ b`, vốn chứa các phần tử chỉ có ở đúng một nhóm.

**No Note — Không chú thích**

```python
a = {'SV1', 'SV2'}
b = {'SV2', 'SV3'}
print(sorted(a & b), sorted(a - b))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tách mã học viên thuộc cả hai nhóm và chỉ thuộc nhóm thứ nhất bằng phép giao/hiệu.
# Dữ liệu: a={SV1,SV2}, b={SV2,SV3}; SV2 là phần chung, SV1 chỉ ở a.
# set không lưu phần tử trùng; a là nhóm đầu.
a = {'SV1', 'SV2'}
# b là nhóm sau, có một thành viên chung với a.
b = {'SV2', 'SV3'}
# & lấy giao: mã xuất hiện trong CẢ HAI set; - lấy hiệu a-b: chỉ mã ở a; sorted() giữ thứ tự xuất ổn định.
print(sorted(a & b), sorted(a - b))
```

**Kết quả khi chạy:**

```text
['SV2'] ['SV1']
```

SV2 học cả hai lớp, còn SV1 chỉ học Python. Hai phép toán trả lời hai câu hỏi khác nhau.

### 4.3. Inclusion–exclusion — Đếm không lặp người

**Từ vựng trong mục:** **Inclusion–exclusion** — bao hàm–loại trừ; **Cardinality** — số phần tử.

Nếu cộng số học viên hai lớp trực tiếp, người học cả hai bị đếm **hai lần**. Ví dụ lớp Python có 2 người, lớp AI có 2 người, một người chung: số người khác nhau bằng `2 + 2 - 1 = 3`. Công thức `|A ∪ B| = |A| + |B| - |A ∩ B|` trừ phần bị đếm lặp. Với hơn hai tập, cần tính thêm các giao nhiều tập.

**No Note — Không chú thích**

```python
a = {'SV1', 'SV2'}
b = {'SV2', 'SV3'}
print(len(a) + len(b) - len(a & b))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Đếm học viên duy nhất của hai nhóm bằng nguyên lý cộng trừ phần giao.
# Dữ liệu: Hai tập hai người, có SV2 lặp trong cả hai.
# Mỗi set đếm một người tối đa một lần.
a = {'SV1', 'SV2'}
# SV2 ở cả hai nên nếu cộng hai số lượng sẽ bị đếm hai lần.
b = {'SV2', 'SV3'}
# len() đếm từng set; trừ len(a & b) vì người thuộc cả hai đã bị cộng hai lần; kết quả là số người duy nhất 3.
print(len(a) + len(b) - len(a & b))
```

**Kết quả khi chạy:**

```text
3
```

Kết quả đếm ba học viên duy nhất, không coi SV2 là hai người khác nhau.

### 4.4. Partition — Chia đủ dữ liệu thành phần rời

**Từ vựng trong mục:** **Partition** — phân hoạch; **Disjoint** — không giao nhau.

**Phân hoạch** tập dữ liệu gốc thành các nhóm **không rỗng**, **không giao nhau**, và **hợp lại bằng đúng tập gốc**. Ví dụ toàn bộ mã `{1,2,3,4,5}`, train `{1,2,3}`, test `{4,5}`. `isdisjoint` chỉ kiểm tra không trùng; để chứng minh phân hoạch còn phải kiểm tra hợp của chúng có phủ đủ dữ liệu gốc. Với Machine Learning, không trùng ID **chưa chắc** loại bỏ mọi hình thức rò rỉ dữ liệu.

**No Note — Không chú thích**

```python
all_ids = {1, 2, 3, 4, 5}
train = {1, 2, 3}
test = {4, 5}
print(bool(train) and bool(test) and train.isdisjoint(test) and train | test == all_ids)
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Xác minh Train/Test chia đủ năm mã nguồn, mỗi nhóm có dữ liệu và không chồng lấn.
# Dữ liệu: all_ids là năm mẫu nguồn; train có ba mẫu, test hai mẫu.
# Tập tất cả mã là tập nguồn cần được chia không sót.
all_ids = {1, 2, 3, 4, 5}
# Tập mẫu dùng để học mô hình.
train = {1, 2, 3}
# Tập mẫu dành kiểm tra, phải không trùng train.
test = {4, 5}
# Tập mẫu dành kiểm tra, phải không trùng train.
# bool(set) là False khi set rỗng; hai bool đảm bảo cả train và test không rỗng.
# isdisjoint(test) trả True nếu giao hai tập RỖNG, tránh dùng lại mẫu train trong test.
# | hợp hai tập; == so với nguồn để xác nhận bao phủ đủ và không có mã lạ.
print(bool(train) and bool(test) and train.isdisjoint(test) and train | test == all_ids)
```

**Kết quả khi chạy:**

```text
True
```

Hai tập đều có dữ liệu, không trùng và phủ đủ toàn bộ năm mã, nên tạo một phân hoạch hợp lệ.
## 5. Năm tình huống Set — từ đếm duy nhất đến kiểm tra phân hoạch dữ liệu

### Tình huống 1 — Cấp 1: Đếm học viên duy nhất từ 10 lượt đăng ký

**Từ vựng trong mục:** **Set** — tập hợp; **Union** — phép hợp.

**Tình huống thực tế:** Trung tâm ngoại ngữ nhận **10 lượt đăng ký môn học**. Mỗi lượt là một cặp gồm **mã học viên** (SV01 đến SV08) và môn **Python hoặc AI**. SV01 và SV05 đều đăng ký cả hai môn nên một người có thể tạo **hai lượt đăng ký**. Giáo vụ cần biết có bao nhiêu **người khác nhau** đã đăng ký ít nhất một môn, đồng thời liệt kê mã những người học cả hai, tránh nhầm số dòng đăng ký với số học viên.

**Vì sao chọn cách này?** **Set** (tập hợp) là kiểu dữ liệu chỉ giữ **mỗi mã duy nhất một lần**, dù mã ấy xuất hiện ở nhiều lượt đăng ký. Chương trình duyệt 10 dòng rồi thêm mã vào `python_students` hoặc `ai_students` theo môn. Phép **hợp** `|` cho tất cả mã có ở ít nhất một tập, còn phép **giao** `&` giữ những mã có ở **cả hai tập**. `sorted()` sắp mã trước khi in vì set không đảm bảo một thứ tự hiển thị cố định. Không dùng `len(registrations)` để đếm người, vì SV01 và SV05 mỗi người được ghi hai lần.

**Quy trình:**
1. Ghi 10 bản ghi, mỗi bản ghi là một lượt đăng ký.
2. Tạo tập mã học viên Python và AI.
3. Lấy hợp/giao, đối chiếu số người và số lượt.

**No Note — Không chú thích**

```python
registrations = [["SV01","Python"],["SV02","AI"],["SV03","Python"],["SV01","AI"],["SV04","AI"],["SV05","Python"],["SV06","AI"],["SV05","AI"],["SV07","Python"],["SV08","AI"]]
python_students = set()
ai_students = set()
for sid, subject in registrations:
    if subject == "Python":
        python_students.add(sid)
    if subject == "AI":
        ai_students.add(sid)
if len(registrations) != 10:
    raise ValueError("Cần đủ 10 lượt đăng ký.")
print("Lượt đăng ký:", len(registrations))
print("Học viên duy nhất:", len(python_students | ai_students))
print("Học cả hai:", ", ".join(sorted(python_students & ai_students)))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Từ 10 lượt đăng ký Python/AI, đếm học viên duy nhất và người học cả hai.
# Dữ liệu: 10 cặp (mã SV, tên môn); một người có thể xuất hiện hai lượt ở hai môn.
# Mỗi list con là một lượt (student_id, subject), KHÔNG phải mỗi hàng một học viên duy nhất.
registrations = [["SV01","Python"],["SV02","AI"],["SV03","Python"],["SV01","AI"],["SV04","AI"],["SV05","Python"],["SV06","AI"],["SV05","AI"],["SV07","Python"],["SV08","AI"]]
# set() tạo tập rỗng, dùng để tự bỏ những mã lặp khi thu thập đăng ký.
python_students = set()
# set() tạo tập rỗng, dùng để tự bỏ những mã lặp khi thu thập đăng ký.
ai_students = set()
# Duyệt từng lượt đăng ký và tách mã học viên/môn của lượt đó.
for sid, subject in registrations:
    if subject == "Python":
        # add() thêm mã vào tập Python; nếu lặp cùng mã cũng chỉ lưu một lần.
        python_students.add(sid)
    if subject == "AI":
        # add() thêm mã vào tập AI, giữ một bản sao mỗi người.
        ai_students.add(sid)
# len() xác nhận có đúng 10 LƯỢT đăng ký, không phải 10 người.
if len(registrations) != 10:
    # ValueError dừng khi dữ liệu hoặc điều kiện đối chiếu không hợp lệ.
    raise ValueError("Cần đủ 10 lượt đăng ký.")
print("Lượt đăng ký:", len(registrations))
# | là hợp: người tham gia ít nhất một môn, bỏ trùng hai môn.
print("Học viên duy nhất:", len(python_students | ai_students))
# & là giao: người học cả hai; sorted() sắp mã vì thứ tự set không cố định, join() ghép bằng ', '.
print("Học cả hai:", ", ".join(sorted(python_students & ai_students)))
```

**Kết quả khi chạy:**

```text
Lượt đăng ký: 10
Học viên duy nhất: 8
Học cả hai: SV01, SV05
```

SV01 đăng ký hai lớp vẫn là **một người**. Đây là bài tập phép hợp/giao với dữ liệu theo hàng, không đếm trùng người.

### Tình huống 2 — Cấp 2: Tách người chỉ học một môn qua 12 lượt

**Từ vựng trong mục:** **Difference** — hiệu tập hợp; **Symmetric difference** — hiệu đối xứng.

**Tình huống thực tế:** Quầy tư vấn nhận **12 lượt đăng ký học** từ các học viên H01 đến H10. Mỗi dòng chứa **mã người đăng ký** và một trong hai môn Python hoặc AI. H01 và H07 đăng ký cả hai môn; người chỉ có một môn cần được liên hệ để giới thiệu môn còn lại. Nhân viên muốn biết ai **chỉ học Python**, ai **chỉ học AI**, và có tất cả bao nhiêu người chỉ đăng ký đúng một môn.

**Vì sao chọn cách này?** Để tìm người **chỉ học Python**, lấy tập Python **trừ** tập AI bằng `pyt - ai`; chiều ngược lại `ai - pyt` cho người chỉ học AI. Đây là **phép hiệu tập hợp**, giữ mã có ở nhóm đầu nhưng không có nhóm thứ hai. Phép **hiệu đối xứng** `^` gom cả hai nhóm chỉ học một môn, đồng thời loại người học cả hai. H01 và H07 không được đưa vào danh sách cần mời học môn còn lại vì họ đã đăng ký đủ hai môn. Cần chuẩn hóa theo **mã học viên**, không so hai lượt theo số thứ tự đăng ký.

**Quy trình:**
1. Chuyển lượt đăng ký thành tập mã theo từng môn.
2. Tính hiệu từng chiều để biết học viên cần tư vấn môn nào.
3. Tính hiệu đối xứng, đối chiếu tổng hai nhóm.

**No Note — Không chú thích**

```python
registrations = [["H01","AI"],["H02","Python"],["H03","AI"],["H04","Python"],["H05","AI"],["H01","Python"],["H06","Python"],["H07","AI"],["H08","Python"],["H09","AI"],["H07","Python"],["H10","Python"]]
pyt = set()
ai = set()
for sid, sub in registrations:
    if sub == "Python":
        pyt.add(sid)
    if sub == "AI":
        ai.add(sid)
only_python = sorted(pyt - ai)
only_ai = sorted(ai - pyt)
only_one = pyt ^ ai
if len(registrations) != 12:
    raise ValueError("Cần đủ 12 lượt đăng ký.")
print("Lượt:", len(registrations))
print("Chỉ Python:", ", ".join(only_python))
print("Chỉ AI:", ", ".join(only_ai))
print("Chỉ một môn:", len(only_one))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tách học viên chỉ học Python, chỉ học AI và học đúng một môn trong 12 lượt.
# Dữ liệu: 12 lượt môn Python/AI có người đăng ký hai lần; H01 và H07 học hai môn.
# 12 cặp mã Hxx và môn; một học viên có thể được ghi nhiều lần nếu học hai môn.
registrations = [["H01","AI"],["H02","Python"],["H03","AI"],["H04","Python"],["H05","AI"],["H01","Python"],["H06","Python"],["H07","AI"],["H08","Python"],["H09","AI"],["H07","Python"],["H10","Python"]]
# set() khởi tạo tập mã Python không trùng.
pyt = set()
# set() khởi tạo tập mã AI không trùng.
ai = set()
# Duyệt từng cặp và dùng môn để chọn tập cần cập nhật.
for sid, sub in registrations:
    if sub == "Python":
        # add() ghi mã Python duy nhất, không làm tăng tập nếu đã có.
        pyt.add(sid)
    if sub == "AI":
        # add() ghi mã AI duy nhất.
        ai.add(sid)
# pyt - ai lấy người CHỈ Python; sorted() xếp mã để in dễ đối chiếu.
only_python = sorted(pyt - ai)
# ai - pyt lấy người CHỈ AI, không có trong Python.
only_ai = sorted(ai - pyt)
# ^ là hiệu đối xứng: thuộc ĐÚNG MỘT trong hai tập, không thuộc giao; khác | là hợp.
only_one = pyt ^ ai
# len() kiểm đủ số LƯỢT nguồn, không đếm số người.
if len(registrations) != 12:
    # ValueError dừng khi dữ liệu hoặc điều kiện đối chiếu không hợp lệ.
    raise ValueError("Cần đủ 12 lượt đăng ký.")
print("Lượt:", len(registrations))
# join() ghép các mã chỉ Python bằng dấu phẩy + khoảng trắng.
print("Chỉ Python:", ", ".join(only_python))
# join() ghép các mã chỉ AI thành chuỗi báo cáo.
print("Chỉ AI:", ", ".join(only_ai))
# len() đếm số người chỉ học một trong hai môn.
print("Chỉ một môn:", len(only_one))
```

**Kết quả khi chạy:**

```text
Lượt: 12
Chỉ Python: H02, H04, H06, H08, H10
Chỉ AI: H03, H05, H09
Chỉ một môn: 8
```

Một người có thể thuộc hai Set cùng lúc, nên không được dùng tổng kích thước hai Set để suy ra số người cần tư vấn một môn.

### Tình huống 3 — Cấp 3: Đối chiếu 15 lượt truy cập bằng bao hàm–loại trừ

**Từ vựng trong mục:** **Inclusion–exclusion** — bao hàm–loại trừ; **Intersection** — phần chung.

**Tình huống thực tế:** Ứng dụng dịch vụ ghi **15 lượt truy cập** của khách K01 đến K12. Mỗi dòng cho biết mã khách và **kênh truy cập** là `app` (ứng dụng) hoặc `web` (trang web). K01, K03 và K12 đã dùng cả hai kênh, nên đếm số khách trên từng kênh rồi cộng thẳng sẽ bị lặp. Bộ phận kinh doanh cần biết số **khách duy nhất** đã dùng ít nhất một kênh, số khách dùng cả hai và xác nhận phép đếm không bị tính trùng.

**Vì sao chọn cách này?** Mỗi kênh được lưu thành một set mã khách để việc khách ghé nhiều lần không làm số người tăng lên. Khách K01 có trong **cả `app` và `web`**, vì vậy phần giao `app & web` nhận biết người bị đếm hai lần nếu cộng số khách của hai kênh. Quy tắc **bao hàm–loại trừ** diễn giải bằng lời là: cộng người của hai kênh, rồi **trừ một lần số người thuộc cả hai**. Chương trình cũng kiểm tra kết quả bằng `len(app | web)`, tức số mã khác nhau xuất hiện trên ít nhất một kênh. Đây là cách đếm **khách duy nhất**, không phải số lượt truy cập.

**Quy trình:**
1. Tạo hai Set khách hàng dựa trên 15 lượt ghi.
2. Đếm khách riêng từng kênh và khách dùng cả hai.
3. Tính số khách duy nhất bằng quy tắc bao hàm–loại trừ, đối chiếu phép hợp.

**No Note — Không chú thích**

```python
visits = [["K01","app"],["K02","web"],["K01","web"],["K03","app"],["K04","web"],["K05","app"],["K06","web"],["K07","app"],["K03","web"],["K08","app"],["K09","web"],["K10","app"],["K11","web"],["K12","app"],["K12","web"]]
app = set()
web = set()
for sid, channel in visits:
    if channel == "app":
        app.add(sid)
    if channel == "web":
        web.add(sid)
via_count = len(app) + len(web) - len(app & web)
if len(visits) != 15 or via_count != len(app | web):
    raise ValueError("Cần đối chiếu đủ 15 lượt và số khách duy nhất.")
print("Lượt:", len(visits))
print("Dùng app:", len(app))
print("Dùng web:", len(web))
print("Cả hai:", len(app & web))
print("Khách duy nhất:", via_count)
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Đếm khách duy nhất ở 15 lượt ghé app/web bằng nguyên lý cộng trừ phần chung.
# Dữ liệu: 15 cặp (mã khách, kênh); khách ghé hai kênh phải được đếm đúng một lần.
# 15 lượt tiếp xúc, mỗi hàng gồm customer_id và channel app/web; không có nghĩa 15 khách.
visits = [["K01","app"],["K02","web"],["K01","web"],["K03","app"],["K04","web"],["K05","app"],["K06","web"],["K07","app"],["K03","web"],["K08","app"],["K09","web"],["K10","app"],["K11","web"],["K12","app"],["K12","web"]]
# Set chứa mỗi khách app một lần.
app = set()
# Set chứa mỗi khách web một lần.
web = set()
# Duyệt từng lượt và phân loại theo kênh.
for sid, channel in visits:
    if channel == "app":
        # Thêm mã khách vào nhóm app, tự loại lượt lặp.
        app.add(sid)
    if channel == "web":
        # Thêm mã khách vào nhóm web, tự loại lượt lặp.
        web.add(sid)
# Cộng lượng người của hai kênh rồi trừ giao (&) để không đếm hai lần người dùng cả hai.
# & là giao app và web, số người ghé cả hai.
via_count = len(app) + len(web) - len(app & web)
# | là hợp tạo tập tất cả khách, dùng đối chiếu với cách cộng-trừ.
# Kiểm đủ 15 lượt nguồn; or báo sai nếu số khách hợp không khớp.
if len(visits) != 15 or via_count != len(app | web):
    # ValueError dừng khi dữ liệu hoặc điều kiện đối chiếu không hợp lệ.
    raise ValueError("Cần đối chiếu đủ 15 lượt và số khách duy nhất.")
print("Lượt:", len(visits))
print("Dùng app:", len(app))
print("Dùng web:", len(web))
# & là giao app và web, số người ghé cả hai.
print("Cả hai:", len(app & web))
print("Khách duy nhất:", via_count)
```

**Kết quả khi chạy:**

```text
Lượt: 15
Dùng app: 7
Dùng web: 8
Cả hai: 3
Khách duy nhất: 12
```

Số khách duy nhất khác số lượt truy cập, vì mỗi người có thể truy cập hơn một lần hoặc qua hai kênh.

### Tình huống 4 — Cấp 4: Rà soát phân hoạch 18 mẫu train/test bị lặp ID

**Từ vựng trong mục:** **Partition** — phân hoạch; **Disjoint** — không giao nhau; **Coverage** — bao phủ.

**Tình huống thực tế:** Nhóm học máy có **18 mẫu dữ liệu D01 đến D18**, mỗi mã biểu thị một mẫu cần phân vào tập **train** (dùng để học) hoặc **test** (dùng để đánh giá). Trong danh sách được chuẩn bị sẵn, **D12 xuất hiện ở cả hai tập** và **D18 chưa được đưa vào tập nào**. Trước khi huấn luyện, nhóm cần báo rõ mã trùng, mã bị bỏ sót và xác nhận cách chia hiện tại có hợp lệ hay không, chứ không tự động sửa bằng cách xóa một mã.

**Vì sao chọn cách này?** Một cách chia train/test đúng phải thỏa **hai điều kiện cùng lúc**: không có mẫu nằm ở hai tập và không bỏ quên mẫu nào trong danh sách nguồn. `train & test` tìm mã **bị trùng**, còn `source - (train | test)` tìm mã **chưa thuộc nhóm nào**. `isdisjoint()` hỏi hai tập có hoàn toàn **không giao nhau** không; kết hợp thêm việc hợp hai tập phải bằng nguồn mới kiểm tra đủ. Chỉ thấy hai tập không trùng **chưa đủ**, vì vẫn có thể bỏ quên D18. Khi D12 nằm ở cả train lẫn test, kết quả đánh giá mô hình còn có nguy cơ bị lạc quan do gặp lại mẫu đã học.

**Quy trình:**
1. Tạo tập nguồn 18 ID; lưu train/test theo quyết định hiện tại.
2. Tìm ID trùng bằng phép giao và ID thiếu bằng hiệu nguồn với hợp.
3. In các mã cần sửa và kiểm tra phân hoạch đạt/không đạt.

**No Note — Không chú thích**

```python
all_ids = ["D01","D02","D03","D04","D05","D06","D07","D08","D09","D10","D11","D12","D13","D14","D15","D16","D17","D18"]
train = set(["D01","D02","D03","D04","D05","D06","D07","D08","D09","D10","D11","D12"])
test = set(["D12","D13","D14","D15","D16","D17"])
source = set(all_ids)
overlap = sorted(train & test)
missing = sorted(source - (train | test))
valid_partition = train.isdisjoint(test) and (train | test) == source
if len(source) != 18:
    raise ValueError("Cần đủ 18 mẫu nguồn trước khi chia Train/Test.")
print("Mẫu nguồn:", len(source))
print("Trùng:", ", ".join(overlap))
print("Chưa phân nhóm:", ", ".join(missing))
print("Phân hoạch đúng:", valid_partition)
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Kiểm lỗi chia Train/Test trong 18 mẫu bằng giao nhau, hợp và phần thiếu.
# Dữ liệu: 18 mã D01..D18, D12 xuất hiện ở cả train/test; D18 chưa được phân nhóm.
# List 18 mã nguồn; dùng set bên dưới để đối chiếu như tập hợp.
all_ids = ["D01","D02","D03","D04","D05","D06","D07","D08","D09","D10","D11","D12","D13","D14","D15","D16","D17","D18"]
# set() biến list 12 mã thành tập train không trùng nội bộ.
train = set(["D01","D02","D03","D04","D05","D06","D07","D08","D09","D10","D11","D12"])
# set() biến list mã test thành tập; D12 bị trùng với train.
test = set(["D12","D13","D14","D15","D16","D17"])
# set(all_ids) lấy tập 18 mã nguồn không trùng.
source = set(all_ids)
# & là giao train/test: những mẫu BỊ LỘ DỮ LIỆU giữa hai tập; sorted() xếp mã.
overlap = sorted(train & test)
# | hợp mã đã phân nhóm, - trừ khỏi nguồn để tìm mẫu chưa được giao vào nhóm nào.
missing = sorted(source - (train | test))
# isdisjoint() True chỉ khi train và test không có chung một mẫu.
# Hợp phải bằng nguồn để không sót mẫu hay phát sinh mã lạ; and đòi cả 2 phép kiểm.
# Cờ True chỉ khi tập không giao nhau VÀ hợp bằng toàn nguồn.
valid_partition = train.isdisjoint(test) and (train | test) == source
# Kiểm đủ 18 mã khác nhau, không đơn thuần số dòng list.
if len(source) != 18:
    # ValueError dừng khi dữ liệu hoặc điều kiện đối chiếu không hợp lệ.
    raise ValueError("Cần đủ 18 mẫu nguồn trước khi chia Train/Test.")
print("Mẫu nguồn:", len(source))
print("Trùng:", ", ".join(overlap))
print("Chưa phân nhóm:", ", ".join(missing))
# Cờ True chỉ khi tập không giao nhau VÀ hợp bằng toàn nguồn.
print("Phân hoạch đúng:", valid_partition)
```

**Kết quả khi chạy:**

```text
Mẫu nguồn: 18
Trùng: D12
Chưa phân nhóm: D18
Phân hoạch đúng: False
```

Chỉ khi hai điều kiện cùng đúng mới sử dụng train/test: một mẫu trùng có thể làm sai đánh giá, và mẫu bỏ sót làm phân chia chưa đầy đủ.

### Tình huống 5 — Cấp 5: Kiểm kê 20 hồ sơ đa vùng, cảnh báo ID xuất hiện chéo

**Từ vựng trong mục:** **Disjoint sets** — tập rời nhau; **Union** — phép hợp; **Data integrity** — toàn vẹn dữ liệu.

**Tình huống thực tế:** Một chương trình học trực tuyến ghi **20 dòng hoạt động** từ người học ở ba vùng Bắc, Nam và Trung. Mỗi dòng có mã học viên, vùng, kênh truy cập và điểm hoạt động (**điểm**); một người có thể có nhiều dòng. **S04** được ghi ở Bắc và Nam, **S07** ở Bắc và Trung. Nhân viên muốn biết tổng **người khác nhau**, có bao nhiêu dòng dư do mã xuất hiện lại và danh sách học viên có mặt ở nhiều vùng, nhưng không tự đoán vùng đúng để xóa dữ liệu.

**Vì sao chọn cách này?** Nhóm người mỗi vùng được biểu diễn bằng một set mã, vì **một người có nhiều dòng trong cùng vùng** cũng chỉ nên được tính là một thành viên vùng đó. `set().union(*regions.values())` hợp ba nhóm để tìm toàn bộ **mã khác nhau**. Sau đó chương trình duyệt các mã này và đếm một mã nằm trong bao nhiêu set vùng; số lớn hơn một thì ghi vào danh sách **đa vùng**. Lấy số dòng gốc trừ số người duy nhất cho biết có bao nhiêu lượt ghi vượt số mã khác nhau, nhưng **không chứng minh dòng nào sai**. Việc xóa một vùng của S04 hay S07 phải dựa vào hồ sơ đối chiếu thật, không dựa vào phép tính tập hợp.

**Quy trình:**
1. Ghi 20 dòng đầy đủ ID/vùng/kênh/điểm và tạo Set cho từng vùng.
2. Lấy hợp ba vùng để đếm ID duy nhất, kiểm tra giao từng cặp.
3. Liệt kê ID đa vùng và số dòng dư do trùng ID; giữ lại dữ liệu thô để sửa.

**No Note — Không chú thích**

```python
records = [{"id":"S01","region":"Bắc","channel":"app","score":10},{"id":"S02","region":"Nam","channel":"web","score":11},{"id":"S03","region":"Trung","channel":"app","score":12},{"id":"S04","region":"Bắc","channel":"web","score":13},{"id":"S05","region":"Nam","channel":"app","score":14},{"id":"S06","region":"Trung","channel":"web","score":15},{"id":"S07","region":"Bắc","channel":"app","score":16},{"id":"S08","region":"Nam","channel":"web","score":17},{"id":"S09","region":"Trung","channel":"app","score":18},{"id":"S10","region":"Bắc","channel":"web","score":19},{"id":"S11","region":"Nam","channel":"app","score":20},{"id":"S12","region":"Trung","channel":"web","score":21},{"id":"S13","region":"Bắc","channel":"app","score":22},{"id":"S14","region":"Nam","channel":"web","score":23},{"id":"S15","region":"Trung","channel":"app","score":24},{"id":"S16","region":"Bắc","channel":"web","score":25},{"id":"S04","region":"Nam","channel":"app","score":26},{"id":"S07","region":"Trung","channel":"web","score":27},{"id":"S19","region":"Bắc","channel":"app","score":28},{"id":"S20","region":"Nam","channel":"web","score":29}]
regions = {}
for name in ("Bắc", "Nam", "Trung"):
    regions[name] = set()
for row in records:
    regions[row["region"]].add(row["id"])
all_people = set().union(*regions.values())
multiple_regions = []
for sid in all_people:
    membership_count = 0
    for members in regions.values():
        if sid in members:
            membership_count += 1
    if membership_count > 1:
        multiple_regions.append(sid)
multiple_regions.sort()
if len(records) != 20:
    raise ValueError("Cần kiểm tra đủ 20 lượt ghi nhận theo vùng.")
print("Dòng nhận:", len(records))
print("Người duy nhất:", len(all_people))
print("Dòng dư do trùng ID:", len(records) - len(all_people))
print("Đa vùng:", ", ".join(multiple_regions))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Gộp 20 lượt ghi nhận ba vùng, tìm mã người duy nhất và người xuất hiện ở nhiều vùng.
# Dữ liệu: 20 dictionary (id,region,channel,score), ID S04/S07 có thể xuất hiện ở nhiều vùng; một lượt là một hàng.
# 20 bản ghi; region là vùng, channel kênh, score là số điểm giả lập; khóa id có thể trùng giữa các dòng.
records = [{"id":"S01","region":"Bắc","channel":"app","score":10},{"id":"S02","region":"Nam","channel":"web","score":11},{"id":"S03","region":"Trung","channel":"app","score":12},{"id":"S04","region":"Bắc","channel":"web","score":13},{"id":"S05","region":"Nam","channel":"app","score":14},{"id":"S06","region":"Trung","channel":"web","score":15},{"id":"S07","region":"Bắc","channel":"app","score":16},{"id":"S08","region":"Nam","channel":"web","score":17},{"id":"S09","region":"Trung","channel":"app","score":18},{"id":"S10","region":"Bắc","channel":"web","score":19},{"id":"S11","region":"Nam","channel":"app","score":20},{"id":"S12","region":"Trung","channel":"web","score":21},{"id":"S13","region":"Bắc","channel":"app","score":22},{"id":"S14","region":"Nam","channel":"web","score":23},{"id":"S15","region":"Trung","channel":"app","score":24},{"id":"S16","region":"Bắc","channel":"web","score":25},{"id":"S04","region":"Nam","channel":"app","score":26},{"id":"S07","region":"Trung","channel":"web","score":27},{"id":"S19","region":"Bắc","channel":"app","score":28},{"id":"S20","region":"Nam","channel":"web","score":29}]
# Dictionary ánh xạ tên vùng tới tập mã học viên riêng.
regions = {}
# Duyệt ba nhãn Bắc/Nam/Trung để tạo set rỗng cho mỗi vùng.
for name in ("Bắc", "Nam", "Trung"):
    # Tạo tập mã chưa có phần tử; set không lặp cùng ID trong vùng.
    regions[name] = set()
# Mỗi vòng xử lý đúng một dictionary nguồn.
for row in records:
    # Tra set theo khóa region rồi add() mã id; tự loại bản ghi trùng trong một vùng.
    regions[row["region"]].add(row["id"])
# regions.values() lấy ba set; toán tử * trải chúng thành đối số cho union(), hợp mọi người không trùng giữa vùng.
all_people = set().union(*regions.values())
multiple_regions = []
# Duyệt từng người duy nhất để xem họ xuất hiện ở bao nhiêu vùng.
for sid in all_people:
    membership_count = 0
    # Duyệt tập người của ba vùng.
    for members in regions.values():
        # in kiểm tra mã sid nằm trong set vùng hiện tại.
        if sid in members:
            # Đếm số VÙNG chứa một mã, không phải số lượt đăng ký.
            membership_count += 1
    # Người thuộc hơn một vùng được ghi riêng để kiểm tra chồng chéo.
    if membership_count > 1:
        # append() lưu mã người đa vùng.
        multiple_regions.append(sid)
# .sort() xếp list ngay tại chỗ để báo cáo có thứ tự cố định.
multiple_regions.sort()
# Kiểm đủ 20 lượt ghi nhận gốc.
if len(records) != 20:
    # ValueError dừng khi dữ liệu hoặc điều kiện đối chiếu không hợp lệ.
    raise ValueError("Cần kiểm tra đủ 20 lượt ghi nhận theo vùng.")
print("Dòng nhận:", len(records))
print("Người duy nhất:", len(all_people))
# Hiệu số dòng so với người duy nhất cho biết số lượt dư do lặp ID trên toàn dữ liệu.
print("Dòng dư do trùng ID:", len(records) - len(all_people))
# join() nối các mã đa vùng thành một chuỗi có dấu phẩy.
print("Đa vùng:", ", ".join(multiple_regions))
```

**Kết quả khi chạy:**

```text
Dòng nhận: 20
Người duy nhất: 18
Dòng dư do trùng ID: 2
Đa vùng: S04, S07
```

Người học phải phân biệt **dòng**, **ID duy nhất**, **ID trùng xuyên vùng**; đây là các câu hỏi khác nhau và cần kiểm tra cả ba trước khi báo cáo.

## 6. Sai lầm thường gặp

- Set không giữ thứ tự; dùng `sorted()` khi muốn kết quả mẫu có thứ tự ổn định.
- Phép hợp `|` khác phép giao `&`: hợp lấy ít nhất một nhóm, giao lấy cả hai nhóm.
- Hiệu `A - B` khác hiệu đối xứng `A ^ B`: một chiều so với chỉ xuất hiện ở đúng một trong hai tập.
- Bao hàm–loại trừ tránh đếm trùng. Nếu có ba tập trở lên, công thức cần cộng/trừ thêm các giao nhiều tập.
- `isdisjoint()` chỉ chứng minh hai tập không trùng, chưa chứng minh chúng phủ toàn bộ tập gốc.

## 7. Trắc nghiệm

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What does a union contain? | Phép hợp chứa gì?**

A. Elements in at least one set | Phần tử thuộc ít nhất một tập

B. Elements common to both sets | Phần tử có ở cả hai tập

C. Elements in A but not in B | Phần tử thuộc A nhưng không thuộc B

D. Nonempty disjoint parts covering the original set | Các phần không rỗng, rời nhau và phủ đủ tập gốc

**Đáp án: A**

**Giải thích:** Hợp chứa các phần tử khác nhau của hai tập.


**Q2. What does an intersection contain? | Phép giao chứa gì?**

A. Elements in at least one set | Phần tử thuộc ít nhất một tập

B. Elements common to both sets | Phần tử có ở cả hai tập

C. Elements in A but not in B | Phần tử thuộc A nhưng không thuộc B

D. Nonempty disjoint parts covering the original set | Các phần không rỗng, rời nhau và phủ đủ tập gốc

**Đáp án: B**

**Giải thích:** Giao chỉ giữ phần tử chung của hai tập.


**Q3. What is set difference A−B? | Hiệu tập hợp A−B là gì?**

A. Elements in at least one set | Phần tử thuộc ít nhất một tập

B. Elements common to both sets | Phần tử có ở cả hai tập

C. Elements in A but not in B | Phần tử thuộc A nhưng không thuộc B

D. Nonempty disjoint parts covering the original set | Các phần không rỗng, rời nhau và phủ đủ tập gốc

**Đáp án: C**

**Giải thích:** Hiệu A−B loại phần tử của B ra khỏi A.


**Q4. What defines a partition of a set? | Điều gì xác định một phân hoạch?**

A. Elements in at least one set | Phần tử thuộc ít nhất một tập

B. Elements common to both sets | Phần tử có ở cả hai tập

C. Elements in A but not in B | Phần tử thuộc A nhưng không thuộc B

D. Nonempty disjoint parts covering the original set | Các phần không rỗng, rời nhau và phủ đủ tập gốc

**Đáp án: D**

**Giải thích:** Mọi phần không giao nhau và hợp bằng tập gốc.


**Q5. Which operator computes union for sets? | Toán tử nào tính phép hợp Set?**

A. `a | b` | `a | b`

B. `a & b` | `a & b`

C. `a ^ b` | `a ^ b`

D. `a.isdisjoint(b)` | `a.isdisjoint(b)`

**Đáp án: A**

**Giải thích:** Dấu `|` biểu diễn phép hợp tập hợp.


**Q6. Which operator computes intersection? | Toán tử nào tính phép giao?**

A. `a | b` | `a | b`

B. `a & b` | `a & b`

C. `a ^ b` | `a ^ b`

D. `a.isdisjoint(b)` | `a.isdisjoint(b)`

**Đáp án: B**

**Giải thích:** Dấu & giữ các phần tử chung.


**Q7. Which operator computes symmetric difference? | Toán tử nào tính hiệu đối xứng?**

A. `a | b` | `a | b`

B. `a & b` | `a & b`

C. `a ^ b` | `a ^ b`

D. `a.isdisjoint(b)` | `a.isdisjoint(b)`

**Đáp án: C**

**Giải thích:** Hiệu đối xứng giữ phần tử chỉ ở một bên.


**Q8. Which method checks that two sets do not overlap? | Phương thức nào kiểm tra hai Set không trùng nhau?**

A. `a | b` | `a | b`

B. `a & b` | `a & b`

C. `a ^ b` | `a ^ b`

D. `a.isdisjoint(b)` | `a.isdisjoint(b)`

**Đáp án: D**

**Giải thích:** isdisjoint đúng khi phần giao rỗng.


**Q9. Why does inclusion–exclusion subtract an intersection? | Vì sao bao hàm–loại trừ phải trừ phần giao?**

A. To correct double counting | Để sửa việc đếm trùng

B. Distinct elements in either set | Số phần tử khác nhau ở ít nhất một tập

C. When the sets share no members | Khi hai tập không có phần tử chung

D. An ordered List of its elements | List chứa các phần tử được sắp thứ tự

**Đáp án: A**

**Giải thích:** Phần tử giao đã được tính trong cả hai số đếm.


**Q10. What does `len(a | b)` count? | `len(a | b)` đếm gì?**

A. To correct double counting | Để sửa việc đếm trùng

B. Distinct elements in either set | Số phần tử khác nhau ở ít nhất một tập

C. When the sets share no members | Khi hai tập không có phần tử chung

D. An ordered List of its elements | List chứa các phần tử được sắp thứ tự

**Đáp án: B**

**Giải thích:** Hợp tự loại phần trùng của các nhóm.


**Q11. When is `a.isdisjoint(b)` True? | Khi nào `a.isdisjoint(b)` bằng True?**

A. To correct double counting | Để sửa việc đếm trùng

B. Distinct elements in either set | Số phần tử khác nhau ở ít nhất một tập

C. When the sets share no members | Khi hai tập không có phần tử chung

D. An ordered List of its elements | List chứa các phần tử được sắp thứ tự

**Đáp án: C**

**Giải thích:** Hai tập rời có phần giao rỗng.


**Q12. What does `sorted(my_set)` produce? | `sorted(my_set)` tạo gì?**

A. To correct double counting | Để sửa việc đếm trùng

B. Distinct elements in either set | Số phần tử khác nhau ở ít nhất một tập

C. When the sets share no members | Khi hai tập không có phần tử chung

D. An ordered List of its elements | List chứa các phần tử được sắp thứ tự

**Đáp án: D**

**Giải thích:** sorted tạo List và không sửa Set gốc.


**Q13. How many distinct values are in `{1,1,2}`? | `{1,1,2}` có mấy phần tử khác nhau?**

A. 2 | 2

B. 4 | 4

C. Every part is nonempty and the union covers the original set | Mỗi phần không rỗng và hợp phủ đủ tập gốc

D. No element is shared | Không có phần tử chung

**Đáp án: A**

**Giải thích:** Giá trị trùng chỉ xuất hiện một lần trong Set.


**Q14. If |A|=3, |B|=2, |A∩B|=1, what is |A∪B|? | Nếu |A|=3, |B|=2, |A∩B|=1 thì |A∪B| bằng bao nhiêu?**

A. 2 | 2

B. 4 | 4

C. Every part is nonempty and the union covers the original set | Mỗi phần không rỗng và hợp phủ đủ tập gốc

D. No element is shared | Không có phần tử chung

**Đáp án: B**

**Giải thích:** Dùng công thức 3+2−1=4.


**Q15. Which two conditions besides disjointness are needed to verify a nonempty partition? | Ngoài rời nhau, cần kiểm tra gì để xác nhận các phần không rỗng là phân hoạch?**

A. 2 | 2

B. 4 | 4

C. Every part is nonempty and the union covers the original set | Mỗi phần không rỗng và hợp phủ đủ tập gốc

D. No element is shared | Không có phần tử chung

**Đáp án: C**

**Giải thích:** Phân hoạch phải phủ đủ phần tử gốc và không có phần rỗng.


**Q16. What does the empty intersection mean? | Phần giao rỗng nghĩa là gì?**

A. 2 | 2

B. 4 | 4

C. Every part is nonempty and the union covers the original set | Mỗi phần không rỗng và hợp phủ đủ tập gốc

D. No element is shared | Không có phần tử chung

**Đáp án: D**

**Giải thích:** Giao rỗng biểu thị hai tập rời nhau.


**Q17. What does A∪A equal? | A∪A bằng gì?**

A. A | A

B. Empty set | Tập rỗng

C. No fixed order is promised | Không bảo đảm thứ tự cố định

D. Related records or future information may cross splits | Bản ghi liên quan hoặc thông tin tương lai có thể lọt qua hai tập

**Đáp án: A**

**Giải thích:** Hợp một tập với chính nó không thêm phần tử.


**Q18. What does A∩∅ equal? | A∩∅ bằng gì?**

A. A | A

B. Empty set | Tập rỗng

C. No fixed order is promised | Không bảo đảm thứ tự cố định

D. Related records or future information may cross splits | Bản ghi liên quan hoặc thông tin tương lai có thể lọt qua hai tập

**Đáp án: B**

**Giải thích:** Tập rỗng không có phần tử nào chung với A nên phép giao rỗng.


**Q19. Is set iteration order guaranteed? | Thứ tự duyệt Set có được đảm bảo không?**

A. A | A

B. Empty set | Tập rỗng

C. No fixed order is promised | Không bảo đảm thứ tự cố định

D. Related records or future information may cross splits | Bản ghi liên quan hoặc thông tin tương lai có thể lọt qua hai tập

**Đáp án: C**

**Giải thích:** Set Python không phải dãy có thứ tự.


**Q20. Why can two data splits with disjoint IDs still leak information? | Vì sao hai tập dữ liệu không trùng ID vẫn có thể rò rỉ thông tin?**

A. A | A

B. A itself | Chính tập A

C. No fixed order is promised | Không bảo đảm thứ tự cố định

D. Related records or future information may cross splits | Bản ghi liên quan hoặc thông tin tương lai có thể lọt qua hai tập

**Đáp án: D**

**Giải thích:** ID không trùng chưa loại được mọi nguồn rò rỉ.

## 8. Nối sang bài tiếp

`Set → hợp/giao/hiệu → bao hàm–loại trừ → train/test`.

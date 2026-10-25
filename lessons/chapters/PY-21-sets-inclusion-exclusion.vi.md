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

```python
# Mục đích: Ai tham gia ít nhất một nhóm?.
python = {'SV1', 'SV2'}
ai = {'SV2', 'SV3'}
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

```python
# Mục đích: Phần chung và phần riêng.
a = {'SV1', 'SV2'}
b = {'SV2', 'SV3'}
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

```python
# Mục đích: Đếm không lặp người.
a = {'SV1', 'SV2'}
b = {'SV2', 'SV3'}
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

```python
# Mục đích: Chia đủ dữ liệu thành phần rời.
all_ids = {1, 2, 3, 4, 5}
train = {1, 2, 3}
test = {4, 5}
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

**Tình huống thực tế:** Trung tâm nhận **10 lượt đăng ký môn**; mỗi hàng là cặp `(mã học viên, môn)` gồm Python hoặc AI. SV01 và SV05 đăng ký cả hai môn, nên số **lượt** nhiều hơn số **người**. Cần đếm học viên có ít nhất một môn và liệt kê những người có cả hai.

**Vì sao chọn cách này?** Set chỉ lưu mã duy nhất; phép hợp `|` trả mọi học viên thuộc ít nhất một lớp, phép giao `&` tìm người học cả hai. Dùng `sorted` vì Set không có thứ tự hiển thị ổn định.

**Quy trình:**
1. Ghi 10 bản ghi, mỗi bản ghi là một lượt đăng ký.
2. Tạo tập mã học viên Python và AI.
3. Lấy hợp/giao, đối chiếu số người và số lượt.

```python
registrations = [["SV01","Python"],["SV02","AI"],["SV03","Python"],["SV01","AI"],["SV04","AI"],["SV05","Python"],["SV06","AI"],["SV05","AI"],["SV07","Python"],["SV08","AI"]]
python_students = {sid for sid, subject in registrations if subject == "Python"}
ai_students = {sid for sid, subject in registrations if subject == "AI"}
assert len(registrations) == 10
print("Lượt đăng ký:", len(registrations))
print("Học viên duy nhất:", len(python_students | ai_students))
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

**Tình huống thực tế:** Quầy tư vấn nhận **12 lượt đăng ký** giữa Python và AI từ H01…H10. Những người đăng ký cả hai không cần quảng bá môn bổ sung, còn những người **chỉ học đúng một môn** cần được liên hệ. Hãy tìm riêng nhóm chỉ học Python, chỉ học AI và tổng người chỉ có một môn.

**Vì sao chọn cách này?** Hiệu `Python - AI` và `AI - Python` phân biệt hai nhóm không trùng nhau. Hiệu đối xứng `^` trả tổng người chỉ thuộc đúng một Set, không chứa người đăng ký cả hai.

**Quy trình:**
1. Chuyển lượt đăng ký thành tập mã theo từng môn.
2. Tính hiệu từng chiều để biết học viên cần tư vấn môn nào.
3. Tính hiệu đối xứng, đối chiếu tổng hai nhóm.

```python
registrations = [["H01","AI"],["H02","Python"],["H03","AI"],["H04","Python"],["H05","AI"],["H01","Python"],["H06","Python"],["H07","AI"],["H08","Python"],["H09","AI"],["H07","Python"],["H10","Python"]]
pyt = {sid for sid, sub in registrations if sub == "Python"}
ai = {sid for sid, sub in registrations if sub == "AI"}
only_python = sorted(pyt - ai)
only_ai = sorted(ai - pyt)
only_one = pyt ^ ai
assert len(registrations) == 12
print("Lượt:", len(registrations))
print("Chỉ Python:", ", ".join(only_python))
print("Chỉ AI:", ", ".join(only_ai))
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

**Tình huống thực tế:** Một dịch vụ nhận **15 lượt truy cập** từ ứng dụng (`app`) và website (`web`), mỗi hàng lưu mã khách K01…K12 và kênh. Ba khách dùng cả hai kênh. Cần đếm số người không trùng, đồng thời kiểm tra kết quả đếm bằng hai cách.

**Vì sao chọn cách này?** Nếu cộng thẳng số khách của app và web, khách dùng hai kênh bị tính hai lần. Quy tắc bao hàm–loại trừ trừ phần giao, trong khi `len(app | web)` kiểm tra độc lập kết quả.

**Quy trình:**
1. Tạo hai Set khách hàng dựa trên 15 lượt ghi.
2. Đếm khách riêng từng kênh và khách dùng cả hai.
3. Tính số khách duy nhất bằng quy tắc bao hàm–loại trừ, đối chiếu phép hợp.

```python
visits = [["K01","app"],["K02","web"],["K01","web"],["K03","app"],["K04","web"],["K05","app"],["K06","web"],["K07","app"],["K03","web"],["K08","app"],["K09","web"],["K10","app"],["K11","web"],["K12","app"],["K12","web"]]
app = {sid for sid, channel in visits if channel == "app"}
web = {sid for sid, channel in visits if channel == "web"}
via_count = len(app) + len(web) - len(app & web)
assert len(visits) == 15 and via_count == len(app | web)
print("Lượt:", len(visits))
print("Dùng app:", len(app))
print("Dùng web:", len(web))
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

**Tình huống thực tế:** Đội AI có **18 mã mẫu** D01…D18. Dữ liệu phân chia nhầm `D12` vào cả train và test, đồng thời `D18` chưa nằm ở nhóm nào. Cần kiểm tra ba điều kiện của phân hoạch: không có ID trùng, các nhóm phủ toàn bộ tập nguồn và mọi ID đều thuộc nguồn; sau đó chỉ ra mã cần sửa trước khi dùng để học mô hình.

**Vì sao chọn cách này?** Phân hoạch cần **vừa không giao nhau vừa bao phủ nguồn**. Chỉ kiểm tra `isdisjoint()` là chưa đủ, vì tập có thể không trùng nhưng vẫn bỏ sót mẫu.

**Quy trình:**
1. Tạo tập nguồn 18 ID; lưu train/test theo quyết định hiện tại.
2. Tìm ID trùng bằng phép giao và ID thiếu bằng hiệu nguồn với hợp.
3. In các mã cần sửa và kiểm tra phân hoạch đạt/không đạt.

```python
all_ids = ["D01","D02","D03","D04","D05","D06","D07","D08","D09","D10","D11","D12","D13","D14","D15","D16","D17","D18"]
train = set(["D01","D02","D03","D04","D05","D06","D07","D08","D09","D10","D11","D12"])
test = set(["D12","D13","D14","D15","D16","D17"])
source = set(all_ids)
overlap = sorted(train & test)
missing = sorted(source - (train | test))
valid_partition = train.isdisjoint(test) and (train | test) == source
assert len(source) == 18
print("Mẫu nguồn:", len(source))
print("Trùng:", ", ".join(overlap))
print("Chưa phân nhóm:", ", ".join(missing))
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

**Tình huống thực tế:** Hệ thống có **20 dòng ghi nhận học viên** ở ba vùng Bắc/Nam/Trung; mỗi dòng gồm mã học viên, vùng, kênh đăng ký và điểm hoạt động (đơn vị điểm). Hai mã S04 và S07 bị ghi thêm ở vùng khác, nên **20 dòng không tương đương 20 người** và các nhóm vùng không còn là phân hoạch người. Cần phát hiện người xuất hiện nhiều vùng, số người duy nhất và số dòng trùng mã; không tự xóa hồ sơ vì còn phải xác nhận vùng đúng.

**Vì sao chọn cách này?** Set theo vùng gom ID không lặp trong một vùng, sau đó `union` đếm người duy nhất. Duyệt thành viên của hợp để xác định một ID thuộc hơn một vùng; việc xóa tự động có nguy cơ chọn sai vùng.

**Quy trình:**
1. Ghi 20 dòng đầy đủ ID/vùng/kênh/điểm và tạo Set cho từng vùng.
2. Lấy hợp ba vùng để đếm ID duy nhất, kiểm tra giao từng cặp.
3. Liệt kê ID đa vùng và số dòng dư do trùng ID; giữ lại dữ liệu thô để sửa.

```python
records = [{"id":"S01","region":"Bắc","channel":"app","score":10},{"id":"S02","region":"Nam","channel":"web","score":11},{"id":"S03","region":"Trung","channel":"app","score":12},{"id":"S04","region":"Bắc","channel":"web","score":13},{"id":"S05","region":"Nam","channel":"app","score":14},{"id":"S06","region":"Trung","channel":"web","score":15},{"id":"S07","region":"Bắc","channel":"app","score":16},{"id":"S08","region":"Nam","channel":"web","score":17},{"id":"S09","region":"Trung","channel":"app","score":18},{"id":"S10","region":"Bắc","channel":"web","score":19},{"id":"S11","region":"Nam","channel":"app","score":20},{"id":"S12","region":"Trung","channel":"web","score":21},{"id":"S13","region":"Bắc","channel":"app","score":22},{"id":"S14","region":"Nam","channel":"web","score":23},{"id":"S15","region":"Trung","channel":"app","score":24},{"id":"S16","region":"Bắc","channel":"web","score":25},{"id":"S04","region":"Nam","channel":"app","score":26},{"id":"S07","region":"Trung","channel":"web","score":27},{"id":"S19","region":"Bắc","channel":"app","score":28},{"id":"S20","region":"Nam","channel":"web","score":29}]
regions = {name: set() for name in ("Bắc", "Nam", "Trung")}
for row in records:
    regions[row["region"]].add(row["id"])
all_people = set().union(*regions.values())
multiple_regions = sorted(sid for sid in all_people
                          if sum(sid in members for members in regions.values()) > 1)
assert len(records) == 20
print("Dòng nhận:", len(records))
print("Người duy nhất:", len(all_people))
print("Dòng dư do trùng ID:", len(records) - len(all_people))
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

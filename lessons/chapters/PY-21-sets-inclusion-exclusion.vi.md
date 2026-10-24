# PY-21 — Tập hợp, bao hàm–loại trừ và phân hoạch


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Union** — phép hợp; **Intersection** — phép giao.

`Set → hợp/giao/hiệu → bao hàm–loại trừ → train/test`

Bài học giúp sinh viên nhìn rõ quan hệ giữa kiến thức trước và cách xử lý dữ liệu để ứng dụng AI sau này.

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
| `a | b, a & b` | Hợp và giao các tập hợp |
| `a - b, a ^ b` | Hiệu và hiệu đối xứng |
| `len(a | b)` | Đếm phần tử khác nhau |
| `a.isdisjoint(b)` | Kiểm tra hai nhóm có trùng phần tử không |

## 4. Khái niệm liên quan

**Tập hợp** giúp lưu các đối tượng **khác nhau** rồi so sánh thành viên giữa các nhóm. Ta dùng hai lớp học Python và AI làm ví dụ xuyên suốt: phép hợp tìm tất cả học viên, phép giao tìm người học cả hai, quy tắc bao hàm–loại trừ giúp đếm không trùng, còn phân hoạch giúp chia bộ dữ liệu thành các phần rời nhau.

### 4.1. Set và phép hợp — Ai tham gia ít nhất một nhóm?

**Từ vựng trong mục:** **Set** — tập hợp; **Union** — phép hợp.

Set không giữ phần tử trùng. Lớp Python gồm SV1, SV2; lớp AI gồm SV2, SV3. Phép **hợp** `python | ai` chứa tất cả người có mặt trong **ít nhất một** lớp. SV2 nằm ở cả hai nhưng chỉ xuất hiện một lần. Khi cần đầu ra ổn định, dùng `sorted()` vì Set không bảo đảm thứ tự hiển thị.

```python
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
## 5. Năm vấn đề thực tế

### Tình huống 1 — Đếm người học ít nhất một môn

**Từ vựng trong mục:** **Union** — phép hợp.

**Tình huống thực tế:** Một lớp có học viên SV1, SV2, SV3 đăng ký môn Python và SV2, SV4 đăng ký AI. Đếm số học viên học ít nhất một trong hai môn.

**Vì sao chọn cách giải này?** Phép hợp chỉ giữ mỗi mã học viên một lần, đúng yêu cầu đếm người học ít nhất một môn.


**Quy trình giải:**

1. Tạo Set mã người đăng ký Python và Set mã người đăng ký AI.
2. Dùng phép hợp để loại mã xuất hiện trong cả hai nhóm.
3. Dùng `len` đếm số học viên duy nhất.

```python
a = {"SV1", "SV2", "SV3"}
b = {"SV2", "SV4"}
print(len(a|b))
```

**Kết quả khi chạy:**

```text
4
```

### Tình huống 2 — Người học cả hai môn

**Từ vựng trong mục:** **Intersection** — phép giao.

**Tình huống thực tế:** Hai nhóm học viên A gồm SV1, SV2; B gồm SV2, SV3. Tìm mã học viên có mặt ở cả hai nhóm.

**Vì sao chọn cách giải này?** Phép giao trả đúng thành viên có ở cả hai nhóm, không cần duyệt từng mã bằng vòng lặp.


**Quy trình giải:**

1. Lưu danh sách mã của hai nhóm thành Set.
2. Dùng phép giao `&` tìm người có mặt ở cả hai.
3. In kết quả dưới dạng danh sách có thứ tự để dễ đối chiếu.

```python
a = {"SV1", "SV2"}
b = {"SV2", "SV3"}
print(sorted(a & b))
```

**Kết quả khi chạy:**

```text
['SV2']
```

### Tình huống 3 — Kiểm công thức đếm

**Từ vựng trong mục:** **Inclusion–exclusion** — bao hàm–loại trừ.

**Tình huống thực tế:** Hai nhóm mã ID {1,2,3} và {3,4} trùng mã 3. Tính tổng số mã khác nhau và đối chiếu với phép hợp.

**Vì sao chọn cách giải này?** Bao hàm–loại trừ trừ đi phần đã bị tính hai lần và đối chiếu được với phép hợp.


**Quy trình giải:**

1. Xác định số mã trong A, B và phần giao.
2. Tính `len(a) + len(b) - len(a & b)`.
3. So sánh với `len(a | b)` để kiểm chứng hai cách tính.

```python
a = {1, 2, 3}
b = {3, 4}
print(len(a)+len(b)-len(a&b), len(a|b))
```

**Kết quả khi chạy:**

```text
4 4
```

### Tình huống 4 — Chia tập train/test

**Từ vựng trong mục:** **Partition** — phân hoạch.

**Tình huống thực tế:** Đội AI dùng mã dữ liệu {1,2,3} làm tập huấn luyện, {4,5} làm tập kiểm tra. Kiểm tra hai tập có trùng ID không.

**Vì sao chọn cách giải này?** Phân hoạch không chỉ cần hai nhóm không trùng mà còn phải phủ đúng toàn bộ ID nguồn.


**Quy trình giải:**

1. Lưu ID train, ID test và tập ID toàn bộ.
2. Kiểm tra hai nhóm không giao nhau bằng `isdisjoint`.
3. Kiểm tra các ID của train và test gộp lại có đúng tập gốc và không rỗng.

```python
train = {1, 2, 3}
test = {4, 5}
assert train.isdisjoint(test)
print(train.isdisjoint(test) and train | test == True)
```

**Kết quả khi chạy:**

```text
{1, 2, 3, 4, 5}
```

### Tình huống 5 — Tìm sở thích riêng

**Từ vựng trong mục:** **Union** — phép hợp.

**Tình huống thực tế:** Nhóm học Web gồm An, Bình; nhóm học AI gồm Bình, Lan. Tìm học viên chỉ tham gia đúng một trong hai nhóm.

**Vì sao chọn cách giải này?** Hiệu đối xứng trả thành viên chỉ nằm ở một trong hai nhóm; người có mặt cả hai bị loại.


**Quy trình giải:**

1. Lưu danh sách học viên của lớp Web và lớp AI thành hai Set.
2. Lấy hiệu đối xứng `web ^ ai` để bỏ người tham gia cả hai.
3. Sắp xếp và in những người chỉ ở một lớp.

```python
web = {"An", "Binh"}
ai = {"Binh", "Lan"}
print(sorted(web ^ ai))
```

**Kết quả khi chạy:**

```text
['An', 'Lan']
```

## 6. Sai lầm thường gặp

- Set không giữ thứ tự; dùng `sorted()` khi muốn kết quả mẫu có thứ tự ổn định.
- Phép hợp `|` khác phép giao `&`: hợp lấy ít nhất một nhóm, giao lấy cả hai nhóm.
- Hiệu `A - B` khác hiệu đối xứng `A ^ B`: một chiều so với chỉ xuất hiện ở đúng một trong hai tập.
- Bao hàm–loại trừ tránh đếm trùng. Nếu có ba tập trở lên, công thức cần cộng/trừ thêm các giao nhiều tập.
- `isdisjoint()` chỉ chứng minh hai tập không trùng, chưa chứng minh chúng phủ toàn bộ tập gốc.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What does a union contain? — Phép hợp chứa gì?**

A. Elements in at least one set — Phần tử thuộc ít nhất một tập

B. Elements common to both sets — Phần tử có ở cả hai tập

C. Elements in A but not in B — Phần tử thuộc A nhưng không thuộc B

D. Nonempty disjoint parts covering the original set — Các phần không rỗng, rời nhau và phủ đủ tập gốc

**Q2. What does an intersection contain? — Phép giao chứa gì?**

A. Elements in at least one set — Phần tử thuộc ít nhất một tập

B. Elements common to both sets — Phần tử có ở cả hai tập

C. Elements in A but not in B — Phần tử thuộc A nhưng không thuộc B

D. Nonempty disjoint parts covering the original set — Các phần không rỗng, rời nhau và phủ đủ tập gốc

**Q3. What is set difference A−B? — Hiệu tập hợp A−B là gì?**

A. Elements in at least one set — Phần tử thuộc ít nhất một tập

B. Elements common to both sets — Phần tử có ở cả hai tập

C. Elements in A but not in B — Phần tử thuộc A nhưng không thuộc B

D. Nonempty disjoint parts covering the original set — Các phần không rỗng, rời nhau và phủ đủ tập gốc

**Q4. What defines a partition of a set? — Điều gì xác định một phân hoạch?**

A. Elements in at least one set — Phần tử thuộc ít nhất một tập

B. Elements common to both sets — Phần tử có ở cả hai tập

C. Elements in A but not in B — Phần tử thuộc A nhưng không thuộc B

D. Nonempty disjoint parts covering the original set — Các phần không rỗng, rời nhau và phủ đủ tập gốc

**Q5. Which operator computes union for sets? — Toán tử nào tính phép hợp Set?**

A. `a | b` — `a | b`

B. `a & b` — `a & b`

C. `a ^ b` — `a ^ b`

D. `a.isdisjoint(b)` — `a.isdisjoint(b)`

**Q6. Which operator computes intersection? — Toán tử nào tính phép giao?**

A. `a | b` — `a | b`

B. `a & b` — `a & b`

C. `a ^ b` — `a ^ b`

D. `a.isdisjoint(b)` — `a.isdisjoint(b)`

**Q7. Which operator computes symmetric difference? — Toán tử nào tính hiệu đối xứng?**

A. `a | b` — `a | b`

B. `a & b` — `a & b`

C. `a ^ b` — `a ^ b`

D. `a.isdisjoint(b)` — `a.isdisjoint(b)`

**Q8. Which method checks that two sets do not overlap? — Phương thức nào kiểm tra hai Set không trùng nhau?**

A. `a | b` — `a | b`

B. `a & b` — `a & b`

C. `a ^ b` — `a ^ b`

D. `a.isdisjoint(b)` — `a.isdisjoint(b)`

**Q9. Why does inclusion–exclusion subtract an intersection? — Vì sao bao hàm–loại trừ phải trừ phần giao?**

A. To correct double counting — Để sửa việc đếm trùng

B. Distinct elements in either set — Số phần tử khác nhau ở ít nhất một tập

C. When the sets share no members — Khi hai tập không có phần tử chung

D. An ordered List of its elements — List chứa các phần tử được sắp thứ tự

**Q10. What does `len(a | b)` count? — `len(a | b)` đếm gì?**

A. To correct double counting — Để sửa việc đếm trùng

B. Distinct elements in either set — Số phần tử khác nhau ở ít nhất một tập

C. When the sets share no members — Khi hai tập không có phần tử chung

D. An ordered List of its elements — List chứa các phần tử được sắp thứ tự

**Q11. When is `a.isdisjoint(b)` True? — Khi nào `a.isdisjoint(b)` bằng True?**

A. To correct double counting — Để sửa việc đếm trùng

B. Distinct elements in either set — Số phần tử khác nhau ở ít nhất một tập

C. When the sets share no members — Khi hai tập không có phần tử chung

D. An ordered List of its elements — List chứa các phần tử được sắp thứ tự

**Q12. What does `sorted(my_set)` produce? — `sorted(my_set)` tạo gì?**

A. To correct double counting — Để sửa việc đếm trùng

B. Distinct elements in either set — Số phần tử khác nhau ở ít nhất một tập

C. When the sets share no members — Khi hai tập không có phần tử chung

D. An ordered List of its elements — List chứa các phần tử được sắp thứ tự

**Q13. How many distinct values are in `{1,1,2}`? — `{1,1,2}` có mấy phần tử khác nhau?**

A. 2 — 2

B. 4 — 4

C. Every part is nonempty and the union covers the original set — Mỗi phần không rỗng và hợp phủ đủ tập gốc

D. No element is shared — Không có phần tử chung

**Q14. If |A|=3, |B|=2, |A∩B|=1, what is |A∪B|? — Nếu |A|=3, |B|=2, |A∩B|=1 thì |A∪B| bằng bao nhiêu?**

A. 2 — 2

B. 4 — 4

C. Every part is nonempty and the union covers the original set — Mỗi phần không rỗng và hợp phủ đủ tập gốc

D. No element is shared — Không có phần tử chung

**Q15. Which two conditions besides disjointness are needed to verify a nonempty partition? — Ngoài rời nhau, cần kiểm tra gì để xác nhận các phần không rỗng là phân hoạch?**

A. 2 — 2

B. 4 — 4

C. Every part is nonempty and the union covers the original set — Mỗi phần không rỗng và hợp phủ đủ tập gốc

D. No element is shared — Không có phần tử chung

**Q16. What does the empty intersection mean? — Phần giao rỗng nghĩa là gì?**

A. 2 — 2

B. 4 — 4

C. Every part is nonempty and the union covers the original set — Mỗi phần không rỗng và hợp phủ đủ tập gốc

D. No element is shared — Không có phần tử chung

**Q17. What does A∪A equal? — A∪A bằng gì?**

A. A — A

B. Empty set — Tập rỗng

C. No fixed order is promised — Không bảo đảm thứ tự cố định

D. Related records or future information may cross splits — Bản ghi liên quan hoặc thông tin tương lai có thể lọt qua hai tập

**Q18. What does A∩∅ equal? — A∩∅ bằng gì?**

A. A — A

B. Empty set — Tập rỗng

C. No fixed order is promised — Không bảo đảm thứ tự cố định

D. Related records or future information may cross splits — Bản ghi liên quan hoặc thông tin tương lai có thể lọt qua hai tập

**Q19. Is set iteration order guaranteed? — Thứ tự duyệt Set có được đảm bảo không?**

A. A — A

B. Empty set — Tập rỗng

C. No fixed order is promised — Không bảo đảm thứ tự cố định

D. Related records or future information may cross splits — Bản ghi liên quan hoặc thông tin tương lai có thể lọt qua hai tập

**Q20. Why can two data splits with disjoint IDs still leak information? — Vì sao hai tập dữ liệu không trùng ID vẫn có thể rò rỉ thông tin?**

A. A — A

B. A itself — Chính tập A

C. No fixed order is promised — Không bảo đảm thứ tự cố định

D. Related records or future information may cross splits — Bản ghi liên quan hoặc thông tin tương lai có thể lọt qua hai tập

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **A** | Union combines distinct elements of either set. | Hợp chứa các phần tử khác nhau của hai tập. |
| Q2 | **B** | Intersection keeps elements shared by both sets. | Giao chỉ giữ phần tử chung của hai tập. |
| Q3 | **C** | Set difference excludes B's members from A. | Hiệu A−B loại phần tử của B ra khỏi A. |
| Q4 | **D** | All parts must be disjoint and their union the original set. | Mọi phần không giao nhau và hợp bằng tập gốc. |
| Q5 | **A** | The vertical bar denotes set union. | Dấu | là phép hợp tập hợp. |
| Q6 | **B** | The ampersand keeps shared elements. | Dấu & giữ các phần tử chung. |
| Q7 | **C** | Symmetric difference keeps elements exclusive to either side. | Hiệu đối xứng giữ phần tử chỉ ở một bên. |
| Q8 | **D** | isdisjoint is true when the intersection is empty. | isdisjoint đúng khi phần giao rỗng. |
| Q9 | **A** | Intersection elements appear in both individual counts. | Phần tử giao đã được tính trong cả hai số đếm. |
| Q10 | **B** | The union automatically deduplicates overlapping members. | Hợp tự loại phần trùng của các nhóm. |
| Q11 | **C** | Disjoint sets have empty intersection. | Hai tập rời có phần giao rỗng. |
| Q12 | **D** | sorted returns a list without changing the set. | sorted tạo List và không sửa Set gốc. |
| Q13 | **A** | Duplicate values in a set are stored once. | Giá trị trùng chỉ xuất hiện một lần trong Set. |
| Q14 | **B** | Apply 3+2−1 = 4. | Dùng công thức 3+2−1=4. |
| Q15 | **C** | A partition must cover every original element without empty parts. | Phân hoạch phải phủ đủ phần tử gốc và không có phần rỗng. |
| Q16 | **D** | An empty intersection means the sets are disjoint. | Giao rỗng biểu thị hai tập rời nhau. |
| Q17 | **A** | Union with the same set adds nothing new. | Hợp một tập với chính nó không thêm phần tử. |
| Q18 | **B** | The empty set has no members to share in an intersection. | Tập rỗng không có phần tử nào chung với A nên phép giao rỗng. |
| Q19 | **C** | Python sets are not ordered sequences. | Set Python không phải dãy có thứ tự. |
| Q20 | **D** | Disjoint IDs alone do not rule out all leakage. | ID không trùng chưa loại được mọi nguồn rò rỉ. |

## 8. Nối sang bài tiếp

`Set → hợp/giao/hiệu → bao hàm–loại trừ → train/test`.

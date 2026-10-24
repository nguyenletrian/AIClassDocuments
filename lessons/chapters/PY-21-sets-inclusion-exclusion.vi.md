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
a={"SV1","SV2","SV3"}
b={"SV2","SV4"}
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
a={"SV1","SV2"}
b={"SV2","SV3"}
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
a={1,2,3}
b={3,4}
print(len(a)+len(b)-len(a&b),len(a|b))
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
train={1,2,3}
test={4,5}
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
web={"An","Binh"}
ai={"Binh","Lan"}
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


**Q1. What best describes Union? — Mô tả nào đúng với Union?**

A. A different idea is Lấy phần tử có trong cả hai tập — Lấy phần tử có trong cả hai tập

B. It is Lấy tất cả phần tử thuộc ít nhất một tập — Lấy tất cả phần tử thuộc ít nhất một tập

C. A different idea is Cộng từng tập rồi trừ phần giao bị đếm hai lần — Cộng từng tập rồi trừ phần giao bị đếm hai lần

D. A different idea is Chia thành các nhóm rời nhau phủ đủ tập gốc — Chia thành các nhóm rời nhau phủ đủ tập gốc


**Q2. What best describes Intersection? — Mô tả nào đúng với Intersection?**

A. It is Lấy phần tử có trong cả hai tập — Lấy phần tử có trong cả hai tập

B. A different idea is Cộng từng tập rồi trừ phần giao bị đếm hai lần — Cộng từng tập rồi trừ phần giao bị đếm hai lần

C. A different idea is Chia thành các nhóm rời nhau phủ đủ tập gốc — Chia thành các nhóm rời nhau phủ đủ tập gốc

D. A different idea is Lấy tất cả phần tử thuộc ít nhất một tập — Lấy tất cả phần tử thuộc ít nhất một tập


**Q3. What best describes Inclusion–exclusion? — Mô tả nào đúng với Inclusion–exclusion?**

A. A different idea is Chia thành các nhóm rời nhau phủ đủ tập gốc — Chia thành các nhóm rời nhau phủ đủ tập gốc

B. A different idea is Lấy tất cả phần tử thuộc ít nhất một tập — Lấy tất cả phần tử thuộc ít nhất một tập

C. A different idea is Lấy phần tử có trong cả hai tập — Lấy phần tử có trong cả hai tập

D. It is Cộng từng tập rồi trừ phần giao bị đếm hai lần — Cộng từng tập rồi trừ phần giao bị đếm hai lần


**Q4. What best describes Partition? — Mô tả nào đúng với Partition?**

A. A different idea is Lấy tất cả phần tử thuộc ít nhất một tập — Lấy tất cả phần tử thuộc ít nhất một tập

B. A different idea is Lấy phần tử có trong cả hai tập — Lấy phần tử có trong cả hai tập

C. It is Chia thành các nhóm rời nhau phủ đủ tập gốc — Chia thành các nhóm rời nhau phủ đủ tập gốc

D. A different idea is Cộng từng tập rồi trừ phần giao bị đếm hai lần — Cộng từng tập rồi trừ phần giao bị đếm hai lần


**Q5. Which operation matches a | b, a & b? — Mục đích của a | b, a & b là gì?**

A. Another operation is used to Hiệu và hiệu đối xứng — Hiệu và hiệu đối xứng

B. It is used to Hợp và giao các tập hợp — Hợp và giao các tập hợp

C. Another operation is used to Đếm phần tử khác nhau — Đếm phần tử khác nhau

D. Another operation is used to Kiểm tra hai nhóm có trùng phần tử không — Kiểm tra hai nhóm có trùng phần tử không


**Q6. Which operation matches a - b, a ^ b? — Mục đích của a - b, a ^ b là gì?**

A. It is used to Hiệu và hiệu đối xứng — Hiệu và hiệu đối xứng

B. Another operation is used to Đếm phần tử khác nhau — Đếm phần tử khác nhau

C. Another operation is used to Kiểm tra hai nhóm có trùng phần tử không — Kiểm tra hai nhóm có trùng phần tử không

D. Another operation is used to Hợp và giao các tập hợp — Hợp và giao các tập hợp


**Q7. Which operation matches len(a | b)? — Mục đích của len(a | b) là gì?**

A. Another operation is used to Kiểm tra hai nhóm có trùng phần tử không — Kiểm tra hai nhóm có trùng phần tử không

B. Another operation is used to Hợp và giao các tập hợp — Hợp và giao các tập hợp

C. Another operation is used to Hiệu và hiệu đối xứng — Hiệu và hiệu đối xứng

D. It is used to Đếm phần tử khác nhau — Đếm phần tử khác nhau


**Q8. Which operation matches a.isdisjoint(b)? — Mục đích của a.isdisjoint(b) là gì?**

A. Another operation is used to Hợp và giao các tập hợp — Hợp và giao các tập hợp

B. Another operation is used to Hiệu và hiệu đối xứng — Hiệu và hiệu đối xứng

C. It is used to Kiểm tra hai nhóm có trùng phần tử không — Kiểm tra hai nhóm có trùng phần tử không

D. Another operation is used to Đếm phần tử khác nhau — Đếm phần tử khác nhau


**Q9. Why was the method chosen for scenario 1? — Vì sao chọn cách giải của tình huống 1?**

A. Another reason is Phép giao lấy đúng người thuộc hai nhóm — Phép giao lấy đúng người thuộc hai nhóm

B. Because Phép hợp tránh đếm người học cả hai môn hai lần — Phép hợp tránh đếm người học cả hai môn hai lần

C. Another reason is Bao hàm–loại trừ cho kết quả như hợp — Bao hàm–loại trừ cho kết quả như hợp

D. Another reason is Hai nhóm ID đánh giá không trùng nhau — Hai nhóm ID đánh giá không trùng nhau


**Q10. Why was the method chosen for scenario 2? — Vì sao chọn cách giải của tình huống 2?**

A. Because Phép giao lấy đúng người thuộc hai nhóm — Phép giao lấy đúng người thuộc hai nhóm

B. Another reason is Bao hàm–loại trừ cho kết quả như hợp — Bao hàm–loại trừ cho kết quả như hợp

C. Another reason is Hai nhóm ID đánh giá không trùng nhau — Hai nhóm ID đánh giá không trùng nhau

D. Another reason is Hiệu đối xứng lấy người chỉ thuộc một nhóm — Hiệu đối xứng lấy người chỉ thuộc một nhóm


**Q11. Why was the method chosen for scenario 3? — Vì sao chọn cách giải của tình huống 3?**

A. Another reason is Hai nhóm ID đánh giá không trùng nhau — Hai nhóm ID đánh giá không trùng nhau

B. Another reason is Hiệu đối xứng lấy người chỉ thuộc một nhóm — Hiệu đối xứng lấy người chỉ thuộc một nhóm

C. Another reason is Phép hợp tránh đếm người học cả hai môn hai lần — Phép hợp tránh đếm người học cả hai môn hai lần

D. Because Bao hàm–loại trừ cho kết quả như hợp — Bao hàm–loại trừ cho kết quả như hợp


**Q12. Why was the method chosen for scenario 4? — Vì sao chọn cách giải của tình huống 4?**

A. Another reason is Hiệu đối xứng lấy người chỉ thuộc một nhóm — Hiệu đối xứng lấy người chỉ thuộc một nhóm

B. Another reason is Phép hợp tránh đếm người học cả hai môn hai lần — Phép hợp tránh đếm người học cả hai môn hai lần

C. Because Hai nhóm ID đánh giá không trùng nhau — Hai nhóm ID đánh giá không trùng nhau

D. Another reason is Phép giao lấy đúng người thuộc hai nhóm — Phép giao lấy đúng người thuộc hai nhóm


**Q13. Why was the method chosen for scenario 5? — Vì sao chọn cách giải của tình huống 5?**

A. Another reason is Phép hợp tránh đếm người học cả hai môn hai lần — Phép hợp tránh đếm người học cả hai môn hai lần

B. Because Hiệu đối xứng lấy người chỉ thuộc một nhóm — Hiệu đối xứng lấy người chỉ thuộc một nhóm

C. Another reason is Phép giao lấy đúng người thuộc hai nhóm — Phép giao lấy đúng người thuộc hai nhóm

D. Another reason is Bao hàm–loại trừ cho kết quả như hợp — Bao hàm–loại trừ cho kết quả như hợp


**Q14. What input is used in scenario 1? — Tình huống 1 dùng dữ liệu gì?**

A. The data are Nhóm học Python và AI — Nhóm học Python và AI

B. Other data are Nhóm sinh viên hai môn — Nhóm sinh viên hai môn

C. Other data are Hai tập ID có giao — Hai tập ID có giao

D. Other data are train={1,2,3}, test={4,5} — train={1,2,3}, test={4,5}


**Q15. What input is used in scenario 2? — Tình huống 2 dùng dữ liệu gì?**

A. Other data are Hai tập ID có giao — Hai tập ID có giao

B. Other data are train={1,2,3}, test={4,5} — train={1,2,3}, test={4,5}

C. Other data are Hai nhóm Web và AI — Hai nhóm Web và AI

D. The data are Nhóm sinh viên hai môn — Nhóm sinh viên hai môn


**Q16. What input is used in scenario 3? — Tình huống 3 dùng dữ liệu gì?**

A. Other data are train={1,2,3}, test={4,5} — train={1,2,3}, test={4,5}

B. Other data are Hai nhóm Web và AI — Hai nhóm Web và AI

C. The data are Hai tập ID có giao — Hai tập ID có giao

D. Other data are Nhóm học Python và AI — Nhóm học Python và AI


**Q17. What input is used in scenario 4? — Tình huống 4 dùng dữ liệu gì?**

A. Other data are Hai nhóm Web và AI — Hai nhóm Web và AI

B. The data are train={1,2,3}, test={4,5} — train={1,2,3}, test={4,5}

C. Other data are Nhóm học Python và AI — Nhóm học Python và AI

D. Other data are Nhóm sinh viên hai môn — Nhóm sinh viên hai môn


**Q18. What input is used in scenario 5? — Tình huống 5 dùng dữ liệu gì?**

A. The data are Hai nhóm Web và AI — Hai nhóm Web và AI

B. Other data are Nhóm học Python và AI — Nhóm học Python và AI

C. Other data are Nhóm sinh viên hai môn — Nhóm sinh viên hai môn

D. Other data are Hai tập ID có giao — Hai tập ID có giao


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
| Q1 | **B** | It is Lấy tất cả phần tử thuộc ít nhất một tập | Lấy tất cả phần tử thuộc ít nhất một tập |
| Q2 | **A** | It is Lấy phần tử có trong cả hai tập | Lấy phần tử có trong cả hai tập |
| Q3 | **D** | It is Cộng từng tập rồi trừ phần giao bị đếm hai lần | Cộng từng tập rồi trừ phần giao bị đếm hai lần |
| Q4 | **C** | It is Chia thành các nhóm rời nhau phủ đủ tập gốc | Chia thành các nhóm rời nhau phủ đủ tập gốc |
| Q5 | **B** | It is used to Hợp và giao các tập hợp | Hợp và giao các tập hợp |
| Q6 | **A** | It is used to Hiệu và hiệu đối xứng | Hiệu và hiệu đối xứng |
| Q7 | **D** | It is used to Đếm phần tử khác nhau | Đếm phần tử khác nhau |
| Q8 | **C** | It is used to Kiểm tra hai nhóm có trùng phần tử không | Kiểm tra hai nhóm có trùng phần tử không |
| Q9 | **B** | Because Phép hợp tránh đếm người học cả hai môn hai lần | Phép hợp tránh đếm người học cả hai môn hai lần |
| Q10 | **A** | Because Phép giao lấy đúng người thuộc hai nhóm | Phép giao lấy đúng người thuộc hai nhóm |
| Q11 | **D** | Because Bao hàm–loại trừ cho kết quả như hợp | Bao hàm–loại trừ cho kết quả như hợp |
| Q12 | **C** | Because Hai nhóm ID đánh giá không trùng nhau | Hai nhóm ID đánh giá không trùng nhau |
| Q13 | **B** | Because Hiệu đối xứng lấy người chỉ thuộc một nhóm | Hiệu đối xứng lấy người chỉ thuộc một nhóm |
| Q14 | **A** | The data are Nhóm học Python và AI | Nhóm học Python và AI |
| Q15 | **D** | The data are Nhóm sinh viên hai môn | Nhóm sinh viên hai môn |
| Q16 | **C** | The data are Hai tập ID có giao | Hai tập ID có giao |
| Q17 | **B** | The data are train={1,2,3}, test={4,5} | train={1,2,3}, test={4,5} |
| Q18 | **A** | The data are Hai nhóm Web và AI | Hai nhóm Web và AI |
| Q19 | **D** | Meaning of rows, columns and units | Ý nghĩa hàng, cột và đơn vị |
| Q20 | **C** | Check the result and limitations | Kiểm tra kết quả và giới hạn |

## 8. Nối sang bài tiếp

`Set → hợp/giao/hiệu → bao hàm–loại trừ → train/test`.

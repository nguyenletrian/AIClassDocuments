# PY-21 — Tập hợp, bao hàm–loại trừ và phân hoạch

## 1. Vị trí trong chuỗi kiến thức

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

| Hàm / cú pháp | Vì sao dùng |
|---|---|
| `a | b, a & b` | Hợp và giao các tập hợp |
| `a - b, a ^ b` | Hiệu và hiệu đối xứng |
| `len(a | b)` | Đếm phần tử khác nhau |
| `a.isdisjoint(b)` | Kiểm tra hai nhóm có trùng phần tử không |

## 4. Các khái niệm liên quan

### 4.1. Union

Lấy tất cả phần tử thuộc ít nhất một tập. Đọc khái niệm trước rồi kiểm tra bằng ví dụ Python nhỏ.

```python
print({1,2}|{2,3})
```

**Tự kiểm tra nhanh:** Union là gì? **Đáp án:** Lấy tất cả phần tử thuộc ít nhất một tập.

### 4.2. Intersection

Lấy phần tử có trong cả hai tập. Đọc khái niệm trước rồi kiểm tra bằng ví dụ Python nhỏ.

```python
print({1,2}&{2,3})
```

**Tự kiểm tra nhanh:** Intersection là gì? **Đáp án:** Lấy phần tử có trong cả hai tập.

### 4.3. Inclusion–exclusion

Cộng từng tập rồi trừ phần giao bị đếm hai lần. Đọc khái niệm trước rồi kiểm tra bằng ví dụ Python nhỏ.

```python
a={1,2};b={2,3}
print(len(a)+len(b)-len(a&b))
```

**Tự kiểm tra nhanh:** Inclusion–exclusion là gì? **Đáp án:** Cộng từng tập rồi trừ phần giao bị đếm hai lần.

### 4.4. Partition

Chia thành các nhóm rời nhau phủ đủ tập gốc. Đọc khái niệm trước rồi kiểm tra bằng ví dụ Python nhỏ.

```python
train={1,2};test={3}
print(train.isdisjoint(test))
```

**Tự kiểm tra nhanh:** Partition là gì? **Đáp án:** Chia thành các nhóm rời nhau phủ đủ tập gốc.

## 5. Năm vấn đề thực tế

### Tình huống 1 — Đếm người học ít nhất một môn

**Vấn đề:** Đếm người học ít nhất một môn.

**Vì sao chọn phương án này?** Phép hợp tránh đếm người học cả hai môn hai lần. Đừng chọn thuật toán AI khi chỉ cần thống kê hay quy tắc rõ ràng.

**Dữ liệu:** Nhóm học Python và AI. Đầu vào minh họa; nếu dùng bảng, mỗi hàng là một đối tượng và cột là đặc trưng cụ thể.

```python
a={"SV1","SV2","SV3"};b={"SV2","SV4"}
print(len(a|b))
```

### Tình huống 2 — Người học cả hai môn

**Vấn đề:** Người học cả hai môn.

**Vì sao chọn phương án này?** Phép giao lấy đúng người thuộc hai nhóm. Đừng chọn thuật toán AI khi chỉ cần thống kê hay quy tắc rõ ràng.

**Dữ liệu:** Nhóm sinh viên hai môn. Đầu vào minh họa; nếu dùng bảng, mỗi hàng là một đối tượng và cột là đặc trưng cụ thể.

```python
a={"SV1","SV2"};b={"SV2","SV3"}
print(a&b)
```

### Tình huống 3 — Kiểm công thức đếm

**Vấn đề:** Kiểm công thức đếm.

**Vì sao chọn phương án này?** Bao hàm–loại trừ cho kết quả như hợp. Đừng chọn thuật toán AI khi chỉ cần thống kê hay quy tắc rõ ràng.

**Dữ liệu:** Hai tập ID có giao. Đầu vào minh họa; nếu dùng bảng, mỗi hàng là một đối tượng và cột là đặc trưng cụ thể.

```python
a={1,2,3};b={3,4}
print(len(a)+len(b)-len(a&b),len(a|b))
```

### Tình huống 4 — Chia tập train/test

**Vấn đề:** Chia tập train/test.

**Vì sao chọn phương án này?** Hai nhóm ID đánh giá không trùng nhau. Đừng chọn thuật toán AI khi chỉ cần thống kê hay quy tắc rõ ràng.

**Dữ liệu:** train={1,2,3}, test={4,5}. Đầu vào minh họa; nếu dùng bảng, mỗi hàng là một đối tượng và cột là đặc trưng cụ thể.

```python
train={1,2,3};test={4,5}
assert train.isdisjoint(test)
print(train|test)
```

### Tình huống 5 — Tìm sở thích riêng

**Vấn đề:** Tìm sở thích riêng.

**Vì sao chọn phương án này?** Hiệu đối xứng lấy người chỉ thuộc một nhóm. Đừng chọn thuật toán AI khi chỉ cần thống kê hay quy tắc rõ ràng.

**Dữ liệu:** Hai nhóm Web và AI. Đầu vào minh họa; nếu dùng bảng, mỗi hàng là một đối tượng và cột là đặc trưng cụ thể.

```python
web={"An","Binh"};ai={"Binh","Lan"}
print(web^ai)
```

## 6. Các lỗi dễ mắc

Cần phân biệt khi nào thứ tự quan trọng, khi nào phần tử trùng được tính lại, và khi nào dữ liệu thật không có đủ điều kiện như ví dụ. Xem kỹ kiểu dữ liệu và đầu vào trống.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ


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

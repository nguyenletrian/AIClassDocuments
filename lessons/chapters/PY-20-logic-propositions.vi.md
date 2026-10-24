# PY-20 — Logic mệnh đề, bảng chân trị và quy tắc đếm

## 1. Vị trí trong chuỗi kiến thức

`Boolean → logic mệnh đề → tổ hợp → xác suất`

Bài học giúp sinh viên nhìn rõ quan hệ giữa kiến thức trước và cách xử lý dữ liệu để ứng dụng AI sau này.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Giải thích |
|---|---|---|
| Proposition | mệnh đề | Câu có giá trị True hoặc False |
| Truth table | bảng chân trị | Liệt kê kết quả ứng với mọi tổ hợp logic |
| Implication | kéo theo | Quan hệ P⇒Q tương đương (not P) or Q |
| Counting | nguyên lý đếm | Đếm số khả năng khi ghép lựa chọn |

## 3. Hàm Python và tham số

| Hàm / cú pháp | Vì sao dùng |
|---|---|
| `and/or/not` | Ghép điều kiện, chọn ít nhất một hoặc phủ định |
| `(not p) or q` | Biểu diễn phép kéo theo P⇒Q |
| `itertools.product(A,B)` | Tạo tích Descartes của hai tập tùy chọn |
| `math.prod(counts)` | Nhân số lựa chọn từng bước độc lập |

## 4. Các khái niệm liên quan

### 4.1. Proposition

Câu có giá trị True hoặc False. Đọc khái niệm trước rồi kiểm tra bằng ví dụ Python nhỏ.

```python
print(3>1)
```

**Tự kiểm tra nhanh:** Proposition là gì? **Đáp án:** Câu có giá trị True hoặc False.

### 4.2. Truth table

Liệt kê kết quả ứng với mọi tổ hợp logic. Đọc khái niệm trước rồi kiểm tra bằng ví dụ Python nhỏ.

```python
for p in [True,False]:
    print(p,not p)
```

**Tự kiểm tra nhanh:** Truth table là gì? **Đáp án:** Liệt kê kết quả ứng với mọi tổ hợp logic.

### 4.3. Implication

Quan hệ P⇒Q tương đương (not P) or Q. Đọc khái niệm trước rồi kiểm tra bằng ví dụ Python nhỏ.

```python
p,q=True,False
print((not p) or q)
```

**Tự kiểm tra nhanh:** Implication là gì? **Đáp án:** Quan hệ P⇒Q tương đương (not P) or Q.

### 4.4. Counting

Đếm số khả năng khi ghép lựa chọn. Đọc khái niệm trước rồi kiểm tra bằng ví dụ Python nhỏ.

```python
print(3*4)
```

**Tự kiểm tra nhanh:** Counting là gì? **Đáp án:** Đếm số khả năng khi ghép lựa chọn.

## 5. Năm vấn đề thực tế

### Tình huống 1 — Điều kiện đăng nhập

**Vấn đề:** Điều kiện đăng nhập.

**Vì sao chọn phương án này?** Dùng and để đòi cả đăng nhập và xác minh. Đừng chọn thuật toán AI khi chỉ cần thống kê hay quy tắc rõ ràng.

**Dữ liệu:** Hai cờ Boolean. Đầu vào minh họa; nếu dùng bảng, mỗi hàng là một đối tượng và cột là đặc trưng cụ thể.

```python
logged_in,verified=True,False
print(logged_in and verified)
```

### Tình huống 2 — Bảng chân trị

**Vấn đề:** Bảng chân trị.

**Vì sao chọn phương án này?** Quét bốn tổ hợp của hai mệnh đề. Đừng chọn thuật toán AI khi chỉ cần thống kê hay quy tắc rõ ràng.

**Dữ liệu:** P và Q nhận True/False. Đầu vào minh họa; nếu dùng bảng, mỗi hàng là một đối tượng và cột là đặc trưng cụ thể.

```python
for p in [True,False]:
    for q in [True,False]:
        print(p,q,p and q,p or q)
```

### Tình huống 3 — Kiểm quy tắc kéo theo

**Vấn đề:** Kiểm quy tắc kéo theo.

**Vì sao chọn phương án này?** Phép kéo theo chỉ sai khi P đúng nhưng Q sai. Đừng chọn thuật toán AI khi chỉ cần thống kê hay quy tắc rõ ràng.

**Dữ liệu:** P đúng, Q sai. Đầu vào minh họa; nếu dùng bảng, mỗi hàng là một đối tượng và cột là đặc trưng cụ thể.

```python
p,q=True,False
print((not p) or q)
```

### Tình huống 4 — Cấu hình áo

**Vấn đề:** Cấu hình áo.

**Vì sao chọn phương án này?** Nguyên lý nhân đếm số tổ hợp. Đừng chọn thuật toán AI khi chỉ cần thống kê hay quy tắc rõ ràng.

**Dữ liệu:** 3 màu và 4 cỡ áo. Đầu vào minh họa; nếu dùng bảng, mỗi hàng là một đối tượng và cột là đặc trưng cụ thể.

```python
print(3*4)
```

### Tình huống 5 — Ghép các tùy chọn

**Vấn đề:** Ghép các tùy chọn.

**Vì sao chọn phương án này?** product liệt kê từng cặp màu và size. Đừng chọn thuật toán AI khi chỉ cần thống kê hay quy tắc rõ ràng.

**Dữ liệu:** 2 màu và 2 size. Đầu vào minh họa; nếu dùng bảng, mỗi hàng là một đối tượng và cột là đặc trưng cụ thể.

```python
from itertools import product
print(list(product(["red","blue"],["S","M"])))
```

## 6. Các lỗi dễ mắc

Cần phân biệt khi nào thứ tự quan trọng, khi nào phần tử trùng được tính lại, và khi nào dữ liệu thật không có đủ điều kiện như ví dụ. Xem kỹ kiểu dữ liệu và đầu vào trống.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ


**Q1. What best describes Proposition? — Mô tả nào đúng với Proposition?**

A. A different idea is Liệt kê kết quả ứng với mọi tổ hợp logic — Liệt kê kết quả ứng với mọi tổ hợp logic

B. It is Câu có giá trị True hoặc False — Câu có giá trị True hoặc False

C. A different idea is Quan hệ P⇒Q tương đương (not P) or Q — Quan hệ P⇒Q tương đương (not P) or Q

D. A different idea is Đếm số khả năng khi ghép lựa chọn — Đếm số khả năng khi ghép lựa chọn


**Q2. What best describes Truth table? — Mô tả nào đúng với Truth table?**

A. It is Liệt kê kết quả ứng với mọi tổ hợp logic — Liệt kê kết quả ứng với mọi tổ hợp logic

B. A different idea is Quan hệ P⇒Q tương đương (not P) or Q — Quan hệ P⇒Q tương đương (not P) or Q

C. A different idea is Đếm số khả năng khi ghép lựa chọn — Đếm số khả năng khi ghép lựa chọn

D. A different idea is Câu có giá trị True hoặc False — Câu có giá trị True hoặc False


**Q3. What best describes Implication? — Mô tả nào đúng với Implication?**

A. A different idea is Đếm số khả năng khi ghép lựa chọn — Đếm số khả năng khi ghép lựa chọn

B. A different idea is Câu có giá trị True hoặc False — Câu có giá trị True hoặc False

C. A different idea is Liệt kê kết quả ứng với mọi tổ hợp logic — Liệt kê kết quả ứng với mọi tổ hợp logic

D. It is Quan hệ P⇒Q tương đương (not P) or Q — Quan hệ P⇒Q tương đương (not P) or Q


**Q4. What best describes Counting? — Mô tả nào đúng với Counting?**

A. A different idea is Câu có giá trị True hoặc False — Câu có giá trị True hoặc False

B. A different idea is Liệt kê kết quả ứng với mọi tổ hợp logic — Liệt kê kết quả ứng với mọi tổ hợp logic

C. It is Đếm số khả năng khi ghép lựa chọn — Đếm số khả năng khi ghép lựa chọn

D. A different idea is Quan hệ P⇒Q tương đương (not P) or Q — Quan hệ P⇒Q tương đương (not P) or Q


**Q5. Which operation matches and/or/not? — Mục đích của and/or/not là gì?**

A. Another operation is used to Biểu diễn phép kéo theo P⇒Q — Biểu diễn phép kéo theo P⇒Q

B. It is used to Ghép điều kiện, chọn ít nhất một hoặc phủ định — Ghép điều kiện, chọn ít nhất một hoặc phủ định

C. Another operation is used to Tạo tích Descartes của hai tập tùy chọn — Tạo tích Descartes của hai tập tùy chọn

D. Another operation is used to Nhân số lựa chọn từng bước độc lập — Nhân số lựa chọn từng bước độc lập


**Q6. Which operation matches (not p) or q? — Mục đích của (not p) or q là gì?**

A. It is used to Biểu diễn phép kéo theo P⇒Q — Biểu diễn phép kéo theo P⇒Q

B. Another operation is used to Tạo tích Descartes của hai tập tùy chọn — Tạo tích Descartes của hai tập tùy chọn

C. Another operation is used to Nhân số lựa chọn từng bước độc lập — Nhân số lựa chọn từng bước độc lập

D. Another operation is used to Ghép điều kiện, chọn ít nhất một hoặc phủ định — Ghép điều kiện, chọn ít nhất một hoặc phủ định


**Q7. Which operation matches itertools.product(A,B)? — Mục đích của itertools.product(A,B) là gì?**

A. Another operation is used to Nhân số lựa chọn từng bước độc lập — Nhân số lựa chọn từng bước độc lập

B. Another operation is used to Ghép điều kiện, chọn ít nhất một hoặc phủ định — Ghép điều kiện, chọn ít nhất một hoặc phủ định

C. Another operation is used to Biểu diễn phép kéo theo P⇒Q — Biểu diễn phép kéo theo P⇒Q

D. It is used to Tạo tích Descartes của hai tập tùy chọn — Tạo tích Descartes của hai tập tùy chọn


**Q8. Which operation matches math.prod(counts)? — Mục đích của math.prod(counts) là gì?**

A. Another operation is used to Ghép điều kiện, chọn ít nhất một hoặc phủ định — Ghép điều kiện, chọn ít nhất một hoặc phủ định

B. Another operation is used to Biểu diễn phép kéo theo P⇒Q — Biểu diễn phép kéo theo P⇒Q

C. It is used to Nhân số lựa chọn từng bước độc lập — Nhân số lựa chọn từng bước độc lập

D. Another operation is used to Tạo tích Descartes của hai tập tùy chọn — Tạo tích Descartes của hai tập tùy chọn


**Q9. Why was the method chosen for scenario 1? — Vì sao chọn cách giải của tình huống 1?**

A. Another reason is Quét bốn tổ hợp của hai mệnh đề — Quét bốn tổ hợp của hai mệnh đề

B. Because Dùng and để đòi cả đăng nhập và xác minh — Dùng and để đòi cả đăng nhập và xác minh

C. Another reason is Phép kéo theo chỉ sai khi P đúng nhưng Q sai — Phép kéo theo chỉ sai khi P đúng nhưng Q sai

D. Another reason is Nguyên lý nhân đếm số tổ hợp — Nguyên lý nhân đếm số tổ hợp


**Q10. Why was the method chosen for scenario 2? — Vì sao chọn cách giải của tình huống 2?**

A. Because Quét bốn tổ hợp của hai mệnh đề — Quét bốn tổ hợp của hai mệnh đề

B. Another reason is Phép kéo theo chỉ sai khi P đúng nhưng Q sai — Phép kéo theo chỉ sai khi P đúng nhưng Q sai

C. Another reason is Nguyên lý nhân đếm số tổ hợp — Nguyên lý nhân đếm số tổ hợp

D. Another reason is product liệt kê từng cặp màu và size — product liệt kê từng cặp màu và size


**Q11. Why was the method chosen for scenario 3? — Vì sao chọn cách giải của tình huống 3?**

A. Another reason is Nguyên lý nhân đếm số tổ hợp — Nguyên lý nhân đếm số tổ hợp

B. Another reason is product liệt kê từng cặp màu và size — product liệt kê từng cặp màu và size

C. Another reason is Dùng and để đòi cả đăng nhập và xác minh — Dùng and để đòi cả đăng nhập và xác minh

D. Because Phép kéo theo chỉ sai khi P đúng nhưng Q sai — Phép kéo theo chỉ sai khi P đúng nhưng Q sai


**Q12. Why was the method chosen for scenario 4? — Vì sao chọn cách giải của tình huống 4?**

A. Another reason is product liệt kê từng cặp màu và size — product liệt kê từng cặp màu và size

B. Another reason is Dùng and để đòi cả đăng nhập và xác minh — Dùng and để đòi cả đăng nhập và xác minh

C. Because Nguyên lý nhân đếm số tổ hợp — Nguyên lý nhân đếm số tổ hợp

D. Another reason is Quét bốn tổ hợp của hai mệnh đề — Quét bốn tổ hợp của hai mệnh đề


**Q13. Why was the method chosen for scenario 5? — Vì sao chọn cách giải của tình huống 5?**

A. Another reason is Dùng and để đòi cả đăng nhập và xác minh — Dùng and để đòi cả đăng nhập và xác minh

B. Because product liệt kê từng cặp màu và size — product liệt kê từng cặp màu và size

C. Another reason is Quét bốn tổ hợp của hai mệnh đề — Quét bốn tổ hợp của hai mệnh đề

D. Another reason is Phép kéo theo chỉ sai khi P đúng nhưng Q sai — Phép kéo theo chỉ sai khi P đúng nhưng Q sai


**Q14. What input is used in scenario 1? — Tình huống 1 dùng dữ liệu gì?**

A. The data are Hai cờ Boolean — Hai cờ Boolean

B. Other data are P và Q nhận True/False — P và Q nhận True/False

C. Other data are P đúng, Q sai — P đúng, Q sai

D. Other data are 3 màu và 4 cỡ áo — 3 màu và 4 cỡ áo


**Q15. What input is used in scenario 2? — Tình huống 2 dùng dữ liệu gì?**

A. Other data are P đúng, Q sai — P đúng, Q sai

B. Other data are 3 màu và 4 cỡ áo — 3 màu và 4 cỡ áo

C. Other data are 2 màu và 2 size — 2 màu và 2 size

D. The data are P và Q nhận True/False — P và Q nhận True/False


**Q16. What input is used in scenario 3? — Tình huống 3 dùng dữ liệu gì?**

A. Other data are 3 màu và 4 cỡ áo — 3 màu và 4 cỡ áo

B. Other data are 2 màu và 2 size — 2 màu và 2 size

C. The data are P đúng, Q sai — P đúng, Q sai

D. Other data are Hai cờ Boolean — Hai cờ Boolean


**Q17. What input is used in scenario 4? — Tình huống 4 dùng dữ liệu gì?**

A. Other data are 2 màu và 2 size — 2 màu và 2 size

B. The data are 3 màu và 4 cỡ áo — 3 màu và 4 cỡ áo

C. Other data are Hai cờ Boolean — Hai cờ Boolean

D. Other data are P và Q nhận True/False — P và Q nhận True/False


**Q18. What input is used in scenario 5? — Tình huống 5 dùng dữ liệu gì?**

A. The data are 2 màu và 2 size — 2 màu và 2 size

B. Other data are Hai cờ Boolean — Hai cờ Boolean

C. Other data are P và Q nhận True/False — P và Q nhận True/False

D. Other data are P đúng, Q sai — P đúng, Q sai


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
| Q1 | **B** | It is Câu có giá trị True hoặc False | Câu có giá trị True hoặc False |
| Q2 | **A** | It is Liệt kê kết quả ứng với mọi tổ hợp logic | Liệt kê kết quả ứng với mọi tổ hợp logic |
| Q3 | **D** | It is Quan hệ P⇒Q tương đương (not P) or Q | Quan hệ P⇒Q tương đương (not P) or Q |
| Q4 | **C** | It is Đếm số khả năng khi ghép lựa chọn | Đếm số khả năng khi ghép lựa chọn |
| Q5 | **B** | It is used to Ghép điều kiện, chọn ít nhất một hoặc phủ định | Ghép điều kiện, chọn ít nhất một hoặc phủ định |
| Q6 | **A** | It is used to Biểu diễn phép kéo theo P⇒Q | Biểu diễn phép kéo theo P⇒Q |
| Q7 | **D** | It is used to Tạo tích Descartes của hai tập tùy chọn | Tạo tích Descartes của hai tập tùy chọn |
| Q8 | **C** | It is used to Nhân số lựa chọn từng bước độc lập | Nhân số lựa chọn từng bước độc lập |
| Q9 | **B** | Because Dùng and để đòi cả đăng nhập và xác minh | Dùng and để đòi cả đăng nhập và xác minh |
| Q10 | **A** | Because Quét bốn tổ hợp của hai mệnh đề | Quét bốn tổ hợp của hai mệnh đề |
| Q11 | **D** | Because Phép kéo theo chỉ sai khi P đúng nhưng Q sai | Phép kéo theo chỉ sai khi P đúng nhưng Q sai |
| Q12 | **C** | Because Nguyên lý nhân đếm số tổ hợp | Nguyên lý nhân đếm số tổ hợp |
| Q13 | **B** | Because product liệt kê từng cặp màu và size | product liệt kê từng cặp màu và size |
| Q14 | **A** | The data are Hai cờ Boolean | Hai cờ Boolean |
| Q15 | **D** | The data are P và Q nhận True/False | P và Q nhận True/False |
| Q16 | **C** | The data are P đúng, Q sai | P đúng, Q sai |
| Q17 | **B** | The data are 3 màu và 4 cỡ áo | 3 màu và 4 cỡ áo |
| Q18 | **A** | The data are 2 màu và 2 size | 2 màu và 2 size |
| Q19 | **D** | Meaning of rows, columns and units | Ý nghĩa hàng, cột và đơn vị |
| Q20 | **C** | Check the result and limitations | Kiểm tra kết quả và giới hạn |

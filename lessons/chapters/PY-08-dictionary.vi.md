# 08 — Dictionary: key/value và thao tác CRUD

*Trạng thái: DRAFT · Ví dụ giả lập · Cần xác minh thực thi trước khi phát hành*

## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Dictionary** — từ điển; **Key** — khóa.

`List/Set → Dictionary → JSON/CSV → DataFrame`

Từ kiến thức trước, phần này giúp sinh viên quyết định nên tổ chức và xử lý dữ liệu bằng cấu trúc nào, rồi mới tiến tới các bài xử lý dữ liệu cho AI.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Giải thích dễ nhớ |
|---|---|---|
| Dictionary | từ điển | Ánh xạ khóa sang giá trị |
| Key | khóa | Tên hoặc mã để truy tìm giá trị |
| Value | giá trị | Thông tin được lưu theo một khóa |
| Nested dict | từ điển lồng | Một từ điển có từ điển con |

## 3. Hàm và cú pháp Python

**Từ vựng trong mục:** **Function** — hàm; **Argument** — đối số.

| Hàm / cú pháp | Mục đích và lựa chọn liên quan |
|---|---|
| `obj[key], obj.get(key)` | Tra cứu khóa hoặc nhận giá trị mặc định |
| `obj.items(), obj.values()` | Duyệt cặp khóa/giá trị hay riêng giá trị |
| `obj[key] = value` | Thêm hoặc cập nhật dữ liệu |
| `del, pop(key)` | Xóa thông tin bằng khóa |

## 4. Khái niệm liên quan và ví dụ nhỏ

### 4.1. Dictionary

**Từ vựng trong mục:** **Dictionary** — từ điển.

Ánh xạ khóa sang giá trị. Đây là khái niệm cần nắm trước khi áp dụng bước xử lý bên dưới.

```python
print({'id':'O1'})
```

**Tự kiểm tra:** Dictionary có nghĩa gì? **Đáp án:** Ánh xạ khóa sang giá trị.

### 4.2. Key

**Từ vựng trong mục:** **Key** — khóa.

Tên hoặc mã để truy tìm giá trị. Đây là khái niệm cần nắm trước khi áp dụng bước xử lý bên dưới.

```python
print({'id':'O1'}['id'])
```

**Tự kiểm tra:** Key có nghĩa gì? **Đáp án:** Tên hoặc mã để truy tìm giá trị.

### 4.3. Value

**Từ vựng trong mục:** **Value** — giá trị.

Thông tin được lưu theo một khóa. Đây là khái niệm cần nắm trước khi áp dụng bước xử lý bên dưới.

```python
print({'x':5}.get('x'))
```

**Tự kiểm tra:** Value có nghĩa gì? **Đáp án:** Thông tin được lưu theo một khóa.

### 4.4. Nested dict

**Từ vựng trong mục:** **Nested dict** — từ điển lồng.

Một từ điển có từ điển con. Đây là khái niệm cần nắm trước khi áp dụng bước xử lý bên dưới.

```python
print({'A':{'score':8}}['A']['score'])
```

**Tự kiểm tra:** Nested dict có nghĩa gì? **Đáp án:** Một từ điển có từ điển con.

## 5. Năm tình huống lập trình thực tế

### Tình huống 1 — Tra cứu đơn theo mã

**Từ vựng trong mục:** **Dictionary** — từ điển.

**Vấn đề thực tế:** Tra cứu đơn theo mã.

**Vì sao chọn cách này?** Tra khóa trực tiếp thay vì duyệt từng vị trí trong list; không cần công cụ phức tạp hơn khi một quy tắc rõ ràng đã giải được vấn đề.

**Dữ liệu:** Hai đơn O1 và O2; nếu là bảng thì mỗi hàng là một đối tượng và mỗi cột mang một thuộc tính có thứ tự. Các giá trị ở đây đều là ví dụ.

**Quy trình:** Xác định dữ liệu → chọn phép xử lý → chạy code → đọc kết quả và thử trường hợp biên.

```python
orders={"O1":"paid","O2":"pending"}
print(orders.get("O3","Not found"))
```

**Đọc kết quả:** Đối chiếu với giả định đầu vào; đổi dữ liệu và xem kết quả có đúng ý nghĩa không.

### Tình huống 2 — Cập nhật tồn kho

**Từ vựng trong mục:** **Key** — khóa.

**Vấn đề thực tế:** Cập nhật tồn kho.

**Vì sao chọn cách này?** SKU là khóa ổn định phù hợp cập nhật số lượng; không cần công cụ phức tạp hơn khi một quy tắc rõ ràng đã giải được vấn đề.

**Dữ liệu:** SKU01 tồn 5, bán 2; nếu là bảng thì mỗi hàng là một đối tượng và mỗi cột mang một thuộc tính có thứ tự. Các giá trị ở đây đều là ví dụ.

**Quy trình:** Xác định dữ liệu → chọn phép xử lý → chạy code → đọc kết quả và thử trường hợp biên.

```python
stock={"SKU01":5}
stock["SKU01"]-=2
print(stock)
```

**Đọc kết quả:** Đối chiếu với giả định đầu vào; đổi dữ liệu và xem kết quả có đúng ý nghĩa không.

### Tình huống 3 — Đếm nhãn

**Từ vựng trong mục:** **Value** — giá trị.

**Vấn đề thực tế:** Đếm nhãn.

**Vì sao chọn cách này?** get(key,0) giúp cộng dồn an toàn từ 0; không cần công cụ phức tạp hơn khi một quy tắc rõ ràng đã giải được vấn đề.

**Dữ liệu:** Ba nhãn AI Math AI; nếu là bảng thì mỗi hàng là một đối tượng và mỗi cột mang một thuộc tính có thứ tự. Các giá trị ở đây đều là ví dụ.

**Quy trình:** Xác định dữ liệu → chọn phép xử lý → chạy code → đọc kết quả và thử trường hợp biên.

```python
labels=["AI","Math","AI"]
count={}
for x in labels: count[x]=count.get(x,0)+1
print(count)
```

**Đọc kết quả:** Đối chiếu với giả định đầu vào; đổi dữ liệu và xem kết quả có đúng ý nghĩa không.

### Tình huống 4 — Hồ sơ lồng nhau

**Từ vựng trong mục:** **Nested dict** — từ điển lồng.

**Vấn đề thực tế:** Hồ sơ lồng nhau.

**Vì sao chọn cách này?** Từ điển con gom dữ liệu theo từng mã sinh viên; không cần công cụ phức tạp hơn khi một quy tắc rõ ràng đã giải được vấn đề.

**Dữ liệu:** Hai SV với điểm 8 và 9; nếu là bảng thì mỗi hàng là một đối tượng và mỗi cột mang một thuộc tính có thứ tự. Các giá trị ở đây đều là ví dụ.

**Quy trình:** Xác định dữ liệu → chọn phép xử lý → chạy code → đọc kết quả và thử trường hợp biên.

```python
students={"SV1":{"name":"An","score":8},"SV2":{"name":"Lan","score":9}}
print(students["SV2"]["score"])
```

**Đọc kết quả:** Đối chiếu với giả định đầu vào; đổi dữ liệu và xem kết quả có đúng ý nghĩa không.

### Tình huống 5 — Xóa SKU không có

**Từ vựng trong mục:** **Dictionary** — từ điển.

**Vấn đề thực tế:** Xóa SKU không có.

**Vì sao chọn cách này?** pop mặc định None ngăn lỗi khi mã không tồn tại; không cần công cụ phức tạp hơn khi một quy tắc rõ ràng đã giải được vấn đề.

**Dữ liệu:** Danh sách có P01 nhưng không có P02; nếu là bảng thì mỗi hàng là một đối tượng và mỗi cột mang một thuộc tính có thứ tự. Các giá trị ở đây đều là ví dụ.

**Quy trình:** Xác định dữ liệu → chọn phép xử lý → chạy code → đọc kết quả và thử trường hợp biên.

```python
items={"P01":10}
removed=items.pop("P02",None)
print(removed)
```

**Đọc kết quả:** Đối chiếu với giả định đầu vào; đổi dữ liệu và xem kết quả có đúng ý nghĩa không.

## 6. Nhầm lẫn dễ gặp

Không sử dụng cấu trúc dữ liệu sai với mục đích: ví dụ tập hợp không hỗ trợ truy cập theo chỉ số như list; tuple không sửa từng phần tử. Mọi dữ liệu thật cần xác minh kiểu, đơn vị và tính hợp lệ.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is Dictionary? — Thuật ngữ Dictionary có nghĩa gì?**

A. A different concept: Tên hoặc mã để truy tìm giá trị — Tên hoặc mã để truy tìm giá trị

B. A concept described as: Ánh xạ khóa sang giá trị — Ánh xạ khóa sang giá trị

C. A different concept: Thông tin được lưu theo một khóa — Thông tin được lưu theo một khóa

D. A different concept: Một từ điển có từ điển con — Một từ điển có từ điển con


**Q2. What is Key? — Thuật ngữ Key có nghĩa gì?**

A. A concept described as: Tên hoặc mã để truy tìm giá trị — Tên hoặc mã để truy tìm giá trị

B. A different concept: Thông tin được lưu theo một khóa — Thông tin được lưu theo một khóa

C. A different concept: Một từ điển có từ điển con — Một từ điển có từ điển con

D. A different concept: Ánh xạ khóa sang giá trị — Ánh xạ khóa sang giá trị


**Q3. What is Value? — Thuật ngữ Value có nghĩa gì?**

A. A different concept: Một từ điển có từ điển con — Một từ điển có từ điển con

B. A different concept: Ánh xạ khóa sang giá trị — Ánh xạ khóa sang giá trị

C. A different concept: Tên hoặc mã để truy tìm giá trị — Tên hoặc mã để truy tìm giá trị

D. A concept described as: Thông tin được lưu theo một khóa — Thông tin được lưu theo một khóa


**Q4. What is Nested dict? — Thuật ngữ Nested dict có nghĩa gì?**

A. A different concept: Ánh xạ khóa sang giá trị — Ánh xạ khóa sang giá trị

B. A different concept: Tên hoặc mã để truy tìm giá trị — Tên hoặc mã để truy tìm giá trị

C. A concept described as: Một từ điển có từ điển con — Một từ điển có từ điển con

D. A different concept: Thông tin được lưu theo một khóa — Thông tin được lưu theo một khóa


**Q5. Which statement fits 'obj[key], obj.get(key)'? — Mô tả nào đúng với 'obj[key], obj.get(key)'?**

A. It is used for: Duyệt cặp khóa/giá trị hay riêng giá trị — Duyệt cặp khóa/giá trị hay riêng giá trị

B. This syntax is used for: Tra cứu khóa hoặc nhận giá trị mặc định — Tra cứu khóa hoặc nhận giá trị mặc định

C. It is used for: Thêm hoặc cập nhật dữ liệu — Thêm hoặc cập nhật dữ liệu

D. It is used for: Xóa thông tin bằng khóa — Xóa thông tin bằng khóa


**Q6. Which statement fits 'obj.items(), obj.values()'? — Mô tả nào đúng với 'obj.items(), obj.values()'?**

A. This syntax is used for: Duyệt cặp khóa/giá trị hay riêng giá trị — Duyệt cặp khóa/giá trị hay riêng giá trị

B. It is used for: Thêm hoặc cập nhật dữ liệu — Thêm hoặc cập nhật dữ liệu

C. It is used for: Xóa thông tin bằng khóa — Xóa thông tin bằng khóa

D. It is used for: Tra cứu khóa hoặc nhận giá trị mặc định — Tra cứu khóa hoặc nhận giá trị mặc định


**Q7. Which statement fits 'obj[key] = value'? — Mô tả nào đúng với 'obj[key] = value'?**

A. It is used for: Xóa thông tin bằng khóa — Xóa thông tin bằng khóa

B. It is used for: Tra cứu khóa hoặc nhận giá trị mặc định — Tra cứu khóa hoặc nhận giá trị mặc định

C. It is used for: Duyệt cặp khóa/giá trị hay riêng giá trị — Duyệt cặp khóa/giá trị hay riêng giá trị

D. This syntax is used for: Thêm hoặc cập nhật dữ liệu — Thêm hoặc cập nhật dữ liệu


**Q8. Which statement fits 'del, pop(key)'? — Mô tả nào đúng với 'del, pop(key)'?**

A. It is used for: Tra cứu khóa hoặc nhận giá trị mặc định — Tra cứu khóa hoặc nhận giá trị mặc định

B. It is used for: Duyệt cặp khóa/giá trị hay riêng giá trị — Duyệt cặp khóa/giá trị hay riêng giá trị

C. This syntax is used for: Xóa thông tin bằng khóa — Xóa thông tin bằng khóa

D. It is used for: Thêm hoặc cập nhật dữ liệu — Thêm hoặc cập nhật dữ liệu


**Q9. Why use this method in scenario 1? — Vì sao chọn cách này ở tình huống 1?**

A. Because SKU là khóa ổn định phù hợp cập nhật số lượng — SKU là khóa ổn định phù hợp cập nhật số lượng

B. Because Tra khóa trực tiếp thay vì duyệt từng vị trí trong list — Tra khóa trực tiếp thay vì duyệt từng vị trí trong list

C. Because get(key,0) giúp cộng dồn an toàn từ 0 — get(key,0) giúp cộng dồn an toàn từ 0

D. Because Từ điển con gom dữ liệu theo từng mã sinh viên — Từ điển con gom dữ liệu theo từng mã sinh viên


**Q10. Why use this method in scenario 2? — Vì sao chọn cách này ở tình huống 2?**

A. Because SKU là khóa ổn định phù hợp cập nhật số lượng — SKU là khóa ổn định phù hợp cập nhật số lượng

B. Because get(key,0) giúp cộng dồn an toàn từ 0 — get(key,0) giúp cộng dồn an toàn từ 0

C. Because Từ điển con gom dữ liệu theo từng mã sinh viên — Từ điển con gom dữ liệu theo từng mã sinh viên

D. Because pop mặc định None ngăn lỗi khi mã không tồn tại — pop mặc định None ngăn lỗi khi mã không tồn tại


**Q11. Why use this method in scenario 3? — Vì sao chọn cách này ở tình huống 3?**

A. Because Từ điển con gom dữ liệu theo từng mã sinh viên — Từ điển con gom dữ liệu theo từng mã sinh viên

B. Because pop mặc định None ngăn lỗi khi mã không tồn tại — pop mặc định None ngăn lỗi khi mã không tồn tại

C. Because Tra khóa trực tiếp thay vì duyệt từng vị trí trong list — Tra khóa trực tiếp thay vì duyệt từng vị trí trong list

D. Because get(key,0) giúp cộng dồn an toàn từ 0 — get(key,0) giúp cộng dồn an toàn từ 0


**Q12. Why use this method in scenario 4? — Vì sao chọn cách này ở tình huống 4?**

A. Because pop mặc định None ngăn lỗi khi mã không tồn tại — pop mặc định None ngăn lỗi khi mã không tồn tại

B. Because Tra khóa trực tiếp thay vì duyệt từng vị trí trong list — Tra khóa trực tiếp thay vì duyệt từng vị trí trong list

C. Because Từ điển con gom dữ liệu theo từng mã sinh viên — Từ điển con gom dữ liệu theo từng mã sinh viên

D. Because SKU là khóa ổn định phù hợp cập nhật số lượng — SKU là khóa ổn định phù hợp cập nhật số lượng


**Q13. Why use this method in scenario 5? — Vì sao chọn cách này ở tình huống 5?**

A. Because Tra khóa trực tiếp thay vì duyệt từng vị trí trong list — Tra khóa trực tiếp thay vì duyệt từng vị trí trong list

B. Because pop mặc định None ngăn lỗi khi mã không tồn tại — pop mặc định None ngăn lỗi khi mã không tồn tại

C. Because SKU là khóa ổn định phù hợp cập nhật số lượng — SKU là khóa ổn định phù hợp cập nhật số lượng

D. Because get(key,0) giúp cộng dồn an toàn từ 0 — get(key,0) giúp cộng dồn an toàn từ 0


**Q14. What input belongs to scenario 1? — Tình huống 1 sử dụng dữ liệu gì?**

A. The stated input: Hai đơn O1 và O2 — Hai đơn O1 và O2

B. The input is SKU01 tồn 5, bán 2 — SKU01 tồn 5, bán 2

C. The input is Ba nhãn AI Math AI — Ba nhãn AI Math AI

D. The input is Hai SV với điểm 8 và 9 — Hai SV với điểm 8 và 9


**Q15. What input belongs to scenario 2? — Tình huống 2 sử dụng dữ liệu gì?**

A. The input is Ba nhãn AI Math AI — Ba nhãn AI Math AI

B. The input is Hai SV với điểm 8 và 9 — Hai SV với điểm 8 và 9

C. The input is Danh sách có P01 nhưng không có P02 — Danh sách có P01 nhưng không có P02

D. The stated input: SKU01 tồn 5, bán 2 — SKU01 tồn 5, bán 2


**Q16. What input belongs to scenario 3? — Tình huống 3 sử dụng dữ liệu gì?**

A. The input is Hai SV với điểm 8 và 9 — Hai SV với điểm 8 và 9

B. The input is Danh sách có P01 nhưng không có P02 — Danh sách có P01 nhưng không có P02

C. The stated input: Ba nhãn AI Math AI — Ba nhãn AI Math AI

D. The input is Hai đơn O1 và O2 — Hai đơn O1 và O2


**Q17. What input belongs to scenario 4? — Tình huống 4 sử dụng dữ liệu gì?**

A. The input is Danh sách có P01 nhưng không có P02 — Danh sách có P01 nhưng không có P02

B. The stated input: Hai SV với điểm 8 và 9 — Hai SV với điểm 8 và 9

C. The input is Hai đơn O1 và O2 — Hai đơn O1 và O2

D. The input is SKU01 tồn 5, bán 2 — SKU01 tồn 5, bán 2


**Q18. What input belongs to scenario 5? — Tình huống 5 sử dụng dữ liệu gì?**

A. The stated input: Danh sách có P01 nhưng không có P02 — Danh sách có P01 nhưng không có P02

B. The input is Hai đơn O1 và O2 — Hai đơn O1 và O2

C. The input is SKU01 tồn 5, bán 2 — SKU01 tồn 5, bán 2

D. The input is Ba nhãn AI Math AI — Ba nhãn AI Math AI


**Q19. What must be known before processing data? — Cần biết gì trước khi xử lý dữ liệu?**

A. Only file name — Chỉ tên file

B. Only editor theme — Chỉ màu giao diện

C. Only line count — Chỉ số dòng

D. Input meaning, type and units — Ý nghĩa, kiểu và đơn vị đầu vào


**Q20. How should a student check an example? — Nên kiểm tra ví dụ như thế nào?**

A. Assume all inputs work — Cho rằng dữ liệu nào cũng đúng

B. Ignore errors — Bỏ qua lỗi

C. Verify output and edge cases — Đối chiếu kết quả và thử trường hợp biên

D. Delete comments — Xóa chú thích

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **B** | A concept described as: Ánh xạ khóa sang giá trị | Ánh xạ khóa sang giá trị |
| Q2 | **A** | A concept described as: Tên hoặc mã để truy tìm giá trị | Tên hoặc mã để truy tìm giá trị |
| Q3 | **D** | A concept described as: Thông tin được lưu theo một khóa | Thông tin được lưu theo một khóa |
| Q4 | **C** | A concept described as: Một từ điển có từ điển con | Một từ điển có từ điển con |
| Q5 | **B** | This syntax is used for: Tra cứu khóa hoặc nhận giá trị mặc định | Tra cứu khóa hoặc nhận giá trị mặc định |
| Q6 | **A** | This syntax is used for: Duyệt cặp khóa/giá trị hay riêng giá trị | Duyệt cặp khóa/giá trị hay riêng giá trị |
| Q7 | **D** | This syntax is used for: Thêm hoặc cập nhật dữ liệu | Thêm hoặc cập nhật dữ liệu |
| Q8 | **C** | This syntax is used for: Xóa thông tin bằng khóa | Xóa thông tin bằng khóa |
| Q9 | **B** | Because Tra khóa trực tiếp thay vì duyệt từng vị trí trong list | Tra khóa trực tiếp thay vì duyệt từng vị trí trong list |
| Q10 | **A** | Because SKU là khóa ổn định phù hợp cập nhật số lượng | SKU là khóa ổn định phù hợp cập nhật số lượng |
| Q11 | **D** | Because get(key,0) giúp cộng dồn an toàn từ 0 | get(key,0) giúp cộng dồn an toàn từ 0 |
| Q12 | **C** | Because Từ điển con gom dữ liệu theo từng mã sinh viên | Từ điển con gom dữ liệu theo từng mã sinh viên |
| Q13 | **B** | Because pop mặc định None ngăn lỗi khi mã không tồn tại | pop mặc định None ngăn lỗi khi mã không tồn tại |
| Q14 | **A** | The stated input: Hai đơn O1 và O2 | Hai đơn O1 và O2 |
| Q15 | **D** | The stated input: SKU01 tồn 5, bán 2 | SKU01 tồn 5, bán 2 |
| Q16 | **C** | The stated input: Ba nhãn AI Math AI | Ba nhãn AI Math AI |
| Q17 | **B** | The stated input: Hai SV với điểm 8 và 9 | Hai SV với điểm 8 và 9 |
| Q18 | **A** | The stated input: Danh sách có P01 nhưng không có P02 | Danh sách có P01 nhưng không có P02 |
| Q19 | **D** | Input meaning, type and units | Ý nghĩa, kiểu và đơn vị đầu vào |
| Q20 | **C** | Verify output and edge cases | Đối chiếu kết quả và thử trường hợp biên |

## 8. Kết nối bài tiếp theo

`List/Set → Dictionary → JSON/CSV → DataFrame`.

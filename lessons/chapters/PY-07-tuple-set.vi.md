# 07 — Tuple, Set và phép hợp/giao

*Trạng thái: DRAFT · Ví dụ giả lập · Cần xác minh thực thi trước khi phát hành*

## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Tuple** — bộ giá trị; **Set** — tập hợp.

`List → Tuple và Set → Tập hợp/Jaccard`

Từ kiến thức trước, phần này giúp sinh viên quyết định nên tổ chức và xử lý dữ liệu bằng cấu trúc nào, rồi mới tiến tới các bài xử lý dữ liệu cho AI.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Giải thích dễ nhớ |
|---|---|---|
| Tuple | bộ giá trị | Dãy có thứ tự không sửa phần tử được |
| Set | tập hợp | Nhóm phần tử không trùng lặp |
| Union | phép hợp | Mọi phần tử có trong ít nhất một tập |
| Intersection | phép giao | Phần tử chung của hai tập |

## 3. Hàm và cú pháp Python

**Từ vựng trong mục:** **Function** — hàm; **Argument** — đối số.

| Hàm / cú pháp | Mục đích và lựa chọn liên quan |
|---|---|
| `tuple(items)` | Lưu một bộ dữ liệu có thứ tự và cố định |
| `set(items)` | Khử giá trị trùng, không giữ thứ tự đáng tin |
| `a ` |  b, a & b |
| `a - b, a ^ b` | Tìm phần tử còn thiếu hoặc khác nhau |

## 4. Khái niệm liên quan và ví dụ nhỏ

### 4.1. Tuple

**Từ vựng trong mục:** **Tuple** — bộ giá trị.

Dãy có thứ tự không sửa phần tử được. Đây là khái niệm cần nắm trước khi áp dụng bước xử lý bên dưới.

```python
point=(2,3)
print(point)
```

**Tự kiểm tra:** Tuple có nghĩa gì? **Đáp án:** Dãy có thứ tự không sửa phần tử được.

### 4.2. Set

**Từ vựng trong mục:** **Set** — tập hợp.

Nhóm phần tử không trùng lặp. Đây là khái niệm cần nắm trước khi áp dụng bước xử lý bên dưới.

```python
print(set([1,1,2]))
```

**Tự kiểm tra:** Set có nghĩa gì? **Đáp án:** Nhóm phần tử không trùng lặp.

### 4.3. Union

**Từ vựng trong mục:** **Union** — phép hợp.

Mọi phần tử có trong ít nhất một tập. Đây là khái niệm cần nắm trước khi áp dụng bước xử lý bên dưới.

```python
print({1,2}
```

**Tự kiểm tra:** Union có nghĩa gì? **Đáp án:** Mọi phần tử có trong ít nhất một tập.

### 4.4. Intersection

**Từ vựng trong mục:** **Intersection** — phép giao.

Phần tử chung của hai tập. Đây là khái niệm cần nắm trước khi áp dụng bước xử lý bên dưới.

```python
print({1,2}&{2,3})
```

**Tự kiểm tra:** Intersection có nghĩa gì? **Đáp án:** Phần tử chung của hai tập.

## 5. Năm tình huống lập trình thực tế

### Tình huống 1 — Khử email trùng

**Từ vựng trong mục:** **Tuple** — bộ giá trị.

**Vấn đề thực tế:** Khử email trùng.

**Vì sao chọn cách này?** Set loại bản ghi email giống hệt nhau; không cần công cụ phức tạp hơn khi một quy tắc rõ ràng đã giải được vấn đề.

**Dữ liệu:** Bốn email có hai trùng; nếu là bảng thì mỗi hàng là một đối tượng và mỗi cột mang một thuộc tính có thứ tự. Các giá trị ở đây đều là ví dụ.

**Quy trình:** Xác định dữ liệu → chọn phép xử lý → chạy code → đọc kết quả và thử trường hợp biên.

```python
emails=["a@x.vn","b@x.vn","a@x.vn","c@x.vn"]
print(len(set(emails)))
```

**Đọc kết quả:** Đối chiếu với giả định đầu vào; đổi dữ liệu và xem kết quả có đúng ý nghĩa không.

### Tình huống 2 — Lưu tọa độ

**Từ vựng trong mục:** **Set** — tập hợp.

**Vấn đề thực tế:** Lưu tọa độ.

**Vì sao chọn cách này?** Tuple phù hợp điểm cố định (x,y) trong một phép tính; không cần công cụ phức tạp hơn khi một quy tắc rõ ràng đã giải được vấn đề.

**Dữ liệu:** Tọa độ (3,4); nếu là bảng thì mỗi hàng là một đối tượng và mỗi cột mang một thuộc tính có thứ tự. Các giá trị ở đây đều là ví dụ.

**Quy trình:** Xác định dữ liệu → chọn phép xử lý → chạy code → đọc kết quả và thử trường hợp biên.

```python
point=(3,4)
x,y=point
print(x*x+y*y)
```

**Đọc kết quả:** Đối chiếu với giả định đầu vào; đổi dữ liệu và xem kết quả có đúng ý nghĩa không.

### Tình huống 3 — Tìm kỹ năng chung

**Từ vựng trong mục:** **Union** — phép hợp.

**Vấn đề thực tế:** Tìm kỹ năng chung.

**Vì sao chọn cách này?** Phép giao cho biết kỹ năng cả hai cùng có; không cần công cụ phức tạp hơn khi một quy tắc rõ ràng đã giải được vấn đề.

**Dữ liệu:** Hai danh sách kỹ năng; nếu là bảng thì mỗi hàng là một đối tượng và mỗi cột mang một thuộc tính có thứ tự. Các giá trị ở đây đều là ví dụ.

**Quy trình:** Xác định dữ liệu → chọn phép xử lý → chạy code → đọc kết quả và thử trường hợp biên.

```python
a={"Python","AI","SQL"}
b={"Python","Math","AI"}
print(a&b)
```

**Đọc kết quả:** Đối chiếu với giả định đầu vào; đổi dữ liệu và xem kết quả có đúng ý nghĩa không.

### Tình huống 4 — Gộp nhóm chủ đề

**Từ vựng trong mục:** **Intersection** — phép giao.

**Vấn đề thực tế:** Gộp nhóm chủ đề.

**Vì sao chọn cách này?** Phép hợp giữ mỗi chủ đề một lần; không cần công cụ phức tạp hơn khi một quy tắc rõ ràng đã giải được vấn đề.

**Dữ liệu:** Hai nhóm nhãn tài liệu; nếu là bảng thì mỗi hàng là một đối tượng và mỗi cột mang một thuộc tính có thứ tự. Các giá trị ở đây đều là ví dụ.

**Quy trình:** Xác định dữ liệu → chọn phép xử lý → chạy code → đọc kết quả và thử trường hợp biên.

```python
a={"Python","Math"}
b={"Math","AI"}
print(a|b)
```

**Đọc kết quả:** Đối chiếu với giả định đầu vào; đổi dữ liệu và xem kết quả có đúng ý nghĩa không.

### Tình huống 5 — Liệt kê bài còn thiếu

**Từ vựng trong mục:** **Tuple** — bộ giá trị.

**Vấn đề thực tế:** Liệt kê bài còn thiếu.

**Vì sao chọn cách này?** Hiệu tập cho ra mục cần học nhưng chưa hoàn thành; không cần công cụ phức tạp hơn khi một quy tắc rõ ràng đã giải được vấn đề.

**Dữ liệu:** Yêu cầu Python SQL AI, đã học Python; nếu là bảng thì mỗi hàng là một đối tượng và mỗi cột mang một thuộc tính có thứ tự. Các giá trị ở đây đều là ví dụ.

**Quy trình:** Xác định dữ liệu → chọn phép xử lý → chạy code → đọc kết quả và thử trường hợp biên.

```python
required={"Python","SQL","AI"}
done={"Python"}
print(required-done)
```

**Đọc kết quả:** Đối chiếu với giả định đầu vào; đổi dữ liệu và xem kết quả có đúng ý nghĩa không.

## 6. Nhầm lẫn dễ gặp

Không sử dụng cấu trúc dữ liệu sai với mục đích: ví dụ tập hợp không hỗ trợ truy cập theo chỉ số như list; tuple không sửa từng phần tử. Mọi dữ liệu thật cần xác minh kiểu, đơn vị và tính hợp lệ.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is Tuple? — Thuật ngữ Tuple có nghĩa gì?**

A. A different concept: Nhóm phần tử không trùng lặp — Nhóm phần tử không trùng lặp

B. A concept described as: Dãy có thứ tự không sửa phần tử được — Dãy có thứ tự không sửa phần tử được

C. A different concept: Mọi phần tử có trong ít nhất một tập — Mọi phần tử có trong ít nhất một tập

D. A different concept: Phần tử chung của hai tập — Phần tử chung của hai tập


**Q2. What is Set? — Thuật ngữ Set có nghĩa gì?**

A. A concept described as: Nhóm phần tử không trùng lặp — Nhóm phần tử không trùng lặp

B. A different concept: Mọi phần tử có trong ít nhất một tập — Mọi phần tử có trong ít nhất một tập

C. A different concept: Phần tử chung của hai tập — Phần tử chung của hai tập

D. A different concept: Dãy có thứ tự không sửa phần tử được — Dãy có thứ tự không sửa phần tử được


**Q3. What is Union? — Thuật ngữ Union có nghĩa gì?**

A. A different concept: Phần tử chung của hai tập — Phần tử chung của hai tập

B. A different concept: Dãy có thứ tự không sửa phần tử được — Dãy có thứ tự không sửa phần tử được

C. A different concept: Nhóm phần tử không trùng lặp — Nhóm phần tử không trùng lặp

D. A concept described as: Mọi phần tử có trong ít nhất một tập — Mọi phần tử có trong ít nhất một tập


**Q4. What is Intersection? — Thuật ngữ Intersection có nghĩa gì?**

A. A different concept: Dãy có thứ tự không sửa phần tử được — Dãy có thứ tự không sửa phần tử được

B. A different concept: Nhóm phần tử không trùng lặp — Nhóm phần tử không trùng lặp

C. A concept described as: Phần tử chung của hai tập — Phần tử chung của hai tập

D. A different concept: Mọi phần tử có trong ít nhất một tập — Mọi phần tử có trong ít nhất một tập


**Q5. Which statement fits 'tuple(items)'? — Mô tả nào đúng với 'tuple(items)'?**

A. It is used for: Khử giá trị trùng, không giữ thứ tự đáng tin — Khử giá trị trùng, không giữ thứ tự đáng tin

B. This syntax is used for: Lưu một bộ dữ liệu có thứ tự và cố định — Lưu một bộ dữ liệu có thứ tự và cố định

C. It is used for:  b, a & b —  b, a & b

D. It is used for: Tìm phần tử còn thiếu hoặc khác nhau — Tìm phần tử còn thiếu hoặc khác nhau


**Q6. Which statement fits 'set(items)'? — Mô tả nào đúng với 'set(items)'?**

A. This syntax is used for: Khử giá trị trùng, không giữ thứ tự đáng tin — Khử giá trị trùng, không giữ thứ tự đáng tin

B. It is used for:  b, a & b —  b, a & b

C. It is used for: Tìm phần tử còn thiếu hoặc khác nhau — Tìm phần tử còn thiếu hoặc khác nhau

D. It is used for: Lưu một bộ dữ liệu có thứ tự và cố định — Lưu một bộ dữ liệu có thứ tự và cố định


**Q7. Which statement fits 'a '? — Mô tả nào đúng với 'a '?**

A. It is used for: Tìm phần tử còn thiếu hoặc khác nhau — Tìm phần tử còn thiếu hoặc khác nhau

B. It is used for: Lưu một bộ dữ liệu có thứ tự và cố định — Lưu một bộ dữ liệu có thứ tự và cố định

C. It is used for: Khử giá trị trùng, không giữ thứ tự đáng tin — Khử giá trị trùng, không giữ thứ tự đáng tin

D. This syntax is used for:  b, a & b —  b, a & b


**Q8. Which statement fits 'a - b, a ^ b'? — Mô tả nào đúng với 'a - b, a ^ b'?**

A. It is used for: Lưu một bộ dữ liệu có thứ tự và cố định — Lưu một bộ dữ liệu có thứ tự và cố định

B. It is used for: Khử giá trị trùng, không giữ thứ tự đáng tin — Khử giá trị trùng, không giữ thứ tự đáng tin

C. This syntax is used for: Tìm phần tử còn thiếu hoặc khác nhau — Tìm phần tử còn thiếu hoặc khác nhau

D. It is used for:  b, a & b —  b, a & b


**Q9. Why use this method in scenario 1? — Vì sao chọn cách này ở tình huống 1?**

A. Because Tuple phù hợp điểm cố định (x,y) trong một phép tính — Tuple phù hợp điểm cố định (x,y) trong một phép tính

B. Because Set loại bản ghi email giống hệt nhau — Set loại bản ghi email giống hệt nhau

C. Because Phép giao cho biết kỹ năng cả hai cùng có — Phép giao cho biết kỹ năng cả hai cùng có

D. Because Phép hợp giữ mỗi chủ đề một lần — Phép hợp giữ mỗi chủ đề một lần


**Q10. Why use this method in scenario 2? — Vì sao chọn cách này ở tình huống 2?**

A. Because Tuple phù hợp điểm cố định (x,y) trong một phép tính — Tuple phù hợp điểm cố định (x,y) trong một phép tính

B. Because Phép giao cho biết kỹ năng cả hai cùng có — Phép giao cho biết kỹ năng cả hai cùng có

C. Because Phép hợp giữ mỗi chủ đề một lần — Phép hợp giữ mỗi chủ đề một lần

D. Because Hiệu tập cho ra mục cần học nhưng chưa hoàn thành — Hiệu tập cho ra mục cần học nhưng chưa hoàn thành


**Q11. Why use this method in scenario 3? — Vì sao chọn cách này ở tình huống 3?**

A. Because Phép hợp giữ mỗi chủ đề một lần — Phép hợp giữ mỗi chủ đề một lần

B. Because Hiệu tập cho ra mục cần học nhưng chưa hoàn thành — Hiệu tập cho ra mục cần học nhưng chưa hoàn thành

C. Because Set loại bản ghi email giống hệt nhau — Set loại bản ghi email giống hệt nhau

D. Because Phép giao cho biết kỹ năng cả hai cùng có — Phép giao cho biết kỹ năng cả hai cùng có


**Q12. Why use this method in scenario 4? — Vì sao chọn cách này ở tình huống 4?**

A. Because Hiệu tập cho ra mục cần học nhưng chưa hoàn thành — Hiệu tập cho ra mục cần học nhưng chưa hoàn thành

B. Because Set loại bản ghi email giống hệt nhau — Set loại bản ghi email giống hệt nhau

C. Because Phép hợp giữ mỗi chủ đề một lần — Phép hợp giữ mỗi chủ đề một lần

D. Because Tuple phù hợp điểm cố định (x,y) trong một phép tính — Tuple phù hợp điểm cố định (x,y) trong một phép tính


**Q13. Why use this method in scenario 5? — Vì sao chọn cách này ở tình huống 5?**

A. Because Set loại bản ghi email giống hệt nhau — Set loại bản ghi email giống hệt nhau

B. Because Hiệu tập cho ra mục cần học nhưng chưa hoàn thành — Hiệu tập cho ra mục cần học nhưng chưa hoàn thành

C. Because Tuple phù hợp điểm cố định (x,y) trong một phép tính — Tuple phù hợp điểm cố định (x,y) trong một phép tính

D. Because Phép giao cho biết kỹ năng cả hai cùng có — Phép giao cho biết kỹ năng cả hai cùng có


**Q14. What input belongs to scenario 1? — Tình huống 1 sử dụng dữ liệu gì?**

A. The stated input: Bốn email có hai trùng — Bốn email có hai trùng

B. The input is Tọa độ (3,4) — Tọa độ (3,4)

C. The input is Hai danh sách kỹ năng — Hai danh sách kỹ năng

D. The input is Hai nhóm nhãn tài liệu — Hai nhóm nhãn tài liệu


**Q15. What input belongs to scenario 2? — Tình huống 2 sử dụng dữ liệu gì?**

A. The input is Hai danh sách kỹ năng — Hai danh sách kỹ năng

B. The input is Hai nhóm nhãn tài liệu — Hai nhóm nhãn tài liệu

C. The input is Yêu cầu Python SQL AI, đã học Python — Yêu cầu Python SQL AI, đã học Python

D. The stated input: Tọa độ (3,4) — Tọa độ (3,4)


**Q16. What input belongs to scenario 3? — Tình huống 3 sử dụng dữ liệu gì?**

A. The input is Hai nhóm nhãn tài liệu — Hai nhóm nhãn tài liệu

B. The input is Yêu cầu Python SQL AI, đã học Python — Yêu cầu Python SQL AI, đã học Python

C. The stated input: Hai danh sách kỹ năng — Hai danh sách kỹ năng

D. The input is Bốn email có hai trùng — Bốn email có hai trùng


**Q17. What input belongs to scenario 4? — Tình huống 4 sử dụng dữ liệu gì?**

A. The input is Yêu cầu Python SQL AI, đã học Python — Yêu cầu Python SQL AI, đã học Python

B. The stated input: Hai nhóm nhãn tài liệu — Hai nhóm nhãn tài liệu

C. The input is Bốn email có hai trùng — Bốn email có hai trùng

D. The input is Tọa độ (3,4) — Tọa độ (3,4)


**Q18. What input belongs to scenario 5? — Tình huống 5 sử dụng dữ liệu gì?**

A. The stated input: Yêu cầu Python SQL AI, đã học Python — Yêu cầu Python SQL AI, đã học Python

B. The input is Bốn email có hai trùng — Bốn email có hai trùng

C. The input is Tọa độ (3,4) — Tọa độ (3,4)

D. The input is Hai danh sách kỹ năng — Hai danh sách kỹ năng


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
| Q1 | **B** | A concept described as: Dãy có thứ tự không sửa phần tử được | Dãy có thứ tự không sửa phần tử được |
| Q2 | **A** | A concept described as: Nhóm phần tử không trùng lặp | Nhóm phần tử không trùng lặp |
| Q3 | **D** | A concept described as: Mọi phần tử có trong ít nhất một tập | Mọi phần tử có trong ít nhất một tập |
| Q4 | **C** | A concept described as: Phần tử chung của hai tập | Phần tử chung của hai tập |
| Q5 | **B** | This syntax is used for: Lưu một bộ dữ liệu có thứ tự và cố định | Lưu một bộ dữ liệu có thứ tự và cố định |
| Q6 | **A** | This syntax is used for: Khử giá trị trùng, không giữ thứ tự đáng tin | Khử giá trị trùng, không giữ thứ tự đáng tin |
| Q7 | **D** | This syntax is used for:  b, a & b |  b, a & b |
| Q8 | **C** | This syntax is used for: Tìm phần tử còn thiếu hoặc khác nhau | Tìm phần tử còn thiếu hoặc khác nhau |
| Q9 | **B** | Because Set loại bản ghi email giống hệt nhau | Set loại bản ghi email giống hệt nhau |
| Q10 | **A** | Because Tuple phù hợp điểm cố định (x,y) trong một phép tính | Tuple phù hợp điểm cố định (x,y) trong một phép tính |
| Q11 | **D** | Because Phép giao cho biết kỹ năng cả hai cùng có | Phép giao cho biết kỹ năng cả hai cùng có |
| Q12 | **C** | Because Phép hợp giữ mỗi chủ đề một lần | Phép hợp giữ mỗi chủ đề một lần |
| Q13 | **B** | Because Hiệu tập cho ra mục cần học nhưng chưa hoàn thành | Hiệu tập cho ra mục cần học nhưng chưa hoàn thành |
| Q14 | **A** | The stated input: Bốn email có hai trùng | Bốn email có hai trùng |
| Q15 | **D** | The stated input: Tọa độ (3,4) | Tọa độ (3,4) |
| Q16 | **C** | The stated input: Hai danh sách kỹ năng | Hai danh sách kỹ năng |
| Q17 | **B** | The stated input: Hai nhóm nhãn tài liệu | Hai nhóm nhãn tài liệu |
| Q18 | **A** | The stated input: Yêu cầu Python SQL AI, đã học Python | Yêu cầu Python SQL AI, đã học Python |
| Q19 | **D** | Input meaning, type and units | Ý nghĩa, kiểu và đơn vị đầu vào |
| Q20 | **C** | Verify output and edge cases | Đối chiếu kết quả và thử trường hợp biên |

## 8. Kết nối bài tiếp theo

`List → Tuple và Set → Tập hợp/Jaccard`.

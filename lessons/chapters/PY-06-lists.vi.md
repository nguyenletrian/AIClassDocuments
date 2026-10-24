# 06 — List, chỉ số, slicing và sắp xếp

*Trạng thái: DRAFT · Ví dụ giả lập · Cần xác minh thực thi trước khi phát hành*

## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **List** — danh sách; **Index** — chỉ số.

`Vòng lặp → List → Vector/Array`

Từ kiến thức trước, phần này giúp sinh viên quyết định nên tổ chức và xử lý dữ liệu bằng cấu trúc nào, rồi mới tiến tới các bài xử lý dữ liệu cho AI.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Giải thích dễ nhớ |
|---|---|---|
| List | danh sách | Tập hợp có thứ tự, có thể thay đổi |
| Index | chỉ số | Vị trí tính từ 0 để lấy phần tử |
| Slice | cắt lát | Lấy đoạn phần tử theo start:stop |
| Mutability | khả năng sửa | Có thể cập nhật phần tử của danh sách |

## 3. Hàm và cú pháp Python

**Từ vựng trong mục:** **Function** — hàm; **Argument** — đối số.

| Hàm / cú pháp | Mục đích và lựa chọn liên quan |
|---|---|
| `append(), extend(), insert()` | Thêm từng phần tử hoặc nhiều phần tử vào danh sách |
| `pop(), remove(), del` | Xóa theo vị trí hoặc giá trị |
| `sort(), sorted()` | Sắp xếp tại chỗ hoặc tạo danh sách mới |
| `items[start:stop]` | Lấy vùng con không bao gồm stop |

## 4. Khái niệm liên quan và ví dụ nhỏ

### 4.1. List

**Từ vựng trong mục:** **List** — danh sách.

Tập hợp có thứ tự, có thể thay đổi. Đây là khái niệm cần nắm trước khi áp dụng bước xử lý bên dưới.

```python
a=[1,2]
print(a)
```

**Tự kiểm tra:** List có nghĩa gì? **Đáp án:** Tập hợp có thứ tự, có thể thay đổi.

### 4.2. Index

**Từ vựng trong mục:** **Index** — chỉ số.

Vị trí tính từ 0 để lấy phần tử. Đây là khái niệm cần nắm trước khi áp dụng bước xử lý bên dưới.

```python
print([8,9][0])
```

**Tự kiểm tra:** Index có nghĩa gì? **Đáp án:** Vị trí tính từ 0 để lấy phần tử.

### 4.3. Slice

**Từ vựng trong mục:** **Slice** — cắt lát.

Lấy đoạn phần tử theo start:stop. Đây là khái niệm cần nắm trước khi áp dụng bước xử lý bên dưới.

```python
print([1,2,3][:2])
```

**Tự kiểm tra:** Slice có nghĩa gì? **Đáp án:** Lấy đoạn phần tử theo start:stop.

### 4.4. Mutability

**Từ vựng trong mục:** **Mutability** — khả năng sửa.

Có thể cập nhật phần tử của danh sách. Đây là khái niệm cần nắm trước khi áp dụng bước xử lý bên dưới.

```python
a=[1,2]
a[1]=5
print(a)
```

**Tự kiểm tra:** Mutability có nghĩa gì? **Đáp án:** Có thể cập nhật phần tử của danh sách.

## 5. Năm tình huống lập trình thực tế

### Tình huống 1 — Giỏ hàng

**Từ vựng trong mục:** **List** — danh sách.

**Vấn đề thực tế:** Giỏ hàng.

**Vì sao chọn cách này?** Thêm món mới vào danh sách thứ tự đã chọn; không cần công cụ phức tạp hơn khi một quy tắc rõ ràng đã giải được vấn đề.

**Dữ liệu:** Hai món ban đầu; nếu là bảng thì mỗi hàng là một đối tượng và mỗi cột mang một thuộc tính có thứ tự. Các giá trị ở đây đều là ví dụ.

**Quy trình:** Xác định dữ liệu → chọn phép xử lý → chạy code → đọc kết quả và thử trường hợp biên.

```python
basket=["milk","bread"]
basket.append("rice")
print(basket)
```

**Đọc kết quả:** Đối chiếu với giả định đầu vào; đổi dữ liệu và xem kết quả có đúng ý nghĩa không.

### Tình huống 2 — Lấy hai ưu tiên cao

**Từ vựng trong mục:** **Index** — chỉ số.

**Vấn đề thực tế:** Lấy hai ưu tiên cao.

**Vì sao chọn cách này?** Sắp xếp bản sao giữ thứ tự gốc để còn so sánh; không cần công cụ phức tạp hơn khi một quy tắc rõ ràng đã giải được vấn đề.

**Dữ liệu:** Điểm ưu tiên [2,9,4,7]; nếu là bảng thì mỗi hàng là một đối tượng và mỗi cột mang một thuộc tính có thứ tự. Các giá trị ở đây đều là ví dụ.

**Quy trình:** Xác định dữ liệu → chọn phép xử lý → chạy code → đọc kết quả và thử trường hợp biên.

```python
scores=[2,9,4,7]
print(sorted(scores,reverse=True)[:2])
```

**Đọc kết quả:** Đối chiếu với giả định đầu vào; đổi dữ liệu và xem kết quả có đúng ý nghĩa không.

### Tình huống 3 — Lọc điểm đạt

**Từ vựng trong mục:** **Slice** — cắt lát.

**Vấn đề thực tế:** Lọc điểm đạt.

**Vì sao chọn cách này?** Chọn điểm >=5 bằng điều kiện trong list comprehension; không cần công cụ phức tạp hơn khi một quy tắc rõ ràng đã giải được vấn đề.

**Dữ liệu:** 4 điểm thang 10; nếu là bảng thì mỗi hàng là một đối tượng và mỗi cột mang một thuộc tính có thứ tự. Các giá trị ở đây đều là ví dụ.

**Quy trình:** Xác định dữ liệu → chọn phép xử lý → chạy code → đọc kết quả và thử trường hợp biên.

```python
scores=[4,7,9,3]
passed=[x for x in scores if x>=5]
print(passed)
```

**Đọc kết quả:** Đối chiếu với giả định đầu vào; đổi dữ liệu và xem kết quả có đúng ý nghĩa không.

### Tình huống 4 — Sửa tồn kho

**Từ vựng trong mục:** **Mutability** — khả năng sửa.

**Vấn đề thực tế:** Sửa tồn kho.

**Vì sao chọn cách này?** Sửa trực tiếp phần tử thứ hai khi kiểm đếm sai; không cần công cụ phức tạp hơn khi một quy tắc rõ ràng đã giải được vấn đề.

**Dữ liệu:** Tồn 3 mặt hàng; nếu là bảng thì mỗi hàng là một đối tượng và mỗi cột mang một thuộc tính có thứ tự. Các giá trị ở đây đều là ví dụ.

**Quy trình:** Xác định dữ liệu → chọn phép xử lý → chạy code → đọc kết quả và thử trường hợp biên.

```python
stock=[8,6,9]
stock[1]=4
print(stock)
```

**Đọc kết quả:** Đối chiếu với giả định đầu vào; đổi dữ liệu và xem kết quả có đúng ý nghĩa không.

### Tình huống 5 — Hàng đợi yêu cầu

**Từ vựng trong mục:** **List** — danh sách.

**Vấn đề thực tế:** Hàng đợi yêu cầu.

**Vì sao chọn cách này?** Lấy yêu cầu đầu tiên và xóa nó khỏi danh sách; không cần công cụ phức tạp hơn khi một quy tắc rõ ràng đã giải được vấn đề.

**Dữ liệu:** 3 mã yêu cầu; nếu là bảng thì mỗi hàng là một đối tượng và mỗi cột mang một thuộc tính có thứ tự. Các giá trị ở đây đều là ví dụ.

**Quy trình:** Xác định dữ liệu → chọn phép xử lý → chạy code → đọc kết quả và thử trường hợp biên.

```python
queue=["REQ01","REQ02","REQ03"]
done=queue.pop(0)
print(done,queue)
```

**Đọc kết quả:** Đối chiếu với giả định đầu vào; đổi dữ liệu và xem kết quả có đúng ý nghĩa không.

## 6. Nhầm lẫn dễ gặp

Không sử dụng cấu trúc dữ liệu sai với mục đích: ví dụ tập hợp không hỗ trợ truy cập theo chỉ số như list; tuple không sửa từng phần tử. Mọi dữ liệu thật cần xác minh kiểu, đơn vị và tính hợp lệ.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is List? — Thuật ngữ List có nghĩa gì?**

A. A different concept: Vị trí tính từ 0 để lấy phần tử — Vị trí tính từ 0 để lấy phần tử

B. A concept described as: Tập hợp có thứ tự, có thể thay đổi — Tập hợp có thứ tự, có thể thay đổi

C. A different concept: Lấy đoạn phần tử theo start:stop — Lấy đoạn phần tử theo start:stop

D. A different concept: Có thể cập nhật phần tử của danh sách — Có thể cập nhật phần tử của danh sách


**Q2. What is Index? — Thuật ngữ Index có nghĩa gì?**

A. A concept described as: Vị trí tính từ 0 để lấy phần tử — Vị trí tính từ 0 để lấy phần tử

B. A different concept: Lấy đoạn phần tử theo start:stop — Lấy đoạn phần tử theo start:stop

C. A different concept: Có thể cập nhật phần tử của danh sách — Có thể cập nhật phần tử của danh sách

D. A different concept: Tập hợp có thứ tự, có thể thay đổi — Tập hợp có thứ tự, có thể thay đổi


**Q3. What is Slice? — Thuật ngữ Slice có nghĩa gì?**

A. A different concept: Có thể cập nhật phần tử của danh sách — Có thể cập nhật phần tử của danh sách

B. A different concept: Tập hợp có thứ tự, có thể thay đổi — Tập hợp có thứ tự, có thể thay đổi

C. A different concept: Vị trí tính từ 0 để lấy phần tử — Vị trí tính từ 0 để lấy phần tử

D. A concept described as: Lấy đoạn phần tử theo start:stop — Lấy đoạn phần tử theo start:stop


**Q4. What is Mutability? — Thuật ngữ Mutability có nghĩa gì?**

A. A different concept: Tập hợp có thứ tự, có thể thay đổi — Tập hợp có thứ tự, có thể thay đổi

B. A different concept: Vị trí tính từ 0 để lấy phần tử — Vị trí tính từ 0 để lấy phần tử

C. A concept described as: Có thể cập nhật phần tử của danh sách — Có thể cập nhật phần tử của danh sách

D. A different concept: Lấy đoạn phần tử theo start:stop — Lấy đoạn phần tử theo start:stop


**Q5. Which statement fits 'append(), extend(), insert()'? — Mô tả nào đúng với 'append(), extend(), insert()'?**

A. It is used for: Xóa theo vị trí hoặc giá trị — Xóa theo vị trí hoặc giá trị

B. This syntax is used for: Thêm từng phần tử hoặc nhiều phần tử vào danh sách — Thêm từng phần tử hoặc nhiều phần tử vào danh sách

C. It is used for: Sắp xếp tại chỗ hoặc tạo danh sách mới — Sắp xếp tại chỗ hoặc tạo danh sách mới

D. It is used for: Lấy vùng con không bao gồm stop — Lấy vùng con không bao gồm stop


**Q6. Which statement fits 'pop(), remove(), del'? — Mô tả nào đúng với 'pop(), remove(), del'?**

A. This syntax is used for: Xóa theo vị trí hoặc giá trị — Xóa theo vị trí hoặc giá trị

B. It is used for: Sắp xếp tại chỗ hoặc tạo danh sách mới — Sắp xếp tại chỗ hoặc tạo danh sách mới

C. It is used for: Lấy vùng con không bao gồm stop — Lấy vùng con không bao gồm stop

D. It is used for: Thêm từng phần tử hoặc nhiều phần tử vào danh sách — Thêm từng phần tử hoặc nhiều phần tử vào danh sách


**Q7. Which statement fits 'sort(), sorted()'? — Mô tả nào đúng với 'sort(), sorted()'?**

A. It is used for: Lấy vùng con không bao gồm stop — Lấy vùng con không bao gồm stop

B. It is used for: Thêm từng phần tử hoặc nhiều phần tử vào danh sách — Thêm từng phần tử hoặc nhiều phần tử vào danh sách

C. It is used for: Xóa theo vị trí hoặc giá trị — Xóa theo vị trí hoặc giá trị

D. This syntax is used for: Sắp xếp tại chỗ hoặc tạo danh sách mới — Sắp xếp tại chỗ hoặc tạo danh sách mới


**Q8. Which statement fits 'items[start:stop]'? — Mô tả nào đúng với 'items[start:stop]'?**

A. It is used for: Thêm từng phần tử hoặc nhiều phần tử vào danh sách — Thêm từng phần tử hoặc nhiều phần tử vào danh sách

B. It is used for: Xóa theo vị trí hoặc giá trị — Xóa theo vị trí hoặc giá trị

C. This syntax is used for: Lấy vùng con không bao gồm stop — Lấy vùng con không bao gồm stop

D. It is used for: Sắp xếp tại chỗ hoặc tạo danh sách mới — Sắp xếp tại chỗ hoặc tạo danh sách mới


**Q9. Why use this method in scenario 1? — Vì sao chọn cách này ở tình huống 1?**

A. Because Sắp xếp bản sao giữ thứ tự gốc để còn so sánh — Sắp xếp bản sao giữ thứ tự gốc để còn so sánh

B. Because Thêm món mới vào danh sách thứ tự đã chọn — Thêm món mới vào danh sách thứ tự đã chọn

C. Because Chọn điểm >=5 bằng điều kiện trong list comprehension — Chọn điểm >=5 bằng điều kiện trong list comprehension

D. Because Sửa trực tiếp phần tử thứ hai khi kiểm đếm sai — Sửa trực tiếp phần tử thứ hai khi kiểm đếm sai


**Q10. Why use this method in scenario 2? — Vì sao chọn cách này ở tình huống 2?**

A. Because Sắp xếp bản sao giữ thứ tự gốc để còn so sánh — Sắp xếp bản sao giữ thứ tự gốc để còn so sánh

B. Because Chọn điểm >=5 bằng điều kiện trong list comprehension — Chọn điểm >=5 bằng điều kiện trong list comprehension

C. Because Sửa trực tiếp phần tử thứ hai khi kiểm đếm sai — Sửa trực tiếp phần tử thứ hai khi kiểm đếm sai

D. Because Lấy yêu cầu đầu tiên và xóa nó khỏi danh sách — Lấy yêu cầu đầu tiên và xóa nó khỏi danh sách


**Q11. Why use this method in scenario 3? — Vì sao chọn cách này ở tình huống 3?**

A. Because Sửa trực tiếp phần tử thứ hai khi kiểm đếm sai — Sửa trực tiếp phần tử thứ hai khi kiểm đếm sai

B. Because Lấy yêu cầu đầu tiên và xóa nó khỏi danh sách — Lấy yêu cầu đầu tiên và xóa nó khỏi danh sách

C. Because Thêm món mới vào danh sách thứ tự đã chọn — Thêm món mới vào danh sách thứ tự đã chọn

D. Because Chọn điểm >=5 bằng điều kiện trong list comprehension — Chọn điểm >=5 bằng điều kiện trong list comprehension


**Q12. Why use this method in scenario 4? — Vì sao chọn cách này ở tình huống 4?**

A. Because Lấy yêu cầu đầu tiên và xóa nó khỏi danh sách — Lấy yêu cầu đầu tiên và xóa nó khỏi danh sách

B. Because Thêm món mới vào danh sách thứ tự đã chọn — Thêm món mới vào danh sách thứ tự đã chọn

C. Because Sửa trực tiếp phần tử thứ hai khi kiểm đếm sai — Sửa trực tiếp phần tử thứ hai khi kiểm đếm sai

D. Because Sắp xếp bản sao giữ thứ tự gốc để còn so sánh — Sắp xếp bản sao giữ thứ tự gốc để còn so sánh


**Q13. Why use this method in scenario 5? — Vì sao chọn cách này ở tình huống 5?**

A. Because Thêm món mới vào danh sách thứ tự đã chọn — Thêm món mới vào danh sách thứ tự đã chọn

B. Because Lấy yêu cầu đầu tiên và xóa nó khỏi danh sách — Lấy yêu cầu đầu tiên và xóa nó khỏi danh sách

C. Because Sắp xếp bản sao giữ thứ tự gốc để còn so sánh — Sắp xếp bản sao giữ thứ tự gốc để còn so sánh

D. Because Chọn điểm >=5 bằng điều kiện trong list comprehension — Chọn điểm >=5 bằng điều kiện trong list comprehension


**Q14. What input belongs to scenario 1? — Tình huống 1 sử dụng dữ liệu gì?**

A. The stated input: Hai món ban đầu — Hai món ban đầu

B. The input is Điểm ưu tiên [2,9,4,7] — Điểm ưu tiên [2,9,4,7]

C. The input is 4 điểm thang 10 — 4 điểm thang 10

D. The input is Tồn 3 mặt hàng — Tồn 3 mặt hàng


**Q15. What input belongs to scenario 2? — Tình huống 2 sử dụng dữ liệu gì?**

A. The input is 4 điểm thang 10 — 4 điểm thang 10

B. The input is Tồn 3 mặt hàng — Tồn 3 mặt hàng

C. The input is 3 mã yêu cầu — 3 mã yêu cầu

D. The stated input: Điểm ưu tiên [2,9,4,7] — Điểm ưu tiên [2,9,4,7]


**Q16. What input belongs to scenario 3? — Tình huống 3 sử dụng dữ liệu gì?**

A. The input is Tồn 3 mặt hàng — Tồn 3 mặt hàng

B. The input is 3 mã yêu cầu — 3 mã yêu cầu

C. The stated input: 4 điểm thang 10 — 4 điểm thang 10

D. The input is Hai món ban đầu — Hai món ban đầu


**Q17. What input belongs to scenario 4? — Tình huống 4 sử dụng dữ liệu gì?**

A. The input is 3 mã yêu cầu — 3 mã yêu cầu

B. The stated input: Tồn 3 mặt hàng — Tồn 3 mặt hàng

C. The input is Hai món ban đầu — Hai món ban đầu

D. The input is Điểm ưu tiên [2,9,4,7] — Điểm ưu tiên [2,9,4,7]


**Q18. What input belongs to scenario 5? — Tình huống 5 sử dụng dữ liệu gì?**

A. The stated input: 3 mã yêu cầu — 3 mã yêu cầu

B. The input is Hai món ban đầu — Hai món ban đầu

C. The input is Điểm ưu tiên [2,9,4,7] — Điểm ưu tiên [2,9,4,7]

D. The input is 4 điểm thang 10 — 4 điểm thang 10


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
| Q1 | **B** | A concept described as: Tập hợp có thứ tự, có thể thay đổi | Tập hợp có thứ tự, có thể thay đổi |
| Q2 | **A** | A concept described as: Vị trí tính từ 0 để lấy phần tử | Vị trí tính từ 0 để lấy phần tử |
| Q3 | **D** | A concept described as: Lấy đoạn phần tử theo start:stop | Lấy đoạn phần tử theo start:stop |
| Q4 | **C** | A concept described as: Có thể cập nhật phần tử của danh sách | Có thể cập nhật phần tử của danh sách |
| Q5 | **B** | This syntax is used for: Thêm từng phần tử hoặc nhiều phần tử vào danh sách | Thêm từng phần tử hoặc nhiều phần tử vào danh sách |
| Q6 | **A** | This syntax is used for: Xóa theo vị trí hoặc giá trị | Xóa theo vị trí hoặc giá trị |
| Q7 | **D** | This syntax is used for: Sắp xếp tại chỗ hoặc tạo danh sách mới | Sắp xếp tại chỗ hoặc tạo danh sách mới |
| Q8 | **C** | This syntax is used for: Lấy vùng con không bao gồm stop | Lấy vùng con không bao gồm stop |
| Q9 | **B** | Because Thêm món mới vào danh sách thứ tự đã chọn | Thêm món mới vào danh sách thứ tự đã chọn |
| Q10 | **A** | Because Sắp xếp bản sao giữ thứ tự gốc để còn so sánh | Sắp xếp bản sao giữ thứ tự gốc để còn so sánh |
| Q11 | **D** | Because Chọn điểm >=5 bằng điều kiện trong list comprehension | Chọn điểm >=5 bằng điều kiện trong list comprehension |
| Q12 | **C** | Because Sửa trực tiếp phần tử thứ hai khi kiểm đếm sai | Sửa trực tiếp phần tử thứ hai khi kiểm đếm sai |
| Q13 | **B** | Because Lấy yêu cầu đầu tiên và xóa nó khỏi danh sách | Lấy yêu cầu đầu tiên và xóa nó khỏi danh sách |
| Q14 | **A** | The stated input: Hai món ban đầu | Hai món ban đầu |
| Q15 | **D** | The stated input: Điểm ưu tiên [2,9,4,7] | Điểm ưu tiên [2,9,4,7] |
| Q16 | **C** | The stated input: 4 điểm thang 10 | 4 điểm thang 10 |
| Q17 | **B** | The stated input: Tồn 3 mặt hàng | Tồn 3 mặt hàng |
| Q18 | **A** | The stated input: 3 mã yêu cầu | 3 mã yêu cầu |
| Q19 | **D** | Input meaning, type and units | Ý nghĩa, kiểu và đơn vị đầu vào |
| Q20 | **C** | Verify output and edge cases | Đối chiếu kết quả và thử trường hợp biên |

## 8. Kết nối bài tiếp theo

`Vòng lặp → List → Vector/Array`.

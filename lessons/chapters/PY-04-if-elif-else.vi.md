# 04 — Điều kiện if/elif/else

*Trạng thái: DRAFT · Ví dụ giả lập · Cần xác minh thực thi trước khi phát hành*

## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Condition** — điều kiện; **Branch** — nhánh.

`Toán tử → Điều kiện → Phân loại theo quy tắc`

Từ kiến thức trước, phần này giúp sinh viên quyết định nên tổ chức và xử lý dữ liệu bằng cấu trúc nào, rồi mới tiến tới các bài xử lý dữ liệu cho AI.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Giải thích dễ nhớ |
|---|---|---|
| Condition | điều kiện | Phép kiểm tra đúng hoặc sai |
| Branch | nhánh | Phần chương trình được chọn để chạy |
| Threshold | ngưỡng | Ranh giới để chuyển trạng thái |
| Nested if | điều kiện lồng | Kiểm tra bổ sung bên trong một nhánh |

## 3. Hàm và cú pháp Python

**Từ vựng trong mục:** **Function** — hàm; **Argument** — đối số.

| Hàm / cú pháp | Mục đích và lựa chọn liên quan |
|---|---|
| `if expression:` | Chỉ chạy nhánh nếu điều kiện đúng |
| `elif expression:` | Thử điều kiện tiếp theo khi nhánh trước không đúng |
| `else:` | Trường hợp còn lại không cần điều kiện mới |
| `in, and, or` | Kiểm tra thành viên hoặc kết hợp nhiều điều kiện |

## 4. Khái niệm liên quan và ví dụ nhỏ

### 4.1. Condition

**Từ vựng trong mục:** **Condition** — điều kiện.

Phép kiểm tra đúng hoặc sai. Đây là khái niệm cần nắm trước khi áp dụng bước xử lý bên dưới.

```python
print(5>3)
```

**Tự kiểm tra:** Condition có nghĩa gì? **Đáp án:** Phép kiểm tra đúng hoặc sai.

### 4.2. Branch

**Từ vựng trong mục:** **Branch** — nhánh.

Phần chương trình được chọn để chạy. Đây là khái niệm cần nắm trước khi áp dụng bước xử lý bên dưới.

```python
if True: print('ok')
```

**Tự kiểm tra:** Branch có nghĩa gì? **Đáp án:** Phần chương trình được chọn để chạy.

### 4.3. Threshold

**Từ vựng trong mục:** **Threshold** — ngưỡng.

Ranh giới để chuyển trạng thái. Đây là khái niệm cần nắm trước khi áp dụng bước xử lý bên dưới.

```python
print(85>=80)
```

**Tự kiểm tra:** Threshold có nghĩa gì? **Đáp án:** Ranh giới để chuyển trạng thái.

### 4.4. Nested if

**Từ vựng trong mục:** **Nested if** — điều kiện lồng.

Kiểm tra bổ sung bên trong một nhánh. Đây là khái niệm cần nắm trước khi áp dụng bước xử lý bên dưới.

```python
x=2
if x>0:
    if x%2==0: print('even')
```

**Tự kiểm tra:** Nested if có nghĩa gì? **Đáp án:** Kiểm tra bổ sung bên trong một nhánh.

## 5. Năm tình huống lập trình thực tế

### Tình huống 1 — Xếp loại điểm

**Từ vựng trong mục:** **Condition** — điều kiện.

**Vấn đề thực tế:** Xếp loại điểm.

**Vì sao chọn cách này?** Kiểm ngưỡng từ cao xuống thấp để không gán sai xếp loại; không cần công cụ phức tạp hơn khi một quy tắc rõ ràng đã giải được vấn đề.

**Dữ liệu:** Một điểm số 85/100; nếu là bảng thì mỗi hàng là một đối tượng và mỗi cột mang một thuộc tính có thứ tự. Các giá trị ở đây đều là ví dụ.

**Quy trình:** Xác định dữ liệu → chọn phép xử lý → chạy code → đọc kết quả và thử trường hợp biên.

```python
score=85
if score>=90: grade="A"
elif score>=80: grade="B"
else: grade="Other"
print(grade)
```

**Đọc kết quả:** Đối chiếu với giả định đầu vào; đổi dữ liệu và xem kết quả có đúng ý nghĩa không.

### Tình huống 2 — Cảnh báo hàng gần hết

**Từ vựng trong mục:** **Branch** — nhánh.

**Vấn đề thực tế:** Cảnh báo hàng gần hết.

**Vì sao chọn cách này?** Chia tồn kho thành hết/gần hết/bình thường; không cần công cụ phức tạp hơn khi một quy tắc rõ ràng đã giải được vấn đề.

**Dữ liệu:** Số lượng 4 món; nếu là bảng thì mỗi hàng là một đối tượng và mỗi cột mang một thuộc tính có thứ tự. Các giá trị ở đây đều là ví dụ.

**Quy trình:** Xác định dữ liệu → chọn phép xử lý → chạy code → đọc kết quả và thử trường hợp biên.

```python
qty=4
if qty<=0: state="Out"
elif qty<=5: state="Low"
else: state="OK"
print(state)
```

**Đọc kết quả:** Đối chiếu với giả định đầu vào; đổi dữ liệu và xem kết quả có đúng ý nghĩa không.

### Tình huống 3 — Xét VIP

**Từ vựng trong mục:** **Threshold** — ngưỡng.

**Vấn đề thực tế:** Xét VIP.

**Vì sao chọn cách này?** Yêu cầu cả năm đăng ký và mức chi tiêu đạt ngưỡng; không cần công cụ phức tạp hơn khi một quy tắc rõ ràng đã giải được vấn đề.

**Dữ liệu:** Khách 6 năm và chi 1500000 đồng; nếu là bảng thì mỗi hàng là một đối tượng và mỗi cột mang một thuộc tính có thứ tự. Các giá trị ở đây đều là ví dụ.

**Quy trình:** Xác định dữ liệu → chọn phép xử lý → chạy code → đọc kết quả và thử trường hợp biên.

```python
years,paid=6,1500000
if years>=5 and paid>=1000000: print("VIP")
else: print("Regular")
```

**Đọc kết quả:** Đối chiếu với giả định đầu vào; đổi dữ liệu và xem kết quả có đúng ý nghĩa không.

### Tình huống 4 — Kiểm tra cảm biến

**Từ vựng trong mục:** **Nested if** — điều kiện lồng.

**Vấn đề thực tế:** Kiểm tra cảm biến.

**Vì sao chọn cách này?** Kiểm tra thiết bị online trước khi xét nhiệt độ; không cần công cụ phức tạp hơn khi một quy tắc rõ ràng đã giải được vấn đề.

**Dữ liệu:** Nhiệt độ 82 độ C và online=True; nếu là bảng thì mỗi hàng là một đối tượng và mỗi cột mang một thuộc tính có thứ tự. Các giá trị ở đây đều là ví dụ.

**Quy trình:** Xác định dữ liệu → chọn phép xử lý → chạy code → đọc kết quả và thử trường hợp biên.

```python
online,temp=True,82
if online:
    print("Hot" if temp>=80 else "Normal")
else: print("Offline")
```

**Đọc kết quả:** Đối chiếu với giả định đầu vào; đổi dữ liệu và xem kết quả có đúng ý nghĩa không.

### Tình huống 5 — Tính quý của tháng

**Từ vựng trong mục:** **Condition** — điều kiện.

**Vấn đề thực tế:** Tính quý của tháng.

**Vì sao chọn cách này?** Dùng khoảng tháng hợp lệ trước khi tính quý; không cần công cụ phức tạp hơn khi một quy tắc rõ ràng đã giải được vấn đề.

**Dữ liệu:** Tháng 10; nếu là bảng thì mỗi hàng là một đối tượng và mỗi cột mang một thuộc tính có thứ tự. Các giá trị ở đây đều là ví dụ.

**Quy trình:** Xác định dữ liệu → chọn phép xử lý → chạy code → đọc kết quả và thử trường hợp biên.

```python
month=10
if 1<=month<=12: print((month-1)//3+1)
else: print("Invalid")
```

**Đọc kết quả:** Đối chiếu với giả định đầu vào; đổi dữ liệu và xem kết quả có đúng ý nghĩa không.

## 6. Nhầm lẫn dễ gặp

Không sử dụng cấu trúc dữ liệu sai với mục đích: ví dụ tập hợp không hỗ trợ truy cập theo chỉ số như list; tuple không sửa từng phần tử. Mọi dữ liệu thật cần xác minh kiểu, đơn vị và tính hợp lệ.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is Condition? — Thuật ngữ Condition có nghĩa gì?**

A. A different concept: Phần chương trình được chọn để chạy — Phần chương trình được chọn để chạy

B. A concept described as: Phép kiểm tra đúng hoặc sai — Phép kiểm tra đúng hoặc sai

C. A different concept: Ranh giới để chuyển trạng thái — Ranh giới để chuyển trạng thái

D. A different concept: Kiểm tra bổ sung bên trong một nhánh — Kiểm tra bổ sung bên trong một nhánh


**Q2. What is Branch? — Thuật ngữ Branch có nghĩa gì?**

A. A concept described as: Phần chương trình được chọn để chạy — Phần chương trình được chọn để chạy

B. A different concept: Ranh giới để chuyển trạng thái — Ranh giới để chuyển trạng thái

C. A different concept: Kiểm tra bổ sung bên trong một nhánh — Kiểm tra bổ sung bên trong một nhánh

D. A different concept: Phép kiểm tra đúng hoặc sai — Phép kiểm tra đúng hoặc sai


**Q3. What is Threshold? — Thuật ngữ Threshold có nghĩa gì?**

A. A different concept: Kiểm tra bổ sung bên trong một nhánh — Kiểm tra bổ sung bên trong một nhánh

B. A different concept: Phép kiểm tra đúng hoặc sai — Phép kiểm tra đúng hoặc sai

C. A different concept: Phần chương trình được chọn để chạy — Phần chương trình được chọn để chạy

D. A concept described as: Ranh giới để chuyển trạng thái — Ranh giới để chuyển trạng thái


**Q4. What is Nested if? — Thuật ngữ Nested if có nghĩa gì?**

A. A different concept: Phép kiểm tra đúng hoặc sai — Phép kiểm tra đúng hoặc sai

B. A different concept: Phần chương trình được chọn để chạy — Phần chương trình được chọn để chạy

C. A concept described as: Kiểm tra bổ sung bên trong một nhánh — Kiểm tra bổ sung bên trong một nhánh

D. A different concept: Ranh giới để chuyển trạng thái — Ranh giới để chuyển trạng thái


**Q5. Which statement fits 'if expression:'? — Mô tả nào đúng với 'if expression:'?**

A. It is used for: Thử điều kiện tiếp theo khi nhánh trước không đúng — Thử điều kiện tiếp theo khi nhánh trước không đúng

B. This syntax is used for: Chỉ chạy nhánh nếu điều kiện đúng — Chỉ chạy nhánh nếu điều kiện đúng

C. It is used for: Trường hợp còn lại không cần điều kiện mới — Trường hợp còn lại không cần điều kiện mới

D. It is used for: Kiểm tra thành viên hoặc kết hợp nhiều điều kiện — Kiểm tra thành viên hoặc kết hợp nhiều điều kiện


**Q6. Which statement fits 'elif expression:'? — Mô tả nào đúng với 'elif expression:'?**

A. This syntax is used for: Thử điều kiện tiếp theo khi nhánh trước không đúng — Thử điều kiện tiếp theo khi nhánh trước không đúng

B. It is used for: Trường hợp còn lại không cần điều kiện mới — Trường hợp còn lại không cần điều kiện mới

C. It is used for: Kiểm tra thành viên hoặc kết hợp nhiều điều kiện — Kiểm tra thành viên hoặc kết hợp nhiều điều kiện

D. It is used for: Chỉ chạy nhánh nếu điều kiện đúng — Chỉ chạy nhánh nếu điều kiện đúng


**Q7. Which statement fits 'else:'? — Mô tả nào đúng với 'else:'?**

A. It is used for: Kiểm tra thành viên hoặc kết hợp nhiều điều kiện — Kiểm tra thành viên hoặc kết hợp nhiều điều kiện

B. It is used for: Chỉ chạy nhánh nếu điều kiện đúng — Chỉ chạy nhánh nếu điều kiện đúng

C. It is used for: Thử điều kiện tiếp theo khi nhánh trước không đúng — Thử điều kiện tiếp theo khi nhánh trước không đúng

D. This syntax is used for: Trường hợp còn lại không cần điều kiện mới — Trường hợp còn lại không cần điều kiện mới


**Q8. Which statement fits 'in, and, or'? — Mô tả nào đúng với 'in, and, or'?**

A. It is used for: Chỉ chạy nhánh nếu điều kiện đúng — Chỉ chạy nhánh nếu điều kiện đúng

B. It is used for: Thử điều kiện tiếp theo khi nhánh trước không đúng — Thử điều kiện tiếp theo khi nhánh trước không đúng

C. This syntax is used for: Kiểm tra thành viên hoặc kết hợp nhiều điều kiện — Kiểm tra thành viên hoặc kết hợp nhiều điều kiện

D. It is used for: Trường hợp còn lại không cần điều kiện mới — Trường hợp còn lại không cần điều kiện mới


**Q9. Why use this method in scenario 1? — Vì sao chọn cách này ở tình huống 1?**

A. Because Chia tồn kho thành hết/gần hết/bình thường — Chia tồn kho thành hết/gần hết/bình thường

B. Because Kiểm ngưỡng từ cao xuống thấp để không gán sai xếp loại — Kiểm ngưỡng từ cao xuống thấp để không gán sai xếp loại

C. Because Yêu cầu cả năm đăng ký và mức chi tiêu đạt ngưỡng — Yêu cầu cả năm đăng ký và mức chi tiêu đạt ngưỡng

D. Because Kiểm tra thiết bị online trước khi xét nhiệt độ — Kiểm tra thiết bị online trước khi xét nhiệt độ


**Q10. Why use this method in scenario 2? — Vì sao chọn cách này ở tình huống 2?**

A. Because Chia tồn kho thành hết/gần hết/bình thường — Chia tồn kho thành hết/gần hết/bình thường

B. Because Yêu cầu cả năm đăng ký và mức chi tiêu đạt ngưỡng — Yêu cầu cả năm đăng ký và mức chi tiêu đạt ngưỡng

C. Because Kiểm tra thiết bị online trước khi xét nhiệt độ — Kiểm tra thiết bị online trước khi xét nhiệt độ

D. Because Dùng khoảng tháng hợp lệ trước khi tính quý — Dùng khoảng tháng hợp lệ trước khi tính quý


**Q11. Why use this method in scenario 3? — Vì sao chọn cách này ở tình huống 3?**

A. Because Kiểm tra thiết bị online trước khi xét nhiệt độ — Kiểm tra thiết bị online trước khi xét nhiệt độ

B. Because Dùng khoảng tháng hợp lệ trước khi tính quý — Dùng khoảng tháng hợp lệ trước khi tính quý

C. Because Kiểm ngưỡng từ cao xuống thấp để không gán sai xếp loại — Kiểm ngưỡng từ cao xuống thấp để không gán sai xếp loại

D. Because Yêu cầu cả năm đăng ký và mức chi tiêu đạt ngưỡng — Yêu cầu cả năm đăng ký và mức chi tiêu đạt ngưỡng


**Q12. Why use this method in scenario 4? — Vì sao chọn cách này ở tình huống 4?**

A. Because Dùng khoảng tháng hợp lệ trước khi tính quý — Dùng khoảng tháng hợp lệ trước khi tính quý

B. Because Kiểm ngưỡng từ cao xuống thấp để không gán sai xếp loại — Kiểm ngưỡng từ cao xuống thấp để không gán sai xếp loại

C. Because Kiểm tra thiết bị online trước khi xét nhiệt độ — Kiểm tra thiết bị online trước khi xét nhiệt độ

D. Because Chia tồn kho thành hết/gần hết/bình thường — Chia tồn kho thành hết/gần hết/bình thường


**Q13. Why use this method in scenario 5? — Vì sao chọn cách này ở tình huống 5?**

A. Because Kiểm ngưỡng từ cao xuống thấp để không gán sai xếp loại — Kiểm ngưỡng từ cao xuống thấp để không gán sai xếp loại

B. Because Dùng khoảng tháng hợp lệ trước khi tính quý — Dùng khoảng tháng hợp lệ trước khi tính quý

C. Because Chia tồn kho thành hết/gần hết/bình thường — Chia tồn kho thành hết/gần hết/bình thường

D. Because Yêu cầu cả năm đăng ký và mức chi tiêu đạt ngưỡng — Yêu cầu cả năm đăng ký và mức chi tiêu đạt ngưỡng


**Q14. What input belongs to scenario 1? — Tình huống 1 sử dụng dữ liệu gì?**

A. The stated input: Một điểm số 85/100 — Một điểm số 85/100

B. The input is Số lượng 4 món — Số lượng 4 món

C. The input is Khách 6 năm và chi 1500000 đồng — Khách 6 năm và chi 1500000 đồng

D. The input is Nhiệt độ 82 độ C và online=True — Nhiệt độ 82 độ C và online=True


**Q15. What input belongs to scenario 2? — Tình huống 2 sử dụng dữ liệu gì?**

A. The input is Khách 6 năm và chi 1500000 đồng — Khách 6 năm và chi 1500000 đồng

B. The input is Nhiệt độ 82 độ C và online=True — Nhiệt độ 82 độ C và online=True

C. The input is Tháng 10 — Tháng 10

D. The stated input: Số lượng 4 món — Số lượng 4 món


**Q16. What input belongs to scenario 3? — Tình huống 3 sử dụng dữ liệu gì?**

A. The input is Nhiệt độ 82 độ C và online=True — Nhiệt độ 82 độ C và online=True

B. The input is Tháng 10 — Tháng 10

C. The stated input: Khách 6 năm và chi 1500000 đồng — Khách 6 năm và chi 1500000 đồng

D. The input is Một điểm số 85/100 — Một điểm số 85/100


**Q17. What input belongs to scenario 4? — Tình huống 4 sử dụng dữ liệu gì?**

A. The input is Tháng 10 — Tháng 10

B. The stated input: Nhiệt độ 82 độ C và online=True — Nhiệt độ 82 độ C và online=True

C. The input is Một điểm số 85/100 — Một điểm số 85/100

D. The input is Số lượng 4 món — Số lượng 4 món


**Q18. What input belongs to scenario 5? — Tình huống 5 sử dụng dữ liệu gì?**

A. The stated input: Tháng 10 — Tháng 10

B. The input is Một điểm số 85/100 — Một điểm số 85/100

C. The input is Số lượng 4 món — Số lượng 4 món

D. The input is Khách 6 năm và chi 1500000 đồng — Khách 6 năm và chi 1500000 đồng


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
| Q1 | **B** | A concept described as: Phép kiểm tra đúng hoặc sai | Phép kiểm tra đúng hoặc sai |
| Q2 | **A** | A concept described as: Phần chương trình được chọn để chạy | Phần chương trình được chọn để chạy |
| Q3 | **D** | A concept described as: Ranh giới để chuyển trạng thái | Ranh giới để chuyển trạng thái |
| Q4 | **C** | A concept described as: Kiểm tra bổ sung bên trong một nhánh | Kiểm tra bổ sung bên trong một nhánh |
| Q5 | **B** | This syntax is used for: Chỉ chạy nhánh nếu điều kiện đúng | Chỉ chạy nhánh nếu điều kiện đúng |
| Q6 | **A** | This syntax is used for: Thử điều kiện tiếp theo khi nhánh trước không đúng | Thử điều kiện tiếp theo khi nhánh trước không đúng |
| Q7 | **D** | This syntax is used for: Trường hợp còn lại không cần điều kiện mới | Trường hợp còn lại không cần điều kiện mới |
| Q8 | **C** | This syntax is used for: Kiểm tra thành viên hoặc kết hợp nhiều điều kiện | Kiểm tra thành viên hoặc kết hợp nhiều điều kiện |
| Q9 | **B** | Because Kiểm ngưỡng từ cao xuống thấp để không gán sai xếp loại | Kiểm ngưỡng từ cao xuống thấp để không gán sai xếp loại |
| Q10 | **A** | Because Chia tồn kho thành hết/gần hết/bình thường | Chia tồn kho thành hết/gần hết/bình thường |
| Q11 | **D** | Because Yêu cầu cả năm đăng ký và mức chi tiêu đạt ngưỡng | Yêu cầu cả năm đăng ký và mức chi tiêu đạt ngưỡng |
| Q12 | **C** | Because Kiểm tra thiết bị online trước khi xét nhiệt độ | Kiểm tra thiết bị online trước khi xét nhiệt độ |
| Q13 | **B** | Because Dùng khoảng tháng hợp lệ trước khi tính quý | Dùng khoảng tháng hợp lệ trước khi tính quý |
| Q14 | **A** | The stated input: Một điểm số 85/100 | Một điểm số 85/100 |
| Q15 | **D** | The stated input: Số lượng 4 món | Số lượng 4 món |
| Q16 | **C** | The stated input: Khách 6 năm và chi 1500000 đồng | Khách 6 năm và chi 1500000 đồng |
| Q17 | **B** | The stated input: Nhiệt độ 82 độ C và online=True | Nhiệt độ 82 độ C và online=True |
| Q18 | **A** | The stated input: Tháng 10 | Tháng 10 |
| Q19 | **D** | Input meaning, type and units | Ý nghĩa, kiểu và đơn vị đầu vào |
| Q20 | **C** | Verify output and edge cases | Đối chiếu kết quả và thử trường hợp biên |

## 8. Kết nối bài tiếp theo

`Toán tử → Điều kiện → Phân loại theo quy tắc`.

# PY-03 — Toán tử số học, so sánh và logic


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Arithmetic** — số học; **Comparison** — so sánh.

`Kiểu dữ liệu → Toán tử → Điều kiện → Quy tắc nghiệp vụ`

Sau khi biết dùng biến và kiểu dữ liệu, ta học các phép tính và cách kiểm tra điều kiện. Toán tử giúp tính hóa đơn, xét ưu đãi và xử lý các trạng thái đúng/sai.

## 2. English vocabulary — Từ vựng

| English | Nghĩa tiếng Việt | Giải thích |
|---|---|---|
| Arithmetic | số học | Phép cộng trừ nhân chia |
| Comparison | so sánh | So sánh hai giá trị |
| Logical | logic | Kết hợp các điều kiện |
| Bitwise | thao tác bit | Phép tính trên các bit của số nguyên |

## 3. Các hàm và tùy chọn Python

**Từ vựng trong mục:** **Function** — hàm; **Argument** — đối số.

| Hàm / cú pháp | Mục đích và ý nghĩa lựa chọn |
|---|---|
| `+, -, *, /` | Tính số học và tỷ lệ |
| `//, %, **` | Chia nguyên, lấy dư, lũy thừa |
| `==, !=, <=, >=, and, or` | So sánh và kết hợp điều kiện |
| `&, |, ^` | Chỉ dùng cho cờ bit hoặc toán bit được thiết kế rõ |


## 4. Khái niệm liên quan

### 4.1. Arithmetic

**Từ vựng trong mục:** **Arithmetic** — số học.

Toán tử số học dùng để tính cộng `+`, trừ `-`, nhân `*`, chia `/`. Ví dụ `5 * 3` cho kết quả `15`. Python còn có `//` để chia lấy phần nguyên và `%` để lấy phần dư.

```python
print(5 * 3)
```

**Kết quả khi chạy:**

```text
15
```


### 4.2. Comparison

**Từ vựng trong mục:** **Comparison** — so sánh.

Toán tử so sánh kiểm tra hai giá trị bằng nhau, khác nhau, lớn hơn hay nhỏ hơn. Ví dụ, `8 >= 5` trả về `True` vì 8 lớn hơn 5. Dùng `==` để so sánh bằng nhau, khác với `=` để gán giá trị.

```python
print(8 >= 5)
```

**Kết quả khi chạy:**

```text
True
```


### 4.3. Logical

**Từ vựng trong mục:** **Logical** — logic.

Toán tử logic nối các điều kiện đúng/sai: `and` cần cả hai đúng, `or` chỉ cần ít nhất một điều kiện đúng, còn `not` đảo ngược kết quả. `True and False` trả về `False`.

```python
print(True and False)
```

**Kết quả khi chạy:**

```text
False
```


### 4.4. Bitwise

**Từ vựng trong mục:** **Bitwise** — thao tác bit.

Bit là một chữ số nhị phân, chỉ có thể là `0` hoặc `1`. Phép `&` chỉ giữ bit bằng 1 ở cả hai số: `5` (`0101`) và `3` (`0011`) cho kết quả `1` (`0001`). Đây là phép xử lý bit, khác với toán tử logic `and`.

```python
print(5 & 3)
```

**Kết quả khi chạy:**

```text
1
```


## 5. Năm tình huống lập trình thực tế

### Tình huống 1 — Tính ưu đãi

**Từ vựng trong mục:** **Arithmetic** — số học; **Discount** — giảm giá.

**Tình huống thực tế:** Cửa hàng bán một sản phẩm giá 250.000 đồng và giảm 10% trên giá niêm yết.

**Yêu cầu:** Tính số tiền khách phải trả sau giảm giá.

**Vì sao chọn cách giải này?** Nhân giá gốc với `(1 - 0.10)` để lấy 90% giá ban đầu.

**Quy trình giải:**

1. Lưu giá gốc vào `price`.
2. Tính tỷ lệ còn lại là `1 - 0.10`.
3. Nhân giá với tỷ lệ còn lại và in kết quả.

```python
price = 250000
print(price * (1 - 0.10))
```

**Kết quả khi chạy:**

```text
225000.0
```

**Kết quả:** `225000.0` đồng — khách được giảm 25.000 đồng.

### Tình huống 2 — Xét VIP

**Từ vựng trong mục:** **Comparison** — so sánh; **Logical AND** — phép và.

**Tình huống thực tế:** Một cửa hàng công nhận khách VIP khi đã là thành viên ít nhất 5 năm và chi tiêu từ 1.000.000 đồng. Một khách đã tham gia 5 năm và chi 1.200.000 đồng.

**Yêu cầu:** Kiểm tra khách này có đủ điều kiện VIP hay không.

**Vì sao chọn cách giải này?** Dùng `>=` để kiểm tra từng ngưỡng, rồi dùng `and` vì hai điều kiện phải đồng thời đúng.

**Quy trình giải:**

1. Lưu số năm thành viên và tổng chi tiêu.
2. Kiểm tra từng giá trị có đạt ngưỡng không.
3. Nối hai điều kiện bằng `and` và in kết quả.

```python
years, spending = 5, 1200000
print(years >= 5 and spending >= 1000000)
```

**Kết quả khi chạy:**

```text
True
```

**Kết quả:** `True` — khách đạt cả hai tiêu chí VIP.

### Tình huống 3 — Đóng thùng hàng

**Từ vựng trong mục:** **Integer division** — chia lấy phần nguyên; **Remainder** — số dư.

**Tình huống thực tế:** Kho hàng có 23 sản phẩm và dùng thùng chứa đúng 5 sản phẩm khi đầy. Sản phẩm chưa đủ một thùng được giữ lại.

**Yêu cầu:** Tính số thùng đầy và số sản phẩm còn dư.

**Vì sao chọn cách giải này?** Chia nguyên `//` cho số thùng đầy; chia lấy dư `%` cho số sản phẩm còn lại.

**Quy trình giải:**

1. Lưu số sản phẩm và sức chứa mỗi thùng.
2. Dùng `//` đếm số thùng đầy.
3. Dùng `%` tính sản phẩm còn dư.

```python
items, box_size = 23, 5
print(items // box_size, items % box_size)
```

**Kết quả khi chạy:**

```text
4 3
```

**Kết quả:** `4 3` — có 4 thùng đầy và 3 sản phẩm dư.

### Tình huống 4 — Đọc cờ thiết bị

**Từ vựng trong mục:** **Bitwise AND** — phép và theo bit; **Mask** — mặt nạ bit.

**Tình huống thực tế:** Một thiết bị lưu trạng thái bốn công tắc trong số nhị phân `0b1010`. Mỗi bit thể hiện một công tắc bật (`1`) hoặc tắt (`0`). Công tắc tương ứng với bit `0b0010` cần được kiểm tra.

**Yêu cầu:** In `True` nếu công tắc đó bật, ngược lại in `False`.

**Vì sao chọn cách giải này?** Dùng phép AND bit `&` cùng mặt nạ `0b0010` để lấy đúng bit cần kiểm tra; `bool()` đổi kết quả thành đúng/sai.

**Quy trình giải:**

1. Lưu trạng thái nhị phân.
2. Dùng `status & 0b0010` để lấy bit mục tiêu.
3. Dùng `bool()` và in kết quả.

```python
status = 0b1010
print(bool(status & 0b0010))
```

**Kết quả khi chạy:**

```text
True
```

**Kết quả:** `True` — bit `0b0010` đang bật.

### Tình huống 5 — Ưu tiên đơn hàng

**Từ vựng trong mục:** **Logical OR** — phép hoặc; **Comparison** — so sánh.

**Tình huống thực tế:** Cửa hàng ưu tiên một đơn hàng nếu giá trị từ 2.000.000 đồng hoặc đơn bị trễ hơn 2 ngày. Một đơn có giá trị 3.000.000 đồng và chưa trễ ngày nào (`delay = 0`).

**Yêu cầu:** Kiểm tra đơn hàng có được ưu tiên hay không.

**Vì sao chọn cách giải này?** Dùng `or` vì chỉ cần một trong hai điều kiện đạt ngưỡng là đủ.

**Quy trình giải:**

1. Lưu giá trị đơn và số ngày trễ.
2. Kiểm tra giá trị đơn đạt từ 2.000.000 đồng.
3. Kiểm tra số ngày trễ lớn hơn 2, nối hai kết quả bằng `or`.

```python
amount, delay = 3000000, 0
print(amount >= 2000000 or delay > 2)
```

**Kết quả khi chạy:**

```text
True
```

**Kết quả:** `True` — đơn được ưu tiên nhờ giá trị đạt ngưỡng.

## 6. Những nhầm lẫn thường gặp

- `=` dùng để gán giá trị, còn `==` dùng để so sánh bằng nhau.
- `and` và `or` kiểm tra điều kiện; `&` và `|` thao tác trên các bit, không thay thế tùy tiện cho nhau.
- `/` cho kết quả chia thông thường, `//` lấy phần nguyên theo hướng làm tròn xuống, `%` lấy số dư.
- Với giá tiền cần tính chính xác đến từng đồng, nên cân nhắc dùng số nguyên đồng hoặc `Decimal` thay vì dựa vào số thực cho phép tính tiền phức tạp.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is Arithmetic? — Thuật ngữ Arithmetic có nghĩa gì?**

A. A true-or-false comparison — So sánh hai giá trị

B. Math operations on numbers — Phép cộng trừ nhân chia

C. Combining boolean conditions — Kết hợp các điều kiện

D. Operations on binary digits — Phép tính trên các bit của số nguyên


**Q2. What is Comparison? — Thuật ngữ Comparison có nghĩa gì?**

A. A true-or-false comparison — So sánh hai giá trị

B. Combining boolean conditions — Kết hợp các điều kiện

C. Operations on binary digits — Phép tính trên các bit của số nguyên

D. Math operations on numbers — Phép cộng trừ nhân chia


**Q3. What is Logical? — Thuật ngữ Logical có nghĩa gì?**

A. Operations on binary digits — Phép tính trên các bit của số nguyên

B. Math operations on numbers — Phép cộng trừ nhân chia

C. A true-or-false comparison — So sánh hai giá trị

D. Combining boolean conditions — Kết hợp các điều kiện


**Q4. What is Bitwise? — Thuật ngữ Bitwise có nghĩa gì?**

A. Math operations on numbers — Phép cộng trừ nhân chia

B. A true-or-false comparison — So sánh hai giá trị

C. Operations on binary digits — Phép tính trên các bit của số nguyên

D. Combining boolean conditions — Kết hợp các điều kiện


**Q5. Which use matches +, -, *, /? — Công dụng nào đúng với +, -, *, /?**

A. It always creates perfect predictions — Nó luôn dự đoán đúng tuyệt đối

B. These operators perform arithmetic calculations — Tính số học và tỷ lệ

C. It automatically trains a neural network — Nó tự huấn luyện mạng nơ-ron

D. It removes the need for input checks — Nó loại bỏ nhu cầu kiểm tra đầu vào


**Q6. Which use matches //, %, **? — Công dụng nào đúng với //, %, **?**

A. These operators calculate floor division, remainder and powers — Chia nguyên, lấy dư, lũy thừa

B. It always creates perfect predictions — Nó luôn dự đoán đúng tuyệt đối

C. It automatically trains a neural network — Nó tự huấn luyện mạng nơ-ron

D. It removes the need for input checks — Nó loại bỏ nhu cầu kiểm tra đầu vào


**Q7. Which use matches ==, !=, <=, >=, and, or? — Công dụng nào đúng với ==, !=, <=, >=, and, or?**

A. It always creates perfect predictions — Nó luôn dự đoán đúng tuyệt đối

B. It automatically trains a neural network — Nó tự huấn luyện mạng nơ-ron

C. It removes the need for input checks — Nó loại bỏ nhu cầu kiểm tra đầu vào

D. These operators compare values and combine conditions — So sánh và kết hợp điều kiện


**Q8. Which use matches &, |, ^? — Công dụng nào đúng với &, |, ^?**

A. It always creates perfect predictions — Nó luôn dự đoán đúng tuyệt đối

B. It automatically trains a neural network — Nó tự huấn luyện mạng nơ-ron

C. These operators work on individual bits of integers — Chỉ dùng cho cờ bit hoặc toán bit được thiết kế rõ

D. It removes the need for input checks — Nó loại bỏ nhu cầu kiểm tra đầu vào


**Q9. Which reason fits 'Discount'? — Lý do nào phù hợp với 'Tính ưu đãi'?**

A. Require both VIP conditions — Hai điều kiện đều phải đúng

B. Compute discount proportion — Nhân tỷ lệ giảm với giá để tính tiền còn lại

C. Use division and remainder — Chia nguyên đếm thùng đủ và dư đếm món lẻ

D. Inspect a device bit — Kiểm một bit bằng phép AND trên số nhị phân


**Q10. Which reason fits 'VIP eligibility'? — Lý do nào phù hợp với 'Xét VIP'?**

A. Require both VIP conditions — Hai điều kiện đều phải đúng

B. Use division and remainder — Chia nguyên đếm thùng đủ và dư đếm món lẻ

C. Inspect a device bit — Kiểm một bit bằng phép AND trên số nhị phân

D. Trigger if either threshold is crossed — Chỉ cần một trong hai ngưỡng được đáp ứng


**Q11. Which reason fits 'Packing'? — Lý do nào phù hợp với 'Đóng thùng hàng'?**

A. Inspect a device bit — Kiểm một bit bằng phép AND trên số nhị phân

B. Trigger if either threshold is crossed — Chỉ cần một trong hai ngưỡng được đáp ứng

C. Compute discount proportion — Nhân tỷ lệ giảm với giá để tính tiền còn lại

D. Use division and remainder — Chia nguyên đếm thùng đủ và dư đếm món lẻ


**Q12. Which reason fits 'Device status flag'? — Lý do nào phù hợp với 'Đọc cờ thiết bị'?**

A. Trigger if either threshold is crossed — Chỉ cần một trong hai ngưỡng được đáp ứng

B. Compute discount proportion — Nhân tỷ lệ giảm với giá để tính tiền còn lại

C. Inspect a device bit — Kiểm một bit bằng phép AND trên số nhị phân

D. Require both VIP conditions — Hai điều kiện đều phải đúng


**Q13. Which reason fits 'Priority'? — Lý do nào phù hợp với 'Ưu tiên đơn hàng'?**

A. Compute discount proportion — Nhân tỷ lệ giảm với giá để tính tiền còn lại

B. Trigger if either threshold is crossed — Chỉ cần một trong hai ngưỡng được đáp ứng

C. Require both VIP conditions — Hai điều kiện đều phải đúng

D. Use division and remainder — Chia nguyên đếm thùng đủ và dư đếm món lẻ


**Q14. Which input fits 'Discount'? — Dữ liệu nào được dùng cho 'Tính ưu đãi'?**

A. The sample described for Discount — Giá 250000 đồng giảm 10%

B. Input from VIP eligibility — Khách 5 năm, chi 1200000 đồng

C. Input from Packing — 23 sản phẩm, 5 sản phẩm/thùng

D. Input from Device status flag — Trạng thái mô phỏng 0b1010


**Q15. Which input fits 'VIP eligibility'? — Dữ liệu nào được dùng cho 'Xét VIP'?**

A. Input from Packing — 23 sản phẩm, 5 sản phẩm/thùng

B. Input from Device status flag — Trạng thái mô phỏng 0b1010

C. Input from Priority — Giá trị 3000000 đồng hoặc trễ 2 ngày

D. The sample described for VIP eligibility — Khách 5 năm, chi 1200000 đồng


**Q16. Which input fits 'Packing'? — Dữ liệu nào được dùng cho 'Đóng thùng hàng'?**

A. Input from Device status flag — Trạng thái mô phỏng 0b1010

B. Input from Priority — Giá trị 3000000 đồng hoặc trễ 2 ngày

C. The sample described for Packing — 23 sản phẩm, 5 sản phẩm/thùng

D. Input from Discount — Giá 250000 đồng giảm 10%


**Q17. Which input fits 'Device status flag'? — Dữ liệu nào được dùng cho 'Đọc cờ thiết bị'?**

A. Input from Priority — Giá trị 3000000 đồng hoặc trễ 2 ngày

B. The sample described for Device status flag — Trạng thái mô phỏng 0b1010

C. Input from Discount — Giá 250000 đồng giảm 10%

D. Input from VIP eligibility — Khách 5 năm, chi 1200000 đồng


**Q18. Which input fits 'Priority'? — Dữ liệu nào được dùng cho 'Ưu tiên đơn hàng'?**

A. The sample described for Priority — Giá trị 3000000 đồng hoặc trễ 2 ngày

B. Input from Discount — Giá 250000 đồng giảm 10%

C. Input from VIP eligibility — Khách 5 năm, chi 1200000 đồng

D. Input from Packing — 23 sản phẩm, 5 sản phẩm/thùng


**Q19. What must be checked before processing input? — Cần xác định gì trước xử lý?**

A. Only text size — Chỉ kích thước chữ

B. Only the file name length — Chỉ độ dài tên file

C. Only program comments — Chỉ phần comment

D. Input meaning, type and units — Ý nghĩa, kiểu và đơn vị đầu vào


**Q20. What should follow a successful example? — Sau khi ví dụ chạy đúng nên làm gì?**

A. Assume all datasets work identically — Cho rằng mọi bộ dữ liệu giống nhau

B. Delete all tests — Xóa toàn bộ kiểm thử

C. Validate output and edge cases — Kiểm tra kết quả và trường hợp biên

D. Ignore input errors — Bỏ qua lỗi nhập liệu

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **B** | Math operations on numbers | Phép cộng trừ nhân chia |
| Q2 | **A** | A true-or-false comparison | So sánh hai giá trị |
| Q3 | **D** | Combining boolean conditions | Kết hợp các điều kiện |
| Q4 | **C** | Operations on binary digits | Phép tính trên các bit của số nguyên |
| Q5 | **B** | These operators perform arithmetic calculations | Tính số học và tỷ lệ |
| Q6 | **A** | These operators calculate floor division, remainder and powers | Chia nguyên, lấy dư, lũy thừa |
| Q7 | **D** | These operators compare values and combine conditions | So sánh và kết hợp điều kiện |
| Q8 | **C** | These operators work on individual bits of integers | Chỉ dùng cho cờ bit hoặc toán bit được thiết kế rõ |
| Q9 | **B** | Compute discount proportion | Nhân tỷ lệ giảm với giá để tính tiền còn lại |
| Q10 | **A** | Require both VIP conditions | Hai điều kiện đều phải đúng |
| Q11 | **D** | Use division and remainder | Chia nguyên đếm thùng đủ và dư đếm món lẻ |
| Q12 | **C** | Inspect a device bit | Kiểm một bit bằng phép AND trên số nhị phân |
| Q13 | **B** | Trigger if either threshold is crossed | Chỉ cần một trong hai ngưỡng được đáp ứng |
| Q14 | **A** | The sample described for Discount | Giá 250000 đồng giảm 10% |
| Q15 | **D** | The sample described for VIP eligibility | Khách 5 năm, chi 1200000 đồng |
| Q16 | **C** | The sample described for Packing | 23 sản phẩm, 5 sản phẩm/thùng |
| Q17 | **B** | The sample described for Device status flag | Trạng thái mô phỏng 0b1010 |
| Q18 | **A** | The sample described for Priority | Giá trị 3000000 đồng hoặc trễ 2 ngày |
| Q19 | **D** | Input meaning, type and units | Ý nghĩa, kiểu và đơn vị đầu vào |
| Q20 | **C** | Validate output and edge cases | Kiểm tra kết quả và trường hợp biên |

## 8. Nối sang bài kế tiếp

`Kiểu dữ liệu → Toán tử → Điều kiện → Quy tắc nghiệp vụ`.

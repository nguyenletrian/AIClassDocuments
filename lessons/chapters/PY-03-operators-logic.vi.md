# PY-03 — Toán tử số học, so sánh và logic


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Arithmetic** — số học; **Comparison** — so sánh.

`Kiểu dữ liệu → Toán tử → Điều kiện → Quy tắc nghiệp vụ`

Khái niệm trong bài nằm ở bước này của chuỗi học; hãy hiểu đầu vào, thao tác và đầu ra trước khi dùng cho dữ liệu AI.

## 2. English vocabulary — Từ vựng

| English | Nghĩa tiếng Việt | Giải thích |
|---|---|---|
| Arithmetic | số học | Phép cộng trừ nhân chia |
| Comparison | so sánh | Đối chiếu hai giá trị |
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


## 4. Khái niệm liên quan — từ lời giải thích đến Python

### 4.1. Arithmetic

**Từ vựng trong mục:** **Arithmetic** — số học.

Phép cộng trừ nhân chia. xác định giá trị đầu vào có ý nghĩa gì.

```python
print(5 * 3)
```

**Tự kiểm tra:** Arithmetic có ý nghĩa gì?

**Đáp án:** Phép cộng trừ nhân chia.

### 4.2. Comparison

**Từ vựng trong mục:** **Comparison** — so sánh.

Đối chiếu hai giá trị. xác định giá trị đầu vào có ý nghĩa gì.

```python
print(8 >= 5)
```

**Tự kiểm tra:** Comparison có ý nghĩa gì?

**Đáp án:** Đối chiếu hai giá trị.

### 4.3. Logical

**Từ vựng trong mục:** **Logical** — logic.

Kết hợp các điều kiện. xác định giá trị đầu vào có ý nghĩa gì.

```python
print(True and False)
```

**Tự kiểm tra:** Logical có ý nghĩa gì?

**Đáp án:** Kết hợp các điều kiện.

### 4.4. Bitwise

**Từ vựng trong mục:** **Bitwise** — thao tác bit.

Phép tính trên các bit của số nguyên. xác định giá trị đầu vào có ý nghĩa gì.

```python
print(5 & 3)
```

**Tự kiểm tra:** Bitwise có ý nghĩa gì?

**Đáp án:** Phép tính trên các bit của số nguyên.

## 5. Năm tình huống lập trình thực tế

### Tình huống 1 — Tính ưu đãi

**Từ vựng trong mục:** **Arithmetic** — số học.

**Vấn đề:** Tính ưu đãi.

**Vì sao chọn cách này?** Nhân tỷ lệ giảm với giá để tính tiền còn lại.

**Dữ liệu:** Giá 250000 đồng giảm 10%.

**Quy trình:** xác định đầu vào → thực hiện phép tính / điều kiện → in kết quả → kiểm tra các trường hợp khác.

```python
price = 250000
print(price * (1 - 0.10))
```


### Tình huống 2 — Xét VIP

**Từ vựng trong mục:** **Comparison** — so sánh.

**Vấn đề:** Xét VIP.

**Vì sao chọn cách này?** Hai điều kiện đều phải đúng.

**Dữ liệu:** Khách 5 năm, chi 1200000 đồng.

**Quy trình:** xác định đầu vào → thực hiện phép tính / điều kiện → in kết quả → kiểm tra các trường hợp khác.

```python
years, spending = 5, 1200000
print(years >= 5 and spending >= 1000000)
```


### Tình huống 3 — Đóng thùng hàng

**Từ vựng trong mục:** **Logical** — logic.

**Vấn đề:** Đóng thùng hàng.

**Vì sao chọn cách này?** Chia nguyên đếm thùng đủ và dư đếm món lẻ.

**Dữ liệu:** 23 sản phẩm, 5 sản phẩm/thùng.

**Quy trình:** xác định đầu vào → thực hiện phép tính / điều kiện → in kết quả → kiểm tra các trường hợp khác.

```python
items, box_size = 23, 5
print(items // box_size, items % box_size)
```


### Tình huống 4 — Đọc cờ thiết bị

**Từ vựng trong mục:** **Bitwise** — thao tác bit.

**Vấn đề:** Đọc cờ thiết bị.

**Vì sao chọn cách này?** Kiểm một bit bằng phép AND trên số nhị phân.

**Dữ liệu:** Trạng thái mô phỏng 0b1010.

**Quy trình:** xác định đầu vào → thực hiện phép tính / điều kiện → in kết quả → kiểm tra các trường hợp khác.

```python
status = 0b1010
print(bool(status & 0b0010))
```


### Tình huống 5 — Ưu tiên đơn hàng

**Từ vựng trong mục:** **Arithmetic** — số học.

**Vấn đề:** Ưu tiên đơn hàng.

**Vì sao chọn cách này?** Chỉ cần một trong hai ngưỡng được đáp ứng.

**Dữ liệu:** Giá trị 3000000 đồng hoặc trễ 2 ngày.

**Quy trình:** xác định đầu vào → thực hiện phép tính / điều kiện → in kết quả → kiểm tra các trường hợp khác.

```python
amount, delay = 3000000, 0
print(amount >= 2000000 or delay > 2)
```


## 6. Những nhầm lẫn thường gặp

- Không suy diễn từ một ví dụ minh họa sang mọi bộ dữ liệu thật.
- Dùng phép xử lý phù hợp với kiểu dữ liệu và đơn vị đo. Khi có đầu vào người dùng, cần kiểm tra lỗi.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is Arithmetic? — Thuật ngữ Arithmetic có nghĩa gì?**

A. A true-or-false comparison — Đối chiếu hai giá trị

B. Math operations on numbers — Phép cộng trừ nhân chia

C. Combining boolean conditions — Kết hợp các điều kiện

D. Operations on binary digits — Phép tính trên các bit của số nguyên


**Q2. What is Comparison? — Thuật ngữ Comparison có nghĩa gì?**

A. A true-or-false comparison — Đối chiếu hai giá trị

B. Combining boolean conditions — Kết hợp các điều kiện

C. Operations on binary digits — Phép tính trên các bit của số nguyên

D. Math operations on numbers — Phép cộng trừ nhân chia


**Q3. What is Logical? — Thuật ngữ Logical có nghĩa gì?**

A. Operations on binary digits — Phép tính trên các bit của số nguyên

B. Math operations on numbers — Phép cộng trừ nhân chia

C. A true-or-false comparison — Đối chiếu hai giá trị

D. Combining boolean conditions — Kết hợp các điều kiện


**Q4. What is Bitwise? — Thuật ngữ Bitwise có nghĩa gì?**

A. Math operations on numbers — Phép cộng trừ nhân chia

B. A true-or-false comparison — Đối chiếu hai giá trị

C. Operations on binary digits — Phép tính trên các bit của số nguyên

D. Combining boolean conditions — Kết hợp các điều kiện


**Q5. Which use matches +, -, *, /? — Công dụng nào đúng với +, -, *, /?**

A. It always creates perfect predictions — Nó luôn dự đoán đúng tuyệt đối

B. This Python operation supports the described task — Tính số học và tỷ lệ

C. It automatically trains a neural network — Nó tự huấn luyện mạng nơ-ron

D. It removes the need for input checks — Nó loại bỏ nhu cầu kiểm tra đầu vào


**Q6. Which use matches //, %, **? — Công dụng nào đúng với //, %, **?**

A. This Python operation supports the described task — Chia nguyên, lấy dư, lũy thừa

B. It always creates perfect predictions — Nó luôn dự đoán đúng tuyệt đối

C. It automatically trains a neural network — Nó tự huấn luyện mạng nơ-ron

D. It removes the need for input checks — Nó loại bỏ nhu cầu kiểm tra đầu vào


**Q7. Which use matches ==, !=, <=, >=, and, or? — Công dụng nào đúng với ==, !=, <=, >=, and, or?**

A. It always creates perfect predictions — Nó luôn dự đoán đúng tuyệt đối

B. It automatically trains a neural network — Nó tự huấn luyện mạng nơ-ron

C. It removes the need for input checks — Nó loại bỏ nhu cầu kiểm tra đầu vào

D. This Python operation supports the described task — So sánh và kết hợp điều kiện


**Q8. Which use matches &, |, ^? — Công dụng nào đúng với &, |, ^?**

A. It always creates perfect predictions — Nó luôn dự đoán đúng tuyệt đối

B. It automatically trains a neural network — Nó tự huấn luyện mạng nơ-ron

C. This Python operation supports the described task — Chỉ dùng cho cờ bit hoặc toán bit được thiết kế rõ

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
| Q2 | **A** | A true-or-false comparison | Đối chiếu hai giá trị |
| Q3 | **D** | Combining boolean conditions | Kết hợp các điều kiện |
| Q4 | **C** | Operations on binary digits | Phép tính trên các bit của số nguyên |
| Q5 | **B** | This Python operation supports the described task | Tính số học và tỷ lệ |
| Q6 | **A** | This Python operation supports the described task | Chia nguyên, lấy dư, lũy thừa |
| Q7 | **D** | This Python operation supports the described task | So sánh và kết hợp điều kiện |
| Q8 | **C** | This Python operation supports the described task | Chỉ dùng cho cờ bit hoặc toán bit được thiết kế rõ |
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

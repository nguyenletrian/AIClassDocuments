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

**Vấn đề thực tế:** Một cửa hàng bán sản phẩm có giá niêm yết 250.000 đồng và áp dụng mức giảm giá 10% trên giá niêm yết.

**Yêu cầu:** Viết Python tính số tiền khách phải thanh toán sau khi giảm giá.

**Vì sao chọn cách giải này?** Phép nhân với `(1 - 0.10)` lấy trực tiếp 90% giá gốc, là số tiền còn phải trả.

**Quy trình giải:**

1. Lưu giá niêm yết `price = 250000` (đồng).
2. Chuyển mức giảm 10% thành tỷ lệ `0.10`.
3. Nhân giá với phần tỷ lệ còn lại và in số tiền phải trả.

```python
price = 250000
print(price * (1 - 0.10))
```

**Kết quả:** `225000.0` đồng, tương ứng giá gốc trừ 25.000 đồng.

### Tình huống 2 — Xét VIP

**Từ vựng trong mục:** **Comparison** — so sánh.

**Vấn đề thực tế:** Cửa hàng chỉ công nhận khách hàng VIP khi họ là thành viên **ít nhất 5 năm** và có tổng chi tiêu **từ 1.000.000 đồng**. Một khách đã tham gia 5 năm và chi 1.200.000 đồng.

**Yêu cầu:** Viết chương trình xác định khách hàng này có đủ điều kiện VIP hay không.

**Vì sao chọn cách giải này?** Hai điều kiện phải đồng thời đúng, nên dùng toán tử logic `and` để kết hợp hai phép so sánh ngưỡng `>=`.

**Quy trình giải:**

1. Lưu số năm là thành viên và tổng chi tiêu.
2. Kiểm tra `years >= 5` và `spending >= 1000000`.
3. Dùng `and` để trả về `True` chỉ khi cả hai điều kiện đúng.

```python
years, spending = 5, 1200000
print(years >= 5 and spending >= 1000000)
```

**Kết quả:** `True` — khách hàng đủ điều kiện VIP vì đạt cả ngưỡng thời gian lẫn chi tiêu.

### Tình huống 3 — Đóng thùng hàng

**Từ vựng trong mục:** **Logical** — logic.

**Vấn đề thực tế:** Một kho cần đóng 23 sản phẩm vào các thùng, mỗi thùng chứa đúng 5 sản phẩm khi đầy. Các sản phẩm còn dư được để riêng.

**Yêu cầu:** Tính số thùng đầy và số sản phẩm chưa đủ để đóng thêm một thùng.

**Vì sao chọn cách giải này?** Chia nguyên `//` đếm số nhóm đủ 5 món, còn phép chia lấy dư `%` cho biết số món chưa đủ một thùng.

**Quy trình giải:**

1. Ghi số sản phẩm `23` và sức chứa `5`.
2. Tính `items // box_size` để đếm thùng đầy.
3. Tính `items % box_size` để đếm sản phẩm dư.

```python
items, box_size = 23, 5
print(items // box_size, items % box_size)
```

**Kết quả:** `4 3` — đóng được 4 thùng đầy và còn 3 sản phẩm.

### Tình huống 4 — Đọc cờ thiết bị

**Từ vựng trong mục:** **Bitwise** — thao tác bit.

**Vấn đề thực tế:** Bộ điều khiển lưu trạng thái bốn công tắc trong số nhị phân `0b1010`. Bit `0b0010` biểu thị công tắc thứ hai tính từ phải qua có đang bật hay không.

**Yêu cầu:** Viết chương trình kiểm tra công tắc này đang bật (`True`) hay tắt (`False`).

**Vì sao chọn cách giải này?** Phép AND bit `&` giữ lại đúng vị trí bit cần kiểm tra; `bool` chuyển kết quả khác 0 thành `True`.

**Quy trình giải:**

1. Lưu trạng thái thiết bị dưới dạng `0b1010`.
2. Dùng mặt nạ `0b0010` với toán tử `&`.
3. Chuyển thành Boolean và in trạng thái.

```python
status = 0b1010
print(bool(status & 0b0010))
```

**Kết quả:** `True` — bit `0b0010` đang bật trong trạng thái `0b1010`.

### Tình huống 5 — Ưu tiên đơn hàng

**Từ vựng trong mục:** **Arithmetic** — số học.

**Vấn đề thực tế:** Cửa hàng ưu tiên xử lý đơn hàng nếu **giá trị từ 2.000.000 đồng** hoặc **bị trễ hơn 2 ngày**. Một đơn có giá trị 3.000.000 đồng và hiện chưa bị trễ (`delay = 0` ngày).

**Yêu cầu:** Viết chương trình kiểm tra đơn này có thuộc diện ưu tiên hay không.

**Vì sao chọn cách giải này?** Điều kiện ưu tiên chỉ cần đạt một trong hai ngưỡng, nên dùng toán tử `or` để kết hợp các phép so sánh.

**Quy trình giải:**

1. Lưu giá trị đơn `amount` và số ngày trễ `delay`.
2. Kiểm tra `amount >= 2000000`.
3. Kiểm tra `delay > 2`, rồi nối hai kết quả bằng `or`.

```python
amount, delay = 3000000, 0
print(amount >= 2000000 or delay > 2)
```

**Kết quả:** `True` — đơn được ưu tiên vì giá trị đạt ngưỡng dù chưa trễ ngày nào.

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

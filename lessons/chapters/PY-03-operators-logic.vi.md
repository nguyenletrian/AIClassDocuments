# PY-03 — Toán tử số học, so sánh và logic


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Arithmetic** — số học; **Comparison** — so sánh.

`Kiểu dữ liệu → Toán tử → Điều kiện → Quy tắc nghiệp vụ`

**Học xong dùng để làm gì?** Tính tổng tiền, so sánh ngưỡng điểm và kết hợp nhiều điều kiện thành kết quả đúng/sai.

**Kết nối kiến thức tiếp theo:** Sang PY-04, dùng chính các phép so sánh và logic đó để quyết định chương trình đi nhánh nào.

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

**Toán tử (operator)** là dấu hoặc từ khóa thực hiện một thao tác trên dữ liệu. Với một đơn hàng, ta dùng toán tử số học để tính tiền, so sánh để kiểm tra ngưỡng, rồi dùng logic để ghép điều kiện. Toán tử bit cũng dùng ký hiệu nhưng xử lý các chữ số nhị phân thay vì điều kiện thông thường.

### 4.1. Arithmetic — Toán tử số học

**Từ vựng trong mục:** **Arithmetic** — số học; **Multiplication** — phép nhân.

Số học giúp tính từ các dữ liệu có sẵn: `+` cộng, `-` trừ, `*` nhân, `/` chia. Ví dụ cửa hàng bán 5 món, mỗi món 3 nghìn đồng: lấy số lượng nhân đơn giá để được tổng 15 nghìn đồng. Python còn có `//` chia lấy phần nguyên và `%` lấy phần dư khi chia thùng hoặc chia nhóm.

```python
print(5 * 3)
```

**Kết quả khi chạy:**

```text
15
```

Giá trị `15` là tổng tiền theo đơn vị nghìn đồng của ví dụ.

### 4.2. Comparison — Toán tử so sánh

**Từ vựng trong mục:** **Comparison** — so sánh; **Boolean** — đúng/sai.

So sánh trả lời một câu hỏi bằng `True` hoặc `False`. Nếu kho có 8 món và đơn hàng cần 5 món, điều kiện `8 >= 5` kiểm tra đủ hàng để giao không. Các dấu `>`, `<`, `>=`, `<=`, `==`, `!=` biểu diễn lớn hơn, nhỏ hơn, bằng hoặc khác nhau. Phân biệt `==` để kiểm tra với `=` để gán.

```python
print(8 >= 5)
```

**Kết quả khi chạy:**

```text
True
```

Kho có ít nhất 5 món nên điều kiện đủ hàng là đúng.

### 4.3. Logical — Toán tử logic

**Từ vựng trong mục:** **Logical** — logic; **AND** — và; **OR** — hoặc.

Sau khi có các điều kiện đúng/sai, `and` yêu cầu mọi điều kiện cùng đúng; `or` chỉ cần một điều kiện đúng; `not` đảo trạng thái. Ví dụ người dùng đã đăng nhập (`True`) nhưng chưa xác minh (`False`): nếu hệ thống bắt buộc cả hai thì `and` trả về `False`.

```python
print(True and False)
```

**Kết quả khi chạy:**

```text
False
```

Một trong hai điều kiện chưa đạt, nên không thỏa yêu cầu `and`.

### 4.4. Bitwise — Toán tử theo bit

**Từ vựng trong mục:** **Bitwise** — theo bit; **Binary** — nhị phân.

Máy tính biểu diễn số nguyên bằng các bit `0` và `1`. Toán tử `&` so từng vị trí bit và chỉ giữ `1` khi hai phía cùng có `1`. Số 5 là `0101`, số 3 là `0011`; phần chung chỉ còn `0001`, tương ứng số 1. Đây là phép xử lý số nguyên theo bit, **khác** `and` dùng để nối điều kiện logic.

```python
print(5 & 3)
```

**Kết quả khi chạy:**

```text
1
```

Số `1` là kết quả phép AND theo bit giữa 5 và 3.
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

**Q1. Which operator performs multiplication? — Toán tử nào thực hiện phép nhân?**

A. `*` — `*`

B. `&` — `&`

C. `==` — `==`

D. `and` — `and`

**Đáp án: A**

**Giải thích:** `*` nhân các số, ví dụ `3 * 4` cho `12`. `==` so sánh giá trị, `and` kết hợp điều kiện logic, còn `&` thực hiện AND theo bit trên số nguyên.


**Q2. Which operator tests equality? — Toán tử nào kiểm tra bằng nhau?**

A. `*` — `*`

B. `==` — `==`

C. `&` — `&`

D. `and` — `and`

**Đáp án: B**

**Giải thích:** `==` kiểm tra hai giá trị có bằng nhau và tạo Boolean, ví dụ `2 == 2` là `True`. Một dấu `=` dùng để gán giá trị cho tên, chứ không so sánh.


**Q3. Which Python keyword performs short-circuit logical AND? — Từ khóa Python nào thực hiện phép VÀ logic có đánh giá ngắn mạch?**

A. `==` — `==`

B. `&` — `&`

C. `and` — `and`

D. `*` — `*`

**Đáp án: C**

**Giải thích:** Từ khóa `and` thực hiện phép VÀ logic ngắn mạch: nếu vế trái sai, Python không đánh giá vế phải. Ký hiệu `&` thực hiện AND theo bit trên số nguyên và kể cả dùng với Boolean cũng không đánh giá ngắn mạch.


**Q4. Which operator performs bitwise AND on integers? — Toán tử nào thực hiện AND theo bit trên số nguyên?**

A. `and` — `and`

B. `==` — `==`

C. `*` — `*`

D. `&` — `&`

**Đáp án: D**

**Giải thích:** Với số nguyên, `&` thực hiện AND trên từng bit: `5 & 3` đối chiếu `0101` và `0011`, được `0001` (`1`). Đây không phải phép nhân thông thường hay từ khóa logic `and`.


**Q5. What does `7 // 2` return? — `7 // 2` trả về gì?**

A. `1` — `1`

B. `3.5` — `3.5`

C. `3` — `3`

D. `8` — `8`

**Đáp án: C**

**Giải thích:** `//` thực hiện chia lấy sàn: `7 / 2` bằng `3.5`, làm tròn xuống được `3`. Với thương âm, làm tròn xuống nghĩa là về âm vô cực nên `-7 // 2` bằng `-4`.


**Q6. What does `7 % 2` return? — `7 % 2` trả về gì?**

A. `1` — `1`

B. `3.5` — `3.5`

C. `3` — `3`

D. `8` — `8`

**Đáp án: A**

**Giải thích:** `%` trả phần dư theo phép chia lấy sàn: `7 = 2 * 3 + 1`, nên `7 % 2` bằng `1`. Nó không phải thương `3` hay kết quả chia thực `3.5`.


**Q7. What does `2 ** 3` return? — `2 ** 3` trả về gì?**

A. `3` — `3`

B. `1` — `1`

C. `3.5` — `3.5`

D. `8` — `8`

**Đáp án: D**

**Giải thích:** `**` là phép lũy thừa: `2 ** 3` nhân 2 với chính nó ba lần, cho `8`. Một dấu `*` là phép nhân, còn `^` trong Python là XOR theo bit, không phải lũy thừa.


**Q8. What does `7 / 2` return? — `7 / 2` trả về gì?**

A. `3.5` — `3.5`

B. `3` — `3`

C. `1` — `1`

D. `8` — `8`

**Đáp án: A**

**Giải thích:** Trong Python 3, `/` chia thực nên `7 / 2` trả về số thực `3.5`. Toán tử `//` lấy sàn thương được `3`, còn `%` trả phần dư `1`.


**Q9. What is `True and False`? — `True and False` bằng gì?**

A. `True` (Boolean) — `True` (Boolean)

B. `None` — `None`

C. `0` (integer) — `0` (số nguyên)

D. `False` (Boolean) — `False` (Boolean)

**Đáp án: D**

**Giải thích:** `and` Boolean yêu cầu cả hai vế đều đúng, nhưng vế thứ hai là `False`. Vì thế `True and False` cho Boolean `False`, không phải số nguyên `0` hay `None`.


**Q10. What is `False or True`? — `False or True` bằng gì?**

A. `1` (integer) — `1` (số nguyên)

B. `True` (Boolean) — `True` (Boolean)

C. `False` (Boolean) — `False` (Boolean)

D. `None` — `None`

**Đáp án: B**

**Giải thích:** `or` Boolean đúng nếu có ít nhất một vế đúng; vế phải của `False or True` là `True`. Kết quả ở đây là Boolean `True`, không phải số nguyên `1`, dù `True` có thể hoạt động như 1 trong một số phép số học.


**Q11. What does `not True` produce? — `not True` cho kết quả gì?**

A. `0` (integer) — `0` (số nguyên)

B. `None` — `None`

C. `False` (Boolean) — `False` (Boolean)

D. `True` (Boolean) — `True` (Boolean)

**Đáp án: C**

**Giải thích:** `not` đảo giá trị logic nên `not True` thành Boolean `False`. Ngược lại `not False` là `True`; số nguyên không là giá trị thuộc kiểu khác.


**Q12. What does `5 & 3` produce? — `5 & 3` tạo ra gì?**

A. `False` (Boolean) — `False` (Boolean)

B. `5` (integer) — `5` (số nguyên)

C. `True` (Boolean) — `True` (Boolean)

D. `1` (integer) — `1` (số nguyên)

**Đáp án: D**

**Giải thích:** Hai số nguyên là `5 = 0101` và `3 = 0011` ở hệ nhị phân bốn bit. Toán tử `&` chỉ giữ vị trí có cả hai bit bằng 1, cho `0001`, tức số nguyên `1`, không phải Boolean `True`.


**Q13. Which operator tests that two values differ? — Toán tử nào kiểm tra hai giá trị khác nhau?**

A. `!=` — `!=`

B. `>=` — `>=`

C. `=` — `=`

D. `in` — `in`

**Đáp án: A**

**Giải thích:** `!=` kiểm tra hai giá trị có khác nhau: `3 != 4` là `True`, còn `3 != 3` là `False`. Nó đối lập với `==` dùng để kiểm tra bằng nhau.


**Q14. Which operator means 'at least'? — Toán tử nào biểu diễn 'lớn hơn hoặc bằng'?**

A. `!=` — `!=`

B. `in` — `in`

C. `>=` — `>=`

D. `=` — `=`

**Đáp án: C**

**Giải thích:** `>=` nghĩa là lớn hơn hoặc bằng, nên `5 >= 5` và `6 >= 5` đều là `True`. Trường hợp bằng ngưỡng rất quan trọng: dùng `>` sẽ loại đúng giá trị 5.


**Q15. Which operator checks membership in a collection? — Toán tử nào kiểm tra phần tử thuộc một tập dữ liệu?**

A. `!=` — `!=`

B. `in` — `in`

C. `>=` — `>=`

D. `=` — `=`

**Đáp án: B**

**Giải thích:** Toán tử `in` kiểm tra phần tử có thuộc tập hợp: `2 in [1, 2, 3]` là `True`, còn `4 in [1, 2, 3]` là `False`. Nó không gán giá trị hay so sánh độ lớn.


**Q16. Which operator assigns a new value to a variable? — Toán tử nào gán giá trị mới cho biến?**

A. `>=` — `>=`

B. `!=` — `!=`

C. `=` — `=`

D. `in` — `in`

**Đáp án: C**

**Giải thích:** Toán tử gán `=` liên kết tên với giá trị, như `total = 10`. Muốn so sánh hai giá trị thì dùng `==`; dùng `=` trong điều kiện so sánh thông thường sẽ sai cú pháp.


**Q17. Which result comes from `3 > 5`? — `3 > 5` trả về gì?**

A. `0` (integer) — `0` (số nguyên)

B. `False` (Boolean) — `False` (Boolean)

C. `True` (Boolean) — `True` (Boolean)

D. `None` — `None`

**Đáp án: B**

**Giải thích:** `>` kiểm tra lớn hơn nghiêm ngặt, mà 3 nhỏ hơn 5 nên `3 > 5` cho Boolean `False`. Kết quả là giá trị logic, không phải số nguyên `0`.


**Q18. What result comes from `2 + 3 * 4`? — `2 + 3 * 4` bằng bao nhiêu?**

A. `9` — `9`

B. `14` — `14`

C. `False` — `False`

D. `20` — `20`

**Đáp án: B**

**Giải thích:** Phép nhân có độ ưu tiên cao hơn cộng: tính `3 * 4 = 12` trước, rồi `2 + 12 = 14`. Thêm ngoặc như `(2 + 3) * 4` sẽ đổi kết quả thành `20`.


**Q19. What does `True or False` return? — `True or False` trả về gì?**

A. `True` (Boolean) — `True` (Boolean)

B. `1` (integer) — `1` (số nguyên)

C. `False` (Boolean) — `False` (Boolean)

D. `None` — `None`

**Đáp án: A**

**Giải thích:** `or` đúng khi ít nhất một toán hạng Boolean đúng; vì vế trái là `True` nên `True or False` trả `True`. Với đầu vào Boolean, đây là Boolean `True`, không phải số nguyên `1`.


**Q20. What does `5 ^ 3` return for integers? — `5 ^ 3` trả về gì với số nguyên?**

A. `5` — `5`

B. `2` — `2`

C. `15` — `15`

D. `6` — `6`

**Đáp án: D**

**Giải thích:** `^` là XOR theo bit, không phải lũy thừa: `5 = 0101` và `3 = 0011` khác nhau tại các vị trí bit `0100` và `0010`, cho `0110` = `6`. Lũy thừa phải dùng `**`, không dùng `^`.

## 8. Nối sang bài kế tiếp

`Kiểu dữ liệu → Toán tử → Điều kiện → Quy tắc nghiệp vụ`.

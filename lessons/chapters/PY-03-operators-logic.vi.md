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

B. `==` — `==`

C. `and` — `and`

D. `&` — `&`

**Q2. Which operator tests equality? — Toán tử nào kiểm tra bằng nhau?**

A. `*` — `*`

B. `==` — `==`

C. `and` — `and`

D. `&` — `&`

**Q3. Which operator represents logical AND? — Toán tử nào biểu diễn phép VÀ logic?**

A. `*` — `*`

B. `==` — `==`

C. `and` — `and`

D. `&` — `&`

**Q4. Which operator performs bitwise AND on integers? — Toán tử nào thực hiện AND theo bit trên số nguyên?**

A. `*` — `*`

B. `==` — `==`

C. `and` — `and`

D. `&` — `&`

**Q5. What does `7 // 2` return? — `7 // 2` trả về gì?**

A. `3` — `3`

B. `1` — `1`

C. `8` — `8`

D. `3.5` — `3.5`

**Q6. What does `7 % 2` return? — `7 % 2` trả về gì?**

A. `3` — `3`

B. `1` — `1`

C. `8` — `8`

D. `3.5` — `3.5`

**Q7. What does `2 ** 3` return? — `2 ** 3` trả về gì?**

A. `3` — `3`

B. `1` — `1`

C. `8` — `8`

D. `3.5` — `3.5`

**Q8. What does `7 / 2` return? — `7 / 2` trả về gì?**

A. `3` — `3`

B. `1` — `1`

C. `8` — `8`

D. `3.5` — `3.5`

**Q9. What is `True and False`? — `True and False` bằng gì?**

A. `False` — `False`

B. `True` — `True`

C. The opposite Boolean value — Giá trị Boolean đảo ngược

D. The integer `1` — Số nguyên `1`

**Q10. What is `False or True`? — `False or True` bằng gì?**

A. `False` — `False`

B. `True` — `True`

C. The opposite Boolean value — Giá trị Boolean đảo ngược

D. The integer `1` — Số nguyên `1`

**Q11. What does `not True` produce? — `not True` cho kết quả gì?**

A. `False` — `False`

B. `True` — `True`

C. The opposite Boolean value — Giá trị Boolean đảo ngược

D. The integer `1` — Số nguyên `1`

**Q12. What does `5 & 3` produce? — `5 & 3` tạo ra gì?**

A. `False` — `False`

B. `True` — `True`

C. The opposite Boolean value — Giá trị Boolean đảo ngược

D. The integer `1` — Số nguyên `1`

**Q13. Which operator tests that two values differ? — Toán tử nào kiểm tra hai giá trị khác nhau?**

A. `!=` — `!=`

B. `>=` — `>=`

C. `in` — `in`

D. `=` — `=`

**Q14. Which operator means 'at least'? — Toán tử nào biểu diễn 'lớn hơn hoặc bằng'?**

A. `!=` — `!=`

B. `>=` — `>=`

C. `in` — `in`

D. `=` — `=`

**Q15. Which operator checks membership in a collection? — Toán tử nào kiểm tra phần tử thuộc một tập dữ liệu?**

A. `!=` — `!=`

B. `>=` — `>=`

C. `in` — `in`

D. `=` — `=`

**Q16. Which operator assigns a new value to a variable? — Toán tử nào gán giá trị mới cho biến?**

A. `!=` — `!=`

B. `>=` — `>=`

C. `in` — `in`

D. `=` — `=`

**Q17. Which result comes from `3 > 5`? — `3 > 5` trả về gì?**

A. `False` — `False`

B. `14` — `14`

C. `True` — `True`

D. `6` — `6`

**Q18. What result comes from `2 + 3 * 4`? — `2 + 3 * 4` bằng bao nhiêu?**

A. `False` — `False`

B. `14` — `14`

C. `True` — `True`

D. `6` — `6`

**Q19. What does `True or False` return? — `True or False` trả về gì?**

A. `False` — `False`

B. `14` — `14`

C. `True` — `True`

D. `6` — `6`

**Q20. What does `5 ^ 3` return for integers? — `5 ^ 3` trả về gì với số nguyên?**

A. `False` — `False`

B. `14` — `14`

C. `True` — `True`

D. `6` — `6`

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **A** | The star operator multiplies numeric operands. | Dấu sao nhân các toán hạng số. |
| Q2 | **B** | Double equals compares values; a single equals assigns. | Hai dấu bằng so sánh giá trị; một dấu bằng dùng để gán. |
| Q3 | **C** | and requires both Boolean conditions to be true. | and chỉ đúng khi cả hai điều kiện đúng. |
| Q4 | **D** | The ampersand combines corresponding binary bits. | Dấu & xử lý các bit tương ứng của số nguyên. |
| Q5 | **A** | Floor division rounds the mathematical quotient down. | Phép // lấy phần nguyên theo hướng làm tròn xuống. |
| Q6 | **B** | 7 divided by 2 leaves remainder 1. | Chia 7 cho 2 có dư 1. |
| Q7 | **C** | The double star denotes exponentiation, 2 cubed. | Hai dấu sao biểu diễn lũy thừa, 2 mũ 3. |
| Q8 | **D** | The slash performs true division in Python 3. | Dấu / thực hiện phép chia cho kết quả số thực trong Python 3. |
| Q9 | **A** | Logical AND fails if either condition is false. | AND sai khi ít nhất một điều kiện sai. |
| Q10 | **B** | Logical OR is true if either operand is true. | OR đúng khi có ít nhất một điều kiện đúng. |
| Q11 | **C** | not negates a Boolean expression. | not phủ định biểu thức Boolean. |
| Q12 | **D** | Binary 0101 AND 0011 equals 0001. | Nhị phân 0101 AND 0011 bằng 0001. |
| Q13 | **A** | Not-equal checks inequality. | != kiểm tra hai giá trị không bằng nhau. |
| Q14 | **B** | Greater-than-or-equal includes the boundary value. | >= bao gồm cả giá trị ở ngưỡng. |
| Q15 | **C** | in tests whether a value occurs in a collection. | in kiểm tra giá trị có nằm trong tập dữ liệu hay không. |
| Q16 | **D** | A single equal sign performs assignment, not comparison. | Một dấu bằng thực hiện gán chứ không so sánh. |
| Q17 | **A** | Three is not greater than five. | Số 3 không lớn hơn số 5. |
| Q18 | **B** | Multiplication has higher precedence than addition. | Phép nhân được thực hiện trước phép cộng. |
| Q19 | **C** | One true operand is enough for logical OR. | OR đúng khi có ít nhất một vế đúng. |
| Q20 | **D** | XOR of binary 0101 and 0011 equals 0110. | XOR của 0101 và 0011 cho 0110. |

## 8. Nối sang bài kế tiếp

`Kiểu dữ liệu → Toán tử → Điều kiện → Quy tắc nghiệp vụ`.

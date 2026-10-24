# PY-02 — Kiểu số, Boolean và chuỗi


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Integer** — số nguyên; **Float** — số thực.

`Biến → int/float/bool/str → Slicing → Xử lý văn bản`

Khái niệm trong bài nằm ở bước này của chuỗi học; hãy hiểu đầu vào, thao tác và đầu ra trước khi dùng cho dữ liệu AI.

## 2. English vocabulary — Từ vựng

| English | Nghĩa tiếng Việt | Giải thích |
|---|---|---|
| Integer | số nguyên | Giá trị không có phần thập phân |
| Float | số thực | Số có thể có phần lẻ |
| Boolean | giá trị logic | Giá trị True hoặc False |
| String | chuỗi | Dãy ký tự có thể cắt lát |

## 3. Các hàm và tùy chọn Python

**Từ vựng trong mục:** **Function** — hàm; **Argument** — đối số.

| Hàm / cú pháp | Mục đích và ý nghĩa lựa chọn |
|---|---|
| `str()/int()/float()` | Chuyển kiểu phù hợp trước khi xử lý |
| `strip()/lower()/upper()` | Dọn khoảng trắng và chuẩn hóa chữ |
| `split()/replace()` | Tách chuỗi hoặc thay thế đoạn văn bản |
| `s[start:stop]` | Cắt ký tự theo vị trí, không lấy chỉ số stop |


## 4. Khái niệm liên quan — từ lời giải thích đến Python

### 4.1. Integer

**Từ vựng trong mục:** **Integer** — số nguyên.

Giá trị không có phần thập phân. xác định giá trị đầu vào có ý nghĩa gì.

```python
n = 5
print(type(n))
```

**Tự kiểm tra:** Integer có ý nghĩa gì?

**Đáp án:** Giá trị không có phần thập phân.

### 4.2. Float

**Từ vựng trong mục:** **Float** — số thực.

Số có thể có phần lẻ. xác định giá trị đầu vào có ý nghĩa gì.

```python
x = 3.5
print(x)
```

**Tự kiểm tra:** Float có ý nghĩa gì?

**Đáp án:** Số có thể có phần lẻ.

### 4.3. Boolean

**Từ vựng trong mục:** **Boolean** — giá trị logic.

Giá trị True hoặc False. xác định giá trị đầu vào có ý nghĩa gì.

```python
ok = True
print(ok)
```

**Tự kiểm tra:** Boolean có ý nghĩa gì?

**Đáp án:** Giá trị True hoặc False.

### 4.4. String

**Từ vựng trong mục:** **String** — chuỗi.

Dãy ký tự có thể cắt lát. xác định giá trị đầu vào có ý nghĩa gì.

```python
code = 'AB12'
print(code[:2])
```

**Tự kiểm tra:** String có ý nghĩa gì?

**Đáp án:** Dãy ký tự có thể cắt lát.

## 5. Năm tình huống lập trình thực tế

### Tình huống 1 — Chuẩn hóa email

**Từ vựng trong mục:** **Integer** — số nguyên.

**Tình huống thực tế:** Một ứng dụng thực tế cần chuẩn hóa email. Dữ liệu hiện có: Email nhập thừa khoảng trắng. Hãy viết chương trình xử lý dữ liệu này và xác định kết quả theo yêu cầu.

**Vì sao chọn cách này?** Bỏ khoảng trắng và đổi chữ thường trước so trùng.


**Quy trình:** xác định đầu vào → thực hiện phép tính / điều kiện → in kết quả → kiểm tra các trường hợp khác.

```python
email = "  Lan@Example.COM "
print(email.strip().lower())
```


### Tình huống 2 — Tách nhãn sản phẩm

**Từ vựng trong mục:** **Float** — số thực.

**Tình huống thực tế:** Một cửa hàng cần tách nhãn sản phẩm. Dữ liệu hiện có: Chuỗi có 3 nhãn. Hãy viết chương trình xử lý dữ liệu này và xác định kết quả theo yêu cầu.

**Vì sao chọn cách này?** Dấu phẩy tạo ranh giới giữa nhãn.


**Quy trình:** xác định đầu vào → thực hiện phép tính / điều kiện → in kết quả → kiểm tra các trường hợp khác.

```python
labels = "AI,Python,Math"
print(labels.split(","))
```


### Tình huống 3 — Giữ mã đầu 0

**Từ vựng trong mục:** **Boolean** — giá trị logic.

**Tình huống thực tế:** Một ứng dụng thực tế cần giữ mã đầu 0. Dữ liệu hiện có: Mã đơn 00045. Hãy viết chương trình xử lý dữ liệu này và xác định kết quả theo yêu cầu.

**Vì sao chọn cách này?** Mã không được mất chữ số đầu khi dùng để tra cứu.


**Quy trình:** xác định đầu vào → thực hiện phép tính / điều kiện → in kết quả → kiểm tra các trường hợp khác.

```python
order_id = "00045"
print(order_id[:3])
```


### Tình huống 4 — Đổi số từ CSV

**Từ vựng trong mục:** **String** — chuỗi.

**Tình huống thực tế:** Một ứng dụng thực tế cần đổi số từ csv. Dữ liệu hiện có: Giá 12.5, số lượng 3. Hãy viết chương trình xử lý dữ liệu này và xác định kết quả theo yêu cầu.

**Vì sao chọn cách này?** Chuyển chuỗi số trước khi tính tổng.


**Quy trình:** xác định đầu vào → thực hiện phép tính / điều kiện → in kết quả → kiểm tra các trường hợp khác.

```python
price = float("12.5")
qty = int("3")
print(price * qty)
```


### Tình huống 5 — Che số liên lạc

**Từ vựng trong mục:** **Integer** — số nguyên.

**Tình huống thực tế:** Một ứng dụng thực tế cần che số liên lạc. Dữ liệu hiện có: Số mô phỏng 0900123456. Hãy viết chương trình xử lý dữ liệu này và xác định kết quả theo yêu cầu.

**Vì sao chọn cách này?** Lấy ba ký tự cuối mà không lộ phần trước.


**Quy trình:** xác định đầu vào → thực hiện phép tính / điều kiện → in kết quả → kiểm tra các trường hợp khác.

```python
phone = "0900123456"
print("*" * (len(phone)-3) + phone[-3:])
```


## 6. Những nhầm lẫn thường gặp

- Không suy diễn từ một ví dụ minh họa sang mọi bộ dữ liệu thật.
- Dùng phép xử lý phù hợp với kiểu dữ liệu và đơn vị đo. Khi có đầu vào người dùng, cần kiểm tra lỗi.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is Integer? — Thuật ngữ Integer có nghĩa gì?**

A. A fractional numeric value — Số có thể có phần lẻ

B. A whole-number value — Giá trị không có phần thập phân

C. A true-or-false value — Giá trị True hoặc False

D. An ordered sequence of characters — Dãy ký tự có thể cắt lát


**Q2. What is Float? — Thuật ngữ Float có nghĩa gì?**

A. A fractional numeric value — Số có thể có phần lẻ

B. A true-or-false value — Giá trị True hoặc False

C. An ordered sequence of characters — Dãy ký tự có thể cắt lát

D. A whole-number value — Giá trị không có phần thập phân


**Q3. What is Boolean? — Thuật ngữ Boolean có nghĩa gì?**

A. An ordered sequence of characters — Dãy ký tự có thể cắt lát

B. A whole-number value — Giá trị không có phần thập phân

C. A fractional numeric value — Số có thể có phần lẻ

D. A true-or-false value — Giá trị True hoặc False


**Q4. What is String? — Thuật ngữ String có nghĩa gì?**

A. A whole-number value — Giá trị không có phần thập phân

B. A fractional numeric value — Số có thể có phần lẻ

C. An ordered sequence of characters — Dãy ký tự có thể cắt lát

D. A true-or-false value — Giá trị True hoặc False


**Q5. Which use matches str()/int()/float()? — Công dụng nào đúng với str()/int()/float()?**

A. It always creates perfect predictions — Nó luôn dự đoán đúng tuyệt đối

B. This Python operation supports the described task — Chuyển kiểu phù hợp trước khi xử lý

C. It automatically trains a neural network — Nó tự huấn luyện mạng nơ-ron

D. It removes the need for input checks — Nó loại bỏ nhu cầu kiểm tra đầu vào


**Q6. Which use matches strip()/lower()/upper()? — Công dụng nào đúng với strip()/lower()/upper()?**

A. This Python operation supports the described task — Dọn khoảng trắng và chuẩn hóa chữ

B. It always creates perfect predictions — Nó luôn dự đoán đúng tuyệt đối

C. It automatically trains a neural network — Nó tự huấn luyện mạng nơ-ron

D. It removes the need for input checks — Nó loại bỏ nhu cầu kiểm tra đầu vào


**Q7. Which use matches split()/replace()? — Công dụng nào đúng với split()/replace()?**

A. It always creates perfect predictions — Nó luôn dự đoán đúng tuyệt đối

B. It automatically trains a neural network — Nó tự huấn luyện mạng nơ-ron

C. It removes the need for input checks — Nó loại bỏ nhu cầu kiểm tra đầu vào

D. This Python operation supports the described task — Tách chuỗi hoặc thay thế đoạn văn bản


**Q8. Which use matches s[start:stop]? — Công dụng nào đúng với s[start:stop]?**

A. It always creates perfect predictions — Nó luôn dự đoán đúng tuyệt đối

B. It automatically trains a neural network — Nó tự huấn luyện mạng nơ-ron

C. This Python operation supports the described task — Cắt ký tự theo vị trí, không lấy chỉ số stop

D. It removes the need for input checks — Nó loại bỏ nhu cầu kiểm tra đầu vào


**Q9. Which reason fits 'Email cleanup'? — Lý do nào phù hợp với 'Chuẩn hóa email'?**

A. Split comma-separated labels — Dấu phẩy tạo ranh giới giữa nhãn

B. Normalize contact text before matching — Bỏ khoảng trắng và đổi chữ thường trước so trùng

C. Keep identifier as text — Mã không được mất chữ số đầu khi dùng để tra cứu

D. Convert numeric strings — Chuyển chuỗi số trước khi tính tổng


**Q10. Which reason fits 'Split labels'? — Lý do nào phù hợp với 'Tách nhãn sản phẩm'?**

A. Split comma-separated labels — Dấu phẩy tạo ranh giới giữa nhãn

B. Keep identifier as text — Mã không được mất chữ số đầu khi dùng để tra cứu

C. Convert numeric strings — Chuyển chuỗi số trước khi tính tổng

D. Mask a contact string — Lấy ba ký tự cuối mà không lộ phần trước


**Q11. Which reason fits 'Preserve leading zero'? — Lý do nào phù hợp với 'Giữ mã đầu 0'?**

A. Convert numeric strings — Chuyển chuỗi số trước khi tính tổng

B. Mask a contact string — Lấy ba ký tự cuối mà không lộ phần trước

C. Normalize contact text before matching — Bỏ khoảng trắng và đổi chữ thường trước so trùng

D. Keep identifier as text — Mã không được mất chữ số đầu khi dùng để tra cứu


**Q12. Which reason fits 'Parse price'? — Lý do nào phù hợp với 'Đổi số từ CSV'?**

A. Mask a contact string — Lấy ba ký tự cuối mà không lộ phần trước

B. Normalize contact text before matching — Bỏ khoảng trắng và đổi chữ thường trước so trùng

C. Convert numeric strings — Chuyển chuỗi số trước khi tính tổng

D. Split comma-separated labels — Dấu phẩy tạo ranh giới giữa nhãn


**Q13. Which reason fits 'Mask contact'? — Lý do nào phù hợp với 'Che số liên lạc'?**

A. Normalize contact text before matching — Bỏ khoảng trắng và đổi chữ thường trước so trùng

B. Mask a contact string — Lấy ba ký tự cuối mà không lộ phần trước

C. Split comma-separated labels — Dấu phẩy tạo ranh giới giữa nhãn

D. Keep identifier as text — Mã không được mất chữ số đầu khi dùng để tra cứu


**Q14. Which input fits 'Email cleanup'? — Dữ liệu nào được dùng cho 'Chuẩn hóa email'?**

A. The sample described for Email cleanup — Email nhập thừa khoảng trắng

B. Input from Split labels — Chuỗi có 3 nhãn

C. Input from Preserve leading zero — Mã đơn 00045

D. Input from Parse price — Giá 12.5, số lượng 3


**Q15. Which input fits 'Split labels'? — Dữ liệu nào được dùng cho 'Tách nhãn sản phẩm'?**

A. Input from Preserve leading zero — Mã đơn 00045

B. Input from Parse price — Giá 12.5, số lượng 3

C. Input from Mask contact — Số mô phỏng 0900123456

D. The sample described for Split labels — Chuỗi có 3 nhãn


**Q16. Which input fits 'Preserve leading zero'? — Dữ liệu nào được dùng cho 'Giữ mã đầu 0'?**

A. Input from Parse price — Giá 12.5, số lượng 3

B. Input from Mask contact — Số mô phỏng 0900123456

C. The sample described for Preserve leading zero — Mã đơn 00045

D. Input from Email cleanup — Email nhập thừa khoảng trắng


**Q17. Which input fits 'Parse price'? — Dữ liệu nào được dùng cho 'Đổi số từ CSV'?**

A. Input from Mask contact — Số mô phỏng 0900123456

B. The sample described for Parse price — Giá 12.5, số lượng 3

C. Input from Email cleanup — Email nhập thừa khoảng trắng

D. Input from Split labels — Chuỗi có 3 nhãn


**Q18. Which input fits 'Mask contact'? — Dữ liệu nào được dùng cho 'Che số liên lạc'?**

A. The sample described for Mask contact — Số mô phỏng 0900123456

B. Input from Email cleanup — Email nhập thừa khoảng trắng

C. Input from Split labels — Chuỗi có 3 nhãn

D. Input from Preserve leading zero — Mã đơn 00045


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
| Q1 | **B** | A whole-number value | Giá trị không có phần thập phân |
| Q2 | **A** | A fractional numeric value | Số có thể có phần lẻ |
| Q3 | **D** | A true-or-false value | Giá trị True hoặc False |
| Q4 | **C** | An ordered sequence of characters | Dãy ký tự có thể cắt lát |
| Q5 | **B** | This Python operation supports the described task | Chuyển kiểu phù hợp trước khi xử lý |
| Q6 | **A** | This Python operation supports the described task | Dọn khoảng trắng và chuẩn hóa chữ |
| Q7 | **D** | This Python operation supports the described task | Tách chuỗi hoặc thay thế đoạn văn bản |
| Q8 | **C** | This Python operation supports the described task | Cắt ký tự theo vị trí, không lấy chỉ số stop |
| Q9 | **B** | Normalize contact text before matching | Bỏ khoảng trắng và đổi chữ thường trước so trùng |
| Q10 | **A** | Split comma-separated labels | Dấu phẩy tạo ranh giới giữa nhãn |
| Q11 | **D** | Keep identifier as text | Mã không được mất chữ số đầu khi dùng để tra cứu |
| Q12 | **C** | Convert numeric strings | Chuyển chuỗi số trước khi tính tổng |
| Q13 | **B** | Mask a contact string | Lấy ba ký tự cuối mà không lộ phần trước |
| Q14 | **A** | The sample described for Email cleanup | Email nhập thừa khoảng trắng |
| Q15 | **D** | The sample described for Split labels | Chuỗi có 3 nhãn |
| Q16 | **C** | The sample described for Preserve leading zero | Mã đơn 00045 |
| Q17 | **B** | The sample described for Parse price | Giá 12.5, số lượng 3 |
| Q18 | **A** | The sample described for Mask contact | Số mô phỏng 0900123456 |
| Q19 | **D** | Input meaning, type and units | Ý nghĩa, kiểu và đơn vị đầu vào |
| Q20 | **C** | Validate output and edge cases | Kiểm tra kết quả và trường hợp biên |

## 8. Nối sang bài kế tiếp

`Biến → int/float/bool/str → Slicing → Xử lý văn bản`.

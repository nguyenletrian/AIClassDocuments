# PY-02 — Kiểu số, Boolean và chuỗi


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Integer** — số nguyên; **Float** — số thực.

`Biến → int/float/bool/str → Slicing → Xử lý văn bản`

Sau khi biết lưu thông tin vào biến, ta học cách phân biệt số, chữ và giá trị đúng/sai. Nhờ vậy, Python có thể tính tiền, kiểm tra điều kiện và xử lý văn bản đúng cách.

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


## 4. Khái niệm liên quan

### 4.1. Integer

**Từ vựng trong mục:** **Integer** — số nguyên.

`int` dùng để lưu số nguyên như số sản phẩm hay số học viên. Trong ví dụ, `n = 5` là số nguyên; `type(n)` cho biết kiểu dữ liệu là `int`.

```python
n = 5
print(type(n))
```

**Kết quả khi chạy:**

```text
<class 'int'>
```


### 4.2. Float

**Từ vựng trong mục:** **Float** — số thực.

`float` dùng cho số có phần thập phân như nhiệt độ `36.5` °C hay điểm `8.5`. Ví dụ dưới đây in ra `3.5`.

```python
x = 3.5
print(x)
```

**Kết quả khi chạy:**

```text
3.5
```


### 4.3. Boolean

**Từ vựng trong mục:** **Boolean** — giá trị logic.

`bool` thể hiện hai trạng thái `True` (đúng) hoặc `False` (sai). Ví dụ, biến `ok = True` có thể dùng để ghi lại một bước kiểm tra đã đạt.

```python
ok = True
print(ok)
```

**Kết quả khi chạy:**

```text
True
```


### 4.4. String

**Từ vựng trong mục:** **String** — chuỗi.

`str` lưu chữ, số điện thoại hoặc mã đơn. Chuỗi `AB12` có bốn ký tự; `code[:2]` lấy hai ký tự đầu, nên in ra `AB`.

```python
code = 'AB12'
print(code[:2])
```

**Kết quả khi chạy:**

```text
AB
```


## 5. Năm tình huống lập trình thực tế

### Tình huống 1 — Chuẩn hóa email

**Từ vựng trong mục:** **String** — chuỗi; **Method** — phương thức.

**Tình huống thực tế:** Một ứng dụng lưu email do khách nhập là `"  Lan@Example.COM "`, trong đó có khoảng trắng thừa ở đầu và cuối, còn chữ hoa và chữ thường được nhập lẫn nhau.

**Yêu cầu:** In email không còn khoảng trắng ở hai đầu và được đổi thành chữ thường.

**Vì sao chọn cách giải này?** `strip()` bỏ khoảng trắng hai đầu; `lower()` đổi chữ thành chữ thường, giúp thống nhất cách hiển thị và hỗ trợ so sánh email. Cách này không kiểm tra email có hợp lệ hay không.

**Quy trình giải:**

1. Lưu chuỗi email ban đầu.
2. Dùng `strip()` bỏ khoảng trắng đầu và cuối.
3. Dùng `lower()` đổi chữ thành chữ thường rồi in kết quả.

```python
email = "  Lan@Example.COM "
print(email.strip().lower())
```

**Kết quả khi chạy:**

```text
lan@example.com
```

**Kết quả:** `lan@example.com` — email không còn khoảng trắng thừa và đã viết thường.

### Tình huống 2 — Tách nhãn sản phẩm

**Từ vựng trong mục:** **String** — chuỗi; **Split** — tách.

**Tình huống thực tế:** Một cửa hàng nhận chuỗi nhãn sản phẩm `"AI,Python,Math"`. Ba nhãn được ngăn cách bằng dấu phẩy và cần tách riêng để xử lý từng nhãn.

**Yêu cầu:** Tạo danh sách gồm ba nhãn từ chuỗi này.

**Vì sao chọn cách giải này?** `split(",")` tách chuỗi ở mỗi dấu phẩy thành các phần tử riêng trong một danh sách.

**Quy trình giải:**

1. Lưu chuỗi nhãn vào `labels`.
2. Truyền dấu phẩy vào `split()` để tách các nhãn.
3. In danh sách nhận được.

```python
labels = "AI,Python,Math"
print(labels.split(","))
```

**Kết quả khi chạy:**

```text
['AI', 'Python', 'Math']
```

**Kết quả:** `['AI', 'Python', 'Math']` — ba nhãn được tách thành ba phần tử.

### Tình huống 3 — Giữ mã đầu 0

**Từ vựng trong mục:** **String** — chuỗi; **Slice** — cắt chuỗi.

**Tình huống thực tế:** Hệ thống quản lý đơn hàng lưu mã `00045`. Các số `0` đầu mã phải được giữ nguyên vì đây là mã nhận diện, không phải số để tính toán.

**Yêu cầu:** Lưu mã đơn và in ba ký tự đầu của mã để kiểm tra chúng vẫn còn nguyên.

**Vì sao chọn cách giải này?** Chuỗi `str` giữ được các số `0` đứng đầu. Cú pháp `[:3]` lấy ba ký tự đầu, không chuyển mã sang số nguyên.

**Quy trình giải:**

1. Lưu `"00045"` vào `order_id`.
2. Lấy ba ký tự đầu bằng `order_id[:3]`.
3. In kết quả để xem phần đầu của mã.

```python
order_id = "00045"
print(order_id[:3])
```

**Kết quả khi chạy:**

```text
000
```

**Kết quả:** `000` — ba ký tự đầu của mã vẫn được giữ nguyên. Chương trình không in cả mã `00045`.

### Tình huống 4 — Đổi số từ CSV

**Từ vựng trong mục:** **Float** — số thực; **Integer** — số nguyên.

**Tình huống thực tế:** Một cửa hàng nhập từ file CSV giá một sản phẩm là chuỗi `"12.5"` và số lượng là chuỗi `"3"`. Giá tính theo cùng đơn vị tiền của hệ thống.

**Yêu cầu:** Đổi hai chuỗi thành số, rồi tính số tiền cho ba sản phẩm.

**Vì sao chọn cách giải này?** Dùng `float()` cho giá có phần thập phân và `int()` cho số lượng nguyên, sau đó nhân hai số để tính tiền.

**Quy trình giải:**

1. Đổi `"12.5"` thành số thực bằng `float()`.
2. Đổi `"3"` thành số nguyên bằng `int()`.
3. Nhân giá và số lượng rồi in kết quả.

```python
price = float("12.5")
qty = int("3")
print(price * qty)
```

**Kết quả khi chạy:**

```text
37.5
```

**Kết quả:** `37.5` đơn vị tiền — tổng giá của ba sản phẩm.

### Tình huống 5 — Che số liên lạc

**Từ vựng trong mục:** **String** — chuỗi; **Slice** — cắt chuỗi.

**Tình huống thực tế:** Ứng dụng chăm sóc khách hàng có số điện thoại mẫu `0900123456`. Khi hiển thị trên màn hình, ứng dụng chỉ được để lộ ba chữ số cuối.

**Yêu cầu:** In số điện thoại dưới dạng dấu `*` che toàn bộ ký tự trừ ba số cuối.

**Vì sao chọn cách giải này?** Lưu số điện thoại dạng chuỗi để giữ số `0` đầu. `phone[-3:]` lấy ba ký tự cuối; `len(phone)-3` tính số dấu `*` cần in.

**Quy trình giải:**

1. Lưu số điện thoại dưới dạng chuỗi.
2. Tạo số dấu `*` bằng độ dài chuỗi trừ ba.
3. Ghép phần che với ba ký tự cuối rồi in.

```python
phone = "0900123456"
print("*" * (len(phone)-3) + phone[-3:])
```

**Kết quả khi chạy:**

```text
*******456
```

**Kết quả:** `*******456` — bảy ký tự đầu được che, chỉ còn `456`.

## 6. Những nhầm lẫn thường gặp

- `int("12.5")` gây lỗi vì chuỗi này không viết theo dạng số nguyên; dùng `float("12.5")` nếu cần số có phần thập phân.
- Không chuyển mã đơn hoặc số điện thoại sang `int` nếu cần giữ số `0` ở đầu.
- `strip()` chỉ bỏ khoảng trắng ở hai đầu chuỗi; `lower()` không tự kiểm tra email hợp lệ.
- `s[:3]` lấy ba ký tự đầu (vị trí 0, 1, 2), không lấy ký tự ở vị trí 3.

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

B. These functions convert values between text and numeric types — Chuyển kiểu phù hợp trước khi xử lý

C. It automatically trains a neural network — Nó tự huấn luyện mạng nơ-ron

D. It removes the need for input checks — Nó loại bỏ nhu cầu kiểm tra đầu vào


**Q6. Which use matches strip()/lower()/upper()? — Công dụng nào đúng với strip()/lower()/upper()?**

A. These methods trim surrounding spaces or change letter case — Dọn khoảng trắng và chuẩn hóa chữ

B. It always creates perfect predictions — Nó luôn dự đoán đúng tuyệt đối

C. It automatically trains a neural network — Nó tự huấn luyện mạng nơ-ron

D. It removes the need for input checks — Nó loại bỏ nhu cầu kiểm tra đầu vào


**Q7. Which use matches split()/replace()? — Công dụng nào đúng với split()/replace()?**

A. It always creates perfect predictions — Nó luôn dự đoán đúng tuyệt đối

B. It automatically trains a neural network — Nó tự huấn luyện mạng nơ-ron

C. It removes the need for input checks — Nó loại bỏ nhu cầu kiểm tra đầu vào

D. These methods split text or replace part of it — Tách chuỗi hoặc thay thế đoạn văn bản


**Q8. Which use matches s[start:stop]? — Công dụng nào đúng với s[start:stop]?**

A. It always creates perfect predictions — Nó luôn dự đoán đúng tuyệt đối

B. It automatically trains a neural network — Nó tự huấn luyện mạng nơ-ron

C. This slice returns characters before the stop index — Cắt ký tự theo vị trí, không lấy chỉ số stop

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

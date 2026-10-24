# PY-09 — Hàm, return, lambda và phạm vi biến


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Function** — hàm; **Parameter** — tham số.

`Vòng lặp → Hàm → OOP → Pipeline`

Bài này nối trực tiếp kiến thức trước với bước xử lý dữ liệu/AI sau đó. Hãy nắm ý nghĩa dữ liệu trước khi chạy code.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Ý nghĩa |
|---|---|---|
| Function | hàm | Khối code tái sử dụng và nhận tham số |
| Parameter | tham số | Tên đầu vào dùng trong định nghĩa hàm |
| Return | trả về | Kết quả gửi từ hàm về nơi gọi |
| Lambda | hàm ẩn danh | Biểu thức hàm ngắn không cần đặt tên |

## 3. Thư viện, hàm và tham số

**Từ vựng trong mục:** **Function** — hàm; **Parameter** — tham số.

| Hàm/cú pháp | Giải thích và lý do dùng |
|---|---|
| `def func(...):` | Định nghĩa một hàm, sử dụng return để trả kết quả |
| `default / keyword arguments` | Dùng tham số mặc định hoặc gọi theo tên cho dễ đọc |
| `lambda x: expr` | Dùng biểu thức ngắn khi hàm không cần nhiều câu lệnh |
| `sorted(..., key=...)` | Chọn tiêu chí để sắp xếp bản ghi |


## 4. Khái niệm và ví dụ nhỏ

### 4.1. Function

**Từ vựng trong mục:** **Function** — hàm.

Khối code tái sử dụng và nhận tham số. Đây là bước nhỏ của chuỗi kiến thức, không cần chứng minh toán học để hiểu cách tính bằng Python.

```python
def twice(x): return x*2
print(twice(3))
```

**Tự kiểm tra:** Function là gì? **Đáp án:** Khối code tái sử dụng và nhận tham số.

### 4.2. Parameter

**Từ vựng trong mục:** **Parameter** — tham số.

Tên đầu vào dùng trong định nghĩa hàm. Đây là bước nhỏ của chuỗi kiến thức, không cần chứng minh toán học để hiểu cách tính bằng Python.

```python
def hello(name): return name
print(hello('Lan'))
```

**Tự kiểm tra:** Parameter là gì? **Đáp án:** Tên đầu vào dùng trong định nghĩa hàm.

### 4.3. Return

**Từ vựng trong mục:** **Return** — trả về.

Kết quả gửi từ hàm về nơi gọi. Đây là bước nhỏ của chuỗi kiến thức, không cần chứng minh toán học để hiểu cách tính bằng Python.

```python
def add(a,b): return a+b
print(add(2,3))
```

**Tự kiểm tra:** Return là gì? **Đáp án:** Kết quả gửi từ hàm về nơi gọi.

### 4.4. Lambda

**Từ vựng trong mục:** **Lambda** — hàm ẩn danh.

Biểu thức hàm ngắn không cần đặt tên. Đây là bước nhỏ của chuỗi kiến thức, không cần chứng minh toán học để hiểu cách tính bằng Python.

```python
print((lambda x: x+1)(5))
```

**Tự kiểm tra:** Lambda là gì? **Đáp án:** Biểu thức hàm ngắn không cần đặt tên.

## 5. Năm tình huống lập trình thực tế

### Tình huống 1 — Tính thuế giá trị gia tăng

**Từ vựng trong mục:** **Function** — hàm.

**Tình huống thực tế:** Một cửa hàng đang cần giải quyết việc tính thuế giá trị gia tăng. Thông tin đầu vào: Giá 100000 đồng, VAT 10%. Dữ liệu minh họa; khi có bảng, mỗi hàng là đối tượng và mỗi cột là một thuộc tính với ý nghĩa rõ. Hãy lập trình thực hiện việc này và in kết quả để nhân viên kiểm tra.

**Vì sao chọn cách giải?** Hàm có mặc định rate nên mọi hóa đơn dùng cùng quy tắc. Đây là phương án phù hợp bài toán nhỏ, không tự suy ra đủ an toàn với mọi dữ liệu thật.


**Quy trình:** Nắm dữ liệu → chọn cấu trúc/hàm → tính → in và kiểm tra kết quả.

```python
def with_vat(price, rate=0.10):
    return round(price*(1+rate))
print(with_vat(100000))
```

**Đọc kết quả:** So sánh kết quả với tình huống đầu vào và thử trường hợp ngoại lệ.

### Tình huống 2 — Sắp điểm theo thứ hạng

**Từ vựng trong mục:** **Parameter** — tham số.

**Tình huống thực tế:** Một trung tâm đào tạo đang cần giải quyết việc sắp điểm theo thứ hạng. Thông tin đầu vào: Hai hồ sơ tên và điểm. Dữ liệu minh họa; khi có bảng, mỗi hàng là đối tượng và mỗi cột là một thuộc tính với ý nghĩa rõ. Hãy lập trình thực hiện việc này và in kết quả để nhân viên kiểm tra.

**Vì sao chọn cách giải?** Dùng lambda làm khóa sắp để không cần dựng hàm dài. Đây là phương án phù hợp bài toán nhỏ, không tự suy ra đủ an toàn với mọi dữ liệu thật.


**Quy trình:** Nắm dữ liệu → chọn cấu trúc/hàm → tính → in và kiểm tra kết quả.

```python
people=[{"name":"A","score":8},{"name":"B","score":10}]
print(sorted(people,key=lambda r:r["score"],reverse=True))
```

**Đọc kết quả:** So sánh kết quả với tình huống đầu vào và thử trường hợp ngoại lệ.

### Tình huống 3 — Kiểm tra điểm hợp lệ

**Từ vựng trong mục:** **Return** — trả về.

**Tình huống thực tế:** Một trung tâm đào tạo đang cần giải quyết việc kiểm tra điểm hợp lệ. Thông tin đầu vào: Điểm phải nằm từ 0 đến 10. Dữ liệu minh họa; khi có bảng, mỗi hàng là đối tượng và mỗi cột là một thuộc tính với ý nghĩa rõ. Hãy lập trình thực hiện việc này và in kết quả để nhân viên kiểm tra.

**Vì sao chọn cách giải?** Hàm trả Boolean để nhiều nơi có thể dùng chung. Đây là phương án phù hợp bài toán nhỏ, không tự suy ra đủ an toàn với mọi dữ liệu thật.


**Quy trình:** Nắm dữ liệu → chọn cấu trúc/hàm → tính → in và kiểm tra kết quả.

```python
def valid_score(x): return 0<=x<=10
print(valid_score(11))
```

**Đọc kết quả:** So sánh kết quả với tình huống đầu vào và thử trường hợp ngoại lệ.

### Tình huống 4 — Trả thống kê đơn giản

**Từ vựng trong mục:** **Lambda** — hàm ẩn danh.

**Tình huống thực tế:** Một cửa hàng đang cần giải quyết việc trả thống kê đơn giản. Thông tin đầu vào: Ba số lượng [7,8,9]. Dữ liệu minh họa; khi có bảng, mỗi hàng là đối tượng và mỗi cột là một thuộc tính với ý nghĩa rõ. Hãy lập trình thực hiện việc này và in kết quả để nhân viên kiểm tra.

**Vì sao chọn cách giải?** Một hàm trả tuple gồm tổng và trung bình. Đây là phương án phù hợp bài toán nhỏ, không tự suy ra đủ an toàn với mọi dữ liệu thật.


**Quy trình:** Nắm dữ liệu → chọn cấu trúc/hàm → tính → in và kiểm tra kết quả.

```python
def summary(values):
    return sum(values), sum(values)/len(values)
total,average=summary([7,8,9])
print(total,average)
```

**Đọc kết quả:** So sánh kết quả với tình huống đầu vào và thử trường hợp ngoại lệ.

### Tình huống 5 — Lọc yêu cầu ưu tiên

**Từ vựng trong mục:** **Function** — hàm.

**Tình huống thực tế:** Một bộ phận vận hành đang cần giải quyết việc lọc yêu cầu ưu tiên. Thông tin đầu vào: Điểm ưu tiên [1,5,2,4]. Dữ liệu minh họa; khi có bảng, mỗi hàng là đối tượng và mỗi cột là một thuộc tính với ý nghĩa rõ. Hãy lập trình thực hiện việc này và in kết quả để nhân viên kiểm tra.

**Vì sao chọn cách giải?** filter áp dụng cùng điều kiện cho từng yêu cầu. Đây là phương án phù hợp bài toán nhỏ, không tự suy ra đủ an toàn với mọi dữ liệu thật.


**Quy trình:** Nắm dữ liệu → chọn cấu trúc/hàm → tính → in và kiểm tra kết quả.

```python
priorities=[1,5,2,4]
print(list(filter(lambda x:x>=4,priorities)))
```

**Đọc kết quả:** So sánh kết quả với tình huống đầu vào và thử trường hợp ngoại lệ.

## 6. Sai lầm thường gặp

- Không dùng đầu ra mẫu để suy diễn về người thật, hàng hóa thật hoặc kết quả dự đoán AI.
- Cần chú ý thứ tự xử lý, kiểu dữ liệu và đơn vị đo. Trường hợp rỗng/thiếu dữ liệu phải có cách xử lý rõ ràng.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.


**Q1. Which description matches Function? — Mô tả nào đúng với Function?**

A. A different concept described as Tên đầu vào dùng trong định nghĩa hàm — Tên đầu vào dùng trong định nghĩa hàm

B. The concept described as Khối code tái sử dụng và nhận tham số — Khối code tái sử dụng và nhận tham số

C. A different concept described as Kết quả gửi từ hàm về nơi gọi — Kết quả gửi từ hàm về nơi gọi

D. A different concept described as Biểu thức hàm ngắn không cần đặt tên — Biểu thức hàm ngắn không cần đặt tên


**Q2. Which description matches Parameter? — Mô tả nào đúng với Parameter?**

A. The concept described as Tên đầu vào dùng trong định nghĩa hàm — Tên đầu vào dùng trong định nghĩa hàm

B. A different concept described as Kết quả gửi từ hàm về nơi gọi — Kết quả gửi từ hàm về nơi gọi

C. A different concept described as Biểu thức hàm ngắn không cần đặt tên — Biểu thức hàm ngắn không cần đặt tên

D. A different concept described as Khối code tái sử dụng và nhận tham số — Khối code tái sử dụng và nhận tham số


**Q3. Which description matches Return? — Mô tả nào đúng với Return?**

A. A different concept described as Biểu thức hàm ngắn không cần đặt tên — Biểu thức hàm ngắn không cần đặt tên

B. A different concept described as Khối code tái sử dụng và nhận tham số — Khối code tái sử dụng và nhận tham số

C. A different concept described as Tên đầu vào dùng trong định nghĩa hàm — Tên đầu vào dùng trong định nghĩa hàm

D. The concept described as Kết quả gửi từ hàm về nơi gọi — Kết quả gửi từ hàm về nơi gọi


**Q4. Which description matches Lambda? — Mô tả nào đúng với Lambda?**

A. A different concept described as Khối code tái sử dụng và nhận tham số — Khối code tái sử dụng và nhận tham số

B. A different concept described as Tên đầu vào dùng trong định nghĩa hàm — Tên đầu vào dùng trong định nghĩa hàm

C. The concept described as Biểu thức hàm ngắn không cần đặt tên — Biểu thức hàm ngắn không cần đặt tên

D. A different concept described as Kết quả gửi từ hàm về nơi gọi — Kết quả gửi từ hàm về nơi gọi


**Q5. Which use matches def func(...):? — Công dụng nào đúng với def func(...):?**

A. Use a different operation to Dùng tham số mặc định hoặc gọi theo tên cho dễ đọc — Dùng tham số mặc định hoặc gọi theo tên cho dễ đọc

B. Use this syntax to Định nghĩa một hàm, sử dụng return để trả kết quả — Định nghĩa một hàm, sử dụng return để trả kết quả

C. Use a different operation to Dùng biểu thức ngắn khi hàm không cần nhiều câu lệnh — Dùng biểu thức ngắn khi hàm không cần nhiều câu lệnh

D. Use a different operation to Chọn tiêu chí để sắp xếp bản ghi — Chọn tiêu chí để sắp xếp bản ghi


**Q6. Which use matches default / keyword arguments? — Công dụng nào đúng với default / keyword arguments?**

A. Use this syntax to Dùng tham số mặc định hoặc gọi theo tên cho dễ đọc — Dùng tham số mặc định hoặc gọi theo tên cho dễ đọc

B. Use a different operation to Dùng biểu thức ngắn khi hàm không cần nhiều câu lệnh — Dùng biểu thức ngắn khi hàm không cần nhiều câu lệnh

C. Use a different operation to Chọn tiêu chí để sắp xếp bản ghi — Chọn tiêu chí để sắp xếp bản ghi

D. Use a different operation to Định nghĩa một hàm, sử dụng return để trả kết quả — Định nghĩa một hàm, sử dụng return để trả kết quả


**Q7. Which use matches lambda x: expr? — Công dụng nào đúng với lambda x: expr?**

A. Use a different operation to Chọn tiêu chí để sắp xếp bản ghi — Chọn tiêu chí để sắp xếp bản ghi

B. Use a different operation to Định nghĩa một hàm, sử dụng return để trả kết quả — Định nghĩa một hàm, sử dụng return để trả kết quả

C. Use a different operation to Dùng tham số mặc định hoặc gọi theo tên cho dễ đọc — Dùng tham số mặc định hoặc gọi theo tên cho dễ đọc

D. Use this syntax to Dùng biểu thức ngắn khi hàm không cần nhiều câu lệnh — Dùng biểu thức ngắn khi hàm không cần nhiều câu lệnh


**Q8. Which use matches sorted(..., key=...)? — Công dụng nào đúng với sorted(..., key=...)?**

A. Use a different operation to Định nghĩa một hàm, sử dụng return để trả kết quả — Định nghĩa một hàm, sử dụng return để trả kết quả

B. Use a different operation to Dùng tham số mặc định hoặc gọi theo tên cho dễ đọc — Dùng tham số mặc định hoặc gọi theo tên cho dễ đọc

C. Use this syntax to Chọn tiêu chí để sắp xếp bản ghi — Chọn tiêu chí để sắp xếp bản ghi

D. Use a different operation to Dùng biểu thức ngắn khi hàm không cần nhiều câu lệnh — Dùng biểu thức ngắn khi hàm không cần nhiều câu lệnh


**Q9. What solves scenario 1? — Cách nào giải quyết tình huống 1?**

A. Another method is chosen because Dùng lambda làm khóa sắp để không cần dựng hàm dài — Dùng lambda làm khóa sắp để không cần dựng hàm dài

B. Choose the method because Hàm có mặc định rate nên mọi hóa đơn dùng cùng quy tắc — Hàm có mặc định rate nên mọi hóa đơn dùng cùng quy tắc

C. Another method is chosen because Hàm trả Boolean để nhiều nơi có thể dùng chung — Hàm trả Boolean để nhiều nơi có thể dùng chung

D. Another method is chosen because Một hàm trả tuple gồm tổng và trung bình — Một hàm trả tuple gồm tổng và trung bình


**Q10. What solves scenario 2? — Cách nào giải quyết tình huống 2?**

A. Choose the method because Dùng lambda làm khóa sắp để không cần dựng hàm dài — Dùng lambda làm khóa sắp để không cần dựng hàm dài

B. Another method is chosen because Hàm trả Boolean để nhiều nơi có thể dùng chung — Hàm trả Boolean để nhiều nơi có thể dùng chung

C. Another method is chosen because Một hàm trả tuple gồm tổng và trung bình — Một hàm trả tuple gồm tổng và trung bình

D. Another method is chosen because filter áp dụng cùng điều kiện cho từng yêu cầu — filter áp dụng cùng điều kiện cho từng yêu cầu


**Q11. What solves scenario 3? — Cách nào giải quyết tình huống 3?**

A. Another method is chosen because Một hàm trả tuple gồm tổng và trung bình — Một hàm trả tuple gồm tổng và trung bình

B. Another method is chosen because filter áp dụng cùng điều kiện cho từng yêu cầu — filter áp dụng cùng điều kiện cho từng yêu cầu

C. Another method is chosen because Hàm có mặc định rate nên mọi hóa đơn dùng cùng quy tắc — Hàm có mặc định rate nên mọi hóa đơn dùng cùng quy tắc

D. Choose the method because Hàm trả Boolean để nhiều nơi có thể dùng chung — Hàm trả Boolean để nhiều nơi có thể dùng chung


**Q12. What solves scenario 4? — Cách nào giải quyết tình huống 4?**

A. Another method is chosen because filter áp dụng cùng điều kiện cho từng yêu cầu — filter áp dụng cùng điều kiện cho từng yêu cầu

B. Another method is chosen because Hàm có mặc định rate nên mọi hóa đơn dùng cùng quy tắc — Hàm có mặc định rate nên mọi hóa đơn dùng cùng quy tắc

C. Choose the method because Một hàm trả tuple gồm tổng và trung bình — Một hàm trả tuple gồm tổng và trung bình

D. Another method is chosen because Dùng lambda làm khóa sắp để không cần dựng hàm dài — Dùng lambda làm khóa sắp để không cần dựng hàm dài


**Q13. What solves scenario 5? — Cách nào giải quyết tình huống 5?**

A. Another method is chosen because Hàm có mặc định rate nên mọi hóa đơn dùng cùng quy tắc — Hàm có mặc định rate nên mọi hóa đơn dùng cùng quy tắc

B. Choose the method because filter áp dụng cùng điều kiện cho từng yêu cầu — filter áp dụng cùng điều kiện cho từng yêu cầu

C. Another method is chosen because Dùng lambda làm khóa sắp để không cần dựng hàm dài — Dùng lambda làm khóa sắp để không cần dựng hàm dài

D. Another method is chosen because Hàm trả Boolean để nhiều nơi có thể dùng chung — Hàm trả Boolean để nhiều nơi có thể dùng chung


**Q14. Which data is used in scenario 1? — Tình huống 1 dùng dữ liệu nào?**

A. The described input Giá 100000 đồng, VAT 10% — Giá 100000 đồng, VAT 10%

B. Another input Hai hồ sơ tên và điểm — Hai hồ sơ tên và điểm

C. Another input Điểm phải nằm từ 0 đến 10 — Điểm phải nằm từ 0 đến 10

D. Another input Ba số lượng [7,8,9] — Ba số lượng [7,8,9]


**Q15. Which data is used in scenario 2? — Tình huống 2 dùng dữ liệu nào?**

A. Another input Điểm phải nằm từ 0 đến 10 — Điểm phải nằm từ 0 đến 10

B. Another input Ba số lượng [7,8,9] — Ba số lượng [7,8,9]

C. Another input Điểm ưu tiên [1,5,2,4] — Điểm ưu tiên [1,5,2,4]

D. The described input Hai hồ sơ tên và điểm — Hai hồ sơ tên và điểm


**Q16. Which data is used in scenario 3? — Tình huống 3 dùng dữ liệu nào?**

A. Another input Ba số lượng [7,8,9] — Ba số lượng [7,8,9]

B. Another input Điểm ưu tiên [1,5,2,4] — Điểm ưu tiên [1,5,2,4]

C. The described input Điểm phải nằm từ 0 đến 10 — Điểm phải nằm từ 0 đến 10

D. Another input Giá 100000 đồng, VAT 10% — Giá 100000 đồng, VAT 10%


**Q17. Which data is used in scenario 4? — Tình huống 4 dùng dữ liệu nào?**

A. Another input Điểm ưu tiên [1,5,2,4] — Điểm ưu tiên [1,5,2,4]

B. The described input Ba số lượng [7,8,9] — Ba số lượng [7,8,9]

C. Another input Giá 100000 đồng, VAT 10% — Giá 100000 đồng, VAT 10%

D. Another input Hai hồ sơ tên và điểm — Hai hồ sơ tên và điểm


**Q18. Which data is used in scenario 5? — Tình huống 5 dùng dữ liệu nào?**

A. The described input Điểm ưu tiên [1,5,2,4] — Điểm ưu tiên [1,5,2,4]

B. Another input Giá 100000 đồng, VAT 10% — Giá 100000 đồng, VAT 10%

C. Another input Hai hồ sơ tên và điểm — Hai hồ sơ tên và điểm

D. Another input Điểm phải nằm từ 0 đến 10 — Điểm phải nằm từ 0 đến 10


**Q19. What must be clear before computing? — Cần hiểu gì trước khi tính?**

A. Only font color — Chỉ màu chữ

B. Only filename length — Chỉ độ dài tên file

C. Only number of comments — Chỉ số comment

D. Input meaning and units — Ý nghĩa và đơn vị dữ liệu


**Q20. What should follow a successful demo? — Sau khi demo chạy đúng nên làm gì?**

A. Assume it works for all data — Cho rằng luôn đúng với mọi dữ liệu

B. Remove input validation — Xóa kiểm tra đầu vào

C. Verify output and unusual inputs — Kiểm tra đầu ra và giá trị biên

D. Ignore unexpected results — Bỏ qua kết quả bất thường

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **B** | The concept described as Khối code tái sử dụng và nhận tham số | Khối code tái sử dụng và nhận tham số |
| Q2 | **A** | The concept described as Tên đầu vào dùng trong định nghĩa hàm | Tên đầu vào dùng trong định nghĩa hàm |
| Q3 | **D** | The concept described as Kết quả gửi từ hàm về nơi gọi | Kết quả gửi từ hàm về nơi gọi |
| Q4 | **C** | The concept described as Biểu thức hàm ngắn không cần đặt tên | Biểu thức hàm ngắn không cần đặt tên |
| Q5 | **B** | Use this syntax to Định nghĩa một hàm, sử dụng return để trả kết quả | Định nghĩa một hàm, sử dụng return để trả kết quả |
| Q6 | **A** | Use this syntax to Dùng tham số mặc định hoặc gọi theo tên cho dễ đọc | Dùng tham số mặc định hoặc gọi theo tên cho dễ đọc |
| Q7 | **D** | Use this syntax to Dùng biểu thức ngắn khi hàm không cần nhiều câu lệnh | Dùng biểu thức ngắn khi hàm không cần nhiều câu lệnh |
| Q8 | **C** | Use this syntax to Chọn tiêu chí để sắp xếp bản ghi | Chọn tiêu chí để sắp xếp bản ghi |
| Q9 | **B** | Choose the method because Hàm có mặc định rate nên mọi hóa đơn dùng cùng quy tắc | Hàm có mặc định rate nên mọi hóa đơn dùng cùng quy tắc |
| Q10 | **A** | Choose the method because Dùng lambda làm khóa sắp để không cần dựng hàm dài | Dùng lambda làm khóa sắp để không cần dựng hàm dài |
| Q11 | **D** | Choose the method because Hàm trả Boolean để nhiều nơi có thể dùng chung | Hàm trả Boolean để nhiều nơi có thể dùng chung |
| Q12 | **C** | Choose the method because Một hàm trả tuple gồm tổng và trung bình | Một hàm trả tuple gồm tổng và trung bình |
| Q13 | **B** | Choose the method because filter áp dụng cùng điều kiện cho từng yêu cầu | filter áp dụng cùng điều kiện cho từng yêu cầu |
| Q14 | **A** | The described input Giá 100000 đồng, VAT 10% | Giá 100000 đồng, VAT 10% |
| Q15 | **D** | The described input Hai hồ sơ tên và điểm | Hai hồ sơ tên và điểm |
| Q16 | **C** | The described input Điểm phải nằm từ 0 đến 10 | Điểm phải nằm từ 0 đến 10 |
| Q17 | **B** | The described input Ba số lượng [7,8,9] | Ba số lượng [7,8,9] |
| Q18 | **A** | The described input Điểm ưu tiên [1,5,2,4] | Điểm ưu tiên [1,5,2,4] |
| Q19 | **D** | Input meaning and units | Ý nghĩa và đơn vị dữ liệu |
| Q20 | **C** | Verify output and unusual inputs | Kiểm tra đầu ra và giá trị biên |

## 8. Nối sang bài tiếp theo

`Vòng lặp → Hàm → OOP → Pipeline`.

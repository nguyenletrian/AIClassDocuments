# 05 — Vòng lặp for/while, break/continue

*Trạng thái: DRAFT · Ví dụ giả lập · Cần xác minh thực thi trước khi phát hành*

## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Iteration** — lần lặp; **For loop** — vòng for.

`Điều kiện → Vòng lặp → Xử lý hàng loạt`

Từ kiến thức trước, phần này giúp sinh viên quyết định nên tổ chức và xử lý dữ liệu bằng cấu trúc nào, rồi mới tiến tới các bài xử lý dữ liệu cho AI.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Giải thích dễ nhớ |
|---|---|---|
| Iteration | lần lặp | Một lượt thực hiện trong quá trình lặp |
| For loop | vòng for | Lặp qua từng phần tử trong một nhóm |
| While loop | vòng while | Lặp khi một điều kiện còn đúng |
| Break/continue | dừng/bỏ qua | Dừng hẳn vòng lặp hoặc bỏ qua lượt hiện tại |

## 3. Hàm và cú pháp Python

**Từ vựng trong mục:** **Function** — hàm; **Argument** — đối số.

| Hàm / cú pháp | Mục đích và lựa chọn liên quan |
|---|---|
| `range(start,stop)` | Tạo chỉ số nguyên, không bao gồm stop |
| `enumerate(iterable)` | Lấy đồng thời vị trí và giá trị |
| `break` | Dừng sớm khi đã tìm thấy |
| `continue` | Bỏ qua dữ liệu của một lượt lặp |

## 4. Khái niệm liên quan và ví dụ nhỏ

### 4.1. Iteration

**Từ vựng trong mục:** **Iteration** — lần lặp.

Một lượt thực hiện trong quá trình lặp. Đây là khái niệm cần nắm trước khi áp dụng bước xử lý bên dưới.

```python
for i in range(2): print(i)
```

**Tự kiểm tra:** Iteration có nghĩa gì? **Đáp án:** Một lượt thực hiện trong quá trình lặp.

### 4.2. For loop

**Từ vựng trong mục:** **For loop** — vòng for.

Lặp qua từng phần tử trong một nhóm. Đây là khái niệm cần nắm trước khi áp dụng bước xử lý bên dưới.

```python
for x in [1,2]: print(x)
```

**Tự kiểm tra:** For loop có nghĩa gì? **Đáp án:** Lặp qua từng phần tử trong một nhóm.

### 4.3. While loop

**Từ vựng trong mục:** **While loop** — vòng while.

Lặp khi một điều kiện còn đúng. Đây là khái niệm cần nắm trước khi áp dụng bước xử lý bên dưới.

```python
n=2
while n>0:
    n-=1
```

**Tự kiểm tra:** While loop có nghĩa gì? **Đáp án:** Lặp khi một điều kiện còn đúng.

### 4.4. Break/continue

**Từ vựng trong mục:** **Break/continue** — dừng/bỏ qua.

Dừng hẳn vòng lặp hoặc bỏ qua lượt hiện tại. Đây là khái niệm cần nắm trước khi áp dụng bước xử lý bên dưới.

```python
for x in [0,1,2]:
    if x==0: continue
    print(x)
```

**Tự kiểm tra:** Break/continue có nghĩa gì? **Đáp án:** Dừng hẳn vòng lặp hoặc bỏ qua lượt hiện tại.

## 5. Năm tình huống lập trình thực tế

### Tình huống 1 — Tổng hợp doanh thu

**Từ vựng trong mục:** **Iteration** — lần lặp.

**Vấn đề thực tế:** Tổng hợp doanh thu.

**Vì sao chọn cách này?** Duyệt từng giao dịch và cộng dồn thay vì gõ từng phép cộng; không cần công cụ phức tạp hơn khi một quy tắc rõ ràng đã giải được vấn đề.

**Dữ liệu:** 3 đơn vị nghìn đồng: 120, 80, 200; nếu là bảng thì mỗi hàng là một đối tượng và mỗi cột mang một thuộc tính có thứ tự. Các giá trị ở đây đều là ví dụ.

**Quy trình:** Xác định dữ liệu → chọn phép xử lý → chạy code → đọc kết quả và thử trường hợp biên.

```python
orders=[120,80,200]
total=0
for value in orders: total+=value
print(total)
```

**Đọc kết quả:** Đối chiếu với giả định đầu vào; đổi dữ liệu và xem kết quả có đúng ý nghĩa không.

### Tình huống 2 — Loại dòng trống

**Từ vựng trong mục:** **For loop** — vòng for.

**Vấn đề thực tế:** Loại dòng trống.

**Vì sao chọn cách này?** Bỏ qua None nhưng vẫn xử lý các giá trị hợp lệ khác; không cần công cụ phức tạp hơn khi một quy tắc rõ ràng đã giải được vấn đề.

**Dữ liệu:** Bốn giá trị nhiệt độ, một None; nếu là bảng thì mỗi hàng là một đối tượng và mỗi cột mang một thuộc tính có thứ tự. Các giá trị ở đây đều là ví dụ.

**Quy trình:** Xác định dữ liệu → chọn phép xử lý → chạy code → đọc kết quả và thử trường hợp biên.

```python
data=[30,None,35,33]
valid=[]
for x in data:
    if x is None: continue
    valid.append(x)
print(valid)
```

**Đọc kết quả:** Đối chiếu với giả định đầu vào; đổi dữ liệu và xem kết quả có đúng ý nghĩa không.

### Tình huống 3 — Tìm hàng hết tồn

**Từ vựng trong mục:** **While loop** — vòng while.

**Vấn đề thực tế:** Tìm hàng hết tồn.

**Vì sao chọn cách này?** Dừng ngay khi thấy số lượng bằng 0; không cần công cụ phức tạp hơn khi một quy tắc rõ ràng đã giải được vấn đề.

**Dữ liệu:** Bốn mã hàng có số lượng [5,3,0,4]; nếu là bảng thì mỗi hàng là một đối tượng và mỗi cột mang một thuộc tính có thứ tự. Các giá trị ở đây đều là ví dụ.

**Quy trình:** Xác định dữ liệu → chọn phép xử lý → chạy code → đọc kết quả và thử trường hợp biên.

```python
stocks=[5,3,0,4]
for i,x in enumerate(stocks):
    if x==0:
        print("Hết hàng:",i)
        break
```

**Đọc kết quả:** Đối chiếu với giả định đầu vào; đổi dữ liệu và xem kết quả có đúng ý nghĩa không.

### Tình huống 4 — Giới hạn kết nối

**Từ vựng trong mục:** **Break/continue** — dừng/bỏ qua.

**Vấn đề thực tế:** Giới hạn kết nối.

**Vì sao chọn cách này?** While có giới hạn số lượt tránh chạy vô hạn; không cần công cụ phức tạp hơn khi một quy tắc rõ ràng đã giải được vấn đề.

**Dữ liệu:** Tối đa ba lần thử kết nối mô phỏng; nếu là bảng thì mỗi hàng là một đối tượng và mỗi cột mang một thuộc tính có thứ tự. Các giá trị ở đây đều là ví dụ.

**Quy trình:** Xác định dữ liệu → chọn phép xử lý → chạy code → đọc kết quả và thử trường hợp biên.

```python
attempts,connected=0,False
while attempts<3 and not connected:
    attempts+=1
    connected=(attempts==2)
print(attempts,connected)
```

**Đọc kết quả:** Đối chiếu với giả định đầu vào; đổi dữ liệu và xem kết quả có đúng ý nghĩa không.

### Tình huống 5 — Lập bảng lịch học

**Từ vựng trong mục:** **Iteration** — lần lặp.

**Vấn đề thực tế:** Lập bảng lịch học.

**Vì sao chọn cách này?** Lặp lồng khi có hai chiều sinh viên và ngày; không cần công cụ phức tạp hơn khi một quy tắc rõ ràng đã giải được vấn đề.

**Dữ liệu:** 2 sinh viên, 3 ngày; nếu là bảng thì mỗi hàng là một đối tượng và mỗi cột mang một thuộc tính có thứ tự. Các giá trị ở đây đều là ví dụ.

**Quy trình:** Xác định dữ liệu → chọn phép xử lý → chạy code → đọc kết quả và thử trường hợp biên.

```python
students=["An","Lan"]
for student in students:
    for day in range(1,4):
        print(student,day)
```

**Đọc kết quả:** Đối chiếu với giả định đầu vào; đổi dữ liệu và xem kết quả có đúng ý nghĩa không.

## 6. Nhầm lẫn dễ gặp

Không sử dụng cấu trúc dữ liệu sai với mục đích: ví dụ tập hợp không hỗ trợ truy cập theo chỉ số như list; tuple không sửa từng phần tử. Mọi dữ liệu thật cần xác minh kiểu, đơn vị và tính hợp lệ.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is Iteration? — Thuật ngữ Iteration có nghĩa gì?**

A. A different concept: Lặp qua từng phần tử trong một nhóm — Lặp qua từng phần tử trong một nhóm

B. A concept described as: Một lượt thực hiện trong quá trình lặp — Một lượt thực hiện trong quá trình lặp

C. A different concept: Lặp khi một điều kiện còn đúng — Lặp khi một điều kiện còn đúng

D. A different concept: Dừng hẳn vòng lặp hoặc bỏ qua lượt hiện tại — Dừng hẳn vòng lặp hoặc bỏ qua lượt hiện tại


**Q2. What is For loop? — Thuật ngữ For loop có nghĩa gì?**

A. A concept described as: Lặp qua từng phần tử trong một nhóm — Lặp qua từng phần tử trong một nhóm

B. A different concept: Lặp khi một điều kiện còn đúng — Lặp khi một điều kiện còn đúng

C. A different concept: Dừng hẳn vòng lặp hoặc bỏ qua lượt hiện tại — Dừng hẳn vòng lặp hoặc bỏ qua lượt hiện tại

D. A different concept: Một lượt thực hiện trong quá trình lặp — Một lượt thực hiện trong quá trình lặp


**Q3. What is While loop? — Thuật ngữ While loop có nghĩa gì?**

A. A different concept: Dừng hẳn vòng lặp hoặc bỏ qua lượt hiện tại — Dừng hẳn vòng lặp hoặc bỏ qua lượt hiện tại

B. A different concept: Một lượt thực hiện trong quá trình lặp — Một lượt thực hiện trong quá trình lặp

C. A different concept: Lặp qua từng phần tử trong một nhóm — Lặp qua từng phần tử trong một nhóm

D. A concept described as: Lặp khi một điều kiện còn đúng — Lặp khi một điều kiện còn đúng


**Q4. What is Break/continue? — Thuật ngữ Break/continue có nghĩa gì?**

A. A different concept: Một lượt thực hiện trong quá trình lặp — Một lượt thực hiện trong quá trình lặp

B. A different concept: Lặp qua từng phần tử trong một nhóm — Lặp qua từng phần tử trong một nhóm

C. A concept described as: Dừng hẳn vòng lặp hoặc bỏ qua lượt hiện tại — Dừng hẳn vòng lặp hoặc bỏ qua lượt hiện tại

D. A different concept: Lặp khi một điều kiện còn đúng — Lặp khi một điều kiện còn đúng


**Q5. Which statement fits 'range(start,stop)'? — Mô tả nào đúng với 'range(start,stop)'?**

A. It is used for: Lấy đồng thời vị trí và giá trị — Lấy đồng thời vị trí và giá trị

B. This syntax is used for: Tạo chỉ số nguyên, không bao gồm stop — Tạo chỉ số nguyên, không bao gồm stop

C. It is used for: Dừng sớm khi đã tìm thấy — Dừng sớm khi đã tìm thấy

D. It is used for: Bỏ qua dữ liệu của một lượt lặp — Bỏ qua dữ liệu của một lượt lặp


**Q6. Which statement fits 'enumerate(iterable)'? — Mô tả nào đúng với 'enumerate(iterable)'?**

A. This syntax is used for: Lấy đồng thời vị trí và giá trị — Lấy đồng thời vị trí và giá trị

B. It is used for: Dừng sớm khi đã tìm thấy — Dừng sớm khi đã tìm thấy

C. It is used for: Bỏ qua dữ liệu của một lượt lặp — Bỏ qua dữ liệu của một lượt lặp

D. It is used for: Tạo chỉ số nguyên, không bao gồm stop — Tạo chỉ số nguyên, không bao gồm stop


**Q7. Which statement fits 'break'? — Mô tả nào đúng với 'break'?**

A. It is used for: Bỏ qua dữ liệu của một lượt lặp — Bỏ qua dữ liệu của một lượt lặp

B. It is used for: Tạo chỉ số nguyên, không bao gồm stop — Tạo chỉ số nguyên, không bao gồm stop

C. It is used for: Lấy đồng thời vị trí và giá trị — Lấy đồng thời vị trí và giá trị

D. This syntax is used for: Dừng sớm khi đã tìm thấy — Dừng sớm khi đã tìm thấy


**Q8. Which statement fits 'continue'? — Mô tả nào đúng với 'continue'?**

A. It is used for: Tạo chỉ số nguyên, không bao gồm stop — Tạo chỉ số nguyên, không bao gồm stop

B. It is used for: Lấy đồng thời vị trí và giá trị — Lấy đồng thời vị trí và giá trị

C. This syntax is used for: Bỏ qua dữ liệu của một lượt lặp — Bỏ qua dữ liệu của một lượt lặp

D. It is used for: Dừng sớm khi đã tìm thấy — Dừng sớm khi đã tìm thấy


**Q9. Why use this method in scenario 1? — Vì sao chọn cách này ở tình huống 1?**

A. Because Bỏ qua None nhưng vẫn xử lý các giá trị hợp lệ khác — Bỏ qua None nhưng vẫn xử lý các giá trị hợp lệ khác

B. Because Duyệt từng giao dịch và cộng dồn thay vì gõ từng phép cộng — Duyệt từng giao dịch và cộng dồn thay vì gõ từng phép cộng

C. Because Dừng ngay khi thấy số lượng bằng 0 — Dừng ngay khi thấy số lượng bằng 0

D. Because While có giới hạn số lượt tránh chạy vô hạn — While có giới hạn số lượt tránh chạy vô hạn


**Q10. Why use this method in scenario 2? — Vì sao chọn cách này ở tình huống 2?**

A. Because Bỏ qua None nhưng vẫn xử lý các giá trị hợp lệ khác — Bỏ qua None nhưng vẫn xử lý các giá trị hợp lệ khác

B. Because Dừng ngay khi thấy số lượng bằng 0 — Dừng ngay khi thấy số lượng bằng 0

C. Because While có giới hạn số lượt tránh chạy vô hạn — While có giới hạn số lượt tránh chạy vô hạn

D. Because Lặp lồng khi có hai chiều sinh viên và ngày — Lặp lồng khi có hai chiều sinh viên và ngày


**Q11. Why use this method in scenario 3? — Vì sao chọn cách này ở tình huống 3?**

A. Because While có giới hạn số lượt tránh chạy vô hạn — While có giới hạn số lượt tránh chạy vô hạn

B. Because Lặp lồng khi có hai chiều sinh viên và ngày — Lặp lồng khi có hai chiều sinh viên và ngày

C. Because Duyệt từng giao dịch và cộng dồn thay vì gõ từng phép cộng — Duyệt từng giao dịch và cộng dồn thay vì gõ từng phép cộng

D. Because Dừng ngay khi thấy số lượng bằng 0 — Dừng ngay khi thấy số lượng bằng 0


**Q12. Why use this method in scenario 4? — Vì sao chọn cách này ở tình huống 4?**

A. Because Lặp lồng khi có hai chiều sinh viên và ngày — Lặp lồng khi có hai chiều sinh viên và ngày

B. Because Duyệt từng giao dịch và cộng dồn thay vì gõ từng phép cộng — Duyệt từng giao dịch và cộng dồn thay vì gõ từng phép cộng

C. Because While có giới hạn số lượt tránh chạy vô hạn — While có giới hạn số lượt tránh chạy vô hạn

D. Because Bỏ qua None nhưng vẫn xử lý các giá trị hợp lệ khác — Bỏ qua None nhưng vẫn xử lý các giá trị hợp lệ khác


**Q13. Why use this method in scenario 5? — Vì sao chọn cách này ở tình huống 5?**

A. Because Duyệt từng giao dịch và cộng dồn thay vì gõ từng phép cộng — Duyệt từng giao dịch và cộng dồn thay vì gõ từng phép cộng

B. Because Lặp lồng khi có hai chiều sinh viên và ngày — Lặp lồng khi có hai chiều sinh viên và ngày

C. Because Bỏ qua None nhưng vẫn xử lý các giá trị hợp lệ khác — Bỏ qua None nhưng vẫn xử lý các giá trị hợp lệ khác

D. Because Dừng ngay khi thấy số lượng bằng 0 — Dừng ngay khi thấy số lượng bằng 0


**Q14. What input belongs to scenario 1? — Tình huống 1 sử dụng dữ liệu gì?**

A. The stated input: 3 đơn vị nghìn đồng: 120, 80, 200 — 3 đơn vị nghìn đồng: 120, 80, 200

B. The input is Bốn giá trị nhiệt độ, một None — Bốn giá trị nhiệt độ, một None

C. The input is Bốn mã hàng có số lượng [5,3,0,4] — Bốn mã hàng có số lượng [5,3,0,4]

D. The input is Tối đa ba lần thử kết nối mô phỏng — Tối đa ba lần thử kết nối mô phỏng


**Q15. What input belongs to scenario 2? — Tình huống 2 sử dụng dữ liệu gì?**

A. The input is Bốn mã hàng có số lượng [5,3,0,4] — Bốn mã hàng có số lượng [5,3,0,4]

B. The input is Tối đa ba lần thử kết nối mô phỏng — Tối đa ba lần thử kết nối mô phỏng

C. The input is 2 sinh viên, 3 ngày — 2 sinh viên, 3 ngày

D. The stated input: Bốn giá trị nhiệt độ, một None — Bốn giá trị nhiệt độ, một None


**Q16. What input belongs to scenario 3? — Tình huống 3 sử dụng dữ liệu gì?**

A. The input is Tối đa ba lần thử kết nối mô phỏng — Tối đa ba lần thử kết nối mô phỏng

B. The input is 2 sinh viên, 3 ngày — 2 sinh viên, 3 ngày

C. The stated input: Bốn mã hàng có số lượng [5,3,0,4] — Bốn mã hàng có số lượng [5,3,0,4]

D. The input is 3 đơn vị nghìn đồng: 120, 80, 200 — 3 đơn vị nghìn đồng: 120, 80, 200


**Q17. What input belongs to scenario 4? — Tình huống 4 sử dụng dữ liệu gì?**

A. The input is 2 sinh viên, 3 ngày — 2 sinh viên, 3 ngày

B. The stated input: Tối đa ba lần thử kết nối mô phỏng — Tối đa ba lần thử kết nối mô phỏng

C. The input is 3 đơn vị nghìn đồng: 120, 80, 200 — 3 đơn vị nghìn đồng: 120, 80, 200

D. The input is Bốn giá trị nhiệt độ, một None — Bốn giá trị nhiệt độ, một None


**Q18. What input belongs to scenario 5? — Tình huống 5 sử dụng dữ liệu gì?**

A. The stated input: 2 sinh viên, 3 ngày — 2 sinh viên, 3 ngày

B. The input is 3 đơn vị nghìn đồng: 120, 80, 200 — 3 đơn vị nghìn đồng: 120, 80, 200

C. The input is Bốn giá trị nhiệt độ, một None — Bốn giá trị nhiệt độ, một None

D. The input is Bốn mã hàng có số lượng [5,3,0,4] — Bốn mã hàng có số lượng [5,3,0,4]


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
| Q1 | **B** | A concept described as: Một lượt thực hiện trong quá trình lặp | Một lượt thực hiện trong quá trình lặp |
| Q2 | **A** | A concept described as: Lặp qua từng phần tử trong một nhóm | Lặp qua từng phần tử trong một nhóm |
| Q3 | **D** | A concept described as: Lặp khi một điều kiện còn đúng | Lặp khi một điều kiện còn đúng |
| Q4 | **C** | A concept described as: Dừng hẳn vòng lặp hoặc bỏ qua lượt hiện tại | Dừng hẳn vòng lặp hoặc bỏ qua lượt hiện tại |
| Q5 | **B** | This syntax is used for: Tạo chỉ số nguyên, không bao gồm stop | Tạo chỉ số nguyên, không bao gồm stop |
| Q6 | **A** | This syntax is used for: Lấy đồng thời vị trí và giá trị | Lấy đồng thời vị trí và giá trị |
| Q7 | **D** | This syntax is used for: Dừng sớm khi đã tìm thấy | Dừng sớm khi đã tìm thấy |
| Q8 | **C** | This syntax is used for: Bỏ qua dữ liệu của một lượt lặp | Bỏ qua dữ liệu của một lượt lặp |
| Q9 | **B** | Because Duyệt từng giao dịch và cộng dồn thay vì gõ từng phép cộng | Duyệt từng giao dịch và cộng dồn thay vì gõ từng phép cộng |
| Q10 | **A** | Because Bỏ qua None nhưng vẫn xử lý các giá trị hợp lệ khác | Bỏ qua None nhưng vẫn xử lý các giá trị hợp lệ khác |
| Q11 | **D** | Because Dừng ngay khi thấy số lượng bằng 0 | Dừng ngay khi thấy số lượng bằng 0 |
| Q12 | **C** | Because While có giới hạn số lượt tránh chạy vô hạn | While có giới hạn số lượt tránh chạy vô hạn |
| Q13 | **B** | Because Lặp lồng khi có hai chiều sinh viên và ngày | Lặp lồng khi có hai chiều sinh viên và ngày |
| Q14 | **A** | The stated input: 3 đơn vị nghìn đồng: 120, 80, 200 | 3 đơn vị nghìn đồng: 120, 80, 200 |
| Q15 | **D** | The stated input: Bốn giá trị nhiệt độ, một None | Bốn giá trị nhiệt độ, một None |
| Q16 | **C** | The stated input: Bốn mã hàng có số lượng [5,3,0,4] | Bốn mã hàng có số lượng [5,3,0,4] |
| Q17 | **B** | The stated input: Tối đa ba lần thử kết nối mô phỏng | Tối đa ba lần thử kết nối mô phỏng |
| Q18 | **A** | The stated input: 2 sinh viên, 3 ngày | 2 sinh viên, 3 ngày |
| Q19 | **D** | Input meaning, type and units | Ý nghĩa, kiểu và đơn vị đầu vào |
| Q20 | **C** | Verify output and edge cases | Đối chiếu kết quả và thử trường hợp biên |

## 8. Kết nối bài tiếp theo

`Điều kiện → Vòng lặp → Xử lý hàng loạt`.

# PY-04 — Câu lệnh điều kiện if, elif, else


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Condition** — điều kiện; **Branch** — nhánh.

`Toán tử → Điều kiện → Phân loại theo quy tắc`

Ở bài trước, ta đã biết so sánh và nối các điều kiện. Bài này dùng `if`, `elif`, `else` để chương trình chọn việc cần làm dựa trên kết quả đúng hoặc sai.

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

## 4. Khái niệm liên quan

### 4.1. Condition

**Từ vựng trong mục:** **Condition** — điều kiện.

Điều kiện là phép kiểm tra cho kết quả `True` hoặc `False`. Ví dụ `5 > 3` là đúng nên Python in `True`.

```python
print(5>3)
```

**Kết quả khi chạy:**

```text
True
```

### 4.2. Branch

**Từ vựng trong mục:** **Branch** — nhánh.

Nhánh là phần code chỉ chạy khi điều kiện phù hợp. Sau `if` phải có dấu `:`; các lệnh nằm trong nhánh phải được thụt vào. Trong ví dụ, `True` khiến Python in `ok`.

```python
if True: print('ok')
```

**Kết quả khi chạy:**

```text
ok
```

### 4.3. Threshold

**Từ vựng trong mục:** **Threshold** — ngưỡng.

Ngưỡng là mốc dùng để quyết định kết quả. Chẳng hạn điểm từ 80 trở lên được xét đạt mức B. Phép `85 >= 80` trả về `True`.

```python
print(85>=80)
```

**Kết quả khi chạy:**

```text
True
```

### 4.4. Nested if

**Từ vựng trong mục:** **Nested if** — điều kiện lồng.

`if` lồng nhau nghĩa là kiểm tra thêm một điều kiện bên trong nhánh đã đúng. Ví dụ chỉ kiểm tra số chẵn khi `x` là số dương; với `x = 2`, code in `even`.

```python
x=2
if x>0:
    if x%2==0: print('even')
```

**Kết quả khi chạy:**

```text
even
```

## 5. Năm tình huống lập trình thực tế

### Tình huống 1 — Xếp loại điểm

**Từ vựng trong mục:** **Condition** — điều kiện.

**Tình huống thực tế:** Trung tâm đào tạo xếp điểm từ 90 trở lên là A, từ 80 đến dưới 90 là B, còn lại ghi `Other`. Một học viên đạt 85 điểm trên thang 100.

**Yêu cầu:** Viết chương trình in mức xếp loại của học viên.

**Vì sao chọn cách giải này?** Dùng `if` xét mốc cao nhất trước, `elif` xét mốc 80 khi chưa đạt 90; `else` xử lý các điểm còn lại.

**Quy trình giải:**

1. Lưu điểm `85`.
2. Kiểm tra điểm từ 90 trở lên.
3. Nếu không đạt, kiểm tra từ 80 trở lên.
4. In loại tương ứng.

```python
score=85
if score>=90: grade="A"
elif score>=80: grade="B"
else: grade="Other"
print(grade)
```

**Kết quả khi chạy:**

```text
B
```

**Kết quả:** `B` — 85 điểm đạt mức B theo quy tắc đã nêu.

### Tình huống 2 — Cảnh báo hàng gần hết

**Từ vựng trong mục:** **Branch** — nhánh.

**Tình huống thực tế:** Cửa hàng chia tồn kho thành ba trạng thái: hết hàng nếu số lượng không lớn hơn 0, gần hết nếu còn từ 1 đến 5 món, bình thường nếu còn trên 5 món. Một sản phẩm hiện còn 4 món.

**Yêu cầu:** Viết chương trình in trạng thái tồn kho bằng `Out`, `Low` hoặc `OK`.

**Vì sao chọn cách giải này?** Dùng `if`/`elif`/`else` để chỉ chọn một trong ba trạng thái; kiểm tra hết hàng trước khi kiểm tra gần hết.

**Quy trình giải:**

1. Lưu số lượng `qty = 4`.
2. Kiểm tra hết hàng (`qty <= 0`).
3. Nếu chưa hết, kiểm tra gần hết (`qty <= 5`).
4. In trạng thái phù hợp.

```python
qty=4
if qty<=0: state="Out"
elif qty<=5: state="Low"
else: state="OK"
print(state)
```

**Kết quả khi chạy:**

```text
Low
```

**Kết quả:** `Low` — còn 4 món nên hàng đang gần hết.

### Tình huống 3 — Xét VIP

**Từ vựng trong mục:** **Threshold** — ngưỡng.

**Tình huống thực tế:** Cửa hàng chỉ công nhận VIP khi khách là thành viên ít nhất 5 năm và đã chi tối thiểu 1.000.000 đồng. Một khách đã tham gia 6 năm và chi 1.500.000 đồng.

**Yêu cầu:** In `VIP` nếu khách đạt cả hai điều kiện, ngược lại in `Regular`.

**Vì sao chọn cách giải này?** `and` nối hai phép so sánh; `if` chọn nhánh VIP khi cả hai đúng và `else` xử lý trường hợp còn lại.

**Quy trình giải:**

1. Lưu thời gian tham gia và tổng tiền đã chi.
2. So sánh từng giá trị với ngưỡng.
3. Kết hợp hai điều kiện bằng `and`.
4. In loại khách theo nhánh phù hợp.

```python
years,paid=6,1500000
if years>=5 and paid>=1000000: print("VIP")
else: print("Regular")
```

**Kết quả khi chạy:**

```text
VIP
```

**Kết quả:** `VIP` — khách đạt cả hai ngưỡng quy định.

### Tình huống 4 — Kiểm tra cảm biến

**Từ vựng trong mục:** **Nested if** — điều kiện lồng.

**Tình huống thực tế:** Hệ thống giám sát nhận trạng thái kết nối `online = True` và nhiệt độ `82` °C. Khi thiết bị mất kết nối, màn hình phải hiển thị `Offline`; nếu kết nối, nhiệt độ từ 80 °C trở lên báo `Hot`, còn thấp hơn báo `Normal`.

**Yêu cầu:** Viết chương trình hiển thị đúng trạng thái thiết bị.

**Vì sao chọn cách giải này?** Kiểm tra kết nối bằng `if` trước; chỉ khi đang online mới xét nhiệt độ bằng biểu thức điều kiện. Không kết luận nhiệt độ của thiết bị đã mất kết nối.

**Quy trình giải:**

1. Lưu trạng thái online và nhiệt độ.
2. Nếu online, so sánh nhiệt độ với mốc 80 °C.
3. In `Hot` hoặc `Normal`; nếu offline, in `Offline`.

```python
online,temp=True,82
if online:
    print("Hot" if temp>=80 else "Normal")
else: print("Offline")
```

**Kết quả khi chạy:**

```text
Hot
```

**Kết quả:** `Hot` — thiết bị đang kết nối và nhiệt độ 82 °C đạt ngưỡng cảnh báo.

### Tình huống 5 — Tính quý của tháng

**Từ vựng trong mục:** **Condition** — điều kiện.

**Tình huống thực tế:** Một phần mềm báo cáo cần đổi số tháng thành quý trong năm: tháng 1–3 là quý 1, 4–6 là quý 2, 7–9 là quý 3, 10–12 là quý 4. Tháng cần kiểm tra là tháng 10.

**Yêu cầu:** Viết chương trình in số quý của tháng đã cho; nếu tháng không thuộc khoảng 1–12, in `Invalid`.

**Vì sao chọn cách giải này?** Dùng `if` kiểm tra tháng hợp lệ trước, rồi phép chia nguyên `//` để xác định quý; `else` bắt tháng ngoài khoảng.

**Quy trình giải:**

1. Lưu tháng bằng `month = 10`.
2. Kiểm tra `1 <= month <= 12`.
3. Nếu hợp lệ, tính `(month - 1) // 3 + 1`; ngược lại báo `Invalid`.

```python
month=10
if 1<=month<=12: print((month-1)//3+1)
else: print("Invalid")
```

**Kết quả khi chạy:**

```text
4
```

**Kết quả:** `4` — tháng 10 thuộc quý 4.

## 6. Nhầm lẫn dễ gặp

- Phải đặt dấu `:` sau `if`, `elif`, `else` và thụt các lệnh trong nhánh.
- Nếu một `if`/`elif` đã đúng, các nhánh sau trong cùng chuỗi sẽ không chạy.
- `else` không có điều kiện riêng. Không nhầm `=` (gán giá trị) với `==` (so sánh bằng nhau).
- Khi chia khoảng điểm hay nhiệt độ, phải chọn đúng `>=`, `>`, `<=` để không xếp nhầm giá trị tại ngưỡng.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is Condition? — Thuật ngữ Condition có nghĩa gì?**

A. A block of code selected to run — Phần chương trình được chọn để chạy

B. A test that is true or false — Phép kiểm tra đúng hoặc sai

C. A cutoff point for changing categories — Ranh giới để chuyển trạng thái

D. A second condition checked inside a branch — Kiểm tra bổ sung bên trong một nhánh


**Q2. What is Branch? — Thuật ngữ Branch có nghĩa gì?**

A. A block of code selected to run — Phần chương trình được chọn để chạy

B. A cutoff point for changing categories — Ranh giới để chuyển trạng thái

C. A second condition checked inside a branch — Kiểm tra bổ sung bên trong một nhánh

D. A test that is true or false — Phép kiểm tra đúng hoặc sai


**Q3. What is Threshold? — Thuật ngữ Threshold có nghĩa gì?**

A. A second condition checked inside a branch — Kiểm tra bổ sung bên trong một nhánh

B. A test that is true or false — Phép kiểm tra đúng hoặc sai

C. A block of code selected to run — Phần chương trình được chọn để chạy

D. A cutoff point for changing categories — Ranh giới để chuyển trạng thái


**Q4. What is Nested if? — Thuật ngữ Nested if có nghĩa gì?**

A. A test that is true or false — Phép kiểm tra đúng hoặc sai

B. A block of code selected to run — Phần chương trình được chọn để chạy

C. A second condition checked inside a branch — Kiểm tra bổ sung bên trong một nhánh

D. A cutoff point for changing categories — Ranh giới để chuyển trạng thái


**Q5. Which statement fits 'if expression:'? — Mô tả nào đúng với 'if expression:'?**

A. Try another condition if earlier branches did not match — Thử điều kiện tiếp theo khi nhánh trước không đúng

B. Run the branch only when its condition is true — Chỉ chạy nhánh nếu điều kiện đúng

C. Run the fallback branch without a new condition — Trường hợp còn lại không cần điều kiện mới

D. Check membership or combine conditions — Kiểm tra thành viên hoặc kết hợp nhiều điều kiện


**Q6. Which statement fits 'elif expression:'? — Mô tả nào đúng với 'elif expression:'?**

A. Try another condition if earlier branches did not match — Thử điều kiện tiếp theo khi nhánh trước không đúng

B. Run the fallback branch without a new condition — Trường hợp còn lại không cần điều kiện mới

C. Check membership or combine conditions — Kiểm tra thành viên hoặc kết hợp nhiều điều kiện

D. Run the branch only when its condition is true — Chỉ chạy nhánh nếu điều kiện đúng


**Q7. Which statement fits 'else:'? — Mô tả nào đúng với 'else:'?**

A. Check membership or combine conditions — Kiểm tra thành viên hoặc kết hợp nhiều điều kiện

B. Run the branch only when its condition is true — Chỉ chạy nhánh nếu điều kiện đúng

C. Try another condition if earlier branches did not match — Thử điều kiện tiếp theo khi nhánh trước không đúng

D. Run the fallback branch without a new condition — Trường hợp còn lại không cần điều kiện mới


**Q8. Which statement fits 'in, and, or'? — Mô tả nào đúng với 'in, and, or'?**

A. Run the branch only when its condition is true — Chỉ chạy nhánh nếu điều kiện đúng

B. Try another condition if earlier branches did not match — Thử điều kiện tiếp theo khi nhánh trước không đúng

C. Check membership or combine conditions — Kiểm tra thành viên hoặc kết hợp nhiều điều kiện

D. Run the fallback branch without a new condition — Trường hợp còn lại không cần điều kiện mới


**Q9. Why use this method in scenario 1? — Vì sao chọn cách này ở tình huống 1?**

A. Classify inventory as out, low or normal — Chia tồn kho thành hết/gần hết/bình thường

B. Check highest grade threshold first to avoid misclassification — Kiểm ngưỡng từ cao xuống thấp để không gán sai xếp loại

C. Both membership duration and spending must reach their thresholds — Yêu cầu cả năm đăng ký và mức chi tiêu đạt ngưỡng

D. Check that the device is online before interpreting temperature — Kiểm tra thiết bị online trước khi xét nhiệt độ


**Q10. Why use this method in scenario 2? — Vì sao chọn cách này ở tình huống 2?**

A. Classify inventory as out, low or normal — Chia tồn kho thành hết/gần hết/bình thường

B. Both membership duration and spending must reach their thresholds — Yêu cầu cả năm đăng ký và mức chi tiêu đạt ngưỡng

C. Check that the device is online before interpreting temperature — Kiểm tra thiết bị online trước khi xét nhiệt độ

D. Validate the month range before calculating the quarter — Dùng khoảng tháng hợp lệ trước khi tính quý


**Q11. Why use this method in scenario 3? — Vì sao chọn cách này ở tình huống 3?**

A. Check that the device is online before interpreting temperature — Kiểm tra thiết bị online trước khi xét nhiệt độ

B. Validate the month range before calculating the quarter — Dùng khoảng tháng hợp lệ trước khi tính quý

C. Check highest grade threshold first to avoid misclassification — Kiểm ngưỡng từ cao xuống thấp để không gán sai xếp loại

D. Both membership duration and spending must reach their thresholds — Yêu cầu cả năm đăng ký và mức chi tiêu đạt ngưỡng


**Q12. Why use this method in scenario 4? — Vì sao chọn cách này ở tình huống 4?**

A. Validate the month range before calculating the quarter — Dùng khoảng tháng hợp lệ trước khi tính quý

B. Check highest grade threshold first to avoid misclassification — Kiểm ngưỡng từ cao xuống thấp để không gán sai xếp loại

C. Check that the device is online before interpreting temperature — Kiểm tra thiết bị online trước khi xét nhiệt độ

D. Classify inventory as out, low or normal — Chia tồn kho thành hết/gần hết/bình thường


**Q13. Why use this method in scenario 5? — Vì sao chọn cách này ở tình huống 5?**

A. Check highest grade threshold first to avoid misclassification — Kiểm ngưỡng từ cao xuống thấp để không gán sai xếp loại

B. Validate the month range before calculating the quarter — Dùng khoảng tháng hợp lệ trước khi tính quý

C. Classify inventory as out, low or normal — Chia tồn kho thành hết/gần hết/bình thường

D. Both membership duration and spending must reach their thresholds — Yêu cầu cả năm đăng ký và mức chi tiêu đạt ngưỡng


**Q14. What input belongs to scenario 1? — Tình huống 1 sử dụng dữ liệu gì?**

A. A score of 85 out of 100 — Một điểm số 85/100

B. A stock count of four items — Số lượng 4 món

C. A customer with six membership years and 1,500,000 VND spent — Khách 6 năm và chi 1500000 đồng

D. Temperature 82 °C and online=True — Nhiệt độ 82 độ C và online=True


**Q15. What input belongs to scenario 2? — Tình huống 2 sử dụng dữ liệu gì?**

A. A customer with six membership years and 1,500,000 VND spent — Khách 6 năm và chi 1500000 đồng

B. Temperature 82 °C and online=True — Nhiệt độ 82 độ C và online=True

C. Month 10 — Tháng 10

D. A stock count of four items — Số lượng 4 món


**Q16. What input belongs to scenario 3? — Tình huống 3 sử dụng dữ liệu gì?**

A. Temperature 82 °C and online=True — Nhiệt độ 82 độ C và online=True

B. Month 10 — Tháng 10

C. A customer with six membership years and 1,500,000 VND spent — Khách 6 năm và chi 1500000 đồng

D. A score of 85 out of 100 — Một điểm số 85/100


**Q17. What input belongs to scenario 4? — Tình huống 4 sử dụng dữ liệu gì?**

A. Month 10 — Tháng 10

B. Temperature 82 °C and online=True — Nhiệt độ 82 độ C và online=True

C. A score of 85 out of 100 — Một điểm số 85/100

D. A stock count of four items — Số lượng 4 món


**Q18. What input belongs to scenario 5? — Tình huống 5 sử dụng dữ liệu gì?**

A. Month 10 — Tháng 10

B. A score of 85 out of 100 — Một điểm số 85/100

C. A stock count of four items — Số lượng 4 món

D. A customer with six membership years and 1,500,000 VND spent — Khách 6 năm và chi 1500000 đồng


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
| Q1 | **B** | A test that is true or false | Phép kiểm tra đúng hoặc sai |
| Q2 | **A** | A block of code selected to run | Phần chương trình được chọn để chạy |
| Q3 | **D** | A cutoff point for changing categories | Ranh giới để chuyển trạng thái |
| Q4 | **C** | A second condition checked inside a branch | Kiểm tra bổ sung bên trong một nhánh |
| Q5 | **B** | Run the branch only when its condition is true | Chỉ chạy nhánh nếu điều kiện đúng |
| Q6 | **A** | Try another condition if earlier branches did not match | Thử điều kiện tiếp theo khi nhánh trước không đúng |
| Q7 | **D** | Run the fallback branch without a new condition | Trường hợp còn lại không cần điều kiện mới |
| Q8 | **C** | Check membership or combine conditions | Kiểm tra thành viên hoặc kết hợp nhiều điều kiện |
| Q9 | **B** | Check highest grade threshold first to avoid misclassification | Kiểm ngưỡng từ cao xuống thấp để không gán sai xếp loại |
| Q10 | **A** | Classify inventory as out, low or normal | Chia tồn kho thành hết/gần hết/bình thường |
| Q11 | **D** | Both membership duration and spending must reach their thresholds | Yêu cầu cả năm đăng ký và mức chi tiêu đạt ngưỡng |
| Q12 | **C** | Check that the device is online before interpreting temperature | Kiểm tra thiết bị online trước khi xét nhiệt độ |
| Q13 | **B** | Validate the month range before calculating the quarter | Dùng khoảng tháng hợp lệ trước khi tính quý |
| Q14 | **A** | A score of 85 out of 100 | Một điểm số 85/100 |
| Q15 | **D** | A stock count of four items | Số lượng 4 món |
| Q16 | **C** | A customer with six membership years and 1,500,000 VND spent | Khách 6 năm và chi 1500000 đồng |
| Q17 | **B** | Temperature 82 °C and online=True | Nhiệt độ 82 độ C và online=True |
| Q18 | **A** | Month 10 | Tháng 10 |
| Q19 | **D** | Input meaning, type and units | Ý nghĩa, kiểu và đơn vị đầu vào |
| Q20 | **C** | Verify output and edge cases | Đối chiếu kết quả và thử trường hợp biên |

## 8. Nối sang bài tiếp theo

`Toán tử → Điều kiện → Phân loại theo quy tắc`.

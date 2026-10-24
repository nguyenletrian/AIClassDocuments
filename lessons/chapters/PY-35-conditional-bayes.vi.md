# PY-35 — Xác suất có điều kiện, Bayes và xác suất toàn phần

*DRAFT · Dữ liệu minh họa, các quy tắc khoa học chỉ áp dụng khi giả định được thỏa*

## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Conditional probability** — xác suất có điều kiện; **Independence** — độc lập.

`Biến cố → Điều kiện → Bayes → Đánh giá mô hình AI`

Bài này kết nối dữ liệu thực nghiệm với cách tính xác suất, thống kê và các bước học máy.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Khái niệm |
|---|---|---|
| Conditional probability | xác suất có điều kiện | Khả năng A xảy ra khi biết B đã xảy ra |
| Independence | độc lập | Hai biến cố không ảnh hưởng xác suất của nhau |
| Bayes theorem | định lý Bayes | Cập nhật xác suất giả thuyết khi có bằng chứng |
| Total probability | xác suất toàn phần | Cộng xác suất qua các nhóm loại trừ và đủ |

## 3. Hàm Python và tham số quan trọng

**Từ vựng trong mục:** **Function** — hàm; **Parameter** — tham số.

| Hàm / cú pháp | Cách sử dụng |
|---|---|
| `P(A` | B)=P(A∩B)/P(B) |
| `P(A∩B)=P(A` | B)*P(B) |
| `posterior=likelihood*prior/evidence` | Bayes khi có chứng cứ và mẫu nền |
| `sum(P(Gi)*P(A` | Gi)) |

## 4. Khái niệm liên quan, ví dụ nhỏ

### 4.1. Conditional probability

**Từ vựng trong mục:** **Conditional probability** — xác suất có điều kiện.

Khả năng A xảy ra khi biết B đã xảy ra. Trước khi tính, phân biệt điều kiện áp dụng và ý nghĩa của đầu vào.

```python
print(.2/.5)
```

**Tự kiểm tra:** Conditional probability là gì? **Đáp án:** Khả năng A xảy ra khi biết B đã xảy ra.

### 4.2. Independence

**Từ vựng trong mục:** **Independence** — độc lập.

Hai biến cố không ảnh hưởng xác suất của nhau. Trước khi tính, phân biệt điều kiện áp dụng và ý nghĩa của đầu vào.

```python
print(.4*.5)
```

**Tự kiểm tra:** Independence là gì? **Đáp án:** Hai biến cố không ảnh hưởng xác suất của nhau.

### 4.3. Bayes theorem

**Từ vựng trong mục:** **Bayes theorem** — định lý Bayes.

Cập nhật xác suất giả thuyết khi có bằng chứng. Trước khi tính, phân biệt điều kiện áp dụng và ý nghĩa của đầu vào.

```python
prior=.01;sens=.99;fp=.05
print(sens*prior/(sens*prior+fp*(1-prior)))
```

**Tự kiểm tra:** Bayes theorem là gì? **Đáp án:** Cập nhật xác suất giả thuyết khi có bằng chứng.

### 4.4. Total probability

**Từ vựng trong mục:** **Total probability** — xác suất toàn phần.

Cộng xác suất qua các nhóm loại trừ và đủ. Trước khi tính, phân biệt điều kiện áp dụng và ý nghĩa của đầu vào.

```python
print(.6*.8+.4*.2)
```

**Tự kiểm tra:** Total probability là gì? **Đáp án:** Cộng xác suất qua các nhóm loại trừ và đủ.

## 5. Năm tình huống thực tế

### Tình huống 1 — Đánh giá tín hiệu kiểm tra

**Từ vựng trong mục:** **Conditional probability** — xác suất có điều kiện.

**Vấn đề:** Đánh giá tín hiệu kiểm tra.

**Vì sao chọn phương pháp này?** Cần tính tỷ lệ dương tính thật sau khi nhận kết quả dương. Không dùng kết quả mô phỏng làm bằng chứng thống kê khi thiếu đủ mẫu và giả định.

**Dữ liệu:** Tỷ lệ nền 1%, độ nhạy 99%, dương giả 5%. Các số liệu là giả lập và đơn vị/thứ tự được nêu ngay tại đây; không suy ra kết luận cho người thật.

**Quy trình:** làm rõ giả định → mô tả biến cố/đặc trưng → chọn hàm → kiểm tra kết quả, giới hạn và độ nhạy.

```python
prior=.01;sens=.99;false_positive=.05
posterior=sens*prior/(sens*prior+false_positive*(1-prior))
print(round(posterior,4))
```

**Đọc kết quả:** Đối chiếu kết quả với ý nghĩa xác suất hoặc đơn vị đo; lưu ý sai số và cách lấy mẫu.

### Tình huống 2 — Tỷ lệ mua khi đã xem quảng cáo

**Từ vựng trong mục:** **Independence** — độc lập.

**Vấn đề:** Tỷ lệ mua khi đã xem quảng cáo.

**Vì sao chọn phương pháp này?** Chỉ xét những khách đã thấy quảng cáo. Không dùng kết quả mô phỏng làm bằng chứng thống kê khi thiếu đủ mẫu và giả định.

**Dữ liệu:** 20 mua trên 100 khách đã thấy. Các số liệu là giả lập và đơn vị/thứ tự được nêu ngay tại đây; không suy ra kết luận cho người thật.

**Quy trình:** làm rõ giả định → mô tả biến cố/đặc trưng → chọn hàm → kiểm tra kết quả, giới hạn và độ nhạy.

```python
seen=100;bought_after=20
print(bought_after/seen)
```

**Đọc kết quả:** Đối chiếu kết quả với ý nghĩa xác suất hoặc đơn vị đo; lưu ý sai số và cách lấy mẫu.

### Tình huống 3 — Tính tỷ lệ ủng hộ chung

**Từ vựng trong mục:** **Bayes theorem** — định lý Bayes.

**Vấn đề:** Tính tỷ lệ ủng hộ chung.

**Vì sao chọn phương pháp này?** Gộp các nhóm theo tỷ lệ thành viên thay vì cộng trực tiếp. Không dùng kết quả mô phỏng làm bằng chứng thống kê khi thiếu đủ mẫu và giả định.

**Dữ liệu:** 60% nhóm X ủng hộ 80%, 40% nhóm Y ủng hộ 20%. Các số liệu là giả lập và đơn vị/thứ tự được nêu ngay tại đây; không suy ra kết luận cho người thật.

**Quy trình:** làm rõ giả định → mô tả biến cố/đặc trưng → chọn hàm → kiểm tra kết quả, giới hạn và độ nhạy.

```python
share=[.6,.4];support=[.8,.2]
print(sum(a*b for a,b in zip(share,support)))
```

**Đọc kết quả:** Đối chiếu kết quả với ý nghĩa xác suất hoặc đơn vị đo; lưu ý sai số và cách lấy mẫu.

### Tình huống 4 — Kiểm độc lập hai biến cố

**Từ vựng trong mục:** **Total probability** — xác suất toàn phần.

**Vấn đề:** Kiểm độc lập hai biến cố.

**Vì sao chọn phương pháp này?** So P(A∩B) với P(A)P(B) theo giả định số liệu. Không dùng kết quả mô phỏng làm bằng chứng thống kê khi thiếu đủ mẫu và giả định.

**Dữ liệu:** P(A)=0.5, P(B)=0.4, giao=0.2. Các số liệu là giả lập và đơn vị/thứ tự được nêu ngay tại đây; không suy ra kết luận cho người thật.

**Quy trình:** làm rõ giả định → mô tả biến cố/đặc trưng → chọn hàm → kiểm tra kết quả, giới hạn và độ nhạy.

```python
pa,pb,pab=.5,.4,.2
print(abs(pab-pa*pb)<1e-12)
```

**Đọc kết quả:** Đối chiếu kết quả với ý nghĩa xác suất hoặc đơn vị đo; lưu ý sai số và cách lấy mẫu.

### Tình huống 5 — Phân tích kiểm thử lỗi hàng hóa

**Từ vựng trong mục:** **Conditional probability** — xác suất có điều kiện.

**Vấn đề:** Phân tích kiểm thử lỗi hàng hóa.

**Vì sao chọn phương pháp này?** Bayes giúp tránh hiểu lầm độ nhạy cao nghĩa là xác suất lỗi thật cao. Không dùng kết quả mô phỏng làm bằng chứng thống kê khi thiếu đủ mẫu và giả định.

**Dữ liệu:** Tỷ lệ lỗi 2%, phát hiện lỗi 95%, dương giả 10%. Các số liệu là giả lập và đơn vị/thứ tự được nêu ngay tại đây; không suy ra kết luận cho người thật.

**Quy trình:** làm rõ giả định → mô tả biến cố/đặc trưng → chọn hàm → kiểm tra kết quả, giới hạn và độ nhạy.

```python
p=.02;s=.95;f=.10
print(round(s*p/(s*p+f*(1-p)),3))
```

**Đọc kết quả:** Đối chiếu kết quả với ý nghĩa xác suất hoặc đơn vị đo; lưu ý sai số và cách lấy mẫu.

## 6. Những nhầm lẫn thường gặp

Xác suất có điều kiện cần mẫu nền; xác suất của phân phối liên tục tại một điểm không phải PDF; thống kê từ một nhóm nhỏ không tự chứng minh kết quả cho quần thể. Chú ý định nghĩa mean/std và giả định độc lập.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.


**Q1. What is Conditional probability? — Thuật ngữ Conditional probability là gì?**

A. Another concept means Hai biến cố không ảnh hưởng xác suất của nhau — Hai biến cố không ảnh hưởng xác suất của nhau

B. It means Khả năng A xảy ra khi biết B đã xảy ra — Khả năng A xảy ra khi biết B đã xảy ra

C. Another concept means Cập nhật xác suất giả thuyết khi có bằng chứng — Cập nhật xác suất giả thuyết khi có bằng chứng

D. Another concept means Cộng xác suất qua các nhóm loại trừ và đủ — Cộng xác suất qua các nhóm loại trừ và đủ


**Q2. What is Independence? — Thuật ngữ Independence là gì?**

A. It means Hai biến cố không ảnh hưởng xác suất của nhau — Hai biến cố không ảnh hưởng xác suất của nhau

B. Another concept means Cập nhật xác suất giả thuyết khi có bằng chứng — Cập nhật xác suất giả thuyết khi có bằng chứng

C. Another concept means Cộng xác suất qua các nhóm loại trừ và đủ — Cộng xác suất qua các nhóm loại trừ và đủ

D. Another concept means Khả năng A xảy ra khi biết B đã xảy ra — Khả năng A xảy ra khi biết B đã xảy ra


**Q3. What is Bayes theorem? — Thuật ngữ Bayes theorem là gì?**

A. Another concept means Cộng xác suất qua các nhóm loại trừ và đủ — Cộng xác suất qua các nhóm loại trừ và đủ

B. Another concept means Khả năng A xảy ra khi biết B đã xảy ra — Khả năng A xảy ra khi biết B đã xảy ra

C. Another concept means Hai biến cố không ảnh hưởng xác suất của nhau — Hai biến cố không ảnh hưởng xác suất của nhau

D. It means Cập nhật xác suất giả thuyết khi có bằng chứng — Cập nhật xác suất giả thuyết khi có bằng chứng


**Q4. What is Total probability? — Thuật ngữ Total probability là gì?**

A. Another concept means Khả năng A xảy ra khi biết B đã xảy ra — Khả năng A xảy ra khi biết B đã xảy ra

B. Another concept means Hai biến cố không ảnh hưởng xác suất của nhau — Hai biến cố không ảnh hưởng xác suất của nhau

C. It means Cộng xác suất qua các nhóm loại trừ và đủ — Cộng xác suất qua các nhóm loại trừ và đủ

D. Another concept means Cập nhật xác suất giả thuyết khi có bằng chứng — Cập nhật xác suất giả thuyết khi có bằng chứng


**Q5. What does P(A calculate? — Hàm P(A tính gì?**

A. Another calculation is B)*P(B) — B)*P(B)

B. It calculates B)=P(A∩B)/P(B) — B)=P(A∩B)/P(B)

C. Another calculation is Bayes khi có chứng cứ và mẫu nền — Bayes khi có chứng cứ và mẫu nền

D. Another calculation is Gi)) — Gi))


**Q6. What does P(A∩B)=P(A calculate? — Hàm P(A∩B)=P(A tính gì?**

A. It calculates B)*P(B) — B)*P(B)

B. Another calculation is Bayes khi có chứng cứ và mẫu nền — Bayes khi có chứng cứ và mẫu nền

C. Another calculation is Gi)) — Gi))

D. Another calculation is B)=P(A∩B)/P(B) — B)=P(A∩B)/P(B)


**Q7. What does posterior=likelihood*prior/evidence calculate? — Hàm posterior=likelihood*prior/evidence tính gì?**

A. Another calculation is Gi)) — Gi))

B. Another calculation is B)=P(A∩B)/P(B) — B)=P(A∩B)/P(B)

C. Another calculation is B)*P(B) — B)*P(B)

D. It calculates Bayes khi có chứng cứ và mẫu nền — Bayes khi có chứng cứ và mẫu nền


**Q8. What does sum(P(Gi)*P(A calculate? — Hàm sum(P(Gi)*P(A tính gì?**

A. Another calculation is B)=P(A∩B)/P(B) — B)=P(A∩B)/P(B)

B. Another calculation is B)*P(B) — B)*P(B)

C. It calculates Gi)) — Gi))

D. Another calculation is Bayes khi có chứng cứ và mẫu nền — Bayes khi có chứng cứ và mẫu nền


**Q9. Why use this method in scenario 1? — Vì sao chọn phương pháp trong tình huống 1?**

A. Chỉ xét những khách đã thấy quảng cáo — Chỉ xét những khách đã thấy quảng cáo

B. Cần tính tỷ lệ dương tính thật sau khi nhận kết quả dương — Cần tính tỷ lệ dương tính thật sau khi nhận kết quả dương

C. Gộp các nhóm theo tỷ lệ thành viên thay vì cộng trực tiếp — Gộp các nhóm theo tỷ lệ thành viên thay vì cộng trực tiếp

D. So P(A∩B) với P(A)P(B) theo giả định số liệu — So P(A∩B) với P(A)P(B) theo giả định số liệu


**Q10. Why use this method in scenario 2? — Vì sao chọn phương pháp trong tình huống 2?**

A. Chỉ xét những khách đã thấy quảng cáo — Chỉ xét những khách đã thấy quảng cáo

B. Gộp các nhóm theo tỷ lệ thành viên thay vì cộng trực tiếp — Gộp các nhóm theo tỷ lệ thành viên thay vì cộng trực tiếp

C. So P(A∩B) với P(A)P(B) theo giả định số liệu — So P(A∩B) với P(A)P(B) theo giả định số liệu

D. Bayes giúp tránh hiểu lầm độ nhạy cao nghĩa là xác suất lỗi thật cao — Bayes giúp tránh hiểu lầm độ nhạy cao nghĩa là xác suất lỗi thật cao


**Q11. Why use this method in scenario 3? — Vì sao chọn phương pháp trong tình huống 3?**

A. So P(A∩B) với P(A)P(B) theo giả định số liệu — So P(A∩B) với P(A)P(B) theo giả định số liệu

B. Bayes giúp tránh hiểu lầm độ nhạy cao nghĩa là xác suất lỗi thật cao — Bayes giúp tránh hiểu lầm độ nhạy cao nghĩa là xác suất lỗi thật cao

C. Cần tính tỷ lệ dương tính thật sau khi nhận kết quả dương — Cần tính tỷ lệ dương tính thật sau khi nhận kết quả dương

D. Gộp các nhóm theo tỷ lệ thành viên thay vì cộng trực tiếp — Gộp các nhóm theo tỷ lệ thành viên thay vì cộng trực tiếp


**Q12. Why use this method in scenario 4? — Vì sao chọn phương pháp trong tình huống 4?**

A. Bayes giúp tránh hiểu lầm độ nhạy cao nghĩa là xác suất lỗi thật cao — Bayes giúp tránh hiểu lầm độ nhạy cao nghĩa là xác suất lỗi thật cao

B. Cần tính tỷ lệ dương tính thật sau khi nhận kết quả dương — Cần tính tỷ lệ dương tính thật sau khi nhận kết quả dương

C. So P(A∩B) với P(A)P(B) theo giả định số liệu — So P(A∩B) với P(A)P(B) theo giả định số liệu

D. Chỉ xét những khách đã thấy quảng cáo — Chỉ xét những khách đã thấy quảng cáo


**Q13. Why use this method in scenario 5? — Vì sao chọn phương pháp trong tình huống 5?**

A. Cần tính tỷ lệ dương tính thật sau khi nhận kết quả dương — Cần tính tỷ lệ dương tính thật sau khi nhận kết quả dương

B. Bayes giúp tránh hiểu lầm độ nhạy cao nghĩa là xác suất lỗi thật cao — Bayes giúp tránh hiểu lầm độ nhạy cao nghĩa là xác suất lỗi thật cao

C. Chỉ xét những khách đã thấy quảng cáo — Chỉ xét những khách đã thấy quảng cáo

D. Gộp các nhóm theo tỷ lệ thành viên thay vì cộng trực tiếp — Gộp các nhóm theo tỷ lệ thành viên thay vì cộng trực tiếp


**Q14. Which input is from scenario 1? — Dữ liệu nào thuộc tình huống 1?**

A. The input is Tỷ lệ nền 1%, độ nhạy 99%, dương giả 5% — Tỷ lệ nền 1%, độ nhạy 99%, dương giả 5%

B. Another input is 20 mua trên 100 khách đã thấy — 20 mua trên 100 khách đã thấy

C. Another input is 60% nhóm X ủng hộ 80%, 40% nhóm Y ủng hộ 20% — 60% nhóm X ủng hộ 80%, 40% nhóm Y ủng hộ 20%

D. Another input is P(A)=0.5, P(B)=0.4, giao=0.2 — P(A)=0.5, P(B)=0.4, giao=0.2


**Q15. Which input is from scenario 2? — Dữ liệu nào thuộc tình huống 2?**

A. Another input is 60% nhóm X ủng hộ 80%, 40% nhóm Y ủng hộ 20% — 60% nhóm X ủng hộ 80%, 40% nhóm Y ủng hộ 20%

B. Another input is P(A)=0.5, P(B)=0.4, giao=0.2 — P(A)=0.5, P(B)=0.4, giao=0.2

C. Another input is Tỷ lệ lỗi 2%, phát hiện lỗi 95%, dương giả 10% — Tỷ lệ lỗi 2%, phát hiện lỗi 95%, dương giả 10%

D. The input is 20 mua trên 100 khách đã thấy — 20 mua trên 100 khách đã thấy


**Q16. Which input is from scenario 3? — Dữ liệu nào thuộc tình huống 3?**

A. Another input is P(A)=0.5, P(B)=0.4, giao=0.2 — P(A)=0.5, P(B)=0.4, giao=0.2

B. Another input is Tỷ lệ lỗi 2%, phát hiện lỗi 95%, dương giả 10% — Tỷ lệ lỗi 2%, phát hiện lỗi 95%, dương giả 10%

C. The input is 60% nhóm X ủng hộ 80%, 40% nhóm Y ủng hộ 20% — 60% nhóm X ủng hộ 80%, 40% nhóm Y ủng hộ 20%

D. Another input is Tỷ lệ nền 1%, độ nhạy 99%, dương giả 5% — Tỷ lệ nền 1%, độ nhạy 99%, dương giả 5%


**Q17. Which input is from scenario 4? — Dữ liệu nào thuộc tình huống 4?**

A. Another input is Tỷ lệ lỗi 2%, phát hiện lỗi 95%, dương giả 10% — Tỷ lệ lỗi 2%, phát hiện lỗi 95%, dương giả 10%

B. The input is P(A)=0.5, P(B)=0.4, giao=0.2 — P(A)=0.5, P(B)=0.4, giao=0.2

C. Another input is Tỷ lệ nền 1%, độ nhạy 99%, dương giả 5% — Tỷ lệ nền 1%, độ nhạy 99%, dương giả 5%

D. Another input is 20 mua trên 100 khách đã thấy — 20 mua trên 100 khách đã thấy


**Q18. Which input is from scenario 5? — Dữ liệu nào thuộc tình huống 5?**

A. The input is Tỷ lệ lỗi 2%, phát hiện lỗi 95%, dương giả 10% — Tỷ lệ lỗi 2%, phát hiện lỗi 95%, dương giả 10%

B. Another input is Tỷ lệ nền 1%, độ nhạy 99%, dương giả 5% — Tỷ lệ nền 1%, độ nhạy 99%, dương giả 5%

C. Another input is 20 mua trên 100 khách đã thấy — 20 mua trên 100 khách đã thấy

D. Another input is 60% nhóm X ủng hộ 80%, 40% nhóm Y ủng hộ 20% — 60% nhóm X ủng hộ 80%, 40% nhóm Y ủng hộ 20%


**Q19. What must a statistical report mention? — Báo cáo thống kê cần nêu gì?**

A. Only plot colors — Chỉ màu biểu đồ

B. Only a filename — Chỉ tên tệp

C. Only code line count — Chỉ số dòng code

D. Assumptions, units and sample size — Giả định, đơn vị và kích thước mẫu


**Q20. What makes a numerical result reliable? — Điều gì làm kết quả số đáng tin?**

A. Assuming all data independent — Cho rằng mọi dữ liệu độc lập

B. Deleting verification — Xóa bước xác minh

C. Checking assumptions and edge cases — Kiểm tra giả định và trường hợp biên

D. Ignoring missing inputs — Bỏ dữ liệu thiếu mà không đánh giá

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **B** | It means Khả năng A xảy ra khi biết B đã xảy ra | Khả năng A xảy ra khi biết B đã xảy ra |
| Q2 | **A** | It means Hai biến cố không ảnh hưởng xác suất của nhau | Hai biến cố không ảnh hưởng xác suất của nhau |
| Q3 | **D** | It means Cập nhật xác suất giả thuyết khi có bằng chứng | Cập nhật xác suất giả thuyết khi có bằng chứng |
| Q4 | **C** | It means Cộng xác suất qua các nhóm loại trừ và đủ | Cộng xác suất qua các nhóm loại trừ và đủ |
| Q5 | **B** | It calculates B)=P(A∩B)/P(B) | B)=P(A∩B)/P(B) |
| Q6 | **A** | It calculates B)*P(B) | B)*P(B) |
| Q7 | **D** | It calculates Bayes khi có chứng cứ và mẫu nền | Bayes khi có chứng cứ và mẫu nền |
| Q8 | **C** | It calculates Gi)) | Gi)) |
| Q9 | **B** | Cần tính tỷ lệ dương tính thật sau khi nhận kết quả dương | Cần tính tỷ lệ dương tính thật sau khi nhận kết quả dương |
| Q10 | **A** | Chỉ xét những khách đã thấy quảng cáo | Chỉ xét những khách đã thấy quảng cáo |
| Q11 | **D** | Gộp các nhóm theo tỷ lệ thành viên thay vì cộng trực tiếp | Gộp các nhóm theo tỷ lệ thành viên thay vì cộng trực tiếp |
| Q12 | **C** | So P(A∩B) với P(A)P(B) theo giả định số liệu | So P(A∩B) với P(A)P(B) theo giả định số liệu |
| Q13 | **B** | Bayes giúp tránh hiểu lầm độ nhạy cao nghĩa là xác suất lỗi thật cao | Bayes giúp tránh hiểu lầm độ nhạy cao nghĩa là xác suất lỗi thật cao |
| Q14 | **A** | The input is Tỷ lệ nền 1%, độ nhạy 99%, dương giả 5% | Tỷ lệ nền 1%, độ nhạy 99%, dương giả 5% |
| Q15 | **D** | The input is 20 mua trên 100 khách đã thấy | 20 mua trên 100 khách đã thấy |
| Q16 | **C** | The input is 60% nhóm X ủng hộ 80%, 40% nhóm Y ủng hộ 20% | 60% nhóm X ủng hộ 80%, 40% nhóm Y ủng hộ 20% |
| Q17 | **B** | The input is P(A)=0.5, P(B)=0.4, giao=0.2 | P(A)=0.5, P(B)=0.4, giao=0.2 |
| Q18 | **A** | The input is Tỷ lệ lỗi 2%, phát hiện lỗi 95%, dương giả 10% | Tỷ lệ lỗi 2%, phát hiện lỗi 95%, dương giả 10% |
| Q19 | **D** | Assumptions, units and sample size | Giả định, đơn vị và kích thước mẫu |
| Q20 | **C** | Checking assumptions and edge cases | Kiểm tra giả định và trường hợp biên |

## 8. Liên hệ bài tiếp theo

`Biến cố → Điều kiện → Bayes → Đánh giá mô hình AI`.

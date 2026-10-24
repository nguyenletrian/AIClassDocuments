# PY-42 — Tiền xử lý văn bản, token và Jaccard trong NLP


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Token** — đơn vị từ; **Vocabulary** — từ vựng.

`String → Set → Tokenization → Vector hóa văn bản`

Kiến thức giúp sinh viên dùng Python để hiểu dữ liệu, đánh giá độ bất định và chuẩn bị dữ liệu cho AI.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Khái niệm |
|---|---|---|
| Token | đơn vị từ | Một phần văn bản sau khi tách theo quy tắc |
| Vocabulary | từ vựng | Tập token khác nhau trong dữ liệu |
| Normalization | chuẩn hóa văn bản | Đưa chữ về dạng phù hợp để so khớp |
| Jaccard | tương đồng Jaccard | Tỷ lệ giao trên hợp của hai tập token |

## 3. Thư viện và hàm Python

**Từ vựng trong mục:** **Function** — hàm; **Argument** — đối số.

| Hàm / cách viết | Khi nào dùng, ý nghĩa tham số |
|---|---|
| `str.lower()/strip()` | Chuẩn hóa chữ hoa và khoảng trắng đơn giản |
| `str.split()` | Tách theo khoảng trắng; không đủ cho mọi ngôn ngữ |
| `set(tokens)` | Lọc trùng khi so tập từ vựng |
| `len(a&b)/len(a` | b) |

## 4. Khái niệm với ví dụ nhỏ

### 4.1. Token

**Từ vựng trong mục:** **Token** — đơn vị từ.

Một phần văn bản sau khi tách theo quy tắc. Thử đoạn code để thấy ý nghĩa đầu ra trước khi đọc bài tập.

```python
print('AI helps'.split())
```

**Tự kiểm tra:** Token là gì? **Đáp án:** Một phần văn bản sau khi tách theo quy tắc.

### 4.2. Vocabulary

**Từ vựng trong mục:** **Vocabulary** — từ vựng.

Tập token khác nhau trong dữ liệu. Thử đoạn code để thấy ý nghĩa đầu ra trước khi đọc bài tập.

```python
print(set('AI Python AI'.split()))
```

**Tự kiểm tra:** Vocabulary là gì? **Đáp án:** Tập token khác nhau trong dữ liệu.

### 4.3. Normalization

**Từ vựng trong mục:** **Normalization** — chuẩn hóa văn bản.

Đưa chữ về dạng phù hợp để so khớp. Thử đoạn code để thấy ý nghĩa đầu ra trước khi đọc bài tập.

```python
print('  AI  '.strip().lower())
```

**Tự kiểm tra:** Normalization là gì? **Đáp án:** Đưa chữ về dạng phù hợp để so khớp.

### 4.4. Jaccard

**Từ vựng trong mục:** **Jaccard** — tương đồng Jaccard.

Tỷ lệ giao trên hợp của hai tập token. Thử đoạn code để thấy ý nghĩa đầu ra trước khi đọc bài tập.

```python
a={'ai','python'};b={'ai'}
print(len(a&b)/len(a
```

**Tự kiểm tra:** Jaccard là gì? **Đáp án:** Tỷ lệ giao trên hợp của hai tập token.

## 5. Năm tình huống thực tế

### Tình huống 1 — Chuẩn hóa câu tìm kiếm

**Từ vựng trong mục:** **Token** — đơn vị từ.

**Vấn đề:** Chuẩn hóa câu tìm kiếm.

**Vì sao chọn cách này?** Chữ hoa và khoảng trắng làm tìm kiếm không khớp; không áp dụng kết luận ngoài phạm vi giả định của dữ liệu.

**Dữ liệu:** Chuỗi '  Machine LEARNING '. Dữ liệu ví dụ và đơn vị đo nêu rõ; không thay cho dữ liệu kiểm chứng ngoài đời.

**Quy trình:** làm rõ ý nghĩa đầu vào → chọn phương pháp → chạy code → kiểm tra/diễn giải kết quả.

```python
text="  Machine LEARNING "
print(text.strip().lower())
```

**Đọc kết quả:** Kiểm tra đầu ra với ví dụ, thay đầu vào để thấy giới hạn và trường hợp không phù hợp.

### Tình huống 2 — Tách từ câu đơn giản

**Từ vựng trong mục:** **Vocabulary** — từ vựng.

**Vấn đề:** Tách từ câu đơn giản.

**Vì sao chọn cách này?** split theo khoảng trắng phù hợp demo nhưng không đủ cho tiếng Việt phức tạp; không áp dụng kết luận ngoài phạm vi giả định của dữ liệu.

**Dữ liệu:** Câu tiếng Anh 'AI helps Python'. Dữ liệu ví dụ và đơn vị đo nêu rõ; không thay cho dữ liệu kiểm chứng ngoài đời.

**Quy trình:** làm rõ ý nghĩa đầu vào → chọn phương pháp → chạy code → kiểm tra/diễn giải kết quả.

```python
sentence="AI helps Python"
print(sentence.lower().split())
```

**Đọc kết quả:** Kiểm tra đầu ra với ví dụ, thay đầu vào để thấy giới hạn và trường hợp không phù hợp.

### Tình huống 3 — Lập kho từ vựng

**Từ vựng trong mục:** **Normalization** — chuẩn hóa văn bản.

**Vấn đề:** Lập kho từ vựng.

**Vì sao chọn cách này?** Set lọc token lặp để đếm từ duy nhất; không áp dụng kết luận ngoài phạm vi giả định của dữ liệu.

**Dữ liệu:** Hai câu ngắn tiếng Anh. Dữ liệu ví dụ và đơn vị đo nêu rõ; không thay cho dữ liệu kiểm chứng ngoài đời.

**Quy trình:** làm rõ ý nghĩa đầu vào → chọn phương pháp → chạy code → kiểm tra/diễn giải kết quả.

```python
sentences=["AI uses data","AI uses Python"]
words=set(" ".join(sentences).lower().split())
print(sorted(words))
```

**Đọc kết quả:** Kiểm tra đầu ra với ví dụ, thay đầu vào để thấy giới hạn và trường hợp không phù hợp.

### Tình huống 4 — Độ giống hai tài liệu

**Từ vựng trong mục:** **Jaccard** — tương đồng Jaccard.

**Vấn đề:** Độ giống hai tài liệu.

**Vì sao chọn cách này?** Jaccard xét số từ chung không tính tần suất; không áp dụng kết luận ngoài phạm vi giả định của dữ liệu.

**Dữ liệu:** Hai văn bản có từ 'python' chung. Dữ liệu ví dụ và đơn vị đo nêu rõ; không thay cho dữ liệu kiểm chứng ngoài đời.

**Quy trình:** làm rõ ý nghĩa đầu vào → chọn phương pháp → chạy code → kiểm tra/diễn giải kết quả.

```python
a=set("python for ai".split());b=set("python and sql".split())
print(len(a&b)/len(a|b))
```

**Đọc kết quả:** Kiểm tra đầu ra với ví dụ, thay đầu vào để thấy giới hạn và trường hợp không phù hợp.

### Tình huống 5 — Kiểm văn bản không có từ

**Từ vựng trong mục:** **Token** — đơn vị từ.

**Vấn đề:** Kiểm văn bản không có từ.

**Vì sao chọn cách này?** Hợp rỗng phải được định nghĩa cách trả kết quả tránh chia 0; không áp dụng kết luận ngoài phạm vi giả định của dữ liệu.

**Dữ liệu:** Hai chuỗi rỗng. Dữ liệu ví dụ và đơn vị đo nêu rõ; không thay cho dữ liệu kiểm chứng ngoài đời.

**Quy trình:** làm rõ ý nghĩa đầu vào → chọn phương pháp → chạy code → kiểm tra/diễn giải kết quả.

```python
a=set();b=set()
score=1.0 if not(a|b) else len(a&b)/len(a|b)
print(score)
```

**Đọc kết quả:** Kiểm tra đầu ra với ví dụ, thay đầu vào để thấy giới hạn và trường hợp không phù hợp.

## 6. Nhầm lẫn thường gặp

- Không nhầm thống kê/tỷ lệ mô phỏng với xác suất dự đoán chắc chắn.
- Kiểm tra giả định, cỡ mẫu, đơn vị, độ nhạy kết quả và data leakage trước khi ứng dụng AI thật.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.


**Q1. What is Token? — Khái niệm Token là gì?**

A. Another concept is Tập token khác nhau trong dữ liệu — Tập token khác nhau trong dữ liệu

B. It is Một phần văn bản sau khi tách theo quy tắc — Một phần văn bản sau khi tách theo quy tắc

C. Another concept is Đưa chữ về dạng phù hợp để so khớp — Đưa chữ về dạng phù hợp để so khớp

D. Another concept is Tỷ lệ giao trên hợp của hai tập token — Tỷ lệ giao trên hợp của hai tập token


**Q2. What is Vocabulary? — Khái niệm Vocabulary là gì?**

A. It is Tập token khác nhau trong dữ liệu — Tập token khác nhau trong dữ liệu

B. Another concept is Đưa chữ về dạng phù hợp để so khớp — Đưa chữ về dạng phù hợp để so khớp

C. Another concept is Tỷ lệ giao trên hợp của hai tập token — Tỷ lệ giao trên hợp của hai tập token

D. Another concept is Một phần văn bản sau khi tách theo quy tắc — Một phần văn bản sau khi tách theo quy tắc


**Q3. What is Normalization? — Khái niệm Normalization là gì?**

A. Another concept is Tỷ lệ giao trên hợp của hai tập token — Tỷ lệ giao trên hợp của hai tập token

B. Another concept is Một phần văn bản sau khi tách theo quy tắc — Một phần văn bản sau khi tách theo quy tắc

C. Another concept is Tập token khác nhau trong dữ liệu — Tập token khác nhau trong dữ liệu

D. It is Đưa chữ về dạng phù hợp để so khớp — Đưa chữ về dạng phù hợp để so khớp


**Q4. What is Jaccard? — Khái niệm Jaccard là gì?**

A. Another concept is Một phần văn bản sau khi tách theo quy tắc — Một phần văn bản sau khi tách theo quy tắc

B. Another concept is Tập token khác nhau trong dữ liệu — Tập token khác nhau trong dữ liệu

C. It is Tỷ lệ giao trên hợp của hai tập token — Tỷ lệ giao trên hợp của hai tập token

D. Another concept is Đưa chữ về dạng phù hợp để so khớp — Đưa chữ về dạng phù hợp để so khớp


**Q5. When should str.lower()/strip() be used? — Khi nào nên dùng str.lower()/strip()?**

A. Another operation is for Tách theo khoảng trắng; không đủ cho mọi ngôn ngữ — Tách theo khoảng trắng; không đủ cho mọi ngôn ngữ

B. When you need to Chuẩn hóa chữ hoa và khoảng trắng đơn giản — Chuẩn hóa chữ hoa và khoảng trắng đơn giản

C. Another operation is for Lọc trùng khi so tập từ vựng — Lọc trùng khi so tập từ vựng

D. Another operation is for b) — b)


**Q6. When should str.split() be used? — Khi nào nên dùng str.split()?**

A. When you need to Tách theo khoảng trắng; không đủ cho mọi ngôn ngữ — Tách theo khoảng trắng; không đủ cho mọi ngôn ngữ

B. Another operation is for Lọc trùng khi so tập từ vựng — Lọc trùng khi so tập từ vựng

C. Another operation is for b) — b)

D. Another operation is for Chuẩn hóa chữ hoa và khoảng trắng đơn giản — Chuẩn hóa chữ hoa và khoảng trắng đơn giản


**Q7. When should set(tokens) be used? — Khi nào nên dùng set(tokens)?**

A. Another operation is for b) — b)

B. Another operation is for Chuẩn hóa chữ hoa và khoảng trắng đơn giản — Chuẩn hóa chữ hoa và khoảng trắng đơn giản

C. Another operation is for Tách theo khoảng trắng; không đủ cho mọi ngôn ngữ — Tách theo khoảng trắng; không đủ cho mọi ngôn ngữ

D. When you need to Lọc trùng khi so tập từ vựng — Lọc trùng khi so tập từ vựng


**Q8. When should len(a&b)/len(a be used? — Khi nào nên dùng len(a&b)/len(a?**

A. Another operation is for Chuẩn hóa chữ hoa và khoảng trắng đơn giản — Chuẩn hóa chữ hoa và khoảng trắng đơn giản

B. Another operation is for Tách theo khoảng trắng; không đủ cho mọi ngôn ngữ — Tách theo khoảng trắng; không đủ cho mọi ngôn ngữ

C. When you need to b) — b)

D. Another operation is for Lọc trùng khi so tập từ vựng — Lọc trùng khi so tập từ vựng


**Q9. Why is this method used in scenario 1? — Vì sao dùng phương pháp ở tình huống 1?**

A. split theo khoảng trắng phù hợp demo nhưng không đủ cho tiếng Việt phức tạp — split theo khoảng trắng phù hợp demo nhưng không đủ cho tiếng Việt phức tạp

B. Chữ hoa và khoảng trắng làm tìm kiếm không khớp — Chữ hoa và khoảng trắng làm tìm kiếm không khớp

C. Set lọc token lặp để đếm từ duy nhất — Set lọc token lặp để đếm từ duy nhất

D. Jaccard xét số từ chung không tính tần suất — Jaccard xét số từ chung không tính tần suất


**Q10. Why is this method used in scenario 2? — Vì sao dùng phương pháp ở tình huống 2?**

A. split theo khoảng trắng phù hợp demo nhưng không đủ cho tiếng Việt phức tạp — split theo khoảng trắng phù hợp demo nhưng không đủ cho tiếng Việt phức tạp

B. Set lọc token lặp để đếm từ duy nhất — Set lọc token lặp để đếm từ duy nhất

C. Jaccard xét số từ chung không tính tần suất — Jaccard xét số từ chung không tính tần suất

D. Hợp rỗng phải được định nghĩa cách trả kết quả tránh chia 0 — Hợp rỗng phải được định nghĩa cách trả kết quả tránh chia 0


**Q11. Why is this method used in scenario 3? — Vì sao dùng phương pháp ở tình huống 3?**

A. Jaccard xét số từ chung không tính tần suất — Jaccard xét số từ chung không tính tần suất

B. Hợp rỗng phải được định nghĩa cách trả kết quả tránh chia 0 — Hợp rỗng phải được định nghĩa cách trả kết quả tránh chia 0

C. Chữ hoa và khoảng trắng làm tìm kiếm không khớp — Chữ hoa và khoảng trắng làm tìm kiếm không khớp

D. Set lọc token lặp để đếm từ duy nhất — Set lọc token lặp để đếm từ duy nhất


**Q12. Why is this method used in scenario 4? — Vì sao dùng phương pháp ở tình huống 4?**

A. Hợp rỗng phải được định nghĩa cách trả kết quả tránh chia 0 — Hợp rỗng phải được định nghĩa cách trả kết quả tránh chia 0

B. Chữ hoa và khoảng trắng làm tìm kiếm không khớp — Chữ hoa và khoảng trắng làm tìm kiếm không khớp

C. Jaccard xét số từ chung không tính tần suất — Jaccard xét số từ chung không tính tần suất

D. split theo khoảng trắng phù hợp demo nhưng không đủ cho tiếng Việt phức tạp — split theo khoảng trắng phù hợp demo nhưng không đủ cho tiếng Việt phức tạp


**Q13. Why is this method used in scenario 5? — Vì sao dùng phương pháp ở tình huống 5?**

A. Chữ hoa và khoảng trắng làm tìm kiếm không khớp — Chữ hoa và khoảng trắng làm tìm kiếm không khớp

B. Hợp rỗng phải được định nghĩa cách trả kết quả tránh chia 0 — Hợp rỗng phải được định nghĩa cách trả kết quả tránh chia 0

C. split theo khoảng trắng phù hợp demo nhưng không đủ cho tiếng Việt phức tạp — split theo khoảng trắng phù hợp demo nhưng không đủ cho tiếng Việt phức tạp

D. Set lọc token lặp để đếm từ duy nhất — Set lọc token lặp để đếm từ duy nhất


**Q14. Which input describes scenario 1? — Dữ liệu nào thuộc tình huống 1?**

A. The input is Chuỗi '  Machine LEARNING ' — Chuỗi '  Machine LEARNING '

B. Another input is Câu tiếng Anh 'AI helps Python' — Câu tiếng Anh 'AI helps Python'

C. Another input is Hai câu ngắn tiếng Anh — Hai câu ngắn tiếng Anh

D. Another input is Hai văn bản có từ 'python' chung — Hai văn bản có từ 'python' chung


**Q15. Which input describes scenario 2? — Dữ liệu nào thuộc tình huống 2?**

A. Another input is Hai câu ngắn tiếng Anh — Hai câu ngắn tiếng Anh

B. Another input is Hai văn bản có từ 'python' chung — Hai văn bản có từ 'python' chung

C. Another input is Hai chuỗi rỗng — Hai chuỗi rỗng

D. The input is Câu tiếng Anh 'AI helps Python' — Câu tiếng Anh 'AI helps Python'


**Q16. Which input describes scenario 3? — Dữ liệu nào thuộc tình huống 3?**

A. Another input is Hai văn bản có từ 'python' chung — Hai văn bản có từ 'python' chung

B. Another input is Hai chuỗi rỗng — Hai chuỗi rỗng

C. The input is Hai câu ngắn tiếng Anh — Hai câu ngắn tiếng Anh

D. Another input is Chuỗi '  Machine LEARNING ' — Chuỗi '  Machine LEARNING '


**Q17. Which input describes scenario 4? — Dữ liệu nào thuộc tình huống 4?**

A. Another input is Hai chuỗi rỗng — Hai chuỗi rỗng

B. The input is Hai văn bản có từ 'python' chung — Hai văn bản có từ 'python' chung

C. Another input is Chuỗi '  Machine LEARNING ' — Chuỗi '  Machine LEARNING '

D. Another input is Câu tiếng Anh 'AI helps Python' — Câu tiếng Anh 'AI helps Python'


**Q18. Which input describes scenario 5? — Dữ liệu nào thuộc tình huống 5?**

A. The input is Hai chuỗi rỗng — Hai chuỗi rỗng

B. Another input is Chuỗi '  Machine LEARNING ' — Chuỗi '  Machine LEARNING '

C. Another input is Câu tiếng Anh 'AI helps Python' — Câu tiếng Anh 'AI helps Python'

D. Another input is Hai câu ngắn tiếng Anh — Hai câu ngắn tiếng Anh


**Q19. What should be stated before analyzing data? — Cần nêu gì trước khi phân tích dữ liệu?**

A. Only file extensions — Chỉ đuôi file

B. Only terminal colors — Chỉ màu terminal

C. Only number of lines — Chỉ số dòng code

D. Units, sample meaning and assumptions — Đơn vị, ý nghĩa mẫu và giả định


**Q20. Why is validating results important? — Vì sao cần kiểm tra kết quả?**

A. One example guarantees AI accuracy — Một ví dụ bảo đảm AI đúng

B. It replaces data collection — Nó thay việc thu thập dữ liệu

C. An example may not generalize — Ví dụ có thể không tổng quát

D. It removes test sets — Nó không cần tập kiểm tra

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **B** | It is Một phần văn bản sau khi tách theo quy tắc | Một phần văn bản sau khi tách theo quy tắc |
| Q2 | **A** | It is Tập token khác nhau trong dữ liệu | Tập token khác nhau trong dữ liệu |
| Q3 | **D** | It is Đưa chữ về dạng phù hợp để so khớp | Đưa chữ về dạng phù hợp để so khớp |
| Q4 | **C** | It is Tỷ lệ giao trên hợp của hai tập token | Tỷ lệ giao trên hợp của hai tập token |
| Q5 | **B** | When you need to Chuẩn hóa chữ hoa và khoảng trắng đơn giản | Chuẩn hóa chữ hoa và khoảng trắng đơn giản |
| Q6 | **A** | When you need to Tách theo khoảng trắng; không đủ cho mọi ngôn ngữ | Tách theo khoảng trắng; không đủ cho mọi ngôn ngữ |
| Q7 | **D** | When you need to Lọc trùng khi so tập từ vựng | Lọc trùng khi so tập từ vựng |
| Q8 | **C** | When you need to b) | b) |
| Q9 | **B** | Chữ hoa và khoảng trắng làm tìm kiếm không khớp | Chữ hoa và khoảng trắng làm tìm kiếm không khớp |
| Q10 | **A** | split theo khoảng trắng phù hợp demo nhưng không đủ cho tiếng Việt phức tạp | split theo khoảng trắng phù hợp demo nhưng không đủ cho tiếng Việt phức tạp |
| Q11 | **D** | Set lọc token lặp để đếm từ duy nhất | Set lọc token lặp để đếm từ duy nhất |
| Q12 | **C** | Jaccard xét số từ chung không tính tần suất | Jaccard xét số từ chung không tính tần suất |
| Q13 | **B** | Hợp rỗng phải được định nghĩa cách trả kết quả tránh chia 0 | Hợp rỗng phải được định nghĩa cách trả kết quả tránh chia 0 |
| Q14 | **A** | The input is Chuỗi '  Machine LEARNING ' | Chuỗi '  Machine LEARNING ' |
| Q15 | **D** | The input is Câu tiếng Anh 'AI helps Python' | Câu tiếng Anh 'AI helps Python' |
| Q16 | **C** | The input is Hai câu ngắn tiếng Anh | Hai câu ngắn tiếng Anh |
| Q17 | **B** | The input is Hai văn bản có từ 'python' chung | Hai văn bản có từ 'python' chung |
| Q18 | **A** | The input is Hai chuỗi rỗng | Hai chuỗi rỗng |
| Q19 | **D** | Units, sample meaning and assumptions | Đơn vị, ý nghĩa mẫu và giả định |
| Q20 | **C** | An example may not generalize | Ví dụ có thể không tổng quát |

## 8. Liên hệ bài kế tiếp

`String → Set → Tokenization → Vector hóa văn bản`.

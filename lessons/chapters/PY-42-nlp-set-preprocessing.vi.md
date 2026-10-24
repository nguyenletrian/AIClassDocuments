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

## 3. Hàm và công thức quan trọng

| Cú pháp | Cách dùng |
|---|---|
| `text.strip().lower()` | Bỏ khoảng trắng hai đầu rồi chuyển chữ thường |
| `text.split()` | Tách theo khoảng trắng; không đủ cho mọi ngôn ngữ |
| `set(tokens)` | Lấy token khác nhau, bỏ lượt lặp |
| `len(a & b) / len(a | b)` | Jaccard khi hợp khác rỗng; kiểm tra mẫu số trước khi chia |

## 4. Khái niệm chính và liên quan

**Mạch kiến thức:** Một câu văn trước tiên được chuẩn hóa rồi tách thành token. Các token khác nhau tạo vocabulary; từ hai vocabulary, Jaccard đo mức trùng nhau theo mặt chữ. Cần hiểu sự khác nhau giữa tách từ đơn giản và hiểu ngữ nghĩa.

### 4.1. Token — Đơn vị nhỏ sau quy tắc tách

**Từ vựng:** **Token**.

Trong xử lý ngôn ngữ tự nhiên (NLP), **token** là đơn vị văn bản sau một bước tách: có thể là từ, dấu câu, hoặc phần nhỏ của từ. Với câu tiếng Anh đơn giản `AI helps Python`, `split()` theo khoảng trắng tạo ba token. Đây **không phải** bộ tách từ tiếng Việt chuẩn: một từ ghép tiếng Việt có thể gồm nhiều tiếng và cần tokenizer chuyên biệt.

```python
sentence = 'AI helps Python'
print(sentence.lower().split())
```

**Kết quả khi chạy:**

```text
['ai', 'helps', 'python']
```

Ba token chữ thường sau tách theo khoảng trắng; dấu câu chưa được xử lý.

### 4.2. Vocabulary — Tập token duy nhất

**Từ vựng:** **Vocabulary**.

**Vocabulary** là tập các token **khác nhau** quan sát được trong kho văn bản. Hai câu `AI uses data` và `AI uses Python` có token chung `AI`, `uses`; dùng Set chỉ giữ mỗi từ một lần. Set giúp đếm từ duy nhất nhưng không giữ số lần xuất hiện, khác Bag-of-Words. In qua `sorted()` để không phụ thuộc thứ tự Set.

```python
sentences = ['AI uses data', 'AI uses Python']
tokens = ' '.join(sentences).lower().split()
print(sorted(set(tokens)))
```

**Kết quả khi chạy:**

```text
['ai', 'data', 'python', 'uses']
```

Kho từ vựng có bốn token khác nhau; `ai` và `uses` không bị đếm hai lần.

### 4.3. Normalization — Chuẩn hóa trước khi so từ

**Từ vựng:** **Normalization**.

**Normalization** đưa văn bản về một quy ước nhất quán: bỏ khoảng trắng hai đầu, chuyển chữ về thường, đôi khi xử lý Unicode và dấu câu. Ví dụ `  Machine LEARNING ` chuẩn hóa thành `machine learning`. Nếu không chuẩn hóa, `AI` và `ai` có thể bị xem là hai token; tuy nhiên xóa dấu tiếng Việt tùy tiện có thể làm mất nghĩa.

```python
text = '  Machine LEARNING '
print(text.strip().lower())
```

**Kết quả khi chạy:**

```text
machine learning
```

Khoảng trắng ở đầu/cuối bị bỏ, chữ hoa chuyển thành chữ thường.

### 4.4. Jaccard — Tỷ lệ token chung so với tất cả token

**Từ vựng:** **Jaccard similarity**.

**Jaccard** đo độ giống của hai **tập token**: `J(A,B)=|A∩B|/|A∪B|` nếu hợp khác rỗng. Câu A `python for ai` có ba token; câu B `python and sql` cũng ba token. Giao chỉ có `python` (1 phần tử), hợp có năm từ, nên J=0.2. Jaccard Set không tính tần suất và không hiểu nghĩa tương đương của từ; với hai tập rỗng cần chọn quy ước riêng để tránh chia 0.

```python
a = set('python for ai'.split())
b = set('python and sql'.split())
print(round(len(a & b) / len(a | b), 2))
```

**Kết quả khi chạy:**

```text
0.2
```

Hai tài liệu chung một trên năm token khác nhau; độ giống tập hợp 20%.

## 5. Năm tình huống ứng dụng

### Tình huống 1 — Chuẩn hóa từ khóa tìm kiếm

**Tình huống thực tế:** Thanh tìm kiếm nhận chuỗi `  Machine LEARNING ` từ người dùng. Cần bỏ khoảng trắng hai đầu và đồng nhất chữ thường trước khi so khớp đơn giản.

**Vì sao chọn cách giải này?** `strip().lower()` xử lý đúng hai thay đổi đang cần, không tự xóa dấu hoặc ký tự khác.

**Quy trình giải:**

1. Lưu chuỗi gốc.
2. Gọi `strip()` rồi `lower()` theo thứ tự.
3. In chuỗi chuẩn hóa.

```python
text = '  Machine LEARNING '
print(text.strip().lower())
```

**Kết quả khi chạy:**

```text
machine learning
```

Chuỗi được chuẩn hóa để so với từ khóa cùng quy ước.

### Tình huống 2 — Tách token của câu tiếng Anh

**Tình huống thực tế:** Một ứng dụng tìm kiếm thử nghiệm nhận câu `AI helps Python`, chưa có dấu câu. Cần tách thành các token theo khoảng trắng và đưa về chữ thường.

**Vì sao chọn cách giải này?** `lower().split()` đủ cho câu thử đơn giản; công việc NLP thực cần tokenizer theo ngôn ngữ.

**Quy trình giải:**

1. Lưu câu đầu vào.
2. Chuyển chữ thường rồi tách theo khoảng trắng.
3. In danh sách token theo thứ tự xuất hiện.

```python
sentence = 'AI helps Python'
print(sentence.lower().split())
```

**Kết quả khi chạy:**

```text
['ai', 'helps', 'python']
```

Ba token được tạo; cách làm chưa giải quyết từ ghép tiếng Việt hay dấu câu.

### Tình huống 3 — Tạo kho từ vựng từ hai tài liệu

**Tình huống thực tế:** Hai đoạn `AI uses data`, `AI uses Python` có token lặp. Bộ phận tìm kiếm cần tập các từ khác nhau để xây dựng danh sách tra cứu.

**Vì sao chọn cách giải này?** Set bỏ trùng; sắp xếp khi in giúp học viên kiểm tra kết quả dễ.

**Quy trình giải:**

1. Ghép hai câu bằng khoảng trắng.
2. Chuyển chữ thường, tách và đưa vào Set.
3. Sắp thứ tự token rồi in.

```python
sentences = ['AI uses data', 'AI uses Python']
words = set(' '.join(sentences).lower().split())
print(sorted(words))
```

**Kết quả khi chạy:**

```text
['ai', 'data', 'python', 'uses']
```

Vocabulary có bốn từ khác nhau, không đếm số lần xuất hiện.

### Tình huống 4 — So hai tài liệu bằng Jaccard

**Tình huống thực tế:** Hai câu có từ chung `python`: A=`python for ai`, B=`python and sql`. Đội tìm kiếm muốn tỷ lệ trùng token khác nhau, chưa cần so ngữ nghĩa.

**Vì sao chọn cách giải này?** Jaccard của hai Set cho tỷ lệ giao/hợp; phù hợp so trùng từ không xét tần suất.

**Quy trình giải:**

1. Biến mỗi câu thành Set token.
2. Tính kích thước giao và hợp; kiểm tra hợp không rỗng.
3. Chia, làm tròn hai chữ số và in.

```python
a = set('python for ai'.split())
b = set('python and sql'.split())
print(round(len(a & b) / len(a | b), 2))
```

**Kết quả khi chạy:**

```text
0.2
```

Tập từ trùng chiếm một phần năm tất cả từ, Jaccard bằng 0,2.

### Tình huống 5 — Tránh chia cho 0 ở hai văn bản rỗng

**Tình huống thực tế:** Hệ thống có thể nhận hai chuỗi chỉ gồm khoảng trắng. Sau `split()`, cả hai tập token rỗng. Cần quy ước đánh giá giống nhau 100% trong **ứng dụng này** và tránh chia cho 0.

**Vì sao chọn cách giải này?** Kiểm tra hợp rỗng trước khi chia; kết quả 1 cho hai tập rỗng là **quy ước**, không phải công thức Jaccard thông thường.

**Quy trình giải:**

1. Tách hai chuỗi rỗng thành Set.
2. Nếu hợp rỗng, trả 1.0 theo chính sách này.
3. Ngược lại chia giao cho hợp và in.

```python
a = set(' '.split())
b = set(''.split())
union = a | b
score = 1.0 if not union else len(a & b) / len(union)
print(score)
```

**Kết quả khi chạy:**

```text
1.0
```

Hai tập rỗng được gán độ giống 1.0 theo quy ước đã công bố.

## 6. Sai lầm thường gặp

- Tách theo khoảng trắng không luôn phân đoạn từ tiếng Việt chính xác; tokenizer phụ thuộc ngôn ngữ và mục tiêu.
- `lower()` không xóa dấu câu, `strip()` không xóa mọi khoảng trắng giữa câu.
- Set bỏ trùng nhưng đánh mất thứ tự và tần suất; Jaccard trên Set không hiểu từ đồng nghĩa.
- Mẫu số của Jaccard là kích thước **hợp**, không phải độ dài một tài liệu.
- Hai tập rỗng gây phép chia 0/0, cần nêu rõ quy ước ứng dụng.
- Không so sánh tài liệu khác cách chuẩn hóa, vì khác tiền xử lý sẽ tạo token khác nhau.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Q1. What is a token? — Token là gì?**

A. A unit produced by a text-splitting rule — Đơn vị do quy tắc tách văn bản tạo

B. A collection of distinct tokens — Tập các token khác nhau

C. Applying consistent text representations — Đưa văn bản về dạng biểu diễn nhất quán

D. Intersection size divided by union size — Số phần tử giao chia số phần tử hợp

**Q2. What is a vocabulary? — Vocabulary là gì?**

A. A unit produced by a text-splitting rule — Đơn vị do quy tắc tách văn bản tạo

B. A collection of distinct tokens — Tập các token khác nhau

C. Applying consistent text representations — Đưa văn bản về dạng biểu diễn nhất quán

D. Intersection size divided by union size — Số phần tử giao chia số phần tử hợp

**Q3. What is text normalization? — Chuẩn hóa văn bản là gì?**

A. A unit produced by a text-splitting rule — Đơn vị do quy tắc tách văn bản tạo

B. A collection of distinct tokens — Tập các token khác nhau

C. Applying consistent text representations — Đưa văn bản về dạng biểu diễn nhất quán

D. Intersection size divided by union size — Số phần tử giao chia số phần tử hợp

**Q4. What is set-based Jaccard similarity? — Jaccard trên Set là gì?**

A. A unit produced by a text-splitting rule — Đơn vị do quy tắc tách văn bản tạo

B. A collection of distinct tokens — Tập các token khác nhau

C. Applying consistent text representations — Đưa văn bản về dạng biểu diễn nhất quán

D. Intersection size divided by union size — Số phần tử giao chia số phần tử hợp

**Q5. What does `str.split()` do without arguments? — `str.split()` không đối số làm gì?**

A. Splits on runs of whitespace — Tách theo chuỗi khoảng trắng liên tiếp

B. Converts letters to lowercase — Chuyển chữ thành chữ thường

C. Removes leading and trailing whitespace — Bỏ khoảng trắng hai đầu

D. To deduplicate and display consistently — Để bỏ token trùng và hiển thị ổn định

**Q6. What does `lower()` do? — `lower()` làm gì?**

A. Splits on runs of whitespace — Tách theo chuỗi khoảng trắng liên tiếp

B. Converts letters to lowercase — Chuyển chữ thành chữ thường

C. Removes leading and trailing whitespace — Bỏ khoảng trắng hai đầu

D. To deduplicate and display consistently — Để bỏ token trùng và hiển thị ổn định

**Q7. What does `strip()` do? — `strip()` làm gì?**

A. Splits on runs of whitespace — Tách theo chuỗi khoảng trắng liên tiếp

B. Converts letters to lowercase — Chuyển chữ thành chữ thường

C. Removes leading and trailing whitespace — Bỏ khoảng trắng hai đầu

D. To deduplicate and display consistently — Để bỏ token trùng và hiển thị ổn định

**Q8. Why use `sorted(set(tokens))` for examples? — Vì sao dùng `sorted(set(tokens))`?**

A. Splits on runs of whitespace — Tách theo chuỗi khoảng trắng liên tiếp

B. Converts letters to lowercase — Chuyển chữ thành chữ thường

C. Removes leading and trailing whitespace — Bỏ khoảng trắng hai đầu

D. To deduplicate and display consistently — Để bỏ token trùng và hiển thị ổn định

**Q9. What does A & B produce for sets? — A & B trên Set tạo gì?**

A. Common tokens — Các token chung

B. All distinct tokens from either set — Mọi token khác nhau thuộc ít nhất một tập

C. It ignores repeated occurrences — Bỏ qua số lần lặp

D. 1.0 — 1.0

**Q10. What does A | B produce for sets? — A | B trên Set tạo gì?**

A. Common tokens — Các token chung

B. All distinct tokens from either set — Mọi token khác nhau thuộc ít nhất một tập

C. It ignores repeated occurrences — Bỏ qua số lần lặp

D. 1.0 — 1.0

**Q11. How does Set Jaccard treat token frequency? — Jaccard Set xử lý tần suất token ra sao?**

A. Common tokens — Các token chung

B. All distinct tokens from either set — Mọi token khác nhau thuộc ít nhất một tập

C. It ignores repeated occurrences — Bỏ qua số lần lặp

D. 1.0 — 1.0

**Q12. What happens for identical nonempty token sets? — Hai tập token giống hệt và không rỗng cho Jaccard gì?**

A. Common tokens — Các token chung

B. All distinct tokens from either set — Mọi token khác nhau thuộc ít nhất một tập

C. It ignores repeated occurrences — Bỏ qua số lần lặp

D. 1.0 — 1.0

**Q13. What happens for disjoint nonempty token sets? — Hai tập token rời không rỗng cho Jaccard gì?**

A. 0.0 — 0.0

B. The formula has zero denominator; choose a convention — Công thức có mẫu số 0; cần quy ước riêng

C. No, multi-syllable words need more care — Không, từ nhiều tiếng cần xử lý thêm

D. No; punctuation remains — Không, dấu câu vẫn còn

**Q14. What happens when both sets are empty? — Nếu hai Set đều rỗng thì Jaccard sao?**

A. 0.0 — 0.0

B. The formula has zero denominator; choose a convention — Công thức có mẫu số 0; cần quy ước riêng

C. No, multi-syllable words need more care — Không, từ nhiều tiếng cần xử lý thêm

D. No; punctuation remains — Không, dấu câu vẫn còn

**Q15. Does whitespace splitting correctly segment all Vietnamese words? — split theo khoảng trắng có tách đúng mọi từ tiếng Việt không?**

A. 0.0 — 0.0

B. The formula has zero denominator; choose a convention — Công thức có mẫu số 0; cần quy ước riêng

C. No, multi-syllable words need more care — Không, từ nhiều tiếng cần xử lý thêm

D. No; punctuation remains — Không, dấu câu vẫn còn

**Q16. Can lowercasing alone remove punctuation? — Chỉ lower() có xóa dấu câu không?**

A. 0.0 — 0.0

B. The formula has zero denominator; choose a convention — Công thức có mẫu số 0; cần quy ước riêng

C. No, multi-syllable words need more care — Không, từ nhiều tiếng cần xử lý thêm

D. No; punctuation remains — Không, dấu câu vẫn còn

**Q17. Does Jaccard understand semantic synonyms? — Jaccard theo Set có hiểu từ đồng nghĩa không?**

A. No, it compares literal token identities — Không, nó so token theo mặt chữ

B. Number of distinct tokens in either document — Số token khác nhau ở ít nhất một tài liệu

C. Word order and term frequencies — Thứ tự và tần suất từ

D. For complex punctuation or multilingual segmentation — Khi có dấu câu phức tạp hoặc phân đoạn đa ngôn ngữ

**Q18. What does len(A|B) represent? — len(A|B) biểu thị gì?**

A. No, it compares literal token identities — Không, nó so token theo mặt chữ

B. Number of distinct tokens in either document — Số token khác nhau ở ít nhất một tài liệu

C. Word order and term frequencies — Thứ tự và tần suất từ

D. For complex punctuation or multilingual segmentation — Khi có dấu câu phức tạp hoặc phân đoạn đa ngôn ngữ

**Q19. What is lost when building a vocabulary as a Set? — Tạo vocabulary bằng Set mất thông tin nào?**

A. No, it compares literal token identities — Không, nó so token theo mặt chữ

B. Number of distinct tokens in either document — Số token khác nhau ở ít nhất một tài liệu

C. Word order and term frequencies — Thứ tự và tần suất từ

D. For complex punctuation or multilingual segmentation — Khi có dấu câu phức tạp hoặc phân đoạn đa ngôn ngữ

**Q20. When should a specialized tokenizer be considered? — Khi nào nên xem bộ tách từ chuyên biệt?**

A. No, it compares literal token identities — Không, nó so token theo mặt chữ

B. Number of distinct tokens in either document — Số token khác nhau ở ít nhất một tài liệu

C. Word order and term frequencies — Thứ tự và tần suất từ

D. For complex punctuation or multilingual segmentation — Khi có dấu câu phức tạp hoặc phân đoạn đa ngôn ngữ

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **A** | Tokens may be words, word pieces, or punctuation depending on the tokenizer. | Token có thể là từ, mảnh từ hoặc dấu câu tùy bộ tách. |
| Q2 | **B** | Vocabulary deduplicates token identities, unlike a frequency list. | Tập từ vựng bỏ trùng danh tính token, khác bảng tần suất. |
| Q3 | **C** | Lowercasing and trimming help match equivalent surface forms. | Chữ thường và cắt khoảng trắng giúp khớp dạng văn bản. |
| Q4 | **D** | It measures shared distinct tokens relative to all distinct tokens. | Nó đo từ khác nhau chung so với tổng số từ khác nhau. |
| Q5 | **A** | Whitespace splitting does not understand all language word boundaries. | Tách bằng khoảng trắng không hiểu mọi ranh giới từ. |
| Q6 | **B** | It can align case variants for matching but does not remove punctuation. | Giúp so biến thể chữ hoa/thường nhưng không bỏ dấu câu. |
| Q7 | **C** | Interior whitespace is not removed by strip. | strip không xóa khoảng trắng giữa câu. |
| Q8 | **D** | Sets are unordered for display, sorted returns an ordered list. | Set không bảo đảm thứ tự; sorted tạo List có thứ tự. |
| Q9 | **A** | The intersection contains values present in both sets. | Giao chỉ giữ giá trị có ở cả hai tập. |
| Q10 | **B** | The union deduplicates tokens occurring in both. | Hợp loại token trùng ở cả hai bên. |
| Q11 | **C** | Converting to Set removes counts and word order. | Chuyển sang Set mất số lần và thứ tự từ. |
| Q12 | **D** | Their intersection equals their union. | Giao bằng hợp nên tỷ số bằng một. |
| Q13 | **A** | There are no shared tokens in the numerator. | Không có token chung nên tử số bằng không. |
| Q14 | **B** | No mathematical quotient is defined for 0/0. | Phép chia 0/0 không xác định; ứng dụng phải tự quy định. |
| Q15 | **C** | Whitespace-separated syllables need not be distinct lexical words. | Các tiếng ngăn bởi khoảng trắng chưa chắc là từ độc lập. |
| Q16 | **D** | Case conversion and punctuation handling are separate steps. | Đổi chữ thường và xử lý dấu câu là hai bước khác nhau. |
| Q17 | **A** | Different words can mean the same but have zero direct overlap. | Hai từ khác chữ dù đồng nghĩa vẫn có thể không chung token. |
| Q18 | **B** | The union is the denominator of set Jaccard. | Hợp là mẫu số của Jaccard trên Set. |
| Q19 | **C** | Set records membership only, not sequence or counts. | Set chỉ lưu sự có mặt, không lưu vị trí hay lượt xuất hiện. |
| Q20 | **D** | A language-aware tokenizer can handle boundaries beyond whitespace. | Tokenizer theo ngôn ngữ xử lý ranh giới vượt quá khoảng trắng. |

## 8. Liên hệ bài kế tiếp

`String → Set → Tokenization → Vector hóa văn bản`.

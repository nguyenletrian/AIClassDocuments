# PY-42 — Tiền xử lý văn bản, token và Jaccard trong NLP


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Token** — đơn vị từ; **Vocabulary** — từ vựng.

`String → Set → Tokenization → Vector hóa văn bản`

**Học xong dùng để làm gì?** Làm sạch văn bản, tách token và tạo tập từ để so sánh hoặc phân loại nội dung.

**Kết nối kiến thức tiếp theo:** PY-43 quản lý các phiên bản mã/tiền xử lý bằng Git để thí nghiệm tái tạo được.

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
| `len(a & b) / len(a \| b)` | Jaccard khi hợp khác rỗng; kiểm tra mẫu số trước khi chia |

## 4. Khái niệm chính và liên quan

**Mạch kiến thức:** Một câu văn trước tiên được chuẩn hóa rồi tách thành token. Các token khác nhau tạo vocabulary; từ hai vocabulary, Jaccard đo mức trùng nhau theo mặt chữ. Cần hiểu sự khác nhau giữa tách từ đơn giản và hiểu ngữ nghĩa.

### 4.1. Token — Đơn vị nhỏ sau quy tắc tách

**Từ vựng:** **Token**.

Trong xử lý ngôn ngữ tự nhiên (NLP), **token** là đơn vị văn bản sau một bước tách: có thể là từ, dấu câu, hoặc phần nhỏ của từ. Với câu tiếng Anh đơn giản `AI helps Python`, `split()` theo khoảng trắng tạo ba token. Đây **không phải** bộ tách từ tiếng Việt chuẩn: một từ ghép tiếng Việt có thể gồm nhiều tiếng và cần tokenizer chuyên biệt.

```python
# Mục đích: Đơn vị nhỏ sau quy tắc tách.
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
# Mục đích: Tập token duy nhất.
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
# Mục đích: Chuẩn hóa trước khi so từ.
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
# Mục đích: Tỷ lệ token chung so với tất cả token.
a = set('python for ai'.split())
b = set('python and sql'.split())
print(round(len(a & b) / len(a | b), 2))
```

**Kết quả khi chạy:**

```text
0.2
```

Hai tài liệu chung một trên năm token khác nhau; độ giống tập hợp 20%.

## 5. Năm tình huống tiền xử lý NLP — từ 10 từ khóa đến 20 phiếu hỗ trợ

### Tình huống 1 — Cấp 1: Chuẩn hóa 10 từ khóa tìm kiếm khác kiểu viết

**Từ vựng trong mục:** **Normalization** — chuẩn hóa; **Vocabulary** — kho từ khác nhau.

**Tình huống thực tế:** Thư viện nhận **10 lượt tìm kiếm**, mỗi hàng là một cụm từ người dùng nhập, có thể thừa khoảng trắng hay khác chữ hoa/thường. Muốn thống kê số cụm khác nhau để tránh coi `Python` và `PYTHON` thành hai yêu cầu, nhưng **không xóa dấu tiếng Việt** vì có thể đổi nghĩa.

**Vì sao chọn cách này?** `strip().lower()` đưa chuỗi về cách ghi nhất quán, Set đếm số cụm duy nhất. Đây là **chuẩn hóa chữ**, không phải hiểu ý định tìm kiếm của người dùng.

**Quy trình:**
1. Lưu 10 cụm từ theo đúng đầu vào.
2. Chuẩn hóa khoảng trắng hai đầu và chữ hoa/thường.
3. In số lượt và danh sách cụm duy nhất theo thứ tự ổn định.

```python
queries = [" Python ","PYTHON","AI"," ai ","Data","DATA","NLP","nLp","Máy học","máy học"]
normalized = [text.strip().lower() for text in queries]
unique = sorted(set(normalized))
assert len(queries) == 10
print("Lượt tìm:", len(queries))
print("Cụm khác nhau:", len(unique))
print("Cụm:", ", ".join(unique))
```

**Kết quả khi chạy:**

```text
Lượt tìm: 10
Cụm khác nhau: 5
Cụm: ai, data, máy học, nlp, python
```

Từ `máy học` vẫn gồm hai tiếng cách nhau bằng dấu cách. Nếu cần phân tích từ ghép tiếng Việt, phải có tokenizer phù hợp hơn.

### Tình huống 2 — Cấp 2: Tách token của 12 lời nhắn có dấu câu

**Từ vựng trong mục:** **Tokenization** — tách token; **Regex** — biểu thức chính quy.

**Tình huống thực tế:** Nhóm hỗ trợ có **12 lời nhắn tiếng Anh ngắn**, mỗi hàng là một tin nhắn, có dấu chấm và chấm than. Cần tách thành token chữ thường, đếm tổng lượt token và số token khác nhau mà không giữ dấu câu thành nội dung từ.

**Vì sao chọn cách này?** `re.findall(r'[a-z]+', ...)` chỉ là quy tắc đơn giản thích hợp **tiếng Anh ASCII** trong bài. Nó không xử lý chính xác từ ghép tiếng Việt, emoji hay chữ Unicode khác.

**Quy trình:**
1. Tạo 12 tin nhắn không rỗng.
2. Chuẩn hóa chữ thường và tìm chuỗi chữ a–z bằng regex.
3. Đếm tổng token và vốn từ khác nhau để thấy một từ có thể lặp.

```python
import re
messages = ["AI helps Python.","Python helps teams!","Data drives AI.","AI uses data.","Python cleans data.","Teams learn Python.","AI supports teams.","Data needs quality.","Learn AI with Python.","Quality data matters.","Python helps AI.","Teams review data."]
tokens = [word for text in messages for word in re.findall(r"[a-z]+", text.lower())]
vocabulary = set(tokens)
assert len(messages) == 12
print("Tin nhắn:", len(messages))
print("Lượt token:", len(tokens))
print("Token khác nhau:", len(vocabulary))
print("Có từ python:", "python" in vocabulary)
```

**Kết quả khi chạy:**

```text
Tin nhắn: 12
Lượt token: 37
Token khác nhau: 15
Có từ python: True
```

Tổng lượt token tính cả từ lặp, còn vocabulary chỉ tính từ duy nhất — hai đại lượng không thay thế nhau.

### Tình huống 3 — Cấp 3: So Bag-of-Words và Set trên 15 tiêu đề khóa học

**Từ vựng trong mục:** **Bag-of-Words** — đếm lần xuất hiện; **Counter** — bảng tần suất.

**Tình huống thực tế:** Trang học trực tuyến có **15 tiêu đề khóa học**; mỗi hàng gồm một chủ đề Python/AI/Data và từ `course`. Bộ phận tìm kiếm muốn biết từ phổ biến nhất để lập chỉ mục; nếu chỉ dùng Set sẽ đánh mất thông tin từ `course` xuất hiện trong từng tiêu đề.

**Vì sao chọn cách này?** `Counter` giữ số lần xuất hiện của từng token, trong khi `set()` chỉ trả từ khác nhau. Đếm hai cách trên cùng **15 tài liệu** giúp hiểu tần suất không đồng nghĩa kho từ.

**Quy trình:**
1. Lưu 15 tiêu đề có hai token mỗi tiêu đề.
2. Tách từ, dùng Counter để đếm toàn bộ lượt.
3. In số từ khác nhau, tổng lượt token, tên và tần suất của từ phổ biến nhất.

```python
from collections import Counter
headings = ["python course","ai course","data course","python course","ai course","data course","python course","ai course","data course","python course","ai course","data course","python course","ai course","data course"]
tokens = [token for heading in headings for token in heading.split()]
counts = Counter(tokens)
most_common = counts.most_common(1)[0]
assert len(headings) == 15
print("Tiêu đề:", len(headings))
print("Lượt token:", len(tokens))
print("Từ khác nhau:", len(counts))
print("Từ phổ biến nhất:", most_common[0])
print("Số lượt:", most_common[1])
```

**Kết quả khi chạy:**

```text
Tiêu đề: 15
Lượt token: 30
Từ khác nhau: 4
Từ phổ biến nhất: course
Số lượt: 15
```

Từ `course` phổ biến nhất vì có mặt trong mọi tiêu đề; chưa chắc đây là từ tốt nhất để **phân biệt chủ đề** giữa các khóa học.

### Tình huống 4 — Cấp 4: Xếp hạng 18 phiếu hỗ trợ theo Jaccard, có nội dung rỗng

**Từ vựng trong mục:** **Jaccard** — tỷ lệ token chung; **Ranking** — xếp hạng; **Empty-set guard** — bảo vệ mẫu rỗng.

**Tình huống thực tế:** Bộ phận kỹ thuật có **18 phiếu hỗ trợ** T01–T18, mỗi hàng là một mô tả tiếng Anh; có một phiếu để trống đang chờ bổ sung. Người trực quầy tìm các phiếu giống truy vấn `login password` nhất, chỉ so mặt chữ và không suy diễn rằng hai yêu cầu có cùng nguyên nhân.

**Vì sao chọn cách này?** Jaccard Set chia số token chung cho số token khác nhau của hai phía, cần xử lý union rỗng để không chia cho 0. Dùng ID khi đồng điểm để xếp hạng ổn định, đồng thời đếm phiếu rỗng riêng.

**Quy trình:**
1. Chuẩn hóa token cho cả 18 phiếu; phiếu rỗng thành tập rỗng.
2. Tính Jaccard với hai token của truy vấn, sắp theo điểm giảm và ID tăng.
3. In ba phiếu gần nhất và số phiếu không có token.

```python
import re
texts = ["login password reset","login password issue","reset login account","payment invoice request","refund payment card","shipment tracking delayed","delivery package status","account password change","login device blocked","payment not received","invoice missing pdf","courier lost shipment","delivery date change","reset password urgent","account verification failed","general help needed","","password login help"]
def words(text):
    return set(re.findall(r"[a-z]+", text.lower()))
def similarity(a,b):
    common = a & b
    union = a | b
    return len(common)/len(union) if union else 0.0
query = words("login password")
ranked = [(f"T{i:02d}", similarity(query, words(text))) for i,text in enumerate(texts,1)]
ranked.sort(key=lambda row:(-row[1],row[0]))
assert len(texts) == 18
print("Phiếu:", len(texts))
print("Thiếu nội dung:", sum(not words(text) for text in texts))
for code, value in ranked[:3]:
    print(f"{code}: {value:.3f}")
```

**Kết quả khi chạy:**

```text
Phiếu: 18
Thiếu nội dung: 1
T01: 0.667
T02: 0.667
T18: 0.667
```

Jaccard Set bỏ thông tin **thứ tự và tần suất**; phiếu điểm cao vẫn cần người xem ngữ cảnh để trả lời đúng.

### Tình huống 5 — Cấp 5: Định tuyến 20 phiếu qua ba nhóm từ vựng và báo nhóm chưa rõ

**Từ vựng trong mục:** **Rule-based classification** — phân loại theo quy tắc; **Tie-break** — phân xử hòa; **Unknown** — chưa xác định.

**Tình huống thực tế:** Đội chăm sóc khách hàng có **20 phiếu** P01–P20 với mô tả tiếng Anh; mỗi phiếu cần chuyển đến nhóm `account`, `billing`, `delivery` hoặc `unknown` nếu không có token trùng. Một phiếu cuối hoàn toàn rỗng. Hãy phân nhóm từ các tập từ khóa minh họa và kiểm chứng không tự gán phiếu không liên quan cho một nhóm bất kỳ.

**Vì sao chọn cách này?** Set và Jaccard cung cấp cách **định tuyến theo chữ xuất hiện**, nhưng không phải mô hình hiểu ý nghĩa. Khi điểm mọi nhóm đều bằng 0 phải trả `unknown`; nếu bằng điểm dương thì dùng tên nhóm theo thứ tự ổn định thay vì phụ thuộc thứ tự Set.

**Quy trình:**
1. Lưu đủ 20 phiếu và ba nhóm từ khóa.
2. Chuẩn hóa token, tính Jaccard giữa phiếu với từng nhóm.
3. Chọn nhóm điểm dương cao nhất, còn 0 thì unknown; tổng hợp số phiếu của từng nhóm.

```python
import re
from collections import Counter
texts = ["login password reset urgent","invoice payment refund request","shipment delivery tracking update","general question please","login password reset urgent","invoice payment refund request","shipment delivery tracking update","general question please","login password reset urgent","invoice payment refund request","shipment delivery tracking update","general question please","login password reset urgent","invoice payment refund request","shipment delivery tracking update","general question please","login password reset urgent","invoice payment refund request","shipment delivery tracking update",""]
keywords = {"account": {"login","password","reset"},
            "billing": {"invoice","payment","refund"},
            "delivery": {"shipment","delivery","tracking"}}
def tokens(text):
    return set(re.findall(r"[a-z]+", text.lower()))
def route(text):
    words = tokens(text)
    scores = {}
    for name,vocabulary in keywords.items():
        union = words | vocabulary
        scores[name] = len(words & vocabulary)/len(union) if union else 0
    name = sorted(scores, key=lambda n:(-scores[n], n))[0]
    return name if scores[name] > 0 else "unknown"
counts = Counter(route(text) for text in texts)
assert len(texts) == 20
print("Phiếu:", len(texts))
for name in ("account","billing","delivery","unknown"):
    print(f"{name}: {counts[name]}")
print("Phiếu rỗng:", sum(not tokens(t) for t in texts))
```

**Kết quả khi chạy:**

```text
Phiếu: 20
account: 5
billing: 5
delivery: 5
unknown: 5
Phiếu rỗng: 1
```

Quy tắc này không được coi là AI đã **học** từ dữ liệu. Phiếu unknown là yêu cầu bổ sung nội dung hoặc người thật kiểm tra, không phải lỗi cần xóa.

## 6. Sai lầm thường gặp

- Tách theo khoảng trắng không luôn phân đoạn từ tiếng Việt chính xác; tokenizer phụ thuộc ngôn ngữ và mục tiêu.
- `lower()` không xóa dấu câu, `strip()` không xóa mọi khoảng trắng giữa câu.
- Set bỏ trùng nhưng đánh mất thứ tự và tần suất; Jaccard trên Set không hiểu từ đồng nghĩa.
- Mẫu số của Jaccard là kích thước **hợp**, không phải độ dài một tài liệu.
- Hai tập rỗng gây phép chia 0/0, cần nêu rõ quy ước ứng dụng.
- Không so sánh tài liệu khác cách chuẩn hóa, vì khác tiền xử lý sẽ tạo token khác nhau.

## 7. Trắc nghiệm

**Q1. What is a token? | Token là gì?**

A. A unit produced by a text-splitting rule | Đơn vị do quy tắc tách văn bản tạo

B. A collection of distinct tokens | Tập các token khác nhau

C. Applying consistent text representations | Đưa văn bản về dạng biểu diễn nhất quán

D. Intersection size divided by union size | Số phần tử giao chia số phần tử hợp

**Đáp án: A**

**Giải thích:** Token có thể là từ, mảnh từ hoặc dấu câu tùy bộ tách. Đơn vị cụ thể phụ thuộc quy tắc tokenizer; token không nhất thiết là một từ hoàn chỉnh.


**Q2. What is a vocabulary? | Vocabulary là gì?**

A. A unit produced by a text-splitting rule | Đơn vị do quy tắc tách văn bản tạo

B. A collection of distinct tokens | Tập các token khác nhau

C. Applying consistent text representations | Đưa văn bản về dạng biểu diễn nhất quán

D. Intersection size divided by union size | Số phần tử giao chia số phần tử hợp

**Đáp án: B**

**Giải thích:** Tập từ vựng bỏ trùng danh tính token, khác bảng tần suất. Nó trả lời có những token nào, chứ không trả lời mỗi token xuất hiện bao nhiêu lần.


**Q3. What is text normalization? | Chuẩn hóa văn bản là gì?**

A. A unit produced by a text-splitting rule | Đơn vị do quy tắc tách văn bản tạo

B. A collection of distinct tokens | Tập các token khác nhau

C. Applying consistent text representations | Đưa văn bản về dạng biểu diễn nhất quán

D. Intersection size divided by union size | Số phần tử giao chia số phần tử hợp

**Đáp án: C**

**Giải thích:** Chữ thường và cắt khoảng trắng giúp khớp dạng văn bản. Chuẩn hóa đổi cách biểu diễn; quy tắc phải nhất quán giữa các văn bản đem so.


**Q4. What is set-based Jaccard similarity? | Jaccard trên Set là gì?**

A. A unit produced by a text-splitting rule | Đơn vị do quy tắc tách văn bản tạo

B. A collection of distinct tokens | Tập các token khác nhau

C. Applying consistent text representations | Đưa văn bản về dạng biểu diễn nhất quán

D. Intersection size divided by union size | Số phần tử giao chia số phần tử hợp

**Đáp án: D**

**Giải thích:** Nó đo từ khác nhau chung so với tổng số từ khác nhau. Một từ chung trong năm từ khác nhau cho 1/5, không phải lấy độ dài một câu làm mẫu số.


**Q5. What does `str.split()` do without arguments? | `str.split()` không đối số làm gì?**

A. Splits on runs of whitespace | Tách theo chuỗi khoảng trắng liên tiếp

B. Converts letters to lowercase | Chuyển chữ thành chữ thường

C. Removes leading and trailing whitespace | Bỏ khoảng trắng hai đầu

D. To deduplicate and display consistently | Để bỏ token trùng và hiển thị ổn định

**Đáp án: A**

**Giải thích:** Tách bằng khoảng trắng không hiểu mọi ranh giới từ. Đây là quy tắc tách chuỗi, không phải thuật toán phân đoạn từ tiếng Việt về mặt ngôn ngữ.


**Q6. What does `lower()` do? | `lower()` làm gì?**

A. Splits on runs of whitespace | Tách theo chuỗi khoảng trắng liên tiếp

B. Converts letters to lowercase | Chuyển chữ thành chữ thường

C. Removes leading and trailing whitespace | Bỏ khoảng trắng hai đầu

D. To deduplicate and display consistently | Để bỏ token trùng và hiển thị ổn định

**Đáp án: B**

**Giải thích:** Giúp so biến thể chữ hoa/thường nhưng không bỏ dấu câu. `lower` chỉ đổi chữ hoa/thường, không tự xóa khoảng trắng hoặc tách token.


**Q7. What does `strip()` do? | `strip()` làm gì?**

A. Splits on runs of whitespace | Tách theo chuỗi khoảng trắng liên tiếp

B. Converts letters to lowercase | Chuyển chữ thành chữ thường

C. Removes leading and trailing whitespace | Bỏ khoảng trắng hai đầu

D. To deduplicate and display consistently | Để bỏ token trùng và hiển thị ổn định

**Đáp án: C**

**Giải thích:** strip không xóa khoảng trắng giữa câu. Muốn xử lý khoảng trắng giữa câu cần `split` hoặc bước khác, không thể chỉ dùng `strip`.


**Q8. Why use `sorted(set(tokens))` for examples? | Vì sao dùng `sorted(set(tokens))`?**

A. Splits on runs of whitespace | Tách theo chuỗi khoảng trắng liên tiếp

B. Converts letters to lowercase | Chuyển chữ thành chữ thường

C. Removes leading and trailing whitespace | Bỏ khoảng trắng hai đầu

D. To deduplicate and display consistently | Để bỏ token trùng và hiển thị ổn định

**Đáp án: D**

**Giải thích:** Set không bảo đảm thứ tự; sorted tạo List có thứ tự. Set loại phần tử trùng, còn `sorted` tạo List có thứ tự để in ổn định.


**Q9. What does A & B produce for sets? | A & B trên Set tạo gì?**

A. Common tokens | Các token chung

B. All distinct tokens from either set | Mọi token khác nhau thuộc ít nhất một tập

C. It ignores repeated occurrences | Bỏ qua số lần lặp

D. 1.0 | 1.0

**Đáp án: A**

**Giải thích:** Giao chỉ giữ giá trị có ở cả hai tập. Với A={'ai','python'}, B={'ai'}, giao chỉ có 'ai', không chứa toàn bộ A.


**Q10. What does A | B produce for sets? | A | B trên Set tạo gì?**

A. Common tokens | Các token chung

B. All distinct tokens from either set | Mọi token khác nhau thuộc ít nhất một tập

C. It ignores repeated occurrences | Bỏ qua số lần lặp

D. 1.0 | 1.0

**Đáp án: B**

**Giải thích:** Hợp loại token trùng ở cả hai bên. Hợp gồm từ riêng ở mỗi bên lẫn các từ chung giữa hai bên.


**Q11. How does Set Jaccard treat token frequency? | Jaccard Set xử lý tần suất token ra sao?**

A. Common tokens | Các token chung

B. All distinct tokens from either set | Mọi token khác nhau thuộc ít nhất một tập

C. It ignores repeated occurrences | Bỏ qua số lần lặp

D. 1.0 | 1.0

**Đáp án: C**

**Giải thích:** Chuyển sang Set mất số lần và thứ tự từ. Vì vậy Jaccard trên Set không phân biệt từ xuất hiện một lần với mười lần.


**Q12. What happens for identical nonempty token sets? | Hai tập token giống hệt và không rỗng cho Jaccard gì?**

A. Common tokens | Các token chung

B. All distinct tokens from either set | Mọi token khác nhau thuộc ít nhất một tập

C. It ignores repeated occurrences | Bỏ qua số lần lặp

D. 1.0 | 1.0

**Đáp án: D**

**Giải thích:** Giao bằng hợp nên tỷ số bằng một. Kết quả này áp dụng khi hợp không rỗng, đúng điều kiện đã nêu trong câu hỏi.


**Q13. What happens for disjoint nonempty token sets? | Hai tập token rời không rỗng cho Jaccard gì?**

A. 0.0 | 0.0

B. The formula has zero denominator; choose a convention | Công thức có mẫu số 0; cần quy ước riêng

C. No, multi-syllable words need more care | Không, từ nhiều tiếng cần xử lý thêm

D. No; punctuation remains | Không, dấu câu vẫn còn

**Đáp án: A**

**Giải thích:** Không có token chung nên tử số bằng không. Tử số bằng không nhưng mẫu số vẫn dương.


**Q14. What happens when both sets are empty? | Nếu hai Set đều rỗng thì Jaccard sao?**

A. 0.0 | 0.0

B. The formula has zero denominator; choose a convention | Công thức có mẫu số 0; cần quy ước riêng

C. No, multi-syllable words need more care | Không, từ nhiều tiếng cần xử lý thêm

D. No; punctuation remains | Không, dấu câu vẫn còn

**Đáp án: B**

**Giải thích:** Phép chia 0/0 không xác định; ứng dụng phải tự quy định. Ứng dụng có thể quy ước hai văn bản rỗng giống nhau 1, nhưng hệ khác có thể chọn 0 hoặc không xác định.


**Q15. Does whitespace splitting correctly segment all Vietnamese words? | split theo khoảng trắng có tách đúng mọi từ tiếng Việt không?**

A. 0.0 | 0.0

B. The formula has zero denominator; choose a convention | Công thức có mẫu số 0; cần quy ước riêng

C. No, multi-syllable words need more care | Không, từ nhiều tiếng cần xử lý thêm

D. No; punctuation remains | Không, dấu câu vẫn còn

**Đáp án: C**

**Giải thích:** Các tiếng ngăn bởi khoảng trắng chưa chắc là từ độc lập. Một từ tiếng Việt có thể gồm nhiều tiếng được ngăn bằng khoảng trắng.


**Q16. Can lowercasing alone remove punctuation? | Chỉ lower() có xóa dấu câu không?**

A. 0.0 | 0.0

B. The formula has zero denominator; choose a convention | Công thức có mẫu số 0; cần quy ước riêng

C. No, multi-syllable words need more care | Không, từ nhiều tiếng cần xử lý thêm

D. No; punctuation remains | Không, dấu câu vẫn còn

**Đáp án: D**

**Giải thích:** Đổi chữ thường và xử lý dấu câu là hai bước khác nhau. Dấu câu có thể còn dính vào token cho đến khi có bước làm sạch/tách riêng.


**Q17. Does Jaccard understand semantic synonyms? | Jaccard theo Set có hiểu từ đồng nghĩa không?**

A. No, it compares literal token identities | Không, nó so token theo mặt chữ

B. Number of distinct tokens in either document | Số token khác nhau ở ít nhất một tài liệu

C. Word order and term frequencies | Thứ tự và tần suất từ

D. For complex punctuation or multilingual segmentation | Khi có dấu câu phức tạp hoặc phân đoạn đa ngôn ngữ

**Đáp án: A**

**Giải thích:** Hai từ khác chữ dù đồng nghĩa vẫn có thể không chung token. Jaccard đo trùng mặt chữ; muốn so ý nghĩa cần biểu diễn ngôn ngữ phong phú hơn.


**Q18. What does len(A|B) represent? | len(A|B) biểu thị gì?**

A. No, it compares literal token identities | Không, nó so token theo mặt chữ

B. Number of distinct tokens in either document | Số token khác nhau ở ít nhất một tài liệu

C. Word order and term frequencies | Thứ tự và tần suất từ

D. For complex punctuation or multilingual segmentation | Khi có dấu câu phức tạp hoặc phân đoạn đa ngôn ngữ

**Đáp án: B**

**Giải thích:** Hợp là mẫu số của Jaccard trên Set. Khi hợp khác rỗng, đây là mẫu số; chỉ dùng len(A) có thể khiến điểm sai.


**Q19. What is lost when building a vocabulary as a Set? | Tạo vocabulary bằng Set mất thông tin nào?**

A. No, it compares literal token identities | Không, nó so token theo mặt chữ

B. Number of distinct tokens in either document | Số token khác nhau ở ít nhất một tài liệu

C. Word order and term frequencies | Thứ tự và tần suất từ

D. For complex punctuation or multilingual segmentation | Khi có dấu câu phức tạp hoặc phân đoạn đa ngôn ngữ

**Đáp án: C**

**Giải thích:** Set chỉ lưu sự có mặt, không lưu vị trí hay lượt xuất hiện. Khi cần đếm số lần hoặc giữ thứ tự, hãy dùng Counter hoặc List token.


**Q20. When should a specialized tokenizer be considered? | Khi nào nên xem bộ tách từ chuyên biệt?**

A. No, it compares literal token identities | Không, nó so token theo mặt chữ

B. Number of distinct tokens in either document | Số token khác nhau ở ít nhất một tài liệu

C. Word order and term frequencies | Thứ tự và tần suất từ

D. For complex punctuation or multilingual segmentation | Khi có dấu câu phức tạp hoặc phân đoạn đa ngôn ngữ

**Đáp án: D**

**Giải thích:** Tokenizer theo ngôn ngữ xử lý ranh giới vượt quá khoảng trắng. Chọn bộ tách phù hợp ngôn ngữ và dùng thống nhất lúc lập chỉ mục lẫn lúc truy vấn.

## 8. Liên hệ bài kế tiếp

`String → Set → Tokenization → Vector hóa văn bản`.

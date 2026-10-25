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

**No Note — Không chú thích**

```python
sentence = 'AI helps Python'
print(sentence.lower().split())
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tách một câu thành token chữ thường để chuẩn hóa từ ngữ trước khi so sánh.
# Dữ liệu: Câu 'AI helps Python' gồm ba từ cách nhau bởi dấu cách; chưa có dấu câu.
# Giữ câu gốc có chữ hoa để minh họa bước chuẩn hóa.
sentence = 'AI helps Python'
# lower() tạo chuỗi mới viết thường; split() tách theo khoảng trắng và trả list token, KHÔNG tự loại dấu câu.
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

**No Note — Không chú thích**

```python
sentences = ['AI uses data', 'AI uses Python']
tokens = ' '.join(sentences).lower().split()
print(sorted(set(tokens)))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tạo tập token duy nhất từ hai câu sau khi ghép và chuẩn hóa.
# Dữ liệu: Hai câu có từ AI và uses lặp lại; cần danh sách TỪ KHÁC NHAU, không phải tần suất.
# List gồm hai câu đầu vào; mỗi phần tử là một chuỗi.
sentences = ['AI uses data', 'AI uses Python']
# join() nối hai câu bằng dấu cách, tránh nối dính từ cuối câu trước với từ đầu câu sau.
# lower() chuẩn hóa chữ thường rồi split() tách token theo khoảng trắng.
tokens = ' '.join(sentences).lower().split()
# set() bỏ các token lặp; sorted() xếp tăng theo chữ để kết quả in ổn định.
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

**No Note — Không chú thích**

```python
text = '  Machine LEARNING '
print(text.strip().lower())
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Dọn dấu cách thừa hai đầu và viết thường một cụm tìm kiếm.
# Dữ liệu: Chuỗi gốc có khoảng trắng thừa và chữ hoa 'Machine LEARNING'.
# Chuỗi đầu vào vẫn giữ nguyên dấu cách/chữ hoa khi chưa xử lý.
text = '  Machine LEARNING '
# strip() bỏ khoảng trắng ở ĐẦU/CUỐI, không xóa khoảng trắng giữa từ; lower() đổi sang chữ thường, không sửa biến text gốc.
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

**No Note — Không chú thích**

```python
a = set('python for ai'.split())
b = set('python and sql'.split())
print(round(len(a & b) / len(a | b), 2))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Đo độ tương đồng Jaccard giữa hai câu qua tập các từ.
# Dữ liệu: Hai cụm có chung từ python; tập hợp hợp nhất có năm từ khác nhau.
# split() chia theo dấu cách, set() bỏ từ trùng để chỉ còn những từ duy nhất của câu A.
a = set('python for ai'.split())
# Tạo tập từ B theo cùng quy tắc để so công bằng.
b = set('python and sql'.split())
# & là giao các từ chung; | là hợp các từ không trùng; len() đếm số từ, chia tạo Jaccard từ 0 đến 1, round(...,2) chỉ làm tròn khi in.
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

**Tình huống thực tế:** Thư viện ghi **10 lượt nhập từ khóa tìm sách**; một người gõ ` Python `, người khác gõ `PYTHON`, có người gõ `Máy học` và `máy học`. Bộ phận tìm kiếm muốn biết có bao nhiêu **cụm từ khác nhau theo cách viết đã chuẩn hóa**, không đếm nhiều lần cùng một nội dung chỉ vì chữ hoa hay khoảng trắng. Cần giữ nguyên **dấu tiếng Việt**, vì bỏ dấu có thể đổi nghĩa từ.

**Vì sao chọn cách này?** **Chuẩn hóa văn bản** là đưa các cách viết khác nhau về một dạng **nhất quán** trước khi so sánh. `strip()` bỏ khoảng trắng thừa ở **hai đầu** chuỗi, `lower()` đổi sang chữ thường nên `Python` và `PYTHON` trở thành cùng một từ khóa. `set(normalized)` chỉ giữ **mỗi cụm đã chuẩn hóa một lần**, còn `sorted()` sắp để in kết quả ổn định. Các bước này chỉ giải quyết **khác biệt cách viết**, không hiểu câu hỏi tìm kiếm hay tự nối hai từ đồng nghĩa; đặc biệt không tự bỏ dấu tiếng Việt.

**Quy trình:**
1. Lưu 10 cụm từ theo đúng đầu vào.
2. Chuẩn hóa khoảng trắng hai đầu và chữ hoa/thường.
3. In số lượt và danh sách cụm duy nhất theo thứ tự ổn định.

**No Note — Không chú thích**

```python
queries = [" Python ","PYTHON","AI"," ai ","Data","DATA","NLP","nLp","Máy học","máy học"]
normalized = []
for text in queries:
    normalized.append(text.strip().lower())
unique = sorted(set(normalized))
if len(queries) != 10:
    raise ValueError("Cần đủ 10 lượt tìm kiếm.")
print("Lượt tìm:", len(queries))
print("Cụm khác nhau:", len(unique))
print("Cụm:", ", ".join(unique))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Chuẩn hóa mười lượt tìm kiếm và đếm số cụm khác nhau sau khi bỏ chữ hoa/khoảng trắng.
# Dữ liệu: 10 chuỗi truy vấn có bản sao khác kiểu chữ và khoảng trắng; vẫn giữ tiếng Việt có dấu.
# Danh sách mười LƯỢT tìm kiếm; cùng ý định có thể xuất hiện nhiều lần.
queries = [" Python ","PYTHON","AI"," ai ","Data","DATA","NLP","nLp","Máy học","máy học"]
# List mới chứa chuỗi chuẩn hóa theo cùng thứ tự, không ghi đè queries gốc.
normalized = []
# Duyệt một lượt cho mỗi truy vấn.
for text in queries:
    # strip() xóa khoảng trắng hai đầu, lower() đổi chữ hoa sang chữ thường, không bỏ dấu tiếng Việt.
    # append() thêm kết quả chuẩn hóa vào list mới.
    normalized.append(text.strip().lower())
# set() bỏ các truy vấn trùng sau chuẩn hóa; sorted() sắp danh sách khác nhau cho dễ đọc.
unique = sorted(set(normalized))
# len() kiểm đủ mười lượt gốc trước khi kết luận.
if len(queries) != 10:
    # Báo lỗi khi dữ liệu thiếu hoặc sai số lượt, tránh đánh giá không đủ mẫu.
    raise ValueError("Cần đủ 10 lượt tìm kiếm.")
print("Lượt tìm:", len(queries))
# Đếm số cụm KHÁC NHAU, không phải tổng lượt.
print("Cụm khác nhau:", len(unique))
# join() nối các cụm khác nhau bằng dấu phẩy và khoảng trắng.
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

**Tình huống thực tế:** Đội hỗ trợ lưu **12 tin nhắn tiếng Anh ngắn**, chẳng hạn `AI helps Python.` và `Python helps teams!`. Mỗi hàng là **một tin nhắn**, có khoảng trắng và dấu câu. Nhân viên muốn tách thành từng từ **chữ thường**, biết tổng **lượt từ xuất hiện** và có bao nhiêu **từ khác nhau**, rồi kiểm tra từ `python` có xuất hiện không.

**Vì sao chọn cách này?** **Token** là đơn vị văn bản chương trình tách ra để xử lý, trong ví dụ này là **chuỗi chữ cái tiếng Anh**. `re.findall(r'[a-z]+', text.lower())` bỏ dấu chấm/chấm than rồi lấy từng nhóm chữ từ **12 lời nhắn**; danh sách `tokens` giữ **tất cả lượt xuất hiện**, còn `set(tokens)` tạo **vốn từ không lặp**. Từ `python` xuất hiện nhiều lần nhưng chỉ có một mục trong tập từ. Quy tắc `[a-z]` được chọn vì dữ liệu mẫu là **tiếng Anh ASCII**, không phải bộ tách từ chính xác cho tiếng Việt, emoji hay mọi ngôn ngữ.

**Quy trình:**
1. Tạo 12 tin nhắn không rỗng.
2. Chuẩn hóa chữ thường và tìm chuỗi chữ a–z bằng regex.
3. Đếm tổng token và vốn từ khác nhau để thấy một từ có thể lặp.

**No Note — Không chú thích**

```python
import re
messages = ["AI helps Python.","Python helps teams!","Data drives AI.","AI uses data.","Python cleans data.","Teams learn Python.","AI supports teams.","Data needs quality.","Learn AI with Python.","Quality data matters.","Python helps AI.","Teams review data."]
tokens = []
for text in messages:
    for word in re.findall(r"[a-z]+", text.lower()):
        tokens.append(word)
vocabulary = set(tokens)
if len(messages) != 12:
    raise ValueError("Cần đủ 12 tin nhắn.")
print("Tin nhắn:", len(messages))
print("Lượt token:", len(tokens))
print("Token khác nhau:", len(vocabulary))
print("Có từ python:", "python" in vocabulary)
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tách token chữ cái trong 12 tin nhắn và xây vốn từ duy nhất.
# Dữ liệu: 12 câu tiếng Anh có dấu chấm/chấm than; muốn đếm lượt token và số từ khác nhau.
# re là thư viện chuẩn cho biểu thức chính quy (regex), dùng tách từ bỏ dấu câu.
import re
# List 12 tin nhắn; mỗi phần tử là một câu với dấu câu có thể khác nhau.
messages = ["AI helps Python.","Python helps teams!","Data drives AI.","AI uses data.","Python cleans data.","Teams learn Python.","AI supports teams.","Data needs quality.","Learn AI with Python.","Quality data matters.","Python helps AI.","Teams review data."]
# Lưu MỌI lượt token, kể cả những từ lặp lại qua các câu.
tokens = []
# Duyệt từng tin nhắn riêng.
for text in messages:
    # lower() chuyển chữ thường; findall() tìm mọi CHUỖI LIÊN TIẾP chỉ gồm a..z, bỏ dấu câu/chữ số và không hỗ trợ nguyên vẹn từ tiếng Việt có dấu.
    for word in re.findall(r"[a-z]+", text.lower()):
        # append() giữ mỗi lần xuất hiện của từ, kể cả khi trùng.
        tokens.append(word)
# set() biến các lượt token thành vốn từ duy nhất, bỏ lặp.
vocabulary = set(tokens)
# Kiểm đủ 12 tin nhắn nguồn.
if len(messages) != 12:
    # Dừng khi nguồn thiếu tin nhắn theo kịch bản.
    raise ValueError("Cần đủ 12 tin nhắn.")
print("Tin nhắn:", len(messages))
# Đếm tổng lượt xuất hiện của token (có lặp).
print("Lượt token:", len(tokens))
# Đếm số token khác nhau (không lặp).
print("Token khác nhau:", len(vocabulary))
# in kiểm từ python có trong set hay không, trả Boolean.
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

**Tình huống thực tế:** Trang đào tạo có **15 tiêu đề khóa học**, mỗi tiêu đề gồm tên chủ đề `python`, `ai` hoặc `data` và từ `course`. Vì `course` được lặp lại trong mọi tiêu đề, nhân viên muốn tìm **từ phổ biến nhất và số lượt của từ ấy** để xây danh sách tra cứu. Họ cũng muốn biết **kho từ riêng biệt** gồm bao nhiêu từ; chỉ đếm từ khác nhau sẽ không cho biết mức độ phổ biến.

**Vì sao chọn cách này?** **Tần suất** trả lời 'một từ xuất hiện **bao nhiêu lần**', khác **vốn từ** chỉ trả lời 'có **những từ nào**'. Chương trình tách hai từ trong từng tiêu đề bằng `split()`, ghép tất cả thành một danh sách rồi dùng `Counter` cộng lượt xuất hiện của từng token. `most_common(1)` tìm từ nhiều lượt nhất: `course` xuất hiện ở **cả 15 tiêu đề**, còn các tên chủ đề xuất hiện ít hơn. Nếu đổi toàn bộ token sang set ngay lúc đầu, `course` sẽ chỉ còn một lần và **mất thông tin để xếp tần suất**; vì thế dùng Counter trước và nhìn số khóa để biết số từ khác nhau.

**Quy trình:**
1. Lưu 15 tiêu đề có hai token mỗi tiêu đề.
2. Tách từ, dùng Counter để đếm toàn bộ lượt.
3. In số từ khác nhau, tổng lượt token, tên và tần suất của từ phổ biến nhất.

**No Note — Không chú thích**

```python
from collections import Counter
headings = ["python course","ai course","data course","python course","ai course","data course","python course","ai course","data course","python course","ai course","data course","python course","ai course","data course"]
tokens = []
for heading in headings:
    for token in heading.split():
        tokens.append(token)
counts = Counter(tokens)
most_common = counts.most_common(1)[0]
if len(headings) != 15:
    raise ValueError("Cần đủ 15 tiêu đề.")
print("Tiêu đề:", len(headings))
print("Lượt token:", len(tokens))
print("Từ khác nhau:", len(counts))
print("Từ phổ biến nhất:", most_common[0])
print("Số lượt:", most_common[1])
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Đếm tần suất từng từ trong 15 tiêu đề và tìm từ xuất hiện nhiều nhất.
# Dữ liệu: 15 tiêu đề xoay quanh python/ai/data và course; 'course' lặp ở mỗi tiêu đề.
# Counter là kiểu dictionary chuyên đếm số lần mỗi phần tử xuất hiện.
from collections import Counter
# 15 tiêu đề, không phải 15 từ riêng biệt.
headings = ["python course","ai course","data course","python course","ai course","data course","python course","ai course","data course","python course","ai course","data course","python course","ai course","data course"]
# List lưu mọi từ từ các tiêu đề, giữ lặp để tính tần suất.
tokens = []
# Duyệt từng tiêu đề.
for heading in headings:
    # split() tách token tại khoảng trắng, trả list các từ của tiêu đề.
    for token in heading.split():
        # append() lưu từng lượt token, giữ từ lặp.
        tokens.append(token)
# Counter() tạo ánh xạ từ→số lượt xuất hiện từ list có lặp.
counts = Counter(tokens)
# most_common(1) trả list một tuple (từ,số lượt) có tần suất cao nhất; [0] lấy chính tuple đó.
most_common = counts.most_common(1)[0]
# Kiểm đúng 15 tiêu đề nguồn.
if len(headings) != 15:
    # Dừng nếu thiếu tiêu đề.
    raise ValueError("Cần đủ 15 tiêu đề.")
print("Tiêu đề:", len(headings))
# Số lượt token, bao gồm trùng lặp.
print("Lượt token:", len(tokens))
# Số TỪ KHÁC NHAU được Counter lưu làm khóa.
print("Từ khác nhau:", len(counts))
# Chỉ số [0] lấy từ phổ biến nhất trong tuple; [1] là số lần xuất hiện.
print("Từ phổ biến nhất:", most_common[0])
# Đọc số lượt xuất hiện của từ được chọn.
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

**Tình huống thực tế:** Trung tâm nhận **18 phiếu hỗ trợ T01–T18**, mỗi phiếu là một mô tả ngắn **bằng tiếng Anh**, như `login password reset`; **T17 chưa có nội dung**. Khi có câu hỏi mới `login password`, nhân viên cần xếp hạng các phiếu theo **số từ chung so với toàn bộ từ khác nhau**, đề xuất **ba phiếu khớp chữ tốt nhất** và báo số phiếu thiếu nội dung, không suy diễn các phiếu cùng nguyên nhân sự cố.

**Vì sao chọn cách này?** **Jaccard** là mức giống nhau giữa **hai tập từ**: đếm từ chung và so với toàn bộ từ khác nhau của cả hai phía. Hàm `words()` đổi chuỗi thành set từ tiếng Anh chữ thường, tránh tính một từ lặp trong cùng phiếu thành nhiều lần. Hàm `similarity()` trả **0 khi hợp hai tập rỗng** để tránh chia cho 0; phiếu T17 trống vẫn được **đếm là thiếu nội dung**, không lặng lẽ xóa. Mỗi phiếu được gắn mã T01… và sắp **điểm tương đồng giảm dần, mã tăng dần khi hòa**, rồi lấy ba phiếu đầu. Giống chữ không chứng minh hai người bị cùng nguyên nhân lỗi, nên kết quả chỉ là gợi ý **rà soát**, không tự đóng phiếu.

**Quy trình:**
1. Chuẩn hóa token cho cả 18 phiếu; phiếu rỗng thành tập rỗng.
2. Tính Jaccard với hai token của truy vấn, sắp theo điểm giảm và ID tăng.
3. In ba phiếu gần nhất và số phiếu không có token.

**No Note — Không chú thích**

```python
import re
texts = ["login password reset","login password issue","reset login account","payment invoice request","refund payment card","shipment tracking delayed","delivery package status","account password change","login device blocked","payment not received","invoice missing pdf","courier lost shipment","delivery date change","reset password urgent","account verification failed","general help needed","","password login help"]
def words(text):
    return set(re.findall(r"[a-z]+", text.lower()))
def similarity(a,b):
    common = a & b
    union = a | b
    if union:
        return len(common) / len(union)
    return 0.0
query = words("login password")
ranked = []
for i, text in enumerate(texts, 1):
    ranked.append((f"T{i:02d}", similarity(query, words(text))))
ranked.sort(key=lambda row:(-row[1],row[0]))
if len(texts) != 18:
    raise ValueError("Cần đủ 18 phiếu hỗ trợ.")
print("Phiếu:", len(texts))
missing_texts = 0
for text in texts:
    if not words(text):
        missing_texts += 1
print("Thiếu nội dung:", missing_texts)
for code, value in ranked[:3]:
    print(f"{code}: {value:.3f}")
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tính Jaccard giữa từ khóa truy vấn và 18 phiếu hỗ trợ, xếp hạng ba phiếu liên quan nhất.
# Dữ liệu: 18 nội dung phiếu, có một phiếu rỗng; truy vấn 'login password' được tách thành set token.
# Regex re.findall() tìm các chuỗi chữ cái liên tiếp trong từng phiếu.
import re
# 18 phiếu, chuỗi rỗng thể hiện phiếu chưa ghi mô tả.
texts = ["login password reset","login password issue","reset login account","payment invoice request","refund payment card","shipment tracking delayed","delivery package status","account password change","login device blocked","payment not received","invoice missing pdf","courier lost shipment","delivery date change","reset password urgent","account verification failed","general help needed","","password login help"]
# Hàm nhận một câu và trả TẬP từ duy nhất sau chuẩn hóa.
def words(text):
    # lower() chuẩn hóa chữ; findall() chỉ tách từ a-z, bỏ dấu câu; set() loại từ lặp, không tách chuẩn tiếng Việt có dấu.
    return set(re.findall(r"[a-z]+", text.lower()))
# Hàm nhận hai set token và trả điểm Jaccard.
def similarity(a,b):
    # & là giao các token chung giữa hai tập.
    common = a & b
    # | là hợp chứa mọi token có ở ít nhất một tập, không trùng.
    union = a | b
    # Kiểm tập hợp KHÔNG RỖNG trước khi chia, tránh ZeroDivisionError.
    if union:
        # Jaccard = số từ chung / số từ trong hợp; từ 0 đến 1.
        return len(common) / len(union)
    # Nếu cả hai tập đều rỗng, quy ước điểm bằng 0 thay vì chia 0.
    return 0.0
# Chuẩn hóa truy vấn thành set hai từ bằng cùng hàm words().
query = words("login password")
# List lưu tuple (mã phiếu, điểm tương đồng).
ranked = []
# enumerate(...,1) đánh số phiếu từ T01 đến T18 thay vì chỉ số Python 0.
for i, text in enumerate(texts, 1):
    # Định dạng số thứ tự hai chữ số để có mã T01..T18.
    # append() thêm một tuple kết quả cho mỗi phiếu.
    ranked.append((f"T{i:02d}", similarity(query, words(text))))
# sort(key=...) ưu tiên điểm row[1] GIẢM DẦN nhờ dấu âm, nếu hòa thì mã row[0] TĂNG DẦN để ổn định.
ranked.sort(key=lambda row:(-row[1],row[0]))
# Kiểm đủ 18 phiếu ban đầu.
if len(texts) != 18:
    # Dừng nếu sai số lượng phiếu.
    raise ValueError("Cần đủ 18 phiếu hỗ trợ.")
print("Phiếu:", len(texts))
# 18 phiếu, chuỗi rỗng thể hiện phiếu chưa ghi mô tả.
missing_texts = 0
for text in texts:
    # not set đúng khi không rút được token, phát hiện chuỗi rỗng/không có từ a-z.
    if not words(text):
        # Đếm số phiếu thiếu token hữu ích.
        missing_texts += 1
print("Thiếu nội dung:", missing_texts)
# [:3] chọn ba phiếu đầu sau xếp hạng, không lấy phần tử vị trí 3.
for code, value in ranked[:3]:
    # In mã và điểm Jaccard với ba chữ số thập phân.
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

**Tình huống thực tế:** Đội chăm sóc khách hàng có **20 phiếu P01–P20**, mỗi phiếu chứa một lời nhắn tiếng Anh hoặc chuỗi rỗng; **P20 chưa nhập nội dung**. Trung tâm có ba nhóm tiếp nhận: `account` xử lý đăng nhập/mật khẩu, `billing` xử lý thanh toán và `delivery` xử lý giao hàng. Cần định tuyến từng phiếu theo **từ khóa xuất hiện**, đếm phiếu mỗi nhóm và để `unknown` cho nội dung không khớp, không tự gán phiếu chưa hiểu cho một bộ phận.

**Vì sao chọn cách này?** Đây là **bộ định tuyến dựa trên từ khóa**, không phải mô hình hiểu ngôn ngữ tự nhiên. Mỗi nhóm có một **tập từ gợi ý**, còn `tokens(text)` lấy tập từ xuất hiện trong phiếu; chương trình tính **Jaccard** giữa phiếu và từng nhóm để xem mức trùng chữ. Nếu **tất cả điểm đều bằng 0**, `route` trả `unknown`, kể cả phiếu rỗng; nếu có điểm dương bằng nhau, tên nhóm được xếp theo **thứ tự chữ cái** để kết quả ổn định. `Counter` thống kê đủ **20 lượt định tuyến**, không biến P20 thành một phiếu hợp lệ đã biết nội dung. Các từ lạ hoặc cách diễn đạt khác có thể cần người kiểm tra lại; quy tắc này không đánh giá được ý định thực của khách.

**Quy trình:**
1. Lưu đủ 20 phiếu và ba nhóm từ khóa.
2. Chuẩn hóa token, tính Jaccard giữa phiếu với từng nhóm.
3. Chọn nhóm điểm dương cao nhất, còn 0 thì unknown; tổng hợp số phiếu của từng nhóm.

**No Note — Không chú thích**

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
        if union:
            scores[name] = len(words & vocabulary) / len(union)
        else:
            scores[name] = 0
    name = sorted(scores, key=lambda n:(-scores[n], n))[0]
    if scores[name] > 0:
        return name
    return "unknown"
counts = Counter()
for text in texts:
    category = route(text)
    counts[category] += 1
if len(texts) != 20:
    raise ValueError("Cần đủ 20 phiếu cần phân tuyến.")
print("Phiếu:", len(texts))
for name in ("account","billing","delivery","unknown"):
    print(f"{name}: {counts[name]}")
empty_count = 0
for text in texts:
    if not tokens(text):
        empty_count += 1
print("Phiếu rỗng:", empty_count)
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tự động phân tuyến 20 phiếu vào account/billing/delivery bằng Jaccard từ khóa.
# Dữ liệu: 20 chuỗi phiếu, ba nhóm từ khóa; với điểm 0 cho mọi nhóm thì trả unknown.
# Dùng regex để tách token chỉ gồm ký tự a-z.
import re
# Counter đếm số phiếu được gán vào từng nhóm, mặc định khóa chưa có có số đếm 0.
from collections import Counter
# 20 phiếu; dòng rỗng sẽ có tập từ rỗng và thường được trả unknown.
texts = ["login password reset urgent","invoice payment refund request","shipment delivery tracking update","general question please","login password reset urgent","invoice payment refund request","shipment delivery tracking update","general question please","login password reset urgent","invoice payment refund request","shipment delivery tracking update","general question please","login password reset urgent","invoice payment refund request","shipment delivery tracking update","general question please","login password reset urgent","invoice payment refund request","shipment delivery tracking update",""]
# Dictionary ánh xạ tên chủ đề sang tập từ khóa duy nhất; mỗi chủ đề có vốn từ riêng.
keywords = {"account": {"login","password","reset"},
            "billing": {"invoice","payment","refund"},
            "delivery": {"shipment","delivery","tracking"}}
# Tách và chuẩn hóa chuỗi thành set từ không trùng.
def tokens(text):
    # Tìm từ chữ cái ASCII sau lower(); không tách nguyên vẹn tiếng Việt có dấu và bỏ dấu câu.
    return set(re.findall(r"[a-z]+", text.lower()))
# Hàm chọn nhãn chủ đề cho một phiếu theo mức giao từ khóa.
# Phân loại phiếu bằng hàm tính Jaccard vừa định nghĩa.
def route(text):
    # Chuẩn hóa nội dung phiếu thành set từ.
    words = tokens(text)
    # Dictionary điểm tương đồng theo từng tên chủ đề.
    scores = {}
    # items() duyệt cặp (tên nhóm, tập từ khóa) để chấm từng nhóm.
    for name,vocabulary in keywords.items():
        # | lấy hợp mọi từ của phiếu và bộ từ khóa nhóm.
        union = words | vocabulary
        # Tránh chia cho 0 khi cả phiếu và vocabulary rỗng.
        if union:
            # & là giao các từ trong phiếu trùng từ khóa chủ đề.
            # Điểm Jaccard bằng số từ chung chia tổng loại từ, không đếm lặp.
            scores[name] = len(words & vocabulary) / len(union)
        else:
            # Nếu hợp rỗng thì quy ước tương đồng 0.
            scores[name] = 0
    # Xếp nhãn theo điểm GIẢM (âm scores[n]), hòa điểm theo tên A-Z; [0] lấy tên tốt nhất.
    name = sorted(scores, key=lambda n:(-scores[n], n))[0]
    # Chỉ chấp nhận chủ đề khi có ít nhất một phần trùng, tránh tự gán phiếu không liên quan.
    if scores[name] > 0:
        return name
    # Không có từ khóa chung thì gắn unknown, không ép thuộc một nhóm bất kỳ.
    return "unknown"
# Khởi tạo bộ đếm số phiếu cho mỗi tuyến.
counts = Counter()
# Duyệt từng phiếu nguồn đúng một lần.
for text in texts:
    # Phân loại phiếu bằng hàm tính Jaccard vừa định nghĩa.
    category = route(text)
    # Tăng một lượt cho tuyến được chọn; Counter tự khởi tạo số đếm 0.
    counts[category] += 1
# Kiểm đúng hai mươi phiếu nguồn.
if len(texts) != 20:
    # Báo sai số phiếu để tránh báo cáo thiếu.
    raise ValueError("Cần đủ 20 phiếu cần phân tuyến.")
print("Phiếu:", len(texts))
for name in ("account","billing","delivery","unknown"):
    # Tra số phiếu từng tuyến, với Counter tuyến chưa gặp trả 0.
    print(f"{name}: {counts[name]}")
empty_count = 0
# Duyệt từng phiếu nguồn đúng một lần.
for text in texts:
    # Tập token rỗng đánh dấu phiếu rỗng hoặc không có từ phù hợp regex.
    if not tokens(text):
        # Đếm phiếu thiếu nội dung có thể tách token.
        empty_count += 1
print("Phiếu rỗng:", empty_count)
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

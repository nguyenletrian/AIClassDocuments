# [Mã bài] — [Tên khái niệm bằng tiếng Việt và tiếng Anh]

*[Nhóm kiến thức: Python / Data / Machine Learning / AI]*

## 1. Vị trí trong chuỗi kiến thức

```text
[Khái niệm đã biết] → [Kiến thức nền] → [BÀI NÀY] → [Ứng dụng / Bài tiếp theo]
```

[Giải thích bài này đang đứng ở đâu trong chuỗi từ dễ đến khó. Các khái niệm con cũng phải có vị trí logic. Không viết mục tiêu giảng dạy, không viết "sau bài học bạn sẽ...".]

## 2. English vocabulary — Các thuật ngữ cần biết

| English | Nghĩa ngắn gọn | Nhận biết khi dùng Python |
|---|---|---|
| ... | ... | ... |

[Đưa thuật ngữ tiếng Anh lên TRƯỚC thư viện và khái niệm. Thuật ngữ hữu ích, không cố nhồi từ khó.]

## 3. Python libraries & functions — Thư viện, API và hàm

[Cách cài thư viện (nếu có), bảng hàm với công dụng và tham số quan trọng, ví dụ ngắn có thể chạy. Giải thích `fit`, `transform`, `axis`, `shape`... trước khi bài dùng chúng.]
 
**3.x. Các tham số / keyword arguments:** [Giải thích ngay từ phần thư viện: mỗi tham số là gì, tại sao chọn giá trị này và sẽ thay đổi gì nếu đổi/bỏ. Ví dụ `dtype=float` lưu số thực, `axis=0` tính theo từng cột, `rowvar=False`, `n_components=2`, `random_state=42`... Không chỉ liệt kê tên hàm.]

## 4. Khái niệm và các kiến thức liên quan

### 4.1. [Khái niệm chính]
[Khái niệm, mục đích và khi nào dùng bằng ngôn ngữ sinh viên dễ tự đọc.]

```python
# Thể hiện phép tính hay công thức bằng Python, giải thích vì sao dùng cách này.
```

### 4.2. [Khái niệm liên quan 1 — tên tiếng Việt và tiếng Anh]
[Trước hết dùng 1–3 đoạn văn ngắn giải thích **đây là gì**, **xuất hiện ở đâu trong ví dụ đời thường**, **liên hệ với khái niệm chính thế nào**; nếu nhiều thuật ngữ thì giải thích riêng từng thuật ngữ rồi mới đưa code.]

**Nhắc lại kiến thức liên quan:** [Liệt kê và nhắc lại các khái niệm ngay trong bài này, bằng câu dễ hiểu. Nếu có Feature, Vector, Matrix thì giải thích lại chúng chứ không chỉ ghi tên. Nêu rõ mỗi hàng/cột tương ứng đối tượng/đặc trưng nào.]

**Ví dụ nhỏ từng bước trong Python:**

**Dữ liệu gồm:** [Số dòng/mẫu, tên các cột, từng cột đo gì, đơn vị đo; nêu dữ liệu giả lập hay thật. Khi minh họa 5 đối tượng: từ 5 đối tượng tạo 5 vector, ghép thành một matrix và đọc kết quả.]

```python
import numpy as np

# BƯỚC 1 — Mô tả nguồn dữ liệu và cấu trúc trước khi tạo array.
# Mỗi HÀNG = một đối tượng; các CỘT = feature kèm đơn vị đo.
# BƯỚC 2 — Tạo từng vector của đối tượng, chỉ rõ thứ tự feature.
# BƯỚC 3 — Ghép vector thành matrix (nếu phù hợp).
# BƯỚC 4 — Áp dụng hàm/khái niệm; giải thích NGAY TRÊN DÒNG GỌI HÀM
# mỗi lựa chọn như dtype=float, axis=0, n_components=2 có tác dụng gì.
# BƯỚC 5 — In shape / kết quả để kiểm tra ý nghĩa.
```

**Đọc kết quả từng bước:** [Giải thích ý nghĩa từng output, số dòng và số cột, cái gì được giữ nguyên hoặc thay đổi, điều gì KHÔNG thể suy ra].

**Trước / sau (khi có phép biến đổi dữ liệu):** [Hiển thị vài hàng của bảng gốc, vài hàng sau biến đổi và **hình kết quả thực được tính từ đúng dữ liệu minh họa** nếu hình giúp hiểu khái niệm. Ghi shape trước/sau, tỷ lệ thông tin giữ lại nếu có, tên hàng/cột, đơn vị; không dùng đồ thị tùy ý không liên quan dữ liệu.]

**Tự kiểm tra nhanh:** [Một câu ngắn kiểm tra ngay khái niệm vừa học, không cần thêm thư viện. Có **đáp án gợi ý** ngay sau đó. Mỗi nhóm kiến thức chính có một câu để người học không phải đợi tới cuối bài.]

**Quy tắc:** Trong mỗi mục 4.2, 4.3... phải nhắc lại khái niệm liên quan rồi mới bắt đầu ví dụ nhỏ **từng bước**. Khi có mảng số, phải nói rõ hàng/cột, từng đặc trưng/đơn vị và ví dụ minh họa cách ghép vector thành matrix khi cần. Không dùng chữ “Subconcept” làm tiêu đề. Viết “Khái niệm liên quan” hoặc tên chủ đề bằng tiếng Việt dễ hiểu. Không giải thích bằng cú pháp hay tên hàm trước khi nói rõ bằng văn; người học phải hiểu *feature là gì* rồi mới gặp ví dụ `np.array`. Không tạo phần “Toán học đằng sau” hoặc chứng minh hàn lâm. Mỗi công thức thể hiện bằng Python trong một ví dụ nhỏ ngay dưới đoạn giải thích.

## 5. Real-world programming problems — Khoảng năm tình huống thực tế

### Tình huống 1 — [Tên vấn đề có thực trong công việc / AI]

**Vấn đề:** [Ai đang gặp khó khăn gì, cần kết quả nào?]

**Chọn khái niệm:** [Liệt kê các khái niệm phù hợp.]

**Vì sao chọn cách này?** [Một đoạn giải thích rõ vấn đề đòi hỏi gì, tại sao phương pháp/hàm này phù hợp hơn phương án dễ nhầm khác, giả định và khi nào cách này không còn phù hợp. Chỉ liệt kê API không đủ.]

**Quy trình:** [Các bước cụ thể theo đúng thứ tự.]

**Bộ dữ liệu:** [Mỗi hàng là ai/vật gì? Mỗi cột là feature nào, đo bằng đơn vị gì? Có bao nhiêu mẫu? Là dữ liệu thật, mẫu công khai hay ví dụ giả lập?]

```python
# BƯỚC 1 — Chú thích dữ liệu: mỗi HÀNG và từng CỘT/đơn vị.
# BƯỚC 2 — Xây dựng các vector và matrix đầu vào theo thứ tự hợp lý.
# BƯỚC 3 — Chọn API, diễn giải cả các đối số (flags/options)
# chẳng hạn dtype=float (số thực), n_components=2 (hai PC)
# và nêu lý do không dùng giá trị khác.
# BƯỚC 4 — Kiểm tra shape và ý nghĩa kết quả.
```

**Kiểm tra:** [Kết quả thực tế, shape, giới hạn, điều kiện cần thận trọng.]

[Lặp lại đến tình huống 5. Chuyển hóa những bài tập đã ghi nhận trong nguồn nội bộ thành tình huống thực tiễn, không sao chép mô tả hàn lâm.]

**Tính tùy chọn của kiến thức nâng cao:** [Nếu bài tình huống cần KMeans, LogisticRegression, Pipeline hoặc API chưa được dạy trong chuỗi, đánh dấu **Phần mở rộng — có thể đọc sau**, định nghĩa chúng bằng lời ngắn gọn, chỉ yêu cầu nắm vai trò của bài hiện tại; không đột ngột biến chúng thành kiến thức tiên quyết.]

## 6. Những lỗi dễ gặp

[Những hiểu lầm hoặc sai lầm khiến sinh viên viết code sai. Đưa ví dụ Python ngắn nếu hữu ích.]

## 7. English multiple-choice questions

**Q1. [English question]?**

A. ...  
B. ...  
C. ...  
D. ...

[**Đúng 20 câu**: câu hỏi bằng tiếng Anh, 4 đáp án A/B/C/D, gồm khái niệm, tính toán bằng Python và lựa chọn giải pháp thực tiễn. Không đánh đố, câu nào cũng có đáp án đúng và giải thích.]

### Answer key & short explanations

| Question | Answer | Explanation |
|---|---|---|
| Q1 | **B** | Short English explanation. |

## 8. Nối sang bài tiếp theo

```text
[Bài trước] → [BÀI NÀY] → [Bài liên quan / bước tiếp theo]
```

[1 đoạn ngắn giúp sinh viên hệ thống hóa, không lặp mục tiêu học tập.]


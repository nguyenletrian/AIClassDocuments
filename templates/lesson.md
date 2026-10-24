# [Mã bài] — [Tên khái niệm bằng tiếng Việt và tiếng Anh]

*[Nhóm kiến thức: Python / Data / Machine Learning / AI]*

## 1. Vị trí trong chuỗi kiến thức

```text
[Khái niệm đã biết] → [Kiến thức nền] → [BÀI NÀY] → [Ứng dụng / Bài tiếp theo]
```

[Giải thích bài này đang đứng ở đâu trong chuỗi từ dễ đến khó. Các khái niệm con cũng phải có vị trí logic. Không viết mục tiêu giảng dạy, không viết "sau bài học bạn sẽ...".]

## 2. English vocabulary — Các thuật ngữ tổng quan

| English | Nghĩa ngắn gọn | Nhận biết khi dùng Python |
|---|---|---|
| ... | ... | ... |

[Bảng này chỉ là từ vựng tổng quan. **Trước mỗi mục/tiểu mục và mỗi tình huống** đều có thêm dòng **Từ vựng trong mục**: English — Tiếng Việt; chọn 2–5 thuật ngữ thực sự xuất hiện trong mục. Nhắc lại có chọn lọc, không nhồi từ khó. **Không** đặt bản dịch (tiếng Việt) sau mỗi lần dùng thuật ngữ trong câu văn.]

## 3. Python libraries & functions — Thư viện, API và hàm

[Cách cài thư viện (nếu có), **bảng nhóm theo từng hàm**: tên hàm/cú pháp → mục đích → các tham số và ý nghĩa/lý do chọn giá trị, ví dụ ngắn có thể chạy. GỘP `dtype=float` vào `np.array`, `axis=0` vào `mean`/`var`, `rowvar=False` vào `cov`, `n_components` vào `PCA`... **Không tạo chương tham số/flags riêng**. Giải thích `fit`, `transform`, `shape` trước khi sử dụng.]

## 4. Khái niệm và các kiến thức liên quan

[Lời dẫn mục 4: giải thích nội dung chính của bài bằng ví dụ đời thường, các khái niệm liên hệ với nhau thế nào.]

### 4.1. [Khái niệm chính — phải giải thích đủ nội dung tiêu đề bài]

**Từ vựng trong mục:** **English term** — Nghĩa tiếng Việt; **Another term** — Nghĩa tiếng Việt.
[Giải thích khái niệm chính theo mạch: là gì → thành phần/cách hoạt động → dùng khi nào → ví dụ nhỏ có dữ liệu cụ thể; học viên không cần mở bài cũ để hiểu. Nếu tên bài có nhiều thành phần, giải thích đầy đủ các thành phần trong mục 4.]

```python
# Thể hiện phép tính hay công thức bằng Python, giải thích vì sao dùng cách này.
```

### 4.2. [Khái niệm liên quan 1 — tên tiếng Việt và tiếng Anh]

**Từ vựng trong mục:** **Feature** — đặc trưng; **Vector** — véc-tơ; **Matrix** — ma trận.
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
# BƯỚC 4 — Áp dụng hàm đã được giới thiệu ở bảng hàm trước đó.
# Chỉ chú thích vì sao cần bước xử lý này; không lặp lại phần giải nghĩa flags.
# BƯỚC 5 — In shape / kết quả để kiểm tra ý nghĩa.
```

**Đọc kết quả từng bước:** [Giải thích ý nghĩa từng output, số dòng và số cột, cái gì được giữ nguyên hoặc thay đổi, điều gì KHÔNG thể suy ra].

**Trước / sau (khi có phép biến đổi dữ liệu):** [Hiển thị vài hàng của bảng gốc, vài hàng sau biến đổi và **hình kết quả thực được tính từ đúng dữ liệu minh họa** nếu hình giúp hiểu khái niệm. Ghi shape trước/sau, tỷ lệ thông tin giữ lại nếu có, tên hàng/cột, đơn vị; không dùng đồ thị tùy ý không liên quan dữ liệu.]

**Giải thích kết quả:** [Đọc giá trị thực in ra ngay bên dưới code, giải thích dữ liệu/đơn vị và liên hệ với khái niệm. Không có mục tự kiểm tra hoặc đáp án chen giữa bài.]

**QUAN TRỌNG:** Đọc `docs/CURRICULUM-STYLE-GUIDE.md` khi tạo mỗi bài; tuân thủ ví dụ hỏi/đáp song ngữ cùng một dòng.

**Quy tắc thuật ngữ:** Ở đầu mỗi mục, tiểu mục và tình huống có một dòng **Từ vựng trong mục:** liệt kê English — nghĩa tiếng Việt. Trong phần diễn giải sau đó chỉ dùng thuật ngữ tự nhiên, không gắn lại phần dịch trong ngoặc ở mọi lần nhắc. Tên hàm, tham số và biến trong code/backticks luôn giữ nguyên. Câu hỏi trắc nghiệm ở cuối được viết **song ngữ Anh–Việt** (câu hỏi, cả bốn phương án, đáp án và giải thích).

**Quy tắc:** Trong mỗi mục 4.2, 4.3... phải nhắc lại khái niệm liên quan rồi mới bắt đầu ví dụ nhỏ **từng bước**. Khi có mảng số, phải nói rõ hàng/cột, từng đặc trưng/đơn vị và ví dụ minh họa cách ghép vector thành matrix khi cần. Không dùng chữ “Subconcept” làm tiêu đề. Viết “Khái niệm liên quan” hoặc tên chủ đề bằng tiếng Việt dễ hiểu. Không giải thích bằng cú pháp hay tên hàm trước khi nói rõ bằng văn; người học phải hiểu *feature là gì* rồi mới gặp ví dụ `np.array`. Không tạo phần “Toán học đằng sau” hoặc chứng minh hàn lâm. Mỗi công thức thể hiện bằng Python trong một ví dụ nhỏ ngay dưới đoạn giải thích.

## 5. Real-world programming problems — Khoảng năm tình huống thực tế

### Tình huống 1 — [Tên vấn đề có thực trong công việc / AI]

**Từ vựng trong mục:** **Feature** — đặc trưng; **Dataset** — tập dữ liệu. [Thay theo nội dung mỗi tình huống.]

**Tình huống thực tế:** [Viết một đoạn độc lập: nhân vật/đơn vị có nhu cầu gì + dữ liệu đầu vào có giá trị, ý nghĩa cột/hàng/đơn vị + kết quả cần giải quyết. Ví dụ: Cửa hàng xếp VIP cho khách gắn bó từ 5 năm và chi tiêu từ 1.000.000 đồng. Khách An đã mua hàng 5 năm, chi 1.200.000 đồng. Hãy xác định khách An đủ VIP không.]

**Chọn khái niệm:** [Liệt kê các khái niệm phù hợp.]

**Vì sao chọn cách này?** [Một đoạn giải thích rõ vấn đề đòi hỏi gì, tại sao phương pháp/hàm này phù hợp hơn phương án dễ nhầm khác, giả định và khi nào cách này không còn phù hợp. Chỉ liệt kê API không đủ.]

**Quy trình:** [Các bước cụ thể theo đúng thứ tự.]

**Bộ dữ liệu:** [Mỗi hàng là ai/vật gì? Mỗi cột là feature nào, đo bằng đơn vị gì? Có bao nhiêu mẫu? Là dữ liệu thật, mẫu công khai hay ví dụ giả lập?]

```python
# BƯỚC 1 — Chú thích dữ liệu: mỗi HÀNG và từng CỘT/đơn vị.
# BƯỚC 2 — Xây dựng các vector và matrix đầu vào theo thứ tự hợp lý.
# BƯỚC 3 — Dùng API đã được giải thích kèm tham số ở phần thư viện.
# Chỉ giải thích quyết định xử lý dữ liệu, không thuyết minh lại flags.
# BƯỚC 4 — Kiểm tra shape và ý nghĩa kết quả.
```

**Kiểm tra:** [Kết quả thực tế, shape, giới hạn, điều kiện cần thận trọng.]

[Lặp lại đến tình huống 5. Chuyển hóa những bài tập đã ghi nhận trong nguồn nội bộ thành tình huống thực tiễn, không sao chép mô tả hàn lâm.]

**Tính tùy chọn của kiến thức nâng cao:** [Nếu bài tình huống cần KMeans, LogisticRegression, Pipeline hoặc API chưa được dạy trong chuỗi, đánh dấu **Phần mở rộng — có thể đọc sau**, định nghĩa chúng bằng lời ngắn gọn, chỉ yêu cầu nắm vai trò của bài hiện tại; không đột ngột biến chúng thành kiến thức tiên quyết.]

## 6. Những lỗi dễ gặp

[Những hiểu lầm hoặc sai lầm khiến sinh viên viết code sai. Đưa ví dụ Python ngắn nếu hữu ích.]

## 7. English–Vietnamese multiple-choice questions

**Q1. [English question]? — [Bản dịch tiếng Việt]?**

A. English option — Phương án A tiếng Việt

B. English option — Phương án B tiếng Việt

C. English option — Phương án C tiếng Việt

D. English option — Phương án D tiếng Việt

[**Chỉ hỏi lý thuyết và kiến thức bài học** (khái niệm, chức năng, phân biệt, cú pháp, lỗi thường gặp), **không hỏi “tình huống N/ví dụ N giải thế nào”, không hỏi nhớ số liệu/tên nhân vật của ví dụ**.]

[**Đúng 20 câu**: mỗi câu có **English question + bản dịch tiếng Việt**, **bốn lựa chọn Anh–Việt** và đáp án, giải thích **Anh–Việt**. Giữ nguyên cú pháp code, không dịch tên hàm/biến. Không đánh đố.]

### Answer key / Đáp án và giải thích song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **B** | Short English explanation. | Giải thích ngắn bằng tiếng Việt. |

## 8. Nối sang bài tiếp theo

```text
[Bài trước] → [BÀI NÀY] → [Bài liên quan / bước tiếp theo]
```

[1 đoạn ngắn giúp sinh viên hệ thống hóa, không lặp mục tiêu học tập.]


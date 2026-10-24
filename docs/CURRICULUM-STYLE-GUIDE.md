# Chuẩn biên soạn bắt buộc — Curriculum v1

**Áp dụng cho mọi bài mới và khi chỉnh bài cũ.** Mỗi lần tạo bài, agent **phải đọc tệp này và `templates/lesson.md` trước khi viết**, sau đó chạy checklist bên dưới. Không chỉ suy từ một ví dụ PCA hoặc tin rằng ghi nhớ lịch sử là đủ.

## Quy tắc biên tập tinh gọn — bắt buộc cho tất cả bài

**Nội dung dành cho sinh viên phải là kiến thức, không phải ghi chú về quy trình biên soạn.** Bỏ khỏi phần thân bài các dòng `Trạng thái: DRAFT`, `Chưa xác nhận chạy Windows`, `Dữ liệu minh họa giả lập` mang tính metadata. Trạng thái kiểm duyệt vẫn **phải tồn tại trong hồ sơ nội bộ** `sources/`, `docs/CURRICULUM-QA-STATUS.md` và kiểm thử; không được giả vờ bài đã được duyệt.

Cắt các câu hướng dẫn người viết hoặc đệm vô ích: `Các tham số được giải thích ngay cạnh hàm, không chèn quá nhiều comment vào ví dụ.`; `Không dùng thuật toán phức tạp hơn khi quy tắc đơn giản đã đủ.`; `Mỗi giá trị mang ý nghĩa và đơn vị đã nêu.`; `không phải hồ sơ thật.` nếu chỉ lặp trạng thái giả lập. Dữ liệu thực tế/giả lập cần làm rõ **một lần ở nơi có thể gây hiểu nhầm**, không lặp sau mỗi tình huống.

Cắt trạng ngữ và mở đầu nếu bỏ đi không làm thay đổi nghĩa: `Trước khi chạy ví dụ,`, `Ở bước này,`, `Như đã đề cập,`, `Chúng ta có thể thấy rằng`. Rút `Trước khi chạy ví dụ, xác định kiểu dữ liệu đầu vào` thành `Xác định kiểu dữ liệu đầu vào` **nếu phần còn lại vẫn có ích**; không xóa nguyên câu nếu nó chứa điều kiện kỹ thuật quan trọng.

Giữ bằng mọi giá: **định nghĩa, thông số kỹ thuật, điều kiện áp dụng, ý nghĩa hàng/cột/đơn vị, công thức, giải thích tại sao chọn giải pháp khi mang thông tin, kết quả thực tế, cảnh báo an toàn/bảo mật, lỗi biên, hướng dẫn kiểm chứng có tính bài học, code, câu hỏi, phương án và đáp án**. Không biến bài thành quá ngắn hoặc làm mất mạch lập luận. Ưu tiên ví dụ số cụ thể thay vì lời khuyên chung chung; gộp câu lặp nhưng không bỏ chi tiết có giá trị học tập.

Sau mỗi lần biên tập, đối chiếu số ví dụ, code, 5 tình huống, 20 câu hỏi và 80 lựa chọn trắc nghiệm Anh–Việt cùng dòng và bảng đáp án. Soát lại Markdown, liên kết hình và code block. **Không sửa nội dung trong code fence bằng quy tắc cắt chữ.**

### Giải thích khái niệm chính và khái niệm liên quan — bắt buộc

**Khái niệm chính cũng phải được giảng giải đầy đủ như khái niệm liên quan.** Đầu mục 4, viết một đoạn dẫn nêu rõ nội dung trung tâm của tiêu đề bài học, tình huống đời thường cần kiến thức ấy, và mạch kết nối các tiểu mục. Ở tiểu mục 4.1, giải thích khái niệm trung tâm theo trình tự **là gì → gồm những gì/cách hoạt động → ví dụ nhỏ có dữ liệu → code dễ đọc → kết quả in thực tế → ý nghĩa kết quả**. Với tiêu đề chứa nhiều thành phần (ví dụ `if/elif/else`), phải giải thích đủ các thành phần chính, không chỉ nói về điều kiện hay ngưỡng. Không dùng định nghĩa một câu rồi đẩy phần hiểu bài cho học viên tự suy luận.

- Mục 4 **phải định nghĩa chính nội dung ghi trong tiêu đề bài học trước**, rồi giải thích lần lượt các khái niệm nền có quan hệ trực tiếp; không biến mục này thành bảng các thuật ngữ liên quan mà bỏ trống kiến thức trung tâm.
- Mỗi tiểu mục phải là **lời giảng độc lập**: định nghĩa rõ **đây là gì**, thành phần/cấu trúc gồm những gì, **vì sao** nó liên quan đến bài, **khi nào** dùng, rồi minh họa bằng một bài toán nhỏ có số liệu. Sinh viên đọc riêng tiểu mục vẫn hiểu mà không bị buộc mở lại bài trước.
- Khi dùng vector/matrix/dataset, nói rõ **mỗi hàng đại diện điều gì**, **mỗi cột đại diện điều gì**, biến/ẩn nào ứng với cột nào, giá trị ở từng ô biểu thị gì, kích thước (shape), đơn vị (nếu có). Liên kết các ý trong **một ví dụ xuyên suốt**; không chèn câu rỗng như `Trước khi sử dụng biểu thức hãy xem phần tử, hàng/cột và đơn vị đầu vào`.
- Giải thích thuật ngữ mới **trước khi** dùng thuật ngữ đó trong công thức; nêu công thức bằng lời và đối chiếu từng thành phần với dữ liệu cụ thể. Độ sâu vừa đủ cho học viên bắt đầu học Python/AI, không lặp định nghĩa hoặc lý thuyết ngoài phạm vi bài.
- **Cấm toàn bộ mục hỏi đáp chen giữa nội dung bài** dưới các nhãn `**Tự kiểm tra:**`, `**Tự kiểm tra nhanh:**`, `**Đáp án:**` hoặc biến thể. Chỉ giữ **20 câu hỏi trắc nghiệm song ngữ ở mục 7**, với đáp án và giải thích trong bảng trả lời cuối mục.
- Kết quả code in ra vẫn phải đặt **ngay dưới khối Python** theo quy tắc trước; giải thích kết quả bằng giá trị thật, không lặp một định nghĩa chung chung.

**Mẫu giảng đúng cho hệ phương trình tuyến tính:** Có hai món hàng chưa biết giá là `x` và `y`. Một món mỗi loại giá 5 nghìn đồng: `x + y = 5`; hai món loại thứ nhất và một món loại thứ hai giá 8 nghìn đồng: `2x + y = 8`. Đây là **hệ hai phương trình tuyến tính cùng hai ẩn**. Viết thành `A @ [x, y] = b`, trong đó `A = [[1, 1], [2, 1]]`; **mỗi hàng là một giao dịch/phương trình**, **mỗi cột là số lượng của loại hàng tương ứng với ẩn x/y**; `b = [5, 8]` là tổng tiền từng giao dịch, đơn vị nghìn đồng. Giải được `x=3`, `y=2` (nghìn đồng). Có thể nối sang rank, nghiệm và sai số dư bằng **chính ví dụ này**.

### Viết đề bài thực tế thành một đoạn hoàn chỉnh

Mỗi `### Tình huống N` phải có **một dòng/đoạn `**Tình huống thực tế:**` chứa đủ bối cảnh cụ thể (ai/cơ quan nào gặp nhu cầu gì), dữ liệu/số liệu thực tế có đơn vị và **yêu cầu đầu ra/điều cần quyết định**. Không tách thành `**Vấn đề:** Xét VIP` và `**Dữ liệu:** Khách 5 năm...` vì đó không phải đề bài có thể tự hiểu. Cũng không dùng lời mơ hồ như `xử lý dữ liệu và cho biết kết quả theo yêu cầu` nếu có thể nêu rõ kết quả cần tính.

**Ví dụ đúng:** `**Tình huống thực tế:** Một cửa hàng chỉ xếp khách vào hạng VIP nếu đã gắn bó ít nhất 5 năm **và** có tổng chi tiêu từ 1.000.000 đồng. Khách An đã mua hàng được 5 năm và chi 1.200.000 đồng. Hãy viết chương trình trả về khách An có đủ điều kiện VIP không.`

**Sau đề bài:** `**Vì sao chọn cách này?**` giải thích phép toán/phương pháp phù hợp; `**Quy trình:**` nêu các bước **riêng cho tình huống** (không lặp các bước chung chung kiểu "xác định đầu vào → in kết quả" cho cả 5 bài); tiếp đến code và giải thích đầu ra cụ thể. Không lặp lại dữ liệu ở một nhãn `**Dữ liệu:**` riêng. **Giữ nguyên dữ liệu, ngưỡng và điều kiện thật trong code**, nếu không suy ra được ý nghĩa thì phải rà code, không tự đặt chính sách khác.

### Định dạng code Python dễ đọc — bắt buộc

- Mọi ví dụ Python phải đặt trong khối `python` với **mỗi lệnh trên một dòng riêng**, các khối `class`, `def`, `if/elif/else`, `for`, `while`, `try/except`, `with` xuống dòng và **thụt lề 4 dấu cách** ở thân khối. Không dùng dạng nén `def f(x): return x`, `if ok: print(...)`, hay nhiều câu lệnh ngăn bởi dấu `;` trên cùng dòng; ví dụ:

```python
class Counter:
    def __init__(self):
        self.n = 0

    def add(self):
        self.n += 1

c = Counter()
c.add()
print(c.n)
```

**Kết quả khi chạy:**

```text
1
```

- Chỉ thay đổi **trình bày code**, không tự ý thay đổi tên biến, logic, thứ tự chạy, giá trị in ra, ví dụ, hoặc xóa lời giải có ý nghĩa. Với `lambda`, biểu thức một dòng là cú pháp Python hợp lệ và được giữ nguyên.
- Xóa các dòng kết luận rập khuôn như `**Kết quả:** Chương trình thực hiện yêu cầu với dữ liệu đã cho.`; thay bằng **kết quả thật ngay dưới code** và lời giải thích cụ thể nếu có ích. Không để dòng Kết quả chung chung lặp với `Kết quả khi chạy`.

### Hiển thị kết quả ngay sau ví dụ Python

Sau **mọi** khối code minh họa, thêm dòng **`**Kết quả khi chạy:**`** và một khối `text` chứa đúng những gì chương trình in ra. Không yêu cầu người học tự chạy để mới thấy kết quả. Nếu code không in gì, ghi rõ **“Không in ra màn hình”** và nêu trạng thái cuối nếu có ích. Không tự nhận xét một giá trị được in nếu chương trình chưa `print` giá trị đó; không thêm chú thích `#` giả làm output trong code Python.

Ví dụ: `print((2, 3))` in `(2, 3)`; `print(set([1, 1, 2]))` in tập `{1, 2}`, **không** phải list `[1, 2]`. Với Set nhiều phần tử, thứ tự hiển thị không được đảm bảo; cho một kết quả mẫu và nói rõ thứ tự có thể khác. Mọi dòng kết quả phải khớp đúng với code, kể cả chữ hoa, dấu cách, dấu ngoặc, `True`/`False` và dữ liệu `None`.


### Phạm vi câu hỏi trắc nghiệm — chỉ kiểm tra kiến thức bài học

- **Cả 20 câu hỏi trong mục 7 chỉ kiểm tra khái niệm, nguyên lý hoạt động, cú pháp, hàm/tham số, sự khác biệt giữa các khái niệm, cách đọc biểu thức và lỗi thường gặp được dạy trong bài.** Ví dụ nhỏ tự chứa để đọc và dự đoán một biểu thức là được; không cần nhớ các tình huống ở mục 5.
- **Tuyệt đối không hỏi về ví dụ/tình huống đánh số**: `What solves scenario 4?`, `Which data is used in scenario 2?`, `Which reason fits example 3?`, hoặc bất kỳ câu nào tham chiếu “tình huống N”, “ví dụ N”, nhân vật, số liệu cụ thể chỉ có trong tình huống. Không kiểm tra khả năng nhớ đề bài đã đọc.
- Câu hỏi phải **độc lập**, đọc riêng vẫn hiểu, có một đáp án đúng rõ ràng và ba lựa chọn nhiễu hợp lý; ưu tiên hỏi khác nhau giữa `for` và `while`, `class` và `object`, `axis=0` và `axis=1`, `slice` và `fancy indexing`... theo đúng chủ đề bài.
- Phân bố câu hỏi đa dạng, không dùng máy móc cùng một khuôn `What does ... mean?`; bảng đáp án **giải thích vì sao đáp án đúng**, không chỉ lặp nguyên văn phương án. Mỗi câu và từng A/B/C/D đều phải có cả tiếng Anh và tiếng Việt cùng dòng.
- Trước khi merge, tìm các cụm `scenario [0-9]`, `example [0-9]`, `tình huống [0-9]`, `ví dụ [0-9]` trong **mục 7** và sửa hết; kiểm tra đủ 20 câu, 80 phương án và 20 dòng đáp án đúng thứ tự.

### Kiểm tra chất lượng trắc nghiệm theo ý nghĩa — bắt buộc trước merge

**Không chỉ kiểm tra đủ 20 câu và 80 phương án.** Với từng câu Q1–Q20, người biên tập phải đọc **nguyên văn câu hỏi Anh–Việt, cả bốn lựa chọn Anh–Việt, đáp án được đánh dấu và hai lời giải thích** rồi xác nhận:
1. **Đúng câu hỏi:** đáp án thực sự trả lời đúng điều được hỏi, không phải chỉ là một câu đúng nhưng lệch trọng tâm. Kiểm tra tính đúng của công thức, cú pháp, đơn vị, giá trị chạy Python, điều kiện áp dụng và ngữ cảnh.
2. **Duy nhất một đáp án:** ba phương án nhiễu đều sai **theo điều kiện đã nêu** nhưng có lý do hợp lý khiến người mới học dễ nhầm; không trùng ý, không có phương án nào khác cũng đúng một phần hoặc đúng trong một trường hợp chưa loại trừ. Nếu có nhiều cách hiểu, **sửa câu hỏi hoặc các phương án**, không ép một đáp án.
3. **Bản dịch tương đương:** câu hỏi và từng A/B/C/D tiếng Việt phải giữ đúng nội hàm của tiếng Anh; kiểm tra cả toán tử, dấu phủ định, từ “không”, “chỉ”, “luôn”, “xấp xỉ”, “ít nhất”, “tối đa”.
4. **Giải thích mang giá trị học:** mỗi đáp án giải thích **vì sao lựa chọn đúng**, quy tắc/định nghĩa đứng sau và ít nhất một phân biệt quan trọng hoặc ví dụ rất ngắn nếu có ích. Ưu tiên **2–3 câu cụ thể bằng mỗi ngôn ngữ**, không chỉ diễn đạt lại một câu của phương án. Khi có phép tính, trình bày các bước hoặc thay số; khi có code, giải thích điều kiện và kết quả; khi có quan hệ thống kê, nêu rõ giả định.
5. **Nhất quán thực sự:** chữ A/B/C/D trong bảng phải trỏ tới chính lựa chọn đúng của câu tương ứng. Không được chỉ dựa vào mẫu phân bố đáp án A–B–C–D; câu trả lời được xác nhận bằng nội dung. Không chỉnh phương án mà quên cập nhật bảng và giải thích.
6. **Bảng Markdown hợp lệ:** trong ô bảng, escape ký tự `|` thành `&#124;` (hoặc dạng mã tương đương) để không tách cột. Kiểm tra chính xác bốn cột, 20 hàng, 20 giải thích song ngữ.
7. **Ưu tiên kiểm chứng:** câu hỏi có kết quả mã nguồn/số cụ thể phải thực thi hoặc tự tính và so đáp án; câu còn tranh cãi/không xác minh được phải gắn trạng thái cần rà, **không khẳng định đã kiểm chứng chính xác**.

Sau chỉnh sửa, chạy kiểm tra tự động về cấu trúc và **đọc duyệt thủ công 20/20 câu về nội dung**, lưu vấn đề/sửa đổi trong phần theo dõi QA. `STRUCTURE_PASS` **không đồng nghĩa** `SEMANTIC_QA_PASS`. Không tuyên bố toàn bộ câu đúng chỉ vì không có phương án trùng hoặc đáp án đủ dòng.

## Kết cấu dành cho sinh viên
1. **Bài đang ở đâu trong chuỗi kiến thức?** Trình bày các bài trước → bài hiện tại → bài liên quan, dễ theo dõi.
2. **Từ vựng trong mục:** trước từng mục và tiểu mục, 2–5 thuật ngữ `English — tiếng Việt`; đoạn văn phía sau viết tự nhiên, **không** thêm `(Vietnamese)` sau mỗi lần nhắc. Những bảng thuật ngữ chỉ ghi từ thật sự dùng trong mục.
3. **Thư viện và hàm:** cú pháp, mục đích, các tham số được giải thích cùng hàm (`dtype=float` trong `np.array`, `axis=0` trong các phép thống kê...), không rải quá nhiều chú thích tham số khắp code.
4. **Khái niệm chính và khái niệm liên quan:** có lời dẫn về chủ đề của bài; định nghĩa khái niệm chính đầy đủ, rồi giải thích khái niệm liên quan theo cùng chuẩn: logic, dữ liệu và ví dụ nhỏ dễ hiểu → code Python → kết quả in ngay dưới code → giải thích ý nghĩa. **Không chèn tự kiểm tra/đáp án giữa bài.** Không có mục chứng minh toán học, mục tiêu dành cho giảng viên hoặc chữ “Subconcept”.
5. **5 tình huống thực tế:** gộp bối cảnh + vấn đề + số liệu + yêu cầu đầu ra thành **một đề bài có thể tự hiểu** ở `**Tình huống thực tế:**`. Sau đó trình bày vì sao chọn phép giải, các bước cụ thể, code và đầu ra. Không lặp nhãn vấn đề/dữ liệu hoặc quy trình chung.
6. **20 câu trắc nghiệm Anh–Việt chỉ về kiến thức/lý thuyết của bài, tuyệt đối không tham chiếu tình huống hoặc ví dụ đánh số**, với mỗi câu và **bản dịch trên CÙNG MỘT DÒNG**, ví dụ: `**Q1. What is a vector? — Vector là gì?**`. Mỗi phương án nằm trên **một dòng**: `A. A sequence of numbers — Một dãy số`. Đủ 4 lựa chọn cho một câu. Phần answer key là bảng 4 cột: `Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt)`. Không viết một dòng dịch tách dưới câu hỏi/phương án.
7. **Nối sang bài kế tiếp:** giải thích mối liên hệ trong chuỗi kiến thức, không ép hiểu thuật toán nâng cao trước khi học nền.
8. Hình minh họa khi có ích phải là file SVG/PNG có thật, đường dẫn tương đối **đúng chính xác** với file Markdown và kiểm tra tồn tại. Không chỉnh tên file trong quá trình dịch thuật. Nếu ảnh được tạo từ dữ liệu thì phải khớp tọa độ/số liệu.
9. **Markdown là bản gốc**. PDF sau này phát hành riêng ở `exports/pdf/`, bảo toàn bảng/hình/code/dấu tiếng Việt và được render kiểm tra trước khi công bố.

## Nguồn nội bộ, coverage và chất lượng
- Chỉ sử dụng nội dung kiến thức có căn cứ từ source code/notebook/bài tập đã đọc. **Không nhắc tên repository ghi chép trong bài dành cho sinh viên.** Nguồn từng mục, source commit và vấn đề chỉnh sửa được ghi tại `sources/` và bản đồ coverage nội bộ.
- Không sao chép nguyên ví dụ sai ở ghi chép; tái tạo tình huống đúng cú pháp và logic.
- Khi nguồn DOCX/PPTX/XLSX/binary chưa trích xuất được: ghi `SOURCE_UNREAD` trong coverage, không khẳng định đã bao phủ nội dung bên trong. Phân biệt `DRAFT`, `CODE_VERIFIED`, `EDITOR_REVIEWED`, `APPROVED`.
- Agent kiểm tra cấu trúc và syntax của từng đoạn code; chỉ công bố `CODE_VERIFIED` khi thực sự chạy và kiểm tra kết quả. Tất cả lệnh cần thư viện cài ngoài phải ghi rõ điều kiện cài đặt.
- 20 câu phải liên quan trực tiếp bài, không chèn trắc nghiệm chung chung về chủ đề khác. Đáp án đúng có giải thích kỹ thuật.

## Quy trình vận hành không phụ thuộc bộ nhớ hội thoại
Trước mỗi bài: mở `docs/CURRICULUM-STYLE-GUIDE.md` → `templates/lesson.md` → coverage ledger của nguồn → lên cấu trúc và viết → kiểm tra hình/code/20 QA → cập nhật ledger và trạng thái. Tuyệt đối không bỏ bước guide khi tác vụ được giao tự động cho worker mới.

## Về việc mở rộng toàn giáo trình
Chủ dự án **đã trực tiếp yêu cầu tạo tất cả bài còn lại ngày 2026-10-24**, không còn giữ cổng chờ phê duyệt cho việc tạo các bản thảo. Tuy nhiên, **cho phép tạo ≠ coi là đã kiểm định**: cần phân biệt bản thảo với bài được chạy unit test và review. Không tự kích hoạt Bridge hoặc restart worker chỉ vì tài liệu này được cập nhật.

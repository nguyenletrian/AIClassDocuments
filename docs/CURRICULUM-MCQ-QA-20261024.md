# Rà soát trắc nghiệm song ngữ — 24/10/2026

## Phạm vi rà soát

- Đọc và đối chiếu câu hỏi với **phương án được khoanh** ở tất cả 46 bài PY-01–PY-46: tổng 920 câu, 3.680 lựa chọn, 920 dòng đáp án.
- Soát cấu trúc bốn lựa chọn Anh–Việt/câu, đánh số, chữ cái A–D, trùng nguyên văn, tham chiếu tình huống đánh số và dấu phân cột Markdown. Đây là **QA cấu trúc**, không phải bằng chứng tự động rằng mọi lựa chọn sai về mặt ngữ nghĩa.
- Với PY-41–PY-46: viết mới 120 câu lý thuyết có đáp án liên quan trực tiếp nội dung bài; kiểm tra lại key/choices và mở rộng 120 lời giải thích thành tối thiểu hai ý bằng mỗi ngôn ngữ, nêu nguyên lý và nhầm lẫn gần.
- Với PY-01–PY-40: rà tính phù hợp của phương án được chọn với câu hỏi; những lời giải thích còn ngắn **chưa được biên tập đồng loạt thành hai ý**. Rà toàn bộ ba phương án nhiễu về ngữ nghĩa và chất lượng sư phạm vẫn cần vòng độc lập trước phát hành.

## Phát hiện và sửa chữa có bằng chứng

| Bài | Phát hiện | Khắc phục |
|---|---|---|
| PY-07 Q9 (PR #102) | Dấu `&#124;` trong bảng đáp án tạo các cột Markdown sai | Escape bằng entity `&#124;`, giải thích rõ hợp so với giao |
| PY-20 Q4 (PR QA) | Từ "independent choices" ở nguyên lý nhân đếm dễ bị hiểu nhầm là độc lập xác suất | Sửa điều kiện đếm theo số lựa chọn nối tiếp hợp lệ, nêu rõ không cần độc lập xác suất |
| PY-41 Q13 và Q19 | Cách hỏi chưa khớp chính xác với kiểu đáp án | Viết lại câu hỏi để chỉ có một cách hiểu |
| PY-42 | Biểu thức Jaccard gốc bị thiếu cú pháp/mẫu số | Sửa `len(a & b) / len(a | b)`, xử lý hợp rỗng bằng quy ước rõ |
| PY-41–46 | Giải thích đáp án quá ngắn theo chuẩn mới | Thêm phân biệt, ví dụ hoặc hệ quả riêng cho từng câu Anh–Việt |

## Những thay đổi đồng thời

Guide kiểm tra tính đúng theo nghĩa đã được merge riêng tại **PR #101**. Bản sửa bảng đáp án PY-07 Q9 đã merge tại **PR #102**. Nhánh rà soát này giữ nguyên hai kết quả trên và chỉ bổ sung bản ghi QA cùng sửa khái niệm đếm ở PY-20.

## Chuẩn duyệt trước khi phát hành

1. Không coi kiểm tra đủ số câu là đã xác nhận đáp án đúng. Mỗi câu cần người duyệt độc lập kiểm tra phát biểu, ba distractor và đáp án; câu có điều kiện thiếu phải sửa trước khi phát hành.
2. Đối với câu tính toán/output, chạy code hoặc phép tính độc lập; không đoán kết quả từ tên hàm.
3. Kiểm bảng Markdown bốn cột và kết quả Python ngay dưới mỗi khối; code cần được thử trên môi trường đích khi phát hành.
4. Các bản sửa hiện tại được thực hiện qua GitHub; **chưa phải chứng nhận QA runtime trên Windows**, và chưa phải duyệt học thuật độc lập toàn bộ 920 câu.


## Vòng QA chuyên sâu PY-01–PY-05 (24/10/2026) — đang thực hiện

- Đọc riêng mục 7 và bảng đáp án của 5 bài: 100 câu, 400 phương án. Kiểm tra tự động trên nhánh: mỗi bài vẫn có 20 Q, 80 phương án, 20 dòng đáp án đúng thứ tự, không tham chiếu tình huống/ví dụ đánh số. Đây chỉ là kiểm tra cấu trúc sau sửa, **không phải SEMANTIC_QA_PASS cho cả 100 câu**.
- **PY-01 Q18:** bỏ dấu chấm phẩy nén hai phép gán trong đề; diễn đạt theo hai dòng và giải thích giá trị ghi đè.
- **PY-02 Q17:** thay ba phương án nhiễu không cùng loại câu trả lời bằng ba nhận định về tính bất biến của chuỗi; giải thích lỗi `TypeError` khi gán chỉ số.
- **PY-03 Q11:** phương án C trước đây là “The opposite Boolean value”, cũng mô tả đúng đáp án `False`. Sửa C thành `not False` và cập nhật key **C → A**; giải thích phân biệt Boolean với số nguyên.
- **PY-04 Q13–Q16:** loại những phương án nhiễu cùng có `False` hoặc diễn đạt `False` khiến có hơn một phương án đúng, thay bằng giá trị cụ thể khác kiểu. Riêng Q15 sửa key **C → A**; Q16 key D giữ nguyên sau khi phân biệt Boolean và số nguyên.
- **PY-05 Q8:** giải thích điều kiện vòng lặp kết thúc bình thường với `else`, phân biệt `break` và `else` của `if`.
- **Chưa hoàn tất:** biên tập sâu tất cả lời giải thích còn ngắn, kiểm chứng độc lập mọi distractor trong 100 câu và chạy thử toàn bộ code. Chưa kiểm Windows; không đánh dấu cả nhóm đã duyệt học thuật. Tiếp tục mở rộng giải thích và kiểm toán ngữ nghĩa trước khi công bố.


## Vòng biên tập chiều sâu PY-01–PY-05 — 24/10/2026 (sau PR #107)

**Phạm vi thay đổi:** đúng mục 7 của 5 bài PY-01–PY-05, hồ sơ QA này và một assertion trong `tests/test_curriculum_structure.py`. Phần giảng, 5 tình huống và code fence của bài học không thay đổi so với `main` ở thời điểm bắt đầu nhánh.

### Đã thực hiện và kiểm chứng

- Đọc từng câu Q1–Q20, bốn phương án và key của 5 bài; **viết lại 100 lời giải thích bằng cả tiếng Anh và tiếng Việt**, với nguyên lý, ví dụ tính toán/cú pháp và phân biệt nhầm lẫn. Mở rộng các distractor thiếu tính cùng loại thành lựa chọn sai nhưng hợp lý; sửa PY-03 Q3 để phân biệt toán tử logic ngắn mạch `and` với phép bitwise `&`.
- Xáo trộn lựa chọn một cách xác định, cập nhật key theo **nội dung phương án đúng**, không dựa vào mẫu A–B–C–D cũ. Mỗi bài phân phối A/B/C/D đúng 5 lần, không cho học viên đoán theo vòng lặp ABCD.
- Kiểm tra từ chính nội dung ở đầu ra sau ghi GitHub: **100 câu, 400 phương án, 100 key đúng thứ tự**, đủ cấu trúc song ngữ, không có phương án trùng nguyên văn trong một câu, không hỏi nhớ tình huống/ví dụ đánh số; mọi key được đối chiếu với 100 mô tả đáp án đúng độc lập với vị trí chữ cái. **100/100 đối chiếu đạt**. Bảng Markdown key được phân tích theo bốn cột; không có dòng lỗi.
- So sánh nội dung ngoài mục 7 giữa nhánh và commit gốc của 5 bài: **không đổi**. Giữ 5 tình huống/bài, 9 code fence Python/bài và 9 nhãn `**Kết quả khi chạy:**`/bài.
- **43 kiểm chứng runtime trên Python 3.13.5**: 38 biểu thức/kiểu/giá trị, 2 trường hợp ngoại lệ (`ValueError`, `TypeError`), 2 kết quả `print()` và 1 kiểm chứng short-circuit `and`. **43/43 đạt**. Các kiểm chứng này là kiểm chứng có phạm vi, không phải thử nghiệm mọi code block hoặc chạy trên Windows.
- Phát hiện assertion `self.assertIn("*DRAFT", text)` trong test cấu trúc đi ngược quy tắc hiện hành bỏ metadata DRAFT. Thay bằng kiểm tra không còn dòng trạng thái DRAFT; thay đổi chỉ ở test, không sửa nội dung bài để làm hài lòng assertion cũ.

### Kết luận và giới hạn

- **PY-01–PY-05:** đã hoàn tất một vòng biên tập QA ngữ nghĩa do AI thực hiện, với việc đọc và sửa 100/100 câu cùng lời giải thích. Các lựa chọn đúng đã được đối chiếu độc lập với vị trí key và các biểu thức chọn lọc đã chạy thành công. **Chưa phải thẩm định học thuật độc lập bởi giảng viên**.
- **Chưa chạy Windows**; chưa chạy toàn bộ `tests/test_curriculum_structure.py` trên checkout có đủ 46 file và chưa chạy mọi code fence của giáo trình. Không gắn `WINDOWS_VERIFIED` hoặc khẳng định mọi bài đã qua kiểm thử runtime.
- **PY-06–PY-40:** cần tiếp tục vòng rà distractor chuyên sâu và mở rộng giải thích; **PY-41–PY-46:** vẫn cần xác nhận học thuật độc lập trước phát hành.


## Vòng biên tập chiều sâu PY-06–PY-10 — 24/10/2026

**Phạm vi:** năm bài List, Tuple/Set, Dictionary, Function/Lambda và OOP. Đọc và biên tập lại toàn bộ 100 câu trắc nghiệm; chỉnh cả phương án nhiễu và **100 lời giải thích Anh–Việt**. Với các câu hỏi có tiền điều kiện, làm rõ kiểu đầu vào hoặc trường hợp áp dụng: PY-06 Q3 yêu cầu `a` là List, PY-07 Q17 chọn dãy bất biến có thứ tự, PY-07 Q20 yêu cầu Set số có thể so sánh, PY-09 Q17 giả định hàm chạy đến cuối mà không thực hiện `return`, PY-10 Q6 không cần đối số bắt buộc và Q18 thuộc tính tồn tại.

### Kiểm chứng sau khi sửa

- Trực tiếp đọc lại nội dung GitHub trên nhánh QA: **100 câu, 400 phương án song ngữ, 100 dòng đáp án bốn cột** đúng thứ tự. Các lời giải thích có nguyên lý và ví dụ/so sánh; không tham chiếu tình huống hoặc ví dụ đánh số trong câu hỏi. Không có lựa chọn trùng nguyên văn trong một câu.
- **100/100** chữ cái đáp án trỏ tới chính nội dung lựa chọn đúng đã đối chiếu bằng tiêu chí từ ngữ độc lập với vị trí A/B/C/D. Trong lần đối chiếu đầu, phát hiện **5 sai lệch do hoán đổi lựa chọn trong quá trình biên tập** ở PY-08 Q20, PY-09 Q10/Q11/Q16 và PY-10 Q14; đã sửa trước merge rồi đối chiếu lại **100/100 đạt**. Không coi sự phù hợp của chữ cái theo mẫu là bằng chứng đúng học thuật.
- Mỗi bài có 5 đáp án A, 5 B, 5 C, 5 D; phá quy luật đáp án A–B–C–D tuần hoàn trước đây.
- So sánh phần trước mục 7 và sau mục 7 giữa nhánh và commit gốc: **không đổi nội dung ngoài trắc nghiệm**. Mỗi bài vẫn có 5 tình huống; số khối Python và nhãn `**Kết quả khi chạy:**` được giữ nguyên lần lượt **PY-06: 10/10, PY-07: 10/10, PY-08: 9/9, PY-09: 10/10, PY-10: 9/9**.
- **60/60 kiểm chứng runtime trên Python 3.13.5 đạt**: phép xử lý List, Set, Dictionary, Function/Lambda, OOP cùng kết quả `print`, ngoại lệ, tính bất biến và phạm vi biến. Kiểm thử này chạy trong môi trường Python hiện có, **không phải Windows** và không phải chạy mọi code fence trong cả giáo trình.

### Giới hạn và công việc tiếp theo

- Đây là một vòng đọc, biên tập và xác minh ngữ nghĩa do AI thực hiện; chưa có phản biện học thuật độc lập bởi giảng viên.
- Chưa chạy toàn bộ unit test của repository trên checkout 46 bài, chưa xác minh runtime Windows; không tuyên bố `WINDOWS_VERIFIED`.
- Tiếp tục QA theo cùng tiêu chuẩn cho **PY-11–PY-15**, rồi lần lượt đến PY-40; PY-41–PY-46 vẫn cần phê duyệt học thuật độc lập trước phát hành.


## Sửa lỗi nghiêm trọng trong bảng đáp án PY-11–PY-15 — 24/10/2026

**Vấn đề phát hiện:** Cả 100/100 hàng Q1–Q20 của 5 bài PY-11–PY-15 có định dạng `Explanation English~Giải thích tiếng Việt` trong cùng một ô của bảng Markdown, còn ô **Giải thích (Tiếng Việt)** chứa nguyên chữ `undefined`. Đây là lỗi chất lượng nội dung song ngữ, không thể được coi là đạt QA dù bảng vẫn hiển thị đủ bốn cột.

**Đã sửa:**
- Tách chính xác 100 bản dịch sẵn có về hai cột giải thích tương ứng, xóa toàn bộ `undefined` và ký tự nối `~` trong bảng answer key của PY-11–PY-15. Không tự suy diễn thêm nội dung của những giải thích chưa biên tập sâu.
- **PY-13 Q18:** bản tiếng Anh trước đó hỏi ép số nguyên sang kiểu nguyên, còn tiếng Việt hỏi số có phần lẻ; nội dung đáp án về mất phần thập phân mâu thuẫn với tiền đề tiếng Anh. Viết lại câu hỏi song ngữ với điều kiện số thực hữu hạn nằm trong miền giá trị kiểu nguyên đích, sửa A/B/C/D và lý do đáp án B. Kiểm chứng trực tiếp trong Python 3.13.5 và NumPy 2.3.5: `np.array([2.9, -2.9]).astype(int)` cho `[2, -2]` và giữ shape `(2,)`.
- Đọc lại trên nhánh: mỗi bài vẫn có **20 câu hỏi, 80 lựa chọn song ngữ, 20 dòng đáp án**; không có hàng sai 4 cột hay dấu `undefined`/`~`. Nội dung ngoài mục 7 không thay đổi.
- Quét 31 bài **PY-16–PY-46** ở `main`: mỗi bài 20 answer rows, không phát hiện kiểu hỏng `undefined`/`~` này. Đây chỉ là phép kiểm tra một dạng lỗi cụ thể, không chứng nhận 31 bài đạt QA học thuật.

**Trạng thái:** `BILINGUAL_TABLE_REPAIRED` cho PY-11–PY-15; **chưa** `SEMANTIC_QA_PASS` cho 100 câu. Phần lớn giải thích cũ vẫn ngắn, cần đọc và nâng cấp toàn bộ câu hỏi, ba nhiễu, giải thích bằng quy trình chuyên sâu; chưa có rà duyệt giảng viên, chạy full repository tests hay kiểm thử Windows.

## Bổ sung QA ngữ nghĩa PY-01–PY-05 — 24/10/2026 (sau PR #107)

- Đối chiếu lại 100 câu và bốn phương án của từng câu trên `main` đã có các thay đổi mới: các giải thích Anh–Việt đều nêu thêm quy tắc, ví dụ hoặc phân biệt; bộ lựa chọn và vị trí đáp án đã được sắp xếp lại. Không sao chép đáp án cũ theo vị trí.
- **PY-02 Q1:** thay cụm tiếng Anh `whole number` vốn dễ được hiểu chỉ là số không âm bằng diễn đạt bao gồm số nguyên âm, 0 và số nguyên dương; làm rõ `int` lưu chính xác giá trị nguyên.
- **PY-05 Q13:** câu hỏi cũ hỏi số giá trị nhưng phương án lại ghi số lượt lặp. Thống nhất cả hai ngôn ngữ thành số lượt thực thi của vòng `for` duyệt hết `range(3)`, làm rõ mốc dừng bị loại.
- **Đã kiểm tra:** không thay đổi mã Python hoặc đáp án khóa ở hai câu; mỗi bài vẫn cần đầy đủ 20 câu/80 lựa chọn/20 dòng key. **Chưa xác nhận Windows runtime** và chưa có duyệt học thuật bên thứ ba. Đây là sửa lỗi có căn cứ, không phải chứng nhận phát hành trọn bộ.

## Vòng QA chuyên sâu PY-11–PY-15 — 24/10/2026

**Phạm vi:** 100 câu và 400 lựa chọn về OOP/kế thừa, File–CSV, NumPy array, indexing và broadcasting. Đã đọc toàn bộ lựa chọn A/B/C/D và bảng khóa; viết lại **100 giải thích Anh–Việt** thành lời giải có quy tắc, ví dụ ngắn hoặc phân biệt nhầm lẫn. Đây là vòng biên tập ngữ nghĩa do AI thực hiện, không phải phản biện học thuật độc lập của giảng viên.

### Chỉnh sửa ngữ nghĩa
- **PY-11:** làm rõ quan hệ kế thừa, thứ tự phân giải phương thức khi dùng `super()`, override và cơ chế `ABC`/`@abstractmethod` (không phải mọi phương thức trong ABC đều tự trừu tượng).
- **PY-12 Q5:** UTF-8 dùng cho cả mã hóa khi ghi và giải mã khi đọc, không phải bảo mật. **Q8:** xác định `DictReader` trả chuỗi trong hàng đầy đủ; trường thiếu có thể trả `None`. **Q13:** `except ValueError:` bắt loại ngoại lệ `ValueError`, không chỉ một trường hợp chuyển đổi số.
- **PY-13:** giải thích shape/size/ndim/dtype bằng ví dụ có kích thước; phân biệt `axis=0` với `axis=1`, ép float sang int theo hướng về 0.
- **PY-14:** giải thích basic slicing thường trả view, integer-array indexing trả copy; phân biệt gán trực tiếp theo chỉ số, mask theo hàng, và cách đọc hàng/cột.
- **PY-15 Q3:** làm rõ phép `max` lấy cực đại toàn mảng khi không chỉ định trục hoặc theo trục nếu có; **Q13:** nêu rõ điều kiện dữ liệu số hữu hạn khi minh họa chặn trên bằng `np.minimum`. Bổ sung cách tương thích broadcasting và shape sau phép gộp.

### Bằng chứng kiểm tra trên nhánh QA
- Mỗi bài giữ nguyên 20 Q, 80 lựa chọn, 20 dòng khóa bốn cột; tổng **100 Q / 400 lựa chọn / 100 khóa**. Từng khóa sau xáo lựa chọn được đối chiếu với chính nội dung phương án đúng trước đó, sau đó kiểm tra lại 100 lựa chọn đúng bằng cụm đáp án kỳ vọng viết độc lập, không chỉ dựa mẫu vị trí chữ cái.
- Tất cả lựa chọn được phân bổ lại để tránh chuỗi **A–B–C–D lặp máy móc**. Mỗi bài có 5 A, 5 B, 5 C, 5 D; các đáp án mang nội dung chính xác được bảo toàn qua phép hoán vị.
- Đối chiếu phần trước mục 7 và sau mục 7: **không đổi** nội dung bài, mã Python, các tình huống thực tế, bảng dữ liệu hay phần chuyển tiếp; diff chỉ gồm 5 chương và hồ sơ QA.
- Chạy **14/14 kiểm chứng Python độc lập đạt** trên Python 3.13.5, NumPy 2.3.5 của môi trường hiện tại: CSV `DictReader` cả trường đầy đủ và thiếu, shape/size/ndim, mean/sum theo trục, ép int, mask/indexing/copy, broadcasting, `np.minimum`.
- Không xuất hiện hàng giải thích `undefined` hoặc dấu nối `~`; không có tham chiếu tình huống/ví dụ đánh số trong trắc nghiệm.

### Giới hạn
- **Chưa kiểm Windows**, chưa chạy toàn bộ repository test suite hay mọi code fence, chưa có duyệt học thuật độc lập của giảng viên. Không đánh dấu `WINDOWS_VERIFIED` hoặc xem kiểm tra cấu trúc là chứng nhận phát hành. Vòng tiếp theo: **PY-16–PY-20**.

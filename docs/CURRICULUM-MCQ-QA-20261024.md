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

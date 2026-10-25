## Chỉ đạo owner 2026-10-25 — GOAL "NO NOTE" SAU KHI CHÚ THÍCH 46/46 BÀI

**Đã được chủ dự án duyệt và chỉ kích hoạt sau goal chú thích code 10/10 hoàn tất:** `aiclassdocuments-no-note-comparison-copies-20261025`. Nguồn chính: `docs/CURRICULUM-NO-NOTE-GOAL.json` và ledger `docs/CURRICULUM-NO-NOTE-PROGRESS.json`. Trước khi chạy mỗi batch đọc lại cả hai cùng `bridgeTask.json`.

- **Tất cả ví dụ code thực thi trong PY-01..PY-46**, kể cả Python và Bash/Git, có **hai bản đặt liên tiếp**: `**No Note — Không chú thích**` rồi một fenced code không có comment diễn giải; kế đó `**Code có chú thích — Giải thích từng bước**` rồi fenced code hiện tại giữ **nguyên văn** mọi dòng/comment.
- Bản No Note phải giữ đúng lệnh, thứ tự, chuỗi, dữ liệu và stdout như bản có chú thích; dùng Python tokenizer/AST khi bỏ comment, không xóa dấu `#` trong string; với Bash tôn trọng cú pháp quote/comment. Không lặp khối kết quả `text`, hình, sơ đồ, 920 câu trắc nghiệm hay phần lời giảng.
- **Kiểm thử hiện tại giả định một fenced Python trong mỗi tình huống**: khi tăng thành hai, cập nhật test để phân biệt No Note/bản annotated, chạy code đúng và so stdout cũ, không xóa/bỏ qua test. Kiểm tính liền kề, đủ hai bản, không trùng bản thứ ba.
- Thực hiện **tối đa 5 bài một lượt**, commit riêng từng bài, một PR/batch, CI tại final PR HEAD phải SUCCESS rồi merge/ghi ledger, mới sửa revision của Bridge để nhắc batch kế. Đợt cuối chỉ PY-46. Heartbeat liên tục 15 giây là thông tin, không cho phép tạo task trùng. Không tuyên bố Windows PASS khi chưa có chứng cứ Bridge.

# AIClassDocuments — Hướng dẫn agent (PythoClass-first)

## Chỉ đạo owner 2026-10-25 — GOAL MỚI: CHÚ THÍCH CODE ĐẦY ĐỦ 46 BÀI

**Sau khi đã xuất bộ 920 MCQ PDF** và hoàn thành goal diễn giải tình huống 10/10, chủ dự án duyệt goal `aiclassdocuments-full-code-annotations-20261025` để bổ sung các dòng `#` giải thích code trên **toàn bộ PY-01–PY-46**. Trước mỗi đợt phải đọc `docs/CURRICULUM-CODE-ANNOTATION-GOAL.json`, `docs/CURRICULUM-CODE-ANNOTATION-PROGRESS.json` và mục **Quy tắc mới — owner 2026-10-25** của `docs/CURRICULUM-STYLE-GUIDE.md`.

- Mỗi khối Python cần `# Mục đích:` chính xác và các giải thích trực tiếp cạnh **mọi API, thuộc tính, tham số hoặc phép xử lý không hiển nhiên**. Không chỉ ghi một câu mục đích rồi để lại chuỗi code khó đọc. Ví dụ cần giải nghĩa riêng `matplotlib.use('Agg')` (không cần GUI, chọn trước `pyplot`), `plt.gca()` (Axes hiện tại), `.lines[0]` (đường đầu tiên), `.get_xdata()` (dãy tọa độ x), `len()` (số mốc) và `plt.close()` (đóng hình/giải phóng bộ nhớ).
- **Chỉ sửa comment Python, giữ nguyên AST chạy thật, stdout, toàn bộ 920 MCQ, giải thích tình huống và dữ liệu**. Kiểm AST tương đương từng code fence, test script/stdout, kiểm Markdown; không điền chú thích sai hoặc dài dòng vô ích.
- 10 batch tuần tự, mỗi batch tối đa 5 bài; commit mỗi bài, PR/CI cuối PASS rồi merge và cập nhật ledger. Không tự nhận Windows PASS; CDP `9224` chưa xác minh danh tính; không khởi động lại Jetking, replay task cũ hoặc gửi nhắc trùng.
- Sau batch 10/10 mới đánh dấu `COMPLETED` và vô hiệu goal review; không tự kích hoạt goal tiếp theo khi chưa được duyệt.


## Chỉ đạo mới — owner 2026-10-25 — BẮT BUỘC CHO VIỆC NÂNG CẤP 46 BÀI

**Thay thế mọi cách làm hàng loạt cũ:** Nâng cấp mục 5 của PY-01…PY-46 thành **5 tình huống khó tăng dần** (cấp 1–5 với khoảng **10, 12, 15, 18, 20 quan sát**); cập nhật **tối đa 5 bài liên tiếp mỗi đợt**, test/commit/PR/merge xong và ghi sổ rồi mới làm đợt kế. Đợt cuối PY-46 chỉ 1 bài. **Không sửa cả 46 bài trong một đợt** và không chỉ tăng dòng dữ liệu mà giữ nguyên độ khó.

**Đọc đầu tiên trước khi làm bất cứ bài nào:** [docs/BRIDGE-FIVE-LESSON-BATCHES.md](docs/BRIDGE-FIVE-LESSON-BATCHES.md) và ledger [docs/CURRICULUM-5-LESSON-PROGRESS.json](docs/CURRICULUM-5-LESSON-PROGRESS.json). Bản nháp `feat/46-lessons-scenarios-progression-20261025` có PY-01…PY-42 chưa kiểm định; **chỉ tham khảo, không merge thẳng hoặc coi là đã xong**. Trạng thái thực tế chỉ dựa trên PR merge + CI/test evidence + ledger. Khi worker chạy, Architect tiếp tục lần lượt đủ 10 đợt không cần owner hỏi lại; khi hoàn thành 46/46 phải báo một bản tổng kết. Khi blocked, giữ bằng chứng và báo blocker, không gắn nhãn PASS.

Người dùng sẽ tự mở AIBridge. Không giả định Bridge/Windows worker đang chạy chỉ vì cập nhật guide. `goal_review` được chủ dự án cho phép cho goal cụ thể này; tuân thủ giới hạn tối đa một đợt active, chống nhắc trùng/ACK nhầm, không đánh thức tác vụ Jetking cũ và tắt nhắc khi hoàn thành.

## Mục đích được chủ dự án đổi ngày 2026-10-24
Tài liệu tham chiếu **chính** là repository [nguyenletrian/PythoClass](https://github.com/nguyenletrian/PythoClass), chứa bài ghi chép, lab, scripts và notebooks của chủ dự án. Nhiệm vụ mới là **biên soạn lại thành giáo trình Python ứng dụng AI chuẩn xác và có thể thực hành**, không phải chép lại nguyên văn hay dịch khóa Jetking. Các ghi nhận Jetking cũ chỉ còn là hồ sơ lịch sử, không được tự ý tái kích hoạt.

Mọi công việc biên soạn **PHẢI đọc** [docs/CURRICULUM-STYLE-GUIDE.md](docs/CURRICULUM-STYLE-GUIDE.md) và [templates/lesson.md](templates/lesson.md) **trước khi viết bất kỳ bài nào**. Quy trình nguồn chi tiết ở [docs/PYTHOCLASS-CURRICULUM.md](docs/PYTHOCLASS-CURRICULUM.md).

## Nguyên tắc biên soạn
1. Kiểm kê nguồn tại `sources/curriculum-source-coverage.csv` (68 file trong phiên bản nguồn 24/10/2026), bóc tách mọi khái niệm **dù chỉ nhắc ngắn**. Bảng `sources/pythoclass-file-inventory.csv` chỉ là snapshot 65 file trước đó. Không công bố bao phủ toàn bộ nếu còn nguồn chưa đọc.
2. Tài liệu dành cho sinh viên đi theo thứ tự: **vị trí kiến thức → English vocabulary → thư viện/hàm Python → các khái niệm được giải thích bằng lời rồi minh họa bằng ví dụ Python nhỏ → 5 tình huống thực tế có lý do chọn phương pháp, quy trình và code → 20 câu trắc nghiệm song ngữ Anh–Việt với lựa chọn và giải thích → bài tiếp theo**. Các từ như Feature/Vector/Matrix phải được định nghĩa riêng bằng ngôn ngữ phổ thông trước khi xuất hiện trong phép tính; không dùng nhãn tiêu đề “Subconcept”, không có mục tiêu học tập/chứng minh toán học hoặc ngôn ngữ giáo án.
3. Dùng tiếng Việt rõ ràng; có bảng thuật ngữ tiếng Anh đặt trước thư viện và khái niệm. Mỗi bài phải có sơ đồ chuỗi kiến thức (ví dụ Vector → Matrix → Features → PCA → ML) để sinh viên biết nội dung đang ở đâu trong hệ thống.
3a. Ở mỗi mục khái niệm liên quan (4.2, 4.3...), **nhắc lại bằng lời khái niệm xuất hiện trong mục**, rồi trình bày **một ví dụ nhỏ tăng tiến từng bước**: đối tượng → vector → matrix → phép xử lý → đọc kết quả. Bất cứ khối dữ liệu nào cũng phải chú thích: số hàng, **mỗi hàng biểu diễn ai/cái gì**, tên & ý nghĩa từng cột, đơn vị đo, nguồn dữ liệu (giả lập/công khai). Không đưa array số trần mà thiếu nghĩa dữ liệu. Mỗi code block gắn bước và lý do chọn thao tác.
3b. Thiết kế cho sinh viên năng lực học bình thường: **giải thích trực quan và đặt đầu ra ngay sau code; không chèn mục tự kiểm tra/đáp án ở tiểu mục (20 MCQ chỉ nằm ở mục 7)**; khái niệm trừu tượng như Eigenvector cần **ẩn dụ/thí dụ đời thường trước code**. Với phép biến đổi như PCA/scale/clustering, hiển thị dữ liệu **trước và sau**, tọa độ thật và hình trực quan khớp chính dữ liệu/thuật toán đã chạy (không dùng minh họa vô căn cứ). Đánh dấu rõ **phần mở rộng — có thể đọc sau** cho API/thuật toán vượt quá kiến thức tiên quyết. Duy trì 20 câu hỏi trắc nghiệm song ngữ Anh–Việt cuối bài; tự kiểm tra ngắn không thay thế trắc nghiệm.
3c. **Gộp đối số/flags vào từng hàm ở phần thư viện**: giải thích `dtype=float` bên cạnh `np.array`, `axis=0` bên cạnh `mean`, `rowvar=False` bên cạnh `np.cov`, `n_components` bên cạnh `PCA`... nêu tham số có nghĩa gì, vì sao chọn và hệ quả nếu đổi. **KHÔNG tạo một bảng tham số chung tách khỏi hàm.** Trong code demo chỉ chú thích nguồn dữ liệu, số hàng/cột, mục đích và lý do thực hiện từng bước; tránh lặp lại ý nghĩa cờ ở từng dòng. Giữ code minh họa ngắn, có cấu trúc.
3e. **Đề bài tình huống tự đủ nghĩa:** Trước code, đặt `**Tình huống thực tế:**` với **bối cảnh + số liệu + câu hỏi/yêu cầu đầu ra** trong cùng đoạn; không tách `**Vấn đề:**` và `**Dữ liệu:**`. Sau đó mới giải thích lý do chọn phép tính và quy trình riêng. Xem ví dụ VIP ở guide. Không thêm câu lặp chung chung.
3d. **Bảng thuật ngữ gọn trước mỗi mục:** Trước **mỗi mục, tiểu mục và tình huống** có một dòng `Từ vựng trong mục:` dạng `Eigenvector — vector riêng; Eigenvalue — giá trị riêng`. Sau đó dùng thuật ngữ tự nhiên trong văn bản, **không gắn nghĩa tiếng Việt trong ngoặc sau từng lần nhắc**. Giữ nguyên định danh Python và đường dẫn Markdown/ảnh. Cấm tự động thay thế từ khóa bên trong `](path)`, đường dẫn ảnh hoặc code. Trắc nghiệm **20 câu song ngữ Anh–Việt**, dịch cả câu hỏi, bốn lựa chọn và giải thích đáp án.
4. Truy nguyên `GHI CHÉP GỐC`, `ĐÃ HIỆU ĐÍNH`, `AI MỞ RỘNG` **chỉ ở hồ sơ nội bộ** `sources/`/docs, KHÔNG trong bài dành cho sinh viên. Không nhắc tên repo PythoClass/PythonClass, đường dẫn ghi chép hoặc quá trình biên soạn trong `lessons/`. Không truyền lại công thức hoặc code sai; thử cú pháp, test giá trị, tránh dữ liệu rò rỉ trong ML.
5. Không sửa repository PythoClass. Không lưu secret, output chứa thông tin cá nhân hoặc nguồn bị hạn chế quyền sử dụng lên GitHub.
6. Không yêu cầu chủ dự án thủ công gửi ảnh/chép notes khi nguồn đã có thể đọc qua GitHub và công cụ được phép. Tự kiểm tra file binary bằng công cụ phù hợp, báo cáo chính xác blocker nếu không đọc được.
7. **Đã có lệnh chủ dự án 2026-10-24 triển khai toàn bộ chương trình**. Cho phép soạn các bài còn lại theo style guide. Riêng goal nâng cấp 46 bài ngày 25/10, cho phép `goal_review.enabled=true` khi owner mở Bridge, với chống lặp và giới hạn đúng một đợt 5 bài. Không đổi ACK/tác vụ cũ. Bài mới mang trạng thái `DRAFT` tới khi test thật.

## Tiêu chí sẵn sàng
Đã có 46 bài DRAFT trong `lessons/chapters/` và một bài PCA tham chiếu, được chủ dự án cho phép biên soạn. Chỉ nâng bài sang `CODE_VERIFIED` khi chạy code/test có bằng chứng, sang `EDITOR_REVIEWED` khi rà chuẩn mực, nguồn và trắc nghiệm. Xem `docs/CURRICULUM-QA-STATUS.md`; không đồng nhất việc có bài với đã hoàn thành mọi khái niệm nguồn.

## Hệ thống Bridge
AIBridge giữ worker identity, queue/ACK và các quyền task theo cơ chế cũ. Đổi mục tiêu tài liệu **không** là giấy phép để restart, gửi idle reminders lặp lại, replay ambiguous sends, tự tạo New Chat hay chạy lại các task Jetking. Khi cần đọc/tạo tài liệu từ PythoClass, ưu tiên GitHub; chỉ tạo các task Bridge giới hạn nhiệm vụ thật và có thể kiểm chứng.

## Kiểm tra log AIBridge theo yêu cầu

Khi owner nói `kiểm tra log`, `xem log Bridge` hoặc `chẩn đoán lỗi Bridge`,
thực hiện trực tiếp workflow trong `docs/ON_DEMAND_BRIDGE_LOG_REVIEW.md`:
fetch TaskSource chính thức → append đúng một task `runtime:read_log`
(`review_mode=on_demand`, `ack_policy=architect_review`,
`return_route=provider:OpenAI/web`) → đợi Bridge gửi log thật →
phân tích lỗi có chứng cứ → ACK chính task đó trong Git.

Không yêu cầu owner copy log VS Code nếu worker đang hoạt động.
Không tự đặt `auto_success` cho log; không biến đọc log thành
tín hiệu tiến độ bài Jetking; không đánh thức lại goal đang tạm dừng;
không đặt lịch định kỳ hoặc tạo task lặp vì chưa thấy kết quả.
Nếu chưa có `task_result`, nói rõ chưa nhận được log thực tế.

## Test script dùng chung AIBridge

Khi cần chạy unittest từ Bridge, ưu tiên route dùng chung
`verification:test_script` trong AIBridge, thay vì sao chép một
test runner riêng vào dự án. Hợp đồng tham khảo:
`nguyenletrian/AIBridge/docs/TEST_SCRIPT_CAPABILITY.md`.

- Test bộ chẩn đoán AIBridge đã đóng gói:
  `payload.suite=bridge_diagnostics`, không cần `project.workdir`.
- Test code AIClassDocuments hoặc dự án khác:
  `payload.suite=project_unittest`,
  `payload.pattern=test_<name>.py`; cần `project.workdir` cục bộ
  rõ ràng và file có sẵn trong `tests/`.
- Mọi task đều phải khai báo `permissions.run_tests=true`,
  `ack_policy=architect_review`, route trả kết quả về Architect.
  Việc chạy Python test là thực thi code đáng tin cậy, không phải sandbox.
- PASS của GitHub CI không thay thế PASS từ Windows worker.
  Sau khi nhận đúng `task_result`, Architect review và ACK.
- Route kiểm thử **không dùng thay** `runtime:read_log` để
  thu thập dữ liệu log runtime và không được tự truy cập tài khoản/nguồn học.

## Git
- Đặt bài giảng ở `lessons/chapters/PY-<nn>-<slug>.vi.md` và cập nhật `lessons/chapters/README.md` theo chuỗi tiên quyết.
- Không commit credential, session hoặc thông tin cá nhân.
- Commit nhỏ, mô tả được công việc; không overwrite công việc người dùng.
- Repo và Bridge là các thành phần riêng: cấu hình máy, endpoint và secret đặt ngoài repo.

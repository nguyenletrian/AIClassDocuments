# AIClassDocuments — Bridge guide: mỗi lần chỉ cập nhật 5 bài

> **Owner-approved goal (25/10/2026):** Nâng cấp **mục 5 — năm tình huống thực tế** trong **46 bài PY-01…PY-46**, sao cho tình huống 1→5 tăng độ khó thật sự, với dữ liệu minh họa khoảng **10–20 bản ghi**. **Mỗi lần cập nhật tối đa 5 bài học liên tiếp**. Xong từng đợt thì kiểm tra, commit/merge, ghi tiến độ; làm tiếp đợt kế tiếp không cần owner nhắc. Khi đủ 46/46 và có bằng chứng kiểm định, Architect thông báo owner.

## 1. Điểm bắt đầu có thật

- Đích: repository `nguyenletrian/AIClassDocuments`, nhánh chính `main`, 46 bài `lessons/chapters/PY-*.vi.md`. Không sửa `nguyenletrian/PythoClass` (repo nguồn private).
- Nhánh **tham khảo chưa kiểm định**: `feat/46-lessons-scenarios-progression-20261025`. Có bản nháp **PY-01…PY-42** và chưa có PY-43…PY-46. **Không merge nhánh này trực tiếp hoặc coi bất cứ bài nào trên đó đã hoàn thành**. Chỉ đọc/chọn ý hữu ích sau khi kiểm tra nội dung, đầu ra và code; ưu tiên biên tập lại trường hợp máy móc hoặc lỗi.
- Tình trạng hoàn thành nhiệm vụ **khi guide ra đời**: **0/46 bài được xác nhận nâng cấp + merge theo quy trình mới**. Nội dung cũ ở `main` vẫn tồn tại, nhưng không có nghĩa đạt yêu cầu độ khó tăng dần.
- Sổ cái bền vững: `docs/CURRICULUM-5-LESSON-PROGRESS.json`. **Đây là nguồn xác định đợt tiếp theo**, không lấy trí nhớ chat, số tin nhắn hay tên nhánh làm trạng thái đã xong.
- Quy tắc chi tiết hiện hành: `AGENTS.md`, `docs/CURRICULUM-STYLE-GUIDE.md`, `templates/lesson.md`, `docs/PYTHOCLASS-CURRICULUM.md` và `tests/test_curriculum_structure.py`. Nếu mẫu cũ mâu thuẫn về mục 5/trắc nghiệm, ưu tiên style guide đã cập nhật và quy định mới ở tài liệu này.

## 2. Mười đợt cố định, không vượt ranh giới

| Đợt | Bài được phép sửa trong đợt | Số bài |
|---|---|---:|
| 01 | PY-01 → PY-05 | 5 |
| 02 | PY-06 → PY-10 | 5 |
| 03 | PY-11 → PY-15 | 5 |
| 04 | PY-16 → PY-20 | 5 |
| 05 | PY-21 → PY-25 | 5 |
| 06 | PY-26 → PY-30 | 5 |
| 07 | PY-31 → PY-35 | 5 |
| 08 | PY-36 → PY-40 | 5 |
| 09 | PY-41 → PY-45 | 5 |
| 10 | PY-46 | 1 |

**Chỉ chạy một đợt tại một thời điểm.** Không tạo 10 PR song song, không sửa/merge bài của đợt tiếp theo khi đợt hiện tại đang PENDING/IN_PROGRESS/FAILED/BLOCKED. Một đợt được công nhận `MERGED` sau khi **đúng các bài trong đợt** đã qua kiểm tra có chứng cứ, PR đã merge vào `main` và ledger được cập nhật với PR, commit, test evidence. Nếu lỡ đứt kết nối, đọc ledger và trạng thái PR/commit trước, tiếp tục đúng bài chưa hoàn tất. Không chạy lại bài đã merge chỉ vì task cũ gửi lại.

## 3. Yêu cầu biên tập: 5 tình huống tăng độ khó thật

Cả 5 tình huống của mỗi bài đều **đúng trọng tâm bài học**, có một đoạn `**Tình huống thực tế:**` nêu đủ người dùng/bối cảnh, số liệu có ý nghĩa và **câu hỏi đầu ra**. Có `**Từ vựng trong mục:**`, `**Vì sao chọn cách này?**`, `**Quy trình:**`, code, **đầu ra có thể đối chiếu** và giải thích số liệu/đơn vị. Mỗi tình huống có dữ liệu thực hành đủ **10, 12, 15, 18, 20 bản ghi** tương ứng mức 1–5, trừ trường hợp cấu trúc toán học buộc dùng số chiều nhỏ: vẫn tạo 10–20 **quan sát/lượt thử** để phân tích (không tạo ma trận 20×20 chỉ để làm đầy số liệu). Nói rõ **một bản ghi là ai/cái gì**, tên & đơn vị các cột; khi dữ liệu giả lập, ghi nhận ở ngữ cảnh phù hợp một lần.

| Cấp | Yêu cầu khác nhau về tư duy, không chỉ số dòng |
|---|---|
| **1 — Nền tảng** | Nhận diện bài toán, dùng **một** phép toán/hàm/khái niệm chính, đọc kết quả. 10 bản ghi để luyện quan sát; không dùng API chưa học. |
| **2 — Vận dụng** | Cùng chủ đề nhưng xử lý **toàn bộ 12 bản ghi**, lọc/tổng hợp hoặc lặp đúng cách, đọc nhiều kết quả. |
| **3 — Phối hợp** | **15 bản ghi**, kết hợp **ít nhất hai thao tác/tiêu chí/đặc trưng** để giải nhu cầu thực tế; có kiểm chứng trung gian. |
| **4 — Ngoại lệ** | **18 bản ghi** có dữ liệu thiếu/trùng/ngoại lệ/điều kiện biên **phù hợp bài học**. Giải thích và xử lý có chủ đích, không im lặng đổi `None` thành 0. |
| **5 — Tổng hợp** | **20 bản ghi**, giải một **quy trình hoàn chỉnh** từ đầu vào → kiểm tra → xử lý → kết quả/báo cáo/so sánh. Đối chiếu kết quả, hạn chế, chọn phương pháp phù hợp. |

**Cấm nâng cấp hình thức:** chỉ đổi nhãn “Cấp 1…5”, tăng từ `range(10)` lên `range(20)` mà không nâng yêu cầu; dùng một khối code chung giống hệt cả năm tình huống; viết 5 lời giải đều chỉ `sum()/mean()/filter()` bất kể chủ đề; bổ sung bản ghi chung chung không liên quan thực tế; cố nhồi nhiều phương pháp nâng cao vào cấp 1; in `result` mà không đọc kết quả; chèn phụ lục “Bài nâng cấp” bên dưới tình huống cũ nhưng **đề/chương trình chính vẫn quá dễ**. **Thay thế/tái cấu trúc tình huống thành một bài hoàn chỉnh**; giữ phần khái niệm, thứ tự bài và trắc nghiệm nguyên vẹn trừ khi có lỗi độc lập được kiểm chứng.

Đầu ra minh họa phải khớp code thực tế, tránh hardcode kết quả. Các bài toán khó có thể dùng đồ thị được tạo từ chính dữ liệu hiện có; giải thích các trục và đơn vị. Cấp 4 không cần cố tạo `NaN` cho bài Git; thay bằng lỗi phù hợp chủ đề: commit nhầm file, conflict, file chưa stage. Cấp 5 của phần ML phải so mô hình đúng cùng split, tránh leakage; bài xác suất dùng mô phỏng đối chiếu lý thuyết; thống kê nói rõ mẫu nhỏ chỉ minh họa.

## 4. Pipeline chuẩn của một đợt 5 bài

1. **Khởi động/khôi phục:** Xác minh worker `AIClassDocuments-architect`, repo, `main` SHA, task/ACK đang chờ, `goal_review`, ledger và PR đang mở. Không chạy lại task chưa ACK, không đoán kết quả pending. Nếu task đang `RESULT_PENDING`, xem log/result thật, ACK đúng task sau khi review.
2. **Chỉ chọn đợt đầu tiên chưa MERGED** theo ledger, tối đa 5 bài. Nếu `IN_PROGRESS`, khôi phục nhánh/PR đã ghi; nếu `BLOCKED`, kiểm tra lại chứng cứ rồi quyết định có thể tiếp tục hay cần báo blocker, không nhảy sang đợt khác.
3. **Trước mỗi bài:** Đọc toàn bộ bài từ `main`, style guide, template và nguồn/coverage liên quan. Đọc bản nháp chưa kiểm định nếu giúp tiết kiệm thời gian nhưng kiểm chứng lại từng phép tính, mô tả và phụ thuộc.
4. **Sửa một bài:** Chỉnh mục 5 để năm tình huống đúng các cấp; đảm bảo tình huống là đề trọn vẹn, code chạy độc lập và có đầu ra đúng. **Không sửa mục 1–4, 6–8 hoặc 20 MCQ** trừ khi phát hiện lỗi và ghi lý do cụ thể. Commit riêng cho từng bài (vd. `feat(PY-01): progressive scenarios 10–20 records`); hoàn tất bài nào lưu SHA ngay bài đó, tránh mất tiến độ.
5. **Kiểm thử trước PR:** Chạy `python -m unittest tests.test_curriculum_structure -v` cùng kiểm tra riêng 5 bài (đúng 5 đầu mục, 20 câu song ngữ + 80 phương án + 20 đáp án, cú pháp code fence, dữ liệu 10/12/15/18/20, tính đúng của output, thiếu/lỗi biên). Nếu thêm code block mục 5, **cập nhật bài kiểm tra đếm block** có lý do thay vì cố giữ số code block cũ; không làm suy yếu kiểm tra MCQ.
6. **Chạy code thật:** Ưu tiên test tự động từng code block mới và đối chiếu output; Python 3.12 trên CI; với máy chủ owner, dùng Bridge route `verification:test_script` (suite `project_unittest`, giới hạn file `tests/test_*.py`, `permissions.run_tests=true`), sau khi biết đúng `project.workdir`. Windows PASS **chỉ** khi nhận kết quả từ đúng worker có evidence; không tự nhận GitHub CI PASS thay cho Windows. Nếu thiếu runner, có thể giữ DRAFT + CI evidence, không gắn nhãn CODE_VERIFIED/Windows PASS.
7. **Một PR cho đúng đợt:** Đăng PR vào `main`, chỉ chứa thay đổi 1–5 bài của đợt + tests/ledger cần thiết. Phải chờ CI và review kết quả thật; nếu lỗi sửa trên nhánh cùng PR, không phát hành đợt tiếp. Merge an toàn và xác minh commit trong `main`. Không force-push `main` hay sửa code ngoài phạm vi.
8. **Ghi sổ rồi đi tiếp:** Cập nhật ledger trạng thái `MERGED` với số PR, commit SHA, bằng chứng kiểm thử, 5 bài và thời điểm; commit lên `main` (có thể ngay trong PR nếu biết trước rồi bổ sung SHA merge sau). **Phải xác minh cập nhật ledger bền vững trước khi bắt đầu đợt kế tiếp.** Nếu quá trình cập nhật ledger đứt kết nối sau merge, reconcile từ GitHub PR để tránh merge lại.
9. **Lặp đến đợt 10**. Sau 46 bài, rà lại toàn bộ chương trình, yêu cầu mọi đợt `MERGED`, đủ 230 tình huống, kiểm tra trắc nghiệm vẫn 920 câu, chạy test cuối. Đặt `goal_review.status=completed`, `goal_review.enabled=false`, bật lại `owner_pause.suppress_idle_reminders=true` và **gửi đúng một báo cáo tổng kết** cho owner, gồm PR/bằng chứng, lỗi còn mở và những phần chưa có Windows verification.

## 5. Bridge/Architect phối hợp, không spam

- Chủ dự án đã duyệt **goal nâng cấp 46 bài**; người dùng sẽ tự mở Bridge. Bridge chỉ kích hoạt khi runtime/worker thực sự chạy; guide cập nhật **không chứng minh runtime đã bật**.
- Architect chịu trách nhiệm lập nội dung, commit/PR, kiểm tra, ACK; Bridge là kênh chuyển task/kết quả và Windows testing theo quyền. **Không tạo task chung chung yêu cầu Bridge biên soạn bài nếu action chưa được Bridge hỗ trợ**; dùng Architect xử lý GitHub và gửi task test `verification:test_script` hợp lệ khi cần.
- Không gửi 10 task cùng lúc; tối đa **một đợt nội dung đang active** và mỗi task test phải có `task_id` duy nhất. Mọi `RESULT_PENDING` phải được kiểm tra thay vì chờ vô hạn hoặc gửi lại vô điều kiện.
- Sau mỗi kết quả task, rà bằng chứng rồi ACK đúng task, cập nhật ledger/PR, tự tiếp tục việc còn sẵn. Không tạo New Chat chưa cần; tôn trọng ngưỡng, conversation registry và worker ownership của AIBridge; không tự restart Bridge chỉ vì hướng dẫn mới.
- `goal_review.enabled=true` cho goal này cho phép Bridge nhắc Architect làm việc khi đang idle; nhắc không phải bằng chứng đã làm xong. Phải chặn nhắc trùng khi có task đang chạy, PR chưa merge hoặc `RESULT_PENDING`. Nếu không có thay đổi mới, giữ yên, không gửi lặp thông báo owner. `goal_review.enabled` về `false` khi hoàn tất hoặc bị blocker không thể tiếp tục.
- Khi có lỗi kết nối, đọc `docs/CURRICULUM-5-LESSON-PROGRESS.json` + GitHub `main`, PR và trạng thái task trước khi sửa. Không dựa trên lịch sử hội thoại. Không đụng lại các 18 task Jetking/Bridge lịch sử đã ACK; Jetking vẫn nằm trong lịch sử, không kích hoạt lại.
- Nếu phát hiện secret/PII từ `PythoClass` (private), giữ dữ liệu nguồn ở repo private; code minh họa của 46 bài ở repo public phải dùng dữ liệu giả lập hoặc tài liệu được phép.

## 6. Điều kiện báo hoàn thành

Chỉ thông báo **46/46 hoàn thành** sau khi 10 đợt đã `MERGED` thật vào `main`, ledger đầy đủ, kiểm tra 46 bài có 5 cấp tăng độ khó và dữ liệu 10–20 hàng/lượt, không làm sai câu hỏi trắc nghiệm và không còn test chặn. Ghi rõ CI/Windows nào có chứng cứ, chưa có thì nói chưa xác minh. Nếu một đợt `BLOCKED`, không báo “xong” và không bỏ qua bài.

**Mẫu kết quả ngắn sau mỗi đợt trong kênh Bridge/Architect:** `PY-01…PY-05 | 5/5 | PR #... merged <sha> | CI PASS <run> | Windows PASS/UNVERIFIED | next PY-06…PY-10`. Chỉ gửi **owner** một báo cáo tổng kết ở cuối, trừ khi có lỗi cần quyết định của owner.


## 7. Goal kế tiếp đã duyệt — diễn đạt tình huống dễ hiểu (CHƯA ĐƯỢC KÍCH HOẠT)

**Nguồn quyền:** chủ dự án duyệt ngày 25/10/2026. **Thứ tự bắt buộc:** hoàn tất goal hiện tại *Python tường minh* (PY-01…PY-46, 10/10 batch đã MERGED, ledger \`docs/CURRICULUM-EXPLICIT-PYTHON-PROGRESS.json\` \`COMPLETED\`, không còn PR/task chưa xử lý) **trước** khi kích hoạt goal này. Đặc tả lưu ở \`docs/CURRICULUM-SCENARIO-CLARITY-GOAL.json\` với trạng thái \`APPROVED_DEFERRED\`; không sửa ngay nội dung tình huống trong batch của goal hiện tại.

Khi tới lượt goal này, xử lý theo **10 đợt tối đa 5 bài** và quy trình commit → test từng code fence/đối chiếu stdout → CI → PR merge → ghi ledger → sang đợt tiếp. Với **mỗi** tình huống:

- **Tình huống thực tế:** nêu ai/cái gì cần giải quyết, bối cảnh và ý nghĩa từng dữ liệu (mỗi hàng, đơn vị, nguồn/gỉa định), câu hỏi người học cần trả lời. Viết ngắn gọn, dễ hình dung như chuyện thật; nếu từ chuyên ngành chưa học xuất hiện, giải nghĩa bình dân ngay tại đây. Không đưa yêu cầu kỹ thuật như seed, số vòng mô phỏng, thuật toán cài đặt hoặc lời bác bỏ cách giải vào đoạn nêu vấn đề nếu không thiết yếu.
- **Vì sao chọn cách này?:** giải thích **đúng thuật ngữ, nguồn gốc con số**, tại sao cần phương pháp và các bước nghĩ/diễn giải nó theo lời nói, lý do tránh cách ngây thơ cho kết quả sai, cách đọc kết quả và hạn chế. Khi có tham số \`5000\` lượt/seed \`42\`, nói đây là giá trị minh họa: nhiều lượt thường làm tỷ lệ mô phỏng ổn định hơn nhưng tốn thêm thời gian, seed cố định giúp tái lập chứ không bảo đảm trùng xác suất lý thuyết. Không giấu giải thích ấy trong câu tình huống.
- **Ví dụ về trọng số/xác suất:** 20 trạng thái S01…S20 được **người soạn giả định** mức ảnh hưởng 1…20 để thử mô hình; **trọng số không phải số lần xuất hiện**. Chuẩn hóa nghĩa là cộng 20 mức (=210), rồi lấy từng mức chia cho 210 để chúng cộng thành 100%; tổng mức của S16…S20 là 90 nên khả năng gộp là 90/210 ≈ 42,86%, **không phải 5/20=25%** do các trạng thái không đồng khả năng. Nếu muốn đo xác suất máy thật, cần giải thích cách ghi nhận dữ liệu và xác thực giả định.
- Các định nghĩa không nhồi công thức; nói rõ dùng để làm gì, vì sao xuất hiện và được tính/thiết lập bằng cách nào. 5 tình huống vẫn tăng độ khó, giữ đúng số bản ghi có ý nghĩa 10/12/15/18/20, không đổi kiến thức chính, mã ví dụ, stdout, 20 MCQ/bài hay đáp án nếu chưa có lý do và kiểm chứng độc lập.

**Ranh giới nhiệm vụ:** mục 7 là yêu cầu đã duyệt nhưng **chưa thực thi**. Không tạo task/PR nội dung cho goal này trong khi goal Python tường minh còn ACTIVE, ngay cả khi heartbeat liên tục nhắc.

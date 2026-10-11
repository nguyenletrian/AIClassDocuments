# AIClassDocuments

Dự án biên soạn **tài liệu học tập tiếng Việt** từ các bài học mà chủ dự án có quyền truy cập và cung cấp, bắt đầu với khóa Jetking VN Course.

## Mục tiêu
- Diễn giải nội dung bài giảng rõ ràng, chính xác, có ví dụ và bài tập ứng dụng.
- Giữ thuật ngữ chuyên môn tiếng Anh bên cạnh giải thích tiếng Việt.
- Quản lý nguồn, phiên bản và lịch sử cập nhật bằng Git.
- Bản chính ở Markdown; có thể xuất DOCX/PDF khi cần.

## Bài học nguồn đầu tiên
- Course: https://www.jetking.co/learn/home/VN-course?lessonId=4371618
- Lesson ID: `4371618`
- Trạng thái: **AWAITING_SOURCE** — chưa truy cập được nội dung thực tế. Không tự sáng tác nội dung bài học.

## Cấu trúc
- `AGENTS.md`: quy tắc dành cho AI agent và review.
- `docs/WORKFLOW.md`: quy trình từ dữ liệu nguồn đến tài liệu đã kiểm định.
- `templates/lesson.md`: mẫu tài liệu tiếng Việt.
- `sources/lesson-index.csv`: sổ theo dõi bài học, đường dẫn và trạng thái.
- `lessons/`: tài liệu Markdown đã biên soạn.

## Làm việc trong VS Code
```powershell
git clone https://github.com/nguyenletrian/AIClassDocuments.git
cd AIClassDocuments
code .
```

Nếu đã có thư mục cùng tên chứa code/tài liệu, hãy kiểm tra `git status` trước khi clone/checkout, tránh ghi đè file.

## Nguyên tắc nguồn
Chỉ dùng văn bản bài học, bản ghi (transcript), ảnh hoặc ghi chú được phép sử dụng. Không vượt đăng nhập, paywall hay cơ chế bảo vệ nội dung. Không commit cookie, token, thông tin tài khoản hoặc bản sao trái phép của học liệu.

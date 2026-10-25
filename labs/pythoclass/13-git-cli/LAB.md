# Lab 13 — Git và quy trình bài tập CLI

**Bài học liên quan:** PY-43–PY-44.  
**Bối cảnh thực tế:** Một nhóm học viên chỉnh sửa công cụ quản lý kho theo các phiên bản.

## Dữ liệu đầu vào
Bộ tệp gồm code, README và CSV giả lập; mỗi commit ghi nhận một thay đổi có ý nghĩa. Mỗi lab sử dụng **ít nhất 10 bản ghi**. Nếu có bảng dữ liệu đính kèm thì dùng file tại `../data/` (từ thư mục lab đi lên một cấp).

## Bài tập tăng tiến
1. **Mức 1:** Tạo repository thử nghiệm, xem git status và thêm tệp vào stage.
2. **Mức 2:** Thực hiện ít nhất 3 commit: tạo chương trình, thêm kiểm tra đầu vào, thêm test.
3. **Mức 3:** Tạo nhánh sửa bug và dùng git diff xem thay đổi trước khi merge.
4. **Mức 4:** Ghi README hướng dẫn chạy một chương trình CRUD mà không cần secret.

## Kiểm tra kết quả
- Đếm số bản ghi: tối thiểu 10; kiểm tra số hàng/cột và đơn vị trước khi xử lý.
- Với dữ liệu có giá hoặc điểm: kiểm tra giá trị âm/ngoài miền hợp lệ, dữ liệu rỗng và nhập sai kiểu.
- Đối chiếu ít nhất một kết quả thủ công với đầu ra Python; giải thích ý nghĩa kết quả chứ không chỉ in số.
- **Lời giải tham khảo:** xem `solution.py` nếu thư mục có tệp này; dùng để đối chiếu sau khi đã tự làm.

**Lưu ý:** Không commit mật khẩu, token hoặc tệp dữ liệu cá nhân.

**Liên hệ kiến thức:** [Mục lục 46 chương](../../../lessons/chapters/README.md) được đặt tại thư mục `lessons/chapters/` của repository. Đọc các chương nêu ở đầu lab trước khi mở bài liên quan đến thư viện mới.

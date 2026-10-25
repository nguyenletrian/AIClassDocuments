# Lab 04 — Hàm, OOP, kế thừa và lớp trừu tượng

**Bài học liên quan:** PY-09–PY-11.  
**Bối cảnh thực tế:** Một hệ thống quản lý 12 sản phẩm phân loại điện tử và gia dụng.

## Dữ liệu đầu vào
Mỗi dòng có mã, giá bán (nghìn đồng), danh mục và thuộc tính riêng theo danh mục. Mỗi lab sử dụng **ít nhất 10 bản ghi**. Nếu có bảng dữ liệu đính kèm thì dùng file tại `../data/` (từ thư mục lab đi lên một cấp).

## Bài tập tăng tiến
1. **Mức 1:** Tách logic tính giá sau giảm vào hàm có đối số và giá trị trả về.
2. **Mức 2:** Tạo Product chung với các thuộc tính mã, tên, giá; định nghĩa phương thức hiển thị.
3. **Mức 3:** Tạo hai lớp con có thuộc tính riêng; dùng super() và ghi đè phương thức.
4. **Mức 4:** Tạo bộ quản lý để tìm, lọc và thống kê tối thiểu 12 sản phẩm.

## Kiểm tra kết quả
- Đếm số bản ghi: tối thiểu 10; kiểm tra số hàng/cột và đơn vị trước khi xử lý.
- Với dữ liệu có giá hoặc điểm: kiểm tra giá trị âm/ngoài miền hợp lệ, dữ liệu rỗng và nhập sai kiểu.
- Đối chiếu ít nhất một kết quả thủ công với đầu ra Python; giải thích ý nghĩa kết quả chứ không chỉ in số.
- **Lời giải tham khảo:** xem `solution.py` nếu thư mục có tệp này; dùng để đối chiếu sau khi đã tự làm.

**Lưu ý:** Chương trình minh họa nên chạy không cần giao diện hay nhập trực tiếp.

**Liên hệ kiến thức:** [Mục lục 46 chương](../../../lessons/chapters/README.md) được đặt tại thư mục `lessons/chapters/` của repository. Đọc các chương nêu ở đầu lab trước khi mở bài liên quan đến thư viện mới.

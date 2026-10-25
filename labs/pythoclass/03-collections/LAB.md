# Lab 03 — List, tuple, set, dictionary và CRUD

**Bài học liên quan:** PY-06–PY-08, PY-44.  
**Bối cảnh thực tế:** Một cửa hàng muốn quản lý tối thiểu 12 sản phẩm, nhóm hàng và số lượng.

## Dữ liệu đầu vào
Mỗi sản phẩm có mã, tên giả lập, nhóm, giá (nghìn đồng), số lượng (chiếc). Mỗi lab sử dụng **ít nhất 10 bản ghi**. Nếu có bảng dữ liệu đính kèm thì dùng file tại `../data/` (từ thư mục lab đi lên một cấp).

## Bài tập tăng tiến
1. **Mức 1:** Lưu 12 sản phẩm trong list của dictionary; in sản phẩm còn hàng.
2. **Mức 2:** Tạo tập hợp nhóm hàng không trùng bằng set, trình bày sự khác nhau giữa list/tuple/set.
3. **Mức 3:** Viết chức năng tìm sản phẩm theo mã, thêm sản phẩm mới sau khi kiểm tra trùng mã.
4. **Mức 4:** Viết cập nhật tồn kho và xóa theo mã, kiểm tra dữ liệu đầu vào trước khi thay đổi.

## Kiểm tra kết quả
- Đếm số bản ghi: tối thiểu 10; kiểm tra số hàng/cột và đơn vị trước khi xử lý.
- Với dữ liệu có giá hoặc điểm: kiểm tra giá trị âm/ngoài miền hợp lệ, dữ liệu rỗng và nhập sai kiểu.
- Đối chiếu ít nhất một kết quả thủ công với đầu ra Python; giải thích ý nghĩa kết quả chứ không chỉ in số.
- **Lời giải tham khảo:** xem `solution.py` nếu thư mục có tệp này; dùng để đối chiếu sau khi đã tự làm.

**Lưu ý:** Không dùng tên biến list, dict, set để che khuất kiểu dựng sẵn.

**Liên hệ kiến thức:** [Mục lục 46 chương](../../../lessons/chapters/README.md) được đặt tại thư mục `lessons/chapters/` của repository. Đọc các chương nêu ở đầu lab trước khi mở bài liên quan đến thư viện mới.

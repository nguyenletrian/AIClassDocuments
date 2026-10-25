# Lab 11 — Xác suất và thống kê ứng dụng

**Bài học liên quan:** PY-34–PY-40.  
**Bối cảnh thực tế:** Đo thời gian hoàn thành 20 lượt xử lý đơn hàng.

## Dữ liệu đầu vào
20 dòng là 20 lượt xử lý; đơn vị mỗi số là phút; các giá trị là giả lập. Mỗi lab sử dụng **ít nhất 10 bản ghi**. Nếu có bảng dữ liệu đính kèm thì dùng file tại `../data/` (từ thư mục lab đi lên một cấp).

## Bài tập tăng tiến
1. **Mức 1:** Tính mean, median, min, max, độ lệch chuẩn và phân vị.
2. **Mức 2:** Tính tỷ lệ quan sát hoàn thành trong 15 phút; không đồng nhất tỷ lệ mẫu với xác suất tuyệt đối.
3. **Mức 3:** Chia dữ liệu thành nhóm nhanh/chậm, minh họa xác suất có điều kiện.
4. **Mức 4:** Tự viết mô phỏng bootstrap có random seed cố định và diễn giải khoảng ước lượng.

## Kiểm tra kết quả
- Đếm số bản ghi: tối thiểu 10; kiểm tra số hàng/cột và đơn vị trước khi xử lý.
- Với dữ liệu có giá hoặc điểm: kiểm tra giá trị âm/ngoài miền hợp lệ, dữ liệu rỗng và nhập sai kiểu.
- Đối chiếu ít nhất một kết quả thủ công với đầu ra Python; giải thích ý nghĩa kết quả chứ không chỉ in số.
- **Lời giải tham khảo:** xem `solution.py` nếu thư mục có tệp này; dùng để đối chiếu sau khi đã tự làm.

**Lưu ý:** Phân biệt thống kê mô tả mẫu và kết luận suy diễn ra tổng thể.

**Liên hệ kiến thức:** [Mục lục 46 chương](../../../lessons/chapters/README.md) được đặt tại thư mục `lessons/chapters/` của repository. Đọc các chương nêu ở đầu lab trước khi mở bài liên quan đến thư viện mới.

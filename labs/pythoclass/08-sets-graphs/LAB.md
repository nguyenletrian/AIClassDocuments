# Lab 08 — Tập hợp, tương đồng Jaccard và đồ thị

**Bài học liên quan:** PY-20–PY-23, PY-42.  
**Bối cảnh thực tế:** 12 học viên chọn những môn học yêu thích; tìm nhóm có sở thích tương đồng.

## Dữ liệu đầu vào
Mỗi học viên là một đỉnh; tập hợp môn học là dữ liệu đầu vào; cạnh nối hai học viên khi độ tương đồng đạt ngưỡng. Mỗi lab sử dụng **ít nhất 10 bản ghi**. Nếu có bảng dữ liệu đính kèm thì dùng file tại `../data/` (từ thư mục lab đi lên một cấp).

## Bài tập tăng tiến
1. **Mức 1:** Tạo 12 tập hợp sở thích và tập tất cả các môn xuất hiện.
2. **Mức 2:** Tính hợp, giao, hiệu cho hai học viên cụ thể.
3. **Mức 3:** Tính Jaccard cho từng cặp; xử lý trường hợp cả hai tập rỗng.
4. **Mức 4:** Tạo danh sách kề của đồ thị tại ngưỡng 0.5; phân biệt đỉnh và cạnh.

## Kiểm tra kết quả
- Đếm số bản ghi: tối thiểu 10; kiểm tra số hàng/cột và đơn vị trước khi xử lý.
- Với dữ liệu có giá hoặc điểm: kiểm tra giá trị âm/ngoài miền hợp lệ, dữ liệu rỗng và nhập sai kiểu.
- Đối chiếu ít nhất một kết quả thủ công với đầu ra Python; giải thích ý nghĩa kết quả chứ không chỉ in số.
- **Lời giải tham khảo:** xem `solution.py` nếu thư mục có tệp này; dùng để đối chiếu sau khi đã tự làm.

**Lưu ý:** Kết quả tương đồng chỉ mô tả sở thích chung, không chứng minh năng lực học tập.

**Liên hệ kiến thức:** [Mục lục 46 chương](../../../lessons/chapters/README.md) được đặt tại thư mục `lessons/chapters/` của repository. Đọc các chương nêu ở đầu lab trước khi mở bài liên quan đến thư viện mới.

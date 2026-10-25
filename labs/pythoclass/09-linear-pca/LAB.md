# Lab 09 — Vector, ma trận, Eigen và PCA

**Bài học liên quan:** PY-24–PY-27, AI-MATH-01.  
**Bối cảnh thực tế:** Một bảng 12 học viên có 3 điểm thành phần; muốn xem hướng biến thiên chính của dữ liệu.

## Dữ liệu đầu vào
Mỗi hàng là học viên, cột là điểm ba môn (0–10); dữ liệu ví dụ, không phải hồ sơ thật. Mỗi lab sử dụng **ít nhất 10 bản ghi**. Nếu có bảng dữ liệu đính kèm thì dùng file tại `../data/` (từ thư mục lab đi lên một cấp).

## Bài tập tăng tiến
1. **Mức 1:** Tạo ma trận 12×3; tính độ lớn vector và tích vô hướng của hai hàng.
2. **Mức 2:** Lấy vector trung bình theo cột, tạo dữ liệu đã trừ trung bình.
3. **Mức 3:** Tìm độ lớn biến thiên từng hướng qua PCA với n_components=2.
4. **Mức 4:** So sánh trước/sau bằng shape và tỷ lệ phương sai giải thích; không gọi đây là độ chính xác dự đoán.

## Kiểm tra kết quả
- Đếm số bản ghi: tối thiểu 10; kiểm tra số hàng/cột và đơn vị trước khi xử lý.
- Với dữ liệu có giá hoặc điểm: kiểm tra giá trị âm/ngoài miền hợp lệ, dữ liệu rỗng và nhập sai kiểu.
- Đối chiếu ít nhất một kết quả thủ công với đầu ra Python; giải thích ý nghĩa kết quả chứ không chỉ in số.
- **Lời giải tham khảo:** xem `solution.py` nếu thư mục có tệp này; dùng để đối chiếu sau khi đã tự làm.

**Lưu ý:** PCA là biến đổi dữ liệu, không phải mô hình tự động phân loại học viên.

**Liên hệ kiến thức:** [Mục lục 46 chương](../../../lessons/chapters/README.md) được đặt tại thư mục `lessons/chapters/` của repository. Đọc các chương nêu ở đầu lab trước khi mở bài liên quan đến thư viện mới.

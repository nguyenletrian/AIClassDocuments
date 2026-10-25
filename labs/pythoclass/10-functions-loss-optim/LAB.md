# Lab 10 — Hàm số, loss và gradient descent

**Bài học liên quan:** PY-28–PY-33.  
**Bối cảnh thực tế:** Ước lượng doanh số từ ngân sách quảng cáo cho 12 kỳ.

## Dữ liệu đầu vào
12 cặp số: chi phí quảng cáo (triệu đồng) và doanh số (triệu đồng). Mỗi lab sử dụng **ít nhất 10 bản ghi**. Nếu có bảng dữ liệu đính kèm thì dùng file tại `../data/` (từ thư mục lab đi lên một cấp).

## Bài tập tăng tiến
1. **Mức 1:** Dùng hàm tuyến tính dự đoán doanh số từ quảng cáo.
2. **Mức 2:** Tính MSE của bộ dự đoán ban đầu và đọc ý nghĩa sai số.
3. **Mức 3:** Cập nhật tham số bằng gradient descent trên dữ liệu được chuẩn hóa hợp lý.
4. **Mức 4:** So sánh sai số trước và sau; mô tả trường hợp learning rate quá cao.

## Kiểm tra kết quả
- Đếm số bản ghi: tối thiểu 10; kiểm tra số hàng/cột và đơn vị trước khi xử lý.
- Với dữ liệu có giá hoặc điểm: kiểm tra giá trị âm/ngoài miền hợp lệ, dữ liệu rỗng và nhập sai kiểu.
- Đối chiếu ít nhất một kết quả thủ công với đầu ra Python; giải thích ý nghĩa kết quả chứ không chỉ in số.
- **Lời giải tham khảo:** xem `solution.py` nếu thư mục có tệp này; dùng để đối chiếu sau khi đã tự làm.

**Lưu ý:** Không sử dụng dữ liệu mục tiêu khi chuẩn bị đặc trưng cho tập kiểm tra trong bài mô hình hóa.

**Liên hệ kiến thức:** [Mục lục 46 chương](../../../lessons/chapters/README.md) được đặt tại thư mục `lessons/chapters/` của repository. Đọc các chương nêu ở đầu lab trước khi mở bài liên quan đến thư viện mới.

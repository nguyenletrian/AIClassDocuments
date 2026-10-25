# Lab 06 — NumPy ndarray, indexing, aggregate, broadcast

**Bài học liên quan:** PY-13–PY-16.  
**Bối cảnh thực tế:** Phân tích điểm ba môn của 12 học viên như một ma trận.

## Dữ liệu đầu vào
12 hàng là học viên, 3 cột là Python/Toán/Tiếng Anh; mỗi ô là điểm 0–10. Mỗi lab sử dụng **ít nhất 10 bản ghi**. Nếu có bảng dữ liệu đính kèm thì dùng file tại `../data/` (từ thư mục lab đi lên một cấp).

## Bài tập tăng tiến
1. **Mức 1:** Tạo ndarray 12×3, kiểm tra shape, ndim và dtype.
2. **Mức 2:** Đọc hàng, cột và một lát cắt của ma trận.
3. **Mức 3:** Tính trung bình theo từng cột và từng học viên; giải thích trục axis.
4. **Mức 4:** Thử cộng điểm khuyến khích cho một cột bằng broadcasting, không vượt quá 10.

## Kiểm tra kết quả
- Đếm số bản ghi: tối thiểu 10; kiểm tra số hàng/cột và đơn vị trước khi xử lý.
- Với dữ liệu có giá hoặc điểm: kiểm tra giá trị âm/ngoài miền hợp lệ, dữ liệu rỗng và nhập sai kiểu.
- Đối chiếu ít nhất một kết quả thủ công với đầu ra Python; giải thích ý nghĩa kết quả chứ không chỉ in số.
- **Lời giải tham khảo:** xem `solution.py` nếu thư mục có tệp này; dùng để đối chiếu sau khi đã tự làm.

**Lưu ý:** Làm rõ trước/sau khi biến đổi và không đồng nhất phép cộng vào cột với cải thiện năng lực thực.

**Liên hệ kiến thức:** [Mục lục 46 chương](../../../lessons/chapters/README.md) được đặt tại thư mục `lessons/chapters/` của repository. Đọc các chương nêu ở đầu lab trước khi mở bài liên quan đến thư viện mới.

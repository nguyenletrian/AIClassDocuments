# Lab 12 — Tách train/test và mini-project AI

**Bài học liên quan:** PY-41, PY-46.  
**Bối cảnh thực tế:** Ước lượng doanh thu cửa hàng từ ngân sách marketing và lượng khách ở 24 tuần giả lập.

## Dữ liệu đầu vào
24 hàng là tuần, mỗi hàng có marketing (triệu đồng), visitors (người) và revenue (triệu đồng). Mỗi lab sử dụng **ít nhất 10 bản ghi**. Nếu có bảng dữ liệu đính kèm thì dùng file tại `../data/` (từ thư mục lab đi lên một cấp).

## Bài tập tăng tiến
1. **Mức 1:** Tạo tập dữ liệu 24 hàng, giải thích đâu là feature và target.
2. **Mức 2:** Dùng train_test_split tách train/test, cố định random_state.
3. **Mức 3:** Fit mô hình hồi quy trên train, dự đoán trên test và báo cáo MAE.
4. **Mức 4:** So sánh baseline với mô hình, giải thích giới hạn dữ liệu tổng hợp.

## Kiểm tra kết quả
- Đếm số bản ghi: tối thiểu 10; kiểm tra số hàng/cột và đơn vị trước khi xử lý.
- Với dữ liệu có giá hoặc điểm: kiểm tra giá trị âm/ngoài miền hợp lệ, dữ liệu rỗng và nhập sai kiểu.
- Đối chiếu ít nhất một kết quả thủ công với đầu ra Python; giải thích ý nghĩa kết quả chứ không chỉ in số.
- **Lời giải tham khảo:** xem `solution.py` nếu thư mục có tệp này; dùng để đối chiếu sau khi đã tự làm.

**Lưu ý:** Tuyệt đối không fit scaler/mô hình trước khi tách train/test.

**Liên hệ kiến thức:** [Mục lục 46 chương](../../../lessons/chapters/README.md) được đặt tại thư mục `lessons/chapters/` của repository. Đọc các chương nêu ở đầu lab trước khi mở bài liên quan đến thư viện mới.

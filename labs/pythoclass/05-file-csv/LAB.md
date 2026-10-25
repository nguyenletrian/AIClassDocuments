# Lab 05 — Làm việc với file CSV và ngoại lệ

**Bài học liên quan:** PY-12, PY-44.  
**Bối cảnh thực tế:** Bộ phận kho muốn đọc bảng 15 giao dịch bán hàng và tính tổng tiền.

## Dữ liệu đầu vào
File ../data/sales_sample.csv: mỗi dòng là một giao dịch, gồm order_id, product, category, quantity (cái), unit_price (nghìn đồng), month. Mỗi lab sử dụng **ít nhất 10 bản ghi**. Nếu có bảng dữ liệu đính kèm thì dùng file tại `../data/` (từ thư mục lab đi lên một cấp).

## Bài tập tăng tiến
1. **Mức 1:** Dùng csv.DictReader đọc 15 dòng và xem tên cột.
2. **Mức 2:** Đổi quantity/unit_price sang số, tính thành tiền từng dòng.
3. **Mức 3:** Bắt lỗi không tồn tại tệp, sai định dạng số và thiếu cột, giải thích nguyên nhân.
4. **Mức 4:** Thống kê tổng doanh thu toàn bộ và theo nhóm hàng; không ghi đè tệp dữ liệu gốc.

## Kiểm tra kết quả
- Đếm số bản ghi: tối thiểu 10; kiểm tra số hàng/cột và đơn vị trước khi xử lý.
- Với dữ liệu có giá hoặc điểm: kiểm tra giá trị âm/ngoài miền hợp lệ, dữ liệu rỗng và nhập sai kiểu.
- Đối chiếu ít nhất một kết quả thủ công với đầu ra Python; giải thích ý nghĩa kết quả chứ không chỉ in số.
- **Lời giải tham khảo:** xem `solution.py` nếu thư mục có tệp này; dùng để đối chiếu sau khi đã tự làm.

**Lưu ý:** Đường dẫn đọc được neo theo __file__, không phụ thuộc thư mục chạy lệnh.

**Liên hệ kiến thức:** [Mục lục 46 chương](../../../lessons/chapters/README.md) được đặt tại thư mục `lessons/chapters/` của repository. Đọc các chương nêu ở đầu lab trước khi mở bài liên quan đến thư viện mới.

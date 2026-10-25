# Lab 02 — Điều kiện, vòng lặp, kiểm tra dữ liệu

**Bài học liên quan:** PY-04–PY-05.  
**Bối cảnh thực tế:** Một cửa hàng có doanh thu theo 12 tháng; cần xếp quý, đánh giá tháng vượt chỉ tiêu.

## Dữ liệu đầu vào
12 bản ghi tương ứng tháng 1–12; doanh thu theo triệu đồng. Mỗi lab sử dụng **ít nhất 10 bản ghi**. Nếu có bảng dữ liệu đính kèm thì dùng file tại `../data/` (từ thư mục lab đi lên một cấp).

## Bài tập tăng tiến
1. **Mức 1:** Dùng if/elif/else xác định quý của từng tháng; kiểm tra tháng thuộc 1–12.
2. **Mức 2:** Dùng for tính tổng doanh thu năm và đếm tháng vượt 25 triệu đồng.
3. **Mức 3:** Dùng while mô phỏng nhập đến khi giá trị hợp lệ; bảo vệ trước đầu vào không phải số.
4. **Mức 4:** Mở rộng: kiểm tra năm nhuận và số ngày theo tháng với quy tắc lịch Gregorian.

## Kiểm tra kết quả
- Đếm số bản ghi: tối thiểu 10; kiểm tra số hàng/cột và đơn vị trước khi xử lý.
- Với dữ liệu có giá hoặc điểm: kiểm tra giá trị âm/ngoài miền hợp lệ, dữ liệu rỗng và nhập sai kiểu.
- Đối chiếu ít nhất một kết quả thủ công với đầu ra Python; giải thích ý nghĩa kết quả chứ không chỉ in số.
- **Lời giải tham khảo:** xem `solution.py` nếu thư mục có tệp này; dùng để đối chiếu sau khi đã tự làm.

**Lưu ý:** Không phân loại tháng 0, 13 thành quý hợp lệ.

**Liên hệ kiến thức:** [Mục lục 46 chương](../../../lessons/chapters/README.md) được đặt tại thư mục `lessons/chapters/` của repository. Đọc các chương nêu ở đầu lab trước khi mở bài liên quan đến thư viện mới.

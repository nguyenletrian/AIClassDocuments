# Lab 07 — Pandas DataFrame, làm sạch, groupby

**Bài học liên quan:** PY-17–PY-19, PY-45.  
**Bối cảnh thực tế:** Phân tích 15 giao dịch bán hàng và báo cáo theo danh mục.

## Dữ liệu đầu vào
Nguồn dùng ../data/sales_sample.csv; 15 dòng là giao dịch, giá tính nghìn đồng. Mỗi lab sử dụng **ít nhất 10 bản ghi**. Nếu có bảng dữ liệu đính kèm thì dùng file tại `../data/` (từ thư mục lab đi lên một cấp).

## Bài tập tăng tiến
1. **Mức 1:** Đọc CSV vào DataFrame, xem shape, head, dtype.
2. **Mức 2:** Kiểm tra thiếu và trùng dữ liệu, báo cáo trước khi quyết định xóa.
3. **Mức 3:** Thêm cột revenue = quantity × unit_price, tính tổng theo danh mục bằng groupby.
4. **Mức 4:** Sắp xếp doanh thu giảm dần và trực quan hóa theo danh mục khi có Matplotlib.

## Kiểm tra kết quả
- Đếm số bản ghi: tối thiểu 10; kiểm tra số hàng/cột và đơn vị trước khi xử lý.
- Với dữ liệu có giá hoặc điểm: kiểm tra giá trị âm/ngoài miền hợp lệ, dữ liệu rỗng và nhập sai kiểu.
- Đối chiếu ít nhất một kết quả thủ công với đầu ra Python; giải thích ý nghĩa kết quả chứ không chỉ in số.
- **Lời giải tham khảo:** xem `solution.py` nếu thư mục có tệp này; dùng để đối chiếu sau khi đã tự làm.

**Lưu ý:** Không gán kết quả nhóm vào dữ liệu gốc; ghi rõ dữ liệu minh họa.

**Liên hệ kiến thức:** [Mục lục 46 chương](../../../lessons/chapters/README.md) được đặt tại thư mục `lessons/chapters/` của repository. Đọc các chương nêu ở đầu lab trước khi mở bài liên quan đến thư viện mới.

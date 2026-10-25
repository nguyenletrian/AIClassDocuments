# Lab 01 — Biến, kiểu dữ liệu, nhập/xuất

**Bài học liên quan:** PY-01–PY-03.  
**Bối cảnh thực tế:** Một lớp 12 học viên có mã HV001–HV012, tuổi và 3 điểm môn học (0–10).

## Dữ liệu đầu vào
Mỗi dòng biểu diễn một học viên; các cột: mã học viên, tuổi (năm), điểm Python, Toán và Tiếng Anh (thang 10). Mỗi lab sử dụng **ít nhất 10 bản ghi**. Nếu có bảng dữ liệu đính kèm thì dùng file tại `../data/` (từ thư mục lab đi lên một cấp).

## Bài tập tăng tiến
1. **Mức 1:** Tạo 12 bản ghi có mã, tuổi và ba điểm; in một bản ghi bằng f-string.
2. **Mức 2:** Chuyển dữ liệu điểm từ chuỗi sang số trước khi tính trung bình.
3. **Mức 3:** Dùng toán tử so sánh để đánh dấu người có trung bình từ 8.0 trở lên.
4. **Mức 4:** Xử lý trường hợp một điểm nhập sai kiểu hoặc nằm ngoài 0–10.

## Kiểm tra kết quả
- Đếm số bản ghi: tối thiểu 10; kiểm tra số hàng/cột và đơn vị trước khi xử lý.
- Với dữ liệu có giá hoặc điểm: kiểm tra giá trị âm/ngoài miền hợp lệ, dữ liệu rỗng và nhập sai kiểu.
- Đối chiếu ít nhất một kết quả thủ công với đầu ra Python; giải thích ý nghĩa kết quả chứ không chỉ in số.
- **Lời giải tham khảo:** xem `solution.py` nếu thư mục có tệp này; dùng để đối chiếu sau khi đã tự làm.

**Lưu ý:** Không đưa dữ liệu nhận dạng sinh viên thật vào ví dụ.

**Liên hệ kiến thức:** [Mục lục 46 chương](../../../lessons/chapters/README.md) được đặt tại thư mục `lessons/chapters/` của repository. Đọc các chương nêu ở đầu lab trước khi mở bài liên quan đến thư viện mới.

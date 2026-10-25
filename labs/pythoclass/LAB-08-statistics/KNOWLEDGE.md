# Tổng hợp kiến thức — Lab Session 8

## Bài học liên quan
- [PY-17 — Pandas](../../../lessons/chapters/PY-17-pandas-dataframe.vi.md)
- [PY-37 — Thống kê mô tả](../../../lessons/chapters/PY-37-descriptive-statistics.vi.md)
- [PY-38 — Phân vị và Outlier](../../../lessons/chapters/PY-38-quantile-outlier.vi.md)
- [PY-39 — Lấy mẫu](../../../lessons/chapters/PY-39-sampling-clt.vi.md)
- [PY-40 — Kiểm định](../../../lessons/chapters/PY-40-hypothesis-confidence.vi.md)

## 1. 50 hàng, mỗi hàng là một người dùng
Một giá trị là **số phút dùng ứng dụng trong một ngày**. Trung bình (mean) dễ bị kéo lên bởi 480 phút; trung vị (median) mô tả giá trị ở giữa. Mốt (mode) là giá trị xuất hiện nhiều lần nhất.

## 2. Độ phân tán
**Range:** max−min; **sample variance:** đo độ phân tán bình phương, tính với `ddof=1`; **sample standard deviation:** đơn vị phút, dễ diễn giải hơn phương sai.

## 3. Tần suất và outlier
`pd.cut` chia nhóm độ dài đã nêu trong Word; chú ý ranh giới 60, 120... thuộc nhóm nào để **không đếm trùng**. `value_counts` cho số lượng mỗi nhóm; `cumsum` cho tần suất tích lũy. Q1/Q3 chia dữ liệu thành 4 phần; **IQR = Q3−Q1**. Quy tắc 1.5×IQR chỉ là gợi ý phát hiện ngoại lệ, không tự động cho phép xóa.

## 4. T-test
- `H0: mu = 120` phút/ngày.
- `H1: mu != 120` (kiểm định hai phía).
- `alpha = 0.05`. Nếu `p < 0.05`, bác bỏ H0; ngược lại **chưa đủ bằng chứng bác bỏ**, không chứng minh H0 đúng.
- Các 50 bản ghi là dữ liệu minh họa; muốn suy diễn tổng thể phải bảo đảm giả thiết lấy mẫu.

Cài: `pip install numpy pandas scipy matplotlib`.

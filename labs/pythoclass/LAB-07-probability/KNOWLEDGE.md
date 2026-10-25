# Tổng hợp kiến thức — Lab Session 7

## Bài học liên quan
- [PY-21 — Tập hợp](../../../lessons/chapters/PY-21-sets-inclusion-exclusion.vi.md)
- [PY-34 — Xác suất](../../../lessons/chapters/PY-34-probability-foundations.vi.md)
- [PY-35 — Xác suất có điều kiện và Bayes](../../../lessons/chapters/PY-35-conditional-bayes.vi.md)
- [PY-36 — Phân phối xác suất](../../../lessons/chapters/PY-36-probability-distributions.vi.md)
- [PY-45 — Biểu đồ](../../../lessons/chapters/PY-45-visualize-data.vi.md)

## 1. Từ tập hợp đến xác suất
**Sample space:** mọi kết quả có thể xảy ra, ví dụ các thẻ 1..10. **Event:** tập con của kết quả, như số chẵn. **Intersection:** cả A và B xảy ra. **Union:** ít nhất một trong hai xảy ra.

## 2. Lý thuyết và mô phỏng
**Theoretical probability** dựa trên giả thiết và số trường hợp. **Experimental probability** là tỷ lệ quan sát trong mô phỏng 5000 lần, thường gần lý thuyết nhưng không bắt buộc trùng khít. Dùng `np.random.default_rng(seed)` để tái lập.

## 3. Điều kiện và Bayes
Xác suất có điều kiện `P(A|B)` đo khả năng A khi biết B đã xảy ra; khác `P(B|A)`. Trong ví dụ spam, kết quả được đánh dấu spam **không đồng nghĩa chắc chắn là spam** do còn tỷ lệ báo nhầm.

## 4. Binomial
Nếu có 8 yêu cầu độc lập, xác suất giải quyết mỗi yêu cầu là 0.75, số thành công có phân phối nhị thức. Dùng `scipy.stats.binom.pmf(k,8,0.75)` để xem đúng k yêu cầu, và cộng từ k=6 đến 8 để tính ít nhất 6. Trực quan hóa từng cột k=0..8.

Cài: `pip install numpy scipy matplotlib`.

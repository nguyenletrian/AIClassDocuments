# PY-15 — NumPy tổng hợp, axis và broadcasting

## 1. Vị trí trong chuỗi kiến thức

`Index/Slice → Aggregate/Broadcast → Vectorization → AI`

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Dùng khi nào |
|---|---|---|
| Aggregate | phép tổng hợp | Gom nhiều giá trị thành chỉ số thống kê |
| Axis | trục tính | Chiều dọc theo phép gom giá trị |
| Broadcasting | quảng bá mảng | Mở rộng kích thước tương thích khi tính |
| Vectorization | vector hóa | Tính cả mảng không cần viết vòng for từng phần tử |

## 3. Thư viện, hàm và lựa chọn

| Hàm / tham số | Giải thích ngay theo hàm |
|---|---|
| `np.sum(X,axis=0)` | Tổng theo từng cột, axis=1 tổng theo hàng |
| `np.mean()/np.max()/np.min()` | Tổng hợp trung bình, cực đại và cực tiểu |
| `X + scalar / X + vector` | Broadcast nếu shape tương thích |
| `np.sqrt()/np.exp()` | Biến đổi từng phần tử, chú ý miền giá trị |

## 4. Khái niệm liên quan và ví dụ nhỏ

### 4.1. Aggregate

Gom nhiều giá trị thành chỉ số thống kê.

```python
import numpy as np
print(np.array([1,2,3]).sum())
```

### 4.2. Axis

Chiều dọc theo phép gom giá trị.

```python
import numpy as np
print(np.array([[1,2],[3,4]]).mean(axis=0))
```

### 4.3. Broadcasting

Mở rộng kích thước tương thích khi tính.

```python
import numpy as np
print(np.array([1,2])+3)
```

### 4.4. Vectorization

Tính cả mảng không cần viết vòng for từng phần tử.

```python
import numpy as np
print(np.array([1,2,3])*2)
```

## 5. Năm tình huống thực tế

### Tình huống 1 — Tổng doanh thu mỗi cửa hàng

**Vấn đề:** Tổng doanh thu mỗi cửa hàng.

**Vì sao chọn cách giải này?** axis=1 cộng các ngày trên một hàng/cửa hàng.

**Dữ liệu:** 2 cửa hàng × 3 ngày, nghìn đồng.

```python
import numpy as np
sales=np.array([[10,20,30],[8,12,16]])
print(sales.sum(axis=1))
```

### Tình huống 2 — Điểm trung bình từng môn

**Vấn đề:** Điểm trung bình từng môn.

**Vì sao chọn cách giải này?** axis=0 gom toàn bộ học sinh theo một cột môn.

**Dữ liệu:** 3 học sinh × 2 môn.

```python
import numpy as np
X=np.array([[8,9],[6,7],[9,8]],dtype=float)
print(X.mean(axis=0))
```

### Tình huống 3 — Cộng điểm chuyên cần

**Vấn đề:** Cộng điểm chuyên cần.

**Vì sao chọn cách giải này?** Broadcast cộng thưởng 1 điểm cho từng môn.

**Dữ liệu:** 2 học sinh × 3 môn.

```python
import numpy as np
X=np.array([[7,8,9],[6,7,8]])
print(np.minimum(X+1,10))
```

### Tình huống 4 — Nhân các kênh cảm biến

**Vấn đề:** Nhân các kênh cảm biến.

**Vì sao chọn cách giải này?** Vector hóa nhân hệ số cho toàn bộ kênh.

**Dữ liệu:** 3 giá trị đo và hệ số quy đổi.

```python
import numpy as np
signals=np.array([10,20,30])
factors=np.array([1.0,0.5,2.0])
print(signals*factors)
```

### Tình huống 5 — Tìm giá trị cao nhất theo cột

**Vấn đề:** Tìm giá trị cao nhất theo cột.

**Vì sao chọn cách giải này?** max(axis=0) chọn đỉnh từng feature.

**Dữ liệu:** 3 mẫu × 2 kênh.

```python
import numpy as np
X=np.array([[2,4],[5,1],[3,6]])
print(X.max(axis=0))
```

## 6. Sai lầm thường gặp

Các tham số như axis, shape, dtype hoặc cách xử lý giá trị thiếu có thể thay đổi kết quả. Trước khi xử lý phải biết số hàng, số cột, đơn vị và mục đích của từng phép biến đổi.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ


**Q1. What does Aggregate mean? — Ý nghĩa của Aggregate là gì?**

A. It instead describes Chiều dọc theo phép gom giá trị — Chiều dọc theo phép gom giá trị

B. The concept is Gom nhiều giá trị thành chỉ số thống kê — Gom nhiều giá trị thành chỉ số thống kê

C. It instead describes Mở rộng kích thước tương thích khi tính — Mở rộng kích thước tương thích khi tính

D. It instead describes Tính cả mảng không cần viết vòng for từng phần tử — Tính cả mảng không cần viết vòng for từng phần tử


**Q2. What does Axis mean? — Ý nghĩa của Axis là gì?**

A. The concept is Chiều dọc theo phép gom giá trị — Chiều dọc theo phép gom giá trị

B. It instead describes Mở rộng kích thước tương thích khi tính — Mở rộng kích thước tương thích khi tính

C. It instead describes Tính cả mảng không cần viết vòng for từng phần tử — Tính cả mảng không cần viết vòng for từng phần tử

D. It instead describes Gom nhiều giá trị thành chỉ số thống kê — Gom nhiều giá trị thành chỉ số thống kê


**Q3. What does Broadcasting mean? — Ý nghĩa của Broadcasting là gì?**

A. It instead describes Tính cả mảng không cần viết vòng for từng phần tử — Tính cả mảng không cần viết vòng for từng phần tử

B. It instead describes Gom nhiều giá trị thành chỉ số thống kê — Gom nhiều giá trị thành chỉ số thống kê

C. It instead describes Chiều dọc theo phép gom giá trị — Chiều dọc theo phép gom giá trị

D. The concept is Mở rộng kích thước tương thích khi tính — Mở rộng kích thước tương thích khi tính


**Q4. What does Vectorization mean? — Ý nghĩa của Vectorization là gì?**

A. It instead describes Gom nhiều giá trị thành chỉ số thống kê — Gom nhiều giá trị thành chỉ số thống kê

B. It instead describes Chiều dọc theo phép gom giá trị — Chiều dọc theo phép gom giá trị

C. The concept is Tính cả mảng không cần viết vòng for từng phần tử — Tính cả mảng không cần viết vòng for từng phần tử

D. It instead describes Mở rộng kích thước tương thích khi tính — Mở rộng kích thước tương thích khi tính


**Q5. What is the role of np.sum(X,axis=0)? — Vai trò của np.sum(X,axis=0) là gì?**

A. Another operation would Tổng hợp trung bình, cực đại và cực tiểu — Tổng hợp trung bình, cực đại và cực tiểu

B. It is used to Tổng theo từng cột, axis=1 tổng theo hàng — Tổng theo từng cột, axis=1 tổng theo hàng

C. Another operation would Broadcast nếu shape tương thích — Broadcast nếu shape tương thích

D. Another operation would Biến đổi từng phần tử, chú ý miền giá trị — Biến đổi từng phần tử, chú ý miền giá trị


**Q6. What is the role of np.mean()/np.max()/np.min()? — Vai trò của np.mean()/np.max()/np.min() là gì?**

A. It is used to Tổng hợp trung bình, cực đại và cực tiểu — Tổng hợp trung bình, cực đại và cực tiểu

B. Another operation would Broadcast nếu shape tương thích — Broadcast nếu shape tương thích

C. Another operation would Biến đổi từng phần tử, chú ý miền giá trị — Biến đổi từng phần tử, chú ý miền giá trị

D. Another operation would Tổng theo từng cột, axis=1 tổng theo hàng — Tổng theo từng cột, axis=1 tổng theo hàng


**Q7. What is the role of X + scalar / X + vector? — Vai trò của X + scalar / X + vector là gì?**

A. Another operation would Biến đổi từng phần tử, chú ý miền giá trị — Biến đổi từng phần tử, chú ý miền giá trị

B. Another operation would Tổng theo từng cột, axis=1 tổng theo hàng — Tổng theo từng cột, axis=1 tổng theo hàng

C. Another operation would Tổng hợp trung bình, cực đại và cực tiểu — Tổng hợp trung bình, cực đại và cực tiểu

D. It is used to Broadcast nếu shape tương thích — Broadcast nếu shape tương thích


**Q8. What is the role of np.sqrt()/np.exp()? — Vai trò của np.sqrt()/np.exp() là gì?**

A. Another operation would Tổng theo từng cột, axis=1 tổng theo hàng — Tổng theo từng cột, axis=1 tổng theo hàng

B. Another operation would Tổng hợp trung bình, cực đại và cực tiểu — Tổng hợp trung bình, cực đại và cực tiểu

C. It is used to Biến đổi từng phần tử, chú ý miền giá trị — Biến đổi từng phần tử, chú ý miền giá trị

D. Another operation would Broadcast nếu shape tương thích — Broadcast nếu shape tương thích


**Q9. Which reason fits example 1? — Lý do nào phù hợp ví dụ 1?**

A. axis=0 gom toàn bộ học sinh theo một cột môn — axis=0 gom toàn bộ học sinh theo một cột môn

B. axis=1 cộng các ngày trên một hàng/cửa hàng — axis=1 cộng các ngày trên một hàng/cửa hàng

C. Broadcast cộng thưởng 1 điểm cho từng môn — Broadcast cộng thưởng 1 điểm cho từng môn

D. Vector hóa nhân hệ số cho toàn bộ kênh — Vector hóa nhân hệ số cho toàn bộ kênh


**Q10. Which reason fits example 2? — Lý do nào phù hợp ví dụ 2?**

A. axis=0 gom toàn bộ học sinh theo một cột môn — axis=0 gom toàn bộ học sinh theo một cột môn

B. Broadcast cộng thưởng 1 điểm cho từng môn — Broadcast cộng thưởng 1 điểm cho từng môn

C. Vector hóa nhân hệ số cho toàn bộ kênh — Vector hóa nhân hệ số cho toàn bộ kênh

D. max(axis=0) chọn đỉnh từng feature — max(axis=0) chọn đỉnh từng feature


**Q11. Which reason fits example 3? — Lý do nào phù hợp ví dụ 3?**

A. Vector hóa nhân hệ số cho toàn bộ kênh — Vector hóa nhân hệ số cho toàn bộ kênh

B. max(axis=0) chọn đỉnh từng feature — max(axis=0) chọn đỉnh từng feature

C. axis=1 cộng các ngày trên một hàng/cửa hàng — axis=1 cộng các ngày trên một hàng/cửa hàng

D. Broadcast cộng thưởng 1 điểm cho từng môn — Broadcast cộng thưởng 1 điểm cho từng môn


**Q12. Which reason fits example 4? — Lý do nào phù hợp ví dụ 4?**

A. max(axis=0) chọn đỉnh từng feature — max(axis=0) chọn đỉnh từng feature

B. axis=1 cộng các ngày trên một hàng/cửa hàng — axis=1 cộng các ngày trên một hàng/cửa hàng

C. Vector hóa nhân hệ số cho toàn bộ kênh — Vector hóa nhân hệ số cho toàn bộ kênh

D. axis=0 gom toàn bộ học sinh theo một cột môn — axis=0 gom toàn bộ học sinh theo một cột môn


**Q13. Which reason fits example 5? — Lý do nào phù hợp ví dụ 5?**

A. axis=1 cộng các ngày trên một hàng/cửa hàng — axis=1 cộng các ngày trên một hàng/cửa hàng

B. max(axis=0) chọn đỉnh từng feature — max(axis=0) chọn đỉnh từng feature

C. axis=0 gom toàn bộ học sinh theo một cột môn — axis=0 gom toàn bộ học sinh theo một cột môn

D. Broadcast cộng thưởng 1 điểm cho từng môn — Broadcast cộng thưởng 1 điểm cho từng môn


**Q14. Which input matches example 1? — Dữ liệu nào phù hợp ví dụ 1?**

A. The stated data are 2 cửa hàng × 3 ngày, nghìn đồng — 2 cửa hàng × 3 ngày, nghìn đồng

B. Other data: 3 học sinh × 2 môn — 3 học sinh × 2 môn

C. Other data: 2 học sinh × 3 môn — 2 học sinh × 3 môn

D. Other data: 3 giá trị đo và hệ số quy đổi — 3 giá trị đo và hệ số quy đổi


**Q15. Which input matches example 2? — Dữ liệu nào phù hợp ví dụ 2?**

A. Other data: 2 học sinh × 3 môn — 2 học sinh × 3 môn

B. Other data: 3 giá trị đo và hệ số quy đổi — 3 giá trị đo và hệ số quy đổi

C. Other data: 3 mẫu × 2 kênh — 3 mẫu × 2 kênh

D. The stated data are 3 học sinh × 2 môn — 3 học sinh × 2 môn


**Q16. Which input matches example 3? — Dữ liệu nào phù hợp ví dụ 3?**

A. Other data: 3 giá trị đo và hệ số quy đổi — 3 giá trị đo và hệ số quy đổi

B. Other data: 3 mẫu × 2 kênh — 3 mẫu × 2 kênh

C. The stated data are 2 học sinh × 3 môn — 2 học sinh × 3 môn

D. Other data: 2 cửa hàng × 3 ngày, nghìn đồng — 2 cửa hàng × 3 ngày, nghìn đồng


**Q17. Which input matches example 4? — Dữ liệu nào phù hợp ví dụ 4?**

A. Other data: 3 mẫu × 2 kênh — 3 mẫu × 2 kênh

B. The stated data are 3 giá trị đo và hệ số quy đổi — 3 giá trị đo và hệ số quy đổi

C. Other data: 2 cửa hàng × 3 ngày, nghìn đồng — 2 cửa hàng × 3 ngày, nghìn đồng

D. Other data: 3 học sinh × 2 môn — 3 học sinh × 2 môn


**Q18. Which input matches example 5? — Dữ liệu nào phù hợp ví dụ 5?**

A. The stated data are 3 mẫu × 2 kênh — 3 mẫu × 2 kênh

B. Other data: 2 cửa hàng × 3 ngày, nghìn đồng — 2 cửa hàng × 3 ngày, nghìn đồng

C. Other data: 3 học sinh × 2 môn — 3 học sinh × 2 môn

D. Other data: 2 học sinh × 3 môn — 2 học sinh × 3 môn


**Q19. What must every table clarify? — Bảng dữ liệu cần nêu rõ gì?**

A. Only editor color — Chỉ màu trình soạn

B. Only variable length — Chỉ độ dài tên biến

C. Only number of blank lines — Chỉ số dòng trống

D. Rows, columns and units — Hàng, cột và đơn vị


**Q20. Why test with different inputs? — Tại sao cần thử đầu vào khác?**

A. To guarantee machine learning accuracy — Để bảo đảm AI luôn đúng

B. To remove input validation — Để bỏ kiểm tra dữ liệu

C. To check limitations and edge cases — Để thấy giới hạn và trường hợp biên

D. To change column meanings — Để thay đổi nghĩa các cột

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **B** | The concept is Gom nhiều giá trị thành chỉ số thống kê | Gom nhiều giá trị thành chỉ số thống kê |
| Q2 | **A** | The concept is Chiều dọc theo phép gom giá trị | Chiều dọc theo phép gom giá trị |
| Q3 | **D** | The concept is Mở rộng kích thước tương thích khi tính | Mở rộng kích thước tương thích khi tính |
| Q4 | **C** | The concept is Tính cả mảng không cần viết vòng for từng phần tử | Tính cả mảng không cần viết vòng for từng phần tử |
| Q5 | **B** | It is used to Tổng theo từng cột, axis=1 tổng theo hàng | Tổng theo từng cột, axis=1 tổng theo hàng |
| Q6 | **A** | It is used to Tổng hợp trung bình, cực đại và cực tiểu | Tổng hợp trung bình, cực đại và cực tiểu |
| Q7 | **D** | It is used to Broadcast nếu shape tương thích | Broadcast nếu shape tương thích |
| Q8 | **C** | It is used to Biến đổi từng phần tử, chú ý miền giá trị | Biến đổi từng phần tử, chú ý miền giá trị |
| Q9 | **B** | axis=1 cộng các ngày trên một hàng/cửa hàng | axis=1 cộng các ngày trên một hàng/cửa hàng |
| Q10 | **A** | axis=0 gom toàn bộ học sinh theo một cột môn | axis=0 gom toàn bộ học sinh theo một cột môn |
| Q11 | **D** | Broadcast cộng thưởng 1 điểm cho từng môn | Broadcast cộng thưởng 1 điểm cho từng môn |
| Q12 | **C** | Vector hóa nhân hệ số cho toàn bộ kênh | Vector hóa nhân hệ số cho toàn bộ kênh |
| Q13 | **B** | max(axis=0) chọn đỉnh từng feature | max(axis=0) chọn đỉnh từng feature |
| Q14 | **A** | The stated data are 2 cửa hàng × 3 ngày, nghìn đồng | 2 cửa hàng × 3 ngày, nghìn đồng |
| Q15 | **D** | The stated data are 3 học sinh × 2 môn | 3 học sinh × 2 môn |
| Q16 | **C** | The stated data are 2 học sinh × 3 môn | 2 học sinh × 3 môn |
| Q17 | **B** | The stated data are 3 giá trị đo và hệ số quy đổi | 3 giá trị đo và hệ số quy đổi |
| Q18 | **A** | The stated data are 3 mẫu × 2 kênh | 3 mẫu × 2 kênh |
| Q19 | **D** | Rows, columns and units | Hàng, cột và đơn vị |
| Q20 | **C** | To check limitations and edge cases | Để thấy giới hạn và trường hợp biên |

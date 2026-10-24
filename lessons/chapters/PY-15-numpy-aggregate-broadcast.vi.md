# PY-15 — NumPy tổng hợp, axis và broadcasting


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Aggregate** — phép tổng hợp; **Axis** — trục tính.

`Index/Slice → Aggregate/Broadcast → Vectorization → AI`

Nắm khái niệm của bài này giúp xử lý đúng dữ liệu có nhiều đối tượng và đặc trưng trước khi dùng trong AI.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Dùng khi nào |
|---|---|---|
| Aggregate | phép tổng hợp | Gom nhiều giá trị thành chỉ số thống kê |
| Axis | trục tính | Chiều dọc theo phép gom giá trị |
| Broadcasting | quảng bá mảng | Mở rộng kích thước tương thích khi tính |
| Vectorization | vector hóa | Tính cả mảng không cần viết vòng for từng phần tử |

## 3. Thư viện, hàm và lựa chọn

**Từ vựng trong mục:** **Function** — hàm; **Argument** — đối số.

| Hàm / tham số | Giải thích ngay theo hàm |
|---|---|
| `np.sum(X,axis=0)` | Tổng theo từng cột, axis=1 tổng theo hàng |
| `np.mean()/np.max()/np.min()` | Tổng hợp trung bình, cực đại và cực tiểu |
| `X + scalar / X + vector` | Broadcast nếu shape tương thích |
| `np.sqrt()/np.exp()` | Biến đổi từng phần tử, chú ý miền giá trị |


## 4. Khái niệm liên quan

### 4.1. Aggregate

**Từ vựng trong mục:** **Aggregate** — phép tổng hợp.

Phép tổng hợp như `sum`, `mean`, `max` rút nhiều giá trị thành một hoặc vài số dễ theo dõi.

```python
import numpy as np
print(np.array([1,2,3]).sum())
```

**Kết quả khi chạy:**

```text
6
```

### 4.2. Axis

**Từ vựng trong mục:** **Axis** — trục tính.

Với mảng hai chiều, `axis=0` tổng hợp theo cột, còn `axis=1` tổng hợp theo hàng.

```python
import numpy as np
print(np.array([[1,2],[3,4]]).mean(axis=0))
```

**Kết quả khi chạy:**

```text
[2. 3.]
```

### 4.3. Broadcasting

**Từ vựng trong mục:** **Broadcasting** — quảng bá mảng.

Broadcasting cho phép cộng hoặc nhân một số với từng phần tử của mảng mà không viết vòng lặp.

```python
import numpy as np
print(np.array([1,2])+3)
```

**Kết quả khi chạy:**

```text
[4 5]
```

### 4.4. Vectorization

**Từ vựng trong mục:** **Vectorization** — vector hóa.

Vectorization tính trực tiếp nhiều phần tử bằng phép toán trên mảng NumPy.

```python
import numpy as np
print(np.array([1,2,3])*2)
```

**Kết quả khi chạy:**

```text
[2 4 6]
```

## 5. Năm tình huống thực tế

### Tình huống 1 — Tổng doanh thu mỗi cửa hàng

**Từ vựng trong mục:** **Aggregate** — phép tổng hợp.

**Tình huống thực tế:** Hai cửa hàng có doanh thu ba ngày là `[10,20,30]` và `[8,12,16]` triệu đồng. Tính doanh thu mỗi cửa hàng.

**Vì sao chọn cách giải này?** `sum(axis=1)` cộng các ngày trong từng hàng.

**Quy trình giải:** Lưu dữ liệu đúng thứ tự hàng/cột → dùng phép NumPy phù hợp → in và giải thích kết quả.

```python
import numpy as np
sales=np.array([[10,20,30],[8,12,16]])
print(sales.sum(axis=1))
```

**Kết quả khi chạy:**

```text
[60 36]
```

**Kết quả:** Xem ngay giá trị bên dưới đoạn code để biết phép tính đã thực hiện gì.

### Tình huống 2 — Điểm trung bình từng môn

**Từ vựng trong mục:** **Axis** — trục tính.

**Tình huống thực tế:** Ba học viên có điểm hai môn lần lượt là `(8,9)`, `(6,7)`, `(9,8)`. Tính trung bình của từng môn.

**Vì sao chọn cách giải này?** `mean(axis=0)` gom các điểm cùng cột môn học.

**Quy trình giải:** Lưu dữ liệu đúng thứ tự hàng/cột → dùng phép NumPy phù hợp → in và giải thích kết quả.

```python
import numpy as np
X=np.array([[8,9],[6,7],[9,8]],dtype=float)
print(X.mean(axis=0))
```

**Kết quả khi chạy:**

```text
[7.66666667 8.        ]
```

**Kết quả:** Xem ngay giá trị bên dưới đoạn code để biết phép tính đã thực hiện gì.

### Tình huống 3 — Cộng điểm chuyên cần

**Từ vựng trong mục:** **Broadcasting** — quảng bá mảng.

**Tình huống thực tế:** Hai học viên có điểm ba môn `(7,8,9)` và `(6,7,8)`, được cộng 1 điểm chuyên cần nhưng không vượt 10. In bảng điểm sau cộng.

**Vì sao chọn cách giải này?** Broadcasting cộng 1 vào mọi ô; `minimum(...,10)` chặn điểm tối đa.

**Quy trình giải:** Lưu dữ liệu đúng thứ tự hàng/cột → dùng phép NumPy phù hợp → in và giải thích kết quả.

```python
import numpy as np
X=np.array([[7,8,9],[6,7,8]])
print(np.minimum(X+1,10))
```

**Kết quả khi chạy:**

```text
[[ 8  9 10]
 [ 7  8  9]]
```

**Kết quả:** Xem ngay giá trị bên dưới đoạn code để biết phép tính đã thực hiện gì.

### Tình huống 4 — Nhân các kênh cảm biến

**Từ vựng trong mục:** **Vectorization** — vector hóa.

**Tình huống thực tế:** Ba kênh cảm biến có tín hiệu `[10,20,30]` và hệ số hiệu chỉnh `[1.0,0.5,2.0]`. Tính tín hiệu sau hiệu chỉnh theo từng kênh.

**Vì sao chọn cách giải này?** Nhân hai mảng cùng chiều để nhân từng cặp phần tử tương ứng.

**Quy trình giải:** Lưu dữ liệu đúng thứ tự hàng/cột → dùng phép NumPy phù hợp → in và giải thích kết quả.

```python
import numpy as np
signals=np.array([10,20,30])
factors=np.array([1.0,0.5,2.0])
print(signals*factors)
```

**Kết quả khi chạy:**

```text
[10. 10. 60.]
```

**Kết quả:** Xem ngay giá trị bên dưới đoạn code để biết phép tính đã thực hiện gì.

### Tình huống 5 — Tìm giá trị cao nhất theo cột

**Từ vựng trong mục:** **Aggregate** — phép tổng hợp.

**Tình huống thực tế:** Bảng hai cột số đo có ba hàng `(2,4)`, `(5,1)`, `(3,6)`. Lấy giá trị cao nhất của mỗi cột.

**Vì sao chọn cách giải này?** `max(axis=0)` lấy cực đại theo cột.

**Quy trình giải:** Lưu dữ liệu đúng thứ tự hàng/cột → dùng phép NumPy phù hợp → in và giải thích kết quả.

```python
import numpy as np
X=np.array([[2,4],[5,1],[3,6]])
print(X.max(axis=0))
```

**Kết quả khi chạy:**

```text
[5 6]
```

**Kết quả:** Xem ngay giá trị bên dưới đoạn code để biết phép tính đã thực hiện gì.

## 6. Sai lầm thường gặp

Các tham số như axis, shape, dtype hoặc cách xử lý giá trị thiếu có thể thay đổi kết quả. Trước khi xử lý phải biết số hàng, số cột, đơn vị và mục đích của từng phép biến đổi.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.


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

## 8. Nối bài tiếp theo

`Index/Slice → Aggregate/Broadcast → Vectorization → AI`.

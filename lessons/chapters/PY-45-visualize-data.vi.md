# PY-45 — Matplotlib: biểu đồ line, scatter và histogram


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Line chart** — biểu đồ đường; **Scatter plot** — biểu đồ phân tán.

`NumPy/Pandas → Visualization → EDA → PCA/ML`

Bài này hệ thống hóa kiến thức đã học thành các thao tác thực hành có đầu vào và đầu ra rõ ràng.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Ý nghĩa |
|---|---|---|
| Line chart | biểu đồ đường | Biểu diễn thay đổi theo thứ tự thời gian |
| Scatter plot | biểu đồ phân tán | Mỗi cặp x,y tạo thành một điểm quan sát |
| Histogram | biểu đồ tần suất | Đếm số mẫu trong từng khoảng giá trị |
| Axis label | nhãn trục | Mô tả đại lượng và đơn vị trên trục |

## 3. Hàm và cách sử dụng

**Từ vựng trong mục:** **Function** — hàm; **Option** — tùy chọn.

| Cú pháp | Mục đích và lựa chọn |
|---|---|
| `plt.plot(x,y)` | Đường thay đổi theo thời gian; x,y có cùng số phần tử |
| `plt.scatter(x,y)` | Vẽ điểm từng mẫu từ hai đại lượng |
| `plt.hist(values,bins=...)` | Gom quan sát vào các khoảng (bins) |
| `plt.xlabel()/ylabel()/savefig()` | Ghi nhãn kèm đơn vị và lưu hình |

## 4. Khái niệm liên quan và ví dụ nhỏ

### 4.1. Line chart

**Từ vựng trong mục:** **Line chart** — biểu đồ đường.

Biểu diễn thay đổi theo thứ tự thời gian. Dưới đây là thao tác tối giản trước khi kết hợp vào bài toán lớn hơn.

```python
import matplotlib.pyplot as plt
plt.plot([1,2,3],[2,3,5]);plt.close()
```

**Tự kiểm tra:** Line chart nghĩa là gì? **Đáp án:** Biểu diễn thay đổi theo thứ tự thời gian.

### 4.2. Scatter plot

**Từ vựng trong mục:** **Scatter plot** — biểu đồ phân tán.

Mỗi cặp x,y tạo thành một điểm quan sát. Dưới đây là thao tác tối giản trước khi kết hợp vào bài toán lớn hơn.

```python
import matplotlib.pyplot as plt
plt.scatter([1,2],[3,4]);plt.close()
```

**Tự kiểm tra:** Scatter plot nghĩa là gì? **Đáp án:** Mỗi cặp x,y tạo thành một điểm quan sát.

### 4.3. Histogram

**Từ vựng trong mục:** **Histogram** — biểu đồ tần suất.

Đếm số mẫu trong từng khoảng giá trị. Dưới đây là thao tác tối giản trước khi kết hợp vào bài toán lớn hơn.

```python
import matplotlib.pyplot as plt
plt.hist([1,1,2,3]);plt.close()
```

**Tự kiểm tra:** Histogram nghĩa là gì? **Đáp án:** Đếm số mẫu trong từng khoảng giá trị.

### 4.4. Axis label

**Từ vựng trong mục:** **Axis label** — nhãn trục.

Mô tả đại lượng và đơn vị trên trục. Dưới đây là thao tác tối giản trước khi kết hợp vào bài toán lớn hơn.

```python
import matplotlib.pyplot as plt
plt.xlabel('Time (s)');plt.close()
```

**Tự kiểm tra:** Axis label nghĩa là gì? **Đáp án:** Mô tả đại lượng và đơn vị trên trục.

## 5. Năm tình huống thực tế

### Tình huống 1 — Doanh thu ba ngày

**Từ vựng trong mục:** **Line chart** — biểu đồ đường.

**Bài toán:** Doanh thu ba ngày.

**Vì sao chọn cách này?** Line chart tốt cho xu hướng theo thời gian; giải pháp phải khớp đúng bối cảnh và phạm vi dữ liệu.

**Dữ liệu:** 3 ngày, doanh thu nghìn đồng. Đây là tình huống học tập giả lập hoặc nguồn mẫu được nêu trong code.

**Quy trình:** Hiểu dữ liệu → chọn lệnh/hàm → thực hiện → kiểm chứng kết quả → ghi hạn chế.

```python
import matplotlib.pyplot as plt
plt.plot([1,2,3],[10,15,12]);plt.xlabel("Day");plt.ylabel("Revenue (thousand VND)");plt.close()
```

**Kiểm tra:** Đọc kết quả, các lỗi/trường hợp biên và cân nhắc trước khi dùng vào dự án thật.

### Tình huống 2 — Giờ học và điểm

**Từ vựng trong mục:** **Scatter plot** — biểu đồ phân tán.

**Bài toán:** Giờ học và điểm.

**Vì sao chọn cách này?** Scatter cho thấy từng sinh viên là một cặp số; giải pháp phải khớp đúng bối cảnh và phạm vi dữ liệu.

**Dữ liệu:** 3 SV, giờ/tuần và điểm/10. Đây là tình huống học tập giả lập hoặc nguồn mẫu được nêu trong code.

**Quy trình:** Hiểu dữ liệu → chọn lệnh/hàm → thực hiện → kiểm chứng kết quả → ghi hạn chế.

```python
import matplotlib.pyplot as plt
plt.scatter([2,4,6],[5,7,9]);plt.xlabel("Hours/week");plt.ylabel("Score");plt.close()
```

**Kiểm tra:** Đọc kết quả, các lỗi/trường hợp biên và cân nhắc trước khi dùng vào dự án thật.

### Tình huống 3 — Phân bố điểm thi

**Từ vựng trong mục:** **Histogram** — biểu đồ tần suất.

**Bài toán:** Phân bố điểm thi.

**Vì sao chọn cách này?** Histogram đếm số SV theo dải điểm; giải pháp phải khớp đúng bối cảnh và phạm vi dữ liệu.

**Dữ liệu:** 6 điểm trên thang 10. Đây là tình huống học tập giả lập hoặc nguồn mẫu được nêu trong code.

**Quy trình:** Hiểu dữ liệu → chọn lệnh/hàm → thực hiện → kiểm chứng kết quả → ghi hạn chế.

```python
import matplotlib.pyplot as plt
plt.hist([5,6,6,7,8,9],bins=5);plt.xlabel("Score");plt.ylabel("Students");plt.close()
```

**Kiểm tra:** Đọc kết quả, các lỗi/trường hợp biên và cân nhắc trước khi dùng vào dự án thật.

### Tình huống 4 — Lưu biểu đồ PNG

**Từ vựng trong mục:** **Axis label** — nhãn trục.

**Bài toán:** Lưu biểu đồ PNG.

**Vì sao chọn cách này?** savefig tạo tài liệu không cần màn hình tương tác; giải pháp phải khớp đúng bối cảnh và phạm vi dữ liệu.

**Dữ liệu:** Dữ liệu hai tháng. Đây là tình huống học tập giả lập hoặc nguồn mẫu được nêu trong code.

**Quy trình:** Hiểu dữ liệu → chọn lệnh/hàm → thực hiện → kiểm chứng kết quả → ghi hạn chế.

```python
import matplotlib.pyplot as plt
from tempfile import TemporaryDirectory
from pathlib import Path
with TemporaryDirectory() as d:
    plt.plot([1,2],[10,15]);plt.savefig(Path(d)/"chart.png");plt.close()
    print((Path(d)/"chart.png").is_file())
```

**Kiểm tra:** Đọc kết quả, các lỗi/trường hợp biên và cân nhắc trước khi dùng vào dự án thật.

### Tình huống 5 — Đặt nhãn đọc được

**Từ vựng trong mục:** **Line chart** — biểu đồ đường.

**Bài toán:** Đặt nhãn đọc được.

**Vì sao chọn cách này?** Nhãn giúp không nhầm giá trị x/y và đơn vị; giải pháp phải khớp đúng bối cảnh và phạm vi dữ liệu.

**Dữ liệu:** 3 điểm thời gian–nhiệt độ. Đây là tình huống học tập giả lập hoặc nguồn mẫu được nêu trong code.

**Quy trình:** Hiểu dữ liệu → chọn lệnh/hàm → thực hiện → kiểm chứng kết quả → ghi hạn chế.

```python
import matplotlib.pyplot as plt
plt.plot([1,2,3],[22,24,23]);plt.xlabel("Time (hours)");plt.ylabel("Temperature (C)");plt.close()
```

**Kiểm tra:** Đọc kết quả, các lỗi/trường hợp biên và cân nhắc trước khi dùng vào dự án thật.

## 6. Nhầm lẫn cần tránh

Đừng sao chép lệnh khi chưa hiểu dữ liệu hoặc trạng thái môi trường; kết quả thử nghiệm không chứng minh rằng mọi máy và mọi bộ dữ liệu đều giống nhau.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer key** — bảng đáp án.


**Q1. What is Line chart? — Thuật ngữ Line chart là gì?**

A. Another term is Mỗi cặp x,y tạo thành một điểm quan sát — Mỗi cặp x,y tạo thành một điểm quan sát

B. It is Biểu diễn thay đổi theo thứ tự thời gian — Biểu diễn thay đổi theo thứ tự thời gian

C. Another term is Đếm số mẫu trong từng khoảng giá trị — Đếm số mẫu trong từng khoảng giá trị

D. Another term is Mô tả đại lượng và đơn vị trên trục — Mô tả đại lượng và đơn vị trên trục


**Q2. What is Scatter plot? — Thuật ngữ Scatter plot là gì?**

A. It is Mỗi cặp x,y tạo thành một điểm quan sát — Mỗi cặp x,y tạo thành một điểm quan sát

B. Another term is Đếm số mẫu trong từng khoảng giá trị — Đếm số mẫu trong từng khoảng giá trị

C. Another term is Mô tả đại lượng và đơn vị trên trục — Mô tả đại lượng và đơn vị trên trục

D. Another term is Biểu diễn thay đổi theo thứ tự thời gian — Biểu diễn thay đổi theo thứ tự thời gian


**Q3. What is Histogram? — Thuật ngữ Histogram là gì?**

A. Another term is Mô tả đại lượng và đơn vị trên trục — Mô tả đại lượng và đơn vị trên trục

B. Another term is Biểu diễn thay đổi theo thứ tự thời gian — Biểu diễn thay đổi theo thứ tự thời gian

C. Another term is Mỗi cặp x,y tạo thành một điểm quan sát — Mỗi cặp x,y tạo thành một điểm quan sát

D. It is Đếm số mẫu trong từng khoảng giá trị — Đếm số mẫu trong từng khoảng giá trị


**Q4. What is Axis label? — Thuật ngữ Axis label là gì?**

A. Another term is Biểu diễn thay đổi theo thứ tự thời gian — Biểu diễn thay đổi theo thứ tự thời gian

B. Another term is Mỗi cặp x,y tạo thành một điểm quan sát — Mỗi cặp x,y tạo thành một điểm quan sát

C. It is Mô tả đại lượng và đơn vị trên trục — Mô tả đại lượng và đơn vị trên trục

D. Another term is Đếm số mẫu trong từng khoảng giá trị — Đếm số mẫu trong từng khoảng giá trị


**Q5. What is plt.plot(x,y) used for? — Cú pháp plt.plot(x,y) dùng để làm gì?**

A. A different function is for Vẽ điểm từng mẫu từ hai đại lượng — Vẽ điểm từng mẫu từ hai đại lượng

B. It is for Đường thay đổi theo thời gian; x,y có cùng số phần tử — Đường thay đổi theo thời gian; x,y có cùng số phần tử

C. A different function is for Gom quan sát vào các khoảng (bins) — Gom quan sát vào các khoảng (bins)

D. A different function is for Ghi nhãn kèm đơn vị và lưu hình — Ghi nhãn kèm đơn vị và lưu hình


**Q6. What is plt.scatter(x,y) used for? — Cú pháp plt.scatter(x,y) dùng để làm gì?**

A. It is for Vẽ điểm từng mẫu từ hai đại lượng — Vẽ điểm từng mẫu từ hai đại lượng

B. A different function is for Gom quan sát vào các khoảng (bins) — Gom quan sát vào các khoảng (bins)

C. A different function is for Ghi nhãn kèm đơn vị và lưu hình — Ghi nhãn kèm đơn vị và lưu hình

D. A different function is for Đường thay đổi theo thời gian; x,y có cùng số phần tử — Đường thay đổi theo thời gian; x,y có cùng số phần tử


**Q7. What is plt.hist(values,bins=...) used for? — Cú pháp plt.hist(values,bins=...) dùng để làm gì?**

A. A different function is for Ghi nhãn kèm đơn vị và lưu hình — Ghi nhãn kèm đơn vị và lưu hình

B. A different function is for Đường thay đổi theo thời gian; x,y có cùng số phần tử — Đường thay đổi theo thời gian; x,y có cùng số phần tử

C. A different function is for Vẽ điểm từng mẫu từ hai đại lượng — Vẽ điểm từng mẫu từ hai đại lượng

D. It is for Gom quan sát vào các khoảng (bins) — Gom quan sát vào các khoảng (bins)


**Q8. What is plt.xlabel()/ylabel()/savefig() used for? — Cú pháp plt.xlabel()/ylabel()/savefig() dùng để làm gì?**

A. A different function is for Đường thay đổi theo thời gian; x,y có cùng số phần tử — Đường thay đổi theo thời gian; x,y có cùng số phần tử

B. A different function is for Vẽ điểm từng mẫu từ hai đại lượng — Vẽ điểm từng mẫu từ hai đại lượng

C. It is for Ghi nhãn kèm đơn vị và lưu hình — Ghi nhãn kèm đơn vị và lưu hình

D. A different function is for Gom quan sát vào các khoảng (bins) — Gom quan sát vào các khoảng (bins)


**Q9. Why choose this approach in scenario 1? — Vì sao chọn cách làm trong tình huống 1?**

A. Scatter cho thấy từng sinh viên là một cặp số — Scatter cho thấy từng sinh viên là một cặp số

B. Line chart tốt cho xu hướng theo thời gian — Line chart tốt cho xu hướng theo thời gian

C. Histogram đếm số SV theo dải điểm — Histogram đếm số SV theo dải điểm

D. savefig tạo tài liệu không cần màn hình tương tác — savefig tạo tài liệu không cần màn hình tương tác


**Q10. Why choose this approach in scenario 2? — Vì sao chọn cách làm trong tình huống 2?**

A. Scatter cho thấy từng sinh viên là một cặp số — Scatter cho thấy từng sinh viên là một cặp số

B. Histogram đếm số SV theo dải điểm — Histogram đếm số SV theo dải điểm

C. savefig tạo tài liệu không cần màn hình tương tác — savefig tạo tài liệu không cần màn hình tương tác

D. Nhãn giúp không nhầm giá trị x/y và đơn vị — Nhãn giúp không nhầm giá trị x/y và đơn vị


**Q11. Why choose this approach in scenario 3? — Vì sao chọn cách làm trong tình huống 3?**

A. savefig tạo tài liệu không cần màn hình tương tác — savefig tạo tài liệu không cần màn hình tương tác

B. Nhãn giúp không nhầm giá trị x/y và đơn vị — Nhãn giúp không nhầm giá trị x/y và đơn vị

C. Line chart tốt cho xu hướng theo thời gian — Line chart tốt cho xu hướng theo thời gian

D. Histogram đếm số SV theo dải điểm — Histogram đếm số SV theo dải điểm


**Q12. Why choose this approach in scenario 4? — Vì sao chọn cách làm trong tình huống 4?**

A. Nhãn giúp không nhầm giá trị x/y và đơn vị — Nhãn giúp không nhầm giá trị x/y và đơn vị

B. Line chart tốt cho xu hướng theo thời gian — Line chart tốt cho xu hướng theo thời gian

C. savefig tạo tài liệu không cần màn hình tương tác — savefig tạo tài liệu không cần màn hình tương tác

D. Scatter cho thấy từng sinh viên là một cặp số — Scatter cho thấy từng sinh viên là một cặp số


**Q13. Why choose this approach in scenario 5? — Vì sao chọn cách làm trong tình huống 5?**

A. Line chart tốt cho xu hướng theo thời gian — Line chart tốt cho xu hướng theo thời gian

B. Nhãn giúp không nhầm giá trị x/y và đơn vị — Nhãn giúp không nhầm giá trị x/y và đơn vị

C. Scatter cho thấy từng sinh viên là một cặp số — Scatter cho thấy từng sinh viên là một cặp số

D. Histogram đếm số SV theo dải điểm — Histogram đếm số SV theo dải điểm


**Q14. What input is used in scenario 1? — Tình huống 1 sử dụng đầu vào nào?**

A. 3 ngày, doanh thu nghìn đồng — 3 ngày, doanh thu nghìn đồng

B. 3 SV, giờ/tuần và điểm/10 — 3 SV, giờ/tuần và điểm/10

C. 6 điểm trên thang 10 — 6 điểm trên thang 10

D. Dữ liệu hai tháng — Dữ liệu hai tháng


**Q15. What input is used in scenario 2? — Tình huống 2 sử dụng đầu vào nào?**

A. 6 điểm trên thang 10 — 6 điểm trên thang 10

B. Dữ liệu hai tháng — Dữ liệu hai tháng

C. 3 điểm thời gian–nhiệt độ — 3 điểm thời gian–nhiệt độ

D. 3 SV, giờ/tuần và điểm/10 — 3 SV, giờ/tuần và điểm/10


**Q16. What input is used in scenario 3? — Tình huống 3 sử dụng đầu vào nào?**

A. Dữ liệu hai tháng — Dữ liệu hai tháng

B. 3 điểm thời gian–nhiệt độ — 3 điểm thời gian–nhiệt độ

C. 6 điểm trên thang 10 — 6 điểm trên thang 10

D. 3 ngày, doanh thu nghìn đồng — 3 ngày, doanh thu nghìn đồng


**Q17. What input is used in scenario 4? — Tình huống 4 sử dụng đầu vào nào?**

A. 3 điểm thời gian–nhiệt độ — 3 điểm thời gian–nhiệt độ

B. Dữ liệu hai tháng — Dữ liệu hai tháng

C. 3 ngày, doanh thu nghìn đồng — 3 ngày, doanh thu nghìn đồng

D. 3 SV, giờ/tuần và điểm/10 — 3 SV, giờ/tuần và điểm/10


**Q18. What input is used in scenario 5? — Tình huống 5 sử dụng đầu vào nào?**

A. 3 điểm thời gian–nhiệt độ — 3 điểm thời gian–nhiệt độ

B. 3 ngày, doanh thu nghìn đồng — 3 ngày, doanh thu nghìn đồng

C. 3 SV, giờ/tuần và điểm/10 — 3 SV, giờ/tuần và điểm/10

D. 6 điểm trên thang 10 — 6 điểm trên thang 10


**Q19. What is important before executing a workflow? — Trước khi chạy workflow cần điều gì?**

A. Only count blank lines — Chỉ đếm dòng trắng

B. Only change editor theme — Chỉ đổi giao diện

C. Ignore credentials — Bỏ qua quản lý tài khoản

D. Understand source, parameters and permissions — Hiểu nguồn, tham số và quyền hạn


**Q20. What should be reported after a test? — Sau khi test cần báo cáo gì?**

A. Only a success claim — Chỉ nói thành công

B. A guess of future results — Đoán kết quả tương lai

C. Observed output, failures and limits — Đầu ra thật, lỗi và giới hạn

D. No evidence — Không cần bằng chứng

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **B** | It is Biểu diễn thay đổi theo thứ tự thời gian | Biểu diễn thay đổi theo thứ tự thời gian |
| Q2 | **A** | It is Mỗi cặp x,y tạo thành một điểm quan sát | Mỗi cặp x,y tạo thành một điểm quan sát |
| Q3 | **D** | It is Đếm số mẫu trong từng khoảng giá trị | Đếm số mẫu trong từng khoảng giá trị |
| Q4 | **C** | It is Mô tả đại lượng và đơn vị trên trục | Mô tả đại lượng và đơn vị trên trục |
| Q5 | **B** | It is for Đường thay đổi theo thời gian; x,y có cùng số phần tử | Đường thay đổi theo thời gian; x,y có cùng số phần tử |
| Q6 | **A** | It is for Vẽ điểm từng mẫu từ hai đại lượng | Vẽ điểm từng mẫu từ hai đại lượng |
| Q7 | **D** | It is for Gom quan sát vào các khoảng (bins) | Gom quan sát vào các khoảng (bins) |
| Q8 | **C** | It is for Ghi nhãn kèm đơn vị và lưu hình | Ghi nhãn kèm đơn vị và lưu hình |
| Q9 | **B** | Line chart tốt cho xu hướng theo thời gian | Line chart tốt cho xu hướng theo thời gian |
| Q10 | **A** | Scatter cho thấy từng sinh viên là một cặp số | Scatter cho thấy từng sinh viên là một cặp số |
| Q11 | **D** | Histogram đếm số SV theo dải điểm | Histogram đếm số SV theo dải điểm |
| Q12 | **C** | savefig tạo tài liệu không cần màn hình tương tác | savefig tạo tài liệu không cần màn hình tương tác |
| Q13 | **B** | Nhãn giúp không nhầm giá trị x/y và đơn vị | Nhãn giúp không nhầm giá trị x/y và đơn vị |
| Q14 | **A** | 3 ngày, doanh thu nghìn đồng | 3 ngày, doanh thu nghìn đồng |
| Q15 | **D** | 3 SV, giờ/tuần và điểm/10 | 3 SV, giờ/tuần và điểm/10 |
| Q16 | **C** | 6 điểm trên thang 10 | 6 điểm trên thang 10 |
| Q17 | **B** | Dữ liệu hai tháng | Dữ liệu hai tháng |
| Q18 | **A** | 3 điểm thời gian–nhiệt độ | 3 điểm thời gian–nhiệt độ |
| Q19 | **D** | Understand source, parameters and permissions | Hiểu nguồn, tham số và quyền hạn |
| Q20 | **C** | Observed output, failures and limits | Đầu ra thật, lỗi và giới hạn |

## 8. Nối sang bài tiếp

`NumPy/Pandas → Visualization → EDA → PCA/ML`.

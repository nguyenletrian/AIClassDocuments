# PY-19 — Pandas: lọc, groupby, merge và sắp xếp


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **loc** — chọn theo nhãn; **iloc** — chọn theo vị trí.

`DataFrame → lọc → nhóm → ghép bảng → AI`

Bài học giúp sinh viên nhìn rõ quan hệ giữa kiến thức trước và cách xử lý dữ liệu để ứng dụng AI sau này.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Giải thích |
|---|---|---|
| loc | chọn theo nhãn | Chọn hàng/cột theo tên |
| iloc | chọn theo vị trí | Chọn hàng/cột theo số nguyên tính từ 0 |
| groupby | nhóm dữ liệu | Gom các hàng cùng giá trị để tổng hợp |
| merge | ghép bảng | Nối bảng qua khóa chung |

## 3. Hàm Python và tham số

**Từ vựng trong mục:** **Function** — hàm; **Parameter** — tham số.

| Hàm / cú pháp | Vì sao dùng |
|---|---|
| `df.loc[label]` | Chọn theo nhãn dòng/cột; slicing theo nhãn có thể gồm điểm cuối |
| `df.iloc[position]` | Chọn theo vị trí; stop của slice không bao gồm |
| `df.groupby(key).agg()` | Gộp nhóm rồi tính tổng/trung bình/số dòng |
| `pd.merge(left,right,on=,how=)` | Ghép theo khóa, cách inner/left/right/outer khác nhau |

## 4. Các khái niệm liên quan

### 4.1. loc

**Từ vựng trong mục:** **loc** — chọn theo nhãn.

Chọn hàng/cột theo tên. Đọc khái niệm trước rồi kiểm tra bằng ví dụ Python nhỏ.

```python
import pandas as pd
x=pd.DataFrame({"score":[8]},index=["SV1"])
print(x.loc["SV1"])
```

**Tự kiểm tra nhanh:** loc là gì? **Đáp án:** Chọn hàng/cột theo tên.

### 4.2. iloc

**Từ vựng trong mục:** **iloc** — chọn theo vị trí.

Chọn hàng/cột theo số nguyên tính từ 0. Đọc khái niệm trước rồi kiểm tra bằng ví dụ Python nhỏ.

```python
import pandas as pd
x=pd.DataFrame({"score":[8,9]})
print(x.iloc[1])
```

**Tự kiểm tra nhanh:** iloc là gì? **Đáp án:** Chọn hàng/cột theo số nguyên tính từ 0.

### 4.3. groupby

**Từ vựng trong mục:** **groupby** — nhóm dữ liệu.

Gom các hàng cùng giá trị để tổng hợp. Đọc khái niệm trước rồi kiểm tra bằng ví dụ Python nhỏ.

```python
import pandas as pd
x=pd.DataFrame({"city":["A","A"],"sale":[2,3]})
print(x.groupby("city").sale.sum())
```

**Tự kiểm tra nhanh:** groupby là gì? **Đáp án:** Gom các hàng cùng giá trị để tổng hợp.

### 4.4. merge

**Từ vựng trong mục:** **merge** — ghép bảng.

Nối bảng qua khóa chung. Đọc khái niệm trước rồi kiểm tra bằng ví dụ Python nhỏ.

```python
import pandas as pd
a=pd.DataFrame({"id":[1],"x":[2]});b=pd.DataFrame({"id":[1],"y":[3]})
print(a.merge(b,on="id"))
```

**Tự kiểm tra nhanh:** merge là gì? **Đáp án:** Nối bảng qua khóa chung.

## 5. Năm vấn đề thực tế

### Tình huống 1 — Đơn hàng giá cao

**Từ vựng trong mục:** **loc** — chọn theo nhãn.

**Tình huống thực tế:** Một doanh nghiệp bán lẻ muốn đơn hàng giá cao. Bộ dữ liệu đang có: 3 sản phẩm, giá nghìn đồng. Đầu vào minh họa; nếu dùng bảng, mỗi hàng là một đối tượng và cột là đặc trưng cụ thể. Hãy lập trình giải quyết yêu cầu này và đưa ra kết quả có thể kiểm tra.

**Vì sao chọn phương án này?** Lọc dựa trên cột đơn giá để lấy bản ghi phù hợp. Đừng chọn thuật toán AI khi chỉ cần thống kê hay quy tắc rõ ràng.


**Quy trình:** Đọc dữ liệu → chọn phương pháp → triển khai → đọc kết quả → kiểm tra trường hợp biên.

```python
import pandas as pd
df=pd.DataFrame({"name":["A","B","C"],"price":[300,900,1200]})
print(df[df.price>=800])
```

**Đọc kết quả:** Giải thích ý nghĩa đầu ra và thử thay một dữ liệu để quan sát kết quả.

### Tình huống 2 — Tra dòng thứ hai

**Từ vựng trong mục:** **iloc** — chọn theo vị trí.

**Tình huống thực tế:** Một tổ chức đang triển khai hệ thống dữ liệu muốn tra dòng thứ hai. Bộ dữ liệu đang có: Ba ID theo thứ tự A B C. Đầu vào minh họa; nếu dùng bảng, mỗi hàng là một đối tượng và cột là đặc trưng cụ thể. Hãy lập trình giải quyết yêu cầu này và đưa ra kết quả có thể kiểm tra.

**Vì sao chọn phương án này?** iloc dùng vị trí thay vì tên index. Đừng chọn thuật toán AI khi chỉ cần thống kê hay quy tắc rõ ràng.


**Quy trình:** Đọc dữ liệu → chọn phương pháp → triển khai → đọc kết quả → kiểm tra trường hợp biên.

```python
import pandas as pd
df=pd.DataFrame({"id":["A","B","C"]})
print(df.iloc[1])
```

**Đọc kết quả:** Giải thích ý nghĩa đầu ra và thử thay một dữ liệu để quan sát kết quả.

### Tình huống 3 — Doanh thu từng vùng

**Từ vựng trong mục:** **groupby** — nhóm dữ liệu.

**Tình huống thực tế:** Một doanh nghiệp bán lẻ muốn doanh thu từng vùng. Bộ dữ liệu đang có: 3 đơn A A B, nghìn đồng. Đầu vào minh họa; nếu dùng bảng, mỗi hàng là một đối tượng và cột là đặc trưng cụ thể. Hãy lập trình giải quyết yêu cầu này và đưa ra kết quả có thể kiểm tra.

**Vì sao chọn phương án này?** groupby theo city rồi sum tránh cộng chung toàn quốc. Đừng chọn thuật toán AI khi chỉ cần thống kê hay quy tắc rõ ràng.


**Quy trình:** Đọc dữ liệu → chọn phương pháp → triển khai → đọc kết quả → kiểm tra trường hợp biên.

```python
import pandas as pd
df=pd.DataFrame({"city":["A","A","B"],"sale":[10,20,8]})
print(df.groupby("city")["sale"].sum())
```

**Đọc kết quả:** Giải thích ý nghĩa đầu ra và thử thay một dữ liệu để quan sát kết quả.

### Tình huống 4 — Đơn hàng và khách

**Từ vựng trong mục:** **merge** — ghép bảng.

**Tình huống thực tế:** Một doanh nghiệp bán lẻ muốn đơn hàng và khách. Bộ dữ liệu đang có: Hai bảng order/customer. Đầu vào minh họa; nếu dùng bảng, mỗi hàng là một đối tượng và cột là đặc trưng cụ thể. Hãy lập trình giải quyết yêu cầu này và đưa ra kết quả có thể kiểm tra.

**Vì sao chọn phương án này?** merge trên customer_id giữ quan hệ ID đúng. Đừng chọn thuật toán AI khi chỉ cần thống kê hay quy tắc rõ ràng.


**Quy trình:** Đọc dữ liệu → chọn phương pháp → triển khai → đọc kết quả → kiểm tra trường hợp biên.

```python
import pandas as pd
a=pd.DataFrame({"id":[1,2],"sale":[10,20]})
b=pd.DataFrame({"id":[1,2],"name":["An","Lan"]})
print(a.merge(b,on="id",how="left"))
```

**Đọc kết quả:** Giải thích ý nghĩa đầu ra và thử thay một dữ liệu để quan sát kết quả.

### Tình huống 5 — Top doanh số

**Từ vựng trong mục:** **loc** — chọn theo nhãn.

**Tình huống thực tế:** Một tổ chức đang triển khai hệ thống dữ liệu muốn top doanh số. Bộ dữ liệu đang có: 4 đơn với doanh thu nghìn đồng. Đầu vào minh họa; nếu dùng bảng, mỗi hàng là một đối tượng và cột là đặc trưng cụ thể. Hãy lập trình giải quyết yêu cầu này và đưa ra kết quả có thể kiểm tra.

**Vì sao chọn phương án này?** sort_values theo revenue rồi head lấy hai dòng đầu. Đừng chọn thuật toán AI khi chỉ cần thống kê hay quy tắc rõ ràng.


**Quy trình:** Đọc dữ liệu → chọn phương pháp → triển khai → đọc kết quả → kiểm tra trường hợp biên.

```python
import pandas as pd
df=pd.DataFrame({"id":["A","B","C","D"],"sale":[30,80,20,60]})
print(df.sort_values("sale",ascending=False).head(2))
```

**Đọc kết quả:** Giải thích ý nghĩa đầu ra và thử thay một dữ liệu để quan sát kết quả.

## 6. Các lỗi dễ mắc

Cần phân biệt khi nào thứ tự quan trọng, khi nào phần tử trùng được tính lại, và khi nào dữ liệu thật không có đủ điều kiện như ví dụ. Xem kỹ kiểu dữ liệu và đầu vào trống.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.


**Q1. What best describes loc? — Mô tả nào đúng với loc?**

A. A different idea is Chọn hàng/cột theo số nguyên tính từ 0 — Chọn hàng/cột theo số nguyên tính từ 0

B. It is Chọn hàng/cột theo tên — Chọn hàng/cột theo tên

C. A different idea is Gom các hàng cùng giá trị để tổng hợp — Gom các hàng cùng giá trị để tổng hợp

D. A different idea is Nối bảng qua khóa chung — Nối bảng qua khóa chung


**Q2. What best describes iloc? — Mô tả nào đúng với iloc?**

A. It is Chọn hàng/cột theo số nguyên tính từ 0 — Chọn hàng/cột theo số nguyên tính từ 0

B. A different idea is Gom các hàng cùng giá trị để tổng hợp — Gom các hàng cùng giá trị để tổng hợp

C. A different idea is Nối bảng qua khóa chung — Nối bảng qua khóa chung

D. A different idea is Chọn hàng/cột theo tên — Chọn hàng/cột theo tên


**Q3. What best describes groupby? — Mô tả nào đúng với groupby?**

A. A different idea is Nối bảng qua khóa chung — Nối bảng qua khóa chung

B. A different idea is Chọn hàng/cột theo tên — Chọn hàng/cột theo tên

C. A different idea is Chọn hàng/cột theo số nguyên tính từ 0 — Chọn hàng/cột theo số nguyên tính từ 0

D. It is Gom các hàng cùng giá trị để tổng hợp — Gom các hàng cùng giá trị để tổng hợp


**Q4. What best describes merge? — Mô tả nào đúng với merge?**

A. A different idea is Chọn hàng/cột theo tên — Chọn hàng/cột theo tên

B. A different idea is Chọn hàng/cột theo số nguyên tính từ 0 — Chọn hàng/cột theo số nguyên tính từ 0

C. It is Nối bảng qua khóa chung — Nối bảng qua khóa chung

D. A different idea is Gom các hàng cùng giá trị để tổng hợp — Gom các hàng cùng giá trị để tổng hợp


**Q5. Which operation matches df.loc[label]? — Mục đích của df.loc[label] là gì?**

A. Another operation is used to Chọn theo vị trí; stop của slice không bao gồm — Chọn theo vị trí; stop của slice không bao gồm

B. It is used to Chọn theo nhãn dòng/cột; slicing theo nhãn có thể gồm điểm cuối — Chọn theo nhãn dòng/cột; slicing theo nhãn có thể gồm điểm cuối

C. Another operation is used to Gộp nhóm rồi tính tổng/trung bình/số dòng — Gộp nhóm rồi tính tổng/trung bình/số dòng

D. Another operation is used to Ghép theo khóa, cách inner/left/right/outer khác nhau — Ghép theo khóa, cách inner/left/right/outer khác nhau


**Q6. Which operation matches df.iloc[position]? — Mục đích của df.iloc[position] là gì?**

A. It is used to Chọn theo vị trí; stop của slice không bao gồm — Chọn theo vị trí; stop của slice không bao gồm

B. Another operation is used to Gộp nhóm rồi tính tổng/trung bình/số dòng — Gộp nhóm rồi tính tổng/trung bình/số dòng

C. Another operation is used to Ghép theo khóa, cách inner/left/right/outer khác nhau — Ghép theo khóa, cách inner/left/right/outer khác nhau

D. Another operation is used to Chọn theo nhãn dòng/cột; slicing theo nhãn có thể gồm điểm cuối — Chọn theo nhãn dòng/cột; slicing theo nhãn có thể gồm điểm cuối


**Q7. Which operation matches df.groupby(key).agg()? — Mục đích của df.groupby(key).agg() là gì?**

A. Another operation is used to Ghép theo khóa, cách inner/left/right/outer khác nhau — Ghép theo khóa, cách inner/left/right/outer khác nhau

B. Another operation is used to Chọn theo nhãn dòng/cột; slicing theo nhãn có thể gồm điểm cuối — Chọn theo nhãn dòng/cột; slicing theo nhãn có thể gồm điểm cuối

C. Another operation is used to Chọn theo vị trí; stop của slice không bao gồm — Chọn theo vị trí; stop của slice không bao gồm

D. It is used to Gộp nhóm rồi tính tổng/trung bình/số dòng — Gộp nhóm rồi tính tổng/trung bình/số dòng


**Q8. Which operation matches pd.merge(left,right,on=,how=)? — Mục đích của pd.merge(left,right,on=,how=) là gì?**

A. Another operation is used to Chọn theo nhãn dòng/cột; slicing theo nhãn có thể gồm điểm cuối — Chọn theo nhãn dòng/cột; slicing theo nhãn có thể gồm điểm cuối

B. Another operation is used to Chọn theo vị trí; stop của slice không bao gồm — Chọn theo vị trí; stop của slice không bao gồm

C. It is used to Ghép theo khóa, cách inner/left/right/outer khác nhau — Ghép theo khóa, cách inner/left/right/outer khác nhau

D. Another operation is used to Gộp nhóm rồi tính tổng/trung bình/số dòng — Gộp nhóm rồi tính tổng/trung bình/số dòng


**Q9. Why was the method chosen for scenario 1? — Vì sao chọn cách giải của tình huống 1?**

A. Another reason is iloc dùng vị trí thay vì tên index — iloc dùng vị trí thay vì tên index

B. Because Lọc dựa trên cột đơn giá để lấy bản ghi phù hợp — Lọc dựa trên cột đơn giá để lấy bản ghi phù hợp

C. Another reason is groupby theo city rồi sum tránh cộng chung toàn quốc — groupby theo city rồi sum tránh cộng chung toàn quốc

D. Another reason is merge trên customer_id giữ quan hệ ID đúng — merge trên customer_id giữ quan hệ ID đúng


**Q10. Why was the method chosen for scenario 2? — Vì sao chọn cách giải của tình huống 2?**

A. Because iloc dùng vị trí thay vì tên index — iloc dùng vị trí thay vì tên index

B. Another reason is groupby theo city rồi sum tránh cộng chung toàn quốc — groupby theo city rồi sum tránh cộng chung toàn quốc

C. Another reason is merge trên customer_id giữ quan hệ ID đúng — merge trên customer_id giữ quan hệ ID đúng

D. Another reason is sort_values theo revenue rồi head lấy hai dòng đầu — sort_values theo revenue rồi head lấy hai dòng đầu


**Q11. Why was the method chosen for scenario 3? — Vì sao chọn cách giải của tình huống 3?**

A. Another reason is merge trên customer_id giữ quan hệ ID đúng — merge trên customer_id giữ quan hệ ID đúng

B. Another reason is sort_values theo revenue rồi head lấy hai dòng đầu — sort_values theo revenue rồi head lấy hai dòng đầu

C. Another reason is Lọc dựa trên cột đơn giá để lấy bản ghi phù hợp — Lọc dựa trên cột đơn giá để lấy bản ghi phù hợp

D. Because groupby theo city rồi sum tránh cộng chung toàn quốc — groupby theo city rồi sum tránh cộng chung toàn quốc


**Q12. Why was the method chosen for scenario 4? — Vì sao chọn cách giải của tình huống 4?**

A. Another reason is sort_values theo revenue rồi head lấy hai dòng đầu — sort_values theo revenue rồi head lấy hai dòng đầu

B. Another reason is Lọc dựa trên cột đơn giá để lấy bản ghi phù hợp — Lọc dựa trên cột đơn giá để lấy bản ghi phù hợp

C. Because merge trên customer_id giữ quan hệ ID đúng — merge trên customer_id giữ quan hệ ID đúng

D. Another reason is iloc dùng vị trí thay vì tên index — iloc dùng vị trí thay vì tên index


**Q13. Why was the method chosen for scenario 5? — Vì sao chọn cách giải của tình huống 5?**

A. Another reason is Lọc dựa trên cột đơn giá để lấy bản ghi phù hợp — Lọc dựa trên cột đơn giá để lấy bản ghi phù hợp

B. Because sort_values theo revenue rồi head lấy hai dòng đầu — sort_values theo revenue rồi head lấy hai dòng đầu

C. Another reason is iloc dùng vị trí thay vì tên index — iloc dùng vị trí thay vì tên index

D. Another reason is groupby theo city rồi sum tránh cộng chung toàn quốc — groupby theo city rồi sum tránh cộng chung toàn quốc


**Q14. What input is used in scenario 1? — Tình huống 1 dùng dữ liệu gì?**

A. The data are 3 sản phẩm, giá nghìn đồng — 3 sản phẩm, giá nghìn đồng

B. Other data are Ba ID theo thứ tự A B C — Ba ID theo thứ tự A B C

C. Other data are 3 đơn A A B, nghìn đồng — 3 đơn A A B, nghìn đồng

D. Other data are Hai bảng order/customer — Hai bảng order/customer


**Q15. What input is used in scenario 2? — Tình huống 2 dùng dữ liệu gì?**

A. Other data are 3 đơn A A B, nghìn đồng — 3 đơn A A B, nghìn đồng

B. Other data are Hai bảng order/customer — Hai bảng order/customer

C. Other data are 4 đơn với doanh thu nghìn đồng — 4 đơn với doanh thu nghìn đồng

D. The data are Ba ID theo thứ tự A B C — Ba ID theo thứ tự A B C


**Q16. What input is used in scenario 3? — Tình huống 3 dùng dữ liệu gì?**

A. Other data are Hai bảng order/customer — Hai bảng order/customer

B. Other data are 4 đơn với doanh thu nghìn đồng — 4 đơn với doanh thu nghìn đồng

C. The data are 3 đơn A A B, nghìn đồng — 3 đơn A A B, nghìn đồng

D. Other data are 3 sản phẩm, giá nghìn đồng — 3 sản phẩm, giá nghìn đồng


**Q17. What input is used in scenario 4? — Tình huống 4 dùng dữ liệu gì?**

A. Other data are 4 đơn với doanh thu nghìn đồng — 4 đơn với doanh thu nghìn đồng

B. The data are Hai bảng order/customer — Hai bảng order/customer

C. Other data are 3 sản phẩm, giá nghìn đồng — 3 sản phẩm, giá nghìn đồng

D. Other data are Ba ID theo thứ tự A B C — Ba ID theo thứ tự A B C


**Q18. What input is used in scenario 5? — Tình huống 5 dùng dữ liệu gì?**

A. The data are 4 đơn với doanh thu nghìn đồng — 4 đơn với doanh thu nghìn đồng

B. Other data are 3 sản phẩm, giá nghìn đồng — 3 sản phẩm, giá nghìn đồng

C. Other data are Ba ID theo thứ tự A B C — Ba ID theo thứ tự A B C

D. Other data are 3 đơn A A B, nghìn đồng — 3 đơn A A B, nghìn đồng


**Q19. What information should a dataset have? — Dataset cần thông tin gì?**

A. Only a filename — Chỉ tên file

B. Only an editor font — Chỉ font soạn code

C. Only a line count — Chỉ số dòng

D. Meaning of rows, columns and units — Ý nghĩa hàng, cột và đơn vị


**Q20. After the program works, what comes next? — Sau khi code chạy đúng thì làm gì?**

A. Assume every input works — Cho rằng mọi đầu vào đều đúng

B. Erase validation — Xóa kiểm tra dữ liệu

C. Check the result and limitations — Kiểm tra kết quả và giới hạn

D. Ignore edge cases — Bỏ qua trường hợp biên

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **B** | It is Chọn hàng/cột theo tên | Chọn hàng/cột theo tên |
| Q2 | **A** | It is Chọn hàng/cột theo số nguyên tính từ 0 | Chọn hàng/cột theo số nguyên tính từ 0 |
| Q3 | **D** | It is Gom các hàng cùng giá trị để tổng hợp | Gom các hàng cùng giá trị để tổng hợp |
| Q4 | **C** | It is Nối bảng qua khóa chung | Nối bảng qua khóa chung |
| Q5 | **B** | It is used to Chọn theo nhãn dòng/cột; slicing theo nhãn có thể gồm điểm cuối | Chọn theo nhãn dòng/cột; slicing theo nhãn có thể gồm điểm cuối |
| Q6 | **A** | It is used to Chọn theo vị trí; stop của slice không bao gồm | Chọn theo vị trí; stop của slice không bao gồm |
| Q7 | **D** | It is used to Gộp nhóm rồi tính tổng/trung bình/số dòng | Gộp nhóm rồi tính tổng/trung bình/số dòng |
| Q8 | **C** | It is used to Ghép theo khóa, cách inner/left/right/outer khác nhau | Ghép theo khóa, cách inner/left/right/outer khác nhau |
| Q9 | **B** | Because Lọc dựa trên cột đơn giá để lấy bản ghi phù hợp | Lọc dựa trên cột đơn giá để lấy bản ghi phù hợp |
| Q10 | **A** | Because iloc dùng vị trí thay vì tên index | iloc dùng vị trí thay vì tên index |
| Q11 | **D** | Because groupby theo city rồi sum tránh cộng chung toàn quốc | groupby theo city rồi sum tránh cộng chung toàn quốc |
| Q12 | **C** | Because merge trên customer_id giữ quan hệ ID đúng | merge trên customer_id giữ quan hệ ID đúng |
| Q13 | **B** | Because sort_values theo revenue rồi head lấy hai dòng đầu | sort_values theo revenue rồi head lấy hai dòng đầu |
| Q14 | **A** | The data are 3 sản phẩm, giá nghìn đồng | 3 sản phẩm, giá nghìn đồng |
| Q15 | **D** | The data are Ba ID theo thứ tự A B C | Ba ID theo thứ tự A B C |
| Q16 | **C** | The data are 3 đơn A A B, nghìn đồng | 3 đơn A A B, nghìn đồng |
| Q17 | **B** | The data are Hai bảng order/customer | Hai bảng order/customer |
| Q18 | **A** | The data are 4 đơn với doanh thu nghìn đồng | 4 đơn với doanh thu nghìn đồng |
| Q19 | **D** | Meaning of rows, columns and units | Ý nghĩa hàng, cột và đơn vị |
| Q20 | **C** | Check the result and limitations | Kiểm tra kết quả và giới hạn |

## 8. Nối sang bài tiếp

`DataFrame → lọc → nhóm → ghép bảng → AI`.

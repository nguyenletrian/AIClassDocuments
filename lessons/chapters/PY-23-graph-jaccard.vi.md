# PY-23 — Đồ thị, danh sách kề và Jaccard similarity


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Graph** — đồ thị; **Vertex** — đỉnh.

`Set → Graph → Similarity → Gợi ý bạn học`

Nắm liên hệ giữa cấu trúc toán học và mảng dữ liệu Python trước khi sử dụng vào học máy.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Giải thích |
|---|---|---|
| Graph | đồ thị | Các đỉnh và cạnh mô tả quan hệ giữa đối tượng |
| Vertex | đỉnh | Một đối tượng được biểu diễn trong đồ thị |
| Edge | cạnh | Liên hệ hoặc đường nối giữa hai đỉnh |
| Jaccard | độ tương đồng | Tỷ lệ số phần tử giao trên hợp giữa hai tập |

## 3. NumPy và các hàm liên quan

**Từ vựng trong mục:** **Function** — hàm; **Shape** — kích thước mảng.

| Hàm / tham số | Dùng làm gì |
|---|---|
| `dict[str,set[str]]` | Danh sách kề đơn giản: key là đỉnh, value là các đỉnh nối |
| `networkx.Graph()/DiGraph()` | Đồ thị vô hướng/có hướng, cần cài networkx |
| `nx.shortest_path(G,a,b)` | Tìm đường nối ngắn nhất nếu có kết nối |
| `len(a&b)/len(a` | b) |

## 4. Khái niệm kèm ví dụ nhỏ

### 4.1. Graph

**Từ vựng trong mục:** **Graph** — đồ thị.

Các đỉnh và cạnh mô tả quan hệ giữa đối tượng. Trước khi sử dụng biểu thức hãy xem phần tử, hàng/cột và đơn vị đầu vào.

```python
graph={'An':{'Binh'},'Binh':{'An'}}
print(graph)
```

**Kết quả khi chạy:**

```text
{'An': {'Binh'}, 'Binh': {'An'}}
```

**Tự kiểm tra:** Graph có nghĩa gì? **Đáp án:** Các đỉnh và cạnh mô tả quan hệ giữa đối tượng.

### 4.2. Vertex

**Từ vựng trong mục:** **Vertex** — đỉnh.

Một đối tượng được biểu diễn trong đồ thị. Trước khi sử dụng biểu thức hãy xem phần tử, hàng/cột và đơn vị đầu vào.

```python
vertices={'An','Binh'}
print(len(vertices))
```

**Kết quả khi chạy:**

```text
2
```

**Tự kiểm tra:** Vertex có nghĩa gì? **Đáp án:** Một đối tượng được biểu diễn trong đồ thị.

### 4.3. Edge

**Từ vựng trong mục:** **Edge** — cạnh.

Liên hệ hoặc đường nối giữa hai đỉnh. Trước khi sử dụng biểu thức hãy xem phần tử, hàng/cột và đơn vị đầu vào.

```python
edges={('An','Binh')}
print(len(edges))
```

**Kết quả khi chạy:**

```text
1
```

**Tự kiểm tra:** Edge có nghĩa gì? **Đáp án:** Liên hệ hoặc đường nối giữa hai đỉnh.

### 4.4. Jaccard

**Từ vựng trong mục:** **Jaccard** — độ tương đồng.

Tỷ lệ số phần tử giao trên hợp giữa hai tập. Trước khi sử dụng biểu thức hãy xem phần tử, hàng/cột và đơn vị đầu vào.

```python
a={'Python','AI'};b={'Python'}
print(len(a & b) / len(a | b))
```

**Kết quả khi chạy:**

```text
0.5
```

**Tự kiểm tra:** Jaccard có nghĩa gì? **Đáp án:** Tỷ lệ số phần tử giao trên hợp giữa hai tập.

## 5. Năm tình huống ứng dụng

### Tình huống 1 — Bạn bè trực tiếp

**Từ vựng trong mục:** **Graph** — đồ thị.

**Tình huống thực tế:** Một tổ chức đang triển khai hệ thống dữ liệu muốn bạn bè trực tiếp. Bộ dữ liệu đang có: Đồ thị An Binh Lan. Mỗi hàng là một đối tượng, mỗi cột là feature trong bài toán (nếu đầu vào là ma trận). Những con số ở đây là minh họa, không phải kết luận thực tế. Hãy lập trình giải quyết yêu cầu này và đưa ra kết quả có thể kiểm tra.

**Vì sao chọn phương án?** Danh sách kề cho phép tra bạn của người đang xét; điều kiện tiên quyết là dữ liệu có shape và ý nghĩa từng giá trị rõ ràng.


**Quy trình:** mô tả dữ liệu → xác định phép tính/shape → tính bằng Python → kiểm tra kết quả.

```python
graph={"An":{"Binh","Lan"},"Binh":{"An"},"Lan":{"An"}}
print(graph["An"])
```

**Kết quả khi chạy:**

```text
{'Binh', 'Lan'}
```

**Đọc kết quả:** Chú ý kích thước và đơn vị kết quả, thử thêm ca biên nếu đưa vào ứng dụng thực tế.

### Tình huống 2 — So trùng sở thích

**Từ vựng trong mục:** **Vertex** — đỉnh.

**Tình huống thực tế:** Một tổ chức đang triển khai hệ thống dữ liệu muốn so trùng sở thích. Bộ dữ liệu đang có: Hai người với sở thích Python AI SQL. Mỗi hàng là một đối tượng, mỗi cột là feature trong bài toán (nếu đầu vào là ma trận). Những con số ở đây là minh họa, không phải kết luận thực tế. Hãy lập trình giải quyết yêu cầu này và đưa ra kết quả có thể kiểm tra.

**Vì sao chọn phương án?** Jaccard so phần giao với toàn bộ nhãn sở thích; điều kiện tiên quyết là dữ liệu có shape và ý nghĩa từng giá trị rõ ràng.


**Quy trình:** mô tả dữ liệu → xác định phép tính/shape → tính bằng Python → kiểm tra kết quả.

```python
a={"Python","AI"};b={"Python","SQL"}
print(len(a&b)/len(a|b))
```

**Kết quả khi chạy:**

```text
0.3333333333333333
```

**Đọc kết quả:** Chú ý kích thước và đơn vị kết quả, thử thêm ca biên nếu đưa vào ứng dụng thực tế.

### Tình huống 3 — Gợi ý đối tác học

**Từ vựng trong mục:** **Edge** — cạnh.

**Tình huống thực tế:** Một tổ chức đang triển khai hệ thống dữ liệu muốn gợi ý đối tác học. Bộ dữ liệu đang có: Nhóm kỹ năng giả lập. Mỗi hàng là một đối tượng, mỗi cột là feature trong bài toán (nếu đầu vào là ma trận). Những con số ở đây là minh họa, không phải kết luận thực tế. Hãy lập trình giải quyết yêu cầu này và đưa ra kết quả có thể kiểm tra.

**Vì sao chọn phương án?** Chọn người có Jaccard lớn nhất; điều kiện tiên quyết là dữ liệu có shape và ý nghĩa từng giá trị rõ ràng.


**Quy trình:** mô tả dữ liệu → xác định phép tính/shape → tính bằng Python → kiểm tra kết quả.

```python
target={"AI","Python"}
people={"B":{"AI"},"C":{"AI","Python"}}
scores={n:len(target&s)/len(target|s) for n,s in people.items()}
print(max(scores,key=scores.get))
```

**Kết quả khi chạy:**

```text
C
```

**Đọc kết quả:** Chú ý kích thước và đơn vị kết quả, thử thêm ca biên nếu đưa vào ứng dụng thực tế.

### Tình huống 4 — Quan hệ có hướng

**Từ vựng trong mục:** **Jaccard** — độ tương đồng.

**Tình huống thực tế:** Một tổ chức đang triển khai hệ thống dữ liệu muốn quan hệ có hướng. Bộ dữ liệu đang có: A→B và B→C. Mỗi hàng là một đối tượng, mỗi cột là feature trong bài toán (nếu đầu vào là ma trận). Những con số ở đây là minh họa, không phải kết luận thực tế. Hãy lập trình giải quyết yêu cầu này và đưa ra kết quả có thể kiểm tra.

**Vì sao chọn phương án?** Cạnh A tới B không nhất thiết có B tới A; điều kiện tiên quyết là dữ liệu có shape và ý nghĩa từng giá trị rõ ràng.


**Quy trình:** mô tả dữ liệu → xác định phép tính/shape → tính bằng Python → kiểm tra kết quả.

```python
graph={"A":{"B"},"B":{"C"},"C":set()}
print("B" in graph["A"],"A" in graph["B"])
```

**Kết quả khi chạy:**

```text
True False
```

**Đọc kết quả:** Chú ý kích thước và đơn vị kết quả, thử thêm ca biên nếu đưa vào ứng dụng thực tế.

### Tình huống 5 — Tìm đường trong mạng

**Từ vựng trong mục:** **Graph** — đồ thị.

**Tình huống thực tế:** Một tổ chức đang triển khai hệ thống dữ liệu muốn tìm đường trong mạng. Bộ dữ liệu đang có: Ba đỉnh A-B-C. Mỗi hàng là một đối tượng, mỗi cột là feature trong bài toán (nếu đầu vào là ma trận). Những con số ở đây là minh họa, không phải kết luận thực tế. Hãy lập trình giải quyết yêu cầu này và đưa ra kết quả có thể kiểm tra.

**Vì sao chọn phương án?** Dùng networkx khi đồ thị cần tìm đường thay vì code vòng thủ công; điều kiện tiên quyết là dữ liệu có shape và ý nghĩa từng giá trị rõ ràng.


**Quy trình:** mô tả dữ liệu → xác định phép tính/shape → tính bằng Python → kiểm tra kết quả.

```python
import networkx as nx
G=nx.Graph();G.add_edges_from([("A","B"),("B","C")])
print(nx.shortest_path(G,"A","C"))
```

**Kết quả khi chạy:**

```text
['A', 'B', 'C']
```

**Đọc kết quả:** Chú ý kích thước và đơn vị kết quả, thử thêm ca biên nếu đưa vào ứng dụng thực tế.

## 6. Sai lầm cần tránh

Phân biệt vector một chiều với ma trận hai chiều, tránh nhân ma trận sai shape; covariance và eigenvalue không phải độ chính xác mô hình. Các ví dụ số không có ý nghĩa dự đoán nếu thiếu bước đánh giá.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.


**Q1. What is Graph? — Thuật ngữ Graph có nghĩa gì?**

A. It instead means Một đối tượng được biểu diễn trong đồ thị — Một đối tượng được biểu diễn trong đồ thị

B. It means Các đỉnh và cạnh mô tả quan hệ giữa đối tượng — Các đỉnh và cạnh mô tả quan hệ giữa đối tượng

C. It instead means Liên hệ hoặc đường nối giữa hai đỉnh — Liên hệ hoặc đường nối giữa hai đỉnh

D. It instead means Tỷ lệ số phần tử giao trên hợp giữa hai tập — Tỷ lệ số phần tử giao trên hợp giữa hai tập


**Q2. What is Vertex? — Thuật ngữ Vertex có nghĩa gì?**

A. It means Một đối tượng được biểu diễn trong đồ thị — Một đối tượng được biểu diễn trong đồ thị

B. It instead means Liên hệ hoặc đường nối giữa hai đỉnh — Liên hệ hoặc đường nối giữa hai đỉnh

C. It instead means Tỷ lệ số phần tử giao trên hợp giữa hai tập — Tỷ lệ số phần tử giao trên hợp giữa hai tập

D. It instead means Các đỉnh và cạnh mô tả quan hệ giữa đối tượng — Các đỉnh và cạnh mô tả quan hệ giữa đối tượng


**Q3. What is Edge? — Thuật ngữ Edge có nghĩa gì?**

A. It instead means Tỷ lệ số phần tử giao trên hợp giữa hai tập — Tỷ lệ số phần tử giao trên hợp giữa hai tập

B. It instead means Các đỉnh và cạnh mô tả quan hệ giữa đối tượng — Các đỉnh và cạnh mô tả quan hệ giữa đối tượng

C. It instead means Một đối tượng được biểu diễn trong đồ thị — Một đối tượng được biểu diễn trong đồ thị

D. It means Liên hệ hoặc đường nối giữa hai đỉnh — Liên hệ hoặc đường nối giữa hai đỉnh


**Q4. What is Jaccard? — Thuật ngữ Jaccard có nghĩa gì?**

A. It instead means Các đỉnh và cạnh mô tả quan hệ giữa đối tượng — Các đỉnh và cạnh mô tả quan hệ giữa đối tượng

B. It instead means Một đối tượng được biểu diễn trong đồ thị — Một đối tượng được biểu diễn trong đồ thị

C. It means Tỷ lệ số phần tử giao trên hợp giữa hai tập — Tỷ lệ số phần tử giao trên hợp giữa hai tập

D. It instead means Liên hệ hoặc đường nối giữa hai đỉnh — Liên hệ hoặc đường nối giữa hai đỉnh


**Q5. What does dict[str,set[str]] help with? — Hàm dict[str,set[str]] giúp làm gì?**

A. Another function helps to Đồ thị vô hướng/có hướng, cần cài networkx — Đồ thị vô hướng/có hướng, cần cài networkx

B. It helps to Danh sách kề đơn giản: key là đỉnh, value là các đỉnh nối — Danh sách kề đơn giản: key là đỉnh, value là các đỉnh nối

C. Another function helps to Tìm đường nối ngắn nhất nếu có kết nối — Tìm đường nối ngắn nhất nếu có kết nối

D. Another function helps to b) — b)


**Q6. What does networkx.Graph()/DiGraph() help with? — Hàm networkx.Graph()/DiGraph() giúp làm gì?**

A. It helps to Đồ thị vô hướng/có hướng, cần cài networkx — Đồ thị vô hướng/có hướng, cần cài networkx

B. Another function helps to Tìm đường nối ngắn nhất nếu có kết nối — Tìm đường nối ngắn nhất nếu có kết nối

C. Another function helps to b) — b)

D. Another function helps to Danh sách kề đơn giản: key là đỉnh, value là các đỉnh nối — Danh sách kề đơn giản: key là đỉnh, value là các đỉnh nối


**Q7. What does nx.shortest_path(G,a,b) help with? — Hàm nx.shortest_path(G,a,b) giúp làm gì?**

A. Another function helps to b) — b)

B. Another function helps to Danh sách kề đơn giản: key là đỉnh, value là các đỉnh nối — Danh sách kề đơn giản: key là đỉnh, value là các đỉnh nối

C. Another function helps to Đồ thị vô hướng/có hướng, cần cài networkx — Đồ thị vô hướng/có hướng, cần cài networkx

D. It helps to Tìm đường nối ngắn nhất nếu có kết nối — Tìm đường nối ngắn nhất nếu có kết nối


**Q8. What does len(a&b)/len(a help with? — Hàm len(a&b)/len(a giúp làm gì?**

A. Another function helps to Danh sách kề đơn giản: key là đỉnh, value là các đỉnh nối — Danh sách kề đơn giản: key là đỉnh, value là các đỉnh nối

B. Another function helps to Đồ thị vô hướng/có hướng, cần cài networkx — Đồ thị vô hướng/có hướng, cần cài networkx

C. It helps to b) — b)

D. Another function helps to Tìm đường nối ngắn nhất nếu có kết nối — Tìm đường nối ngắn nhất nếu có kết nối


**Q9. Why choose this method for scenario 1? — Vì sao chọn cách làm tình huống 1?**

A. Jaccard so phần giao với toàn bộ nhãn sở thích — Jaccard so phần giao với toàn bộ nhãn sở thích

B. Danh sách kề cho phép tra bạn của người đang xét — Danh sách kề cho phép tra bạn của người đang xét

C. Chọn người có Jaccard lớn nhất — Chọn người có Jaccard lớn nhất

D. Cạnh A tới B không nhất thiết có B tới A — Cạnh A tới B không nhất thiết có B tới A


**Q10. Why choose this method for scenario 2? — Vì sao chọn cách làm tình huống 2?**

A. Jaccard so phần giao với toàn bộ nhãn sở thích — Jaccard so phần giao với toàn bộ nhãn sở thích

B. Chọn người có Jaccard lớn nhất — Chọn người có Jaccard lớn nhất

C. Cạnh A tới B không nhất thiết có B tới A — Cạnh A tới B không nhất thiết có B tới A

D. Dùng networkx khi đồ thị cần tìm đường thay vì code vòng thủ công — Dùng networkx khi đồ thị cần tìm đường thay vì code vòng thủ công


**Q11. Why choose this method for scenario 3? — Vì sao chọn cách làm tình huống 3?**

A. Cạnh A tới B không nhất thiết có B tới A — Cạnh A tới B không nhất thiết có B tới A

B. Dùng networkx khi đồ thị cần tìm đường thay vì code vòng thủ công — Dùng networkx khi đồ thị cần tìm đường thay vì code vòng thủ công

C. Danh sách kề cho phép tra bạn của người đang xét — Danh sách kề cho phép tra bạn của người đang xét

D. Chọn người có Jaccard lớn nhất — Chọn người có Jaccard lớn nhất


**Q12. Why choose this method for scenario 4? — Vì sao chọn cách làm tình huống 4?**

A. Dùng networkx khi đồ thị cần tìm đường thay vì code vòng thủ công — Dùng networkx khi đồ thị cần tìm đường thay vì code vòng thủ công

B. Danh sách kề cho phép tra bạn của người đang xét — Danh sách kề cho phép tra bạn của người đang xét

C. Cạnh A tới B không nhất thiết có B tới A — Cạnh A tới B không nhất thiết có B tới A

D. Jaccard so phần giao với toàn bộ nhãn sở thích — Jaccard so phần giao với toàn bộ nhãn sở thích


**Q13. Why choose this method for scenario 5? — Vì sao chọn cách làm tình huống 5?**

A. Danh sách kề cho phép tra bạn của người đang xét — Danh sách kề cho phép tra bạn của người đang xét

B. Dùng networkx khi đồ thị cần tìm đường thay vì code vòng thủ công — Dùng networkx khi đồ thị cần tìm đường thay vì code vòng thủ công

C. Jaccard so phần giao với toàn bộ nhãn sở thích — Jaccard so phần giao với toàn bộ nhãn sở thích

D. Chọn người có Jaccard lớn nhất — Chọn người có Jaccard lớn nhất


**Q14. What input is relevant to scenario 1? — Dữ liệu nào của tình huống 1?**

A. The input is Đồ thị An Binh Lan — Đồ thị An Binh Lan

B. Different data: Hai người với sở thích Python AI SQL — Hai người với sở thích Python AI SQL

C. Different data: Nhóm kỹ năng giả lập — Nhóm kỹ năng giả lập

D. Different data: A→B và B→C — A→B và B→C


**Q15. What input is relevant to scenario 2? — Dữ liệu nào của tình huống 2?**

A. Different data: Nhóm kỹ năng giả lập — Nhóm kỹ năng giả lập

B. Different data: A→B và B→C — A→B và B→C

C. Different data: Ba đỉnh A-B-C — Ba đỉnh A-B-C

D. The input is Hai người với sở thích Python AI SQL — Hai người với sở thích Python AI SQL


**Q16. What input is relevant to scenario 3? — Dữ liệu nào của tình huống 3?**

A. Different data: A→B và B→C — A→B và B→C

B. Different data: Ba đỉnh A-B-C — Ba đỉnh A-B-C

C. The input is Nhóm kỹ năng giả lập — Nhóm kỹ năng giả lập

D. Different data: Đồ thị An Binh Lan — Đồ thị An Binh Lan


**Q17. What input is relevant to scenario 4? — Dữ liệu nào của tình huống 4?**

A. Different data: Ba đỉnh A-B-C — Ba đỉnh A-B-C

B. The input is A→B và B→C — A→B và B→C

C. Different data: Đồ thị An Binh Lan — Đồ thị An Binh Lan

D. Different data: Hai người với sở thích Python AI SQL — Hai người với sở thích Python AI SQL


**Q18. What input is relevant to scenario 5? — Dữ liệu nào của tình huống 5?**

A. The input is Ba đỉnh A-B-C — Ba đỉnh A-B-C

B. Different data: Đồ thị An Binh Lan — Đồ thị An Binh Lan

C. Different data: Hai người với sở thích Python AI SQL — Hai người với sở thích Python AI SQL

D. Different data: Nhóm kỹ năng giả lập — Nhóm kỹ năng giả lập


**Q19. What should be checked for matrix operations? — Phép toán ma trận phải kiểm tra gì?**

A. Only line spacing — Chỉ khoảng cách dòng

B. Only file suffix — Chỉ phần mở rộng file

C. Only terminal width — Chỉ độ rộng terminal

D. Shapes and data units — Shape và đơn vị dữ liệu


**Q20. Why is one numeric example not enough for AI? — Vì sao một ví dụ số chưa đủ đánh giá AI?**

A. It always proves generalization — Nó luôn chứng minh khả năng tổng quát

B. It removes the need for test data — Nó bỏ được tập kiểm tra

C. It does not establish predictive performance — Nó không đo chất lượng dự đoán

D. It guarantees no leakage — Nó bảo đảm không rò rỉ dữ liệu

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **B** | It means Các đỉnh và cạnh mô tả quan hệ giữa đối tượng | Các đỉnh và cạnh mô tả quan hệ giữa đối tượng |
| Q2 | **A** | It means Một đối tượng được biểu diễn trong đồ thị | Một đối tượng được biểu diễn trong đồ thị |
| Q3 | **D** | It means Liên hệ hoặc đường nối giữa hai đỉnh | Liên hệ hoặc đường nối giữa hai đỉnh |
| Q4 | **C** | It means Tỷ lệ số phần tử giao trên hợp giữa hai tập | Tỷ lệ số phần tử giao trên hợp giữa hai tập |
| Q5 | **B** | It helps to Danh sách kề đơn giản: key là đỉnh, value là các đỉnh nối | Danh sách kề đơn giản: key là đỉnh, value là các đỉnh nối |
| Q6 | **A** | It helps to Đồ thị vô hướng/có hướng, cần cài networkx | Đồ thị vô hướng/có hướng, cần cài networkx |
| Q7 | **D** | It helps to Tìm đường nối ngắn nhất nếu có kết nối | Tìm đường nối ngắn nhất nếu có kết nối |
| Q8 | **C** | It helps to b) | b) |
| Q9 | **B** | Danh sách kề cho phép tra bạn của người đang xét | Danh sách kề cho phép tra bạn của người đang xét |
| Q10 | **A** | Jaccard so phần giao với toàn bộ nhãn sở thích | Jaccard so phần giao với toàn bộ nhãn sở thích |
| Q11 | **D** | Chọn người có Jaccard lớn nhất | Chọn người có Jaccard lớn nhất |
| Q12 | **C** | Cạnh A tới B không nhất thiết có B tới A | Cạnh A tới B không nhất thiết có B tới A |
| Q13 | **B** | Dùng networkx khi đồ thị cần tìm đường thay vì code vòng thủ công | Dùng networkx khi đồ thị cần tìm đường thay vì code vòng thủ công |
| Q14 | **A** | The input is Đồ thị An Binh Lan | Đồ thị An Binh Lan |
| Q15 | **D** | The input is Hai người với sở thích Python AI SQL | Hai người với sở thích Python AI SQL |
| Q16 | **C** | The input is Nhóm kỹ năng giả lập | Nhóm kỹ năng giả lập |
| Q17 | **B** | The input is A→B và B→C | A→B và B→C |
| Q18 | **A** | The input is Ba đỉnh A-B-C | Ba đỉnh A-B-C |
| Q19 | **D** | Shapes and data units | Shape và đơn vị dữ liệu |
| Q20 | **C** | It does not establish predictive performance | Nó không đo chất lượng dự đoán |

## 8. Nối sang bài kế tiếp

`Set → Graph → Similarity → Gợi ý bạn học`.

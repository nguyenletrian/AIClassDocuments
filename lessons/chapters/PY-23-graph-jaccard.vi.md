# PY-23 — Đồ thị, danh sách kề và Jaccard similarity


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Graph** — đồ thị
 **Vertex** — đỉnh.

`Set → Graph → Similarity → Gợi ý bạn học`

Nắm liên hệ giữa cấu trúc toán học và mảng dữ liệu Python trước khi sử dụng vào học máy.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Giải thích |
|---|---|---|
| Graph | đồ thị | Các đỉnh và cạnh mô tả quan hệ giữa đối tượng |
| Vertex | đỉnh | Một đối tượng được biểu diễn trong đồ thị |
| Edge | cạnh | Liên hệ hoặc đường nối giữa hai đỉnh |
| Jaccard | độ tương đồng | Tỷ lệ số phần tử giao trên hợp giữa hai tập |

## 3. Hàm và cấu trúc dữ liệu liên quan

**Từ vựng trong mục:** **Function** — hàm; **Adjacency list** — danh sách kề.

| Hàm / tham số | Dùng làm gì |
|---|---|
| `dict[str,set[str]]` | Danh sách kề đơn giản: key là đỉnh, value là các đỉnh nối |
| `networkx.Graph()/DiGraph()` | Đồ thị vô hướng/có hướng, cần cài networkx |
| `nx.shortest_path(G,a,b)` | Tìm đường nối ngắn nhất nếu có kết nối |
| `len(a & b) / len(a | b)` | Tương đồng Jaccard khi hợp khác rỗng |

## 4. Khái niệm liên quan

**Đồ thị (graph)** mô tả mạng quan hệ: **đỉnh (vertex)** là đối tượng, **cạnh (edge)** là mối nối giữa đối tượng. Trong mạng học viên, mỗi người là một đỉnh và một cạnh biểu thị quan hệ bạn bè. Ta biểu diễn mạng bằng **danh sách kề** rồi liên hệ với **Jaccard**, thước đo phần sở thích chung so với toàn bộ sở thích của hai người.

### 4.1. Graph và adjacency list — Mạng và danh sách kề

**Từ vựng trong mục:** **Graph** — đồ thị; **Adjacency list** — danh sách kề.

Một **đồ thị** gồm tập **đỉnh** và tập **cạnh** nối chúng. Để biểu diễn mạng bạn bè An–Bình–Lan mà không cần vẽ, dùng Dictionary: **khóa** là tên người, **Set giá trị** là những người kết nối trực tiếp với họ. Nếu quan hệ hai chiều, cả hai đầu phải ghi tên nhau. Ví dụ An kết bạn với Bình và Lan, còn Bình/Lan đều kết nối ngược lại An.

```python
graph = {
    'An': {'Binh', 'Lan'},
    'Binh': {'An'},
    'Lan': {'An'},
}
print(sorted(graph['An']))
```

**Kết quả khi chạy:**

```text
['Binh', 'Lan']
```

An có hai kết nối trực tiếp là Bình và Lan. Dictionary giúp tra nhanh những người kề với một đỉnh.

### 4.2. Vertex — Đỉnh đại diện một đối tượng

**Từ vựng trong mục:** **Vertex** — đỉnh; **Node** — nút.

**Đỉnh** là một đối tượng trong mạng: một học viên, trạm xe hoặc trang web. Tên đỉnh chỉ là định danh, không nói lên nó đã kết nối với ai. Trong ví dụ có hai học viên An và Bình, ta dùng Set chứa hai tên làm tập đỉnh; `len(vertices)` đếm đối tượng khác nhau, không phải số liên kết.

```python
vertices = {'An', 'Binh'}
print(len(vertices))
```

**Kết quả khi chạy:**

```text
2
```

Mạng có hai đỉnh khác nhau; chưa suy ra có cạnh nào giữa họ.

### 4.3. Edge — Cạnh có hướng và vô hướng

**Từ vựng trong mục:** **Edge** — cạnh; **Directed** — có hướng.

**Cạnh** biểu diễn mối quan hệ giữa hai đỉnh. Với bạn bè hai chiều, cạnh An–Bình là **vô hướng** và chỉ cần tính một lần; với hành động A gửi thông báo tới B, cạnh A→B **có hướng**, không tự suy ra B→A. Danh sách kề có hướng `{'A':{'B'},'B':set()}` diễn tả A gửi B, nhưng B không gửi lại A.

```python
graph = {'A': {'B'}, 'B': set()}
print('B' in graph['A'], 'A' in graph['B'])
```

**Kết quả khi chạy:**

```text
True False
```

Quan hệ A→B tồn tại; chiều ngược lại không tồn tại. Cách lưu cạnh phải phù hợp loại đồ thị.

### 4.4. Jaccard similarity — Độ giống nhau của hai tập

**Từ vựng trong mục:** **Jaccard** — tương đồng Jaccard; **Union/intersection** — hợp/giao.

**Jaccard** đo mức trùng nhau của hai tập: `J(A,B) = |A ∩ B| / |A ∪ B|`, trong khoảng **0–1** khi hợp không rỗng. Người A biết `{Python, AI}`, người B biết `{Python, SQL}`: giao có 1 kỹ năng `Python`, hợp có 3 kỹ năng, nên độ tương đồng là `1/3 ≈ 0.333`. Không dùng số lượng phần tử trùng trực tiếp làm tỷ lệ. Với cả hai tập rỗng phải định nghĩa riêng quy ước để tránh chia 0.

```python
a = {'Python', 'AI'}
b = {'Python', 'SQL'}
print(round(len(a & b) / len(a | b), 3))
```

**Kết quả khi chạy:**

```text
0.333
```

Hai hồ sơ giống nhau khoảng 33,3% theo Jaccard vì chỉ chung một trên ba kỹ năng khác nhau.
## 5. Năm tình huống ứng dụng

### Tình huống 1 — Bạn bè trực tiếp

**Từ vựng trong mục:** **Graph** — đồ thị.

**Tình huống thực tế:** Mạng bạn bè cho biết An kết nối với Bình và Lan, còn Bình kết nối lại An. Liệt kê các bạn trực tiếp của An.

**Vì sao chọn cách giải này?** Danh sách kề cho biết những người nối trực tiếp với An; không cần phép nhân ma trận.


**Quy trình giải:**

1. Tạo Dictionary danh sách kề, trong đó mỗi người là một khóa và tập bạn bè là giá trị.
2. Lấy tập bạn kề của An bằng `graph['An']`.
3. Sắp xếp tên để đầu ra không phụ thuộc thứ tự Set.

```python
graph={"An":{"Binh","Lan"},"Binh":{"An"},"Lan":{"An"}}
print(sorted(graph['An']))
```

**Kết quả khi chạy:**

```text
['Binh', 'Lan']
```

### Tình huống 2 — So trùng sở thích

**Từ vựng trong mục:** **Jaccard similarity** — độ tương đồng tập hợp.

**Tình huống thực tế:** Hai hồ sơ sở thích A={Python,AI}, B={Python,SQL}. Tính mức tương đồng Jaccard bằng số mục chung chia số mục khác nhau.

**Vì sao chọn cách giải này?** Jaccard tính tỷ lệ giao/hợp của hai Set và bảo đảm kết quả trong khoảng 0–1.


**Quy trình giải:**

1. Tạo hai Set kỹ năng `a`, `b` từ hai hồ sơ.
2. Đếm phần giao và phần hợp; mẫu số phải khác 0.
3. Chia số kỹ năng chung cho số kỹ năng khác nhau và in độ tương đồng.

```python
a={"Python","AI"}
b={"Python","SQL"}
print(len(a&b)/len(a|b))
```

**Kết quả khi chạy:**

```text
0.3333333333333333
```

### Tình huống 3 — Gợi ý đối tác học

**Từ vựng trong mục:** **Jaccard similarity** — độ tương đồng tập hợp.

**Tình huống thực tế:** Một học viên thích Python và AI; bạn B thích AI, bạn C thích cả Python lẫn AI. Chọn người có điểm tương đồng cao nhất.

**Vì sao chọn cách giải này?** Tính Jaccard với từng ứng viên rồi chọn điểm lớn nhất sẽ cho người có sở thích trùng nhiều nhất.


**Quy trình giải:**

1. Lưu tập sở thích mục tiêu và Dictionary các ứng viên B, C.
2. Tính Jaccard giữa mục tiêu với từng ứng viên.
3. Dùng `max(scores, key=scores.get)` chọn ứng viên có tỷ lệ cao nhất.

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

### Tình huống 4 — Quan hệ có hướng

**Từ vựng trong mục:** **Directed edge** — cạnh có hướng.

**Tình huống thực tế:** Mạng thông báo có hướng A→B và B→C. Kiểm tra đường A→B có đồng nghĩa với B→A không.

**Vì sao chọn cách giải này?** Đồ thị có hướng phân biệt A→B và B→A; kiểm tra hai chiều phải thực hiện riêng.


**Quy trình giải:**

1. Lưu đồ thị có hướng với A dẫn đến B và B dẫn đến C.
2. Kiểm tra B có thuộc danh sách kề của A không.
3. Kiểm tra riêng A có thuộc danh sách kề của B không và in hai kết quả.

```python
graph={"A":{"B"},"B":{"C"},"C":set()}
print("B" in graph["A"],"A" in graph["B"])
```

**Kết quả khi chạy:**

```text
True False
```

### Tình huống 5 — Tìm đường trong mạng

**Từ vựng trong mục:** **Graph** — đồ thị.

**Tình huống thực tế:** Ba trạm A, B, C nối bằng hai đoạn A-B và B-C. Tìm đường đi ngắn nhất giữa A và C.

**Vì sao chọn cách giải này?** `networkx.shortest_path` tìm chuỗi đỉnh ngắn nhất theo số cạnh khi các cạnh không có trọng số.


**Quy trình giải:**

1. Tạo đồ thị không hướng và thêm cạnh A–B, B–C bằng NetworkX (cần cài thư viện trước).
2. Gọi `nx.shortest_path(G, 'A', 'C')`.
3. In danh sách trạm theo thứ tự đường đi.

```python
import networkx as nx
G=nx.Graph()
G.add_edges_from([("A","B"),("B","C")])
print(nx.shortest_path(G,"A","C"))
```

**Kết quả khi chạy:**

```text
['A', 'B', 'C']
```

## 6. Sai lầm thường gặp

- **Đỉnh** là đối tượng, **cạnh** là quan hệ; không nhầm số đỉnh với số cạnh.
- Đồ thị có hướng không mặc nhiên có cạnh ngược; đồ thị vô hướng cần diễn giải kết nối hai chiều.
- Set không bảo đảm thứ tự in; dùng `sorted()` khi liệt kê tên trong tài liệu.
- Jaccard bằng `|A∩B| / |A∪B|`; nếu cả hai tập rỗng thì phải xử lý trước khi chia.
- `networkx` là thư viện ngoài cần cài đặt; `shortest_path` có thể báo lỗi nếu hai đỉnh không nối với nhau.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi
 **Answer** — đáp án.


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

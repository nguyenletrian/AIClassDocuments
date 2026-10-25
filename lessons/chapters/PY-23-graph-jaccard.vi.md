# PY-23 — Đồ thị, danh sách kề và Jaccard similarity


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Graph** — đồ thị
 **Vertex** — đỉnh.

`Set → Graph → Similarity → Gợi ý bạn học`

**Học xong dùng để làm gì?** Dùng cạnh và nút mô tả liên kết; so nhãn/sở thích bằng hệ số tương đồng Jaccard.

**Kết nối kiến thức tiếp theo:** PY-24 chuyển đặc trưng đối tượng thành vector có thể đo độ dài và hướng.

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
# Mục đích: Mạng và danh sách kề.
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
# Mục đích: Đỉnh đại diện một đối tượng.
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
# Mục đích: Cạnh có hướng và vô hướng.
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
# Mục đích: Độ giống nhau của hai tập.
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

### Tình huống 1 — Bạn bè trực tiếp · Cấp 1: Danh sách kề

**Từ vựng trong mục:** **Graph** — đồ thị.

**Tình huống thực tế:** Mạng bạn bè cho biết An kết nối với Bình và Lan, còn Bình kết nối lại An. Liệt kê các bạn trực tiếp của An.

**Vì sao chọn cách giải này?** Danh sách kề cho biết những người nối trực tiếp với An; không cần phép nhân ma trận.


**Quy trình giải:**

1. Tạo Dictionary danh sách kề, trong đó mỗi người là một khóa và tập bạn bè là giá trị.
2. Lấy tập bạn kề của An bằng `graph['An']`.
3. Sắp xếp tên để đầu ra không phụ thuộc thứ tự Set.

```python
# Mục đích: Bạn bè trực tiếp.
graph = {"An":{"Binh", "Lan"}, "Binh":{"An"}, "Lan":{"An"}}
print(sorted(graph['An']))
```

**Kết quả khi chạy:**

```text
['Binh', 'Lan']
```

**Bài thực hành nâng cấp — cấp 1/5:** Trạm vận tải ghi **10 liên kết** giữa các trạm; một dòng là cạnh có đầu và cuối (mã N01, N02...). Hãy liệt kê các trạm nối trực tiếp với N01. Quy mô tăng đều từ 10 lên 20 liên kết, phép giải tiến từ danh sách kề đến đường đi nhiều bước.

```python
from collections import deque
edges = [(f"N{i:02d}",f"N{i+1:02d}") for i in range(1,11)]
adj, directed = {}, {}
for source,target in edges:
    adj.setdefault(source,set()).add(target)
    adj.setdefault(target,set()).add(source)
    directed.setdefault(source,set()).add(target)
def bfs(start,end):
    queue=deque([(start,[start])])
    visited={start}
    while queue:
        node,path=queue.popleft()
        if node==end: return path
        for nxt in sorted(adj[node]-visited):
            visited.add(nxt)
            queue.append((nxt,path+[nxt]))
    return []
result = sorted(adj['N01'])
print("Số cạnh:",len(edges))
print("Kết quả:",result)
```

**Đọc kết quả:** Số bản ghi cạnh 10; danh sách kề của đồ thị vô hướng và cạnh có hướng được lưu riêng để không nhầm ý nghĩa.

### Tình huống 2 — So trùng sở thích · Cấp 2: Tính độ giống Jaccard

**Từ vựng trong mục:** **Jaccard similarity** — độ tương đồng tập hợp.

**Tình huống thực tế:** Hai hồ sơ sở thích A={Python,AI}, B={Python,SQL}. Tính mức tương đồng Jaccard bằng số mục chung chia số mục khác nhau.

**Vì sao chọn cách giải này?** Jaccard tính tỷ lệ giao/hợp của hai Set và bảo đảm kết quả trong khoảng 0–1.


**Quy trình giải:**

1. Tạo hai Set kỹ năng `a`, `b` từ hai hồ sơ.
2. Đếm phần giao và phần hợp; mẫu số phải khác 0.
3. Chia số kỹ năng chung cho số kỹ năng khác nhau và in độ tương đồng.

```python
# Mục đích: So trùng sở thích.
a = {"Python", "AI"}
b = {"Python", "SQL"}
print(len(a&b)/len(a|b))
```

**Kết quả khi chạy:**

```text
0.3333333333333333
```

**Bài thực hành nâng cấp — cấp 2/5:** Trạm vận tải ghi **12 liên kết** giữa các trạm; một dòng là cạnh có đầu và cuối (mã N01, N02...). Hãy tính Jaccard giữa hai bộ láng giềng N02 và N03. Quy mô tăng đều từ 10 lên 20 liên kết, phép giải tiến từ danh sách kề đến đường đi nhiều bước.

```python
from collections import deque
edges = [(f"N{i:02d}",f"N{i+1:02d}") for i in range(1,13)]
adj, directed = {}, {}
for source,target in edges:
    adj.setdefault(source,set()).add(target)
    adj.setdefault(target,set()).add(source)
    directed.setdefault(source,set()).add(target)
def bfs(start,end):
    queue=deque([(start,[start])])
    visited={start}
    while queue:
        node,path=queue.popleft()
        if node==end: return path
        for nxt in sorted(adj[node]-visited):
            visited.add(nxt)
            queue.append((nxt,path+[nxt]))
    return []
result = len(adj['N02']&adj['N03'])/len(adj['N02']|adj['N03'])
print("Số cạnh:",len(edges))
print("Kết quả:",result)
```

**Đọc kết quả:** Số bản ghi cạnh 12; danh sách kề của đồ thị vô hướng và cạnh có hướng được lưu riêng để không nhầm ý nghĩa.

### Tình huống 3 — Gợi ý đối tác học · Cấp 3: Tìm trạm nhiều kết nối

**Từ vựng trong mục:** **Jaccard similarity** — độ tương đồng tập hợp.

**Tình huống thực tế:** Một học viên thích Python và AI; bạn B thích AI, bạn C thích cả Python lẫn AI. Chọn người có điểm tương đồng cao nhất.

**Vì sao chọn cách giải này?** Tính Jaccard với từng ứng viên rồi chọn điểm lớn nhất sẽ cho người có sở thích trùng nhiều nhất.


**Quy trình giải:**

1. Lưu tập sở thích mục tiêu và Dictionary các ứng viên B, C.
2. Tính Jaccard giữa mục tiêu với từng ứng viên.
3. Dùng `max(scores, key=scores.get)` chọn ứng viên có tỷ lệ cao nhất.

```python
# Mục đích: Gợi ý đối tác học.
target = {"AI", "Python"}
people = {"B":{"AI"}, "C":{"AI", "Python"}}
scores = {n:len(target&s)/len(target|s) for n, s in people.items()}
print(max(scores, key=scores.get))
```

**Kết quả khi chạy:**

```text
C
```

**Bài thực hành nâng cấp — cấp 3/5:** Trạm vận tải ghi **15 liên kết** giữa các trạm; một dòng là cạnh có đầu và cuối (mã N01, N02...). Hãy đếm bậc của từng đỉnh và xếp năm đỉnh nổi bật. Quy mô tăng đều từ 10 lên 20 liên kết, phép giải tiến từ danh sách kề đến đường đi nhiều bước.

```python
from collections import deque
edges = [(f"N{i:02d}",f"N{i+1:02d}") for i in range(1,16)]
adj, directed = {}, {}
for source,target in edges:
    adj.setdefault(source,set()).add(target)
    adj.setdefault(target,set()).add(source)
    directed.setdefault(source,set()).add(target)
def bfs(start,end):
    queue=deque([(start,[start])])
    visited={start}
    while queue:
        node,path=queue.popleft()
        if node==end: return path
        for nxt in sorted(adj[node]-visited):
            visited.add(nxt)
            queue.append((nxt,path+[nxt]))
    return []
result = sorted([(node,len(neighbors)) for node,neighbors in adj.items()],key=lambda t:(-t[1],t[0]))[:5]
print("Số cạnh:",len(edges))
print("Kết quả:",result)
```

**Đọc kết quả:** Số bản ghi cạnh 15; danh sách kề của đồ thị vô hướng và cạnh có hướng được lưu riêng để không nhầm ý nghĩa.

### Tình huống 4 — Quan hệ có hướng · Cấp 4: Phân biệt hướng của cạnh

**Từ vựng trong mục:** **Directed edge** — cạnh có hướng.

**Tình huống thực tế:** Mạng thông báo có hướng A→B và B→C. Kiểm tra đường A→B có đồng nghĩa với B→A không.

**Vì sao chọn cách giải này?** Đồ thị có hướng phân biệt A→B và B→A; kiểm tra hai chiều phải thực hiện riêng.


**Quy trình giải:**

1. Lưu đồ thị có hướng với A dẫn đến B và B dẫn đến C.
2. Kiểm tra B có thuộc danh sách kề của A không.
3. Kiểm tra riêng A có thuộc danh sách kề của B không và in hai kết quả.

```python
# Mục đích: Quan hệ có hướng.
graph = {"A":{"B"}, "B":{"C"}, "C":set()}
print("B" in graph["A"], "A" in graph["B"])
```

**Kết quả khi chạy:**

```text
True False
```

**Bài thực hành nâng cấp — cấp 4/5:** Trạm vận tải ghi **18 liên kết** giữa các trạm; một dòng là cạnh có đầu và cuối (mã N01, N02...). Hãy kiểm tra A→B không tự suy ra B→A trên 18 cạnh có hướng. Quy mô tăng đều từ 10 lên 20 liên kết, phép giải tiến từ danh sách kề đến đường đi nhiều bước.

```python
from collections import deque
edges = [(f"N{i:02d}",f"N{i+1:02d}") for i in range(1,19)]
adj, directed = {}, {}
for source,target in edges:
    adj.setdefault(source,set()).add(target)
    adj.setdefault(target,set()).add(source)
    directed.setdefault(source,set()).add(target)
def bfs(start,end):
    queue=deque([(start,[start])])
    visited={start}
    while queue:
        node,path=queue.popleft()
        if node==end: return path
        for nxt in sorted(adj[node]-visited):
            visited.add(nxt)
            queue.append((nxt,path+[nxt]))
    return []
result = {'N01_to_N02':('N02' in directed.get('N01',set())),'N02_to_N01':('N01' in directed.get('N02',set()))}
print("Số cạnh:",len(edges))
print("Kết quả:",result)
```

**Đọc kết quả:** Số bản ghi cạnh 18; danh sách kề của đồ thị vô hướng và cạnh có hướng được lưu riêng để không nhầm ý nghĩa.

### Tình huống 5 — Tìm đường trong mạng · Cấp 5: Tìm tuyến đường bằng BFS

**Từ vựng trong mục:** **Graph** — đồ thị.

**Tình huống thực tế:** Ba trạm A, B, C nối bằng hai đoạn A-B và B-C. Tìm đường đi ngắn nhất giữa A và C.

**Vì sao chọn cách giải này?** `networkx.shortest_path` tìm chuỗi đỉnh ngắn nhất theo số cạnh khi các cạnh không có trọng số.


**Quy trình giải:**

1. Tạo đồ thị không hướng và thêm cạnh A–B, B–C bằng NetworkX (cần cài thư viện trước).
2. Gọi `nx.shortest_path(G, 'A', 'C')`.
3. In danh sách trạm theo thứ tự đường đi.

```python
# Mục đích: Tìm đường trong mạng.
import networkx as nx
G = nx.Graph()
G.add_edges_from([("A", "B"), ("B", "C")])
print(nx.shortest_path(G, "A", "C"))
```

**Kết quả khi chạy:**

```text
['A', 'B', 'C']
```

**Bài thực hành nâng cấp — cấp 5/5:** Trạm vận tải ghi **20 liên kết** giữa các trạm; một dòng là cạnh có đầu và cuối (mã N01, N02...). Hãy dùng BFS đi từ N01 đến trạm cuối trên 20 liên kết. Quy mô tăng đều từ 10 lên 20 liên kết, phép giải tiến từ danh sách kề đến đường đi nhiều bước.

```python
from collections import deque
edges = [(f"N{i:02d}",f"N{i+1:02d}") for i in range(1,21)]
adj, directed = {}, {}
for source,target in edges:
    adj.setdefault(source,set()).add(target)
    adj.setdefault(target,set()).add(source)
    directed.setdefault(source,set()).add(target)
def bfs(start,end):
    queue=deque([(start,[start])])
    visited={start}
    while queue:
        node,path=queue.popleft()
        if node==end: return path
        for nxt in sorted(adj[node]-visited):
            visited.add(nxt)
            queue.append((nxt,path+[nxt]))
    return []
result = {'nodes':len(adj),'edges':len(edges),'route':bfs('N01',f'N{len(edges)+1:02d}')}
print("Số cạnh:",len(edges))
print("Kết quả:",result)
```

**Đọc kết quả:** Số bản ghi cạnh 20; danh sách kề của đồ thị vô hướng và cạnh có hướng được lưu riêng để không nhầm ý nghĩa.

## 6. Sai lầm thường gặp

- **Đỉnh** là đối tượng, **cạnh** là quan hệ; không nhầm số đỉnh với số cạnh.
- Đồ thị có hướng không mặc nhiên có cạnh ngược; đồ thị vô hướng cần diễn giải kết nối hai chiều.
- Set không bảo đảm thứ tự in; dùng `sorted()` khi liệt kê tên trong tài liệu.
- Jaccard bằng `|A∩B| / |A∪B|`; nếu cả hai tập rỗng thì phải xử lý trước khi chia.
- `networkx` là thư viện ngoài cần cài đặt; `shortest_path` có thể báo lỗi nếu hai đỉnh không nối với nhau.

## 7. Trắc nghiệm

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What is a graph? | Đồ thị là gì?**

A. A collection of vertices and edges | Tập các đỉnh và cạnh

B. An entity or node in the network | Một đối tượng hoặc nút trong mạng

C. A relationship connecting two vertices | Quan hệ nối hai đỉnh

D. A mapping from each vertex to its neighbors | Ánh xạ mỗi đỉnh tới các đỉnh kề

**Đáp án: A**

**Giải thích:** Đồ thị mô tả quan hệ giữa các đối tượng.


**Q2. What is a vertex? | Đỉnh trong đồ thị là gì?**

A. A collection of vertices and edges | Tập các đỉnh và cạnh

B. An entity or node in the network | Một đối tượng hoặc nút trong mạng

C. A relationship connecting two vertices | Quan hệ nối hai đỉnh

D. A mapping from each vertex to its neighbors | Ánh xạ mỗi đỉnh tới các đỉnh kề

**Đáp án: B**

**Giải thích:** Mỗi đỉnh đại diện một đối tượng.


**Q3. What is an edge? | Cạnh của đồ thị là gì?**

A. A collection of vertices and edges | Tập các đỉnh và cạnh

B. An entity or node in the network | Một đối tượng hoặc nút trong mạng

C. A relationship connecting two vertices | Quan hệ nối hai đỉnh

D. A mapping from each vertex to its neighbors | Ánh xạ mỗi đỉnh tới các đỉnh kề

**Đáp án: C**

**Giải thích:** Cạnh biểu diễn kết nối giữa các đỉnh.


**Q4. What is an adjacency list? | Danh sách kề là gì?**

A. A collection of vertices and edges | Tập các đỉnh và cạnh

B. An entity or node in the network | Một đối tượng hoặc nút trong mạng

C. A relationship connecting two vertices | Quan hệ nối hai đỉnh

D. A mapping from each vertex to its neighbors | Ánh xạ mỗi đỉnh tới các đỉnh kề

**Đáp án: D**

**Giải thích:** Danh sách kề lưu các kết nối của từng đỉnh.


**Q5. What does a directed edge A→B assert? | Cạnh có hướng A→B cho biết gì?**

A. A connection from A to B | Kết nối đi từ A đến B

B. A connection without direction | Kết nối không phân biệt chiều

C. The neighbors stored for An | Những đỉnh kề được lưu cho An

D. A sequence of connected vertices | Chuỗi các đỉnh nối tiếp nhau

**Đáp án: A**

**Giải thích:** Chiều kết nối quan trọng; B→A không tự tồn tại.


**Q6. What does an undirected edge mean? | Cạnh vô hướng có ý nghĩa gì?**

A. A connection from A to B | Kết nối đi từ A đến B

B. A connection without direction | Kết nối không phân biệt chiều

C. The neighbors stored for An | Những đỉnh kề được lưu cho An

D. A sequence of connected vertices | Chuỗi các đỉnh nối tiếp nhau

**Đáp án: B**

**Giải thích:** Quan hệ vô hướng đi được theo cả hai chiều.


**Q7. What does `graph['An']` return in an adjacency dictionary? | `graph['An']` trong Dictionary kề trả gì?**

A. A connection from A to B | Kết nối đi từ A đến B

B. A connection without direction | Kết nối không phân biệt chiều

C. The neighbors stored for An | Những đỉnh kề được lưu cho An

D. A sequence of connected vertices | Chuỗi các đỉnh nối tiếp nhau

**Đáp án: C**

**Giải thích:** Giá trị của khóa đỉnh chứa các nút lân cận.


**Q8. What does a path in a graph describe? | Đường đi trong đồ thị biểu diễn gì?**

A. A connection from A to B | Kết nối đi từ A đến B

B. A connection without direction | Kết nối không phân biệt chiều

C. The neighbors stored for An | Những đỉnh kề được lưu cho An

D. A sequence of connected vertices | Chuỗi các đỉnh nối tiếp nhau

**Đáp án: D**

**Giải thích:** Hai đỉnh liên tiếp trên đường đi phải có cạnh nối.


**Q9. What is Jaccard similarity for sets A and B? | Jaccard giữa hai Set A, B bằng gì?**

A. Intersection size divided by union size | Số phần tử giao chia số phần tử hợp

B. 1 | 1

C. 0 | 0

D. A zero union denominator | Mẫu số hợp bằng 0

**Đáp án: A**

**Giải thích:** Jaccard so phần chung với toàn bộ phần tử khác nhau.


**Q10. What is Jaccard for two identical nonempty sets? | Jaccard của hai Set giống nhau và không rỗng là gì?**

A. Intersection size divided by union size | Số phần tử giao chia số phần tử hợp

B. 1 | 1

C. 0 | 0

D. A zero union denominator | Mẫu số hợp bằng 0

**Đáp án: B**

**Giải thích:** Phép giao bằng phép hợp.


**Q11. What is Jaccard for two disjoint nonempty sets? | Jaccard của hai Set không giao nhau, không rỗng là gì?**

A. Intersection size divided by union size | Số phần tử giao chia số phần tử hợp

B. 1 | 1

C. 0 | 0

D. A zero union denominator | Mẫu số hợp bằng 0

**Đáp án: C**

**Giải thích:** Phép giao không có phần tử nào.


**Q12. What must be handled before computing Jaccard on two empty sets? | Cần xử lý gì trước khi tính Jaccard cho hai Set rỗng?**

A. Intersection size divided by union size | Số phần tử giao chia số phần tử hợp

B. 1 | 1

C. 0 | 0

D. A zero union denominator | Mẫu số hợp bằng 0

**Đáp án: D**

**Giải thích:** Nếu không xử lý sẽ chia cho 0.


**Q13. What does `nx.Graph()` create? | `nx.Graph()` tạo gì?**

A. An undirected NetworkX graph | Đồ thị vô hướng NetworkX

B. A directed NetworkX graph | Đồ thị có hướng NetworkX

C. A path with fewest edges | Đường đi có ít cạnh nhất

D. Install and import the package | Cài và import thư viện

**Đáp án: A**

**Giải thích:** Graph tạo cạnh vô hướng theo mặc định.


**Q14. What does `nx.DiGraph()` create? | `nx.DiGraph()` tạo gì?**

A. An undirected NetworkX graph | Đồ thị vô hướng NetworkX

B. A directed NetworkX graph | Đồ thị có hướng NetworkX

C. A path with fewest edges | Đường đi có ít cạnh nhất

D. Install and import the package | Cài và import thư viện

**Đáp án: B**

**Giải thích:** DiGraph phân biệt chiều cạnh.


**Q15. What does `nx.shortest_path()` find on an unweighted graph? | `nx.shortest_path()` tìm gì trên đồ thị không trọng số?**

A. An undirected NetworkX graph | Đồ thị vô hướng NetworkX

B. A directed NetworkX graph | Đồ thị có hướng NetworkX

C. A path with fewest edges | Đường đi có ít cạnh nhất

D. Install and import the package | Cài và import thư viện

**Đáp án: C**

**Giải thích:** Đường ngắn nhất không trọng số có ít cạnh nhất.


**Q16. What is required to use NetworkX in Python? | Để dùng NetworkX trong Python cần gì?**

A. An undirected NetworkX graph | Đồ thị vô hướng NetworkX

B. A directed NetworkX graph | Đồ thị có hướng NetworkX

C. A path with fewest edges | Đường đi có ít cạnh nhất

D. Install and import the package | Cài và import thư viện

**Đáp án: D**

**Giải thích:** NetworkX không thuộc thư viện chuẩn Python.


**Q17. How can neighbor display order be made consistent? | Làm sao in danh sách các đỉnh kề theo thứ tự ổn định?**

A. Call `sorted()` on neighbor sets | Gọi `sorted()` trên Set đỉnh kề

B. No valid route can be returned | Không có tuyến đường hợp lệ để trả về

C. To identify each graph entity unambiguously | Để xác định từng đối tượng không mơ hồ

D. Jaccard compares sets; shortest path follows graph edges | Jaccard so hai tập; đường ngắn nhất đi theo cạnh

**Đáp án: A**

**Giải thích:** Set không bảo đảm thứ tự khi in.


**Q18. What happens if no path exists between two vertices? | Nếu không có đường nối hai đỉnh thì sao?**

A. Call `sorted()` on neighbor sets | Gọi `sorted()` trên Set đỉnh kề

B. No valid route can be returned | Không có tuyến đường hợp lệ để trả về

C. To identify each graph entity unambiguously | Để xác định từng đối tượng không mơ hồ

D. Jaccard compares sets; shortest path follows graph edges | Jaccard so hai tập; đường ngắn nhất đi theo cạnh

**Đáp án: B**

**Giải thích:** Thuật toán tìm đường cần xử lý hai đỉnh không liên thông.


**Q19. Why should node names be unique? | Vì sao tên đỉnh nên duy nhất?**

A. Call `sorted()` on neighbor sets | Gọi `sorted()` trên Set đỉnh kề

B. No valid route can be returned | Không có tuyến đường hợp lệ để trả về

C. To identify each graph entity unambiguously | Để xác định từng đối tượng không mơ hồ

D. Jaccard compares sets; shortest path follows graph edges | Jaccard so hai tập; đường ngắn nhất đi theo cạnh

**Đáp án: C**

**Giải thích:** Mã đỉnh trùng khiến các đối tượng bị nhập làm một.


**Q20. What distinguishes Jaccard from graph shortest path? | Jaccard khác đường đi ngắn nhất ở đâu?**

A. Call `sorted()` on neighbor sets | Gọi `sorted()` trên Set đỉnh kề

B. No valid route can be returned | Không có tuyến đường hợp lệ để trả về

C. To identify each graph entity unambiguously | Để xác định từng đối tượng không mơ hồ

D. Jaccard compares sets; shortest path follows graph edges | Jaccard so hai tập; đường ngắn nhất đi theo cạnh

**Đáp án: D**

**Giải thích:** Hai công cụ trả lời hai loại câu hỏi khác nhau.

## 8. Nối sang bài kế tiếp

`Set → Graph → Similarity → Gợi ý bạn học`.

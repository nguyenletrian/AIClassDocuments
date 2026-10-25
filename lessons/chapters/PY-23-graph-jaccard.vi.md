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
## 5. Năm tình huống Graph/Jaccard — từ bạn trực tiếp đến đường đi và xếp hạng

### Tình huống 1 — Cấp 1: Xây danh sách kề của 10 người từ 12 kết nối

**Từ vựng trong mục:** **Graph** — đồ thị; **Adjacency list** — danh sách kề; **Degree** — bậc đỉnh.

**Tình huống thực tế:** Mạng học tập có **10 học viên A…J** và **12 dòng kết nối hai chiều**, mỗi dòng gồm hai mã học viên được phép liên hệ trực tiếp. Cần xác định số bạn trực tiếp của A và tổng số quan hệ; không được đếm quan hệ A–B và B–A thành hai mối quan hệ riêng.

**Vì sao chọn cách này?** Danh sách kề dùng Dictionary của các Set: khi thêm một cạnh vô hướng phải ghi ở cả hai đầu. Tổng số lượt liên kết theo đỉnh bằng hai lần số cạnh, giúp kiểm tra nhập dữ liệu.

**Quy trình:**
1. Tạo 10 đỉnh, mỗi đỉnh có Set hàng xóm rỗng.
2. Duyệt 12 cạnh và thêm hai chiều.
3. Đếm hàng xóm A và kiểm tra tổng bậc bằng hai lần số cạnh.

```python
nodes = list("ABCDEFGHIJ")
edges = [["A","B"],["A","C"],["A","D"],["B","E"],["C","E"],["D","F"],["E","F"],["F","G"],["G","H"],["H","I"],["I","J"],["C","J"]]
graph = {node: set() for node in nodes}
for left, right in edges:
    graph[left].add(right)
    graph[right].add(left)
assert len(nodes) == 10 and len(edges) == 12
assert sum(map(len, graph.values())) == 2 * len(edges)
print("Người:", len(nodes))
print("Quan hệ:", len(edges))
print("Bạn của A:", ", ".join(sorted(graph["A"])))
print("Số bạn A:", len(graph["A"]))
```

**Kết quả khi chạy:**

```text
Người: 10
Quan hệ: 12
Bạn của A: B, C, D
Số bạn A: 3
```

Một dòng cạnh là một quan hệ giữa hai học viên; khi danh sách kề ghi hai chiều, không được hiểu rằng số quan hệ đã tăng gấp đôi.

### Tình huống 2 — Cấp 2: So Jaccard từ 12 hồ sơ kỹ năng có nhãn

**Từ vựng trong mục:** **Jaccard similarity** — tương đồng tập hợp; **Intersection** — phần giao.

**Tình huống thực tế:** Nền tảng ghép nhóm nhận **12 hồ sơ H01…H12**, mỗi dòng là một người với Set kỹ năng như Python, AI, SQL, Math, Data, Cloud. Một kỹ năng có thể vô tình được ghi lại trong cùng hồ sơ, nhưng phải coi là một mục duy nhất. Dùng H01 làm hồ sơ tham chiếu, tính điểm Jaccard với H02 và tìm người gần H01 nhất trong 11 người còn lại.

**Vì sao chọn cách này?** Jaccard đo tỷ lệ số kỹ năng chung so với tổng kỹ năng khác nhau. Trước khi tính phải dùng Set loại mục lặp trong từng hồ sơ, xử lý tập hợp rỗng an toàn và phân xử đồng điểm bằng mã tăng dần.

**Quy trình:**
1. Tạo 12 dòng hồ sơ, mỗi hồ sơ là tập kỹ năng.
2. Viết hàm Jaccard dùng độ lớn phần giao và hợp.
3. Tính điểm H01–H02 và tìm người gần nhất với H01.

```python
profiles = [{"id":"H01","skills":["Python","AI","Python"]},{"id":"H02","skills":["AI","SQL"]},{"id":"H03","skills":["SQL","Math"]},{"id":"H04","skills":["Math","Data"]},{"id":"H05","skills":["Data","Cloud","Python"]},{"id":"H06","skills":["Cloud","Python"]},{"id":"H07","skills":["Python","AI"]},{"id":"H08","skills":["AI","SQL"]},{"id":"H09","skills":["SQL","Math","Python"]},{"id":"H10","skills":["Math","Data"]},{"id":"H11","skills":["Data","Cloud"]},{"id":"H12","skills":["Cloud","Python"]}]
def jaccard(first, second):
    a, b = set(first), set(second)
    union = a | b
    return len(a & b) / len(union) if union else 0.0
reference = profiles[0]["skills"]
score = jaccard(reference, profiles[1]["skills"])
ranked = sorted(((p["id"], jaccard(reference, p["skills"])) for p in profiles[1:]),
                key=lambda row: (-row[1], row[0]))
assert len(profiles) == 12
print("Hồ sơ:", len(profiles))
print(f"Jaccard H01-H02: {score:.2f}")
print("Gần H01 nhất:", ranked[0][0], f"{ranked[0][1]:.2f}")
```

**Kết quả khi chạy:**

```text
Hồ sơ: 12
Jaccard H01-H02: 0.33
Gần H01 nhất: H07 1.00
```

Độ tương đồng 1 là hai tập kỹ năng giống hệt nhau; đây chỉ là độ tương đồng, **không** tự động chứng minh hai người hợp làm việc.

### Tình huống 3 — Cấp 3: Phân hai cụm kết nối từ 15 cạnh của mạng học viên

**Từ vựng trong mục:** **Connected component** — thành phần liên thông; **Traversal** — duyệt đồ thị.

**Tình huống thực tế:** Một câu lạc bộ ghi **15 cạnh kết nối vô hướng** giữa các học viên A…O (15 người). Dữ liệu có hai mạng bạn bè tách biệt A…G và H…O. Điều phối viên cần biết có bao nhiêu cụm, cụm lớn nhất gồm bao nhiêu người và liệu A có liên hệ nối tiếp được với O không.

**Vì sao chọn cách này?** Đi từ danh sách kề, dùng duyệt DFS/BFS đánh dấu người đã gặp để tìm các thành phần liên thông. Đếm cạnh đơn thuần không cho biết có đường đi từ A tới O.

**Quy trình:**
1. Dựng danh sách kề từ 15 cạnh; mỗi quan hệ ghi cả hai chiều.
2. Duyệt những đỉnh chưa thăm để thu từng cụm kết nối.
3. Sắp các kích thước cụm và kiểm tra A/O có cùng cụm không.

```python
edges = [["A","B"],["B","C"],["C","D"],["A","D"],["D","E"],["E","F"],["F","G"],["H","I"],["I","J"],["J","K"],["K","L"],["H","L"],["L","M"],["M","N"],["N","O"]]
vertices = sorted({name for edge in edges for name in edge})
graph = {v: set() for v in vertices}
for a, b in edges:
    graph[a].add(b)
    graph[b].add(a)
seen, components = set(), []
for start in vertices:
    if start in seen:
        continue
    stack, members = [start], set()
    while stack:
        node = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        members.add(node)
        stack.extend(graph[node] - seen)
    components.append(members)
assert len(edges) == 15 and len(vertices) == 15
print("Cạnh:", len(edges))
print("Cụm:", len(components))
print("Kích thước cụm:", ", ".join(map(str, sorted(map(len, components), reverse=True))))
print("A kết nối O:", any({"A", "O"} <= group for group in components))
```

**Kết quả khi chạy:**

```text
Cạnh: 15
Cụm: 2
Kích thước cụm: 8, 7
A kết nối O: False
```

Hai người có thể không có cạnh trực tiếp nhưng vẫn cùng cụm qua trung gian. A và O nằm ở hai cụm khác nhau nên không có đường nối qua dữ liệu hiện tại.

### Tình huống 4 — Cấp 4: Xếp hạng 17 đối tác từ 18 hồ sơ, xử lý kỹ năng trống

**Từ vựng trong mục:** **Ranking** — xếp hạng; **Empty set** — tập rỗng; **Tie-break** — phân xử hòa điểm.

**Tình huống thực tế:** Cộng đồng học tập có **18 hồ sơ** U01…U18 với kỹ năng mỗi người; U14 chưa nhập bất kỳ kỹ năng nào, còn các hồ sơ khác có thể có mục trùng trong cùng người. Cần gợi ý **ba người** giống U01 nhất bằng Jaccard, không chia cho 0 khi một tập rỗng và không tự coi người thiếu kỹ năng là không có năng lực.

**Vì sao chọn cách này?** Dùng một hàm tính Jaccard có điều kiện với mẫu số rỗng, sau đó xếp theo điểm giảm và ID tăng khi hòa. Không làm dữ liệu thiếu biến mất mà phải báo số hồ sơ cần bổ sung.

**Quy trình:**
1. Chuẩn hóa kỹ năng về Set trên 18 hồ sơ.
2. Tính tương đồng U01 với 17 người còn lại, kiểm tra tập rỗng.
3. Sắp xếp ổn định, in ba ứng viên đầu và số hồ sơ thiếu kỹ năng.

```python
people = [{"id":"U01","skills":["Python","SQL","Python"]},{"id":"U02","skills":["AI","Math"]},{"id":"U03","skills":["SQL","Data"]},{"id":"U04","skills":["Math","Cloud","Python"]},{"id":"U05","skills":["Data","Vision"]},{"id":"U06","skills":["Cloud","NLP"]},{"id":"U07","skills":["Vision","Python","Python"]},{"id":"U08","skills":["NLP","AI"]},{"id":"U09","skills":["Python","SQL"]},{"id":"U10","skills":["AI","Math","Python"]},{"id":"U11","skills":["SQL","Data"]},{"id":"U12","skills":["Math","Cloud"]},{"id":"U13","skills":["Data","Vision","Python"]},{"id":"U14","skills":[]},{"id":"U15","skills":["Vision","Python"]},{"id":"U16","skills":["NLP","AI","Python"]},{"id":"U17","skills":["Python","SQL"]},{"id":"U18","skills":["AI","Math"]}]
def similarity(a, b):
    a, b = set(a), set(b)
    total = a | b
    return len(a & b) / len(total) if total else 0.0
base = people[0]["skills"]
ranked = sorted(((p["id"], similarity(base, p["skills"])) for p in people[1:]),
                key=lambda item: (-item[1], item[0]))
assert len(people) == 18
print("Hồ sơ:", len(people))
print("Thiếu kỹ năng:", sum(not p["skills"] for p in people))
for uid, score in ranked[:3]:
    print(f"{uid}: {score:.2f}")
```

**Kết quả khi chạy:**

```text
Hồ sơ: 18
Thiếu kỹ năng: 1
U09: 1.00
U17: 1.00
U03: 0.33
```

Đây là **xếp hạng theo điểm tập hợp**, không phải kết luận con người nào phù hợp nhất về khả năng học tập thực tế. Hồ sơ trống cần bổ sung dữ liệu.

### Tình huống 5 — Cấp 5: Tìm đường ngắn nhất và so hàng xóm trong mạng có hướng 20 cạnh

**Từ vựng trong mục:** **Directed graph** — đồ thị có hướng; **BFS** — duyệt theo chiều rộng; **Jaccard** — tương đồng tập kề.

**Tình huống thực tế:** Hệ thống chuyển tiếp thông báo ghi **20 cạnh có hướng** giữa các trạm A…S; mỗi dòng `(nguồn, đích)` chỉ cho phép gửi theo **một hướng**. Cần tìm đường đi ít bước nhất từ trạm A tới K, kiểm tra trạm R có đường tới K không, và so sánh tập trạm nhận trực tiếp của A/B bằng Jaccard. Không được đi ngược một cạnh đã cho.

**Vì sao chọn cách này?** Dùng BFS theo từng lớp cạnh để đường đầu tới đích có **ít cạnh nhất** trong mạng không trọng số. Jaccard trên hai tập hàng xóm ra trả câu hỏi khác: mức chồng lấn các trạm nhận trực tiếp.

**Quy trình:**
1. Tạo danh sách kề **một chiều** từ 20 cạnh và xác nhận trạm nguồn/đích.
2. Dùng BFS có kiểm soát đỉnh đã thăm để tìm đường A→K và R→K.
3. Tính Jaccard tập trạm nhận trực tiếp A/B, báo đường và hai kết quả.

```python
from collections import deque
edges = [["A","B"],["A","C"],["B","D"],["C","D"],["D","E"],["E","F"],["B","G"],["G","H"],["H","I"],["I","J"],["F","J"],["J","K"],["C","L"],["L","M"],["M","N"],["N","O"],["O","K"],["K","P"],["P","Q"],["R","S"]]
graph = {}
for source, destination in edges:
    graph.setdefault(source, set()).add(destination)
def shortest(start, end):
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        node, path = queue.popleft()
        if node == end:
            return path
        for neighbor in sorted(graph.get(node, set())):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None
path = shortest("A", "K")
a, b = graph.get("A", set()), graph.get("B", set())
score = len(a & b) / len(a | b) if a | b else 0.0
assert len(edges) == 20
print("Cạnh có hướng:", len(edges))
print("Đường A-K:", " -> ".join(path))
print("Số cạnh đường:", len(path) - 1)
print("R tới K:", shortest("R", "K") is not None)
print(f"Jaccard kề A/B: {score:.2f}")
```

**Kết quả khi chạy:**

```text
Cạnh có hướng: 20
Đường A-K: A -> B -> D -> E -> F -> J -> K
Số cạnh đường: 6
R tới K: False
Jaccard kề A/B: 0.00
```

Đường A→K có thể đi qua trạm trung gian, nhưng R→S không thể tự quay ngược để tới K. Độ giống nhau của tập kề không thay thế thuật toán tìm đường.

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

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
| `len(a & b) / len(a \| b)` | Tương đồng Jaccard khi hợp khác rỗng |

## 4. Khái niệm liên quan

**Đồ thị (graph)** mô tả mạng quan hệ: **đỉnh (vertex)** là đối tượng, **cạnh (edge)** là mối nối giữa đối tượng. Trong mạng học viên, mỗi người là một đỉnh và một cạnh biểu thị quan hệ bạn bè. Ta biểu diễn mạng bằng **danh sách kề** rồi liên hệ với **Jaccard**, thước đo phần sở thích chung so với toàn bộ sở thích của hai người.

### 4.1. Graph và adjacency list — Mạng và danh sách kề

**Từ vựng trong mục:** **Graph** — đồ thị; **Adjacency list** — danh sách kề.

Một **đồ thị** gồm tập **đỉnh** và tập **cạnh** nối chúng. Để biểu diễn mạng bạn bè An–Bình–Lan mà không cần vẽ, dùng Dictionary: **khóa** là tên người, **Set giá trị** là những người kết nối trực tiếp với họ. Nếu quan hệ hai chiều, cả hai đầu phải ghi tên nhau. Ví dụ An kết bạn với Bình và Lan, còn Bình/Lan đều kết nối ngược lại An.

**No Note — Không chú thích**

```python
graph = {
    'An': {'Binh', 'Lan'},
    'Binh': {'An'},
    'Lan': {'An'},
}
print(sorted(graph['An']))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Biểu diễn quan hệ bạn bè bằng dictionary danh sách kề và đọc bạn của An.
# Dữ liệu: Mỗi khóa là một người, giá trị là set những người nối với họ bằng cạnh bạn bè.
# Dictionary dạng {đỉnh: set(đỉnh_kề)} là danh sách kề; An nối Binh và Lan.
graph = {
    'An': {'Binh', 'Lan'},
    'Binh': {'An'},
    'Lan': {'An'},
}
# Tra danh sách kề của An; sorted() chuyển set thành list mã có thứ tự ổn định để in.
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

**No Note — Không chú thích**

```python
vertices = {'An', 'Binh'}
print(len(vertices))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Đếm đỉnh là những đối tượng độc lập trong đồ thị.
# Dữ liệu: Hai đỉnh An và Binh, tập set loại tên trùng nếu có.
# Set chứa đỉnh duy nhất, không có cạnh hay hướng trong ví dụ nhỏ này.
vertices = {'An', 'Binh'}
# len() đếm số đỉnh khác nhau, không đếm số quan hệ.
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

**No Note — Không chú thích**

```python
graph = {'A': {'B'}, 'B': set()}
print('B' in graph['A'], 'A' in graph['B'])
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Phân biệt cạnh có hướng A→B với cạnh ngược B→A không tồn tại.
# Dữ liệu: graph['A'] có B, graph['B'] là set rỗng; kết nối chỉ đi một chiều.
# Dictionary danh sách kề cho đồ thị có hướng; set() tạo danh sách kề rỗng của B.
graph = {'A': {'B'}, 'B': set()}
# in kiểm có cung A→B hay không (True); kiểm ngược A trong graph['B'] là False nên KHÔNG mặc định vô hướng.
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

**No Note — Không chú thích**

```python
a = {'Python', 'AI'}
b = {'Python', 'SQL'}
print(round(len(a & b) / len(a | b), 3))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tính độ tương đồng Jaccard giữa hai bộ kỹ năng bằng giao chia hợp.
# Dữ liệu: a={Python,AI}, b={Python,SQL}; có một kỹ năng chung và ba kỹ năng khác nhau trong hợp.
# Set kỹ năng A, mỗi kỹ năng chỉ xuất hiện một lần.
a = {'Python', 'AI'}
# Set kỹ năng B, giao với a ở Python.
b = {'Python', 'SQL'}
# & lấy tập chung (1), | lấy tất cả kỹ năng không trùng (3), chia để có Jaccard 1/3; round(...,3) chỉ làm tròn khi in.
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

**Tình huống thực tế:** Cộng đồng học tập gồm **10 học viên A đến J**. Danh sách có **12 mối quan hệ trực tiếp**; mỗi dòng lưu hai mã, ví dụ A–B có nghĩa A và B có thể liên hệ với nhau **theo cả hai chiều**. Nhân viên cần biết A liên hệ trực tiếp được với những ai, A có bao nhiêu bạn trực tiếp và toàn mạng có bao nhiêu mối quan hệ, không tính A–B và B–A như hai quan hệ riêng.

**Vì sao chọn cách này?** **Đồ thị** là cách biểu diễn người bằng **đỉnh** và quan hệ trực tiếp bằng **cạnh**. Vì liên hệ trong bài là **hai chiều**, khi có A–B, chương trình thêm B vào set bạn của A **và** thêm A vào set bạn của B. Dictionary `graph` ánh xạ mỗi mã với tập bạn trực tiếp; đây là **danh sách kề**, không phải bảng điểm. Set không giữ một người hai lần, còn `sorted()` giúp in mã đúng thứ tự. Khi cộng số bạn của mọi người, mỗi quan hệ được tính ở **hai đầu**, nên tổng số lượt nối gấp đôi số cạnh thật; bước kiểm tra này phát hiện việc quên ghi một chiều.

**Quy trình:**
1. Tạo 10 đỉnh, mỗi đỉnh có Set hàng xóm rỗng.
2. Duyệt 12 cạnh và thêm hai chiều.
3. Đếm hàng xóm A và kiểm tra tổng bậc bằng hai lần số cạnh.

**No Note — Không chú thích**

```python
nodes = list("ABCDEFGHIJ")
edges = [["A","B"],["A","C"],["A","D"],["B","E"],["C","E"],["D","F"],["E","F"],["F","G"],["G","H"],["H","I"],["I","J"],["C","J"]]
graph = {}
for node in nodes:
    graph[node] = set()
for left, right in edges:
    graph[left].add(right)
    graph[right].add(left)
if len(nodes) != 10 or len(edges) != 12:
    raise ValueError("Cần đúng 10 người và 12 quan hệ.")
if sum(map(len, graph.values())) != 2 * len(edges):
    raise ValueError("Đồ thị vô hướng phải ghi hai đầu mỗi cạnh.")
print("Người:", len(nodes))
print("Quan hệ:", len(edges))
print("Bạn của A:", ", ".join(sorted(graph["A"])))
print("Số bạn A:", len(graph["A"]))
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tạo đồ thị vô hướng từ 10 người và 12 cạnh, đếm bậc của A và kiểm hai chiều.
# Dữ liệu: 10 đỉnh A..J, 12 cặp quan hệ [người đầu, người cuối]; cạnh bạn bè không có hướng.
# list() tách chuỗi thành 10 tên đỉnh A..J.
nodes = list("ABCDEFGHIJ")
# Mỗi list con là một cạnh vô hướng giữa hai người; số cạnh thực là 12.
edges = [["A","B"],["A","C"],["A","D"],["B","E"],["C","E"],["D","F"],["E","F"],["F","G"],["G","H"],["H","I"],["I","J"],["C","J"]]
# Dictionary lưu mỗi đỉnh và set hàng xóm của nó.
graph = {}
for node in nodes:
    # Tạo set kề rỗng trước khi thêm quan hệ, tránh KeyError.
    graph[node] = set()
# Tách hai đầu của mỗi cạnh.
for left, right in edges:
    # add() thêm đầu phải vào danh sách kề của đầu trái.
    graph[left].add(right)
    # Đồ thị VÔ HƯỚNG cần thêm chiều ngược lại; mỗi cạnh đóng góp hai lần vào tổng bậc.
    graph[right].add(left)
# Kiểm 10 đỉnh và 12 cạnh trước khi in.
if len(nodes) != 10 or len(edges) != 12:
    # ValueError báo không đạt điều kiện số bản ghi, cạnh hoặc tính nhất quán của đồ thị.
    raise ValueError("Cần đúng 10 người và 12 quan hệ.")
# graph.values() là mọi set kề; map(len, ...) tính số hàng xóm từng đỉnh; sum() cộng tổng bậc, phải bằng 2×số cạnh.
if sum(map(len, graph.values())) != 2 * len(edges):
    # ValueError báo không đạt điều kiện số bản ghi, cạnh hoặc tính nhất quán của đồ thị.
    raise ValueError("Đồ thị vô hướng phải ghi hai đầu mỗi cạnh.")
print("Người:", len(nodes))
print("Quan hệ:", len(edges))
# Set kề A không bảo đảm thứ tự; sorted() xếp chữ cái, join() ghép tên để in.
print("Bạn của A:", ", ".join(sorted(graph["A"])))
# len() trả bậc của đỉnh A, tức số hàng xóm trực tiếp.
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

**Tình huống thực tế:** Ứng dụng ghép nhóm có **12 hồ sơ kỹ năng H01–H12**; mỗi hồ sơ ghi những kỹ năng người đó khai, như Python, AI, SQL, Math, Data và Cloud. H01 khai `Python` hai lần nhưng đó vẫn là **một kỹ năng**. Người quản lý chọn H01 làm hồ sơ mẫu, muốn biết mức giống nhau về kỹ năng giữa H01 và H02, đồng thời tìm học viên có bộ kỹ năng **giống H01 nhất** trong 11 người còn lại; nếu bằng điểm phải quyết định thứ tự ổn định.

**Vì sao chọn cách này?** **Jaccard** đo mức độ giống nhau giữa **hai tập**: xem chúng chia sẻ bao nhiêu kỹ năng so với tất cả kỹ năng khác nhau của cả hai người. `set()` loại `Python` bị lặp trong hồ sơ H01 trước khi so. Phép **giao** `&` cho kỹ năng chung, phép **hợp** `|` cho các kỹ năng thuộc ít nhất một người; ví dụ chia sẻ một kỹ năng trong tổng ba kỹ năng khác nhau nghĩa là giống một phần ba. Nếu hai tập đều rỗng, chương trình trả 0 thay vì chia cho 0. Danh sách ứng viên được sắp theo điểm từ cao xuống; nếu đồng điểm, mã học viên nhỏ hơn được xếp trước, tránh kết quả thay đổi do thứ tự dữ liệu.

**Quy trình:**
1. Tạo 12 dòng hồ sơ, mỗi hồ sơ là tập kỹ năng.
2. Viết hàm Jaccard dùng độ lớn phần giao và hợp.
3. Tính điểm H01–H02 và tìm người gần nhất với H01.

**No Note — Không chú thích**

```python
profiles = [{"id":"H01","skills":["Python","AI","Python"]},{"id":"H02","skills":["AI","SQL"]},{"id":"H03","skills":["SQL","Math"]},{"id":"H04","skills":["Math","Data"]},{"id":"H05","skills":["Data","Cloud","Python"]},{"id":"H06","skills":["Cloud","Python"]},{"id":"H07","skills":["Python","AI"]},{"id":"H08","skills":["AI","SQL"]},{"id":"H09","skills":["SQL","Math","Python"]},{"id":"H10","skills":["Math","Data"]},{"id":"H11","skills":["Data","Cloud"]},{"id":"H12","skills":["Cloud","Python"]}]
def jaccard(first, second):
    a, b = set(first), set(second)
    union = a | b
    if union:
        return len(a & b) / len(union)
    return 0.0
reference = profiles[0]["skills"]
score = jaccard(reference, profiles[1]["skills"])
ranked = []
for person in profiles[1:]:
    ranked.append((person["id"], jaccard(reference, person["skills"])))
def sort_by_score(row):
    return (-row[1], row[0])
ranked.sort(key=sort_by_score)
if len(profiles) != 12:
    raise ValueError("Cần đúng 12 hồ sơ kỹ năng.")
print("Hồ sơ:", len(profiles))
print(f"Jaccard H01-H02: {score:.2f}")
print("Gần H01 nhất:", ranked[0][0], f"{ranked[0][1]:.2f}")
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tính Jaccard kỹ năng từ 12 hồ sơ và xếp người gần hồ sơ H01 nhất.
# Dữ liệu: 12 dict id/skills, một số kỹ năng bị lặp trong list; H01 là hồ sơ tham chiếu.
# 12 hồ sơ kỹ năng, mỗi row chứa id và list skills; Python có thể lặp trong một hồ sơ.
profiles = [{"id":"H01","skills":["Python","AI","Python"]},{"id":"H02","skills":["AI","SQL"]},{"id":"H03","skills":["SQL","Math"]},{"id":"H04","skills":["Math","Data"]},{"id":"H05","skills":["Data","Cloud","Python"]},{"id":"H06","skills":["Cloud","Python"]},{"id":"H07","skills":["Python","AI"]},{"id":"H08","skills":["AI","SQL"]},{"id":"H09","skills":["SQL","Math","Python"]},{"id":"H10","skills":["Math","Data"]},{"id":"H11","skills":["Data","Cloud"]},{"id":"H12","skills":["Cloud","Python"]}]
# Hàm trả mức giống nhau từ 0 đến 1 dựa trên tập kỹ năng, không dựa số lần lặp.
def jaccard(first, second):
    # set() loại kỹ năng trùng nội bộ trước khi so sánh.
    a, b = set(first), set(second)
    # | hợp hai tập, chứa mọi kỹ năng có ở ít nhất một người, không trùng.
    union = a | b
    # Set rỗng được xem là False; kiểm trước chia để tránh chia cho 0 khi cả hai người không có kỹ năng.
    if union:
        # & lấy giao kỹ năng chung; tỷ lệ số kỹ năng chung / số kỹ năng khác nhau trong hợp là Jaccard.
        return len(a & b) / len(union)
    # Hai tập cùng rỗng được quy ước độ giống 0 trong ví dụ này (cần nêu rõ quy ước).
    return 0.0
# [0] lấy H01, ['skills'] lấy danh sách kỹ năng của H01.
reference = profiles[0]["skills"]
# [1] là H02; so H01 với H02 để minh họa điểm.
score = jaccard(reference, profiles[1]["skills"])
ranked = []
# [1:] bỏ hồ sơ H01 để không tự so H01 với chính mình.
for person in profiles[1:]:
    # append() lưu tuple (mã người, điểm Jaccard so với H01).
    ranked.append((person["id"], jaccard(reference, person["skills"])))
# Hàm key nhận một tuple (mã, điểm), quy định cách sắp xếp.
def sort_by_score(row):
    # row[1] là điểm; dấu âm đưa điểm lớn lên trước khi sort tăng; row[0] là mã phá hòa theo ABC.
    return (-row[1], row[0])
# sort(key=...) sắp trực tiếp list ranked theo khóa vừa định nghĩa.
ranked.sort(key=sort_by_score)
if len(profiles) != 12:
    # ValueError báo không đạt điều kiện số bản ghi, cạnh hoặc tính nhất quán của đồ thị.
    raise ValueError("Cần đúng 12 hồ sơ kỹ năng.")
print("Hồ sơ:", len(profiles))
print(f"Jaccard H01-H02: {score:.2f}")
# [0] lấy người đầu bảng xếp hạng, [0] tiếp lấy mã và [1] lấy điểm; :.2f in hai chữ số thập phân.
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

**Tình huống thực tế:** Một câu lạc bộ có **15 học viên A đến O** và **15 mối quan hệ hai chiều** được ghi nhận. Các mối liên hệ tạo hai nhóm tách biệt: một nhóm từ A đến G và một nhóm từ H đến O. Điều phối viên muốn biết có bao nhiêu **cụm bạn bè nối được với nhau qua một hoặc nhiều người trung gian**, mỗi cụm lớn bao nhiêu người và liệu A có thể liên hệ nối tiếp tới O hay không.

**Vì sao chọn cách này?** **Thành phần liên thông** là một nhóm đỉnh mà từ một người có thể lần theo các liên hệ hai chiều để đến bất kỳ người nào khác trong nhóm, kể cả phải qua bạn trung gian. **DFS/BFS** là hai cách đi thăm lần lượt các người có thể tới; dùng set `visited` đánh dấu người đã gặp để không đi lòng vòng hay đếm lại. Khi hết người có thể thăm, ta hoàn thành một cụm rồi bắt đầu từ người chưa thăm của cụm khác. A và O nằm ở hai cụm riêng trong dữ liệu này nên không có đường nối; chỉ đếm số quan hệ chưa đủ để biết ai liên hệ được với ai.

**Quy trình:**
1. Dựng danh sách kề từ 15 cạnh; mỗi quan hệ ghi cả hai chiều.
2. Duyệt những đỉnh chưa thăm để thu từng cụm kết nối.
3. Sắp các kích thước cụm và kiểm tra A/O có cùng cụm không.

**No Note — Không chú thích**

```python
edges = [["A","B"],["B","C"],["C","D"],["A","D"],["D","E"],["E","F"],["F","G"],["H","I"],["I","J"],["J","K"],["K","L"],["H","L"],["L","M"],["M","N"],["N","O"]]
vertex_set = set()
for edge in edges:
    for name in edge:
        vertex_set.add(name)
vertices = sorted(vertex_set)
graph = {}
for vertex in vertices:
    graph[vertex] = set()
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
if len(edges) != 15 or len(vertices) != 15:
    raise ValueError("Đồ thị cần 15 cạnh và 15 đỉnh.")
print("Cạnh:", len(edges))
print("Cụm:", len(components))
sizes = []
for group in components:
    sizes.append(len(group))
sizes.sort(reverse=True)
labels = []
for size in sizes:
    labels.append(str(size))
connected = False
for group in components:
    if {"A", "O"} <= group:
        connected = True
        break
print("Kích thước cụm:", ", ".join(labels))
print("A kết nối O:", connected)
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Tìm các thành phần liên thông trong đồ thị 15 cạnh bằng ngăn xếp DFS.
# Dữ liệu: 15 cạnh vô hướng nối 15 đỉnh A..O thành nhiều cụm; cần biết A có cùng cụm với O hay không.
# 15 list đôi là các cạnh vô hướng; mỗi đầu nối vào set hàng xóm của nhau.
edges = [["A","B"],["B","C"],["C","D"],["A","D"],["D","E"],["E","F"],["F","G"],["H","I"],["I","J"],["J","K"],["K","L"],["H","L"],["L","M"],["M","N"],["N","O"]]
# Set thu các tên đỉnh xuất hiện trong cạnh, bỏ trùng.
vertex_set = set()
# Duyệt mỗi cặp cạnh để lấy hai đỉnh.
for edge in edges:
    for name in edge:
        # add() đưa đỉnh vào set duy nhất.
        vertex_set.add(name)
# sorted() tạo list đỉnh theo thứ tự cố định để duyệt thành phần.
vertices = sorted(vertex_set)
graph = {}
for vertex in vertices:
    # Tạo set kề rỗng cho từng đỉnh.
    graph[vertex] = set()
for a, b in edges:
    # Thêm hai chiều a→b và b→a để biểu diễn cạnh vô hướng.
    graph[a].add(b)
    graph[b].add(a)
# seen là tập đỉnh đã duyệt toàn đồ thị, components lưu tập đỉnh từng cụm.
seen, components = set(), []
for start in vertices:
    # Bỏ đỉnh đã thuộc cụm tìm trước, tránh ghi cùng cụm hai lần.
    if start in seen:
        continue
    # stack là ngăn xếp LIFO để duyệt DFS; members lưu đỉnh trong cụm hiện tại.
    stack, members = [start], set()
    # Còn đỉnh chờ xử lý thì tiếp tục đi sâu.
    while stack:
        # pop() không chỉ số lấy và xóa phần tử cuối stack, mô phỏng DFS.
        node = stack.pop()
        # Bỏ qua đỉnh đã xử lý để tránh vòng lặp vô hạn trong chu trình.
        if node in seen:
            continue
        # Đánh dấu đỉnh đã duyệt, dùng chung cho cả các cụm.
        seen.add(node)
        # Ghi nhận node thuộc cụm hiện tại.
        members.add(node)
        # graph[node]-seen lấy hàng xóm chưa duyệt; extend() nối nhiều đỉnh vào stack. Set không có thứ tự, nhưng số cụm không đổi.
        stack.extend(graph[node] - seen)
    # Hoàn tất một cụm, đưa set thành viên vào danh sách các cụm.
    components.append(members)
# Kiểm đúng số cạnh và đỉnh nguồn.
if len(edges) != 15 or len(vertices) != 15:
    # ValueError báo không đạt điều kiện số bản ghi, cạnh hoặc tính nhất quán của đồ thị.
    raise ValueError("Đồ thị cần 15 cạnh và 15 đỉnh.")
print("Cạnh:", len(edges))
print("Cụm:", len(components))
sizes = []
for group in components:
    # len(group) đếm số đỉnh mỗi cụm, append() ghi kích cỡ.
    sizes.append(len(group))
# sort(reverse=True) xếp kích cỡ cụm giảm dần tại chỗ.
sizes.sort(reverse=True)
labels = []
for size in sizes:
    # str() đổi số thành chuỗi vì join() chỉ nối chuỗi.
    labels.append(str(size))
connected = False
for group in components:
    # <= giữa set nghĩa tập con: True nếu CẢ A và O đều thuộc cùng group.
    if {"A", "O"} <= group:
        connected = True
        # break dừng khi tìm được cụm có đủ hai đỉnh cần kiểm.
        break
# join() ghép chuỗi kích thước cụm có dấu phẩy.
print("Kích thước cụm:", ", ".join(labels))
print("A kết nối O:", connected)
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

**Tình huống thực tế:** Hệ thống gợi ý bạn học có **18 hồ sơ U01–U18**, mỗi người nhập danh sách kỹ năng. U01 là người cần tìm bạn phù hợp; một số kỹ năng trong hồ sơ được ghi lặp, còn U14 **chưa khai kỹ năng nào**. Người quản lý cần gợi ý **ba người giống U01 nhất** theo kỹ năng, đồng thời báo còn bao nhiêu hồ sơ thiếu thông tin. Hồ sơ trống không được hiểu là người đó thực sự không có khả năng.

**Vì sao chọn cách này?** Hàm so sánh Jaccard trong bài chuyển mỗi danh sách kỹ năng sang set, để kỹ năng bị nhập lặp chỉ được tính một lần. Sau đó nó xem **kỹ năng chung** chiếm bao nhiêu trong toàn bộ kỹ năng khác nhau của hai người; hai tập không có phần tử thì trả 0 để tránh lỗi chia cho 0. U14 có danh sách rỗng nên bài **báo là thiếu dữ liệu**, không kết luận người này không có kỹ năng. Chương trình tính điểm U01 với từng người còn lại, sắp theo **điểm giảm dần**, nếu hòa thì theo **mã tăng dần**, rồi lấy ba mã đầu; đây là gợi ý dựa trên khai báo kỹ năng, chưa phải đánh giá năng lực thực tế.

**Quy trình:**
1. Chuẩn hóa kỹ năng về Set trên 18 hồ sơ.
2. Tính tương đồng U01 với 17 người còn lại, kiểm tra tập rỗng.
3. Sắp xếp ổn định, in ba ứng viên đầu và số hồ sơ thiếu kỹ năng.

**No Note — Không chú thích**

```python
people = [{"id":"U01","skills":["Python","SQL","Python"]},{"id":"U02","skills":["AI","Math"]},{"id":"U03","skills":["SQL","Data"]},{"id":"U04","skills":["Math","Cloud","Python"]},{"id":"U05","skills":["Data","Vision"]},{"id":"U06","skills":["Cloud","NLP"]},{"id":"U07","skills":["Vision","Python","Python"]},{"id":"U08","skills":["NLP","AI"]},{"id":"U09","skills":["Python","SQL"]},{"id":"U10","skills":["AI","Math","Python"]},{"id":"U11","skills":["SQL","Data"]},{"id":"U12","skills":["Math","Cloud"]},{"id":"U13","skills":["Data","Vision","Python"]},{"id":"U14","skills":[]},{"id":"U15","skills":["Vision","Python"]},{"id":"U16","skills":["NLP","AI","Python"]},{"id":"U17","skills":["Python","SQL"]},{"id":"U18","skills":["AI","Math"]}]
def similarity(a, b):
    a, b = set(a), set(b)
    total = a | b
    if total:
        return len(a & b) / len(total)
    return 0.0
base = people[0]["skills"]
ranked = []
for person in people[1:]:
    ranked.append((person["id"], similarity(base, person["skills"])))
def ranking_key(item):
    return (-item[1], item[0])
ranked.sort(key=ranking_key)
if len(people) != 18:
    raise ValueError("Cần đúng 18 hồ sơ kỹ năng.")
print("Hồ sơ:", len(people))
missing_skills = 0
for person in people:
    if not person["skills"]:
        missing_skills += 1
print("Thiếu kỹ năng:", missing_skills)
for uid, score in ranked[:3]:
    print(f"{uid}: {score:.2f}")
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Xếp hạng người có kỹ năng giống U01 từ 18 hồ sơ, xử lý list kỹ năng thiếu.
# Dữ liệu: 18 dict id/skills; người U14 có list rỗng, có hồ sơ lặp kỹ năng Python.
# 18 hồ sơ gồm id và list skills, kỹ năng lặp không được tăng độ tương đồng.
people = [{"id":"U01","skills":["Python","SQL","Python"]},{"id":"U02","skills":["AI","Math"]},{"id":"U03","skills":["SQL","Data"]},{"id":"U04","skills":["Math","Cloud","Python"]},{"id":"U05","skills":["Data","Vision"]},{"id":"U06","skills":["Cloud","NLP"]},{"id":"U07","skills":["Vision","Python","Python"]},{"id":"U08","skills":["NLP","AI"]},{"id":"U09","skills":["Python","SQL"]},{"id":"U10","skills":["AI","Math","Python"]},{"id":"U11","skills":["SQL","Data"]},{"id":"U12","skills":["Math","Cloud"]},{"id":"U13","skills":["Data","Vision","Python"]},{"id":"U14","skills":[]},{"id":"U15","skills":["Vision","Python"]},{"id":"U16","skills":["NLP","AI","Python"]},{"id":"U17","skills":["Python","SQL"]},{"id":"U18","skills":["AI","Math"]}]
# Hàm tự định nghĩa so Jaccard của hai bộ kỹ năng.
def similarity(a, b):
    # set() bỏ kỹ năng trùng, bảo đảm so tập các loại kỹ năng.
    a, b = set(a), set(b)
    # | là hợp hai tập, đếm mọi kỹ năng có ở ít nhất một người.
    total = a | b
    # Không chia cho 0 khi hai tập cùng rỗng; set rỗng được xem là False.
    if total:
        # & lấy tập chung; chia số loại chung cho số loại trong hợp, trả tỷ lệ 0..1.
        return len(a & b) / len(total)
    # Quy ước Jaccard=0 nếu hợp rỗng trong tài liệu này.
    return 0.0
# [0] là kỹ năng của U01, dùng làm tham chiếu.
base = people[0]["skills"]
ranked = []
# [1:] bỏ U01 để chỉ xếp những người còn lại.
for person in people[1:]:
    # append() thêm tuple (mã người, điểm gần U01).
    ranked.append((person["id"], similarity(base, person["skills"])))
# Hàm key trả tiêu chí xếp dựa vào (mã, điểm).
def ranking_key(item):
    # Dấu âm của điểm để xếp cao trước; tên mã phá hòa tăng dần.
    return (-item[1], item[0])
# sort() xếp ngay list theo hàm key; không thay đổi people.
ranked.sort(key=ranking_key)
if len(people) != 18:
    # ValueError báo không đạt điều kiện số bản ghi, cạnh hoặc tính nhất quán của đồ thị.
    raise ValueError("Cần đúng 18 hồ sơ kỹ năng.")
print("Hồ sơ:", len(people))
missing_skills = 0
for person in people:
    # not list đúng khi list rỗng, đếm hồ sơ chưa khai kỹ năng.
    if not person["skills"]:
        # Đếm người không có kỹ năng ghi nhận, khác với người không trùng kỹ năng với U01.
        missing_skills += 1
print("Thiếu kỹ năng:", missing_skills)
# [:3] lấy ba người đầu, không gồm vị trí 3; :.2f định dạng điểm hai số sau dấu thập phân.
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

**Tình huống thực tế:** Mạng chuyển tiếp thông báo có **20 đường liên kết một chiều** giữa các trạm A đến S. Mỗi dòng `(trạm gửi, trạm nhận)` nghĩa là gửi được theo chiều đó, không mặc nhiên gửi ngược lại; riêng trạm R chỉ có đường tới S. Kỹ thuật viên cần tìm đường từ **A đến K** có ít chặng nhất, kiểm tra **R có tới được K** không, và so mức trùng nhau giữa hai tập trạm nhận trực tiếp của **A và B**.

**Vì sao chọn cách này?** Đây là **đồ thị có hướng**: cạnh A→B chỉ cho phép chuyển từ A sang B, không tự suy ra đường B→A. **BFS** (tìm kiếm theo chiều rộng) thử các trạm ở khoảng cách **một chặng**, rồi hai chặng, rồi ba chặng; trong mạng mà mỗi chặng tính như nhau, lần đầu tới K cho một đường **ít cạnh nhất**. `deque` giữ các điểm cần xét theo thứ tự đã vào hàng, `visited` tránh thử lại trạm và đường đã thăm. Trạm R chỉ dẫn tới S, không nối tới K nên không có đường như yêu cầu. **Jaccard** trên tập hàng xóm của A/B là câu hỏi khác: mức giống nhau của các trạm nhận **ngay trong một bước**, không phản ánh việc A và B có cùng đường nhiều chặng hay không.

**Quy trình:**
1. Tạo danh sách kề **một chiều** từ 20 cạnh và xác nhận trạm nguồn/đích.
2. Dùng BFS có kiểm soát đỉnh đã thăm để tìm đường A→K và R→K.
3. Tính Jaccard tập trạm nhận trực tiếp A/B, báo đường và hai kết quả.

**No Note — Không chú thích**

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
union = a | b
if union:
    score = len(a & b) / len(union)
else:
    score = 0.0
if len(edges) != 20:
    raise ValueError("Cần đủ 20 cạnh có hướng.")
print("Cạnh có hướng:", len(edges))
print("Đường A-K:", " -> ".join(path))
print("Số cạnh đường:", len(path) - 1)
print("R tới K:", shortest("R", "K") is not None)
print(f"Jaccard kề A/B: {score:.2f}")
```

**Code có chú thích — Giải thích từng bước**

```python
# Mục đích: Dùng BFS tìm đường đi ngắn nhất theo số cạnh có hướng giữa A và K, so Jaccard danh sách kề A/B.
# Dữ liệu: 20 cung [nguồn,đích] có hướng, một cung R→S tách rời; A và K có thể nối qua nhiều bước.
# deque là hàng đợi hai đầu, popleft() lấy đầu hiệu quả cho duyệt BFS theo từng lớp.
from collections import deque
# Mỗi bộ nguồn-đích là một CUNG CÓ HƯỚNG, không mặc định thêm chiều ngược.
edges = [["A","B"],["A","C"],["B","D"],["C","D"],["D","E"],["E","F"],["B","G"],["G","H"],["H","I"],["I","J"],["F","J"],["J","K"],["C","L"],["L","M"],["M","N"],["N","O"],["O","K"],["K","P"],["P","Q"],["R","S"]]
# Dictionary ánh xạ đỉnh nguồn sang set các đích đi được từ đó.
graph = {}
for source, destination in edges:
    # setdefault(k,set()) lấy set kề hiện có hoặc tạo rỗng nếu thiếu; add() thêm cung source→destination duy nhất.
    graph.setdefault(source, set()).add(destination)
# Hàm BFS trả list các đỉnh trên đường ngắn nhất theo số CẠNH; trả None nếu không tới được.
def shortest(start, end):
    # Hàng đợi chứa tuple (đỉnh đang xét, danh sách đường đi tới đỉnh); ban đầu đường chỉ có start.
    queue = deque([(start, [start])])
    # Set các đỉnh đã đưa vào hàng đợi, tránh thăm lại hoặc vòng lặp chu trình.
    visited = {start}
    # BFS xử lý cho đến khi hàng đợi hết hoặc tìm thấy đích.
    while queue:
        # popleft() lấy phần tử ĐẦU hàng đợi FIFO, giúp BFS duyệt đường ít cạnh trước.
        node, path = queue.popleft()
        # Đến đích thì trả ngay đường được lấy ra; do BFS FIFO nên đây là đường ngắn nhất theo cạnh.
        if node == end:
            return path
        # get(node,set()) lấy hàng xóm có hướng hoặc tập rỗng nếu đỉnh chưa có khóa; sorted() cố định thứ tự đi khi nhiều đường đồng độ dài.
        for neighbor in sorted(graph.get(node, set())):
            # Không mở rộng lại đỉnh đã vào queue, tránh lặp.
            if neighbor not in visited:
                # Ghi nhận đỉnh ngay khi thêm vào queue.
                visited.add(neighbor)
                # append() thêm vào CUỐI queue; path+[neighbor] tạo list đường mới, không sửa path cũ.
                queue.append((neighbor, path + [neighbor]))
    # Trả None khi đã vét hết các đỉnh có thể đi mà không thấy end.
    return None
# Tìm đường A→K theo đúng chiều cung, không phải đường vô hướng.
path = shortest("A", "K")
# Nếu đỉnh A/B không có hàng xóm thì get trả set rỗng để phép toán tập không lỗi.
a, b = graph.get("A", set()), graph.get("B", set())
# | hợp hai set hàng xóm của A và B, dùng làm mẫu số Jaccard.
union = a | b
if union:
    # & giao hàng xóm chung; chia cho số hàng xóm khác nhau trong hợp, chỉ khi union không rỗng.
    score = len(a & b) / len(union)
else:
    score = 0.0
# Xác nhận đủ 20 cung nguồn.
if len(edges) != 20:
    # ValueError báo không đạt điều kiện số bản ghi, cạnh hoặc tính nhất quán của đồ thị.
    raise ValueError("Cần đủ 20 cạnh có hướng.")
print("Cạnh có hướng:", len(edges))
# join() ghép các đỉnh dọc đường tìm được, mũi tên thể hiện chiều di chuyển.
print("Đường A-K:", " -> ".join(path))
# Một đường có n đỉnh chứa n−1 cạnh, nên trừ 1 khi báo độ dài.
print("Số cạnh đường:", len(path) - 1)
# is not None kiểm có đường R→K; False vì thành phần R→S không dẫn tới K.
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

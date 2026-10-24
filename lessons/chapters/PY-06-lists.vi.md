# PY-06 — List, chỉ số, cắt danh sách và sắp xếp


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **List** — danh sách; **Index** — chỉ số.

`Vòng lặp → List → Vector/Array`

Sau khi học vòng lặp, ta dùng List để lưu nhiều giá trị trong cùng một biến. Có thể thêm, xóa, sửa, sắp xếp và duyệt từng phần tử.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Giải thích dễ nhớ |
|---|---|---|
| List | danh sách | Tập hợp có thứ tự, có thể thay đổi |
| Index | chỉ số | Vị trí tính từ 0 để lấy phần tử |
| Slice | cắt lát | Lấy đoạn phần tử theo start:stop |
| Mutability | khả năng sửa | Có thể cập nhật phần tử của danh sách |

## 3. Hàm và cú pháp Python

**Từ vựng trong mục:** **Function** — hàm; **Argument** — đối số.

| Hàm / cú pháp | Mục đích và lựa chọn liên quan |
|---|---|
| `append(), extend(), insert()` | Thêm từng phần tử hoặc nhiều phần tử vào danh sách |
| `pop(), remove(), del` | Xóa theo vị trí hoặc giá trị |
| `sort(), sorted()` | Sắp xếp tại chỗ hoặc tạo danh sách mới |
| `items[start:stop]` | Lấy vùng con không bao gồm stop |

## 4. Khái niệm liên quan

### 4.1. List

**Từ vựng trong mục:** **List** — danh sách.

List là danh sách có thứ tự, có thể chứa nhiều giá trị và có thể chỉnh sửa. Ví dụ `[1, 2]` có hai phần tử. Dùng dấu ngoặc vuông `[]` để tạo list.

```python
a=[1,2]
print(a)
```

**Kết quả khi chạy:**

```text
[1, 2]
```

### 4.2. Index

**Từ vựng trong mục:** **Index** — chỉ số.

Chỉ số cho biết phần tử nằm ở đâu trong list. Python đếm từ `0`, nên `[8, 9][0]` lấy số `8`. Chỉ số `-1` lấy phần tử cuối.

```python
print([8,9][0])
```

**Kết quả khi chạy:**

```text
8
```

### 4.3. Slice

**Từ vựng trong mục:** **Slice** — cắt lát.

Cắt danh sách lấy một đoạn mà không thay đổi danh sách gốc. `[1, 2, 3][:2]` lấy từ đầu tới trước chỉ số 2, cho `[1, 2]`.

```python
print([1,2,3][:2])
```

**Kết quả khi chạy:**

```text
[1, 2]
```

### 4.4. Mutability

**Từ vựng trong mục:** **Mutability** — khả năng sửa.

List có thể sửa nội dung sau khi tạo. Với `a = [1, 2]`, câu lệnh `a[1] = 5` đổi phần tử thứ hai; kết quả là `[1, 5]`.

```python
a=[1,2]
a[1]=5
print(a)
```

**Kết quả khi chạy:**

```text
[1, 5]
```

## 5. Năm tình huống lập trình thực tế

### Tình huống 1 — Giỏ hàng

**Từ vựng trong mục:** **List** — danh sách.

**Tình huống thực tế:** Một cửa hàng đang có giỏ hàng gồm `milk` (sữa) và `bread` (bánh mì). Khách muốn thêm `rice` (gạo) vào cuối giỏ.

**Yêu cầu:** In danh sách hàng sau khi thêm gạo.

**Vì sao chọn cách giải này?** `append()` thêm một phần tử vào cuối list mà vẫn giữ các món trước đó.

**Quy trình giải:**

1. Tạo list `basket` gồm sữa và bánh mì.
2. Gọi `basket.append("rice")`.
3. In toàn bộ giỏ hàng.

```python
basket=["milk","bread"]
basket.append("rice")
print(basket)
```

**Kết quả khi chạy:**

```text
['milk', 'bread', 'rice']
```

**Kết quả:** `['milk', 'bread', 'rice']` — giỏ có ba món theo đúng thứ tự.

### Tình huống 2 — Lấy hai ưu tiên cao

**Từ vựng trong mục:** **Index** — chỉ số.

**Tình huống thực tế:** Một đội hỗ trợ nhận điểm ưu tiên của bốn yêu cầu là `[2, 9, 4, 7]`; điểm càng lớn thì yêu cầu càng cần xử lý trước.

**Yêu cầu:** In hai điểm ưu tiên cao nhất mà không thay đổi list gốc.

**Vì sao chọn cách giải này?** `sorted(..., reverse=True)` tạo danh sách mới từ cao xuống thấp, rồi `[:2]` lấy hai giá trị đầu.

**Quy trình giải:**

1. Lưu bốn điểm vào `scores`.
2. Sắp xếp giảm dần bằng `sorted(scores, reverse=True)`.
3. Cắt `[:2]` và in kết quả.

```python
scores=[2,9,4,7]
print(sorted(scores,reverse=True)[:2])
```

**Kết quả khi chạy:**

```text
[9, 7]
```

**Kết quả:** `[9, 7]` — hai mức ưu tiên cao nhất. List `scores` gốc không bị thay đổi.

### Tình huống 3 — Lọc điểm đạt

**Từ vựng trong mục:** **Slice** — cắt lát.

**Tình huống thực tế:** Trung tâm đào tạo có điểm của bốn học viên là `[4, 7, 9, 3]` trên thang 10. Điểm đạt yêu cầu là từ 5 trở lên.

**Yêu cầu:** Tạo list mới chỉ chứa điểm đạt.

**Vì sao chọn cách giải này?** List comprehension `[x for x in scores if x >= 5]` duyệt từng điểm và chỉ giữ giá trị đạt ngưỡng.

**Quy trình giải:**

1. Lưu điểm vào `scores`.
2. Với mỗi `x`, kiểm tra `x >= 5`.
3. Thêm các điểm đạt vào `passed` và in list mới.

```python
scores=[4,7,9,3]
passed=[x for x in scores if x>=5]
print(passed)
```

**Kết quả khi chạy:**

```text
[7, 9]
```

**Kết quả:** `[7, 9]` — hai điểm đạt, vẫn giữ thứ tự xuất hiện ban đầu.

### Tình huống 4 — Sửa tồn kho

**Từ vựng trong mục:** **Mutability** — khả năng sửa.

**Tình huống thực tế:** Kho lưu số lượng ba mặt hàng trong list `[8, 6, 9]`. Sau kiểm kê, mặt hàng thứ hai thực tế còn 4 sản phẩm, không phải 6.

**Yêu cầu:** Sửa lại số lượng mặt hàng thứ hai rồi in danh sách tồn kho mới.

**Vì sao chọn cách giải này?** List có thể chỉnh trực tiếp theo chỉ số; mặt hàng thứ hai nằm ở chỉ số `1`.

**Quy trình giải:**

1. Lưu `[8, 6, 9]` vào `stock`.
2. Gán `stock[1] = 4`.
3. In danh sách sau khi sửa.

```python
stock=[8,6,9]
stock[1]=4
print(stock)
```

**Kết quả khi chạy:**

```text
[8, 4, 9]
```

**Kết quả:** `[8, 4, 9]` — chỉ số lượng mặt hàng thứ hai được cập nhật.

### Tình huống 5 — Hàng đợi yêu cầu

**Từ vựng trong mục:** **List** — danh sách.

**Tình huống thực tế:** Bộ phận hỗ trợ đang xử lý ba yêu cầu theo thứ tự `REQ01`, `REQ02`, `REQ03`. Yêu cầu đến trước phải được xử lý trước.

**Yêu cầu:** Lấy yêu cầu đầu hàng đợi ra để xử lý và in danh sách còn lại.

**Vì sao chọn cách giải này?** `pop(0)` lấy và xóa phần tử đầu list; phù hợp để minh họa hàng đợi nhỏ. Với hàng đợi lớn hoặc thường xuyên lấy đầu, `collections.deque` phù hợp hơn.

**Quy trình giải:**

1. Tạo list `queue` theo thứ tự yêu cầu đến.
2. Dùng `pop(0)` lấy yêu cầu đầu vào biến `done`.
3. In mã đã xử lý và list còn lại.

```python
queue=["REQ01","REQ02","REQ03"]
done=queue.pop(0)
print(done,queue)
```

**Kết quả khi chạy:**

```text
REQ01 ['REQ02', 'REQ03']
```

**Kết quả:** `REQ01 ['REQ02', 'REQ03']` — yêu cầu đầu đã được lấy ra, hai yêu cầu còn lại giữ nguyên thứ tự.

## 6. Nhầm lẫn dễ gặp

- Chỉ số list bắt đầu từ `0`; truy cập vượt ngoài list gây `IndexError`.
- `append([3,4])` thêm cả list như một phần tử, còn `extend([3,4])` thêm lần lượt `3` và `4`.
- `list.sort()` sửa list gốc và trả về `None`; `sorted(list)` tạo list mới.
- `pop(0)` sẽ lỗi nếu list rỗng. Với hàng đợi lớn, nên dùng `collections.deque`.
- Cắt list bằng `[:2]` không lấy phần tử có chỉ số `2`.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. What does a Python list store? — List lưu gì?**

A. Multiple ordered values — Nhiều giá trị có thứ tự

B. Only one number — Chỉ một số

C. Only file names — Chỉ tên file

D. A running process — Một tiến trình đang chạy

**Q2. What is the first list index? — Chỉ số đầu tiên của list là bao nhiêu?**

A. 1 — 1

B. 0 — 0

C. -2 — -2

D. 10 — 10

**Q3. What does items[:2] return? — items[:2] lấy gì?**

A. The last two items — Hai phần tử cuối

B. The third item only — Chỉ phần tử thứ ba

C. The first two items — Hai phần tử đầu

D. An empty list always — Luôn là list rỗng

**Q4. Can list elements be replaced? — Có thể thay đổi phần tử list không?**

A. No, lists are fixed — Không, list không sửa được

B. Only after sorting — Chỉ sau khi sắp xếp

C. Only with input() — Chỉ bằng input()

D. Yes, using an index — Có, bằng chỉ số

**Q5. What does append(x) do? — append(x) làm gì?**

A. Adds x at the end — Thêm x vào cuối

B. Removes x — Xóa x

C. Sorts the list — Sắp xếp list

D. Returns the first item — Lấy phần tử đầu

**Q6. How does extend differ from append? — extend khác append như thế nào?**

A. Both delete values — Cả hai xóa dữ liệu

B. extend adds elements from an iterable — extend thêm từng phần tử của một nhóm

C. extend sorts the list — extend sắp xếp list

D. append always fails — append luôn lỗi

**Q7. What does pop(0) do? — pop(0) làm gì?**

A. Removes the last item — Xóa phần tử cuối

B. Copies the list — Sao chép list

C. Removes and returns the first item — Xóa và trả về phần tử đầu

D. Clears all items — Xóa toàn bộ

**Q8. Which operation keeps the original list unchanged? — Cách sắp xếp nào không sửa list gốc?**

A. items.sort() — items.sort()

B. items.reverse() — items.reverse()

C. items.append(2) — items.append(2)

D. sorted(items) — sorted(items)

**Q9. What is the basket after appending rice? — Giỏ hàng sau khi thêm rice là gì?**

A. ['milk', 'bread', 'rice'] — ['milk', 'bread', 'rice']

B. ['rice'] — ['rice']

C. ['milk', 'bread'] — ['milk', 'bread']

D. ['bread', 'rice'] — ['bread', 'rice']

**Q10. What are the two highest priority scores? — Hai điểm ưu tiên cao nhất là gì?**

A. [2, 4] — [2, 4]

B. [9, 7] — [9, 7]

C. [7, 4] — [7, 4]

D. [9, 2] — [9, 2]

**Q11. Which scores pass the threshold of 5? — Những điểm nào đạt ngưỡng 5?**

A. [4, 3] — [4, 3]

B. [4, 7, 9, 3] — [4, 7, 9, 3]

C. [7, 9] — [7, 9]

D. [] — []

**Q12. What is the stock after correcting index 1? — Tồn kho sau khi sửa chỉ số 1 là gì?**

A. [4, 6, 9] — [4, 6, 9]

B. [8, 6, 4] — [8, 6, 4]

C. [8, 6, 9] — [8, 6, 9]

D. [8, 4, 9] — [8, 4, 9]

**Q13. Which request is processed first? — Yêu cầu nào được xử lý trước?**

A. REQ01 — REQ01

B. REQ03 — REQ03

C. REQ02 — REQ02

D. None — Không có

**Q14. What is [8, 9][0]? — [8, 9][0] bằng bao nhiêu?**

A. 9 — 9

B. 8 — 8

C. 0 — 0

D. 2 — 2

**Q15. What is [1, 2, 3][:2]? — [1, 2, 3][:2] bằng gì?**

A. [2, 3] — [2, 3]

B. [1, 2, 3] — [1, 2, 3]

C. [1, 2] — [1, 2]

D. [3] — [3]

**Q16. What happens with a[1] = 5 for a = [1, 2]? — a thay đổi thế nào với a[1] = 5?**

A. [5, 2] — [5, 2]

B. [1, 2] — [1, 2]

C. [1, 2, 5] — [1, 2, 5]

D. [1, 5] — [1, 5]

**Q17. Why use sorted(scores, reverse=True)? — Vì sao dùng sorted(scores, reverse=True)?**

A. To sort descending without changing scores — Để sắp giảm dần mà không sửa scores

B. To clear scores — Để xóa scores

C. To select random scores — Để chọn điểm ngẫu nhiên

D. To convert scores to text — Để đổi điểm thành chữ

**Q18. Which condition retains passing scores? — Điều kiện nào giữ lại điểm đạt?**

A. x < 5 — x < 5

B. x >= 5 — x >= 5

C. x == 0 — x == 0

D. x != x — x != x

**Q19. What happens when pop(0) is called on an empty list? — Gọi pop(0) trên list rỗng sẽ thế nào?**

A. Returns zero — Trả về số 0

B. Returns None — Trả về None

C. Raises IndexError — Báo lỗi IndexError

D. Creates one element — Tạo một phần tử

**Q20. What does list.sort() return? — list.sort() trả về gì?**

A. The sorted copy — Bản sao đã sắp

B. The largest item — Phần tử lớn nhất

C. The original length — Độ dài ban đầu

D. None — None

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **A** | A list stores values in order. | List lưu các giá trị theo thứ tự. |
| Q2 | **B** | Python list indexing starts at zero. | Chỉ số list bắt đầu từ 0. |
| Q3 | **C** | The stop index is excluded. | Không lấy phần tử ở vị trí kết thúc. |
| Q4 | **D** | Lists are mutable. | List có thể thay đổi. |
| Q5 | **A** | append adds one element. | append thêm một phần tử. |
| Q6 | **B** | extend adds multiple supplied elements. | extend thêm từng phần tử được truyền vào. |
| Q7 | **C** | Index zero refers to the first item. | Chỉ số 0 là phần tử đầu. |
| Q8 | **D** | sorted produces a new list. | sorted tạo list mới. |
| Q9 | **A** | append keeps existing elements and adds rice. | append giữ các món cũ và thêm rice. |
| Q10 | **B** | Sort descending and take two items. | Sắp giảm dần rồi lấy hai phần tử. |
| Q11 | **C** | Only scores at least five pass. | Chỉ điểm từ 5 trở lên được giữ. |
| Q12 | **D** | Index one is the second item. | Chỉ số 1 là phần tử thứ hai. |
| Q13 | **A** | pop(0) selects the first request. | pop(0) lấy yêu cầu đầu. |
| Q14 | **B** | Index zero retrieves 8. | Chỉ số 0 lấy số 8. |
| Q15 | **C** | Slicing excludes index 2. | Cắt trước chỉ số 2. |
| Q16 | **D** | The second element is replaced. | Phần tử thứ hai được thay. |
| Q17 | **A** | sorted returns a new list in descending order. | sorted trả về list mới theo thứ tự giảm dần. |
| Q18 | **B** | Five or above meets the threshold. | Từ 5 trở lên là đạt. |
| Q19 | **C** | There is no first element to remove. | List rỗng không có phần tử đầu để lấy. |
| Q20 | **D** | sort changes the list in place and returns None. | sort sửa trực tiếp list và trả về None. |

## 8. Nối sang bài tiếp theo

`Vòng lặp → List → Vector/Array`.

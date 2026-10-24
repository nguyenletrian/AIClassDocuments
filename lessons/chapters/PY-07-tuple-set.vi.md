# PY-07 — Tuple, Set và các phép toán tập hợp


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Tuple** — bộ giá trị; **Set** — tập hợp.

`List → Tuple và Set → Tập hợp/Jaccard`

Sau List, ta học hai cách lưu dữ liệu khác: Tuple giữ thứ tự và không cho sửa phần tử; Set chỉ giữ các phần tử khác nhau, giúp tìm phần chung hoặc gộp hai nhóm.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Giải thích dễ nhớ |
|---|---|---|
| Tuple | bộ giá trị | Dãy có thứ tự không sửa phần tử được |
| Set | tập hợp | Nhóm phần tử không trùng lặp |
| Union | phép hợp | Mọi phần tử có trong ít nhất một tập |
| Intersection | phép giao | Phần tử chung của hai tập |

## 3. Hàm và cú pháp Python

**Từ vựng trong mục:** **Function** — hàm; **Argument** — đối số.

| Hàm / cú pháp | Mục đích và lựa chọn liên quan |
|---|---|
| `tuple(items)` | Lưu một bộ dữ liệu có thứ tự và cố định |
| `set(items)` | Khử giá trị trùng, không giữ thứ tự đáng tin |
| `a.union(b)`, `a.intersection(b)` | Lấy toàn bộ phần tử của hai tập (hợp), hoặc chỉ phần tử chung (giao); tương đương `a \| b` và `a & b` |
| `a - b, a ^ b` | Tìm phần tử còn thiếu hoặc khác nhau |

## 4. Khái niệm liên quan

### 4.1. Tuple

**Từ vựng trong mục:** **Tuple** — bộ giá trị.

Tuple giữ các giá trị theo đúng thứ tự và không thể gán lại từng phần tử. Ví dụ `(2, 3)` có thể lưu tọa độ x, y; lấy phần tử bằng chỉ số như List.

```python
point=(2,3)
print(point)
```

**Kết quả khi chạy:**

```text
(2, 3)
```

### 4.2. Set

**Từ vựng trong mục:** **Set** — tập hợp.

Set chỉ giữ mỗi giá trị một lần. `set([1, 1, 2])` tạo tập chứa `1` và `2`. Set không đảm bảo thứ tự, nên không lấy phần tử bằng chỉ số.

```python
print(set([1,1,2]))
```

**Kết quả khi chạy:**

```text
{1, 2}
```

*Thứ tự các phần tử trong Set khi in có thể khác nhau.*

### 4.3. Union

**Từ vựng trong mục:** **Union** — phép hợp.

Phép hợp gộp các phần tử của hai tập và tự loại phần trùng. `{1, 2} | {2, 3}` cho tập chứa `1`, `2`, `3`.

```python
print({1, 2} | {2, 3})
```

**Kết quả khi chạy:**

```text
{1, 2, 3}
```

*Thứ tự các phần tử trong Set khi in có thể khác nhau.*

### 4.4. Intersection

**Từ vựng trong mục:** **Intersection** — phép giao.

Phép giao chỉ giữ phần tử có mặt trong cả hai tập. `{1, 2} & {2, 3}` cho tập chỉ có phần tử `2`.

```python
print({1,2}&{2,3})
```

**Kết quả khi chạy:**

```text
{2}
```

## 5. Năm tình huống lập trình thực tế

### Tình huống 1 — Khử email trùng

**Từ vựng trong mục:** **Set** — tập hợp; **Duplicate** — trùng lặp.

**Tình huống thực tế:** Ứng dụng gửi thông báo đang có bốn email `a@x.vn`, `b@x.vn`, `a@x.vn`, `c@x.vn`. Địa chỉ `a@x.vn` bị nhập hai lần.

**Yêu cầu:** Đếm có bao nhiêu địa chỉ email khác nhau.

**Vì sao chọn cách giải này?** `set()` bỏ bản ghi giống hệt nhau, `len()` đếm số email còn lại. Cách này chưa xử lý khác biệt chữ hoa/chữ thường.

**Quy trình giải:**

1. Lưu bốn email vào list.
2. Chuyển list thành set để bỏ email bị lặp.
3. Dùng `len()` đếm số email khác nhau.

```python
emails=["a@x.vn","b@x.vn","a@x.vn","c@x.vn"]
print(len(set(emails)))
```

**Kết quả khi chạy:**

```text
3
```

**Kết quả:** `3` — có ba địa chỉ email khác nhau.

### Tình huống 2 — Lưu tọa độ

**Từ vựng trong mục:** **Tuple** — bộ giá trị; **Coordinate** — tọa độ.

**Tình huống thực tế:** Một phần mềm bản đồ lưu điểm có tọa độ `(3, 4)` mét, tính từ gốc `(0, 0)`. Hai giá trị lần lượt là vị trí x và y.

**Yêu cầu:** Lấy x, y từ tuple và tính bình phương khoảng cách đến gốc tọa độ.

**Vì sao chọn cách giải này?** Tuple lưu gọn cặp tọa độ có thứ tự. Công thức `x*x + y*y` tính bình phương khoảng cách, không phải khoảng cách thực.

**Quy trình giải:**

1. Lưu tọa độ vào tuple `point`.
2. Tách tuple thành `x` và `y`.
3. Tính `x*x + y*y` rồi in kết quả.

```python
point=(3,4)
x,y=point
print(x*x+y*y)
```

**Kết quả khi chạy:**

```text
25
```

**Kết quả:** `25` m² — bình phương khoảng cách; khoảng cách thật bằng 5 mét.

### Tình huống 3 — Tìm kỹ năng chung

**Từ vựng trong mục:** **Intersection** — phép giao; **Set** — tập hợp.

**Tình huống thực tế:** Hai nhóm học viên có kỹ năng lần lượt là `{'Python', 'AI', 'SQL'}` và `{'Python', 'Math', 'AI'}`.

**Yêu cầu:** Tìm những kỹ năng có ở cả hai nhóm.

**Vì sao chọn cách giải này?** Phép giao `&` chỉ giữ các phần tử chung giữa hai set.

**Quy trình giải:**

1. Lưu kỹ năng của mỗi nhóm thành một set.
2. Dùng `a & b` để tìm phần tử chung.
3. In tập kỹ năng tìm được.

```python
a={"Python","AI","SQL"}
b={"Python","Math","AI"}
print(a&b)
```

**Kết quả khi chạy:**

```text
{'Python', 'AI'}
```

*Thứ tự các phần tử trong Set khi in có thể khác nhau.*

**Kết quả:** Tập chứa `Python` và `AI`; thứ tự hiển thị của set có thể thay đổi.

### Tình huống 4 — Gộp nhóm chủ đề

**Từ vựng trong mục:** **Union** — phép hợp; **Set** — tập hợp.

**Tình huống thực tế:** Hai nhóm tài liệu được gắn nhãn `{'Python', 'Math'}` và `{'Math', 'AI'}`. Nhân viên cần danh sách chủ đề của cả hai nhóm mà không lặp lại `Math`.

**Yêu cầu:** Gộp các nhãn thành một set chỉ chứa các chủ đề khác nhau.

**Vì sao chọn cách giải này?** Phép hợp `|` lấy tất cả phần tử thuộc một trong hai set và bỏ phần trùng.

**Quy trình giải:**

1. Lưu nhãn của từng nhóm thành set.
2. Dùng `a | b` để gộp.
3. In các nhãn sau khi gộp.

```python
a={"Python","Math"}
b={"Math","AI"}
print(a|b)
```

**Kết quả khi chạy:**

```text
{'Python', 'Math', 'AI'}
```

*Thứ tự các phần tử trong Set khi in có thể khác nhau.*

**Kết quả:** Tập chứa `Python`, `Math`, `AI`; thứ tự in không cố định.

### Tình huống 5 — Liệt kê bài còn thiếu

**Từ vựng trong mục:** **Difference** — hiệu tập hợp; **Set** — tập hợp.

**Tình huống thực tế:** Khóa học yêu cầu ba kỹ năng `Python`, `SQL`, `AI`. Một học viên đã học xong `Python`.

**Yêu cầu:** Liệt kê các kỹ năng học viên còn phải học.

**Vì sao chọn cách giải này?** Hiệu tập hợp `required - done` giữ những kỹ năng bắt buộc chưa có trong tập đã hoàn thành.

**Quy trình giải:**

1. Lưu tập kỹ năng bắt buộc.
2. Lưu tập kỹ năng đã học.
3. Lấy hiệu hai tập và in kết quả.

```python
required={"Python","SQL","AI"}
done={"Python"}
print(required-done)
```

**Kết quả khi chạy:**

```text
{'SQL', 'AI'}
```

*Thứ tự các phần tử trong Set khi in có thể khác nhau.*

**Kết quả:** Tập chứa `SQL` và `AI`; thứ tự in không cố định.

## 6. Nhầm lẫn dễ gặp

- Tuple không cho gán lại từng phần tử như `point[0] = 5`; nếu cần sửa tọa độ, tạo tuple mới.
- Set không có thứ tự cố định, không dùng `my_set[0]` và không dựa vào thứ tự khi in.
- Set chỉ giữ phần tử có thể băm được (hashable); không thể đặt list trực tiếp làm phần tử của set.
- Phép hợp `|` lấy tất cả phần tử; phép giao `&` chỉ lấy phần tử chung; phép trừ `-` tìm phần tử còn thiếu.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer** — đáp án.

**Q1. Which property describes a tuple? — Tuple có đặc điểm gì?**

A. Ordered and cannot be changed in place — Có thứ tự và không sửa trực tiếp được

B. Always removes duplicates — Luôn bỏ phần tử trùng

C. Always sorts numbers — Luôn sắp xếp số

D. Has no positions — Không có vị trí

**Q2. What is the main feature of a set? — Set có đặc điểm chính gì?**

A. Keeps every duplicate — Giữ mọi giá trị trùng

B. Contains unique elements — Chỉ chứa phần tử không trùng

C. Supports index access — Có thể lấy bằng chỉ số

D. Always has sorted order — Luôn theo thứ tự sắp xếp

**Q3. What does set union mean? — Phép hợp tập hợp là gì?**

A. Only common elements — Chỉ phần tử chung

B. Only left-side elements — Chỉ phần tử bên trái

C. All distinct elements from either set — Mọi phần tử khác nhau từ hai tập

D. No elements — Không có phần tử

**Q4. What does intersection return? — Phép giao cho kết quả gì?**

A. All original duplicates — Toàn bộ phần tử trùng gốc

B. Elements in exactly one set — Phần tử chỉ thuộc một tập

C. The larger set — Tập lớn hơn

D. Elements shared by both sets — Phần tử chung của cả hai tập

**Q5. What does tuple([3, 4]) create? — tuple([3, 4]) tạo gì?**

A. (3, 4) — (3, 4)

B. {3, 4} — {3, 4}

C. [3, 4] — [3, 4]

D. 3 — 3

**Q6. What is set([1, 1, 2])? — set([1, 1, 2]) chứa gì?**

A. Three separate items — Ba phần tử khác nhau

B. The elements 1 and 2 — Hai phần tử 1 và 2

C. Only 1 — Chỉ có 1

D. An error — Báo lỗi

**Q7. What does a | b perform on sets? — a | b thực hiện phép nào?**

A. Difference — Hiệu

B. Intersection — Giao

C. Union — Hợp

D. Division — Chia

**Q8. What does a & b perform on sets? — a & b thực hiện phép nào?**

A. Union — Hợp

B. Difference — Hiệu

C. Exclusive-or — Hiệu đối xứng

D. Intersection — Giao

**Q9. How many distinct email addresses are listed? — Có bao nhiêu email khác nhau?**

A. 3 — 3

B. 4 — 4

C. 2 — 2

D. 1 — 1

**Q10. What is x*x + y*y for point (3, 4)? — x*x + y*y bằng bao nhiêu với điểm (3, 4)?**

A. 5 — 5

B. 25 — 25

C. 7 — 7

D. 12 — 12

**Q11. Which skills appear in both groups? — Kỹ năng nào có ở cả hai nhóm?**

A. SQL and Math — SQL và Math

B. Only Python — Chỉ Python

C. Python and AI — Python và AI

D. Only SQL — Chỉ SQL

**Q12. Which subjects are in the union of both groups? — Phép hợp hai nhóm chủ đề gồm gì?**

A. Only Math — Chỉ Math

B. Only Python and AI — Chỉ Python và AI

C. Four duplicate labels — Bốn nhãn có trùng

D. Python, Math, and AI — Python, Math và AI

**Q13. What skills remain to learn? — Những kỹ năng nào còn phải học?**

A. SQL and AI — SQL và AI

B. Python only — Chỉ Python

C. None — Không còn gì

D. Python and SQL — Python và SQL

**Q14. Which expression finds missing skills? — Cách nào tìm kỹ năng còn thiếu?**

A. required & done — required & done

B. required - done — required - done

C. required  —  done

D. required == done — required == done

**Q15. Can a tuple element be reassigned? — Có thể gán lại một phần tử tuple không?**

A. Yes, using append — Có, dùng append

B. Yes, with a set — Có, dùng set

C. No, tuples are immutable — Không, tuple không sửa trực tiếp được

D. Only if it stores strings — Chỉ khi chứa chuỗi

**Q16. Can a set be accessed with [0]? — Có thể lấy phần tử set bằng [0] không?**

A. Yes, always — Có, luôn được

B. Only for strings — Chỉ với chuỗi

C. Only after union — Chỉ sau phép hợp

D. No, sets are not indexed — Không, set không có chỉ số

**Q17. What does a ^ b return for sets? — a ^ b cho kết quả gì?**

A. Elements present in exactly one set — Phần tử chỉ thuộc một trong hai tập

B. Only shared elements — Chỉ phần tử chung

C. All duplicates — Mọi phần tử trùng

D. An ordered tuple — Tuple có thứ tự

**Q18. Does printing a set guarantee order? — In một set có đảm bảo thứ tự không?**

A. Yes, alphabetical — Có, theo chữ cái

B. No, the order is not guaranteed — Không, thứ tự không được đảm bảo

C. Yes, insertion order — Có, theo thứ tự thêm

D. Yes, numerical order — Có, theo số

**Q19. What does a - b contain? — a - b gồm phần tử nào?**

A. Only common elements — Chỉ phần tử chung

B. Everything in b — Toàn bộ phần tử b

C. Elements in a but not b — Phần tử thuộc a nhưng không thuộc b

D. Everything in both — Toàn bộ phần tử hai tập

**Q20. What type suits a fixed coordinate pair? — Kiểu nào phù hợp để lưu cặp tọa độ không đổi?**

A. set — set

B. dict — dict

C. list only — Chỉ list

D. tuple — tuple

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **A** | Tuple elements cannot be reassigned. | Không thể gán lại trực tiếp phần tử của tuple. |
| Q2 | **B** | Sets eliminate duplicate elements. | Set bỏ các phần tử trùng. |
| Q3 | **C** | Union contains elements appearing in either set. | Phép hợp chứa phần tử thuộc ít nhất một tập. |
| Q4 | **D** | Intersection keeps shared elements. | Phép giao giữ phần tử chung. |
| Q5 | **A** | tuple converts the list into a tuple. | tuple đổi list thành tuple. |
| Q6 | **B** | The repeated 1 is removed. | Số 1 trùng được bỏ. |
| Q7 | **C** | The  |  operator computes set union. |
| Q8 | **D** | The & operator computes intersection. | Toán tử & tính phép giao. |
| Q9 | **A** | One email is repeated, leaving three unique addresses. | Một email bị lặp nên còn ba địa chỉ khác nhau. |
| Q10 | **B** | 3 squared plus 4 squared equals 25. | 3 bình phương cộng 4 bình phương bằng 25. |
| Q11 | **C** | The intersection contains Python and AI. | Phép giao cho Python và AI. |
| Q12 | **D** | The union keeps each label once. | Phép hợp chỉ giữ mỗi nhãn một lần. |
| Q13 | **A** | Subtracting completed skills leaves SQL and AI. | Trừ kỹ năng đã học còn SQL và AI. |
| Q14 | **B** | Set difference removes completed skills. | Hiệu tập hợp bỏ các kỹ năng đã hoàn thành. |
| Q15 | **C** | Tuple item assignment raises TypeError. | Gán vào phần tử tuple gây TypeError. |
| Q16 | **D** | Sets do not support positional indexing. | Set không hỗ trợ truy cập theo vị trí. |
| Q17 | **A** | Symmetric difference excludes shared elements. | Hiệu đối xứng bỏ phần tử chung. |
| Q18 | **B** | Sets are unordered collections. | Set là tập hợp không có thứ tự cố định. |
| Q19 | **C** | Difference keeps items exclusive to a. | Phép trừ giữ phần tử của a không có trong b. |
| Q20 | **D** | A tuple stores the ordered coordinate pair. | Tuple lưu cặp tọa độ có thứ tự. |

## 8. Nối sang bài tiếp theo

`List → Tuple và Set → Tập hợp/Jaccard`.

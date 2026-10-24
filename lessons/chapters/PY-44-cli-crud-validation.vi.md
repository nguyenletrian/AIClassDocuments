# PY-44 — Ứng dụng CLI: CRUD, kiểm tra dữ liệu và thống kê hồ sơ


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **CRUD** — tạo/đọc/sửa/xóa; **Validation** — xác minh dữ liệu.

`Dictionary/Function → CRUD → CLI → File/CSV → Data App`

Bài này hệ thống hóa kiến thức đã học thành các thao tác thực hành có đầu vào và đầu ra rõ ràng.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Ý nghĩa |
|---|---|---|
| CRUD | tạo/đọc/sửa/xóa | Bốn thao tác quản lý bản ghi |
| Validation | xác minh dữ liệu | Đảm bảo giá trị đúng giới hạn |
| Lookup | tra cứu | Tìm bản ghi qua khóa |
| Aggregate | tổng hợp | Tính chỉ số từ nhiều hồ sơ |

## 3. Hàm và cách sử dụng

**Từ vựng trong mục:** **Function** — hàm; **Option** — tùy chọn.

| Cú pháp | Mục đích và lựa chọn |
|---|---|
| `dict.get(id)` | Đọc bản ghi và trả mặc định nếu thiếu |
| `dict[id] = record` | Thêm/sửa bản ghi khi đã kiểm tra khóa |
| `dict.pop(id,default)` | Xóa có xử lý mã chưa tồn tại |
| `sum()/max()/min()/sorted()` | Tính thống kê và sắp xếp hồ sơ |

## 4. Khái niệm liên quan và ví dụ nhỏ

### 4.1. CRUD

**Từ vựng trong mục:** **CRUD** — tạo/đọc/sửa/xóa.

Bốn thao tác quản lý bản ghi.

```python
db={'S1':8}
print(db)
```

**Tự kiểm tra:** CRUD nghĩa là gì? **Đáp án:** Bốn thao tác quản lý bản ghi.

### 4.2. Validation

**Từ vựng trong mục:** **Validation** — xác minh dữ liệu.

Đảm bảo giá trị đúng giới hạn.

```python
print(0<=8<=10)
```

**Tự kiểm tra:** Validation nghĩa là gì? **Đáp án:** Đảm bảo giá trị đúng giới hạn.

### 4.3. Lookup

**Từ vựng trong mục:** **Lookup** — tra cứu.

Tìm bản ghi qua khóa.

```python
print({'S1':8}.get('S1'))
```

**Tự kiểm tra:** Lookup nghĩa là gì? **Đáp án:** Tìm bản ghi qua khóa.

### 4.4. Aggregate

**Từ vựng trong mục:** **Aggregate** — tổng hợp.

Tính chỉ số từ nhiều hồ sơ.

```python
print(sum([7,8,9])/3)
```

**Tự kiểm tra:** Aggregate nghĩa là gì? **Đáp án:** Tính chỉ số từ nhiều hồ sơ.

## 5. Năm tình huống thực tế

### Tình huống 1 — Thêm sinh viên

**Từ vựng trong mục:** **CRUD** — tạo/đọc/sửa/xóa.

**Tình huống thực tế:** Một trung tâm đào tạo cần thêm sinh viên cho công việc của mình. Dữ liệu đầu vào: Một hồ sơ S1 mới, điểm 8/10. Hãy xây dựng chương trình thực hiện yêu cầu và trình bày kết quả.

**Vì sao chọn cách này?** Kiểm mã trùng trước khi thêm để không ghi đè


**Quy trình:** Hiểu dữ liệu → chọn lệnh/hàm → thực hiện → kiểm chứng kết quả → ghi hạn chế.

```python
db={}
student_id="S1";score=8
if student_id not in db and 0<=score<=10:
    db[student_id]={"name":"An","score":score}
print(db)
```


### Tình huống 2 — Tra cứu bằng mã

**Từ vựng trong mục:** **Validation** — xác minh dữ liệu.

**Tình huống thực tế:** Một nhóm phân tích dữ liệu cần tra cứu bằng mã cho công việc của mình. Dữ liệu đầu vào: Hai sinh viên mã S1 S2. Hãy xây dựng chương trình thực hiện yêu cầu và trình bày kết quả.

**Vì sao chọn cách này?** Dictionary truy xuất bằng khóa không cần biết thứ tự bản ghi


**Quy trình:** Hiểu dữ liệu → chọn lệnh/hàm → thực hiện → kiểm chứng kết quả → ghi hạn chế.

```python
db={"S1":{"score":8},"S2":{"score":9}}
print(db.get("S3","Not found"))
```


### Tình huống 3 — Cập nhật điểm

**Từ vựng trong mục:** **Lookup** — tra cứu.

**Tình huống thực tế:** Một trung tâm đào tạo cần cập nhật điểm cho công việc của mình. Dữ liệu đầu vào: SV S1 có điểm 7 sửa thành 9. Hãy xây dựng chương trình thực hiện yêu cầu và trình bày kết quả.

**Vì sao chọn cách này?** Ràng buộc 0–10 trước khi thay giá trị


**Quy trình:** Hiểu dữ liệu → chọn lệnh/hàm → thực hiện → kiểm chứng kết quả → ghi hạn chế.

```python
db={"S1":{"score":7}};new_score=9
if 0<=new_score<=10:db["S1"]["score"]=new_score
print(db)
```


### Tình huống 4 — Xóa bản ghi

**Từ vựng trong mục:** **Aggregate** — tổng hợp.

**Tình huống thực tế:** Một nhóm phân tích dữ liệu cần xóa bản ghi cho công việc của mình. Dữ liệu đầu vào: Mã S2 chưa tồn tại. Hãy xây dựng chương trình thực hiện yêu cầu và trình bày kết quả.

**Vì sao chọn cách này?** pop với giá trị mặc định tránh KeyError


**Quy trình:** Hiểu dữ liệu → chọn lệnh/hàm → thực hiện → kiểm chứng kết quả → ghi hạn chế.

```python
db={"S1":{"score":8}}
print(db.pop("S2",None))
```


### Tình huống 5 — Báo cáo điểm lớp

**Từ vựng trong mục:** **CRUD** — tạo/đọc/sửa/xóa.

**Tình huống thực tế:** Một trung tâm đào tạo cần báo cáo điểm lớp cho công việc của mình. Dữ liệu đầu vào: Điểm 7,8,9 trên thang 10. Hãy xây dựng chương trình thực hiện yêu cầu và trình bày kết quả.

**Vì sao chọn cách này?** mean tính trung bình và max xác định điểm cao


**Quy trình:** Hiểu dữ liệu → chọn lệnh/hàm → thực hiện → kiểm chứng kết quả → ghi hạn chế.

```python
scores=[7,8,9]
print({"mean":sum(scores)/len(scores),"max":max(scores)})
```


## 6. Nhầm lẫn cần tránh

Đừng sao chép lệnh khi chưa hiểu dữ liệu hoặc trạng thái môi trường; kết quả thử nghiệm không chứng minh rằng mọi máy và mọi bộ dữ liệu đều giống nhau.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Từ vựng trong mục:** **Question** — câu hỏi; **Answer key** — bảng đáp án.


**Q1. What is CRUD? — Thuật ngữ CRUD là gì?**

A. Another term is Đảm bảo giá trị đúng giới hạn — Đảm bảo giá trị đúng giới hạn

B. It is Bốn thao tác quản lý bản ghi — Bốn thao tác quản lý bản ghi

C. Another term is Tìm bản ghi qua khóa — Tìm bản ghi qua khóa

D. Another term is Tính chỉ số từ nhiều hồ sơ — Tính chỉ số từ nhiều hồ sơ


**Q2. What is Validation? — Thuật ngữ Validation là gì?**

A. It is Đảm bảo giá trị đúng giới hạn — Đảm bảo giá trị đúng giới hạn

B. Another term is Tìm bản ghi qua khóa — Tìm bản ghi qua khóa

C. Another term is Tính chỉ số từ nhiều hồ sơ — Tính chỉ số từ nhiều hồ sơ

D. Another term is Bốn thao tác quản lý bản ghi — Bốn thao tác quản lý bản ghi


**Q3. What is Lookup? — Thuật ngữ Lookup là gì?**

A. Another term is Tính chỉ số từ nhiều hồ sơ — Tính chỉ số từ nhiều hồ sơ

B. Another term is Bốn thao tác quản lý bản ghi — Bốn thao tác quản lý bản ghi

C. Another term is Đảm bảo giá trị đúng giới hạn — Đảm bảo giá trị đúng giới hạn

D. It is Tìm bản ghi qua khóa — Tìm bản ghi qua khóa


**Q4. What is Aggregate? — Thuật ngữ Aggregate là gì?**

A. Another term is Bốn thao tác quản lý bản ghi — Bốn thao tác quản lý bản ghi

B. Another term is Đảm bảo giá trị đúng giới hạn — Đảm bảo giá trị đúng giới hạn

C. It is Tính chỉ số từ nhiều hồ sơ — Tính chỉ số từ nhiều hồ sơ

D. Another term is Tìm bản ghi qua khóa — Tìm bản ghi qua khóa


**Q5. What is dict.get(id) used for? — Cú pháp dict.get(id) dùng để làm gì?**

A. A different function is for Thêm/sửa bản ghi khi đã kiểm tra khóa — Thêm/sửa bản ghi khi đã kiểm tra khóa

B. It is for Đọc bản ghi và trả mặc định nếu thiếu — Đọc bản ghi và trả mặc định nếu thiếu

C. A different function is for Xóa có xử lý mã chưa tồn tại — Xóa có xử lý mã chưa tồn tại

D. A different function is for Tính thống kê và sắp xếp hồ sơ — Tính thống kê và sắp xếp hồ sơ


**Q6. What is dict[id] = record used for? — Cú pháp dict[id] = record dùng để làm gì?**

A. It is for Thêm/sửa bản ghi khi đã kiểm tra khóa — Thêm/sửa bản ghi khi đã kiểm tra khóa

B. A different function is for Xóa có xử lý mã chưa tồn tại — Xóa có xử lý mã chưa tồn tại

C. A different function is for Tính thống kê và sắp xếp hồ sơ — Tính thống kê và sắp xếp hồ sơ

D. A different function is for Đọc bản ghi và trả mặc định nếu thiếu — Đọc bản ghi và trả mặc định nếu thiếu


**Q7. What is dict.pop(id,default) used for? — Cú pháp dict.pop(id,default) dùng để làm gì?**

A. A different function is for Tính thống kê và sắp xếp hồ sơ — Tính thống kê và sắp xếp hồ sơ

B. A different function is for Đọc bản ghi và trả mặc định nếu thiếu — Đọc bản ghi và trả mặc định nếu thiếu

C. A different function is for Thêm/sửa bản ghi khi đã kiểm tra khóa — Thêm/sửa bản ghi khi đã kiểm tra khóa

D. It is for Xóa có xử lý mã chưa tồn tại — Xóa có xử lý mã chưa tồn tại


**Q8. What is sum()/max()/min()/sorted() used for? — Cú pháp sum()/max()/min()/sorted() dùng để làm gì?**

A. A different function is for Đọc bản ghi và trả mặc định nếu thiếu — Đọc bản ghi và trả mặc định nếu thiếu

B. A different function is for Thêm/sửa bản ghi khi đã kiểm tra khóa — Thêm/sửa bản ghi khi đã kiểm tra khóa

C. It is for Tính thống kê và sắp xếp hồ sơ — Tính thống kê và sắp xếp hồ sơ

D. A different function is for Xóa có xử lý mã chưa tồn tại — Xóa có xử lý mã chưa tồn tại


**Q9. Why choose this approach in scenario 1? — Vì sao chọn cách làm trong tình huống 1?**

A. Dictionary truy xuất bằng khóa không cần biết thứ tự bản ghi — Dictionary truy xuất bằng khóa không cần biết thứ tự bản ghi

B. Kiểm mã trùng trước khi thêm để không ghi đè — Kiểm mã trùng trước khi thêm để không ghi đè

C. Ràng buộc 0–10 trước khi thay giá trị — Ràng buộc 0–10 trước khi thay giá trị

D. pop với giá trị mặc định tránh KeyError — pop với giá trị mặc định tránh KeyError


**Q10. Why choose this approach in scenario 2? — Vì sao chọn cách làm trong tình huống 2?**

A. Dictionary truy xuất bằng khóa không cần biết thứ tự bản ghi — Dictionary truy xuất bằng khóa không cần biết thứ tự bản ghi

B. Ràng buộc 0–10 trước khi thay giá trị — Ràng buộc 0–10 trước khi thay giá trị

C. pop với giá trị mặc định tránh KeyError — pop với giá trị mặc định tránh KeyError

D. mean tính trung bình và max xác định điểm cao — mean tính trung bình và max xác định điểm cao


**Q11. Why choose this approach in scenario 3? — Vì sao chọn cách làm trong tình huống 3?**

A. pop với giá trị mặc định tránh KeyError — pop với giá trị mặc định tránh KeyError

B. mean tính trung bình và max xác định điểm cao — mean tính trung bình và max xác định điểm cao

C. Kiểm mã trùng trước khi thêm để không ghi đè — Kiểm mã trùng trước khi thêm để không ghi đè

D. Ràng buộc 0–10 trước khi thay giá trị — Ràng buộc 0–10 trước khi thay giá trị


**Q12. Why choose this approach in scenario 4? — Vì sao chọn cách làm trong tình huống 4?**

A. mean tính trung bình và max xác định điểm cao — mean tính trung bình và max xác định điểm cao

B. Kiểm mã trùng trước khi thêm để không ghi đè — Kiểm mã trùng trước khi thêm để không ghi đè

C. pop với giá trị mặc định tránh KeyError — pop với giá trị mặc định tránh KeyError

D. Dictionary truy xuất bằng khóa không cần biết thứ tự bản ghi — Dictionary truy xuất bằng khóa không cần biết thứ tự bản ghi


**Q13. Why choose this approach in scenario 5? — Vì sao chọn cách làm trong tình huống 5?**

A. Kiểm mã trùng trước khi thêm để không ghi đè — Kiểm mã trùng trước khi thêm để không ghi đè

B. mean tính trung bình và max xác định điểm cao — mean tính trung bình và max xác định điểm cao

C. Dictionary truy xuất bằng khóa không cần biết thứ tự bản ghi — Dictionary truy xuất bằng khóa không cần biết thứ tự bản ghi

D. Ràng buộc 0–10 trước khi thay giá trị — Ràng buộc 0–10 trước khi thay giá trị


**Q14. What input is used in scenario 1? — Tình huống 1 sử dụng đầu vào nào?**

A. Một hồ sơ S1 mới, điểm 8/10 — Một hồ sơ S1 mới, điểm 8/10

B. Hai sinh viên mã S1 S2 — Hai sinh viên mã S1 S2

C. SV S1 có điểm 7 sửa thành 9 — SV S1 có điểm 7 sửa thành 9

D. Mã S2 chưa tồn tại — Mã S2 chưa tồn tại


**Q15. What input is used in scenario 2? — Tình huống 2 sử dụng đầu vào nào?**

A. SV S1 có điểm 7 sửa thành 9 — SV S1 có điểm 7 sửa thành 9

B. Mã S2 chưa tồn tại — Mã S2 chưa tồn tại

C. Điểm 7,8,9 trên thang 10 — Điểm 7,8,9 trên thang 10

D. Hai sinh viên mã S1 S2 — Hai sinh viên mã S1 S2


**Q16. What input is used in scenario 3? — Tình huống 3 sử dụng đầu vào nào?**

A. Mã S2 chưa tồn tại — Mã S2 chưa tồn tại

B. Điểm 7,8,9 trên thang 10 — Điểm 7,8,9 trên thang 10

C. SV S1 có điểm 7 sửa thành 9 — SV S1 có điểm 7 sửa thành 9

D. Một hồ sơ S1 mới, điểm 8/10 — Một hồ sơ S1 mới, điểm 8/10


**Q17. What input is used in scenario 4? — Tình huống 4 sử dụng đầu vào nào?**

A. Điểm 7,8,9 trên thang 10 — Điểm 7,8,9 trên thang 10

B. Mã S2 chưa tồn tại — Mã S2 chưa tồn tại

C. Một hồ sơ S1 mới, điểm 8/10 — Một hồ sơ S1 mới, điểm 8/10

D. Hai sinh viên mã S1 S2 — Hai sinh viên mã S1 S2


**Q18. What input is used in scenario 5? — Tình huống 5 sử dụng đầu vào nào?**

A. Điểm 7,8,9 trên thang 10 — Điểm 7,8,9 trên thang 10

B. Một hồ sơ S1 mới, điểm 8/10 — Một hồ sơ S1 mới, điểm 8/10

C. Hai sinh viên mã S1 S2 — Hai sinh viên mã S1 S2

D. SV S1 có điểm 7 sửa thành 9 — SV S1 có điểm 7 sửa thành 9


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
| Q1 | **B** | It is Bốn thao tác quản lý bản ghi | Bốn thao tác quản lý bản ghi |
| Q2 | **A** | It is Đảm bảo giá trị đúng giới hạn | Đảm bảo giá trị đúng giới hạn |
| Q3 | **D** | It is Tìm bản ghi qua khóa | Tìm bản ghi qua khóa |
| Q4 | **C** | It is Tính chỉ số từ nhiều hồ sơ | Tính chỉ số từ nhiều hồ sơ |
| Q5 | **B** | It is for Đọc bản ghi và trả mặc định nếu thiếu | Đọc bản ghi và trả mặc định nếu thiếu |
| Q6 | **A** | It is for Thêm/sửa bản ghi khi đã kiểm tra khóa | Thêm/sửa bản ghi khi đã kiểm tra khóa |
| Q7 | **D** | It is for Xóa có xử lý mã chưa tồn tại | Xóa có xử lý mã chưa tồn tại |
| Q8 | **C** | It is for Tính thống kê và sắp xếp hồ sơ | Tính thống kê và sắp xếp hồ sơ |
| Q9 | **B** | Kiểm mã trùng trước khi thêm để không ghi đè | Kiểm mã trùng trước khi thêm để không ghi đè |
| Q10 | **A** | Dictionary truy xuất bằng khóa không cần biết thứ tự bản ghi | Dictionary truy xuất bằng khóa không cần biết thứ tự bản ghi |
| Q11 | **D** | Ràng buộc 0–10 trước khi thay giá trị | Ràng buộc 0–10 trước khi thay giá trị |
| Q12 | **C** | pop với giá trị mặc định tránh KeyError | pop với giá trị mặc định tránh KeyError |
| Q13 | **B** | mean tính trung bình và max xác định điểm cao | mean tính trung bình và max xác định điểm cao |
| Q14 | **A** | Một hồ sơ S1 mới, điểm 8/10 | Một hồ sơ S1 mới, điểm 8/10 |
| Q15 | **D** | Hai sinh viên mã S1 S2 | Hai sinh viên mã S1 S2 |
| Q16 | **C** | SV S1 có điểm 7 sửa thành 9 | SV S1 có điểm 7 sửa thành 9 |
| Q17 | **B** | Mã S2 chưa tồn tại | Mã S2 chưa tồn tại |
| Q18 | **A** | Điểm 7,8,9 trên thang 10 | Điểm 7,8,9 trên thang 10 |
| Q19 | **D** | Understand source, parameters and permissions | Hiểu nguồn, tham số và quyền hạn |
| Q20 | **C** | Observed output, failures and limits | Đầu ra thật, lỗi và giới hạn |

## 8. Nối sang bài tiếp

`Dictionary/Function → CRUD → CLI → File/CSV → Data App`.

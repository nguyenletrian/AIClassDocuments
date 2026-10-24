# Bản đồ chủ đề PythoClass — dự thảo phủ nguồn

**Repo nguồn:** https://github.com/nguyenletrian/PythoClass, tại commit `3de8ec82a74c79ee22f7538cb81980f0d59407a2`.  
**Quy mô đã xác nhận:** 65 file (35 notebook, 19 script Python, 5 DOCX, 3 CSV, 1 PNG, 1 XLSX, 1 PPTX). Xem `sources/pythoclass-file-inventory.csv` để biết từng file đã đọc đến mức nào.

**Lưu ý:** Bảng sau là **đề xuất chương trình theo những chủ đề đã nhìn thấy**, không phải chứng nhận đã phân tích đủ 65 file. Cần tiếp tục tách từng subtopic nhỏ thành `topic_id` duy nhất và đánh dấu nguồn trùng. Các chủ đề xuất hiện một lần cũng không được bỏ qua.

| Nhóm | Những khái niệm cần đưa vào giáo trình | Nguồn đã nhận diện |
|---|---|---|
| Python nền tảng | Cài đặt/chạy code, input/output, biến, int/float/bool/str, string index/slice/method, ép kiểu, toán tử số học/so sánh/logic/bitwise | `Demo/1_intro.ipynb`; `Demo/2_datatype.ipynb`; `Demo/3_operator.ipynb` |
| Điều kiện và vòng lặp | if/elif/else, nested if, for/while, range, break/continue, lặp lồng, bài tập patterns | `Demo/4_condition.ipynb`; `Demo/4_loop.ipynb` |
| Cấu trúc dữ liệu | list, tuple, set, dictionary; mutable/immutable, indexing, slicing, tìm kiếm, CRUD, union/intersection/difference, nested dict | `Demo/5_list.ipynb`; `Demo/5_tuple.ipynb`; `Demo/5_set.ipynb`; `Demo/5_dictionary.ipynb` |
| Hàm và OOP | def/return, keyword/default args, scope, global/local, lambda/filter/sorted, class/object, constructor, methods, attribute, getter/setter | `Demo/6_function.ipynb`; `Demo/7_oop.ipynb`; `OOP.py` |
| Làm việc với chương trình | lỗi và ngoại lệ, try/except, đọc/ghi file, CSV, menu/CLI, Git cơ bản, lab | `10. File IO.py`; `11.ErrorHandling.py`; `12.Git.py`; `Demo/6_menu.py` |
| NumPy | ndarray 1D/2D, shape/size/dtype/ndim, index/slice, boolean/fancy indexing, reshape/transpose, broadcasting, axis, aggregate, matrix multiplication, random, npy/txt IO | `Demo/8_numpy.ipynb`; `Lession Numpy.py` |
| Pandas | Series/DataFrame, CSV, head/tail/info/describe, missing/duplicate, loc/iloc, filtering, sorting, grouping, merging/join, doanh thu | `Demo/9_pandas.ipynb`; `Pandas.py` |
| Toán rời rạc | logic, bảng chân trị, tautology, Modus Ponens, quy tắc cộng/nhân, Cartesian product, bao hàm–loại trừ, tam giác Pascal, hoán vị/tổ hợp | `MON 2/s2_discretemath.ipynb` |
| Tập hợp, đồ thị & AI | adjacency list/matrix, directed/weighted/complete/cyclic/tree graph, phân hoạch tập, data partition, phân loại, clustering, Jaccard, NLP chuẩn bị dữ liệu | `MON 2/s2_discretemath.ipynb`; `MON 2/3.Exercies.py` |
| Đại số tuyến tính | scalar, vector, norm, unit vector, dot/orthogonality, ma trận, transpose/identity/inverse/determinant/rank, hệ tuyến tính, eigenvalue/eigenvector | `MON 2/Linear Algebra.py`; `MON 2/3. Eigens_PCA.py` |
| PCA | covariance, standardization, eigenvectors, explained variance, chọn `n_components`, PCA trực quan hóa và trong ML pipeline | `MON 2/3. Eigens_PCA.py`; `MON 2/LabSession3_4.py` |
| Hàm số cho AI | linear/quadratic/polynomial/exponential; sigmoid/tanh/ReLU/leaky ReLU/softmax; MSE, MAE, Huber, cross-entropy, hinge, KL divergence | `MON 2/2026-10-16.ipynb` |
| Giới hạn, đạo hàm, tối ưu | limits/continuity, đạo hàm riêng bậc 1/2, gradient, gradient descent/learning rate, Jacobian, Hessian, regression, loss minimization | `MON 2/2026-10-16-2.ipynb`; `MON 2/2026-10-19.ipynb` |
| Xác suất | sample space/event, empirical probability, độc lập/phụ thuộc, conditional probability, Bayes, total probability, phân phối nhị thức/chuẩn | `MON 2/2026-10-21.ipynb` |
| Thống kê | mean/median/mode, frequency, range, variance/std, quantiles/IQR/outliers, skewness/kurtosis, sampling, CLT, standard error, hypothesis tests, confidence intervals | `MON 2/2026-10-23.ipynb` |

## Danh sách công việc tiếp theo sau khi bài mẫu được duyệt
1. **Quét sâu 65 file nguồn:** cả comment ngắn, các cell notebook ít chữ, DOCX lab, PPTX định hướng và lịch học XLSX; phân loại phần nào là nội dung học, bài tập, lịch và tài liệu tham chiếu.
2. **Chuẩn hóa taxonomy:** tạo `concept_id` cho từng đơn vị kiến thức, ghi `file/cell`, mức độ nguồn (note/code/exercise), bài đích; đánh dấu nội dung trùng và chủ đề nhỏ.
3. **Lập thứ tự tiên quyết:** ví dụ NumPy/đại số trước PCA; đạo hàm trước Gradient Descent; Bayes sau xác suất có điều kiện.
4. **Soạn và test:** khoảng 5 bài tập cho mỗi khái niệm lớn/bài; khái niệm quá nhỏ có thể gom thành một bài đồng nhất nhưng vẫn đủ ví dụ minh họa.
5. **Nghiệm thu theo lô:** so sánh coverage với inventory; không gắn `APPROVED` cho mục chưa review.

## Quy tắc đặc biệt
- Không coi notebook đã chạy là nguồn đảm bảo code đúng; luôn chạy lại với dữ liệu và package phù hợp.
- Phân biệt phương sai của PCA với độ chính xác mô hình; phân biệt thống kê mô tả và suy diễn.
- Một khái niệm chỉ được nhắc đến một dòng (ví dụ `Huber Loss` hoặc `Modus Ponens`) vẫn phải có một đơn vị tri thức/tiểu mục rõ ràng, không biến mất vì “ít nội dung”.
- Hiện bài mẫu PCA mới dựa trực tiếp trên **ba file nguồn**. Những hàng khác cần hoàn tất rà soát trước khi khẳng định đã bao phủ.

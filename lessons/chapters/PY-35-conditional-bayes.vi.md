# PY-35 — Xác suất có điều kiện, Bayes và xác suất toàn phần


## 1. Vị trí trong chuỗi kiến thức

**Từ vựng trong mục:** **Conditional probability** — xác suất có điều kiện; **Independence** — độc lập.

`Biến cố → Điều kiện → Bayes → Đánh giá mô hình AI`

Bài này kết nối dữ liệu thực nghiệm với cách tính xác suất, thống kê và các bước học máy.

## 2. English vocabulary — Từ vựng

| English | Tiếng Việt | Khái niệm |
|---|---|---|
| Conditional probability | xác suất có điều kiện | Khả năng A xảy ra khi biết B đã xảy ra |
| Independence | độc lập | Hai biến cố không ảnh hưởng xác suất của nhau |
| Bayes theorem | định lý Bayes | Cập nhật xác suất giả thuyết khi có bằng chứng |
| Total probability | xác suất toàn phần | Cộng xác suất qua các nhóm loại trừ và đủ |

## 3. Công thức và cách gọi bằng Python

**Từ vựng:** **Event** — biến cố; **Prior** — xác suất trước bằng chứng; **Posterior** — xác suất sau bằng chứng.

| Công thức / cú pháp | Cách hiểu |
|---|---|
| `P(A given B) = P(A and B) / P(B)` | Xác suất có điều kiện khi `P(B)>0` |
| `P(A and B) = P(A given B) * P(B)` | Quy tắc nhân xác suất |
| `posterior = likelihood * prior / evidence` | Bayes với xác suất bằng chứng khác 0 |
| `sum(group_share * group_rate)` | Xác suất toàn phần qua các nhóm rời và phủ đủ |

## 4. Khái niệm chính và liên quan

**Mạch kiến thức:** Trước hết xác định nhóm điều kiện B để tính P(A khi B). Khi hai biến cố độc lập, biết B không đổi xác suất của A. Khi có bằng chứng mới, Bayes tính lại xác suất giả thuyết; xác suất toàn phần giúp tính tỷ lệ chung từ các nhóm có tỷ trọng khác nhau.

### 4.1. Conditional probability — Thu hẹp mẫu nền

**Từ vựng:** **Conditional probability** — xác suất có điều kiện; **Conditioning event** — biến cố điều kiện.

**Xác suất có điều kiện** `P(A given B)` chỉ xét những trường hợp **B đã xảy ra**, không còn xét toàn bộ quần thể ban đầu. Ví dụ trong 100 khách **đã xem quảng cáo** có 20 người mua. Khi đó P(mua **khi đã xem**) = 20/100 = 0.2, không phải tỷ lệ mua của tất cả khách. Công thức `P(A given B) = P(A∩B)/P(B)` chỉ dùng khi `P(B)>0`. Tỷ lệ này **không tự chứng minh** xem quảng cáo đã gây ra hành vi mua.

```python
seen = 100
bought = 20
print(bought / seen)
```

**Kết quả khi chạy:**

```text
0.2
```

Trong nhóm 100 người đã xem quảng cáo, tỷ lệ mua quan sát được bằng 20%.

### 4.2. Independence — Không làm đổi xác suất của nhau

**Từ vựng:** **Independence** — độc lập; **Joint probability** — xác suất đồng thời.

Hai biến cố A và B **độc lập** nếu biết B xảy ra không đổi khả năng của A: `P(A given B)=P(A)` (khi P(B)>0). Tương đương `P(A∩B)=P(A)×P(B)`. Giả sử P(A)=0.5 và P(B)=0.4 thì nếu độc lập, P(cả A và B)=0.2. Trong dữ liệu thực, việc hai tỷ lệ gần nhau chưa tự chứng minh độc lập; cần biết cách lấy mẫu và đo sai số.

```python
p_a = 0.5
p_b = 0.4
print(round(p_a * p_b, 3))
```

**Kết quả khi chạy:**

```text
0.2
```

Nếu hai biến cố độc lập thì giao của chúng có xác suất 0.2.

### 4.3. Bayes theorem — Cập nhật từ bằng chứng

**Từ vựng:** **Prior** — tỷ lệ nền trước bằng chứng; **Likelihood** — khả năng bằng chứng khi giả thuyết đúng; **Posterior** — xác suất sau bằng chứng.

Định lý **Bayes** trả lời “khi đã thấy **tín hiệu dương**, xác suất thực sự có lỗi là bao nhiêu?” Ví dụ chỉ 1% sản phẩm lỗi; máy báo dương với 99% hàng lỗi (**độ nhạy**) và 5% hàng không lỗi (**dương giả**). Trên 10.000 sản phẩm giả định có 100 lỗi: khoảng 99 dương thật, nhưng 495 dương giả từ 9.900 hàng tốt. Tổng dương là 594, nên xác suất lỗi khi máy báo dương là `99/594 ≈ 0.167`, **không phải 99%**. Tỷ lệ nền quyết định nhiều đến kết luận.

```python
prior = 0.01
sensitivity = 0.99
false_positive = 0.05
positive = sensitivity * prior + false_positive * (1 - prior)
print(round(sensitivity * prior / positive, 3))
```

**Kết quả khi chạy:**

```text
0.167
```

Sau tín hiệu dương, xác suất lỗi khoảng 16,7% theo các giả định đã nêu.

### 4.4. Total probability — Cộng qua các nhóm đầy đủ

**Từ vựng:** **Total probability** — xác suất toàn phần; **Partition** — phân hoạch.

Nếu quần thể được chia thành các **nhóm rời nhau và phủ đủ**, xác suất chung là trung bình có trọng số của xác suất trong nhóm. Ví dụ 60% khách ở nhóm X, trong đó 80% ủng hộ, còn 40% ở nhóm Y với tỷ lệ ủng hộ 20%. Tỷ lệ chung là `0.6×0.8 + 0.4×0.2 = 0.56`. Không cộng trực tiếp 80% và 20%, vì hai nhóm có quy mô khác nhau. Tổng xác suất các nhóm phải bằng 1.

```python
shares = [0.6, 0.4]
support = [0.8, 0.2]
print(round(sum(a * b for a, b in zip(shares, support)), 3))
```

**Kết quả khi chạy:**

```text
0.56
```

Xác suất chung là 56%, được tính theo tỷ trọng mỗi nhóm.

## 5. Năm tình huống ứng dụng

### Tình huống 1 — Diễn giải cảnh báo của hệ kiểm hàng

**Tình huống thực tế:** Dây chuyền có tỷ lệ lỗi nền 1%, máy kiểm phát hiện 99% hàng lỗi và báo nhầm 5% hàng không lỗi. Khi một sản phẩm bị báo dương, đội kiểm tra muốn biết xác suất **thực sự lỗi**.

**Vì sao chọn cách giải này?** Bayes dùng cả tỷ lệ nền và đặc tính máy; độ nhạy 99% không phải tỷ lệ hàng thật lỗi trong tất cả cảnh báo.

**Quy trình giải:**

1. Gán tỷ lệ lỗi 0.01, độ nhạy 0.99 và dương giả 0.05.
2. Tính xác suất tất cả cảnh báo bằng tổng hai nhóm lỗi/không lỗi.
3. Lấy phần dương thật chia tổng dương, làm tròn ba chữ số.

```python
prior = 0.01
sensitivity = 0.99
false_positive = 0.05
p_alert = sensitivity * prior + false_positive * (1 - prior)
print(round(sensitivity * prior / p_alert, 3))
```

**Kết quả khi chạy:**

```text
0.167
```

Khoảng 16.7% cảnh báo dương là lỗi thật theo giả định; cần kiểm tra bổ sung trước quyết định xử lý.

### Tình huống 2 — Tỷ lệ mua hàng trong nhóm đã xem quảng cáo

**Tình huống thực tế:** Một chiến dịch có 100 khách **đã xem** quảng cáo và trong nhóm đó 20 khách mua. Cần báo tỷ lệ mua có điều kiện trên lượt xem, không phải của mọi người dùng.

**Vì sao chọn cách giải này?** Điều kiện 'đã xem' giới hạn mẫu nền còn 100 khách, nên mẫu số phải là số đã xem.

**Quy trình giải:**

1. Lưu số khách đã xem và số khách vừa xem vừa mua.
2. Chia số mua trong nhóm cho số đã xem.
3. In tỷ lệ và nói rõ đây không phải ước lượng nhân quả.

```python
seen = 100
bought_after_seen = 20
print(bought_after_seen / seen)
```

**Kết quả khi chạy:**

```text
0.2
```

Có 20% người thuộc nhóm đã xem quảng cáo thực hiện mua trong quan sát này.

### Tình huống 3 — Tính tỷ lệ ủng hộ chung theo nhóm

**Tình huống thực tế:** Khảo sát giả định có 60% đối tượng thuộc nhóm X với tỷ lệ ủng hộ 80%; 40% thuộc nhóm Y với tỷ lệ ủng hộ 20%. Hai nhóm rời nhau, bao phủ mọi đối tượng. Cần tính tỷ lệ chung.

**Vì sao chọn cách giải này?** Cộng xác suất toàn phần theo tỷ trọng nhóm; không thể lấy trung bình đơn giản hai tỷ lệ 80% và 20%.

**Quy trình giải:**

1. Ghi tỷ trọng hai nhóm và tỷ lệ ủng hộ trong từng nhóm.
2. Nhân tỷ trọng với tỷ lệ ủng hộ tương ứng.
3. Cộng rồi in xác suất chung.

```python
shares = [0.6, 0.4]
rates = [0.8, 0.2]
print(round(sum(a * b for a, b in zip(shares, rates)), 3))
```

**Kết quả khi chạy:**

```text
0.56
```

Tỷ lệ chung là 56% dưới giả định hai nhóm bao phủ toàn bộ quần thể.

### Tình huống 4 — Kiểm tra giả định độc lập giữa hai sự kiện

**Tình huống thực tế:** Hai sự kiện A, B có xác suất P(A)=0.5, P(B)=0.4 và P(A∩B)=0.2 theo một mô hình xác suất cho sẵn. Cần kiểm tra bộ giá trị này có đáp ứng điều kiện độc lập không.

**Vì sao chọn cách giải này?** So xác suất đồng thời với tích xác suất riêng là tiêu chuẩn độc lập cho mô hình đã cho.

**Quy trình giải:**

1. Lưu ba xác suất đã biết.
2. Tính tích P(A)×P(B).
3. Dùng sai số nhỏ so với P(A∩B) và in Boolean.

```python
p_a = 0.5
p_b = 0.4
p_joint = 0.2
print(abs(p_joint - p_a * p_b) < 1e-12)
```

**Kết quả khi chạy:**

```text
True
```

Các xác suất đã cho thỏa quan hệ độc lập về mặt toán học; dữ liệu khảo sát thực cần xem độ bất định.

### Tình huống 5 — Đánh giá một máy kiểm chất lượng khác

**Tình huống thực tế:** Lô hàng có tỷ lệ lỗi nền 2%, máy phát hiện 95% sản phẩm lỗi nhưng báo nhầm 10% sản phẩm tốt. Cần biết xác suất hàng lỗi sau một cảnh báo dương.

**Vì sao chọn cách giải này?** Bayes tách dương thật và dương giả trước khi xét trong toàn bộ các cảnh báo.

**Quy trình giải:**

1. Dùng prior=0.02, sensitivity=0.95, false_positive=0.10.
2. Tính tổng xác suất báo dương từ hai nhóm.
3. Chia phần dương thật cho tổng, in ba chữ số.

```python
prior = 0.02
sensitivity = 0.95
false_positive = 0.10
p_alert = sensitivity * prior + false_positive * (1 - prior)
print(round(sensitivity * prior / p_alert, 3))
```

**Kết quả khi chạy:**

```text
0.162
```

Chỉ khoảng 16.2% hàng bị báo dương là lỗi thật theo mô hình; không nhầm với độ nhạy 95%.

## 6. Sai lầm thường gặp

- P(A khi B) và P(B khi A) có **hai mẫu nền khác nhau**, không được tráo hai xác suất.
- Độ nhạy của máy kiểm không phải xác suất sản phẩm thực sự lỗi sau cảnh báo; phải tính cả tỷ lệ nền và dương giả.
- Xác suất có điều kiện cần mẫu số P(B) lớn hơn 0.
- Các nhóm trong xác suất toàn phần phải rời nhau và phủ toàn bộ quần thể.
- Quan sát khách mua sau khi thấy quảng cáo không tự chứng minh quảng cáo gây ra mua hàng.
- Kiểm tra độc lập trên dữ liệu khảo sát cần xét sai số và cách lấy mẫu, không chỉ so hai số xấp xỉ.

## 7. English–Vietnamese multiple-choice questions — Trắc nghiệm song ngữ

**Q1. What is conditional probability? — Xác suất có điều kiện là gì?**

A. Probability of A given B has occurred — Xác suất A khi biết B đã xảy ra

B. One event does not change the probability of the other — Biến cố này không đổi xác suất của biến cố kia

C. A posterior from evidence, likelihood and prior — Xác suất sau bằng chứng từ likelihood và prior

D. Overall chance weighted over a partition — Xác suất chung theo trọng số một phân hoạch

**Q2. What is independence of events? — Độc lập giữa hai biến cố là gì?**

A. Probability of A given B has occurred — Xác suất A khi biết B đã xảy ra

B. One event does not change the probability of the other — Biến cố này không đổi xác suất của biến cố kia

C. A posterior from evidence, likelihood and prior — Xác suất sau bằng chứng từ likelihood và prior

D. Overall chance weighted over a partition — Xác suất chung theo trọng số một phân hoạch

**Q3. What does Bayes' theorem compute? — Định lý Bayes tính gì?**

A. Probability of A given B has occurred — Xác suất A khi biết B đã xảy ra

B. One event does not change the probability of the other — Biến cố này không đổi xác suất của biến cố kia

C. A posterior from evidence, likelihood and prior — Xác suất sau bằng chứng từ likelihood và prior

D. Overall chance weighted over a partition — Xác suất chung theo trọng số một phân hoạch

**Q4. What does total probability calculate? — Xác suất toàn phần tính gì?**

A. Probability of A given B has occurred — Xác suất A khi biết B đã xảy ra

B. One event does not change the probability of the other — Biến cố này không đổi xác suất của biến cố kia

C. A posterior from evidence, likelihood and prior — Xác suất sau bằng chứng từ likelihood và prior

D. Overall chance weighted over a partition — Xác suất chung theo trọng số một phân hoạch

**Q5. Which formula gives P(A given B)? — Công thức P(A khi biết B) là gì?**

A. `P(A and B)/P(B)` when P(B)>0 — `P(A và B)/P(B)` khi P(B)>0

B. `P(A and B)=P(A)*P(B)` — `P(A và B)=P(A)*P(B)`

C. `likelihood*prior/evidence` — `likelihood*prior/evidence`

D. Disjoint and exhaustive — Rời nhau và phủ đủ

**Q6. Which equation expresses event independence? — Đẳng thức nào mô tả biến cố độc lập?**

A. `P(A and B)/P(B)` when P(B)>0 — `P(A và B)/P(B)` khi P(B)>0

B. `P(A and B)=P(A)*P(B)` — `P(A và B)=P(A)*P(B)`

C. `likelihood*prior/evidence` — `likelihood*prior/evidence`

D. Disjoint and exhaustive — Rời nhau và phủ đủ

**Q7. Which rule gives posterior after a positive signal? — Quy tắc nào tính posterior khi tín hiệu dương?**

A. `P(A and B)/P(B)` when P(B)>0 — `P(A và B)/P(B)` khi P(B)>0

B. `P(A and B)=P(A)*P(B)` — `P(A và B)=P(A)*P(B)`

C. `likelihood*prior/evidence` — `likelihood*prior/evidence`

D. Disjoint and exhaustive — Rời nhau và phủ đủ

**Q8. What condition is required for total probability groups? — Các nhóm dùng xác suất toàn phần phải thế nào?**

A. `P(A and B)/P(B)` when P(B)>0 — `P(A và B)/P(B)` khi P(B)>0

B. `P(A and B)=P(A)*P(B)` — `P(A và B)=P(A)*P(B)`

C. `likelihood*prior/evidence` — `likelihood*prior/evidence`

D. Disjoint and exhaustive — Rời nhau và phủ đủ

**Q9. What does prior mean? — Prior có nghĩa gì?**

A. Probability before current evidence — Xác suất trước khi có bằng chứng hiện tại

B. Probability of evidence under a hypothesis — Xác suất bằng chứng khi giả thuyết đúng

C. Updated hypothesis probability after evidence — Xác suất giả thuyết được cập nhật sau bằng chứng

D. Probability of positive signal when no defect exists — Xác suất báo dương khi thực tế không có lỗi

**Q10. What does likelihood mean? — Likelihood biểu thị gì?**

A. Probability before current evidence — Xác suất trước khi có bằng chứng hiện tại

B. Probability of evidence under a hypothesis — Xác suất bằng chứng khi giả thuyết đúng

C. Updated hypothesis probability after evidence — Xác suất giả thuyết được cập nhật sau bằng chứng

D. Probability of positive signal when no defect exists — Xác suất báo dương khi thực tế không có lỗi

**Q11. What does posterior mean? — Posterior là gì?**

A. Probability before current evidence — Xác suất trước khi có bằng chứng hiện tại

B. Probability of evidence under a hypothesis — Xác suất bằng chứng khi giả thuyết đúng

C. Updated hypothesis probability after evidence — Xác suất giả thuyết được cập nhật sau bằng chứng

D. Probability of positive signal when no defect exists — Xác suất báo dương khi thực tế không có lỗi

**Q12. What is a false-positive rate? — Tỷ lệ dương giả là gì?**

A. Probability before current evidence — Xác suất trước khi có bằng chứng hiện tại

B. Probability of evidence under a hypothesis — Xác suất bằng chứng khi giả thuyết đúng

C. Updated hypothesis probability after evidence — Xác suất giả thuyết được cập nhật sau bằng chứng

D. Probability of positive signal when no defect exists — Xác suất báo dương khi thực tế không có lỗi

**Q13. What is P(A given B) if 20 of 100 B cases have A? — P(A khi B) là gì nếu 20 trên 100 ca B có A?**

A. 0.2 — 0.2

B. 0.56 — 0.56

C. 0.3 — 0.3

D. No; base rate and false positives also matter — Không; còn tỷ lệ nền và dương giả

**Q14. What is the total with group shares 0.6,0.4 and rates 0.8,0.2? — Tỷ lệ chung từ nhóm 0.6/0.4 với xác suất 0.8/0.2 là gì?**

A. 0.2 — 0.2

B. 0.56 — 0.56

C. 0.3 — 0.3

D. No; base rate and false positives also matter — Không; còn tỷ lệ nền và dương giả

**Q15. If P(A)=0.5 and P(B)=0.6 and they are independent, what is P(A and B)? — Nếu A, B độc lập có xác suất 0.5 và 0.6 thì P(A và B) là gì?**

A. 0.2 — 0.2

B. 0.56 — 0.56

C. 0.3 — 0.3

D. No; base rate and false positives also matter — Không; còn tỷ lệ nền và dương giả

**Q16. If an alert has 99% sensitivity, does that mean 99% of alerts are true defects? — Độ nhạy 99% có nghĩa 99% cảnh báo là lỗi thật không?**

A. 0.2 — 0.2

B. 0.56 — 0.56

C. 0.3 — 0.3

D. No; base rate and false positives also matter — Không; còn tỷ lệ nền và dương giả

**Q17. Why does Bayes need the base rate? — Vì sao Bayes cần tỷ lệ nền?**

A. Rare cases can yield many false alarms among positives — Sự kiện hiếm có thể làm dương giả chiếm nhiều trong cảnh báo

B. The formula divides by P(B) — Vì công thức chia cho P(B)

C. That viewing ads caused purchases — Việc xem quảng cáo gây ra hành vi mua

D. They condition on different reference groups — Chúng xét trên hai nhóm điều kiện khác nhau

**Q18. Why must P(B)>0 for P(A given B)? — Vì sao cần P(B)>0 khi tính P(A khi B)?**

A. Rare cases can yield many false alarms among positives — Sự kiện hiếm có thể làm dương giả chiếm nhiều trong cảnh báo

B. The formula divides by P(B) — Vì công thức chia cho P(B)

C. That viewing ads caused purchases — Việc xem quảng cáo gây ra hành vi mua

D. They condition on different reference groups — Chúng xét trên hai nhóm điều kiện khác nhau

**Q19. What does an observational conditional purchase rate not prove? — Tỷ lệ mua có điều kiện trong quan sát không chứng minh gì?**

A. Rare cases can yield many false alarms among positives — Sự kiện hiếm có thể làm dương giả chiếm nhiều trong cảnh báo

B. The formula divides by P(B) — Vì công thức chia cho P(B)

C. That viewing ads caused purchases — Việc xem quảng cáo gây ra hành vi mua

D. They condition on different reference groups — Chúng xét trên hai nhóm điều kiện khác nhau

**Q20. What distinguishes P(A given B) from P(B given A)? — P(A khi B) khác P(B khi A) ở đâu?**

A. Rare cases can yield many false alarms among positives — Sự kiện hiếm có thể làm dương giả chiếm nhiều trong cảnh báo

B. The formula divides by P(B) — Vì công thức chia cho P(B)

C. That viewing ads caused purchases — Việc xem quảng cáo gây ra hành vi mua

D. They condition on different reference groups — Chúng xét trên hai nhóm điều kiện khác nhau

### Answer key — Đáp án song ngữ

| Câu | Đáp án | Explanation (English) | Giải thích (Tiếng Việt) |
|---|---|---|---|
| Q1 | **A** | It restricts the reference population to B. | Nó thu hẹp mẫu nền về nhóm B. |
| Q2 | **B** | Independence prevents one event from changing the other event's chance. | Độc lập nghĩa là biến cố này không đổi xác suất biến cố kia. |
| Q3 | **C** | Bayes updates a prior using observed evidence. | Bayes cập nhật tỷ lệ nền từ bằng chứng. |
| Q4 | **D** | Total probability weights rates by group sizes. | Xác suất toàn phần dùng tỷ trọng của từng nhóm. |
| Q5 | **A** | Joint probability divided by the conditioning probability. | Lấy xác suất giao chia xác suất biến cố điều kiện. |
| Q6 | **B** | The joint probability equals the product for independence. | Độc lập khi xác suất giao bằng tích hai xác suất. |
| Q7 | **C** | Bayes normalizes likelihood times prior by the evidence rate. | Bayes chuẩn hóa likelihood nhân prior bằng xác suất bằng chứng. |
| Q8 | **D** | Groups cannot overlap and must cover the sample space. | Nhóm phải không giao nhau và phủ toàn bộ. |
| Q9 | **A** | Prior is the baseline probability. | Prior là xác suất nền. |
| Q10 | **B** | Likelihood conditions evidence on the hypothesis. | Likelihood xét bằng chứng khi giả thuyết đúng. |
| Q11 | **C** | Posterior accounts for the observed evidence. | Posterior đã tính đến bằng chứng quan sát. |
| Q12 | **D** | False positive refers to a positive test in a negative case. | Dương giả là cảnh báo dương ở trường hợp không lỗi. |
| Q13 | **A** | Twenty divided by one hundred equals 0.2. | 20 chia 100 bằng 0.2. |
| Q14 | **B** | 0.6×0.8+0.4×0.2 equals 0.56. | 0.6×0.8+0.4×0.2 bằng 0.56. |
| Q15 | **C** | For independent events, 0.5×0.6=0.3. | Với biến cố độc lập, 0.5×0.6=0.3. |
| Q16 | **D** | Sensitivity and posterior condition on different populations. | Độ nhạy và posterior xét hai nhóm mẫu nền khác nhau. |
| Q17 | **A** | Rare events can make most alerts false even with strong sensitivity. | Sự kiện hiếm có thể khiến phần lớn cảnh báo là dương giả. |
| Q18 | **B** | Division by zero would be undefined. | Chia cho 0 không xác định. |
| Q19 | **C** | Observed association does not establish causation. | Liên hệ quan sát không tự chứng minh nhân quả. |
| Q20 | **D** | Reversing the condition changes the denominator. | Đảo điều kiện làm thay đổi mẫu số. |

## 8. Liên hệ bài tiếp theo

`Biến cố → Điều kiện → Bayes → Đánh giá mô hình AI`.

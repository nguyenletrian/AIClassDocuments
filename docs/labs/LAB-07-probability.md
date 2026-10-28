# LAB-07-probability — Đề Anh đầy đủ, đề Việt đầy đủ, hướng giải, toàn bộ code có note

**Nguồn:** Word đã chuyển sang `labs/pythoclass/LAB-07-probability/LAB.md`; code trong `labs/pythoclass/LAB-07-probability/SOLUTION.py` có đối chiếu `DEMO.py` và giáo trình. Dữ liệu, lời giải và thuật toán được kế thừa nguyên tắc từ code đã có; không nhận nhầm lời giải tham khảo là demo cá nhân. Một lab chỉ xuất **một file**.

---

## PART 1 — COMPLETE ORIGINAL ENGLISH ASSIGNMENT

# LAB SESSION 7

## Problem Description
Probability, Simulation, Conditional Probability, Bayes’ Theorem and Probability Distributions.

## Requirements

### Task 1 – Sample Space and Basic Probability
A box contains 10 cards numbered from 1 to 10. One card is randomly selected.

Define the sample space and events:
- A: The selected number is even.
- B: The selected number is greater than 6.

Calculate theoretical probabilities `P(A)`, `P(B)`, `P(A ∩ B)`, and `P(A ∪ B)`.

### Task 2 – Probability Simulation
A basketball player has a 70% probability of successfully making a free throw.

- Use NumPy to simulate **5,000 free throws** and calculate experimental probability of success.
- Simulate two independent players with success probabilities 0.7 and 0.6.
- Calculate probability both succeed and probability at least one succeeds.
- Compare simulation with theoretical probabilities.

### Task 3 – Conditional Probability
A day is randomly selected from a seven-day week.
- Event A: The selected day is a weekday (Monday to Friday).
- Event B: The selected day is Monday, Tuesday, Wednesday or Thursday.

Calculate theoretical conditional probability `P(A | B)`. Simulate 5,000 selections using Python and NumPy, then compare the experimental result.

### Task 4 – Bayes’ Theorem
An email filtering system has these characteristics:
- 30% of emails are spam.
- 90% of spam emails are correctly identified as spam.
- 5% of non-spam emails are incorrectly classified as spam.

Calculate overall probability an email is classified as spam, then use Bayes' theorem to calculate probability an email is actually spam when classified as spam.

### Task 5 – Probability Distributions
A customer service team receives 8 independent requests. Each has a 75% probability of successful resolution.

- Use `scipy.stats.binom.pmf()` to calculate probability of **exactly 6** resolved requests and **at least 6** requests.
- Plot the Binomial probability distribution using Matplotlib.

---

## PHẦN 2 — BẢN DỊCH TIẾNG VIỆT TOÀN BỘ ĐỀ

# Bản dịch toàn bộ LAB LAB-07-probability

Một chuỗi bài thực hành về **xác suất cơ bản, mô phỏng, xác suất có điều kiện, định lý Bayes và phân phối xác suất**. Giữ nguyên đúng 10 thẻ, 5.000 phép thử, các tỷ lệ 0,7/0,6/0,3/0,9/0,05, 8 yêu cầu và mức 75% từ Word.

## Toàn bộ yêu cầu

### Bài 1

Một hộp có 10 thẻ đánh số từ 1 đến 10, lấy ngẫu nhiên một thẻ. Xác định không gian mẫu, biến cố A (số chẵn), B (số lớn hơn 6). Tính xác suất của A, B, đồng thời A và B, và ít nhất A hoặc B.

### Bài 2

Một người chơi bóng rổ ném phạt thành công với xác suất 70%. Dùng NumPy mô phỏng **5.000** lần để tính tỉ lệ thực nghiệm. Tiếp theo mô phỏng hai người độc lập với xác suất thành công 0,7 và 0,6; tính cả hai thành công và ít nhất một người thành công; so sánh với lý thuyết.

### Bài 3

Chọn ngẫu nhiên một ngày trong tuần gồm 7 ngày. A là ngày thường từ thứ Hai đến thứ Sáu, B là thứ Hai đến thứ Năm. Tính `P(A|B)`, mô phỏng 5.000 lần bằng Python/NumPy và so sánh với kết quả lý thuyết.

### Bài 4

Hệ thống lọc email có 30% email spam, phát hiện đúng 90% spam, và báo nhầm 5% email không spam thành spam. Tính xác suất một email được đánh dấu spam và xác suất email thực sự spam khi đã bị đánh dấu.

### Bài 5

Nhóm hỗ trợ nhận 8 yêu cầu độc lập, mỗi yêu cầu có khả năng giải quyết thành công 75%. Dùng `scipy.stats.binom.pmf()` tính xác suất giải quyết **đúng 6** và **ít nhất 6**, vẽ phân phối nhị thức bằng Matplotlib.

---

## Quy trình giải chi tiết và các công thức liên quan

**Phương pháp chung:** Đọc điều kiện và số liệu đúng từ Word → biểu diễn bằng cấu trúc/mảng NumPy/Pandas → chạy hàm tính toán hay mô phỏng đã học → kiểm tra kết quả lý thuyết và trường hợp đặc biệt → trình bày bằng số và biểu đồ. Đây là lời giải đã có trong repo, không thay đổi thuật toán khi viết giáo trình.

### Bài 1 — Quy trình và công thức

Tạo `set(range(1,11))`, lọc từng biến cố bằng set comprehension. Dùng `&` cho giao và `|` cho hợp, rồi chia số phần tử cho kích thước không gian mẫu 10.

**Công thức / kết quả đối chiếu:** P(A)=5/10=0,5; P(B)=4/10=0,4; P(A∩B)=2/10=0,2; P(A∪B)=0,5+0,4−0,2=0,7.

**Công thức/đối chiếu:** P(A)=5/10=0,5; P(B)=4/10=0,4; P(A∩B)=2/10=0,2; P(A∪B)=0,7.

### Bài 2 — Quy trình và công thức

`np.random.default_rng(SEED)` tạo bộ sinh số có thể lặp; mỗi lần so ngẫu nhiên với ngưỡng 0,7/0,6 được một kết quả True/False. `mean()` cho tần suất thành công; dùng `&` và `|` trên hai mảng bool.

**Công thức / kết quả đối chiếu:** Độc lập: P(cả hai)=0,7×0,6=0,42; P(ít nhất một)=1−(1−0,7)(1−0,6)=0,88. Mô phỏng 5.000 lượt chỉ **xấp xỉ**, không bắt buộc trùng lý thuyết.

**Công thức/đối chiếu:** P(cả hai)=0,7×0,6=0,42; P(ít nhất một)=1−(1−0,7)(1−0,6)=0,88. Mô phỏng 5.000 lượt xấp xỉ giá trị này.

### Bài 3 — Quy trình và công thức

Đặt thứ Hai đến Chủ nhật ứng với mã 0–6; B={0,1,2,3} là tập con của A={0..4}. Trong mô phỏng, đếm số lượt chọn vào B rồi kiểm tra đồng thời A∩B để được xác suất có điều kiện.

**Công thức / kết quả đối chiếu:** P(A|B)=P(A∩B)/P(B)=4/4=1 (vì mọi ngày trong B đều là ngày thường).

**Công thức/đối chiếu:** B={thứ Hai..Năm} nằm trong A={thứ Hai..Sáu}; P(A|B)=1.

### Bài 4 — Quy trình và công thức

Tính tổng hai cách bị hệ thống gắn cờ spam: spam thật bị phát hiện và email sạch bị báo nhầm. Sau đó dùng Bayes đổi chiều điều kiện từ P(flag|spam) sang P(spam|flag).

**Công thức / kết quả đối chiếu:** P(flag)=0,3×0,9+0,7×0,05=0,305. P(spam|flag)=0,27/0,305≈0,8852459, **không** phải 90%.

**Công thức/đối chiếu:** P(flag)=0,3×0,9+0,7×0,05=0,305; P(spam|flag)=0,27/0,305≈0,88525.

### Bài 5 — Quy trình và công thức

Số thành công tuân theo nhị thức vì có 8 phép thử độc lập cùng xác suất p=0,75. Hàm pmf trả xác suất đúng k; cộng pmf cho k=6,7,8 để lấy ít nhất 6. Hàm `save_plot` trong code tham khảo dùng `plt.bar`.

**Công thức / kết quả đối chiếu:** P(X=k)=C(8,k)(0,75)^k(0,25)^(8−k); P(X≥6)=P(X=6)+P(X=7)+P(X=8).

**Công thức/đối chiếu:** X~Binom(n=8,p=0,75); P(X=k)=C(8,k)×p^k×(1−p)^(8−k); P(X≥6)=Σ P(X=k), k=6..8.

---

## PHẦN 4 — TOÀN BỘ CODE PYTHON CÙNG CHÚ THÍCH

Sao chép toàn bộ khối sau vào `lab_solution.py`; cài thư viện như yêu cầu bài (`numpy`, `scipy`, `matplotlib`). Chạy `python lab_solution.py --no-plot` để xem kết quả trên terminal; chạy không có `--no-plot` để tạo hình bằng code đã có. Chú thích được thêm vào các hàm, quy trình và câu lệnh quan trọng, **không đổi logic**.

```python
"""LAB SESSION 7 — Sample space, simulation, conditional probability, Bayes and binomial.

Run with --no-plot for console-only evaluation.
Dependencies: numpy, scipy, matplotlib (plotting only).
"""
from pathlib import Path
import sys
import numpy as np
from scipy.stats import binom

SEED=2026
TRIALS=5000

# Tập hợp tạo không gian mẫu và biến cố; dùng & cho giao, | cho hợp.
def task01_cards():
    space=set(range(1,11))
    a={x for x in space if x%2==0}
    b={x for x in space if x>6}
    return {
        "space":sorted(space),"A":sorted(a),"B":sorted(b),
        "P(A)":len(a)/len(space),
        "P(B)":len(b)/len(space),
        "P(A and B)":len(a&b)/len(space),
        "P(A or B)":len(a|b)/len(space),
    }

# Mô phỏng đúng 5000 lượt với cùng seed để so sánh lý thuyết.
def task02_free_throws():
    # Cố định seed để chạy lại được cùng chuỗi ngẫu nhiên.
    rng=np.random.default_rng(SEED)
    single=rng.random(TRIALS)<0.7
    first=rng.random(TRIALS)<0.7
    second=rng.random(TRIALS)<0.6
    both=first & second
    either=first | second
    return {
        "experimental_single":single.mean(),
        "experimental_both":both.mean(),
        "experimental_either":either.mean(),
        "theoretical_single":0.7,
        "theoretical_both":0.7*0.6,
        "theoretical_either":1-(1-0.7)*(1-0.6),
    }

# Tính P(A|B) dựa trên các ngày thuộc B.
def task03_conditional_days():
    # Mon=0, ..., Sun=6; A weekdays Mon–Fri, B Mon–Thu.
    A=set(range(5))
    B=set(range(4))
    theoretical=len(A&B)/len(B)
    # Cố định seed để chạy lại được cùng chuỗi ngẫu nhiên.
    rng=np.random.default_rng(SEED+1)
    drawn=rng.integers(0,7,size=TRIALS)
    given_b=np.isin(drawn,list(B))
    joint=np.isin(drawn,list(A&B))
    experimental=float(joint.sum()/given_b.sum())
    return theoretical,experimental

# Cộng xác suất gắn cờ từ spam thật và từ email bị báo nhầm.
def task04_bayes():
    p_spam=0.30
    p_flag_given_spam=0.90
    p_flag_given_clean=0.05
    p_flag=p_spam*p_flag_given_spam+(1-p_spam)*p_flag_given_clean
    # Công thức Bayes đổi chiều P(flag|spam) thành P(spam|flag).
    posterior=p_spam*p_flag_given_spam/p_flag
    return p_flag,posterior

# Dùng scipy.stats.binom cho đúng sáu và ít nhất sáu.
def task05_binomial():
    k=np.arange(0,9)
    probs=binom.pmf(k,n=8,p=0.75)
    return k,probs,float(binom.pmf(6,n=8,p=0.75)),float(probs[6:].sum())

# Biểu đồ cột phân phối số yêu cầu được giải quyết.
def save_plot(k,probs):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    folder=Path(__file__).resolve().parent/"outputs"
    folder.mkdir(exist_ok=True)
    fig,ax=plt.subplots()
    ax.bar(k,probs)
    ax.set(xlabel="Number of resolved requests (k)",ylabel="P(X=k)",title="Binomial(n=8, p=0.75)")
    ax.set_xticks(k)
    ax.grid(True,axis="y")
    target=folder/"binomial_distribution.png"
    fig.savefig(target,dpi=140,bbox_inches="tight")
    plt.close(fig)
    print("Saved:",target)

# Gọi cả năm bài, so sánh kết quả và tùy chọn vẽ đồ thị.
def main():
    cards=task01_cards()
    simulated=task02_free_throws()
    cond_theory,cond_exp=task03_conditional_days()
    p_flag,p_actual_spam=task04_bayes()
    k,prob,p_exact,p_at_least=task05_binomial()
    assert cards["P(A)"]==0.5
    assert cards["P(B)"]==0.4
    assert cards["P(A and B)"]==0.2
    assert cards["P(A or B)"]==0.7
    assert cond_theory==1.0
    assert abs(simulated["experimental_single"]-0.7)<0.04
    assert np.isclose(p_flag,0.305)
    assert np.isclose(prob.sum(),1)
    print("Task 1:",cards)
    print("Task 2:",simulated)
    print("Task 3 P(A|B), theoretical/experimental:",cond_theory,cond_exp)
    print("Task 4 P(flag), P(spam|flag):",round(p_flag,5),round(p_actual_spam,5))
    print("Task 5 P(X=6), P(X>=6):",round(p_exact,6),round(p_at_least,6))
    if "--no-plot" not in sys.argv:
        save_plot(k,prob)
if __name__=="__main__":
    main()
```

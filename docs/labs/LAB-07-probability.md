# Lab Session 7 — Xác suất, mô phỏng và Bayes

**Word gốc:** `LAB SESSION 7.docx`. Nội dung câu hỏi Anh trích đúng từ `labs/pythoclass/LAB-07-probability/LAB.md`; bản dịch và lời giải bám theo `DEMO.py`, `SOLUTION.py` đã tồn tại và các bài PY-21, PY-34..PY-36, PY-45. Những hàm phía dưới là **trích đoạn** của code tham khảo, không phải thuật toán mới hoặc lời khẳng định mọi hàm đều có trong demo gốc.

### English — Original topic

Probability, Simulation, Conditional Probability, Bayes’ Theorem and Probability Distributions.

### Tiếng Việt — Dịch chủ đề

Xác suất, mô phỏng, xác suất có điều kiện, định lý Bayes và các phân phối xác suất.

**Mã nền của `SOLUTION.py`:**

```python
import numpy as np  # Tạo mẫu số ngẫu nhiên và tính toán mảng.
from scipy.stats import binom  # Tính xác suất nhị thức.
SEED = 2026  # Tái lập kết quả mô phỏng của code tham khảo.
TRIALS = 5000  # Giữ đủ số lượt của đề Word.
```

## Bài 1 — Sample Space and Basic Probability

### English — Original Word requirement

A box contains 10 cards numbered from 1 to 10. One card is randomly selected.

Define the sample space and events:
- A: The selected number is even.
- B: The selected number is greater than 6.

Calculate theoretical probabilities `P(A)`, `P(B)`, `P(A ∩ B)`, and `P(A ∪ B)`.

### Tiếng Việt — Bản dịch

Một hộp có 10 thẻ đánh số từ 1 đến 10, lấy ngẫu nhiên một thẻ. Xác định không gian mẫu, biến cố A (số chẵn), B (số lớn hơn 6). Tính xác suất của A, B, đồng thời A và B, và ít nhất A hoặc B.

### Bài giải — Code demo/giáo trình đã có

**Nguồn:** hàm `task01_cards()` trong `labs/pythoclass/LAB-07-probability/SOLUTION.py`, đối chiếu `DEMO.py` và bài học. Các phần demo ban đầu có thể chỉ minh họa một số thao tác, nên dùng đúng lời giải tham khảo được lưu sẵn, không tự gán tác giả.

```python
# Phần chức năng task01_cards() lấy từ script đã có.
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
```

### Giải thích quy trình giải và công thức

Tạo `set(range(1,11))`, lọc từng biến cố bằng set comprehension. Dùng `&` cho giao và `|` cho hợp, rồi chia số phần tử cho kích thước không gian mẫu 10.

**Công thức / kết quả đối chiếu:** P(A)=5/10=0,5; P(B)=4/10=0,4; P(A∩B)=2/10=0,2; P(A∪B)=0,5+0,4−0,2=0,7.

## Bài 2 — Probability Simulation

### English — Original Word requirement

A basketball player has a 70% probability of successfully making a free throw.

- Use NumPy to simulate **5,000 free throws** and calculate experimental probability of success.
- Simulate two independent players with success probabilities 0.7 and 0.6.
- Calculate probability both succeed and probability at least one succeeds.
- Compare simulation with theoretical probabilities.

### Tiếng Việt — Bản dịch

Một người chơi bóng rổ ném phạt thành công với xác suất 70%. Dùng NumPy mô phỏng **5.000** lần để tính tỉ lệ thực nghiệm. Tiếp theo mô phỏng hai người độc lập với xác suất thành công 0,7 và 0,6; tính cả hai thành công và ít nhất một người thành công; so sánh với lý thuyết.

### Bài giải — Code demo/giáo trình đã có

**Nguồn:** hàm `task02_free_throws()` trong `labs/pythoclass/LAB-07-probability/SOLUTION.py`, đối chiếu `DEMO.py` và bài học. Các phần demo ban đầu có thể chỉ minh họa một số thao tác, nên dùng đúng lời giải tham khảo được lưu sẵn, không tự gán tác giả.

```python
# Phần chức năng task02_free_throws() lấy từ script đã có.
def task02_free_throws():
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
```

### Giải thích quy trình giải và công thức

`np.random.default_rng(SEED)` tạo bộ sinh số có thể lặp; mỗi lần so ngẫu nhiên với ngưỡng 0,7/0,6 được một kết quả True/False. `mean()` cho tần suất thành công; dùng `&` và `|` trên hai mảng bool.

**Công thức / kết quả đối chiếu:** Độc lập: P(cả hai)=0,7×0,6=0,42; P(ít nhất một)=1−(1−0,7)(1−0,6)=0,88. Mô phỏng 5.000 lượt chỉ **xấp xỉ**, không bắt buộc trùng lý thuyết.

## Bài 3 — Conditional Probability

### English — Original Word requirement

A day is randomly selected from a seven-day week.
- Event A: The selected day is a weekday (Monday to Friday).
- Event B: The selected day is Monday, Tuesday, Wednesday or Thursday.

Calculate theoretical conditional probability `P(A | B)`. Simulate 5,000 selections using Python and NumPy, then compare the experimental result.

### Tiếng Việt — Bản dịch

Chọn ngẫu nhiên một ngày trong tuần gồm 7 ngày. A là ngày thường từ thứ Hai đến thứ Sáu, B là thứ Hai đến thứ Năm. Tính `P(A|B)`, mô phỏng 5.000 lần bằng Python/NumPy và so sánh với kết quả lý thuyết.

### Bài giải — Code demo/giáo trình đã có

**Nguồn:** hàm `task03_conditional_days()` trong `labs/pythoclass/LAB-07-probability/SOLUTION.py`, đối chiếu `DEMO.py` và bài học. Các phần demo ban đầu có thể chỉ minh họa một số thao tác, nên dùng đúng lời giải tham khảo được lưu sẵn, không tự gán tác giả.

```python
# Phần chức năng task03_conditional_days() lấy từ script đã có.
def task03_conditional_days():
    # Mon=0, ..., Sun=6; A weekdays Mon–Fri, B Mon–Thu.
    A=set(range(5))
    B=set(range(4))
    theoretical=len(A&B)/len(B)
    rng=np.random.default_rng(SEED+1)
    drawn=rng.integers(0,7,size=TRIALS)
    given_b=np.isin(drawn,list(B))
    joint=np.isin(drawn,list(A&B))
    experimental=float(joint.sum()/given_b.sum())
    return theoretical,experimental
```

### Giải thích quy trình giải và công thức

Đặt thứ Hai đến Chủ nhật ứng với mã 0–6; B={0,1,2,3} là tập con của A={0..4}. Trong mô phỏng, đếm số lượt chọn vào B rồi kiểm tra đồng thời A∩B để được xác suất có điều kiện.

**Công thức / kết quả đối chiếu:** P(A|B)=P(A∩B)/P(B)=4/4=1 (vì mọi ngày trong B đều là ngày thường).

## Bài 4 — Bayes’ Theorem

### English — Original Word requirement

An email filtering system has these characteristics:
- 30% of emails are spam.
- 90% of spam emails are correctly identified as spam.
- 5% of non-spam emails are incorrectly classified as spam.

Calculate overall probability an email is classified as spam, then use Bayes' theorem to calculate probability an email is actually spam when classified as spam.

### Tiếng Việt — Bản dịch

Hệ thống lọc email có 30% email spam, phát hiện đúng 90% spam, và báo nhầm 5% email không spam thành spam. Tính xác suất một email được đánh dấu spam và xác suất email thực sự spam khi đã bị đánh dấu.

### Bài giải — Code demo/giáo trình đã có

**Nguồn:** hàm `task04_bayes()` trong `labs/pythoclass/LAB-07-probability/SOLUTION.py`, đối chiếu `DEMO.py` và bài học. Các phần demo ban đầu có thể chỉ minh họa một số thao tác, nên dùng đúng lời giải tham khảo được lưu sẵn, không tự gán tác giả.

```python
# Phần chức năng task04_bayes() lấy từ script đã có.
def task04_bayes():
    p_spam=0.30
    p_flag_given_spam=0.90
    p_flag_given_clean=0.05
    p_flag=p_spam*p_flag_given_spam+(1-p_spam)*p_flag_given_clean
    posterior=p_spam*p_flag_given_spam/p_flag
    return p_flag,posterior
```

### Giải thích quy trình giải và công thức

Tính tổng hai cách bị hệ thống gắn cờ spam: spam thật bị phát hiện và email sạch bị báo nhầm. Sau đó dùng Bayes đổi chiều điều kiện từ P(flag|spam) sang P(spam|flag).

**Công thức / kết quả đối chiếu:** P(flag)=0,3×0,9+0,7×0,05=0,305. P(spam|flag)=0,27/0,305≈0,8852459, **không** phải 90%.

## Bài 5 — Probability Distributions

### English — Original Word requirement

A customer service team receives 8 independent requests. Each has a 75% probability of successful resolution.

- Use `scipy.stats.binom.pmf()` to calculate probability of **exactly 6** resolved requests and **at least 6** requests.
- Plot the Binomial probability distribution using Matplotlib.

### Tiếng Việt — Bản dịch

Nhóm hỗ trợ nhận 8 yêu cầu độc lập, mỗi yêu cầu có khả năng giải quyết thành công 75%. Dùng `scipy.stats.binom.pmf()` tính xác suất giải quyết **đúng 6** và **ít nhất 6**, vẽ phân phối nhị thức bằng Matplotlib.

### Bài giải — Code demo/giáo trình đã có

**Nguồn:** hàm `task05_binomial()`, `save_plot()` trong `labs/pythoclass/LAB-07-probability/SOLUTION.py`, đối chiếu `DEMO.py` và bài học. Các phần demo ban đầu có thể chỉ minh họa một số thao tác, nên dùng đúng lời giải tham khảo được lưu sẵn, không tự gán tác giả.

```python
# Phần chức năng task05_binomial() lấy từ script đã có.
def task05_binomial():
    k=np.arange(0,9)
    probs=binom.pmf(k,n=8,p=0.75)
    return k,probs,float(binom.pmf(6,n=8,p=0.75)),float(probs[6:].sum())

# Phần chức năng save_plot() lấy từ script đã có.
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
```

### Giải thích quy trình giải và công thức

Số thành công tuân theo nhị thức vì có 8 phép thử độc lập cùng xác suất p=0,75. Hàm pmf trả xác suất đúng k; cộng pmf cho k=6,7,8 để lấy ít nhất 6. Hàm `save_plot` trong code tham khảo dùng `plt.bar`.

**Công thức / kết quả đối chiếu:** P(X=k)=C(8,k)(0,75)^k(0,25)^(8−k); P(X≥6)=P(X=6)+P(X=7)+P(X=8).

## Kiểm chứng từ code đã học

Chạy script tham khảo `labs/pythoclass/LAB-07-probability/SOLUTION.py --no-plot` để xem 5 kết quả và các `assert` có sẵn. Muốn xem phân phối xác suất thì chạy không có `--no-plot` để dùng `save_plot()` của code nguồn. Lưu ý seed là thông số tái lập mô phỏng, **không** thay đổi xác suất lý thuyết. Toàn bộ Lab này chỉ xuất thành `LAB-07-probability.md`.

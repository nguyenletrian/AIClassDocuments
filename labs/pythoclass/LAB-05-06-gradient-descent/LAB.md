# LAB SESSION 5 & 6

## Problem Description
In this project, you will build a simple machine learning model to predict students' exam scores based on their study hours.

You will use Python, NumPy, Matplotlib, and SymPy to explore mathematical concepts used in machine learning, including **partial derivatives, gradients, gradient descent, and the Hessian matrix**.

## Dataset

| Study Hours (X) | Exam Score (y) |
|---:|---:|
| 1 | 35 |
| 2 | 40 |
| 3 | 50 |
| 4 | 55 |
| 5 | 65 |
| 6 | 70 |
| 7 | 80 |
| 8 | 85 |

## Requirements

### Task 1: Create and Visualize the Dataset
- Create two NumPy arrays: `X` (students' study hours) and `y` (students' exam scores).
- Use Matplotlib to create a scatter plot of study hours versus exam scores.
- Add an appropriate title, axis labels, and grid.

### Task 2: Build a Simple Linear Prediction Model
Use the following model:

$$
\hat{y} = wX+b
$$

where `w` is the weight, `b` is the bias, and `ŷ` is the predicted exam score.

- Implement a `predict(X, w, b)` function.
- Implement a `compute_loss(y_true, y_pred)` function using Mean Squared Error (MSE):

$$
\mathrm{MSE}=\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat y_i)^2.
$$

- Initialize `w = 0` and `b = 0`. Calculate/display initial predictions and MSE.

### Task 3: Calculate Partial Derivatives and the Hessian
Consider the loss function for one sample:

$$
L(w,b)=(2w+b-5)^2.
$$

- Calculate the partial derivative of `L` with respect to `w`.
- Calculate the partial derivative of `L` with respect to `b`.
- Construct the gradient vector.
- Calculate/display the Hessian matrix using SymPy.

### Task 4: Implement Gradient Descent
Implement Gradient Descent from scratch to train the model on the dataset above.

For MSE, use:

$$
\frac{\partial L}{\partial w}=\frac{2}{n}\sum_i X_i(wX_i+b-y_i),\qquad
\frac{\partial L}{\partial b}=\frac{2}{n}\sum_i(wX_i+b-y_i).
$$

Update parameters by subtracting the learning rate multiplied by each gradient component.

- Initialize `w = 0`, `b = 0`.
- Set the learning rate to `0.01` and the number of epochs to `1000`.
- Calculate gradients and update `w`, `b` each epoch.
- Record MSE during training.
- Display final `w`, `b`, and MSE.

### Task 5: Analyze the Gradient and Hessian of the Full Dataset Loss
Apply the full-dataset loss:

$$
L(w,b)=\frac{1}{n}\sum_i(y_i-wX_i-b)^2.
$$

- Calculate/display the gradient vector and Hessian matrix.
- Evaluate the gradient at the trained `w` and `b`.
- Calculate Hessian eigenvalues using NumPy.
- Briefly explain what gradient and Hessian tell us about optimization.

*Chuyển từ `LAB SESSION 5_6.docx`. Các biểu thức toán vốn là đối tượng Word/hình công thức được trình bày lại bằng LaTeX để Markdown hiển thị ổn định. Dataset gốc có 8 hàng, được giữ nguyên theo đề.*

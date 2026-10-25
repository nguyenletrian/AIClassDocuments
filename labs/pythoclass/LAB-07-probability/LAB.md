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

*Chuyển từ `LAB SESSION 7.docx` sang Markdown.*

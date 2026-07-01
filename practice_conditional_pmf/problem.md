# Practice Problem: Empirical Conditional PMF

## Background

Given a dataset of paired observations $(x_i, y_i)$ for $i = 0, \ldots, N-1$, we want to estimate the **conditional probability mass function (PMF)** of $X$ given $Y = y^*$ empirically.

The empirical conditional PMF is defined as:

$$\hat{P}(X = k \mid Y = y^*) = \frac{\#\{i : x_i = k \text{ and } y_i = y^*\}}{\#\{i : y_i = y^*\}}$$

for each possible value $k$ of $X$.

## Task

Implement the function `compute_conditional_pmf(samples, y_target, x_values)` in `solution.py`.

**Given:**
- `samples`: a list of tuples `(x_i, y_i)` where each `x_i` and `y_i` is an integer
- `y_target`: an integer — the value of $Y$ we are conditioning on
- `x_values`: a sorted list of distinct integers — the possible values $X$ can take

**Return:**
- A `list` of floats of length `len(x_values)`, where the $k$-th element is the empirical estimate of $\hat{P}(X = x\_values[k] \mid Y = y\_target)$.
- If no sample has $y_i = y\_target$, return a list of zeros of length `len(x_values)`.
- Round each entry to **2 decimal places**.

## Examples

```python
samples = [(0, 1), (1, 1), (0, 1), (1, 0), (0, 0)]
y_target = 1
x_values = [0, 1]
# Among samples with Y=1: (0,1), (1,1), (0,1) → 3 total
# P(X=0|Y=1) = 2/3 ≈ 0.67,  P(X=1|Y=1) = 1/3 ≈ 0.33
# Result: [0.67, 0.33]
```

```python
samples = [(2, 0), (0, 1), (1, 0), (2, 0), (0, 0)]
y_target = 0
x_values = [0, 1, 2]
# Among samples with Y=0: (2,0), (1,0), (2,0), (0,0) → 4 total
# P(X=0|Y=0) = 1/4 = 0.25, P(X=1|Y=0) = 1/4 = 0.25, P(X=2|Y=0) = 2/4 = 0.5
# Result: [0.25, 0.25, 0.5]
```

## Constraints

- $1 \leq N \leq 10^5$
- All $x_i$ values appear in `x_values`
- `x_values` is sorted in ascending order and has no duplicates
- The returned list must sum to 1.0 (up to rounding) when there are matching samples

## Grading

- Public tests: basic correctness (visible, run with `pytest test_public.py`)
- Hidden tests: edge cases, large inputs, floating-point precision (run after submission)

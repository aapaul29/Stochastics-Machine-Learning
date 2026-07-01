# Practice Problem: Empirical PMF, Mean, and Variance

## Background

Given $N$ samples $x_1, \ldots, x_N$ from a discrete random variable $X$, the **empirical PMF** is:

$$\hat{P}(X = k) = \frac{\#\{i : x_i = k\}}{N}$$

The **sample mean** and **unbiased sample variance** are:

$$\hat{\mu} = \frac{1}{N}\sum_{i=1}^N x_i, \qquad \hat{\sigma}^2 = \frac{1}{N-1}\sum_{i=1}^N (x_i - \hat{\mu})^2$$

## Task

Implement the three functions in `solution.py`.

### `empirical_pmf(samples, k)`
- `samples`: list of integers; `k`: integer
- Return $\hat{P}(X=k)$ rounded to **4 decimal places**

### `empirical_mean(samples)`
- Return $\hat{\mu}$ rounded to **4 decimal places**

### `empirical_variance(samples)`
- Return $\hat{\sigma}^2$ (unbiased, divide by $N-1$) rounded to **4 decimal places**
- Return `0.0` if `len(samples) == 1`

## Example

```python
samples = [0, 1, 0, 2, 1, 0]
empirical_pmf(samples, 0)    # 3/6 = 0.5
empirical_pmf(samples, 1)    # 2/6 ≈ 0.3333
empirical_mean(samples)      # 4/6 ≈ 0.6667
empirical_variance(samples)  # ≈ 0.6667
```

## Grading
- `python run.py` → public tests
- `python run.py --all` → full grading

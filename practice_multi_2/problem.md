# Practice Problem: Empirical Covariance and Correlation

## Background

Given paired samples $(x_1,y_1),\ldots,(x_N,y_N)$:

$$\hat{\text{Cov}}(X,Y) = \frac{1}{N-1}\sum_{i=1}^N (x_i-\bar{x})(y_i-\bar{y})$$

$$\hat{\rho}(X,Y) = \frac{\hat{\text{Cov}}(X,Y)}{\hat{\sigma}_X \cdot \hat{\sigma}_Y}$$

where $\hat{\sigma}_X, \hat{\sigma}_Y$ are unbiased sample standard deviations (divided by $N-1$).

## Task

### `empirical_covariance(xs, ys)` → $\hat{\text{Cov}}(X,Y)$, rounded to **4 dp**. Return `0.0` if $N \leq 1$.
### `empirical_correlation(xs, ys)` → $\hat{\rho}$, rounded to **4 dp**. Return `0.0` if either variance is zero.

Both functions receive two equal-length lists of floats.

## Example

```python
xs = [1, 2, 3, 4, 5]
ys = [2, 4, 6, 8, 10]  # ys = 2*xs → perfect correlation
empirical_covariance(xs, ys)  # 5.0
empirical_correlation(xs, ys) # 1.0
```

## Grading
- `python run.py` → public tests
- `python run.py --all` → full grading

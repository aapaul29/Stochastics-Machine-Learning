# Practice Problem: Feature Standardization

## Background

**Standardization** (z-score normalization) maps each feature to zero mean and unit
variance. Given training data, we compute per-feature statistics:

$$\mu_j = \frac{1}{n}\sum_{i=1}^n X_{ij}, \qquad
  \sigma_j = \sqrt{\frac{1}{n}\sum_{i=1}^n (X_{ij} - \mu_j)^2}$$

(population standard deviation, not sample).

At test time, apply the **same** $\mu, \sigma$ from training:

$$X'_{ij} = \frac{X_{ij} - \mu_j}{\sigma_j}$$

If $\sigma_j = 0$, set the standardized value to $0.0$.

## Task

Implement the two functions in `solution.py`.

### `fit_standardizer(X_train)`
- `X_train`: list of $n$ rows, each a list of $d$ floats
- Return `(mu, sigma)` where `mu` and `sigma` are lists of $d$ floats rounded to **6 dp**

### `apply_standardizer(X, mu, sigma)`
- `X`: list of $m$ rows, each a list of $d$ floats
- `mu`, `sigma`: from `fit_standardizer`
- Return standardized matrix (list of lists), each value rounded to **6 dp**

## Example

```python
X = [[1.,2.],[3.,4.],[5.,6.]]
mu, sigma = fit_standardizer(X)
# mu = [3.0, 4.0],  sigma = [√(8/3), √(8/3)] ≈ [1.632993, 1.632993]
apply_standardizer([[1.,2.]], mu, sigma)
# → [[-1.224745, -1.224745]]
```

## Grading
- `python run.py` → public tests
- `python run.py --all` → full grading

# Practice Problem: CLT — Mean, Variance, and Probability of a Sum

## Background

For $S_n = X_1 + \cdots + X_n$ with i.i.d. $X_i \sim F$ (mean $\mu$, variance $\sigma^2$):

$$\mathbb{E}[S_n] = n\mu, \qquad \text{Var}(S_n) = n\sigma^2$$

By the CLT, for large $n$:

$$P(a \leq S_n \leq b) \approx \Phi\!\left(\frac{b - n\mu}{\sqrt{n}\,\sigma}\right) - \Phi\!\left(\frac{a - n\mu}{\sqrt{n}\,\sigma}\right)$$

## Task

Use `scipy.stats` distributions. Implement:

### `clt_mean(distribution, n)` → $\mathbb{E}[S_n]$, rounded to **4 dp**
### `clt_variance(distribution, n)` → $\text{Var}(S_n)$, rounded to **4 dp**
### `clt_prob(distribution, n, a, b)` → $P(a \leq S_n \leq b)$ via CLT, rounded to **4 dp**

`distribution` is a `scipy.stats` frozen distribution with `.mean()` and `.var()` methods.

## Example

```python
import scipy.stats
d = scipy.stats.poisson(mu=3)   # Poisson(3): mean=3, var=3
clt_mean(d, 10)      # 30.0
clt_variance(d, 10)  # 30.0
clt_prob(d, 100, 280, 320)  # P(S_100 in [280,320]) ≈ ?
```

## Grading
- `python run.py` → public tests
- `python run.py --all` → full grading

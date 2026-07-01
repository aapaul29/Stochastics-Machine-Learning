# Practice Problem: Binomial Distribution

## Background

If $X \sim \text{Bin}(n, p)$, its PMF and CDF are:

$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}, \qquad P(X \leq k) = \sum_{j=0}^{k} P(X=j)$$

with mean $\mathbb{E}[X] = np$ and variance $\text{Var}(X) = np(1-p)$.

## Task

Implement the three functions in `solution.py` using `scipy.stats.binom`.

### `binomial_pmf(n, p, k)` → $P(X=k)$, rounded to **4 dp**
### `binomial_cdf(n, p, k)` → $P(X \leq k)$, rounded to **4 dp**
### `binomial_mean_variance(n, p)` → tuple `(mean, variance)`, each rounded to **4 dp**

## Example

```python
# X ~ Bin(10, 0.3)
binomial_pmf(10, 0.3, 3)        # ≈ 0.2668
binomial_cdf(10, 0.3, 3)        # ≈ 0.6496
binomial_mean_variance(10, 0.3) # (3.0, 2.1)
```

## Grading
- `python run.py` → public tests
- `python run.py --all` → full grading

# Practice Problem: Poisson Distribution

## Background

If $X \sim \text{Poisson}(\lambda)$:

$$P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!}, \qquad \mathbb{E}[X] = \text{Var}(X) = \lambda$$

**Poisson approximation to Binomial:** for large $n$ and small $p$, $\text{Bin}(n,p) \approx \text{Poisson}(np)$.

## Task

### `poisson_pmf(lam, k)` → $P(X=k)$, rounded to **4 dp**
### `poisson_cdf(lam, k)` → $P(X \leq k)$, rounded to **4 dp**
### `poisson_approx_binomial(n, p, k)` → approximate $P(\text{Bin}(n,p)=k)$ using Poisson, rounded to **4 dp**

## Example

```python
poisson_pmf(3.0, 2)             # e^{-3} * 9 / 2 ≈ 0.2240
poisson_cdf(3.0, 2)             # P(X<=2) ≈ 0.4232
poisson_approx_binomial(1000, 0.003, 2)  # Poisson(3) PMF at k=2 ≈ 0.2240
```

## Grading
- `python run.py` → public tests
- `python run.py --all` → full grading

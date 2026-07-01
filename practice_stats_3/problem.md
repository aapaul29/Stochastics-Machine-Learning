# Practice Problem: Maximum Likelihood Estimation

## Background

**MLE for $\text{Exp}(\lambda)$:** the log-likelihood is maximised at:
$$\hat{\lambda} = \frac{1}{\bar{x}} = \frac{N}{\sum_i x_i}$$

**MLE for $\mathcal{N}(\mu,\sigma^2)$:**
$$\hat{\mu} = \bar{x}, \qquad \hat{\sigma} = \sqrt{\frac{1}{N}\sum_i (x_i - \bar{x})^2}$$

Note: the MLE for $\sigma$ divides by $N$ (biased), not $N-1$.

## Task

### `mle_exponential(samples)` → $\hat{\lambda}$, rounded to **4 dp**
### `mle_normal(samples)` → tuple $(\hat{\mu}, \hat{\sigma})$, each rounded to **4 dp**

## Example

```python
samples = [1.0, 2.0, 3.0]
mle_exponential(samples)  # 1 / 2.0 = 0.5
mle_normal(samples)       # (2.0, 0.8165)
```

## Grading
- `python run.py` → public tests
- `python run.py --all` → full grading

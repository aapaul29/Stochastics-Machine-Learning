# Practice Problem: Empirical CDF and Quantiles

## Background

The **empirical CDF** of samples $x_1,\ldots,x_N$ is:

$$\hat{F}_N(x) = \frac{1}{N} \#\{i : x_i \leq x\}$$

The **empirical $p$-quantile** is the smallest $x$ in the sorted sample such that $\hat{F}_N(x) \geq p$.

## Task

### `empirical_cdf(samples, x)` → $\hat{F}_N(x)$, rounded to **4 dp**
### `empirical_quantile(samples, p)` → smallest sample value $x$ with $\hat{F}_N(x) \geq p$

## Example

```python
samples = [1, 3, 2, 5, 4]
empirical_cdf(samples, 3)     # 3/5 = 0.6
empirical_cdf(samples, 2.5)   # 2/5 = 0.4
empirical_quantile(samples, 0.5)  # 3  (median)
empirical_quantile(samples, 0.0)  # 1  (minimum)
```

## Grading
- `python run.py` → public tests
- `python run.py --all` → full grading

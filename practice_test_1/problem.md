# Practice Problem: Confidence Interval for the Mean (Known Variance)

## Background

Given $n$ i.i.d. samples with **known** population standard deviation $\sigma$, a $(1-\alpha)$ confidence interval for the mean $\mu$ is:

$$\left[\bar{x} - z_{\alpha/2}\frac{\sigma}{\sqrt{n}},\quad \bar{x} + z_{\alpha/2}\frac{\sigma}{\sqrt{n}}\right]$$

where $z_{\alpha/2} = \Phi^{-1}(1-\alpha/2)$ is the standard normal quantile.

## Task

### `confidence_interval(samples, sigma, alpha)` → tuple `(lo, hi)`, each rounded to **4 dp**

- `samples`: list of floats
- `sigma`: known population standard deviation ($> 0$)
- `alpha`: significance level (e.g. `0.05` for a 95% CI)

Use `scipy.stats.norm.ppf`.

## Example

```python
samples = [2.1, 1.9, 2.0, 2.2, 1.8]
confidence_interval(samples, 0.5, 0.05)
# xbar=2.0, z=1.96, margin = 1.96*0.5/sqrt(5) ≈ 0.4382
# → (1.5618, 2.4382)
```

## Grading
- `python run.py` → public tests
- `python run.py --all` → full grading

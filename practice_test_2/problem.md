# Practice Problem: One-Sample t-Test

## Background

To test $H_0: \mu = \mu_0$ against $H_1: \mu \neq \mu_0$ with **unknown** $\sigma$, compute:

$$t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}, \quad s = \sqrt{\frac{1}{n-1}\sum(x_i-\bar{x})^2}$$

Under $H_0$, $t \sim t_{n-1}$. The two-sided p-value is:

$$p = 2 \cdot P(T \geq |t|) = 2 \cdot (1 - F_{t_{n-1}}(|t|))$$

## Task

### `t_statistic(samples, mu0)` → $t$, rounded to **4 dp**
### `p_value(samples, mu0)` → two-sided p-value, rounded to **4 dp**
### `reject_null(samples, mu0, alpha)` → `True` if p-value $< \alpha$

Use `scipy.stats.t`.

## Example

```python
samples = [2.5, 3.1, 2.8, 3.2, 2.9]
t_statistic(samples, 3.0)   # ≈ -0.6547
p_value(samples, 3.0)       # ≈ 0.5479
reject_null(samples, 3.0, 0.05)  # False
```

## Grading
- `python run.py` → public tests
- `python run.py --all` → full grading

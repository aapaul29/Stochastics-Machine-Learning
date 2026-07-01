# Practice Problem: Exponential Distribution

## Background

If $X \sim \text{Exp}(\lambda)$:

$$f(x) = \lambda e^{-\lambda x} \,(x \geq 0), \qquad F(x) = 1 - e^{-\lambda x}, \qquad Q(p) = -\frac{\ln(1-p)}{\lambda}$$

with $\mathbb{E}[X] = 1/\lambda$ and $\text{Var}(X) = 1/\lambda^2$.

## Task

### `exp_pdf(lam, x)` → $f(x)$, rounded to **4 dp** (return `0.0` if $x < 0$)
### `exp_cdf(lam, x)` → $F(x)$, rounded to **4 dp** (return `0.0` if $x < 0$)
### `exp_quantile(lam, p)` → $Q(p)$, rounded to **4 dp** (assume $0 < p < 1$)

## Example

```python
exp_pdf(2.0, 1.0)      # 2*e^{-2} ≈ 0.2707
exp_cdf(2.0, 1.0)      # 1 - e^{-2} ≈ 0.8647
exp_quantile(2.0, 0.5) # median = ln(2)/2 ≈ 0.3466
```

## Grading
- `python run.py` → public tests
- `python run.py --all` → full grading

# Practice Problem: Joint PMF, Marginals, and Independence

## Background

Given $N$ paired samples $(x_i, y_i)$, the **empirical joint PMF** is:

$$\hat{P}(X=x, Y=y) = \frac{\#\{i: x_i=x,\, y_i=y\}}{N}$$

**Marginals:**

$$\hat{P}(X=x) = \sum_y \hat{P}(X=x, Y=y), \qquad \hat{P}(Y=y) = \sum_x \hat{P}(X=x, Y=y)$$

$X$ and $Y$ are **empirically independent** if for all observed $(x,y)$:

$$\left|\hat{P}(X=x, Y=y) - \hat{P}(X=x)\cdot\hat{P}(Y=y)\right| < \varepsilon$$

## Task

### `empirical_joint(samples, x_val, y_val)` → $\hat{P}(X=x\_val, Y=y\_val)$, rounded to **4 dp**
### `empirical_marginal_x(samples, x_val)` → $\hat{P}(X=x\_val)$, rounded to **4 dp**
### `empirical_marginal_y(samples, y_val)` → $\hat{P}(Y=y\_val)$, rounded to **4 dp**
### `are_independent(samples, x_vals, y_vals, eps)` → `True` if all pairs satisfy the independence condition

## Example

```python
samples = [(0,0),(0,1),(1,0),(1,1)]  # uniform on {0,1}²
empirical_joint(samples, 0, 0)   # 0.25
empirical_marginal_x(samples, 0) # 0.5
are_independent(samples, [0,1], [0,1], 0.01)  # True
```

## Grading
- `python run.py` → public tests
- `python run.py --all` → full grading

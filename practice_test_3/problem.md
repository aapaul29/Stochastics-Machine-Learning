# Practice Problem: Two-Sample Welch's t-Test

## Background

To compare means of two independent samples $x_1,\ldots,x_m$ and $y_1,\ldots,y_n$, use **Welch's t-test**:

$$t = \frac{\bar{x} - \bar{y}}{\sqrt{\frac{s_x^2}{m} + \frac{s_y^2}{n}}}$$

with approximate degrees of freedom (Welch–Satterthwaite):

$$\nu = \frac{\left(\frac{s_x^2}{m}+\frac{s_y^2}{n}\right)^2}{\frac{(s_x^2/m)^2}{m-1}+\frac{(s_y^2/n)^2}{n-1}}$$

Two-sided p-value: $p = 2 \cdot P(T_\nu \geq |t|)$.

## Task

### `welch_t_statistic(xs, ys)` → $t$, rounded to **4 dp**
### `welch_p_value(xs, ys)` → two-sided p-value, rounded to **4 dp**
### `reject_null(xs, ys, alpha)` → `True` if p-value $< \alpha$

Use `scipy.stats`.

## Example

```python
xs = [2.1, 2.5, 2.3, 2.8]
ys = [1.9, 1.7, 2.0, 1.8]
# Means differ → should reject at alpha=0.05
```

## Grading
- `python run.py` → public tests
- `python run.py --all` → full grading

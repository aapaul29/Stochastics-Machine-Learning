# Practice Problem: MSE and R²

## Background

Two fundamental regression metrics:

**Mean Squared Error (MSE):**

$$\text{MSE} = \frac{1}{n}\sum_{i=1}^n (y_i - \hat{y}_i)^2$$

**Coefficient of Determination ($R^2$):**

$$R^2 = 1 - \frac{\sum_{i=1}^n (y_i - \hat{y}_i)^2}{\sum_{i=1}^n (y_i - \bar{y})^2}$$

where $\bar{y} = \frac{1}{n}\sum_i y_i$ is the mean of the true values.

$R^2 = 1$ means a perfect fit; $R^2 = 0$ means the model is no better than predicting the mean.

## Task

Implement `mse(y_true, y_pred)` and `r_squared(y_true, y_pred)` in `solution.py`.

**Given:**
- `y_true`: list of floats — ground-truth targets
- `y_pred`: list of floats — model predictions (same length)

**Return:** float rounded to **4 dp**.

For `r_squared`, if $\sum (y_i - \bar y)^2 = 0$ (all targets identical), return `1.0` if predictions also all match, otherwise `0.0`.

## Example

```python
y_true = [3.0, -0.5, 2.0, 7.0]
y_pred = [2.5,  0.0, 2.0, 8.0]
mse(y_true, y_pred)        # → 0.375
r_squared(y_true, y_pred)  # → 0.9486
```

## Grading
- `python run.py` → public tests
- `python run.py --all` → full grading

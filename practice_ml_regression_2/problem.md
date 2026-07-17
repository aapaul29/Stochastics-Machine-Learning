# Practice Problem: Ridge Regression

## Background

**Ridge regression** adds an $\ell_2$ penalty to the OLS objective:

$$w^* = \arg\min_w \|Xw - y\|^2 + \lambda \|w\|^2$$

The closed-form solution is:

$$w^* = (X^\top X + \lambda I)^{-1} X^\top y$$

where $I$ is the identity matrix. A bias column (all-ones) is prepended to $X$
**before** solving, but the regularisation penalty is usually applied to all weights
including the bias (the simpler convention we use here).

## Task

Implement `ridge_regression(X, y, lam)` in `solution.py`.

**Given:**
- `X`: list of $n$ rows, each a list of $d$ floats (no bias column)
- `y`: list of $n$ floats
- `lam`: float — regularisation parameter $\lambda \geq 0$

**Return:** weight vector $[w_0, w_1, \ldots, w_d]$ as a list of floats rounded to **4 dp**.

Use `numpy` for matrix operations.

## Example

```python
X = [[0.], [1.], [2.], [3.]]
y = [1., 3., 5., 7.]
ridge_regression(X, y, lam=0.0)  # → [1.0, 2.0]  (same as OLS when lam=0)
ridge_regression(X, y, lam=10.0) # regularised solution (bias towards 0)
```

## Grading
- `python run.py` → public tests
- `python run.py --all` → full grading

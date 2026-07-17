# Practice Problem: Polynomial Feature Expansion

## Background

To fit a polynomial of degree $n$ using linear algebra, we map a scalar $x$ to a
feature vector:

$$\phi(x) = [1,\; x,\; x^2,\; \ldots,\; x^n]$$

This allows us to use the linear model $\hat y = w \cdot \phi(x)$ to represent
non-linear functions of $x$.

## Task

Implement `poly_features(x, degree)` in `solution.py`.

**Given:**
- `x`: float — input scalar
- `degree`: int $\geq 0$ — polynomial degree

**Return:** list of `degree + 1` floats $[1.0, x, x^2, \ldots, x^{\text{degree}}]$,
each rounded to **6 dp**.

## Example

```python
poly_features(2.0, 3)   # → [1.0, 2.0, 4.0, 8.0]
poly_features(0.5, 2)   # → [1.0, 0.5, 0.25]
poly_features(3.0, 0)   # → [1.0]
```

## Grading
- `python run.py` → public tests
- `python run.py --all` → full grading

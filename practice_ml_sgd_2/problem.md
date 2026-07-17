# Practice Problem: Polynomial SGD Update

## Background

Given a polynomial of degree $n$:

$$p(x) = w_0 + w_1 x + w_2 x^2 + \cdots + w_n x^n$$

the squared loss on a single sample $(x, y)$ is:

$$\ell(w) = \bigl(p(x) - y\bigr)^2$$

The partial derivative with respect to $w_i$ is:

$$\frac{\partial \ell}{\partial w_i} = 2\,(p(x) - y)\,x^i$$

One SGD step:

$$w_i \leftarrow w_i - \alpha \cdot 2\,(p(x) - y)\,x^i$$

## Task

Implement `poly_sgd_update(w, x, y, alpha)` in `solution.py`.

**Given:**
- `w`: list of floats $[w_0, w_1, \ldots, w_n]$ — current coefficients
- `x`: float — input value
- `y`: float — target value
- `alpha`: float — learning rate

**Return:** new list of coefficients, each rounded to **6 dp**.

## Example

```python
# p(x) = 0 + 0*2 + 0*4 = 0,  error = 0 - 3 = -3
# grad = [2*(-3)*1, 2*(-3)*2, 2*(-3)*4] = [-6, -12, -24]
# w_new = [0-0.01*(-6), 0-0.01*(-12), 0-0.01*(-24)]
poly_sgd_update([0.0, 0.0, 0.0], 2.0, 3.0, 0.01)
# → [0.06, 0.12, 0.24]
```

## Grading
- `python run.py` → public tests
- `python run.py --all` → full grading

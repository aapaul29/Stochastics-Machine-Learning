# Practice Problem: Linear SGD Update

## Background

In **stochastic gradient descent (SGD)** for linear regression, we minimise the
squared loss over a single sample $(x, y)$:

$$\ell(w, b) = \bigl(w \cdot x + b - y\bigr)^2$$

The gradients are:

$$\frac{\partial \ell}{\partial w_i} = 2\,(w \cdot x + b - y)\,x_i, \qquad
  \frac{\partial \ell}{\partial b}   = 2\,(w \cdot x + b - y)$$

One SGD step with learning rate $\alpha$ updates:

$$w_i \leftarrow w_i - \alpha \frac{\partial \ell}{\partial w_i}, \qquad
  b   \leftarrow b   - \alpha \frac{\partial \ell}{\partial b}$$

## Task

Implement `sgd_update(w, b, x, y, alpha)` in `solution.py`.

**Given:**
- `w`: list of floats — current weight vector
- `b`: float — current bias
- `x`: list of floats — feature vector (same length as `w`)
- `y`: float — target value
- `alpha`: float — learning rate $> 0$

**Return:** tuple `(w_new, b_new)` where
- `w_new` is a **new list** of updated weights, each rounded to **6 dp**
- `b_new` is the updated bias, rounded to **6 dp**

Do **not** modify `w` in place.

## Example

```python
w = [1.0, 0.0]
b = 0.0
x = [2.0, 3.0]
y = 5.0
alpha = 0.01

# prediction = 1*2 + 0*3 + 0 = 2,  error = 2 - 5 = -3
# grad_w = [2*(-3)*2, 2*(-3)*3] = [-12, -18]
# grad_b = 2*(-3) = -6
# w_new = [1-0.01*(-12), 0-0.01*(-18)] = [1.12, 0.18]
# b_new = 0 - 0.01*(-6) = 0.06
sgd_update(w, b, x, y, alpha)  # ([1.12, 0.18], 0.06)
```

## Grading
- `python run.py` → public tests
- `python run.py --all` → full grading

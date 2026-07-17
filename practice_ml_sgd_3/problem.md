# Practice Problem: Mini-Batch Gradient Descent

## Background

**Mini-batch gradient descent** updates weights using the **average gradient** over a
batch of $m$ samples:

$$\nabla_w \mathcal{L} = \frac{2}{m}\sum_{i=1}^m (w\cdot x_i + b - y_i)\,x_i, \qquad
  \nabla_b \mathcal{L} = \frac{2}{m}\sum_{i=1}^m (w\cdot x_i + b - y_i)$$

Update rule:

$$w \leftarrow w - \alpha \nabla_w \mathcal{L}, \qquad b \leftarrow b - \alpha \nabla_b \mathcal{L}$$

## Task

Implement `minibatch_sgd_step(w, b, X_batch, y_batch, alpha)` in `solution.py`.

**Given:**
- `w`: list of floats — weight vector (length $d$)
- `b`: float — bias
- `X_batch`: list of $m$ lists (each of length $d$) — batch of feature vectors
- `y_batch`: list of $m$ floats — batch of targets
- `alpha`: float — learning rate

**Return:** `(w_new, b_new)`, each value rounded to **6 dp**.

## Example

```python
w = [1.0]
b = 0.0
X_batch = [[1.0], [2.0], [3.0]]
y_batch  = [1.0,   2.0,   3.0]   # perfect prediction → no update
minibatch_sgd_step(w, b, X_batch, y_batch, 0.01)
# → ([1.0], 0.0)
```

## Grading
- `python run.py` → public tests
- `python run.py --all` → full grading

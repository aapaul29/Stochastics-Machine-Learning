# Practice Problem: Perceptron Learning Rule

## Background

The **Perceptron** is a binary linear classifier. Given weight vector $w$, bias $b$,
and input $x$, it predicts:

$$\hat{y} = \begin{cases} +1 & \text{if } w \cdot x + b \geq 0 \\ -1 & \text{otherwise} \end{cases}$$

The **Perceptron update rule** (with learning rate $\alpha$) corrects on
misclassified samples (where $y \in \{-1, +1\}$):

$$w_i \leftarrow w_i + \alpha \, y \, x_i, \qquad b \leftarrow b + \alpha \, y$$

If the prediction is **correct** ($\hat y = y$), do **not** update.

## Task

Implement the two functions in `solution.py`.

### `perceptron_predict(w, b, x)`
- Return $+1$ if $w \cdot x + b \geq 0$, else $-1$ (as int)

### `perceptron_update(w, b, x, y, alpha)`
- Apply the update rule if misclassified
- Return `(w_new, b_new)`, each value rounded to **6 dp**

## Example

```python
w = [0., 0.]
b = 0.
perceptron_predict(w, b, [1., 2.])   # → +1   (0 ≥ 0)
perceptron_update(w, b, [1., 1.], -1, 0.1)
# misclassified: w → [0-0.1*1, 0-0.1*1], b → 0-0.1 = -0.1
# → ([-0.1, -0.1], -0.1)
```

## Grading
- `python run.py` → public tests
- `python run.py --all` → full grading

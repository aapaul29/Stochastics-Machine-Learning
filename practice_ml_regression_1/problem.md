# Practice Problem: Normal Equations (OLS)

## Background

For linear regression with data matrix $X \in \mathbb{R}^{n \times d}$ and targets
$y \in \mathbb{R}^n$, the **ordinary least squares (OLS)** solution minimises the
squared error:

$$w^* = \arg\min_w \|Xw - y\|^2$$

The closed-form solution is the **normal equations**:

$$w^* = (X^\top X)^{-1} X^\top y$$

To include a bias term, prepend a column of ones to $X$ before solving.

## Task

Implement the two functions in `solution.py`.

### `add_bias_column(X)`
- `X`: list of $n$ rows, each a list of $d$ floats
- Return a new matrix with a column of $1.0$ prepended to each row

### `normal_equations(X, y)`
- `X`: list of $n$ rows (already **without** bias — the function adds it internally)
- `y`: list of $n$ floats
- Return the weight vector $w^*$ as a list of floats rounded to **4 dp**
  (first element is the bias $w_0$, then $w_1, \ldots, w_d$)
- Use `numpy` for matrix operations.

## Example

```python
# y = 1 + 2*x  →  w* = [1.0, 2.0]
X = [[0.0], [1.0], [2.0], [3.0]]
y = [1.0, 3.0, 5.0, 7.0]
normal_equations(X, y)   # → [1.0, 2.0]
```

## Grading
- `python run.py` → public tests
- `python run.py --all` → full grading

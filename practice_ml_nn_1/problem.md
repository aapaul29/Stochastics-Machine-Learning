# Practice Problem: Activation Functions

## Background

**Sigmoid** is the standard binary activation:

$$\sigma(z) = \frac{1}{1 + e^{-z}}$$

Its derivative (useful for backprop):

$$\sigma'(z) = \sigma(z)\,(1 - \sigma(z))$$

**Softmax** converts a vector of real scores to a probability distribution:

$$\text{softmax}(z)_i = \frac{e^{z_i}}{\sum_j e^{z_j}}$$

For numerical stability, subtract the maximum before exponentiating:
$z'_i = z_i - \max(z)$.

## Task

Implement the three functions in `solution.py`.

### `sigmoid(z)` — float → float, rounded to **6 dp**
### `sigmoid_derivative(z)` — float → float, rounded to **6 dp**
### `softmax(z)` — list[float] → list[float], each rounded to **6 dp**

The three values in `softmax(z)` must sum to 1 (within floating-point rounding).

## Example

```python
sigmoid(0.0)              # → 0.5
sigmoid_derivative(0.0)   # → 0.25
softmax([1., 2., 3.])     # → [0.090031, 0.244728, 0.665241]
```

## Grading
- `python run.py` → public tests
- `python run.py --all` → full grading

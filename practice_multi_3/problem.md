# Practice Problem: Gaussian Mixture Model

## Background

A **Gaussian mixture** with $K$ components has PDF:

$$f(x) = \sum_{k=1}^K w_k \cdot \varphi(x;\, \mu_k, \sigma_k)$$

where $\varphi(x;\mu,\sigma) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$ and $\sum_k w_k = 1$.

Its **mean** and **variance** are:

$$\mathbb{E}[X] = \sum_k w_k \mu_k, \qquad \text{Var}(X) = \sum_k w_k(\sigma_k^2 + \mu_k^2) - \left(\sum_k w_k \mu_k\right)^2$$

## Task

### `mixture_pdf(x, weights, means, stds)` → $f(x)$, rounded to **4 dp**
### `mixture_mean(weights, means)` → $\mathbb{E}[X]$, rounded to **4 dp**
### `mixture_variance(weights, means, stds)` → $\text{Var}(X)$, rounded to **4 dp**

All inputs are lists of floats with `len(weights)==len(means)==len(stds)`.

## Example

```python
weights=[0.5,0.5]; means=[-1.0,1.0]; stds=[0.5,0.5]
mixture_mean(weights, means)     # 0.0
mixture_variance(weights, means, stds) # 0.5^2 + 1^2 = 1.25
```

## Grading
- `python run.py` → public tests
- `python run.py --all` → full grading

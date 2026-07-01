# Practice Problem: Law of Large Numbers

## Background

The **Weak Law of Large Numbers** states that for i.i.d. $X_1, X_2, \ldots$ with mean $\mu$, the running average converges in probability:

$$\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i \xrightarrow{P} \mu \quad \text{as } n \to \infty$$

## Task

### `running_average(samples)` → list of floats, where the $n$-th element is $\bar{X}_n = \frac{1}{n}\sum_{i=1}^n x_i$. Round each entry to **4 dp**.

### `lln_converges(samples, true_mean, eps)` → `True` if the **final** running average satisfies $|\bar{X}_N - \mu| < \varepsilon$

### `convergence_index(samples, true_mean, eps)` → smallest $n$ (1-indexed) such that all subsequent running averages are within $\varepsilon$ of `true_mean`. Return $N$ if no such $n$ exists.

## Example

```python
import random; random.seed(0)
samples = [random.expovariate(1) for _ in range(1000)]  # E[X]=1
ra = running_average(samples)
lln_converges(samples, 1.0, 0.1)  # True (likely)
```

## Grading
- `python run.py` → public tests
- `python run.py --all` → full grading

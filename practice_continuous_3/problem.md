# Practice Problem: Simulating Random Variables via Inverse CDF

## Background

The **inverse CDF (quantile) method** generates samples from any distribution:
if $U \sim \text{Uniform}(0,1)$ and $F$ is a CDF, then $X = F^{-1}(U)$ has distribution $F$.

For $\text{Exp}(\lambda)$: $F^{-1}(u) = -\frac{\ln(1-u)}{\lambda}$

For $\text{Uniform}(a,b)$: $F^{-1}(u) = a + (b-a)\,u$

## Task

### `simulate_exponential(lam, n, seed)` → list of `n` floats sampled from $\text{Exp}(\lambda)$ using the inverse CDF method and `random.random()` with the given seed

### `simulate_uniform(a, b, n, seed)` → list of `n` floats sampled from $\text{Uniform}(a,b)$ using inverse CDF and `random.random()`

Both functions must set `random.seed(seed)` before generating samples. Round each sample to **4 dp**.

## Example

```python
simulate_exponential(1.0, 3, 42)  # 3 samples from Exp(1)
simulate_uniform(0, 1, 3, 42)     # 3 samples from U(0,1)
```

## Grading
- `python run.py` → public tests
- `python run.py --all` → full grading

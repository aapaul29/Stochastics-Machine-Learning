# Practice Problem: Summary Statistics

## Background

Given a sample $x_1,\ldots,x_N$, the key summary statistics are:

$$\bar{x} = \frac{1}{N}\sum x_i, \quad s^2 = \frac{1}{N-1}\sum(x_i-\bar{x})^2, \quad \text{median} = \text{middle value}, \quad \text{IQR} = Q_{0.75} - Q_{0.25}$$

Quantile $Q_p$: sort the data; $Q_p$ is the value at position $p(N-1)$ (linear interpolation).

## Task

### `sample_mean(data)` → $\bar{x}$, rounded to **4 dp**
### `sample_variance(data)` → $s^2$ (unbiased), rounded to **4 dp**. Return `0.0` if $N=1$.
### `sample_median(data)` → median, rounded to **4 dp**
### `sample_iqr(data)` → IQR = $Q_{0.75} - Q_{0.25}$, rounded to **4 dp**

You may use `statistics` or `numpy` — but **not** `scipy.stats.describe`.

## Example

```python
data = [2, 4, 4, 4, 5, 5, 7, 9]
sample_mean(data)     # 5.0
sample_variance(data) # 4.5714...
sample_median(data)   # 4.5
sample_iqr(data)      # 2.5
```

## Grading
- `python run.py` → public tests
- `python run.py --all` → full grading

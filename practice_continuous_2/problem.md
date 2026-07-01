# Practice Problem: Normal Distribution

## Background

If $X \sim \mathcal{N}(\mu, \sigma^2)$, we standardize to $Z = (X-\mu)/\sigma \sim \mathcal{N}(0,1)$ and compute probabilities:

$$P(a \leq X \leq b) = \Phi\!\left(\frac{b-\mu}{\sigma}\right) - \Phi\!\left(\frac{a-\mu}{\sigma}\right)$$

where $\Phi$ is the standard normal CDF. The **$p$-quantile** satisfies $P(X \leq q_p) = p$.

## Task

### `standardize(x, mu, sigma)` → $(x-\mu)/\sigma$, rounded to **4 dp**
### `normal_prob(mu, sigma, a, b)` → $P(a \leq X \leq b)$, rounded to **4 dp**
### `normal_quantile(mu, sigma, p)` → $q_p$ such that $P(X \leq q_p)=p$, rounded to **4 dp**

Use `scipy.stats.norm`.

## Example

```python
standardize(1.5, 1.0, 0.5)        # (1.5-1)/0.5 = 1.0
normal_prob(0, 1, -1, 1)          # ≈ 0.6827  (68% rule)
normal_quantile(0, 1, 0.975)      # ≈ 1.96
```

## Grading
- `python run.py` → public tests
- `python run.py --all` → full grading

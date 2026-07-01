# Practice Problem: Empirical Bayes from Samples

## Background

Given $N$ paired observations $(x_i, y_i)$ where $Y$ is a **class label** and $X$ is an **observed feature**, we can estimate all relevant probabilities empirically:

**Empirical joint probability:**
$$\hat{P}(X = x, Y = c) = \frac{\#\{i : x_i = x \text{ and } y_i = c\}}{N}$$

**Empirical marginal (prior):**
$$\hat{P}(Y = c) = \frac{\#\{i : y_i = c\}}{N}$$

**Empirical posterior** via Bayes:
$$\hat{P}(Y = c \mid X = x) = \frac{\hat{P}(X = x, Y = c)}{\hat{P}(X = x)} = \frac{\#\{i : x_i = x,\, y_i = c\}}{\#\{i : x_i = x\}}$$

## Task

Implement the three functions in `solution.py`.

### `empirical_prior(samples, c)`
**Given:**
- `samples`: list of `(x_i, y_i)` tuples
- `c`: a class label (int)

**Return:** $\hat{P}(Y = c)$ as a `float`, rounded to **4 decimal places**.

---

### `empirical_posterior(samples, x_val, c)`
**Given:**
- `samples`: list of `(x_i, y_i)` tuples
- `x_val`: the observed feature value (int)
- `c`: a class label (int)

**Return:** $\hat{P}(Y = c \mid X = x\_val)$ rounded to **4 decimal places**.  
Return `0.0` if no sample has $X = x\_val$.

---

### `most_likely_class(samples, x_val, classes)`
**Given:**
- `samples`: list of `(x_i, y_i)` tuples
- `x_val`: the observed feature value (int)
- `classes`: a list of distinct class labels (ints)

**Return:** the class label $c^*$ in `classes` that maximises $\hat{P}(Y = c \mid X = x\_val)$.  
Break ties by returning the **smallest** class label.  
If no sample has $X = x\_val$, return the class with the highest **prior** $\hat{P}(Y = c)$.

## Examples

```python
samples = [(0,0), (0,1), (0,0), (1,1), (1,1), (0,1)]
# Priors: P(Y=0) = 2/6 ≈ 0.3333,  P(Y=1) = 4/6 ≈ 0.6667
empirical_prior(samples, 0)   # → 0.3333
empirical_prior(samples, 1)   # → 0.6667

# P(Y=0 | X=0): among X=0: (0,0),(0,1),(0,0),(0,1) → 4 total, 2 are Y=0 → 0.5
empirical_posterior(samples, 0, 0)  # → 0.5
empirical_posterior(samples, 0, 1)  # → 0.5

# P(Y=1 | X=1): among X=1: (1,1),(1,1) → both Y=1 → 1.0
most_likely_class(samples, 1, [0, 1])  # → 1
```

## Constraints

- $1 \leq N \leq 10^5$
- All $(x_i, y_i)$ values are non-negative integers
- `classes` contains no duplicates and is sorted

## Grading

- Public tests: basic correctness (run with `python run.py`)
- Hidden tests: unseen x_val, large inputs, tie-breaking

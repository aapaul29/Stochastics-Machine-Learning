# Practice Problem: Bayes' Theorem

## Background

Given a hypothesis $H$ and evidence $E$, Bayes' theorem relates the **posterior** $P(H \mid E)$ to the **prior** $P(H)$ and the **likelihoods** $P(E \mid H)$ and $P(E \mid \neg H)$:

$$P(H \mid E) = \frac{P(E \mid H) \cdot P(H)}{P(E)}$$

where the **marginal probability** of the evidence follows from the Law of Total Probability:

$$P(E) = P(E \mid H) \cdot P(H) + P(E \mid \neg H) \cdot P(\neg H)$$

## Task

Implement the two functions in `solution.py`.

### `marginal_probability(prior, likelihood, likelihood_complement)`

**Given:**
- `prior` $= P(H) \in (0, 1)$
- `likelihood` $= P(E \mid H) \in [0, 1]$
- `likelihood_complement` $= P(E \mid \neg H) \in [0, 1]$

**Return:** $P(E)$ as a `float`, rounded to **4 decimal places**.

---

### `bayes_posterior(prior, likelihood, likelihood_complement)`

**Given:** same inputs as above.

**Return:** $P(H \mid E)$ as a `float`, rounded to **4 decimal places**.

## Examples

```python
# A disease affects 1% of the population.
# A test is positive for 99% of sick people and 5% of healthy people.
prior               = 0.01   # P(sick)
likelihood          = 0.99   # P(positive | sick)
likelihood_complement = 0.05  # P(positive | healthy)

marginal_probability(prior, likelihood, likelihood_complement)
# P(positive) = 0.99*0.01 + 0.05*0.99 = 0.0099 + 0.0495 = 0.0594
# → 0.0594

bayes_posterior(prior, likelihood, likelihood_complement)
# P(sick | positive) = 0.0099 / 0.0594 ≈ 0.1667
# → 0.1667
```

## Constraints

- $0 < \text{prior} < 1$
- $0 \leq \text{likelihood},\ \text{likelihood\_complement} \leq 1$
- $P(E) > 0$ is guaranteed (no division by zero)
- Round both outputs to **4 decimal places**

## Grading

- Public tests: basic correctness (run with `python run.py`)
- Hidden tests: boundary values, floating-point precision

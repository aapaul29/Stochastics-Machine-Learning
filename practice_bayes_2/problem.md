# Practice Problem: Law of Total Probability & Most Likely Cause

## Background

Given a **partition** $\{A_1, \ldots, A_n\}$ of the sample space (i.e. the $A_i$ are mutually exclusive and exhaustive), the **Law of Total Probability** states:

$$P(B) = \sum_{i=1}^{n} P(B \mid A_i) \cdot P(A_i)$$

By Bayes' theorem, the **posterior probability** of each cause $A_i$ given that $B$ occurred is:

$$P(A_i \mid B) = \frac{P(B \mid A_i) \cdot P(A_i)}{P(B)}$$

The **most likely cause** is the index $i^*$ that maximises $P(A_i \mid B)$:

$$i^* = \arg\max_{i} \; P(A_i \mid B) = \arg\max_{i} \; P(B \mid A_i) \cdot P(A_i)$$

## Task

Implement the two functions in `solution.py`.

### `total_probability(priors, conditionals)`

**Given:**
- `priors`: a list of floats $[P(A_1), \ldots, P(A_n)]$ that sum to 1
- `conditionals`: a list of floats $[P(B \mid A_1), \ldots, P(B \mid A_n)]$

**Return:** $P(B)$ as a `float`, rounded to **4 decimal places**.

---

### `most_likely_cause(priors, conditionals)`

**Given:** same inputs as above.

**Return:** the **0-based index** $i^*$ of the partition element with the highest posterior $P(A_{i^*} \mid B)$.

If two causes tie, return the one with the **smaller index**.

## Examples

```python
# Three machines produce a part. Machine 1 makes 50%, Machine 2 makes 30%, Machine 3 makes 20%.
# Defect rates: 2%, 5%, 10%.
priors       = [0.5, 0.3, 0.2]
conditionals = [0.02, 0.05, 0.10]

total_probability(priors, conditionals)
# P(defect) = 0.5*0.02 + 0.3*0.05 + 0.2*0.10
#           = 0.01 + 0.015 + 0.02 = 0.045
# → 0.045

most_likely_cause(priors, conditionals)
# P(A1|defect) ∝ 0.5*0.02 = 0.010
# P(A2|defect) ∝ 0.3*0.05 = 0.015
# P(A3|defect) ∝ 0.2*0.10 = 0.020  ← highest
# → 2
```

## Constraints

- $2 \leq n \leq 100$
- `priors` sums to 1 (within floating-point tolerance)
- All values in $[0, 1]$
- $P(B) > 0$ is guaranteed

## Grading

- Public tests: basic correctness (run with `python run.py`)
- Hidden tests: edge cases, ties, large $n$

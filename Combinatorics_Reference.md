# Combinatorics Reference

## The Four Fundamental Cases

| | **No Repetition** | **With Repetition** |
|---|---|---|
| **Ordered** | $\dfrac{n!}{(n-k)!}$ | $n^k$ |
| **Unordered** | $\dbinom{n}{k} = \dfrac{n!}{k!(n-k)!}$ | $\dbinom{n+k-1}{k}$ |

- **n** = total distinct objects, **k** = number chosen
- "Ordered" = order matters (sequences, arrangements)
- "Unordered" = order doesn't matter (subsets, groups)

---

## All Cases Explained

| Case | Formula | When to use | Example |
|---|---|---|---|
| **Ordered, no repetition** (k-permutation) | $\frac{n!}{(n-k)!}$ | Arranging k items from n, no reuse | How many 3-digit PINs from {1..9} with no repeat? → $9 \cdot 8 \cdot 7 = 504$ |
| **Ordered, with repetition** | $n^k$ | Sequences where each slot has n choices | How many 3-digit PINs from {0..9}? → $10^3 = 1000$ |
| **Unordered, no repetition** (combination) | $\binom{n}{k}$ | Choosing a subset, order irrelevant | Choose 3 people from 10 → $\binom{10}{3} = 120$ |
| **Unordered, with repetition** (multiset) | $\binom{n+k-1}{k}$ | Choosing k items from n types, unlimited supply | Buy 4 fruits from 3 types → $\binom{6}{4} = 15$ |
| **Full permutation** | $n!$ | Arrange all n items | Arrange 5 books → $5! = 120$ |
| **Multinomial** | $\frac{n!}{n_1!\, n_2!\, \cdots\, n_r!}$ | Arrange n items with repeated groups | Arrange MISSISSIPPI → $\frac{11!}{4!4!2!1!}$ |

---

## Multinomial Coefficient

Arranging $n$ objects where group $i$ has $n_i$ identical items ($n_1 + n_2 + \cdots + n_r = n$):

$$\binom{n}{n_1,\, n_2,\, \ldots,\, n_r} = \frac{n!}{n_1!\, n_2!\, \cdots\, n_r!}$$

**Dice example:** Probability of four 6's and two 4's in 6 rolls:
$$\frac{6!}{4!\,2!} = 15 \text{ arrangements} \implies P = \frac{15}{6^6}$$

---

## Binomial Coefficient Properties

| Property | Formula |
|---|---|
| Symmetry | $\binom{n}{k} = \binom{n}{n-k}$ |
| Pascal's rule | $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$ |
| Sum of row | $\sum_{k=0}^{n} \binom{n}{k} = 2^n$ |
| Binomial theorem | $(x+y)^n = \sum_{k=0}^{n} \binom{n}{k} x^k y^{n-k}$ |
| Vandermonde | $\binom{m+n}{r} = \sum_{k=0}^{r} \binom{m}{k}\binom{n}{r-k}$ |

---

## Inclusion-Exclusion

For two events: $|A \cup B| = |A| + |B| - |A \cap B|$

For three events: $|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|$

General principle — alternate adding and subtracting intersections of increasing size.

---

## Complementary Counting

When "at least one" or "at least k" appears, count the complement:

$$P(\text{at least one}) = 1 - P(\text{none})$$
$$P(\text{at least k}) = 1 - P(0) - P(1) - \cdots - P(k-1)$$

**Dice example:** $P(\text{at least four 1's}) = P(4) + P(5) + P(6)$, or equivalently $1 - P(0) - P(1) - P(2) - P(3)$.

---

## Binomial Distribution (k successes in n trials)

$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$$

This is the direct probability version of "unordered, with two outcomes."

| Part | Meaning |
|---|---|
| $\binom{n}{k}$ | Ways to choose which k trials succeed |
| $p^k$ | Probability the k chosen trials all succeed |
| $(1-p)^{n-k}$ | Probability the rest all fail |

---

## Stars and Bars

Distributing $k$ identical objects into $n$ distinct bins (bins can be empty):

$$\binom{n + k - 1}{k}$$

This is the same as "unordered with repetition." Think of $k$ stars and $n-1$ dividers.

If each bin must have **at least 1**: substitute $k' = k - n$, giving $\binom{k-1}{n-1}$.

---

## Quick Decision Tree

```
Does order matter?
├── YES → repetition allowed?
│         ├── YES → n^k
│         └── NO  → n! / (n-k)!
└── NO  → repetition allowed?
          ├── YES → C(n+k-1, k)
          └── NO  → C(n, k)

Are there groups of identical items? → Multinomial n!/(n1! n2! ...)
"At least" in the problem?          → Complement or sum exact cases
Multiple constraints?               → Inclusion-Exclusion
```

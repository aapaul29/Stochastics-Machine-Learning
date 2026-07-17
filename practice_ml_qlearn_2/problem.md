# Practice Problem: Epsilon-Greedy Action Selection

## Background

In reinforcement learning, the **$\varepsilon$-greedy** policy balances exploration
and exploitation:

- With probability $\varepsilon$: choose a **random** action (uniform over all actions)
- With probability $1 - \varepsilon$: choose the **greedy** action
  $a^* = \arg\max_a Q(s, a)$

In case of a tie in Q-values, return the **smallest index**.

## Task

Implement `epsilon_greedy(q_values, epsilon, seed)` in `solution.py`.

**Given:**
- `q_values`: list of floats — Q-values for each action in the current state
- `epsilon`: float $\in [0, 1]$ — exploration probability
- `seed`: int — random seed for reproducibility (`random.seed(seed)` before sampling)

**Return:** selected action index (int).

**Procedure:**
1. `random.seed(seed)`
2. Draw $u \sim \text{Uniform}(0, 1)$ using `random.random()`
3. If $u < \varepsilon$: draw action uniformly from $\{0, \ldots, n-1\}$ using `random.randint(0, n-1)`
4. Else: return argmax (smallest index on tie)

## Example

```python
# With epsilon=0, always greedy
epsilon_greedy([1.0, 3.0, 2.0], epsilon=0.0, seed=0)  # → 1
# With epsilon=1, always random
epsilon_greedy([1.0, 3.0, 2.0], epsilon=1.0, seed=42) # → some int in {0,1,2}
```

## Grading
- `python run.py` → public tests
- `python run.py --all` → full grading

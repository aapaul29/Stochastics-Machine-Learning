# Practice Problem: Q-Learning Bellman Update

## Background

**Q-learning** is a model-free reinforcement learning algorithm. The **Bellman
update** for the Q-value of state-action pair $(s, a)$ is:

$$Q(s, a) \leftarrow Q(s, a) + \alpha \Bigl[r + \gamma \max_{a'} Q(s', a') - Q(s, a)\Bigr]$$

where:
- $\alpha$ — learning rate
- $\gamma$ — discount factor
- $r$ — immediate reward
- $s'$ — next state
- $\max_{a'} Q(s', a')$ — best known Q-value from the next state

## Task

Implement `q_update(q_sa, reward, max_q_next, alpha, gamma)` in `solution.py`.

**Given:**
- `q_sa`: float — current $Q(s, a)$
- `reward`: float — immediate reward $r$
- `max_q_next`: float — $\max_{a'} Q(s', a')$
- `alpha`: float — learning rate $\in (0, 1]$
- `gamma`: float — discount factor $\in [0, 1]$

**Return:** updated Q-value rounded to **6 dp**.

## Example

```python
# target = 1.0 + 0.9*5.0 = 5.5,  delta = 5.5 - 0.0 = 5.5
# Q_new = 0.0 + 0.1 * 5.5 = 0.55
q_update(0.0, 1.0, 5.0, alpha=0.1, gamma=0.9)  # → 0.55
```

## Grading
- `python run.py` → public tests
- `python run.py --all` → full grading

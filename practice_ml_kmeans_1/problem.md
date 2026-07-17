# Practice Problem: k-Means Cluster Assignment

## Background

The **k-Means algorithm** alternates between two steps:

1. **Assignment:** assign each point to the nearest centroid
2. **Update:** recompute centroids as the mean of assigned points

This problem focuses on **Step 1**.

Given $k$ centroids $c_1, \ldots, c_k$, assign each data point $x_i$ to the
centroid with the smallest Euclidean distance:

$$z_i = \arg\min_{j \in \{1,\ldots,k\}} \|x_i - c_j\|$$

In case of a tie, assign to the **smallest index** (0-indexed).

## Task

Implement `assign_clusters(X, centroids)` in `solution.py`.

**Given:**
- `X`: list of $n$ data points (each a list of floats)
- `centroids`: list of $k$ centroid vectors

**Return:** list of $n$ integers (0-indexed cluster assignments).

## Example

```python
X = [[0.,0.],[1.,0.],[3.,0.],[4.,0.]]
centroids = [[0.,0.],[3.,0.]]
assign_clusters(X, centroids)   # → [0, 0, 1, 1]
```

## Grading
- `python run.py` → public tests
- `python run.py --all` → full grading

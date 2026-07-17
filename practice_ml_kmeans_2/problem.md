# Practice Problem: k-Means Centroid Update & Convergence

## Background

After assigning each point to a cluster (see previous problem), the **centroid update**
recomputes each centroid as the mean of its assigned points:

$$c_j = \frac{1}{|S_j|}\sum_{i : z_i = j} x_i$$

If a cluster is **empty**, keep its centroid unchanged.

**Convergence** is declared when every centroid moves by at most $\tau$ (tolerance):

$$\|c_j^{\text{new}} - c_j^{\text{old}}\| \leq \tau \quad \forall j$$

## Task

Implement the two functions in `solution.py`.

### `update_centroids(X, assignments, k)`
- `X`: list of $n$ data points
- `assignments`: list of $n$ ints (cluster IDs, 0-indexed)
- `k`: number of clusters
- Return new centroid list, each value rounded to **6 dp**
- If a cluster is empty, keep its centroid at `[0.0, ..., 0.0]` (same dimension as X)

### `kmeans_converged(old_centroids, new_centroids, tol)`
- `old_centroids`, `new_centroids`: lists of centroid vectors
- `tol`: float — convergence threshold
- Return `True` if all centroids moved by $\leq$ `tol`

## Example

```python
X = [[0.],[2.],[4.],[6.]]
update_centroids(X, [0,0,1,1], k=2)   # → [[1.0], [5.0]]
kmeans_converged([[1.0],[5.0]], [[1.0],[5.0]], tol=1e-4)  # → True
kmeans_converged([[1.0],[5.0]], [[1.1],[5.0]], tol=1e-4)  # → False
```

## Grading
- `python run.py` → public tests
- `python run.py --all` → full grading

# Practice Problem: k-Nearest Neighbours Classification

## Background

**k-NN classification** assigns the label of the majority class among the $k$
nearest training points (by Euclidean distance):

$$d(x, x') = \sqrt{\sum_{j=1}^d (x_j - x'_j)^2}$$

In case of a tie in distance, keep the neighbours in the order they appear in the
training set (i.e., sort by distance stably). In case of a tie in class vote,
return the **smallest label** (as an integer).

## Task

Implement the two functions in `solution.py`.

### `euclidean_distance(x1, x2)`
- `x1`, `x2`: lists of floats (same length)
- Return Euclidean distance as a float rounded to **6 dp**

### `knn_classify(X_train, y_train, x_query, k)`
- `X_train`: list of $n$ feature vectors
- `y_train`: list of $n$ integer labels
- `x_query`: list of floats — query point
- `k`: int $\geq 1$
- Return predicted class label (int)

## Example

```python
X_train = [[0.,0.],[1.,0.],[0.,1.],[1.,1.]]
y_train  = [0, 0, 1, 1]
knn_classify(X_train, y_train, [0.1, 0.1], k=3)  # → 0
knn_classify(X_train, y_train, [0.9, 0.9], k=1)  # → 1
```

## Grading
- `python run.py` → public tests
- `python run.py --all` → full grading

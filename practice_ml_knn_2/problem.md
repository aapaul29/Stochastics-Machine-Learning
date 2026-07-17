# Practice Problem: k-Nearest Neighbours Regression

## Background

**k-NN regression** predicts the **mean** target value of the $k$ nearest
training points (by Euclidean distance):

$$\hat{y}(x) = \frac{1}{k}\sum_{i \in \mathcal{N}_k(x)} y_i$$

Same distance tie-breaking as in k-NN classification: stable sort (original order for equal distances).

## Task

Implement `knn_predict(X_train, y_train, x_query, k)` in `solution.py`.

**Given:**
- `X_train`: list of $n$ feature vectors (lists of floats)
- `y_train`: list of $n$ float targets
- `x_query`: list of floats — query point
- `k`: int $\geq 1$

**Return:** mean of the $k$ nearest targets, rounded to **4 dp**.

## Example

```python
X_train = [[0.],[1.],[2.],[3.]]
y_train  = [0., 1., 2., 3.]
knn_predict(X_train, y_train, [1.5], k=2)  # → 1.5
knn_predict(X_train, y_train, [0.0], k=3)  # → 1.0
```

## Grading
- `python run.py` → public tests
- `python run.py --all` → full grading

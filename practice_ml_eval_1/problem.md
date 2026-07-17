# Practice Problem: k-Fold Cross-Validation

## Background

**k-fold cross-validation** splits $n$ samples into $k$ non-overlapping folds of
(approximately) equal size. In each fold $i$, fold $i$ is the **validation set**
and the remaining folds form the **training set**.

For $n = 10$, $k = 3$: fold sizes are $[4, 3, 3]$ (the first $n \mod k$ folds get
one extra sample). Indices are assigned sequentially:
- Fold 0: indices $0, 1, 2, 3$
- Fold 1: indices $4, 5, 6$
- Fold 2: indices $7, 8, 9$

## Task

Implement `kfold_indices(n, k)` in `solution.py`.

**Given:**
- `n`: int — total number of samples
- `k`: int — number of folds ($1 \leq k \leq n$)

**Return:** list of `k` tuples `(train_indices, val_indices)`, where each is a
sorted list of ints.

## Example

```python
kfold_indices(6, 3)
# → [([2,3,4,5], [0,1]),
#    ([0,1,4,5], [2,3]),
#    ([0,1,2,3], [4,5])]
```

## Grading
- `python run.py` → public tests
- `python run.py --all` → full grading

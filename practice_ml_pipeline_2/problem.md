# Practice Problem: SVC Hyperparameter Search

## Background

Support Vector Classifiers (SVCs) are sensitive to hyperparameters. **GridSearchCV**
automates the search:

```python
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV

param_grid = {"C": [...], "kernel": [...]}
gs = GridSearchCV(SVC(), param_grid, cv=5, scoring="accuracy")
gs.fit(X_train, y_train)
best_model = gs.best_estimator_
```

## Task

Implement `find_best_svc(X_train, y_train)` in `solution.py`.

**Given:**
- `X_train`: 2D list or numpy array of features
- `y_train`: list or array of integer class labels

**Return:** a **fitted** SVC (the best estimator from GridSearchCV) that achieves
**accuracy ≥ 0.70** on the hidden test set.

Your `param_grid` must search at least:
- `C`: values in $\{0.1, 1, 10\}$
- `kernel`: `"linear"` and `"rbf"`

You may add more values or parameters.

## Grading
- `python run.py` → public tests (structural checks)
- `python run.py --all` → full grading (accuracy threshold)

# Practice Problem: Binary Classification Metrics

## Background

Given binary labels (0 = negative, 1 = positive), define:

| | Predicted 1 | Predicted 0 |
|---|---|---|
| **True 1** | TP | FN |
| **True 0** | FP | TN |

$$\text{Accuracy}  = \frac{TP + TN}{n}$$
$$\text{Precision} = \frac{TP}{TP + FP} \quad (\text{return } 0.0 \text{ if denominator is } 0)$$
$$\text{Recall}    = \frac{TP}{TP + FN} \quad (\text{return } 0.0 \text{ if denominator is } 0)$$
$$F_1 = \frac{2 \cdot \text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}} \quad (\text{return } 0.0 \text{ if denominator is } 0)$$

## Task

Implement the four functions in `solution.py`. Each returns a float rounded to **4 dp**.

```python
accuracy(y_true, y_pred)
precision(y_true, y_pred)
recall(y_true, y_pred)
f1_score(y_true, y_pred)
```

## Example

```python
y_true = [1, 0, 1, 1, 0, 1]
y_pred = [1, 0, 1, 0, 1, 1]
# TP=3, TN=1, FP=1, FN=1
accuracy(y_true, y_pred)   # → 0.6667
precision(y_true, y_pred)  # → 0.75
recall(y_true, y_pred)     # → 0.75
f1_score(y_true, y_pred)   # → 0.75
```

## Grading
- `python run.py` → public tests
- `python run.py --all` → full grading

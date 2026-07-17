# Regression

Modify the file `train.py` so that a model trained on this data performs well when evaluated on a separate hidden test set of 100 points. This separate hidden test set is not visible to you.

You may assume that all points in the test dataset and most of the points in `data.csv` are sampled from the same distribution.

**Scoring:** The amount of points you get in this question depends on the R2 score you attain on the hidden test data. This amount is computed with a linear interpolation between (0.79, 0) and (0.85, 6). This means that to get 6 points in this task you must get an R2 score of at least 0.85. To get any amount of points you must get an R2 score above 0.79.

**Hints**

- Take a moment to look at the dataset before you start working on the task.
- A simple linear regression model suffices to get all the points.
- The code below shows how you can select points in the data whose *y* value is at most 5 and whose *y* value is above 0.

```python
valid_mask = (train_df["y"] <= 5) & (train_df["X0"] > 0)

train_X = train_X[valid_mask]
train_y = train_y[valid_mask]
```

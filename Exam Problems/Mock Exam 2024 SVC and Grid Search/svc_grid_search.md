# Support-vector classifiers and grid search

The file `main.py` trains a *support vector classifier* on the data in `data.csv`. A support vector classifier is similar to a support vector regressor, but it is used when you want to classify points in different classes.

Unfortunately, the accuracy of this classifier in a separate hidden test set is 0.258. Use grid search to find the best hyperparameters and increase the accuracy in this hidden test.

**Remarks:**

- Make sure that your code is reproducible by using `SVC(random_state=0)`.
- The file `reference.md` contains the documentation for the `SVC` class and the `GridSearch` class.

**Scoring:** The amount of points you get in this question depends on the accuracy you attain on the hidden test set. This amount is computed with a linear interpolation between (0.26, 0) and (0.42, 7).

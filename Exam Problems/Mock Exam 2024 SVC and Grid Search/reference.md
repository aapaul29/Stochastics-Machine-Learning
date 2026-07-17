### SVC Reference
#### SVC
>class sklearn.svm.SVC(*, C=1.0, kernel='rbf', degree=3, gamma='scale', coef0=0.0, shrinking=True, probability=False, tol=0.001, cache_size=200, class_weight=None, verbose=False, max_iter=-1, decision_function_shape='ovr', break_ties=False, random_state=None)

**Parameters:**
- **C**: `float`. Regularization parameter. **The strength of the regularization is inversely proportional to C. Must be strictly positive.**
- **kernel**: `‘linear’`, `‘poly’`, `‘rbf’`, `‘sigmoid’`, `‘precomputed’` or callable*. The kernel type to be used in the algorithm.
- **degree**: `int`. Degree of the polynomial kernel function (‘poly’). Must be non-negative. Ignored by all other kernels.
- **gamma**: `‘scale’`, `‘auto’`, or `float`. Kernel coefficient for ‘rbf’, ‘poly’ and ‘sigmoid’.
  - if `gamma='scale'` (default) is passed then it uses 1 / (n_features * X.var()) as value of gamma,
  - if `‘auto’`, uses 1 / n_features,
  - if `float`, must be non-negative.

#### GridSearchCV
> class sklearn.model_selection.GridSearchCV(estimator, param_grid, *, scoring=None, n_jobs=None, refit=True, cv=None, verbose=0, pre_dispatch='2*n_jobs', error_score=nan, return_train_score=False)

**Parameters:**
- **estimator**: `estimator object`, e.g., SVC().
- **param_grid**: `dict` or `list` of `dictionaries`, Dictionary with parameters names (`str`) as keys and lists of parameter settings to try as values, or a list of such dictionaries, in which case the grids spanned by each dictionary in the list are explored. This enables searching over any sequence of parameter settings.
- **scoring**: `str`, `callable`, `list`, `tuple` or `dict`, default=`None`. Strategy to evaluate the performance of the cross-validated model on the test set.
  - string options: 'accuracy', 'f1', 'precision', etc.
- **refit**: `bool`, `string`, or `callable`. Refit an estimator using the best found parameters on the whole dataset.
- **cv**: *`int`, `cross-validation generator` or an `iterable`. Determines the cross-validation splitting strategy. If `None`, use the default 5-fold cross validation.

**Attributes:**
- **cv_results_**: a `dict` of grid search results. Use `cv_results_['mean_test_score']` and `cv_results_['params']` to obtain the performance of each hyperparameter set.
- **best_params_**: a `dict` of the Parameter setting that gave the best results on the hold out data.
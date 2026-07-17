# Practice Problem: sklearn Regression Pipeline

## Background

Real-world datasets have missing values and features on different scales.
A standard **sklearn Pipeline** chains preprocessing and modelling steps:

```
Imputer → Scaler → Regressor
```

This ensures the scaler's statistics are computed only on training data and
automatically applied at test time.

## Task

Implement `build_pipeline()` in `solution.py`. The function must return an
**unfitted** sklearn `Pipeline` that:

1. Imputes missing values (`SimpleImputer`, strategy = `"mean"`)
2. Standardizes features (`StandardScaler`)
3. Fits a linear regression model (`LinearRegression`)

The pipeline will be evaluated on a held-out dataset. It must achieve **R² ≥ 0.80**
on the hidden test set.

```python
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

def build_pipeline() -> Pipeline:
    ...
```

## Grading
- `python run.py` → public tests (structural checks)
- `python run.py --all` → full grading (R² threshold)

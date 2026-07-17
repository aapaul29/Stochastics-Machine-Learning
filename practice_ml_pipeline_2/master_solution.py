from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
import numpy as np

def find_best_svc(X_train, y_train) -> SVC:
    """GridSearchCV over SVC hyperparameters."""
    param_grid = {
        "C": [0.1, 1, 10, 100],
        "kernel": ["linear", "rbf"],
        "gamma": ["scale", "auto"],
    }
    gs = GridSearchCV(SVC(), param_grid, cv=5, scoring="accuracy", n_jobs=-1)
    gs.fit(X_train, y_train)
    return gs.best_estimator_

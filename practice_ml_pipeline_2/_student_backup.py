from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV

def find_best_svc(X_train, y_train) -> SVC:
    """Run GridSearchCV over SVC hyperparameters and return the best fitted estimator."""
    # TODO
    svc = SVC()
    svc.fit(X_train, y_train)
    return svc

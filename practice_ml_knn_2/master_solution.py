import math

def knn_predict(X_train: list[list[float]], y_train: list[float],
                x_query: list[float], k: int) -> float:
    """k-NN regression."""
    def dist(x):
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(x, x_query)))
    distances = sorted(enumerate(X_train), key=lambda iv: dist(iv[1]))
    k_vals = [y_train[i] for i, _ in distances[:k]]
    return round(sum(k_vals) / k, 4)

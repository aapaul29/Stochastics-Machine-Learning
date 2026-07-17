import math

def update_centroids(X: list[list[float]], assignments: list[int],
                     k: int) -> list[list[float]]:
    """Recompute centroids as mean of assigned points.
    Empty clusters → centroid of all zeros. Values rounded to 6 dp."""
    # TODO
    return []

def kmeans_converged(old_centroids: list[list[float]],
                     new_centroids: list[list[float]], tol: float) -> bool:
    """True if every centroid moved by at most tol (Euclidean distance)."""
    # TODO
    return False

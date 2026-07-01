def empirical_joint(samples: list[tuple[int,int]], x_val: int, y_val: int) -> float:
    """Return P_hat(X=x_val, Y=y_val), rounded to 4 dp."""
    # TODO
    return -1.0

def empirical_marginal_x(samples: list[tuple[int,int]], x_val: int) -> float:
    """Return P_hat(X=x_val), rounded to 4 dp."""
    # TODO
    return -1.0

def empirical_marginal_y(samples: list[tuple[int,int]], y_val: int) -> float:
    """Return P_hat(Y=y_val), rounded to 4 dp."""
    # TODO
    return -1.0

def are_independent(samples: list[tuple[int,int]], x_vals: list[int], y_vals: list[int], eps: float) -> bool:
    """Return True if |P_hat(X,Y) - P_hat(X)*P_hat(Y)| < eps for all (x,y) in x_vals x y_vals."""
    # TODO
    return False

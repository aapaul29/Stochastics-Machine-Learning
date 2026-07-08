def empirical_joint(samples: list[tuple[int, int]], x_val: int, y_val: int) -> float:
    """Return P_hat(X=x_val, Y=y_val), rounded to 4 dp."""
    return round(sum(1 for x, y in samples if x == x_val and y == y_val) / len(samples), 4)


def empirical_marginal_x(samples: list[tuple[int, int]], x_val: int) -> float:
    """Return P_hat(X=x_val), rounded to 4 dp."""
    return round(sum(1 for x, _ in samples if x == x_val) / len(samples), 4)


def empirical_marginal_y(samples: list[tuple[int, int]], y_val: int) -> float:
    """Return P_hat(Y=y_val), rounded to 4 dp."""
    return round(sum(1 for _, y in samples if y == y_val) / len(samples), 4)


def are_independent(samples: list[tuple[int, int]],
                    x_vals: list[int], y_vals: list[int], eps: float) -> bool:
    """Return True if |P_hat(X=x,Y=y) - P_hat(X=x)*P_hat(Y=y)| < eps for all (x,y)."""
    for xv in x_vals:
        for yv in y_vals:
            joint = empirical_joint(samples, xv, yv)
            product = empirical_marginal_x(samples, xv) * empirical_marginal_y(samples, yv)
            if abs(joint - product) >= eps:
                return False
    return True

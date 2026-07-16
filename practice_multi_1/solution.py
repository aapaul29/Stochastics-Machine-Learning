def empirical_joint(samples: list[tuple[int,int]], x_val: int, y_val: int) -> float:
    """Return P_hat(X=x_val, Y=y_val), rounded to 4 dp."""
    # TODO
    count = 0
    for t in samples:
        if t[0] == x_val and t[1] == y_val:
            count += 1
    joint_prob = count / len(samples)
    return round(joint_prob, 4)

def empirical_marginal_x(samples: list[tuple[int,int]], x_val: int) -> float:
    """Return P_hat(X=x_val), rounded to 4 dp."""
    # TODO
    count = 0
    for t in samples:
        if t[0] == x_val:
            count += 1
    empiricial_marginal_x = count / len(samples)
    return round(empiricial_marginal_x, 4)

def empirical_marginal_y(samples: list[tuple[int,int]], y_val: int) -> float:
    """Return P_hat(Y=y_val), rounded to 4 dp."""
    # TODO
    count = 0
    for t in samples:
        if t[1] == y_val:
            count += 1
    empirical_marginal_y = count / len(samples)
    return round(empirical_marginal_y, 4)
    

def are_independent(samples: list[tuple[int,int]], x_vals: list[int], y_vals: list[int], eps: float) -> bool:
    """Return True if |P_hat(X,Y) - P_hat(X)*P_hat(Y)| < eps for all (x,y) in x_vals x y_vals."""
    # TODO
    empirical_joint_list = []
    marginal_x_list = []
    marginal_y_list = []
    for i in range(len(x_vals)):
        for j in range(len(y_vals)):
            empirical_joint_list.append(empirical_joint(samples, x_vals[i], y_vals[j]))
    for x in x_vals:
        marginal_x_list.append(empirical_marginal_x(samples, x))
    for y in y_vals:
        marginal_y_list.append(empirical_marginal_y(samples, y))
    for i in range(len(marginal_x_list)):
        if abs(empirical_joint_list[i] - marginal_x_list[i] * marginal_y_list[i]) >  eps:
            return False
        
    return True

def running_average(samples: list[float]) -> list[float]:
    """Return list of running averages, each rounded to 4 dp."""
    # TODO
    running_average = []
    for i in range(len(samples)):
        avg = sum(samples[:i + 1]) / (i + 1)
        running_average.append(round(avg, 4))
    return running_average

def lln_converges(samples: list[float], true_mean: float, eps: float) -> bool:
    """Return True if |final_running_average - true_mean| < eps."""
    # TODO
    avg_list = running_average(samples)
    return abs(avg_list[-1] - true_mean) < eps

def convergence_index(samples: list[float], true_mean: float, eps: float) -> int:
    """Return smallest n (1-indexed) from which all running averages stay within eps of true_mean.
    Return len(samples) if no such n exists."""
    # TODO
    avg_list = running_average(samples)
    n = len(avg_list)
    for i in range(n - 1, -1, -1):
        if abs(avg_list[i] - true_mean) >= eps:
            if i + 1 < n:
                return i + 2
            else:
                return n
    return 1
            

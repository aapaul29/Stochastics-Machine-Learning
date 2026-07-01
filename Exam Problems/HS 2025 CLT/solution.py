import scipy

import numpy as np
from scipy.stats import norm, entropy

def student_compute_sample_means(data: np.ndarray, N: int) -> np.ndarray:
    #-----STUDENT SOLUTION START--------#
    """
    Simulates the Central Limit Theorem.

    Parameters:
        data (np.ndarray): A 1D NumPy array of i.i.d. samples from a given 
                           distribution.
        N (int): The number of data points used to compute each sample mean.

    Returns:
        np.ndarray: A NumPy array of normalized sample means that, for large N, 
                    approximate a standard normal distribution.
    """
    # means = [np.mean(data[i:i+N]) for i in range(0, len(data), N) if len(data[i:i+N]) == N]
    n = len(data)
    means = [np.mean(data[i*N:(i+1)*N]) for i in range(n//N)]

    # Theoretical mean and standard deviation for Exp(1)
    mu = data.mean()  #1  # Mean of empirical distribution
    sigma = data.std()  #1  # Standard deviation of empirical distribution
    # Normalize the sample means
    normalized_means = (np.array(means) - mu) / (sigma /  np.sqrt(N))

    return normalized_means
    #-----STUDENT SOLUTION END--------#

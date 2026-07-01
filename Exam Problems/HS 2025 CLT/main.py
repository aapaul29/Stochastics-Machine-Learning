import sys
import os
import solution
import scipy
import numpy as np
from scipy.stats import norm, entropy

def generate_fixed_data(distribution, size=100000, seed=42):
    np.random.seed(seed)
    if distribution == "exponential":
        return np.random.exponential(scale=1, size=size)
    elif distribution == "uniform":
        return np.random.uniform(low=0.0, high=1.0, size=size)
    elif distribution == "poisson":
        return np.random.poisson(3, size)
    elif distribution == "normal":
        return np.random.normal(0, 1, size)
    else:
        raise ValueError(f"Unsupported distribution: {distribution}")

def measure_similarity(sample_means, bins=10):
    hist, bin_edges = np.histogram(sample_means, bins=bins, density=True)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
    normal_pdf = norm.pdf(bin_centers, 0, 1)  # Standard normal with mean 0 and std 1

    hist += 1e-10  # Avoid log(0) in KL computation
    normal_pdf += 1e-10
    kl_divergence = entropy(hist, normal_pdf)

    return kl_divergence

def is_interactive():
  return os.environ['ACTION'] in("run", "debug")

def main():
  # Only display extra instructions if running in an interactive terminal
  # my_input = input('Enter <dist> <a> <b> <n> <low> <high>: \n').split()
  my_input = input('Enter <dist> <N>: \n').split()
  distr = my_input[0]
  N = int(my_input[1])
  samples = generate_fixed_data(distr,seed=42, size=N*100000)
  
  if is_interactive():
    normalized_means = solution.student_compute_sample_means(samples, N)
    kl = measure_similarity(normalized_means, bins=20)
    print (f"KL divergence: {kl:.4f}")
  else:
    value = float(my_input[2])
    delta = float(my_input[3])
    normalized_means = solution.student_compute_sample_means(samples, N)
    kl = measure_similarity(normalized_means, bins=20)
    print("Expected result in [",value-delta,",",value+delta,f"], got {kl}")
    if value - delta <= kl <= value + delta:
      print("within bounds, ok.")

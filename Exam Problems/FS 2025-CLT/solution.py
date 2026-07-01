import scipy

# simulation is not necessary and only serves to roughly confirm the values 
simulate = False 

# -- only for testing --
def empirical_mean(data):
  return sum(data)/len(data)
  
def empirical_variance(data):
  v = data-empirical_mean(data)
  return sum([i*i for i in v])/(len(v)-1)
  
def simulate_mean(distribution,n):
  values = [sum(distribution.rvs(n)) for i in range(10000)]
  return empirical_mean(values)

def simulate_var(distribution,n):
  values = [sum(distribution.rvs(n)) for i in range(10000)]
  return empirical_variance(values)
  
def simulate_probability(distribution,n,left,right):
  values = [sum(distribution.rvs(n)) for i in range(10000)]
  return sum([left <= i <= right for i in values])/len(values)

# return the mean of a sum of n iid random variables
# with given distribution (from scipy.stats)
def mean(distribution: scipy.stats.rv_continuous, n:int):
  if simulate:
    print("mean",distribution.mean())
    print("simulated mean",simulate_mean(distribution,n))
  return distribution.mean()*n

# return the variance of a sum of n iid random variables
# with given distribution (from scipy.stats)
def variance(distribution: scipy.stats.rv_continuous, n:int):
  if simulate:
    print("variance",distribution.var())
    print("simulated variance",simulate_var(distribution,n))
  return distribution.var()*n

# return an approximation of the probability of 
# the sum of n iid random variables each having distribution
# to have values in interval [a,b]
def approximate(distribution: scipy.stats.rv_continuous ,n:int ,a: float, b:float):
  if simulate:
    print("simulated probability",simulate_probability(distribution,n,a,b))
  normal = scipy.stats.norm(distribution.mean()*n,(distribution.var()*n)**0.5)
  return normal.cdf(b)-normal.cdf(a)
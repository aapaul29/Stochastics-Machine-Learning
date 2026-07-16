# Estimating Zeros

The file `main.py` consists of a loop where, at each iteration, a function
`noisy_sin` of the form

$$f(x) = \sin(x - \theta) + \epsilon$$

is generated. The value of $\theta$ is unknown to you and randomly sampled
according to a uniform distribution over $[-5, 5]$. Also, $\epsilon$ is a
random variable with distribution $\mathcal{N}(0, 0.1)$.

## Your Task

Implement the function `estimator` in the file `solution.py`. It takes as
argument a function `noisy_sin`, as described above. The function shall
return an estimate of $\theta$ for this function.

We only show you the actual values of $\theta$ for the first 5 iterations.

## Scoring

The file `main.py` produces 10 functions `noisy_fin`, each with a
different value of $\theta$. It then produces an estimate $\hat{\theta}$
of $\theta$, using your implementation of `estimator`. A penalty is
computed by

$$\left|\sin(\hat{\theta} - \theta)\right|$$

Then the average of these penalties is computed. The amount of points
awarded for this task is a linear interpolation between the following
baselines:

| Average Penalty | Points Awarded |
|------------------|---------------:|
| 0.7              | 0              |
| 0.0              | 6              |

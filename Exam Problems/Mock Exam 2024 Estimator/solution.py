
def estimator(noisy_fun):
  
  estimate = -5
  min_guess = abs(noisy_fun(estimate))
  best_estimate = estimate
  while estimate <= 5:
    estimate += 0.0001
    guess = noisy_fun(estimate)
    if guess < min_guess:
      best_estimate = estimate
    
    return best_estimate
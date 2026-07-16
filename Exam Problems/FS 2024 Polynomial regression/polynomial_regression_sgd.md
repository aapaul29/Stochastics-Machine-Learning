# Polynomial regression with stochastic gradient descent

In this task, you must complete an implementation that fits polynomials to data.

The function `stochastic_gradient_descent` in the file `sgd.py` implements the algorithm *stochastic gradient descent (SGD)* for fitting polynomials. The function takes as input the following:

- A natural number n.
- Two lists of floats X and Y of the same length m.

For i < m, X[i] is a real number between -10 and 10 and Y[i] is the result of f(X[i]) plus some random noise, where f is a polynomial of degree n, unknown to you.

SGD then tries to estimate the coefficients of the polynomial as follows.

First, it stores the coefficient estimates in a list w of length n + 1, with all values initially set to 0.

Second, SGD runs a loop. At each iteration, SGD goes through each point x and y in X and Y, respectively. It then uses the information of each point x, y to update the estimates for the coefficients.

## Task

Your task is to implement the function `update(w, x, y)`, which updates the coefficients, stored in w, using the information from (x, y). We now explain how to do this.

Let w = (w₀, w₁, ..., wₙ) be the current estimates for the coefficients. For i ≤ n, you should update wᵢ as follows:

$$w_i \leftarrow w_i - \alpha \frac{\partial}{\partial w_i} \ell(w, x, y),$$

where α > 0 is an adequate learning rate (which you must define) and

$$\ell(w, x, y) = (w_0 + w_1 x + w_2 x^2 + ... + w_n x^n - y)^2.$$

*Hint: If you follow the formula above to update the estimates, then we recommend using α = 0.000005.*

## Evaluation

Your implementation is used to try to fit 8 polynomials with degrees 2, 2, 3, 3, 4, 4, 5, and 5, respectively. The data used to fit each polynomial is in the .csv files given to you. After fitting each polynomial, CodeExpert computes the R2 Score of this polynomial on a separate test dataset, which is hidden from you. The amount of points awarded is a linear interpolation between (0.8, 0) and (0.98, 7). That is, to get the maximum number of points (7 points), your R2 score should be at least 0.98.

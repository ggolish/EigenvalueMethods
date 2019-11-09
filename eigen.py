
import numpy as np
import utils

# Computes the largest magnitude eigenvalue of A via the power method, within
# a tolerance of delta
def power_method(A, delta=0.0001):
    utils.validate_matrix(A)
    x = np.zeros(A.shape[0])
    x[0] = 1.0
    pn = float("inf")
    while True:
        p = A @ x
        n = np.max(np.abs(p))
        x = (1.0 / n) * p
        if abs(n - pn) < delta:
            break
        pn = n
    return (n, x)

if __name__ == "__main__":
    A = np.array([[7, 9], [9, 7]])
    l, v = power_method(A)
    print(l, v)


import numpy as np
import utils
import sys

# Computes the largest magnitude eigenvalue of A via the power method, within
# a tolerance of delta or for iterations iterations
def power_method(A):
    utils.validate_matrix(A)
    x = np.zeros(A.shape[0])
    x[0] = 1.0
    while True:
        p = A @ x
        n = np.max(np.abs(p))
        x = (1.0 / n) * p
        yield n

def jacobi_method(A, delta=0.0001):
    return (0, np.array())

def read_matrix(fd):
    x = [list(map(float, l.split())) for l in fd.readlines() if l.strip()]
    return np.array(x)

def main(args):
    A = read_matrix(sys.stdin)
    method = jacobi_method if args.jacobi else power_method
    prev_eigenval = float("inf")
    for eigenval in method(A):
        if abs(eigenval - prev_eigenval) < 0.00001:
            break
        prev_eigenval = eigenval
    print("{:0.4f}".format(eigenval))

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
            prog="Eigenvalue Approximator", 
            description="Numerically approximates the eigenvalues of an input matrix",
            usage=f"{sys.argv[0]} [--power | --jacobi]"
    )

    parser.add_argument("--power", action="store_true", help="Use the power method [default]")
    parser.add_argument("--jacobi", action="store_true", help="Use the jacobi method")
    args = parser.parse_args(sys.argv[1:])

    main(args)


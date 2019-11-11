
import numpy as np
import utils
import sys

# Computes the largest magnitude eigenvalue of A via the power method, within
# a tolerance of delta or for iterations iterations
def power_method(A):
    x = np.zeros(A.shape[0])
    x[0] = 1.0
    while True:
        p = A @ x
        n = np.max(np.abs(p))
        x = (1.0 / n) * p
        yield n

def jacobi_method(A):
    norm = utils.outer_norm(A)
    while True:
        i, j = utils.outer_argmax(A)
        theta = 0.5 * (A[i, i] - A[j, j]) / A[i, j]
        t = 1 / (np.abs(theta) + np.sqrt(1 + theta**theta))
        c = 1 / np.sqrt(1 + t**t)
        s = c * t
        print(theta, t, c, s)
        bi = np.zeros(A.shape[0])
        bj = np.zeros(A.shape[0])
        bi[i] = A[i, i] - t * A[i, j]
        bj[j] = A[j, j] + t * A[i, j]
        for l in range(A.shape[0]):
            if l != i and l != j:
                bi[l] = c * A[i, l] + s * A[j, l]
                bj[l] = -s * A[i, l] + c * A[j, l]
        print(bi, bj)
        norm = norm - 2 * A[i, j]**2
        print(norm)
        for l in range(A.shape[0]):
            A[i, l] = A[l, i] = bi[l]
            A[j, l] = A[l, j] = bj[l]
        yield norm

def read_matrix(fd):
    x = [list(map(float, l.split())) for l in fd.readlines() if l.strip()]
    return np.array(x)

def main(args):
    A = read_matrix(sys.stdin)
    utils.validate_matrix(A)
    prev_eigenval = float("inf")
    if args.jacobi:
        for norm in jacobi_method(A):
            print(norm, A)
            break
    else:
        for eigenval in power_method(A):
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


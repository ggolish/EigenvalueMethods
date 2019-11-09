
import numpy as np
import utils
import sys

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

def jacobi_method(A, delta=0.0001):
    return (0, np.array())

def read_matrix(fd):
    x = [list(map(float, l.split())) for l in fd.readlines() if l.strip()]
    return np.array(x)

def main(args):
    infd = sys.stdin
    outfd = sys.stdout

    if args.f:
        try:
            infd = open(args.f, "r")
        except:
            utils.die(f"Unable to open {args.f} for reading")

    if args.o:
        try:
            outfd = open(args.o, "w")
        except:
            utils.die(f"Unable to open {args.o} for writing")

    A = read_matrix(infd)
    infd.close()

    if args.jacobi:
        n, v = jacobi_method(A)
    else:
        n, v = power_method(A)

    outfd.write(f"lambda = {repr(n)}\n")
    outfd.write(f"v = {repr(v.tolist())}\n")
    outfd.close()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
            prog="Eigenvalue Approximator", 
            description="Numerically approximates the eigenvalues of an input matrix",
            usage=f"{sys.argv[0]} [--power | --jacobi] [-f <path-to-file>] [-o <output-path>]"
    )

    parser.add_argument("--power", action="store_true", help="Use the power method [default]")
    parser.add_argument("--jacobi", action="store_true", help="Use the jacobi method")
    parser.add_argument("-f", type=str, help="Read input matrix from file")
    parser.add_argument("-o", type=str, help="Dump output into file")
    args = parser.parse_args(sys.argv[1:])

    main(args)


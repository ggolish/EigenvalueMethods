
import eigen
import utils
import numpy as np
import matplotlib.pyplot as plt
import os

def load_test(number):
    path = os.path.join("data", "test{:02d}".format(number))
    with open(path, "r") as fd:
        return eigen.read_matrix(fd)

def write_test(number, A):
    path = os.path.join("data", "test{:02d}".format(number))
    with open(path, "w") as fd:
        for i in range(A.shape[0]):
            for j in range(A.shape[1]):
                fd.write("{:0.4f}\t".format(A[i, j]))
            fd.write("\n")

def plot_testcase(number, power_data, jacobi_data):
    title = "Test Case {:02d}".format(number)
    plt.subplot(2, 1, 1)
    plt.plot(power_data)
    plt.ylabel("Largest Eigenvalue Approximation")
    plt.xlabel("Iterations")
    plt.title(f"Power Method: {title}")
    plt.subplot(2, 1, 2)
    plt.plot(jacobi_data)
    plt.ylabel("Outer Norm N(A)")
    plt.xlabel("Iterations")
    plt.title(f"Jacobi Method: {title}")
    plt.show()

def run_power(A, threshold=0.0001):
    data = []
    prev = float("inf")
    for approx in eigen.power_method(A):
        data.append(approx)
        if abs(approx - prev) < threshold:
            break
        prev = approx
    return data

def run_jacobi(A, threshold=0.0001):
    data = []
    for norm in eigen.jacobi_method(A):
        data.append(norm)
        if norm < threshold:
            break
    return data

def main(args):
    A = load_test(args.number)
    power_data = run_power(A, threshold=args.threshold)
    jacobi_data = run_jacobi(A, threshold=args.threshold)
    plot_testcase(args.number, power_data, jacobi_data)

def generate_testcase(number):
    A = np.random.rand(10, 10) * 10
    A += A.T
    write_test(number, A)

if __name__ == "__main__":
    import argparse
    import sys

    parser = argparse.ArgumentParser(
            prog="Eigen Tests",
            description="Run test cases for eigen module",
            usage=f"{sys.argv[0]} <test-number>"
    )

    parser.add_argument("number", type=int, help="The test case number")
    parser.add_argument("-t", "--threshold", type=float, default=0.0001,
            help="The threshold value for both Jacobi and power method")
    parser.add_argument("-g", "--generate", action="store_true",
            help="Generate a new test case.")

    args = parser.parse_args(sys.argv[1:])

    if args.generate:
        generate_testcase(args.number)
    else:
        main(args)


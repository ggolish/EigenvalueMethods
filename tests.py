
import eigen
import utils
import numpy as np
import matplotlib.pyplot as plt
import os

def load_test(number):
    path = os.path.join("data", "test{:02d}".format(number))
    with open(path, "r") as fd:
        return eigen.read_matrix(fd)

def plot_testcase(number, power_data):
    title = "Test Case {:02d}".format(number)
    plt.plot(power_data)
    plt.ylabel("Largest Eigenvalue")
    plt.xlabel("Iteration")
    plt.title(f"Power Method: {title}")
    plt.show()

def main(args):
    A = load_test(args.number)
    iterations = args.iterations if args.iterations != None else 100
    eigenval, eigenvec, power_data = eigen.power_method(A, iterations=iterations)
    plot_testcase(args.number, power_data)

if __name__ == "__main__":
    import argparse
    import sys

    parser = argparse.ArgumentParser(
            prog="Eigen Tests",
            description="Run test cases for eigen module",
            usage=f"{sys.argv[0]} <test-number>"
    )

    parser.add_argument("number", type=int, help="The test case number")
    parser.add_argument("-i", "--iterations", type=int, help="Number of iterations to run [default 1000]")

    args = parser.parse_args(sys.argv[1:])

    main(args)


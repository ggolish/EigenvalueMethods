
import eigen
import utils
import numpy as np
import matplotlib.pyplot as plt
import os

def load_test(number):
    path = os.path.join("data", "test{:02d}".format(number))
    return eigen.read_matrix(path)

def main(args):
    pass

if __name__ == "__main__":
    import argparse
    import sys

    parser = argparse.ArgumentParser(
            prog="Eigen Tests",
            description="Run test cases for eigen module",
            usage=f"{sys.argv[0]} <test-number>"
    )

    parser.add_argument("number", type=int, help="The test case number")
    args = parser.parse_args(sys.argv[1:])

    main(args)


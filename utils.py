
import sys
import numpy as np

# Ensures A is a valid 2D matrix, and optionally square / symmetric
def validate_matrix(A, square=True, symmetric=True):
    if len(A.shape) != 2:
        die(f"Matrix does not have two dimensions {A.shape}")
    if square and A.shape[0] != A.shape[1]:
        die(f"Matrix is not square {A.shape}")
    if symmetric and np.any(A != A.T):
        die("Matrix is not symmetric")

def die(error_msg, exit_code=1):
    sys.stderr.write(f"Error: {error_msg}!\n")
    sys.exit(exit_code)

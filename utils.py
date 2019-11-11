
import sys
import numpy as np

# Computes the outer norm of a matrix A, the sum of the squares of the 
# nondiagonal entries
def outer_norm(A):
    lt = np.tril_indices(A.shape[0], -1)
    ut = np.triu_indices(A.shape[0], 1)
    return np.sum(np.square(A[lt])) + np.sum(np.square(A[ut]))

# Returns the index of the largest entry of A, not including 
# diagonal entries
def outer_argmax(A):
    B = np.abs(A.copy())
    B[np.diag_indices(B.shape[0])] = 0
    return np.unravel_index(B.argmax(), B.shape)

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

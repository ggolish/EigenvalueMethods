

# Comparison of Numerical Eigenvalue Approximation Methods


## Power Method

The power method is an iterative method used to find the largest in
magnitude eigenvalue of a linear system and it's corresponding
eigenvector. Each iterative step takes O(N<sup>2</sup>) time.


## Jacobi Method

The Jacobi method is an iterative method that can be used to find
all eigenvalues and corresponding eigenvecotrs of a Hermitian
matrix. It is based on the fact that orthogonal transformations
on such a matrix do not change its eigenvalues, and hence these
transformations can be iteratvely made in order to transform the
matrix into a diagonal matrix in which the diagonal entries are the
eigenvalues. The run time of a single iteration is O(N<sup>2</sup>).


## Usage

There are two main programs in this project, `eigen.py` and
`tests.py`. The former program contains the code for each iterative
method listed above, and the latter contains the code to run the
methods in the test cases found in the `data` directory, and
visualizes the iterations. `eigen.py` can also be run on an
individual matrix read from standard input. 

-   `eigen.py`:
    
        python3 eigen.py [-h] [--jacobi]
    
    -   -h => print usage information
    -   &#x2013;jacobi => use the Jacobi method (power method is the default)
-   `tests.py`:
    
        python3 tests.py [-t <threshold>] [-g] [-h] <test-number>
    
    -   -h => print usage information
    -   -t <threshold> => the threshold for convergence of both
        algorithms (default 0.0001)
    -   -g => generate a new test case and print to stdout
    -   test-number => the number of the test case in the data
        directory


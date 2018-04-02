import sys
sys.path.append('../src')
import matrix_solver as ms
import numpy as np


def test_solver_a():
    A = np.array([[1, 1], [-1, 1]])
    b = np.array([[1], [1]])
    assert (ms.solve_matrix(A, b) == np.array([[0], [1]])).all()

def test_solver_b():
    A = np.array([[1, -2, -2], [-2, 1, -2], [-2, -2, 1]])
    b = np.array([[9], [3], [-3]])
    assert (ms.solve_matrix(A, b) == np.array([[1.], [-1.], [-3.]])).all()


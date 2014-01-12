"""
Routines to solve problems in Docs/source/rational_exp/ratexp1.rst

@author : Spencer Lyon
@author : Chase Coleman
@date : 2014-01-11 15:07:13

"""
import numpy as np
from pyTM.util.lq import olrp


def ex1():
    'Solve exercise 1 from rational expectations module'
    A_0 = 100
    A_1 = 0.05
    beta = 0.95
    d = 10.0
    H_0 = 95.5
    H_1 = 0.95

    A = np.array([[1, 0, 0], [0, H_1, H_0], [0, 0, 1]])
    B = np.array([1, 0, 0])
    R = np.array([[0, -A_1/2, A_0/2], [-A_1/2, 0, 0], [A_0/2, 0, 0]])
    Q = -0.5*d

    F, P = olrp(beta, A, B, R, Q)

    return F

F_1 = ex1()


def ex2():
    'Solve exercise 2 from rational expectations module'
    A_0 = 100
    A_1 = 0.05
    beta = 0.95
    d = 10.0
    H_guesses = [(94.0888, .9211),
                 (93.22, .9433),
                 (95.08187459215024, .95245906270392)]
    rational_equil = []
    for H_0, H_1 in H_guesses:
        A = np.array([[1, 0, 0], [0, H_1, H_0], [0, 0, 1]])
        B = np.array([1, 0, 0])
        R = np.array([[0, -A_1/2, A_0/2], [-A_1/2, 0, 0], [A_0/2, 0, 0]])
        Q = -0.5*d

        F, P = olrp(beta, A, B, R, Q)
        f_1, f_2, f_3 = F[0]  # F is 2-d array, so slice is needed.

        # NOTE: below I check < 1e-8 because we shouldn't check for equality
        #       in floating point numbers.
        if abs(H_1 - (1-f_1-f_2)) < 1e-8 and abs(H_0+f_3 < 1e-8):
            rational_equil.append(True)
        else:
            rational_equil.append(False)

    return rational_equil

F_2 = ex2()

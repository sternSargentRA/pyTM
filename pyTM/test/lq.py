import numpy as np
from pyTM.util.lq import MarkovPerfectDuopoly


# def test_nnash():
    # "use judd test case for nnash. Follows judd.m"

# Define Parameters
delta = 0.02
d = np.array([[-1, 0.5], [0.5, -1]])
B = np.array([25, 25])
c1 = np.array([1, -2, 1])
c2 = np.array([1, -2, 1])
e1 = np.array([10, 10, 3])
e2 = np.array([10, 10, 3])
delta_1 = 1 - delta

## Define matrices
a = np.array([[delta_1, 0, -delta_1*B[0]],
              [0, delta_1, -delta_1*B[1]],
              [0, 0, 1]])

b1 = delta_1 * np.array([[1, -d[0, 0]],
                         [0, -d[1, 0]],
                         [0, 0]])
b2 = delta_1 * np.array([[0, -d[0, 1]],
                         [1, -d[1, 1]],
                         [0, 0]])

r1 = -np.array([[0.5*c1[2], 0, 0.5*c1[1]],
                [0, 0, 0],
                [0.5*c1[1], 0, c1[0]]])
r2 = -np.array([[0, 0, 0],
                [0, 0.5*c2[2], 0.5*c2[1]],
                [0, 0.5*c2[1], c2[0]]])

q1 = np.array([[0.5*e1[2], 0], [0, d[0, 0]]])
q2 = np.array([[0.5*e2[2], 0], [0, d[1, 1]]])

s1 = np.zeros((2, 2))
s2 = np.copy(s1)

w1 = np.array([[0, 0],
               [0, 0],
               [-0.5*e1[1], B[0]/2.]])
w2 = np.array([[0, 0],
               [0, 0],
               [-0.5*e2[1], B[1]/2.]])

m1 = np.array([[0, 0], [0, d[0, 1] / 2.]])
m2 = np.copy(m1)

# build model and solve it
model = MarkovPerfectDuopoly(a, b1, b2, r1, r2, q1, q2, s1, s2, w1, w2,
                             m1, m2)

f1, f2, p1, p2 = model.nnash()



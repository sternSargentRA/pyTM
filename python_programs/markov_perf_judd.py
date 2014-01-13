"""
Tutorial for using nnash to solve the problem proposed by Judd

@author : Spencer Lyon
@date : 2014-01-13 16:24:14

"""
import numpy as np
from pyTM.util.lq import nnash


def pause(prt_msg=None):
    import sys
    if sys.version_info[0] <= 2:
        inp = raw_input
    else:
        inp = input

    if prt_msg:
        msg = prt_msg
    else:
        msg = "\nPress Enter (and nothing else) to continue\n"
    inp(msg)

m = """
      This program computes the Nash feedback equilibrium
      of a linear quadratic dynamic game.   Each of two players
      solves a linear quadratic optimization problem, taking as
      given and known the sequence of linear feedback rules used
      by his opponent.

      The particular game analyzed is a price-quantity setting
      game suggested by Ken Judd."""

print(m)
pause()

m = """
      There are two firms.  There is no uncertainty.  Relevant
      variables are defined as follows:

       Ii(t) = inventories of firm i at beginning of t.
       qi(t) = production of firm i during period t.
       pi(t) = price charged by firm i during period t.
       Si(t) = sales made by firm i during period t.
       Ei(t) = costs of production of firm i during period t.
       Ci(t) = costs of carrying inventories for firm i during t.

      It is assumed that costs obey

       Ci(t) = ci(1) + ci(2)*Ii(t) + .5* ci(3)*Ii(t)^2
       Ei(t) = ei(1) + ei(2)*qi(t) + .5* ei(3)*qi(t)^2

      where ei(j) and ci(j) are constants.

      It is assumed that inventories obey the laws of motion

       Ii(t+1) = (1 - del) * Ii(t) + qi(t) - Si(t)"""

print(m)
pause()

m = """
      It is assumed that demand is governed by the linear schedule


       S(t) = d * p(t) + B

      where S(t) = [S1(t),S2(t)]', d is a (2x2) negative definite
      matrix, and B is a vector of constants.
      Firm i is assumed to maximize the undiscounted sum

       SUM { pi(t)*Si(t) - Ei(t) - Ci(t) }

      by choosing a control law of the form

       ui(t) = -Fi * x(t)

      where ui(t) = [pi(t),qi(t)]', and the state x(t)
      is given by x(t)=[I1(t),I2(t),1]."""

print(m)
pause()

m = """
      Firm i is assumed to solve its control problem taking
      the (sequence of) control laws uj(t) = -Fj(t)*x(t) as
      known and given.

      The program computes the limiting values of the control
      laws (F1(t),F2(t)) as the horizon is extended to infinity."""

print(m)
pause("\nNow the program will set some parameters. Press Enter.\n")

delta = 0.02
d = np.array([[-1, 0.5], [0.5, -1]])
B = np.array([25, 25])
c1 = np.array([1, -2, 1])
c2 = np.array([1, -2, 1])
e1 = np.array([10, 10, 3])
e2 = np.array([10, 10, 3])
delta_1 = 1 - delta

m = """
      Now we'll create the matrices needed to compute the
      Nash feedback equilibrium.  We will proceed by iterating
      on pairs of "Ricatti" equations.  Player 1 has a regulator
      problem with matrices r1,w1,q1,s1,m1 in the objective function
      (see the explanation of these quantities when nnash is
      called shortly) and matrices a,b1,and b2 in the law of motion
      (again, see the explanation when nnash is called)."""

print(m)
pause("\nPress Enter to define these matrices\n")

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

q1 = np.array([[-0.5*e1[2], 0], [0, d[0, 0]]])
q2 = np.array([[-0.5*e2[2], 0], [0, d[1, 1]]])

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

pause("\nPress Enter to call nnash to compute equilibrium\n")
f1, f2, p1, p2 = nnash(a, b1, b2, r1, r2, q1, q2, s1, s2, w1, w2, m1, m2)

pause("\nPress Enter to see Firm 1's feedback rule\n")
print(f1)

pause("\nPress Enter to see Firm 2's feedback rule\n")
print(f2)

pause("\nPress Enter to compute closed loop control law\n")
aaa = a - b1.dot(f1) - b2.dot(f2)

m = """

     Recall that the state is x(t)=[I1(t),I2(t),1]'
     So the equilibrium law of motion is

       x(t+1) = aaa * x(t)
            or
       x(t+1) = (a - b1*F1 - b2*F2) * x(t)"""

print(m)
pause("\nPress Enter to calculate the optimal stationary values\n")
aa = aaa[:2, :2]
tf = np.eye(2)-aa
tfi = np.linalg.inv(tf)
xbar = tfi.dot(aaa[:2, 2])

print("xbar = \n\n\t%s\n" % str(xbar))

print("This concludes the tutorial")

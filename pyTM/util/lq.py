"""
Utility functions needed in the pyTM lectures

@author : Spencer Lyon
@author : Chase Coleman
@date : 2014-01-11 15:07:13

"""
from __future__ import division, print_function
from numbers import Number
from math import sqrt
import numpy as np
from numpy import dot, eye
from scipy.linalg import solve, eig

__all__ = ["doublej", "doubleo", "olrp", "MarkovPerfectDuopoly"]


def doublej(a1, b1, max_it=50):
    """
    Computes the infinite sum V given by

    .. math::

        V = \sum_{j=0}^{\infty} a1^j b1 a1^j'

    where a1 and b1 are each (n X n) matrices with eigenvalues whose
    moduli are bounded by unity and b1 is an (n X n) matrix.

    V is computed by using the following 'doubling algorithm'. We
    iterate to convergence on V(j) on the following recursions for
    j = 1, 2, ... starting from V(0) = b1:

    ..math::

        a1_j = a1_{j-1} a1_{j-1}
        V_j = V_{j-1} + A_{j-1} V_{j-1} a_{j-1}'

    The limiting value is returned in V
    """
    alpha0 = a1
    gamma0 = b1

    diff = 5
    n_its = 1

    while diff > 1e-15:

        alpha1 = alpha0.dot(alpha0)
        gamma1 = gamma0 + dot(alpha0.dot(gamma0), alpha0.T)

        diff = np.max(np.abs(gamma1 - gamma0))
        alpha0 = alpha1
        gamma0 = gamma1

        n_its += 1

        if n_its > max_it:
            raise ValueError('Exceeded maximum iterations of %i.' % (max_it) +
                             ' Check your input matrices')

    return gamma1


def doubleo(A, C, R, Q, tol=1e-15):
    """
    This function uses the "doubling algorithm" to solve the Riccati
    matrix difference equations associated with the Kalman filter.  The
    returns the gain K and the stationary covariance matrix of the
    one-step ahead errors in forecasting the state.

    The function creates the Kalman filter for the following system:

    .. math::

        x_{t+1} = A * x_t + e_{t+1}

        y_t = C * x_t + v_t

    where :math:`E e_{t+1} e_{t+1}' =  R`, and :math:`E v_t v_t' = Q`,
    and :math:`v_s' e_t = 0 \\forall s, t`.

    The function creates the observer system

    .. math::

        xx_{t+1} = A xx_t + K a_t

        y_t = C xx_t + a_t

    where K is the Kalman gain, :math:`S = E (x_t - xx_t)(x_t - xx_t)'`,
    and :math:`a_t = y_t - E[y_t| y_{t-1}, y_{t-2}, \dots ]`, and
    :math:`xx_t = E[x_t|y_{t-1},\dots]`.

    Parameters
    ----------
    A : array_like, dtype=float, shape=(n, n)
        The matrix A in the law of motion for x

    C : array_like, dtype=float, shape=(k, n)
        The matrix C from above

    R : array_like, dtype=float, shape=(n, n)
        The matrix R from above

    Q : array_like, dtype=float, shape=(k, k)
        The matrix Q from above

    tol : float, optional(default=1e-15)
        Tolerance level for convergence.

    Returns
    -------
    K : array_like, dtype=float
        The Kalman gain K

    S : array_like, dtype=float
        The stationary covariance matrix of the one-step ahead errors
        in forecasting the state.

    Notes
    -----
    By using DUALITY, control problems can also be solved.

    """
    a0 = A.T
    b0 = dot(C.T, solve(Q, C))
    g0 = R
    dd = 1.
    ss = max(A.shape)
    v = eye(ss)

    # NOTE: This is a little hack to make sure we update k1 and k0 properly
    #       depending on the dimensions of C
    c_vec = C.shape[0] > 1

    while dd > tol:
        a1 = dot(a0, solve(v + dot(b0, g0), a0))
        b1 = b0 + dot(a0, solve(v + dot(b0, g0), dot(b0, a0.T)))
        g1 = g0 + dot(dot(a0.T, g0), solve(v + dot(b0, g0), a0))

        if c_vec:
            k1 = dot(A.dot(g1), solve(dot(C, g1.T).dot(C.T) + Q.T, C).T)
            k0 = dot(A.dot(g0), solve(dot(C, g0.T).dot(C.T) + Q.T, C).T)
        else:
            k1 = dot(dot(A, g1), C.T / (dot(C, g1).dot(C.T) + Q))
            k0 = dot(A.dot(g0), C.T / (dot(C, g0).dot(C.T) + Q))

        dd = np.max(np.abs(k1 - k0))
        a0 = a1
        b0 = b1
        g0 = g1

    return k1, g1


def olrp(beta, A, B, R, Q, N=None, tol=1e-6, max_iter=1000):
    """
    Calculates F of the feedback law:

    .. math::

        U = -Fx

    that maximizes the function:

    .. math::

        \sum \{\\beta^t [x'Rx + u'Qu +2x' N u] \}

    subject to

    .. math::
        x_{t+1} = A x_t + B u_t

    where x is the nx1 vector of states, u is the kx1 vector of controls

    Parameters
    ----------
    beta : float
        The discount factor from above. If there is no discounting, set
        this equal to 1.

    A : array_like, dtype=float, shape=(n, n)
        The matrix A in the law of motion for x

    B : array_like, dtype=float, shape=(n, k)
        The matrix B in the law of motion for x

    R : array_like, dtype=float, shape=(n, n)
        The matrix R from the objective function

    Q : array_like, dtype=float, shape=(k, k)
        The matrix Q from the objective function

    N : array_like, dtype=float, shape=(n, k), optional(default=0)
        The matrix N from the objective function. Represents the cross
        product terms.

    tol : float, optional(default=1e-6)
        Convergence tolerance for case when largest eigenvalue is below
        1e-5 in modulus

    max_iter : int, optional(default=1000)
        The maximum number of iterations the function will allow before
        stopping

    Returns
    -------
    F : array_like, dtype=float
        The feedback law from the equation above.

    P : array_like, dtype=float
        The steady-state solution to the associated discrete matrix
        Riccati equation

    """
    if isinstance(Q, Number):  # if Q is a numeric scalar
        k = 1
        Q = np.reshape(Q, (1, 1))

    n = A.shape[0]

    B = np.reshape(B, (n, k))

    if N is None:
        N = np.zeros((n, k))

    if np.min(np.abs(eig(np.atleast_2d(Q))[0])) > 1e-5:
        Q_mldiv_N = solve(Q, N.T)
        A = sqrt(beta) * (A - B.dot(Q_mldiv_N))
        B = sqrt(beta) * B
        R = R - N.dot(Q_mldiv_N)

        k, s = doubleo(A.T, B.T, R, Q)

        f = k.T + Q_mldiv_N

        p = s

    else:
        p0 = -0.1 * eye(n)
        dd = 1
        it = 1

        for it in range(max_iter):
            f0 = solve(Q + beta * B.T.dot(p0).dot(B),
                       beta * B.T.dot(p0).dot(A) + N.T)
            p1 = beta * A.T.dot(p0).dot(A) + R - \
                (beta * A.T.dot(p0).dot(B) + N).dot(f0)
            f1 = solve(Q + beta * B.T.dot(p1).dot(B),
                       beta * B.T.dot(p1).dot(A) + N.T)
            dd = np.max(f1 - f0)
            p0 = p1

            if dd < tol:  # success!
                break
        else:
            msg = 'No convergence: Iteration limit of {0} reached in OLRP'
            raise ValueError(msg.format(max_iter))

        f = f1
        p = p1

    return f, p


class MarkovPerfectDuopoly(object):
    """
    This class is for analyzing the linear Markov perfect equilibrium
    associated with the duopoly example. In this example, player i
    maximizes

    .. math::
        - \\sum_{t=0}^{\\infty} \\left\\{x_t' r_i x_t + 2 x_t' w_i
        u_{it} +u_{it}' q_i u_{it} + u_{jt}' s_i u_{jt} + 2 u_{jt}'
        m_i u_{it} \\right\\}

    subject to the law of motion

    .. math::
        x_{t+1} = a x_t + b_1 u_{1t} + b_2 u_{2t}

    and a perceived control law :math:`u_j(t) = - f_j x_t` for the other
    player.

    Parameters
    ----------

    The inputs are the matrices from the equations above:

    * a : shape=(n, n)
    * b1 : shape=(n, k_1)
    * b2 : shape=(n, k_2)
    * r1 : shape=(n, n)
    * r2 : shape=(n, n)
    * q1 : shape=(k_1, k_1)
    * q2 : shape=(k_2, k_2)
    * s1 : shape=(k_1, k_1)
    * s2 : shape=(k_2, k_2)
    * w1 : shape=(n, k_1)
    * w2 : shape=(n, k_2)
    * m1 : shape=(k_2, k_1)
    * m2 : shape=(k_1, k_2)


    """

    def __init__(self, a, b1, b2, r1, r2, q1, q2, s1, s2, w1, w2, m1, m2):

        self.a = a
        self.b1 = b1
        self.b2 = b2
        self.r1 = r1
        self.r2 = r2
        self.q1 = q1
        self.q2 = q2
        self.s1 = s1
        self.s2 = s2
        self.w1 = m1
        self.w2 = m2
        self.m1 = m1
        self.m2 = m2

    def nnash(self, tol=1e-8, max_iter=1000):
        """
        Compute the limit of a Nash linear quadratic dynamic game.

        The solution computed in this routine is the :math:`f_i` and
        :math:`p_i` of the associated double optimal linear regulator
        problem.

        Parameters
        ----------
        tol : float, optional(default=1e-8)
            The tolerance level for convergence

        max_iter :int, optional(default=1000)
            The maximum number of iterations to allow

        Returns
        -------
        f_1 : array_like, dtype=float, shape=(k_1, n)

        f_2 : array_like, dtype=float, shape=(k_2, n)

        p_1 : array_like, dtype=float, shape=TODO

        p_2 : array_like, dtype=float, shape=TODO

        """
        # Unload parameters
        a = np.asarray(self.a)
        b1 = np.asarray(self.b1)
        b2 = np.asarray(self.b2)
        r1 = np.asarray(self.r1)
        r2 = np.asarray(self.r2)
        q1 = np.asarray(self.q1)
        q2 = np.asarray(self.q2)
        s1 = np.asarray(self.s1)
        s2 = np.asarray(self.s2)
        w1 = np.asarray(self.w1)
        w2 = np.asarray(self.w2)
        m1 = np.asarray(self.m1)
        m2 = np.asarray(self.m2)

        n = a.shape[0]

        if b1.ndim == 1:
            k_1 = 1
            b1 = np.reshape(b1, (n, 1))
        else:
            k_1 = b1.shape[1]

        if b2.ndim == 1:
            k_2 = 1
            b2 = np.reshape(b2, (n, 1))
        else:
            k_2 = b2.shape[1]

        v1 = eye(k_1)
        v2 = eye(k_2)
        p1 = np.zeros((n, n))
        p2 = np.zeros((n, n))
        f1 = np.random.randn(n, n)
        f2 = np.random.randn(n, n)

        for it in range(max_iter):
            # update
            f10 = f1
            f20 = f2

            g2 = solve(dot(b2.T, p2.dot(b2))+q2, v2)
            g1 = solve(dot(b1.T, p1.dot(b1))+q1, v1)
            h2 = dot(g2, b2.T.dot(p2))
            h1 = dot(g1, b1.T.dot(p1))

            # break up the computation of f1, f2
            f_1_left = v1 - dot(h1.dot(b2)+g1.dot(m1.T),
                                h2.dot(b1)+g2.dot(m2.T))
            f_1_right = h1.dot(a)+g1.dot(w1.T) - dot(h1.dot(b2)+g1.dot(m1.T),
                                                     h2.dot(a)+g2.dot(w2.T))
            f1 = solve(f_1_left, f_1_right)
            f2 = h2.dot(a)+g2.dt(w2.T) - dot(h2.dot(b1)+g2.dot(m2.T), f1)

            a2 = a - b2.dot(f2)
            a1 = a - b1.dot(f1)

            p1 = (dot(a2.T, p1.dot(a2)) + r1 + dot(f2.T, s1.dot(f2)) -
                  dot(dot(a2.T, p1.dot(b1)) + w1 - f2.T.dot(m1), f1))
            p2 = (dot(a1.T, p2.dot(a1)) + r2 + dot(f1.T, s2.dot(f1)) -
                  dot(dot(a1.T, p2.dot(b2)) + w2 - f1.T.dot(m2), f2))

            if dd < tol:  # success!
                break

        else:
            msg = 'No convergence: Iteration limit of {0} reached in nnash'
            raise ValueError(msg.format(max_iter))

        return f1, f2, p1, p2

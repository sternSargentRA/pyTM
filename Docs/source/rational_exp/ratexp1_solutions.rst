.. _ratexp1_solutions:

*******************************************
Rational Expectations Equilibrium Solutions
*******************************************

Exercise 1
==========

Recall that the objective function of the firm is

.. math::
    \max \sum_{t = 0}^{\infty} \beta^t R^t \\
    \text{subject to } & R_t = p_ty_t - .5 d \left( y_{t+1} - y_t \right)^2\\
    & p_t = A_o - A_1 Y_t \quad A_0, A_1 > 0 \\
    & Y_{t+1} = H_0 + H_1 Y_t.
    :label: ex1_obj


Part a
^^^^^^

The Bellman equation for the firm's problem is given by

.. math::
    v(y, Y) = \max_{y'} (A_0 - A_1 Y) y - .5 d(y' - y)^2 + \beta V(y', Y')

Part b
^^^^^^

The discounted linear control problem is

.. math::
    &\max -\sum_{t=0}^{\infty} \beta^t \left\{ x_t' R x_t  + u_t' Q u_t\right\} \\
    \text{subject to } & x_{t+1} = A x_t + B u_t


To map the firm's problem into a discounted optimal linear control problem, we need to define a state vector :math:`x_t`, a control vector :math:`u_t`, and matrices :math`:A, B, Q, R` that define the preferences in the objective function and the law of motion for the state.

For the state and control vectors choose

.. math::

    x = \begin{bmatrix} y_t \\ Y_t \\ 1 \end{bmatrix}

    u = y_{t+1} - y_{t}.

To see how to define the matrices :math:`A, B, Q, R`, we substitute :math:`R_t` and :math:`p_t` out of :eq:`ex1_obj` and write the objective function as

.. math::
    \max \sum_{t = 0}^{\infty} \beta^t \left[ \left( A_0 - A_1 Y_t\right)y_t - .5 d \left( y_{t+1} - y_t \right)   \right]
    \text{subject to } & Y_{t+1} = H_0 + H_1 Y_t.
    :label: ex1_obj2

Studying :eq:`ex1_obj2` we can now read of the needed matrices

.. math::
    A &= \begin{bmatrix} 1 & 0 & 0 \\ 0 & H_0 & H_1 \\ 0 & 0 & 1 \end{bmatrix} \\
    B &= \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix} \\
    R &= \begin{bmatrix} 0 & -A_1/0 & A_0/2 \\ -A_1/2 & 0 & 0 \\ A_0/2 & 0 & 0 \end{bmatrix} \\
    Q &= -.5 d


Part c
^^^^^^

As given in the solution to part (b), the state for the firm's problem is :math:`x_t = \left[\begin{smallmatrix} y_t \\ Y_t \\ 1 \end{smallmatrix}\right]`.

Part d
^^^^^^

.. todo:: Clean this up. It is a bit verbose. Maybe just link to the files?

Here are functions `doubleo` and `olrp` that solve the linear quadratic control problem.

.. literalinclude:: ../../../pyTM/util/lq.py
   :pyobject: doubleo

.. literalinclude:: ../../../pyTM/util/lq.py
   :pyobject: olrp


The code below uses the `olrp` function above to compute the feedback law :math:`F` governing the solution.

.. literalinclude:: ../../../pyTM/ratexp/ratexp1.py
   :pyobject: ex1

The output of that functions gives us

.. math::
    F = \begin{bmatrix} 0 & 0.0463 & -96.949 \end{bmatrix}

Part f
^^^^^^

The matrix routine `olrp` solves for :math:`F` such that

.. math::
    u_T = - F x_t.

This means we have the following

.. math::
    y_{t+1} - y_t &= - \begin{bmatrix} 0 & 0.0463 & -96.949 \end{bmatrix} \begin{bmatrix} y_t \\ Y_t \\ 1 \end{bmatrix} \\
    y_{t+1} &= 96.949 + y_t - 0.0463 Y_t,

which implies that

.. math::
    h_0 &= 96.949 \\
    h_1 &= 1 \\
    h_2 &= -0.0463 \\

Part g
^^^^^^

In equilibrium we have that :math:`Y_t = n y_t`, which means

.. math::
    Y_{t+1} &= n y_{t+1} \\
    &= n (h_0 + h_1 y_t + h_2 Y_t) \\
    &= n \left( 96.949 + y_t - 0.0463 Y_t \right)  \\
    &= n 96.949 + Y_t - n 0.0463 Y_t \\
    &= n 96.949 + (1 - n 0.0463) Y_t \\

Exercise 2
==========

.. todo:: revise this answer. I was tired

Part a
^^^^^^

A rational expectations equilibrium requires that the actual law of motion is equal to the perceived law of motion. In this case, because there is only one firm, this means that we need :math:`H_0, H_1` to be such that :math:`y_t = Y_t \; \forall t`.

Recall from the problem description that :math:`Y_{t+1} = H_0 + H_1 Y_t`. We also know that the `olrp` routine from above will give us the matrix :math:`F` in the equation :math:`u_t = - F x_t`. Recall that :math:`u_t = y_{t+1} - y_t`, which implies that :math:`y_{t+1} - y_t = -F x_t`. Let :math:`f_i` be the :math:`i` th element of the matrix :math:`F`. Applying the condition for a rational expectations equilibrium (:math:`y_t = Y_t`) we have that

.. math::
    Y_{t+1} &= y_{t+1} \\
    H_0 + H_1 Y_t &= y_t - F x_t \\
    H_0 + H_1 Y_t &= (1 - f_1) y_t - f_2 Y_t - f_3 \\
    H_0 + H_1 Y_t &= (1 - f_1 - f_2) Y_t - f_3 \\
    :label: ex2_cond

must hold for :math:`H_0, H_1` to lead to a rational expectations equilibrium. Note that in the last line we assume that we are in equilibrium and that :math:`y_t = Y_t`

The code below uses each guess for :math:`H_0, H_1`, solves for the implied value of the feedback rule :math:`F`, and checks the condition in :eq:`ex2_cond`.

.. literalinclude:: ../../../pyTM/ratexp/ratexp1.py
   :pyobject: ex2

The return value of this function is `[False, False, True]`, telling us that only under the third parameterization do the values for :math:`H_0, H_1` lead to a rational expectations equilibrium.

Part b
^^^^^^

Short answer: Let :math:`H = \left[\begin{smallmatrix} H_0 & H_1 \end{smallmatrix}\right]`. The optimal value of :math:`H` is a fixed point of the :math:`\cal{M}` mapping, where :math:`H' = \cal{M}{H}`. We can then simply iterate on :math:`\cal{M}` until we converge on a fixed point, which will be the optimal level for :math:`H`.

Exercise 3
==========

The planner would like to maximize the following

.. math::
    \sum_{t=0}^\infty \beta^t S_t
    \text{where } S_t := S(Y_t, Y_{t+1}) = \int_0^{Y_t} \left( A_0 - A_1 x \right) dx -.5d \left(Y_{t+1} - Y_t \right)^2
    :label: ex3_obj

Part a
^^^^^^

We can formulate the planner's Bellman equation by:

.. math::
    V(Y) = \max_{Y'} \int_0^{Y} \left( A_0 - A_1 x \right) dx -.5d \left(Y' - Y \right)^2 + \beta V(Y')

Part b
^^^^^^

The discounted linear control problem is

.. math::
    &\max -\sum_{t=0}^{\infty} \beta^t \left\{ x_t' R x_t  + u_t' Q u_t\right\} \\
    \text{subject to } & x_{t+1} = A x_t + B u_t


To map the firm's problem into a discounted optimal linear control problem, we need to define a state vector :math:`x_t`, a control vector :math:`u_t`, and matrices :math`:A, B, Q, R` that define the preferences in the objective function and the law of motion for the state.

For the state and control vectors choose

.. math::

    x = \begin{bmatrix} Y_t \\ 1 \end{bmatrix}

    u = Y_{t+1} - Y_{t}.

To see how to define the matrices :math:`A, B, Q, R`, we substitute :math:`S_t` out of :eq:`ex3_obj` and write the objective function as

.. math::
    \max \sum_{t = 0}^{\infty} \beta^t \left[ \left( A_0 - A_1 Y_t\right)y_t - .5 d \left( y_{t+1} - y_t \right)   \right]
    \text{subject to } & Y_{t+1} = H_0 + H_1 Y_t.
    :label: ex3_obj2

Studying :eq:`ex3_obj2` we can now read of the needed matrices

.. math::
    A &= \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \\
    B &= \begin{bmatrix} 1 \\ 0 \end{bmatrix} \\
    R &= \begin{bmatrix} A_1/2 & -A_0/2 \\ -A_0/2 & 0 \end{bmatrix} \\
    Q &= -.5 d

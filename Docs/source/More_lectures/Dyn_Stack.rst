Dynamic Stackelberg Problems
****************************

History dependence
==================

Previous lectures have studied  decision problems that are recursive in what we can call "natural" state variables

"natural" state variables describe

* stocks of capital
* wealth
* and information that helps forecast future values of prices and quantities that impinge on future payoffs

In problems that are recursive in the natural state variables, optimal decision rules are functions of the natural state variables.

In this lecture, we  encounter  a class of problems that are not recursive in the natural state variables.

Kydland and Prescott (1977), Prescott (1977), and Calvo (1978) gave macroeconomic examples of decision problems whose solutions exhibited *time inconsistency* because they are not recursive in the natural state variables.

Examples are decision problems of a large agent (a government)  who

* confronts a competitive market composed of many small private agents, and in which
* the private agents' decisions are influenced by their *forecasts* of the government's future actions

In such settings, the natural state variables of private agents at time :math:`t` are partly shaped by past decisions that were influenced by their earlier forecasts of the government's action at time :math:`t`.

In a rational expectations equilibrium, the government confirms private agents' earlier forecasts of the government's time :math:`t` actions.

Confirming prior forecasts puts constraints on the government's time :math:`t` decisions that prevent its problem from being recursive in natural state variables.

These additional constraints make the government's decision rule at :math:`t` depend on the entire history of the state from time :math:`0` to time :math:`t`.

An important finding is that if the natural state variables are augmented with additional state variables that measure costs in terms of the government's *current* continuation value of confirming *past* private sector expectations about its current behavior, this class of problems can be made recursive.

This fact affords immense computational advantages and yields substantial insights.

This lecture displays these within the tractable framework of linear quadratic problems.

The Stackelberg problem
=======================

We use the optimal linear regulator to solve a linear quadratic version of what is known as a dynamic Stackelberg problem.

For now we refer to the Stackelberg leader as the government and the Stackelberg follower as the representative agent or private sector.

Soon we'll give an application with another interpretation of these two players.

Let :math:`z_t` be an :math:`n_z \times 1` vector of natural state variables, :math:`x_t` an :math:`n_x \times 1` vector of endogenous variables free to jump at :math:`t`, and :math:`u_t` a vector of government instruments.

The :math:`z_t` vector is inherited from the past.

But :math:`x_t` is *not* inherited from the past.

The model determines the "jump variables" :math:`x_t` at time :math:`t`.

Included in :math:`x_t` are prices and quantities that adjust instantaneously to clear markets at time :math:`t`.

Let :math:`y_t = \begin{bmatrix} z_t \\ x_t \end{bmatrix}`.

Define the government's one-period loss function [#f1]_

.. math::
    r(y, u)  =  y' R y  + u' Q u
    :label: target

Subject to an initial condition for :math:`z_0`, but not for :math:`x_0`, a government wants to maximize

.. math::
      -  \sum_{t=0}^\infty \beta^t r(y_t, u_t)
      :label: new1

The government makes policy in light of the model

.. math::
  \begin{bmatrix} I & 0 \\ G_{21} & G_{22} \end{bmatrix}
  \begin{bmatrix}    z_{t+1} \\  x_{t+1} \end{bmatrix}
  = \begin{bmatrix}  \hat A_{11}  &  \hat A_{12} \\ \hat A_{21} & \hat A_{22}  \end{bmatrix} \begin{bmatrix}  z_t \\ x_t \end{bmatrix} + \hat B u_t
  :label: new2

We assume that the matrix on the left is invertible, so that we can multiply both sides of the above equation by its inverse to obtain

.. NOTE: I omitted a footnote here.

.. math::
  \begin{bmatrix}    z_{t+1} \\  x_{t+1} \end{bmatrix}
  = \begin{bmatrix}  A_{11}  &   A_{12} \\ A_{21} &  A_{22}  \end{bmatrix}
  \begin{bmatrix}  z_t \\ x_t \end{bmatrix} +  B u_t
  :label: new3

or

.. math::
  y_{t+1} = A y_t + B u_t
  :label: new30

The government maximizes by choosing sequences :math:`\{u_t, x_t, z_{t+1}\}_{t=0}^\infty` subject :eq:`new30` and the initial condition for :math:`z_0`.

The private sector's behavior is summarized by the second block of equations of :eq:`new3` or :eq:`new30`

These typically include the first-order conditions of private agents' optimization problem (i.e., their Euler equations).

They summarize the forward-looking aspect of private agents' behavior.

We shall provide an example later in this lecture XXXXXX in which, as is typical of these problems, the last :math:`n_x` equations of :eq:`new3` or :eq:`new30` constitute
*implementability constraints* that are formed by the Euler equations of a competitive fringe or private sector.

.. TODO: Fill in the XXXXX above

When combined with a stability condition to be imposed below, these Euler equations summarize the private sector's best response to the sequence of actions by the government.

A certainty equivalence principle *John -- we'll have to state it somewhere in our lectures*   allows us to work with a nonstochastic model.

.. TODO: John, see the note in italics above

We would attain the same decision rule if we were to replace :math:`x_{t+1}` with the forecast :math:`E_t x_{t+1}` and to add a shock process :math:`C \epsilon_{t+1}` to the right side of :eq:`new30`, where :math:`\epsilon_{t+1}` is an i.i.d. random vector with mean of zero and identity covariance matrix.

Let :math:`X^t` denote the history of any variable :math:`X` from :math:`0` to :math:`t`. Miller and Salmon (1982, 1985), Hansen, Epple, and Roberds (1985), Pearlman, Currie, and Levine (1986), Sargent (1987), Pearlman (1992), and others have all studied versions of the following problem:

**Problem S:** The *Stackelberg problem* is to maximize :eq:`new1` by choosing an :math:`x_0` and a sequence of decision rules, the time :math:`t` component of which maps the time :math:`t` history of the state :math:`z^t` into the time :math:`t` decision :math:`u_t` of the Stackelberg leader.

The Stackelberg leader commits to this sequence of decision rules at time :math:`0`.

The maximization is subject to a given initial condition for :math:`z_0`.

But :math:`x_0` is among the objects to be chosen by the Stackelberg leader.

The optimal decision rule is history dependent, meaning that :math:`u_t` depends not only on :math:`z_t` but also on lags of :math:`z`.

History dependence has two sources: (a) the government's ability to commit [#f2]_ to a sequence of rules at time :math:`0`, and (b) the forward-looking behavior of the private sector embedded in the second block of equations :eq:`new3`

The history dependence of the government's plan is expressed in the dynamics of Lagrange multipliers :math:`\mu_x` on the last :math:`n_x` equations of :eq:`new2` or :eq:`new3`.

These multipliers measure the costs today of honoring past government promises about current and future settings of :math:`u`.

It is appropriate to initialize the multipliers to zero at time :math:`t=0`, because then there are no past promises about :math:`u` to honor.

But the multipliers :math:`\mu_x` take nonzero values thereafter, reflecting future costs to the government of adhering to its commitment.

Solving the Stackelberg problem
===============================

This section describes a remarkable four-step algorithm for solving the Stackelberg problem.

Step 1: solve an optimal linear regulator
-----------------------------------------

Step 1 seems to disregard the forward-looking aspect of the problem
(step 3 will take account of that).

If we temporarily ignore the fact that the :math:`x_0` component of the state :math:`y_0 = \begin{bmatrix} z_0 \\ x_0 \end{bmatrix}` is *not* actually part of the true state vector, then superficially the Stackelberg problem :eq:`new1`, :eq:`new30` has the form of an optimal linear regulator problem.

It can be solved by forming a Bellman equation and iterating until it converges.


The optimal value function has the form :math:`v(y) = - y' P y`, where :math:`P` satisfies the Riccati equation :eq:`bell3`.

The next steps note how the value function :math:`v(y) = -y'Py` encodes objects that solve the Stackelberg problem, then tell how to decode them.

A reader not wanting to be reminded of the details of the Bellman equation can now move directly to step 2.

For those wanting a reminder, here it is.

The linear regulator is

.. math::
     v(y_0) = -y_0' P y_0
     = \max_{\{  u_t, y_{t+1}\}_{t=0}^\infty} - \sum_{t=0}^\infty \beta^t
     \left( y_t' R y_t +   u_t'   Q   u_t \right)
     :label: olrp1a

where the maximization is subject to a fixed initial condition for :math:`y_0` and the law of motion [#f3]_

.. math::
     y_{t+1} = A y_t +   B   u_t
     :label: new30a

Associated with problem :eq:`olrp1a`, :eq:`new30a` is the Bellman equation

.. math::
   - y' P y = {\rm max}_{  u, y^*} \left\{ -  y' R y -   u'Q u - \beta y^{* \prime} P y^* \right\}
   :label: bell1

where the maximization is subject to

.. math::
    y^* = A y + B   u
    :label:  bell2

where :math:`y^*` denotes next period's value of the state. Problem :eq:`bell1` gives rise to the matrix Riccati equation

.. math::
   P = R + \beta A' P A - \beta^2 A' P   B (  Q
   + \beta   B' P   B)^{-1}   B' P A
   :label: bell3

and the formula for :math:`F` in the decision rule :math:`  u_t = - F y_t`

.. math::
   F = \beta(   Q + \beta   B' P   B)^{-1}
   B' P A
   :label: bell4

Thus, we can solve problem :eq:`bell1`, :eq:`new30` by iterating to convergence on the difference equation counterpart to the algebraic Riccati equation :eq:`bell3`

Step 2: use the stabilizing properties of shadow price :math:`P y_t`
--------------------------------------------------------------------

At this point, we decode the information in the matrix :math:`P` in terms of shadow prices that are associated with a Lagrangian.

We adapt a method described earlier in section XXXXXX that solves a linear quadratic control problem of the form :eq:`new1`, :eq:`new30` by attaching a sequence of Lagrange multipliers :math:` 2 \beta^{t+1} \mu_{t+1}` to the sequence of constraints :eq:`new30` and then forming the Lagrangian:

.. TODO: Fill in the section link given the place holder XXXXXX above

.. math::
   {\cal L} = - \sum_{t=0}^\infty  \beta^t \left[ y_t' R  y_t + u_t' Q u_t
   + 2  \beta \mu_{t+1}'(A y_t + B u_t  - y_{t+1})
   \right]
   :label: olrp3

For the Stackelberg problem, it is important to partition :math:`\mu_t` conformably with our partition of :math:`y_t=\begin{bmatrix} z_t \\ x_t \end{bmatrix}`, so that :math:`\mu_t = \begin{bmatrix}  \mu_{zt} \\ \mu_{xt} \end{bmatrix}`, where :math:`\mu_{xt}` is an :math:`n_x \times 1` vector of multipliers adhering to the implementability constraints.

For now, we can ignore the partitioning of :math:`\mu_t`, but it will be very important when we turn our attention to the specific requirements of the Stackelberg problem in step 3.

We want to maximize :eq:`olrp3` with respect to sequences for :math:`u_t` and :math:`y_{t+1}`. The first-order conditions with respect to :math:`u_t, y_t`, respectively, are:

.. math::
  0 & = Q u_t + \beta B' \mu_{t+1}   \\
  \mu_t & = R y_t + \beta A' \mu_{t+1}
  :label: foc1

Solving :eq:`foc1` for :math:`u_t` and substituting into :eq:`new30` gives

.. math::
	y_{t+1} = A y_t - \beta B Q^{-1} B'  \mu_{t+1}.
	:label: olrp4

We can represent the system formed by :eq:`olrp4`  and :eq:`foc1` and as

.. math::
  \begin{bmatrix} I & \beta B Q^{-1} B' \\ 0 & \beta A' \end{bmatrix}
  \begin{bmatrix} y_{t+1} \\ \mu_{t+1} \end{bmatrix}
  =  \begin{bmatrix} A & 0 \\ - R & I \end{bmatrix}
  \begin{bmatrix} y_t \\ \mu_t \end{bmatrix}
  :label: olrp7

or

.. math::
  L^* \begin{bmatrix} y_{t+1} \\ \mu_{t+1}  \end{bmatrix}
  =  N \begin{bmatrix} y_t \\ \mu_t  \end{bmatrix}.
  :label: olrp8

We seek a "stabilizing" solution of :eq:`olrp8`, i.e., one that satisfies

.. math::
	\sum_{t=0}^\infty  \beta^t y_t' y_t < +\infty

Stabilizing solution
--------------------

By the same argument used in section XXXXXX of chapter XXXXXX, a stabilizing solution satisfies :math:`\mu_0 = P y_0`, where :math:`P` solves the matrix Riccati equation :eq:`bell3`. The solution for :math:`\mu_0` replicates itself over time in the sense that

.. TODO: fill in section and chapter links given the placeholder XXXXXX above

.. math::
	\mu_t = P y_t .
	:label: king4

Appendix :ref:`appAblkstack` verifies that the matrix :math:`P` that satisfies the Riccati equation :eq:`bell3` is the same :math:`P` that defines the stabilizing initial conditions :math:`(y_0, P y_0)`. In Appendix XXXXXXX, we describe how to construct :math:`P` by computing generalized eigenvalues and eigenvectors.

.. TODO: Fill in the link to the appendix given the placeholder XXXXXXX above.

Step 3: convert implementation multipliers into state variables
---------------------------------------------------------------

Key insight
~~~~~~~~~~~

We now confront the fact that the :math:`x_0` component of :math:`y_0` consists of variables that are not state variables, i.e., they are not inherited from the past but are to be determined at time :math:`t`. In the optimal linear regulator problem, :math:`y_0` is a state vector inherited from the past; the multiplier :math:`\mu_0` jumps at :math:`t` to satisfy :math:`\mu_0 = P y_0` and thereby stabilize the system. But in the Stackelberg problem, pertinent components of *both* :math:`y_0` *and* :math:`\mu_0` must adjust to satisfy :math:`\mu_0 = P y_0`. In particular, partition :math:`\mu_t` conformably with the partition of :math:`y_t` into :math:`\begin{bmatrix} z_t' &  x_t' \end{bmatrix}'` [#f4]_:

.. math::
	\mu_t = \begin{bmatrix}  \mu_{zt} \\ \mu_{xt} \end{bmatrix}.

For the Stackelberg problem, the first :math:`n_z` elements of :math:`y_t` are predetermined but the remaining components are free. And while the first :math:`n_z` elements of :math:`\mu_t` are free to jump at :math:`t`, the remaining components are not. The third step completes the solution of the Stackelberg problem by acknowledging these facts.
*After* we have performed the key step of computing the matrix :math:`P` that solves the Riccati equation :eq:`bell3`, we convert the last :math:`n_x` Lagrange multipliers :math:`\mu_{xt}` into state variables by using the following procedure

Write the last :math:`n_x` equations of :eq:`king4` as

.. math::
	\mu_{xt} = P_{21} z_t + P_{22} x_t,
	:label: king5

where the partitioning of :math:`P` is conformable with that of :math:`y_t` into :math:`\begin{bmatrix} z_t &  x_t  \end{bmatrix}'`. The vector :math:`\mu_{xt}` becomes part of the state at :math:`t`, while :math:`x_t` is free to jump at :math:`t`. Therefore, we solve :eq:`king5` for :math:`x_t` in terms of :math:`(z_t, \mu_{xt})`:

.. math::
	x_t = - P_{22}^{-1} P_{21} z_t + P_{22}^{-1} \mu_{xt}.
	:label: king6

Then we can write

.. math::
   y_t =\begin{bmatrix} z_t \\ x_t  \end{bmatrix}
   = \begin{bmatrix} I & 0 \\ - P_{22}^{-1} P_{21} &  P_{22}^{-1} \end{bmatrix}
   \begin{bmatrix} z_t \\ \mu_{xt}  \end{bmatrix}
	:label: king7

and from

.. math::
  \mu_{xt} =  \begin{bmatrix}  P_{21} & P_{22} \end{bmatrix} y_t .
  :label: king8

With these modifications, the key formulas :eq:`bell4` and :eq:`bell3` from the optimal linear regulator for :math:`F` and :math:`P`, respectively, continue to apply. Using :eq:`king7`, the optimal decision rule is

.. math::
  u_t = -F \begin{bmatrix} I & 0 \\ - P_{22}^{-1} P_{21} &  P_{22}^{-1} \end{bmatrix}
  \begin{bmatrix} z_t \\ \mu_{xt}  \end{bmatrix}.
  :label: king10

Then we have the following complete description of the Stackelberg plan: \

.. math::
  \begin{bmatrix}  z_{t+1} \\ \mu_{x,t+1} \end{bmatrix} &=
  \begin{bmatrix} I & 0 \\ P_{21} & P_{22}\end{bmatrix}
  (A - B F)
  \begin{bmatrix}  I & 0 \\ - P_{22}^{-1} P_{21} & P_{22}^{-1}  \end{bmatrix}
  \begin{bmatrix}  z_t \\ \mu_{xt} \end{bmatrix} \\
  x_t &= \begin{bmatrix}  - P_{22}^{-1} P_{21}   & P_{22}^{-1} \end{bmatrix}
  \begin{bmatrix}  z_t \\ \mu_{xt} \end{bmatrix}
  :label: king11

The difference equation :eq:`king11` is to be initialized from the given value of :math:`z_0` and a value for :math:`\mu_{x0}` to be determined in step 4.

Step 4: solve for :math:`x_0` and :math:`\mu_{x0}`
--------------------------------------------------

The value function :math:`V(y_0)` satisfies

.. math::
	V(y_0) = - z_0 ' P_{11} z_0 - 2 x_0' P_{21} z_0 - x_0' P_{22} x_0 .
	:label: valuefny

Now choose :math:`x_0` by equating to zero the gradient of :math:`V(y_0)` with respect to :math:`x_0`:

.. math::
	- 2 P_{21} z_0 - 2 P_{22} x_0 =0,

which by virtue :eq:`king5` of is equivalent with

.. math::
	\mu_{x0} = 0 .
	:label: mu0condition

Then we can compute :math:`x_0` from :eq:`king6` to arrive at

.. math::
	x_0 = - P_{22}^{-1} P_{21} z_0.
	:label: king6x0

The Lagrange multiplier :math:`\mu_{xt}` measures the cost to the Stackelberg leader at :math:`t \geq 0` of confirming expectations about its time :math:`t` action that the followers had held at dates :math:`s < t`. Setting :math:`\mu_{x0}=0` means that at time :math:`0` there are no such prior expectations to confirm.

Summary
-------

In summary, we solve the Stackelberg problem by formulating a particular optimal linear regulator, solving the associated matrix Riccati equation :eq:`bell3` for :math:`P`, computing :math:`F`, and then partitioning :math:`P` to obtain representation :eq:`king11`.

History-dependent representation of decision rule
-------------------------------------------------

For some purposes, it is useful to eliminate the implementation multipliers :math:`\mu_{xt}` and to express the decision rule for :math:`u_t` as a function of :math:`z_t, z_{t-1},` and :math:`u_{t-1}`. This can be accomplished as follows [#f6]_. First represent :eq:`king11` compactly as

.. math::
  \begin{bmatrix}  z_{t+1} \\ \mu_{x,t+1} \end{bmatrix}
  = \begin{bmatrix} m_{11} & m_{12} \\ m_{21} & m_{22}\end{bmatrix}
  \begin{bmatrix}  z_t \\ \mu_{xt} \end{bmatrix}
  :label: vonzer1

and write the feedback rule for :math:`u_t`

.. math::
  u_t  = f_{11}  z_{t} + f_{12} \mu_{xt} .
  :label: vonzer2

Then where :math:`f_{12}^{-1}` denotes the generalized inverse of :math:`f_{12}`, :eq:`vonzer2` implies :math:`\mu_{x,t} = f_{12}^{-1}(u_t - f_{11}z_t)`. Equate the right side of this expression to the right side of the second line of :eq:`vonzer1` lagged once and rearrange by using :eq:`vonzer2` lagged once and rearrange by using lagged once to eliminate :math:`\mu_{x,t-1}` to get

.. math::
  u_t =  f_{12} m_{22} f_{12}^{-1} u_{t-1} + f_{11} z_t + f_{12}(m_{21} - m_{22} f_{12}^{-1} f_{11}) z_{t-1}
  :label: vonzer3a

or

.. math::
  u_t = \rho u_{t-1} + \alpha_0 z_t + \alpha_1 z_{t-1}
  :label: vonzer3b


for :math:`t \geq 1`. For :math:`t=0`, the initialization :math:`\mu_{x,0}=0` implies that

.. math::
	u_0 = f_{11} z_0.
	:label: vonzer3c

By making the instrument feed back on itself, the form of potentially allows for "instrument-smoothing" to emerge as an optimal rule under commitment.

Digression on determinacy of equilibrium
----------------------------------------

Appendix XXXXXXX describes methods for solving a system of difference equations of the form :eq:`new2` or :eq:`new3` with an arbitrary feedback rule that expresses the decision rule for :math:`u_t` as a function of current and previous values of :math:`y_t` and perhaps previous values of itself. The difference equation system has a unique solution satisfying the stability condition :math:`\sum_{t=0}^\infty \beta^t y_t \cdot  y_t` if the eigenvalues of the matrix :eq:`symplec2` split, with half being greater than unity and half being less than unity in modulus. If more than half are less than unity in modulus, the equilibrium is said to be indeterminate in the sense that there are multiple equilibria starting from any initial condition.

.. TODO: Fill in the link to the appendix given the placeholder XXXXXXX above.

If we choose to represent the solution of a Stackelberg or Ramsey problem in the form :eq:`vonzer3`, we can substitute that representation for :math:`u_t` into :eq:`new3`, obtain a difference equation system in :math:`y_t, u_t`, and ask whether the resulting system is determinate. To answer this question, we would use the method of Appendix XXXXXXX, form system , then check whether the generalized eigenvalues split as required. Researchers have used this method to study the determinacy of equilibria under Stackelberg plans with representations like :eq:`vonzer3` and have discovered that sometimes an equilibrium can be indeterminate [#f7]_. See Evans and Honkapohja (2003) for a discussion of determinacy of equilibria under commitment in a class of equilibrium monetary models and how determinacy depends on how the decision rule of the Stackelberg leader is represented. Evans and Honkapohja argue that casting a government decision rule in a way that leads to indeterminacy is a bad idea.

.. TODO: Fill in the link to the appendix given the placeholder XXXXXXX above.

A large firm with a competitive fringe
======================================

As an example, this section studies the equilibrium of an industry with a large firm that acts as a Stackelberg leader with respect to a competitive fringe. Sometimes the large firm is called ‘the monopolist' even though there are actually many firms in the industry. The industry produces a single nonstorable homogeneous good. One large firm produces :math:`Q_t` and a representative firm in a competitive fringe produces :math:`q_t`. The representative firm in the competitive fringe acts as a price taker and chooses sequentially. The large firm commits to a policy at time :math:`0`, taking into account its ability to manipulate the price sequence, both directly through the effects of its quantity choices on prices, and indirectly through the responses of the competitive fringe to its forecasts of prices [#f8]_.

The costs of production are :math:`{\cal C}_t = e Q_t + .5 g Q_t^2+ .5 c (Q_{t+1} - Q_{t})^2` for the large firm and :math:`\sigma_t= d q_t + .5 h q_t^2 + .5 c (q_{t+1} - q_t)^2` for the competitive firm, where :math:`d>0, e >0, c>0, g >0, h>0` are cost parameters. There is a linear inverse demand curve

.. math::
	p_t = A_0 - A_1 (Q_t + \overline q_t) + v_t,
	:label: oli1

where :math:`A_0, A_1` are both positive and :math:`v_t` is a disturbance to demand governed by

.. math::
	v_{t+1}= \rho v_t + C_\epsilon \check \epsilon_{t+1}
	:label: oli2

and where :math:` | \rho | < 1` and :math:`\check \epsilon_{t+1}` is an i.i.d.sequence of random variables with mean zero and variance :math:`1`. In :eq:`oli1`, :math:`\overline q_t` is equilibrium output of the representative competitive firm. In equilibrium, :math:`\overline q_t = q_t`, but we must distinguish between :math:`q_t` and :math:`\overline q_t` in posing the optimum problem of a competitive firm.

The competitive fringe
----------------------

The representative competitive firm regards :math:`\{p_t\}_{t=0}^\infty` as an exogenous stochastic process and chooses an output plan to maximize

.. math::
  E_0 \sum_{t=0}^\infty \beta^t \left\{ p_t q_t - \sigma_t \right\}, \quad \beta \in(0,1)
  :label: oli3

subject to :math:`q_0` given, where :math:`E_t` is the mathematical expectation based on time :math:`t` information. Let :math:`i_t = q_{t+1} - q_t.` We regard :math:`i_t` as the representative firm's control at :math:`t`. The first-order conditions for maximizing :eq:`oli3` are

.. math::
  i_t =  E_t  \beta i_{t+1} -c^{-1} \beta h  q_{t+1} + c^{-1} \beta  E_t( p_{t+1} -d)
  :label: oli4

for :math:`t \geq 0`. We appeal to the certainty equivalence principle stated on page XXXXXXX to justify working with a non-stochastic version of :eq:`oli4` formed by dropping the expectation operator and the random term :math:`\check \epsilon_{t+1}` from :eq:`oli2`. We use a method of Sargent (1979) and Townsend (1983) [#f9]_. We shift :eq:`oli1` forward one period, replace conditional expectations with realized values, use :eq:`oli1` to substitute for :math:`p_{t+1}` in :eq:`oli4`, and set :math:`q_t = \overline q_t` for all :math:`t\geq 0` to get

.. TODO: Fill in the links given the placeholder XXXXXXX above.

.. math::
  i_t = \beta i_{t+1}  - c^{-1} \beta h \overline q_{t+1} + c^{-1} \beta (A_0-d) - c^{-1} \beta    A_1 \overline q_{t+1} -  c^{-1} \beta    A_1 Q_{t+1} + c^{-1} \beta    v_{t+1}.
  :label: oli5

Given sufficiently stable sequences :math:`\{Q_t, v_t\}`, we could solve :eq:`oli5` and :math:`i_t = \overline q_{t+1} - \overline q_t` to express the competitive fringe's output sequence as a function of the (tail of the) monopolist's output sequence. The dependence of :math:`i_t` on future :math:`Q_t`\ 's opens an avenue for the monopolist to influence current outcomes by its choice now of its future actions. It is this feature that makes the monopolist's problem fail to be recursive in the natural state variables :math:`\overline q, Q`. The monopolist arrives at period :math:`t >0` facing the constraint that it must confirm the expectations about its time :math:`t` decision upon which the competitive fringe based its decisions at dates before :math:`t`.

The monopolist's problem
------------------------

The monopolist views the competitive firm's sequence of Euler equations as constraints on its own opportunities. They are *implementability constraints* on the monopolist's choices. Including the implementability constraints , we can represent the constraints in terms of the transition law impinging on the monopolist:

.. math::
  \begin{bmatrix}
  1 & 0 & 0 & 0 & 0 \\
  0 & 1 & 0 & 0 & 0 \\
  0 & 0 & 1 & 0 & 0 \\
  0 & 0 & 0 & 1 & 0 \\
  A_0 -d & 1 & - A_1 & - A_1 -h & c \end{bmatrix}
  \begin{bmatrix}  1 \\ v_{t+1} \\ Q_{t+1} \\ \overline q_{t+1} \\ i_{t+1} \end{bmatrix}
  & = \begin{bmatrix}
  1 & 0 & 0 & 0 & 0 \\
  0 & \rho & 0 & 0 & 0 \\
  0 & 0 & 1 & 0 & 0 \\
  0 & 0 & 0 & 1 & 1 \\
  0 & 0 & 0 & 0 & {c\over \beta} \end{bmatrix}
  \begin{bmatrix}  1 \\ v_t \\ Q_t \\ \overline q_t \\ i_t \end{bmatrix}
  + \begin{bmatrix}  0 \\ 0 \\ 1 \\ 0 \\ 0  \end{bmatrix} u_t
  :label: oli6

where :math:`u_t = Q_{t+1} - Q_t` is the control of the monopolist. The last row portrays the implementability constraints :eq:`oli5`. Represent :eq:`oli6` as

.. math::
	y_{t+1} = A y_t + B u_t .
	:label: oli6a

Although we have entered the competitive fringe's choice variable :math:`i_t` as a component of the "state" :math:`y_t` in the monopolist's transition law :eq:`oli6a`, :math:`i_t` is actually a "jump" variable. Nevertheless, the analysis in earlier sections of this chapter implies that the solution of the large firm's problem is encoded in the Riccati equation associated with :eq:`oli6a` as the transition law. Let's decode it.

To match our general setup, we partition :math:`y_t` as :math:`y_t' = \begin{bmatrix} z_t' &  x_t' \end{bmatrix}` where :math:`z_t' = \begin{bmatrix}  1 & v_t & Q_t & \overline q_t  \end{bmatrix}` and :math:`x_t = i_t`. The large firm's problem is

.. math::
  \max_{\{u_t, p_t, Q_{t+1}, \overline q_{t+1}, i_t\}}
  \sum_{t=0}^\infty \beta^t \left\{ p_t Q_t  - {\cal C}_t \right\}

subject to the given initial condition for :math:`z_0`, equations :eq:`oli1` and :eq:`oli5` and :math:`i_t = \overline q_{t+1} - \overline q_t`, as well as the laws of motion of the natural state variables :math:`z`. Notice that the monopolist in effect chooses the price sequence, as well as the quantity sequence of the competitive fringe, albeit subject to the restrictions imposed by the behavior of consumers, as summarized by the demand curve :eq:`oli1` and the implementability constraint :eq:`oli5` that describes the best responses  of the competitive fringe.

By substituting :eq:`oli1` into the above objective function, the monopolist's problem can be expressed as

.. math::
  \max_{\{u_t\}} \sum_{t=0}^\infty \beta^t \left\{ (A_0 - A_1 (\overline q_t + Q_t) + v_t) Q_t - eQ_t - .5gQ_t^2 - .5 c u_t^2 \right\}
  :label: oli7

subject to :eq:`oli6a`. This can be written

.. math::

   \max_{\{u_t\}}
    -  \sum_{t=0}^\infty \beta^t \left\{ y_t' R y_t +   u_t' Q u_t
      \right\}
	:label: oli9

subject to :eq:`oli6a` where

.. math::
  R =  - \begin{bmatrix}
  0 & 0 & {A_0-e \over 2} & 0 & 0 \\
  0 & 0 & {1 \over 2} & 0 & 0 \\
  {A_0-e \over 2} & {1 \over 2} & - A_1 -.5g
  & -{A_1 \over 2} & 0 \\
  0 & 0 & -{A_1 \over 2} & 0 & 0 \\
  0 & 0 & 0 & 0 & 0 \end{bmatrix}

and :math:`Q= {c \over 2}`.

Equilibrium representation
--------------------------

We can use :eq:`king11` to represent the solution of the monopolist's problem in the form:

.. math::
  \begin{bmatrix} z_{t+1} \\ \mu_{x,t+1} \end{bmatrix}
  = \begin{bmatrix} m_{11} & m_{12} \\ m_{21} & m_{22} \end{bmatrix}
  \begin{bmatrix} z_t \\ \mu_{x,t} \end{bmatrix}
  :label: oli11a

or

.. math::
  \begin{bmatrix} z_{t+1} \\ \mu_{x,t+1} \end{bmatrix}
  = m \begin{bmatrix} z_t \\ \mu_{x,t} \end{bmatrix} .
  :label: oli11

The monopolist is constrained to set :math:`\mu_{x,0} \leq 0`, but will find it optimal to set it to zero. Recall that :math:`z_t =\begin{bmatrix}  1 & v_t & Q_t & \overline q_t  \end{bmatrix}'`. Thus, :eq:`oli11` includes the equilibrium law of motion for the quantity :math:`\overline q_t` of the competitive fringe. By construction, :math:`\overline q_t` satisfies the Euler equation of the representative firm in the competitive fringe, as we elaborate in Appendix XXXXXXX.

.. TODO: Fill in the link to the appendix given the placeholder XXXXXXX above.

Numerical example
-----------------

We computed the optimal Stackelberg plan for parameter settings :math:`A_0, A_1, \rho, C_\epsilon, c, d, e, g, h,  \beta` = :math:`100, 1, .8, .2, 1,  20, 20, .2, .2, .95` [#f10]_. For these parameter values the decision rule is

.. math::
  u_t = (Q_{t+1} - Q_t) =\begin{bmatrix}  19.78 & .19 & -.64 & -.15 & -.30  \end{bmatrix}
  \begin{bmatrix} z_t \\ \mu_{xt} \end{bmatrix}
  :label: urule1

which can also be represented as

.. math::
  u_t= 0.44  u_{t-1} +
  \begin{bmatrix} 19.7827  \\  0.1885 \\   -0.6403  \\  -0.1510  \end{bmatrix}'
  z_t +
  \begin{bmatrix}  -6.9509 \\   -0.0678 \\   0.3030  \\  0.0550  \end{bmatrix}' z_{t-1} .
  :label: urule2

Note how in representation :eq:`urule1` the monopolist's decision for :math:`u_t = Q_{t+1} - Q_t` feeds back negatively on the implementation multiplier. [#f11]_

Concluding remarks
==================

This chapter is our first encounter with a class of problems in which optimal decision rules are history dependent [#f12]_. We shall confront many more such problems in chapters XXXXXXX, XXXXXXX, and XXXXXXX and shall see in various contexts how history dependence can be represented recursively by appropriately augmenting the natural state variables with counterparts to our implementability multipliers. A hint at what these counterparts are is gleaned by appropriately interpreting implementability multipliers as derivatives of value functions. In chapters XXXXXXX, XXXXXXX, and XXXXXXX, we make dynamic incentive and enforcement problems recursive by augmenting the state with continuation values of other decision makers [#f13]_.

.. TODO: Fill in the links given the placeholder XXXXXXX above.

.. _appAblkstack:

Appendix A: The stabilizing :math:`\mu_t = Py_t`
================================================

We verify that the :math:`P` associated with the stabilizing :math:`\mu_0 = P y_0` satisfies the Riccati equation associated with the Bellman equation. Substituting :math:`\mu_t = P y_t` into :eq:`olrp4` and :eq:`foc1` gives

.. math::
  (I + \beta   B   Q^{-1}   B P) y_{t+1} & = A y_t \beta A' P y_{t+1}
  & = - Ry_t + P y_t.
  :label: olrp9

A matrix inversion identity implies

.. math::
  (I + \beta   B   Q^{-1}   B' P)^{-1} = I - \beta   B (  Q + \beta B' P   B)^{-1}   B' P .
  :label: olrp10

Solving :eq:`olrp9` for :math:`y_{t+1}` gives

.. math::
	y_{t+1} = (A -   B F) y_t
	:label: olrp11

where

.. math::
	F = \beta (  Q + \beta   B' P   B)^{-1}   B' P A .
	:label: olrp12

Premultiplying :eq:`olrp11` by :math:` \beta A' P` gives

.. math::
	\beta A' P y_{t+1} = \beta (A'PA - A' P   B F) y_t.
	:label: olrp13

For the right side of :eq:`olrp13` to agree with the right side of :eq:`olrp9` for any initial value of :math:`y_0` requires that

.. math::
   P = R + \beta A'P A -\beta^2 A'P   B (  Q +  \beta   B' P B)^{-1}   B' P A.
	:label: olrp14

Equation :eq:`olrp14` is the algebraic matrix Riccati equation associated with the optimal linear regulator for the system :math:`A,   B, Q,   R`.

.. _appBblkstack:

Appendix B: Matrix linear difference equations
==============================================

This appendix generalizes some calculations from chapter XXXXXXX for solving systems of linear difference equations. Returning to system :eq:`olrp8`, let :math:`L =L^* \beta^{-.5}` and transform the system :eq:`olrp8` to

.. TODO: Fill in the link to the appendix given the placeholder XXXXXXX above.

.. math::
  L \begin{bmatrix}  y_{t+1}^*  \\ \mu_{t+1}^* \end{bmatrix}
  = N  \begin{bmatrix}  y_{t}^*  \\ \mu_t^* \end{bmatrix} ,
  :label: symplec2

where :math:`y_t^* = \beta^{t/2} y_t,  \mu_t^* = \mu_t \beta^{t/2}`. Now :math:`\lambda L - N` is a symplectic pencil [#f14]_, so that the generalized eigenvalues of :math:`L, N` occur in reciprocal pairs: if :math:`\lambda_i` is an eigenvalue, then so is :math:`\lambda_i^{-1}`.

We can use Evan Anderson's Matlab program `schurg.m` to find a stabilizing solution of system :eq:`symplec2` [#f15]_. The program computes the ordered real generalized Schur decomposition of the matrix pencil. Thus, `schurg.m` computes matrices :math:`\bar L, \bar N, V` such that :math:`\bar L` is upper triangular, :math:`\bar N` is upper block triangular, and :math:`V` is the matrix of right Schur vectors such that for some orthogonal matrix :math:`W`, the following hold:

.. math::
  W L V & =  \bar L \\
  W N V & = \bar N
  :label: schur

Let the stable eigenvalues (those less than :math:`1`) appear first. Then the stabilizing solution is

.. math::
	\mu_t^* = P y_t^*
	:label: chisoln

where

.. math::
	P = V_{21}  V_{11}^{-1},

:math:`V_{21}` is the lower left block of :math:`V`, and :math:`V_{11}` is the upper left block.

If :math:`L` is nonsingular, we can represent the solution of the system as [#f16]_

.. math::
  \begin{bmatrix} y_{t+1}^* \\ \mu_{t+1}^* \end{bmatrix}
  = L^{-1} N \begin{bmatrix} I \\ P \end{bmatrix} y_t^*.
  :label: Zsoln

The solution is to be initialized from :eq:`chisoln`. We can use the first half and then the second half of the rows of this representation to deduce the following recursive solutions for :math:`y_{t+1}^*` and :math:`\mu_{t+1}^*`:

.. math::
  y_{t+1}^* &  = A_o^{*} y_t^*  \\
  \mu_{t+1}^* & =   \psi^* y_t^*.
  :label: solnprelim

Now express this solution in terms of the original variables:

.. math::
  y_{t+1} &  = A_o y_t  \\
  \mu_{t+1} & =   \psi y_t
  :label: soln

where :math:`A_o = A_o^{*}\beta^{-.5}, \psi = \psi^* \beta^{-.5}`. We also have the representation

.. math::
	\mu_t = P y_t .
	:label: chicontemp

The matrix :math:`A_o = A -   B F`, where :math:`F` is the matrix for the optimal decision rule.

.. _appCblkstack:

Appendix C: Forecasting formulas
================================

The decision rule for the competitive fringe incorporates forecasts of future prices from :eq:`oli11` under :math:`m`. Thus, the representative competitive firm uses equation :eq:`oli11` to forecast future values of :math:`(Q_t, q_t)` in order to forecast :math:`p_t`. The representative competitive firm's forecasts are generated from the :math:`j` th iterate of  :eq:`oli11` [#f17]_:

.. math::
  \begin{bmatrix} z_{t+j} \\ \mu_{x,t+j} \end{bmatrix}
  = m^j
  \begin{bmatrix} z_t \\ \mu_{x,t} \end{bmatrix} .
  :label: oli12

The following calculation verifies that the representative firm forecasts by iterating the law of motion associated with :math:`m`. Write the Euler equation for :math:`i_t` :eq:`oli4` in terms of a polynomial in the lag operator :math:`L` and factor it: :math:`(1 - (\beta^{-1} + (1+c^{-1}h))L + \beta^{-1} L^2) = -(\beta \lambda)^{-1} L (1 - \beta \lambda L^{-1})(1-\lambda L)` where :math:`\lambda \in (0,1)` and :math:`\lambda =1` when :math:`h =0` [#f18]_.

By taking the nonstochastic version of :eq:`oli4` and solving an unstable root forward and a stable root backward using the technique of Sargent (1979 or 1987a, chap. IX), we obtain

.. math::
   i_t  =  (\lambda-1)q_t +  c^{-1}   \sum_{j=1}^\infty ( \beta \lambda)^j p_{t+j},
	:label: oli4a

or

.. math::
  i_t = (\lambda -1) q_t + c^{-1} \sum_{j=1}^\infty (  \beta \lambda)^j [(A_0-d) - A_1 (Q_{t+j} + q_{t+j}) + v_{t+j}] ,
  :label: oli4b

This can be expressed as

.. math::
  i_t =(\lambda -1) q_t + c^{-1} e_p \beta \lambda m (I - \beta \lambda m)^{-1}
  \begin{bmatrix} z_t \\ \mu_{xt}\end{bmatrix}
  :label: oli4c

where :math:`e_p = \begin{bmatrix}  (A_0 -d ) & 1 & - A_1 & -A_1 & 0 \end{bmatrix}` is a vector that forms :math:`p_t -d` upon postmultiplication by :math:`\begin{bmatrix} z_t \\ \mu_{xt}\end{bmatrix}`. It can be verified that the solution procedure builds in :eq:`oli4c` as an identity, so that :eq:`oli4c` agrees with

.. math::
  i_t = - P_{22}^{-1} P_{21} z_t + P_{22}^{-1} \mu_{xt}.
  :label: oli4d

Exercises
=========

Exercise 1
----------

There is no uncertainty. For :math:`t \geq 0`, a monetary authority sets the growth of the (log) of money according to

.. math::
	m_{t+1} = m_t + u_t
  :label: ex1a

subject to the initial condition :math:`m_0>0` given. The demand for money is

.. math::
	m_t - p_t = - \alpha (p_{t+1} - p_t), \alpha > 0
  :label: ex1b

where :math:`p_t` is the log of the price level. :eq:`ex1a` can be interpreted as the Euler equation of the holders of money.

**a.** Briefly interpret how :eq:`ex1a` makes the demand for real balances vary inversely with the expected rate of inflation. Temporarily (only for this part of the exercise) drop :eq:`ex1a` and assume instead that :math:`\{m_t\}` is a given sequence satisfying :math:`\sum_{t=0}^\infty m_t^2 < + \infty`. Please solve the difference :eq:`ex1a` "forward" to express :math:`p_t` as a function of current and future values of :math:`m_s`. Note how future values of :math:`m` influence the current price level.

At time :math:`0`, a monetary authority chooses a possibly history-dependent strategy for setting :math:`\{u_t\}_{t=0}^\infty`. (The monetary authority commits to this strategy.) The monetary authority orders sequences :math:`\{m_t, p_t\}_{t=0}^\infty` according to

.. math::
  - \sum_{t=0}^\infty .95^t \left[  (p_t - \overline p)^2 +
  u_t^2 + .00001 m_t^2  \right].
  :label: ex1c

Assume that :math:`m_0=10, \alpha=5, \bar p=1`.

**b.** Please briefly interpret this problem as one where the monetary authority wants to stabilize the price level, subject to costs of adjusting the money supply and some implementability constraints. (We include the term :math:`.00001m_t^2` for purely technical reasons that you need not discuss.)

**c.** Please write and run a Matlab program to find the optimal sequence :math:`\{u_t\}_{t=0}^\infty`.

**d.** Display the optimal decision rule for :math:`u_t` as a function of :math:`u_{t-1},  m_t, m_{t-1}`.

**e.** Compute the optimal :math:`\{m_t, p_t\}_t` sequence for :math:`t=0, \ldots,  10`.

.. TODO: Should Matlab be replaced with Python in the preceding paragraph?

*Hint:*  The optimal :math:`\{m_t\}` sequence must satisfy :math:`\sum_{t=0}^\infty (.95)^t m_t^2 < +\infty`. You are free to apply the Matlab program `olrp.m`.

Exercise 2
----------

A representative consumer has quadratic utility functional

.. math::
	\sum_{t=0}^\infty \beta^t \left\{ -.5 (b -c_t)^2 \right\}
  :label: ex2a

where :math:`\beta \in (0,1)`, :math:`b = 30`, and :math:`c_t` is time :math:`t` consumption. The consumer faces a sequence of budget constraints

.. math::
	c_t + a_{t+1} = (1+r)a_t + y_t - \tau_t
  :label: ex2b

where :math:`a_t` is the household's holdings of an asset at the beginning of :math:`t`, :math:`r >0` is a constant net interest rate satisfying :math:`\beta (1+r) <1`, and :math:`y_t` is the consumer's endowment at :math:`t`. The consumer's plan for :math:`(c_t, a_{t+1})` has to obey the boundary condition :math:`\sum_{t=0}^\infty \beta^t a_t^2 < + \infty`. Assume that :math:`y_0, a_0` are given initial conditions and that :math:`y_t` obeys

.. math::
	y_t = \rho y_{t-1}, \quad t \geq 1,
  :label: ex2c

where :math:`|\rho| <1`. Assume that :math:`a_0=0`, :math:`y_0=3`, and :math:`\rho=.9`.

At time :math:`0`, a planner commits to a plan for taxes :math:`\{\tau_t\}_{t=0}^\infty`. The planner designs the plan to maximize

.. math::
  \sum_{t=0}^\infty \beta^t \left\{ -.5 (c_t-b)^2 -   \tau_t^2\right\}
  :label: ex2d

over :math:`\{c_t, \tau_t\}_{t=0}^\infty` subject to the implementability constraints in :eq:ex2b` for :math:`t \geq 0` and

.. math::
	\lambda_t =  \beta (1+r) \lambda_{t+1}
  :label: ex2e

for :math:`t\geq 0`, where :math:`\lambda_t \equiv (b-c_t)`.

**a.** Argue that :eq:`ex2e` is the Euler equation for a consumer who maximizes :eq:`ex2a` subject to :eq:`ex2b`, taking :math:`\{\tau_t\}` as a given sequence.

**b.** Formulate the planner's problem as a Stackelberg problem.

**c.** For :math:`\beta=.95, b=30, \beta(1+r)=.95`, formulate an artificial optimal linear regulator problem and use it to solve the Stackelberg problem.

**d.** Give a recursive representation of the Stackelberg plan for :math:`\tau_t`.


.. rubric:: Footnotes

.. [#f1] The problem assumes that there are no cross products between states and controls in the return function.  There is a simple transformation that converts a problem whose return function has cross products into an equivalent problem that has no cross products. For example, see Hansen and Sargent (2008, chapter 4, pp. 72-73).

.. [#f2] The government would make different choices were it to choose sequentially, that is,  were it to select its time :math:`t` action at time :math`t`.

.. [#f3] In step 4, we acknowledge that the :math:`x_0` component is *not* given but is to be chosen by the Stackelberg leader.

.. [#f4] This argument just adapts one in Pearlman (1992). The Lagrangian associated with the Stackelberg problem remains :eq:`olrp3`, which means that the same  section XXXXXXX logic implies that the stabilizing solution must satisfy :eq:`king4`. It is only  in how we impose :eq:`king4` that the solution diverges from that for the linear regulator.

.. [#f5] When a random shock $C \epsilon_{t+1}$ is present, we must add :math:`\begin{bmatrix} I & 0 \\  P_{21} & P_{22} \end{bmatrix} C \epsilon_{t+1}` to the right side of  :eq:`king11`.

.. [#f6] Peter Von Zur Muehlen suggested this representation to us.

.. [#f7] The existence of a Stackelberg plan is not at issue because we know how to construct one using the method in the text.

.. [#f8] Hansen and Sargent (2008, ch.~16) use this model as a laboratory to illustrate an equilibrium concept featuring robustness in which at least one of the agents has doubts about the stochastic specification of the demand shock process.

.. [#f9] They used this method to compute a rational expectations competitive equilibrium.  The  key step was to eliminate price and output by substituting from the inverse demand curve and the production function into the firm's first-order conditions to get a difference equation in capital.

.. [#f10] These calculations were performed by the Matlab program `oligopoly5.m`

.. [#f11] We also computed impulse responses to the demand innovation :math:`\epsilon_t`. The impulse responses show that a demand innovation pushes the implementation multiplier down and leads the monopolist to expand output while the representative competitive firm contracts output in subsequent periods.  The response of price to a demand shock innovation is to rise on impact but then to decrease in subsequent periods in response to the increase in total supply :math:`\overline q+Q` engineered by the monopolist.

.. [#f12] For another application of the techniques in this chapter and how they related to the method recommended by Kydland and Prescott (1980), see Evans and Sargent (2013).

.. [#f13] In chapter XXXXXXX, we describe Marcet and Marimon's (1992, 1999) method of constructing recursive contracts, which  is closely related to the method that we have presented in this chapter.

.. [#f14] A {\it pencil\/} :math`\lambda L - N` is the family of matrices indexed by the complex variable :math:`\lambda`.  A pencil is *symplectic* if :math:`L J L' = N J N'`, where :math:`J = \begin{bmatrix} 0 & - I \\ I & 0 \end{bmatrix}`. See Anderson, Hansen, McGratten, and Sargent (1996).

.. [#f15] This program is available at `http://www.math.niu.edu/~anderson/ <http://www.math.niu.edu/~anderson/>`_.

.. [#f16] The solution method in the text assumes that :math:`L` is nonsingular and well conditioned.  If it is not, the following method proposed by Evan Anderson will work. We want to solve for a solution of the form :math:`y_{t+1}^* = A_o^{*} y_t^*`. Note that with :`, :math:`L [I; P] y_{t+1}^* = N [I; P] y_t^*` The solution :math:`A_o^{*}` will then  satisfy :math:`L [I; P] A_o^{*} = N [ I;P]`. Thus :math:`A^{o*}` can be computed via the Matlab command :math:`A_o^{*} = (L* [I; P]) \backslash (N* [ I;P])`

.. [#f17] The representative firm  acts as though :math:`(q_t, Q_t)` were exogenous to it.

.. [#f18] See Sargent (1979 or 1987a) for an account of the method we are using here.

.. TODO: in f4, f13 we need to fill in section link given placeholder XXXXXX


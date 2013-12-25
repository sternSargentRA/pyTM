.. role:: math(raw)
   :format: html latex
..

Dynamic Stackelberg Problems

History dependence
==================

Previous chapters described decision problems that are recursive in what
we can call “natural” state variables, i.e., state variables that
describe stocks of capital, wealth, and information that helps forecast
future values of prices and quantities that impinge on future utilities
or profits. In problems that are recursive in the natural state
variables, optimal decision rules are functions of the natural state
variables.

 This chapter is our first encounter with a class of problems that are
not recursive in the natural state variables. Kydland and Prescott
(1977), Prescott (1977), and Calvo (1978) gave macroeconomic examples of
decision problems whose solutions exhibited *time inconsistency* because
they are not recursive in the natural state variables. Those authors
studied the decision problem of a large agent (a government) that
confronts a competitive market composed of many small private agents
whose decisions are influenced by their *forecasts* of the government’s
future actions. In such settings, the natural state variables of private
agents at time :math:`t` are partly shaped by past decisions that were
influenced by their earlier forecasts of the government’s action at time
:math:`t`. In a rational expectations equilibrium, the government on
average confirms private agents’ earlier forecasts of the government’s
time :math:`t` actions. This requirement to confirm prior forecasts puts
constraints on the government’s time :math:`t` decisions that prevent
its problem from being recursive in natural state variables. These
additional constraints make the government’s decision rule at :math:`t`
depend on the entire history of the state from time :math:`0` to time
:math:`t`.

 It took some time for economists to figure out how to formulate policy
problems of this type recursively. Prescott (1977) asserted that
recursive optimal control theory does not apply to problems with this
structure. This chapter and chapters and show how Prescott’s pessimism
about the inapplicability of optimal control theory has been overturned
by more recent work. An important finding is that if the natural state
variables are augmented with additional state variables that measure
costs in terms of the government’s *current* continuation value of
confirming *past* private sector expectations about its current
behavior, this class of problems can be made recursive. This fact
affords immense computational advantages and yields substantial
insights. This chapter displays these within the tractable framework of
linear quadratic problems.

The Stackelberg problem
=======================

To exhibit the essential structure of the problems that concerned
Kydland and Prescott (1977) and Calvo (1979), this chapter uses the
optimal linear regulator to solve a linear quadratic version of what is
known as a dynamic Stackelberg problem. For now we refer to the
Stackelberg leader as the government and the Stackelberg follower as the
representative agent or private sector. Soon we’ll give an application
with another interpretation of these two players.

Let :math:`z_t` be an :math:`n_z \times 1` vector of natural state
variables, :math:`x_t` an :math:`n_x \times 1` vector of endogenous
variables free to jump at :math:`t`, and :math:`u_t` a vector of
government instruments. The :math:`z_t` vector is inherited from the
past. But :math:`x_t` is *not* inherited from the past. The model
determines the “jump variables” :math:`x_t` at time :math:`t`. Included
in :math:`x_t` are prices and quantities that adjust instantaneously to
clear markets at time :math:`t`. Let
:math:` y_t = \left[\matrix{z_t \cr x_t \cr} \right]`. Define the
government’s one-period loss function

.. math:: r(y, u)  =  y' R y  + u' Q u . \EQN target

Subject to an initial condition for :math:`z_0`, but not for
:math:`x_0`, a government wants to maximize

.. math:: -  \sum_{t=0}^\infty \beta^t r(y_t, u_t).  \EQN new1

 The government makes policy in light of the model

.. math::

   \left[\matrix{I & 0 \cr
                    G_{21} & G_{22} \cr}\right]
       \left[ \matrix{   z_{t+1} \cr  x_{t+1} \cr} \right]
     = \left[ \matrix{ \hat A_{11}  &  \hat A_{12} \cr
                       \hat A_{21} & \hat A_{22}  \cr} \right]
   \left[\matrix{ z_t \cr x_t \cr} \right]
       + \hat B u_t   . \EQN new2

 We assume that the matrix on the left is invertible, so that we can
multiply both sides of the above equation by its inverse to obtain

.. math::

   \left[ \matrix{   z_{t+1} \cr  x_{t+1} \cr} \right]
     = \left[ \matrix{ A_{11}  &   A_{12} \cr
                        A_{21} &  A_{22}  \cr} \right]
      \left[\matrix{ z_t \cr x_t \cr} \right]
       +  B u_t   \EQN new3

 or

.. math:: y_{t+1} = A y_t + B u_t  . \EQN new30

 The government maximizes by choosing sequences
:math:`\{u_t, x_t, z_{t+1}\}_{t=0}^\infty` subject to and the initial
condition for :math:`z_0`.

The private sector’s behavior is summarized by the second block of
equations of or . These typically include the first-order conditions of
private agents’ optimization problem (i.e., their Euler equations). They
summarize the forward-looking aspect of private agents’ behavior. We
shall provide an example later in this chapter in which, as is typical
of these problems, the last :math:`n_x` equations of or constitute
*implementability constraints* that are formed by the Euler equations of
a competitive fringe or private sector. When combined with a stability
condition to be imposed below, these Euler equations summarize the
private sector’s best response to the sequence of actions by the
government.

The certainty equivalence principle stated in chapter allows us to work
with a nonstochastic model. We would attain the same decision rule if we
were to replace :math:`x_{t+1}` with the forecast :math:`E_t x_{t+1}`
and to add a shock process :math:`C \epsilon_{t+1}` to the right side of
, where :math:`\epsilon_{t+1}` is an i.i.d. random vector with mean of
zero and identity covariance matrix.

Let :math:`X^t` denote the history of any variable :math:`X` from
:math:`0` to :math:`t`. Miller and Salmon (1982, 1985), Hansen, Epple,
and Roberds (1985), Pearlman, Currie, and Levine (1986), Sargent (1987),
Pearlman (1992), and others have all studied versions of the following
problem: The *Stackelberg problem* is to maximize by choosing an
:math:`x_0` and a sequence of decision rules, the time :math:`t`
component of which maps the time :math:`t` history of the state
:math:`z^t` into the time :math:`t` decision :math:`u_t` of the
Stackelberg leader. The Stackelberg leader commits to this sequence of
decision rules at time :math:`0`. The maximization is subject to a given
initial condition for :math:`z_0`. But :math:`x_0` is among the objects
to be chosen by the Stackelberg leader.

The optimal decision rule is history dependent, meaning that :math:`u_t`
depends not only on :math:`z_t` but also on lags of :math:`z`. History
dependence has two sources: (a) the government’s ability to commit to a
sequence of rules at time :math:`0`, and (b) the forward-looking
behavior of the private sector embedded in the second block of equations
. The history dependence of the government’s plan is expressed in the
dynamics of Lagrange multipliers :math:`\mu_x` on the last :math:`n_x`
equations of or . These multipliers measure the costs today of honoring
past government promises about current and future settings of :math:`u`.
It is appropriate to initialize the multipliers to zero at time
:math:`t=0`, because then there are no past promises about :math:`u` to
honor. But the multipliers :math:`\mu_x` take nonzero values thereafter,
reflecting future costs to the government of adhering to its commitment.

Solving the Stackelberg problem
===============================

This section describes a remarkable four-step algorithm for solving the
Stackelberg problem.

Step 1: solve an optimal linear regulator
-----------------------------------------

Step 1 seems to disregard the forward-looking aspect of the problem
(step 3 will take account of that). If we temporarily ignore the fact
that the :math:`x_0` component of the state
:math:`y_0 = \left[\matrix{z_0 \cr x_0\cr}\right]` is *not* actually
part of the true state vector, then superficially the Stackelberg
problem , has the form of an optimal linear regulator problem. It can be
solved by forming a Bellman equation and iterating until it converges.
The optimal value function has the form :math:`v(y) = - y' P y`, where
:math:`P` satisfies the Riccati equation . The next steps note how the
value function :math:`v(y) = -y'Py` encodes objects that solve the
Stackelberg problem, then tell how to decode them.

A reader not wanting to be reminded of the details of the Bellman
equation can now move directly to step 2. For those wanting a reminder,
here it is. The linear regulator is

.. math::

   v(y_0) = -y_0' P y_0
   = {\rm max}_{\{  u_t, y_{t+1}\}_{t=0}^\infty} - \sum_{t=0}^\infty \beta^t
     \left( y_t' R y_t +   u_t'   Q   u_t \right) \EQN olrp1a

 where the maximization is subject to a fixed initial condition for
:math:`y_0` and the law of motion

.. math:: y_{t+1} = A y_t +   B   u_t . \EQN new30a

 Associated with problem , is the Bellman equation

.. math::

   - y' P y = {\rm max}_{  u, y^*} \left\{ -  y' R y -   u'Q
        u - \beta y^{* \prime} P y^* \right\} \EQN bell1

 where the maximization is subject to

.. math:: y^* = A y + B   u  \EQN bell2

 where :math:`y^*` denotes next period’s value of the state. Problem ,
gives rise to the matrix Riccati equation

.. math::

   P = R + \beta A' P A - \beta^2 A' P   B (  Q
     + \beta   B' P   B)^{-1}   B' P A  \EQN bell3

 and the formula for :math:`F` in the decision rule
:math:`  u_t = - F y_t`

.. math::

   F = \beta(   Q + \beta   B' P   B)^{-1}
       B' P A .  \EQN bell4

 Thus, we can solve problem , by iterating to convergence on the
difference equation counterpart to the algebraic Riccati equation , or
by using a faster computational method that emerges as a by-product in
step 2. This method is described in Appendix .

Step 2: use the stabilizing properties of shadow price :math:`P y_t`
--------------------------------------------------------------------

At this point, we decode the information in the matrix :math:`P` in
terms of shadow prices that are associated with a Lagrangian. We adapt a
method described earlier in section that solves a linear quadratic
control problem of the form , by attaching a sequence of Lagrange
multipliers :math:` 2 \beta^{t+1} \mu_{t+1}` to the sequence of
constraints and then forming the Lagrangian:

.. math::

   {\cal L} = - \sum_{t=0}^\infty  \beta^t \left[ y_t' R  y_t + u_t' Q u_t
      + 2  \beta \mu_{t+1}'(A y_t + B u_t  - y_{t+1})
       \right]. \EQN olrp3

 For the Stackelberg problem, it is important to partition :math:`\mu_t`
conformably with our partition of :math:`y_t=\left[\matrix{z_t \cr
   x_t \cr}\right]`, so that
:math:` \mu_t = \left[\matrix{ \mu_{zt} \cr \mu_{xt} \cr} \right],`
where :math:`\mu_{xt}` is an :math:`n_x \times 1 ` vector of multipliers
adhering to the implementability constraints. For now, we can ignore the
partitioning of :math:`\mu_t`, but it will be very important when we
turn our attention to the specific requirements of the Stackelberg
problem in step 3.

We want to maximize with respect to sequences for :math:`u_t` and
:math:`y_{t+1}`. The first-order conditions with respect to
:math:`u_t, y_t`, respectively, are:

.. math::

   \EQNalign{  0 & = Q u_t + \beta B' \mu_{t+1} \EQN foc1;a  \cr
                \mu_t & = R y_t + \beta A' \mu_{t+1}. \EQN foc1;b \cr}

 Solving for :math:`u_t` and substituting into gives

.. math:: y_{t+1} = A y_t - \beta B Q^{-1} B'  \mu_{t+1}. \EQN olrp4

 We can represent the system formed by and as

.. math::

   \left[\matrix{I & \beta   B   Q^{-1}   B' \cr
                   0 & \beta A' \cr}\right] \left[\matrix{y_{t+1} \cr \mu_{t+1} \cr}
                \right]
    = \left[\matrix{A & 0 \cr
                    - R & I \cr} \right]
     \left[\matrix{y_t \cr \mu_t \cr}\right] \EQN olrp7

 or

.. math::

   L^* \left[\matrix{y_{t+1} \cr \mu_{t+1} \cr}
                \right]
    =  N
     \left[\matrix{y_t \cr \mu_t \cr}\right]. \EQN olrp8

 We seek a “stabilizing” solution of , i.e., one that satisfies

.. math:: \sum_{t=0}^\infty  \beta^t y_t' y_t < +\infty .

Stabilizing solution
--------------------

By the same argument used in section of chapter , a stabilizing solution
satisfies :math:`\mu_0 = P y_0`, where :math:`P` solves the matrix
Riccati equation . The solution for :math:`\mu_0` replicates itself over
time in the sense that

.. math:: \mu_t = P y_t . \EQN king4

 Appendix verifies that the matrix :math:`P` that satisfies the Riccati
equation is the same :math:`P` that defines the stabilizing initial
conditions :math:`(y_0, P y_0)`. In Appendix , we describe how to
construct :math:`P` by computing generalized eigenvalues and
eigenvectors.

Step 3: convert implementation multipliers into state variables
---------------------------------------------------------------

Key insight
~~~~~~~~~~~

We now confront the fact that the :math:`x_0` component of :math:`y_0`
consists of variables that are not state variables, i.e., they are not
inherited from the past but are to be determined at time :math:`t`. In
the optimal linear regulator problem, :math:`y_0` is a state vector
inherited from the past; the multiplier :math:`\mu_0` jumps at :math:`t`
to satisfy :math:`\mu_0 = P y_0` and thereby stabilize the system. But
in the Stackelberg problem, pertinent components of *both* :math:`y_0`
*and* :math:`\mu_0` must adjust to satisfy :math:`\mu_0 = P y_0`. In
particular, partition :math:`\mu_t` conformably with the partition of
:math:`y_t` into :math:`\left[\matrix{z_t' &  x_t' \cr} \right]'`:

.. math:: \mu_t = \left[\matrix{ \mu_{zt} \cr \mu_{xt} \cr} \right].

 For the Stackelberg problem, the first :math:`n_z` elements of
:math:`y_t` are predetermined but the remaining components are free. And
while the first :math:`n_z` elements of :math:`\mu_t` are free to jump
at :math:`t`, the remaining components are not. The third step completes
the solution of the Stackelberg problem by acknowledging these facts.
*After* we have performed the key step of computing the matrix :math:`P`
that solves the Riccati equation , we convert the last :math:`n_x`
Lagrange multipliers :math:`\mu_{xt}` into state variables by using the
following procedure

Write the last :math:`n_x` equations of as

.. math:: \mu_{xt} = P_{21} z_t + P_{22} x_t, \EQN king5

 where the partitioning of :math:`P` is conformable with that of
:math:`y_t` into :math:`\left[ \matrix{z_t &  x_t \cr}\right]'`. The
vector :math:`\mu_{xt}` becomes part of the state at :math:`t`, while
:math:`x_t` is free to jump at :math:`t`. Therefore, we solve for
:math:`x_t` in terms of :math:`(z_t, \mu_{xt})`:

.. math:: x_t = - P_{22}^{-1} P_{21} z_t + P_{22}^{-1} \mu_{xt}. \EQN king6

 Then we can write

.. math::

   y_t =\left[\matrix{z_t \cr x_t \cr}\right]  = \left[ \matrix{I & 0 \cr
              - P_{22}^{-1} P_{21} &  P_{22}^{-1} \cr}  \right]
       \left[\matrix{z_t \cr \mu_{xt} \cr}\right] \EQN king7

 and from

.. math::

   \mu_{xt} =  \left[\matrix{ P_{21} & P_{22} \cr}
   \right] y_t . \EQN king8

With these modifications, the key formulas and from the optimal linear
regulator for :math:`F` and :math:`P`, respectively, continue to apply.
Using , the optimal decision rule is

.. math::

   u_t    = -F
    \left[ \matrix{I & 0 \cr
              - P_{22}^{-1} P_{21} &  P_{22}^{-1} \cr}  \right]
       \left[\matrix{z_t \cr \mu_{xt} \cr}\right]. \EQN king10

 Then we have the following complete description of the Stackelberg
plan: \ 

.. math::

   \EQNalign{ \left[ \matrix{ z_{t+1} \cr \mu_{x,t+1} \cr} \right]
     & = \left[ \matrix{I & 0 \cr P_{21} & P_{22}\cr} \right]
     (A - B F)
            \left[\matrix{ I & 0 \cr
                 - P_{22}^{-1} P_{21} & P_{22}^{-1} \cr}\right]
       \left[\matrix{ z_t \cr \mu_{xt} \cr} \right] \hskip1cm \EQN king11;a \cr
      x_t & = \left[\matrix{ - P_{22}^{-1} P_{21}   & P_{22}^{-1} \cr}
     \right]
       \left[\matrix{ z_t \cr \mu_{xt} \cr} \right] .  \EQN king11;b \cr}

 The difference equation is to be initialized from the given value of
:math:`z_0` and a value for :math:`\mu_{x0}` to be determined in step 4.

Step 4: solve for :math:`x_0` and :math:`\mu_{x0}`
--------------------------------------------------

The value function :math:`V(y_0)` satisfies

.. math:: V(y_0) = - z_0 ' P_{11} z_0 - 2 x_0' P_{21} z_0 - x_0' P_{22} x_0 . \EQN valuefny

 Now choose :math:`x_0` by equating to zero the gradient of
:math:`V(y_0)` with respect to :math:`x_0`:

.. math:: - 2 P_{21} z_0 - 2 P_{22} x_0 =0,

 which by virtue of is equivalent with

.. math:: \mu_{x0} = 0 . \EQN mu0condition

 Then we can compute :math:`x_0` from to arrive at

.. math:: x_0 = - P_{22}^{-1} P_{21} z_0. \EQN king6x0

The Lagrange multiplier :math:`\mu_{xt}` measures the cost to the
Stackelberg leader at :math:`t \geq 0` of confirming expectations about
its time :math:`t` action that the followers had held at dates
:math:`s < t`. Setting :math:`\mu_{x0}=0` means that at time :math:`0`
there are no such prior expectations to confirm.

Summary
-------

In summary, we solve the Stackelberg problem by formulating a particular
optimal linear regulator, solving the associated matrix Riccati equation
for :math:`P`, computing :math:`F`, and then partitioning :math:`P` to
obtain representation .

History-dependent representation of decision rule
-------------------------------------------------

 For some purposes, it is useful to eliminate the implementation
multipliers :math:`\mu_{xt}` and to express the decision rule for
:math:`u_t` as a function of :math:`z_t, z_{t-1},` and :math:`u_{t-1}`.
This can be accomplished as follows. First represent compactly as

.. math::

   \left[ \matrix{ z_{t+1} \cr \mu_{x,t+1} \cr} \right]
      = \left[ \matrix{m_{11} & m_{12} \cr m_{21} & m_{22}\cr} \right]
       \left[\matrix{ z_t \cr \mu_{xt} \cr} \right] \EQN vonzer1

 and write the feedback rule for :math:`u_t`

.. math:: u_t  = f_{11}  z_{t} + f_{12} \mu_{xt} . \EQN vonzer2

 Then where :math:`f_{12}^{-1}` denotes the generalized inverse of
:math:`f_{12}`, implies
:math:`\mu_{x,t} = f_{12}^{-1}(u_t - f_{11}z_t)`. Equate the right side
of this expression to the right side of the second line of lagged once
and rearrange by using lagged once to eliminate :math:`\mu_{x,t-1}` to
get

.. math::

   u_t =  f_{12} m_{22} f_{12}^{-1} u_{t-1} + f_{11} z_t
      + f_{12}(m_{21} - m_{22} f_{12}^{-1} f_{11}) z_{t-1}
      \EQN vonzer3;a

 or

.. math:: u_t = \rho u_{t-1} + \alpha_0 z_t + \alpha_1 z_{t-1} \EQN vonzer3;b

 for :math:`t \geq 1`. For :math:`t=0`, the initialization
:math:`\mu_{x,0}=0` implies that

.. math:: u_0 = f_{11} z_0. \EQN vonzer3;c

By making the instrument feed back on itself, the form of potentially
allows for “instrument-smoothing” to emerge as an optimal rule under
commitment.

Digression on determinacy of equilibrium
----------------------------------------

Appendix describes methods for solving a system of difference equations
of the form or with an arbitrary feedback rule that expresses the
decision rule for :math:`u_t` as a function of current and previous
values of :math:`y_t` and perhaps previous values of itself. The
difference equation system has a unique solution satisfying the
stability condition :math:`\sum_{t=0}^\infty \beta^t y_t \cdot  y_t` if
the eigenvalues of the matrix split, with half being greater than unity
and half being less than unity in modulus. If more than half are less
than unity in modulus, the equilibrium is said to be indeterminate in
the sense that there are multiple equilibria starting from any initial
condition.

If we choose to represent the solution of a Stackelberg or Ramsey
problem in the form , we can substitute that representation for
:math:`u_t` into , obtain a difference equation system in
:math:`y_t, u_t`, and ask whether the resulting system is determinate.
To answer this question, we would use the method of Appendix , form
system , then check whether the generalized eigenvalues split as
required. Researchers have used this method to study the determinacy of
equilibria under Stackelberg plans with representations like and have
discovered that sometimes an equilibrium can be indeterminate. See Evans
and Honkapohja (2003) for a discussion of determinacy of equilibria
under commitment in a class of equilibrium monetary models and how
determinacy depends on how the decision rule of the Stackelberg leader
is represented. Evans and Honkapohja argue that casting a government
decision rule in a way that leads to indeterminacy is a bad idea.

A large firm with a competitive fringe
======================================

As an example, this section studies the equilibrium of an industry with
a large firm that acts as a Stackelberg leader with respect to a
competitive fringe. Sometimes the large firm is called ‘the monopolist’
even though there are actually many firms in the industry. The industry
produces a single nonstorable homogeneous good. One large firm produces
:math:`Q_t` and a representative firm in a competitive fringe produces
:math:`q_t`. The representative firm in the competitive fringe acts as a
price taker and chooses sequentially. The large firm commits to a policy
at time :math:`0`, taking into account its ability to manipulate the
price sequence, both directly through the effects of its quantity
choices on prices, and indirectly through the responses of the
competitive fringe to its forecasts of prices.

The costs of production are
:math:`{\cal C}_t = e Q_t + .5 g Q_t^2+ .5 c (Q_{t+1} - Q_{t})^2 ` for
the large firm and
:math:` \sigma_t= d q_t + .5 h q_t^2 + .5 c (q_{t+1} - q_t)^2` for the
competitive firm, where :math:`d>0, e >0, c>0, g >0, h>0 ` are cost
parameters. There is a linear inverse demand curve

.. math:: p_t = A_0 - A_1 (Q_t + \overline q_t) + v_t, \EQN oli1

 where :math:`A_0, A_1` are both positive and :math:`v_t` is a
disturbance to demand governed by

.. math:: v_{t+1}= \rho v_t + C_\epsilon \check \epsilon_{t+1} \EQN oli2

 and where :math:` | \rho | < 1` and :math:`\check \epsilon_{t+1}` is an
i.i.d.sequence of random variables with mean zero and variance
:math:`1`. In , :math:`\overline q_t` is equilibrium output of the
representative competitive firm. In equilibrium,
:math:`\overline q_t = q_t`, but we must distinguish between :math:`q_t`
and :math:`\overline q_t` in posing the optimum problem of a competitive
firm.

The competitive fringe
----------------------

The representative competitive firm regards :math:`\{p_t\}_{t=0}^\infty`
as an exogenous stochastic process and chooses an output plan to
maximize

.. math::

   E_0 \sum_{t=0}^\infty \beta^t \left\{
    p_t q_t - \sigma_t
    \right\}, \quad \beta \in(0,1) \EQN oli3

 subject to :math:`q_0` given, where :math:`E_t` is the mathematical
expectation based on time :math:`t` information. Let
:math:`i_t = q_{t+1} - q_t.` We regard :math:`i_t` as the representative
firm’s control at :math:`t`. The first-order conditions for maximizing
are

.. math::

   i_t =  E_t  \beta i_{t+1} -c^{-1} \beta h  q_{t+1}
     + c^{-1} \beta  E_t( p_{t+1} -d) \EQN oli4

 for :math:`t \geq 0`. We appeal to the certainty equivalence principle
stated on page to justify working with a non-stochastic version of
formed by dropping the expectation operator and the random term
:math:`\check \epsilon_{t+1}` from . We use a method of Sargent (1979)
and Townsend (1983). We shift forward one period, replace conditional
expectations with realized values, use to substitute for :math:`p_{t+1}`
in , and set :math:`q_t = \overline q_t` for all :math:`t\geq 0` to get

.. math::

   i_t = \beta i_{t+1}  - c^{-1} \beta h \overline q_{t+1}
    + c^{-1} \beta (A_0-d) - c^{-1} \beta    A_1 \overline q_{t+1}
     -  c^{-1} \beta    A_1 Q_{t+1} + c^{-1} \beta    v_{t+1}. \EQN oli5

 Given sufficiently stable sequences :math:`\{Q_t, v_t\}`, we could
solve and :math:`i_t = \overline q_{t+1} - \overline q_t` to express the
competitive fringe’s output sequence as a function of the (tail of the)
monopolist’s output sequence. The dependence of :math:`i_t` on future
:math:`Q_t`\ ’s opens an avenue for the monopolist to influence current
outcomes by its choice now of its future actions. It is this feature
that makes the monopolist’s problem fail to be recursive in the natural
state variables :math:`\overline q, Q`. The monopolist arrives at period
:math:`t >0` facing the constraint that it must confirm the expectations
about its time :math:`t` decision upon which the competitive fringe
based its decisions at dates before :math:`t`.

The monopolist’s problem
------------------------

The monopolist views the competitive firm’s sequence of Euler equations
as constraints on its own opportunities. They are *implementability
constraints* on the monopolist’s choices. Including the implementability
constraints , we can represent the constraints in terms of the
transition law impinging on the monopolist:

.. math::

   \eqalign{ \left[\matrix{ 1 & 0 & 0 & 0 & 0 \cr
                     0 & 1 & 0 & 0 & 0 \cr
                     0 & 0 & 1 & 0 & 0 \cr
                     0 & 0 & 0 & 1 & 0 \cr
                     A_0 -d & 1 & - A_1 & - A_1 -h & c \cr }\right]
      \left[\matrix{ 1 \cr v_{t+1} \cr Q_{t+1} \cr \overline
    q_{t+1} \cr i_{t+1} \cr}
       \right]
     & = \left[ \matrix{ 1 & 0 & 0 & 0 & 0 \cr
                0 & \rho & 0 & 0 & 0 \cr
                0 & 0 & 1 & 0 & 0 \cr
                0 & 0 & 0 & 1 & 1 \cr
                0 & 0 & 0 & 0 & {c\over \beta} \cr} \right]
        \left[ \matrix{ 1 \cr v_t \cr Q_t \cr \overline
       q_t \cr i_t \cr} \right] \cr
   & + \left[\matrix{ 0 \cr 0 \cr 1 \cr 0 \cr 0 \cr}\right] u_t
      , \cr}   \EQN oli6

 where :math:`u_t = Q_{t+1} - Q_t ` is the control of the monopolist.
The last row portrays the implementability constraints . Represent as

.. math:: y_{t+1} = A y_t + B u_t .  \EQN oli6a

Although we have entered the competitive fringe’s choice variable
:math:`i_t` as a component of the “state” :math:`y_t` in the
monopolist’s transition law , :math:`i_t` is actually a “jump” variable.
Nevertheless, the analysis in earlier sections of this chapter implies
that the solution of the large firm’s problem is encoded in the Riccati
equation associated with as the transition law. Let’s decode it.

To match our general setup, we partition :math:`y_t` as
:math:`y_t' = \left[\matrix{z_t' &  x_t' \cr} \right]` where
:math:`z_t' = \left[\matrix{ 1 & v_t & Q_t & \overline q_t \cr}\right]`
and :math:`x_t = i_t`. The large firm’s problem is

.. math::

   \max_{\{u_t, p_t, Q_{t+1}, \overline q_{t+1}, i_t\}}
    \sum_{t=0}^\infty \beta^t \left\{ p_t Q_t  - {\cal C}_t \right\}

 subject to the given initial condition for :math:`z_0`, equations and
and :math:`i_t = \overline q_{t+1} -
\overline q_t`, as well as the laws of motion of the natural state
variables :math:`z`. Notice that the monopolist in effect chooses the
price sequence, as well as the quantity sequence of the competitive
fringe, albeit subject to the restrictions imposed by the behavior of
consumers, as summarized by the demand curve and the implementability
constraint that describes the best responses of the competitive fringe.

By substituting into the above objective function, the monopolist’s
problem can be expressed as

.. math::

   \max_{\{u_t\}}
    \sum_{t=0}^\infty \beta^t
       \left\{ (A_0 - A_1 (\overline q_t + Q_t) + v_t) Q_t - eQ_t - .5gQ_t^2 -
       .5 c u_t^2
    \right\} \EQN oli7

 subject to . This can be written

.. math::

   \max_{\{u_t\}}
    -  \sum_{t=0}^\infty \beta^t \left\{ y_t' R y_t +   u_t' Q u_t
      \right\} \EQN oli9

 subject to where

.. math::

   R =  - \left[\matrix{ 0 & 0 & {A_0-e \over 2} & 0 & 0 \cr
                          0 & 0 & {1 \over 2} & 0 & 0 \cr
                          {A_0-e \over 2} & {1 \over 2} & - A_1 -.5g
                      & -{A_1 \over 2} & 0 \cr
                      0 & 0 & -{A_1 \over 2} & 0 & 0 \cr
                     0 & 0 & 0 & 0 & 0 \cr} \right]

 and :math:`Q= {c \over 2}`.

Equilibrium representation
--------------------------

We can use to represent the solution of the monopolist’s problem in the
form:

.. math::

   \left[\matrix{z_{t+1} \cr \mu_{x,t+1}\cr}\right]
      = \left[\matrix{m_{11} & m_{12} \cr
                      m_{21} & m_{22}\cr}\right]
        \left[\matrix{z_t \cr \mu_{x,t} \cr} \right]  \EQN oli11

 or

.. math::

   \left[\matrix{z_{t+1} \cr \mu_{x,t+1}\cr}\right]
      = m
        \left[\matrix{z_t \cr \mu_{x,t} \cr} \right] . \EQN oli11

 The monopolist is constrained to set :math:`\mu_{x,0} \leq 0`, but will
find it optimal to set it to zero. Recall that
:math:`z_t =\left[\matrix{ 1 & v_t & Q_t & \overline q_t \cr}\right]'`.
Thus, includes the equilibrium law of motion for the quantity
:math:`\overline q_t` of the competitive fringe. By construction,
:math:`\overline q_t` satisfies the Euler equation of the representative
firm in the competitive fringe, as we elaborate in Appendix .

Numerical example
-----------------

We computed the optimal Stackelberg plan for parameter settings
:math:`A_0, A_1, \rho, C_\epsilon,\hfil\break
  c, d, e, g, h,  \beta ` = :math:`100, 1, .8, .2, 1,  20, 20, .2, .2,
.95`. For these parameter values the decision rule is

.. math::

   u_t = (Q_{t+1} - Q_t) =\left[\matrix{ 19.78 & .19 & -.64 & -.15 & -.30 \cr}\right]
   \left[ \matrix{z_t \cr \mu_{xt}\cr}\right] \EQN urule1

 which can also be represented as

.. math::

   u_t=
       0.44  u_{t-1} +
   \left[\matrix{
      19.7827  \cr  0.1885 \cr   -0.6403  \cr  -0.1510 \cr}\right]'  z_t +
   \left[\matrix{ -6.9509 \cr   -0.0678 \cr   0.3030  \cr  0.0550 \cr}\right]'
    z_{t-1} . \EQN urule2

 Note how in representation the monopolist’s decision for
:math:`u_t = Q_{t+1} - Q_t` feeds back negatively on the implementation
multiplier.

Concluding remarks
==================

This chapter is our first encounter with a class of problems in which
optimal decision rules are history dependent. We shall confront many
more such problems in chapters , , and and shall see in various contexts
how history dependence can be represented recursively by appropriately
augmenting the natural state variables with counterparts to our
implementability multipliers. A hint at what these counterparts are is
gleaned by appropriately interpreting implementability multipliers as
derivatives of value functions. In chapters , , and , we make dynamic
incentive and enforcement problems recursive by augmenting the state
with continuation values of other decision makers. We verify that the
:math:`P` associated with the stabilizing :math:`\mu_0 = P
y_0` satisfies the Riccati equation associated with the Bellman
equation. Substituting :math:`\mu_t = P y_t` into and gives

.. math::

   \EQNalign{ (I + \beta   B   Q^{-1}   B P) y_{t+1}
      & = A y_t \EQN olrp9;a \cr
       \beta A' P y_{t+1} & = - Ry_t + P y_t. \EQN olrp9;b \cr }

 A matrix inversion identity implies

.. math::

   (I + \beta   B   Q^{-1}   B' P)^{-1}
     = I - \beta   B (  Q + \beta
       B' P   B)^{-1}   B' P .
     \EQN olrp10

 Solving for :math:`y_{t+1}` gives

.. math:: y_{t+1} = (A -   B F) y_t \EQN olrp11

 where

.. math:: F = \beta (  Q + \beta   B' P   B)^{-1}   B' P A .\EQN olrp12

 Premultiplying by :math:` \beta A' P` gives

.. math:: \beta A' P y_{t+1} = \beta (A'PA - A' P   B F) y_t. \EQN olrp13

 For the right side of to agree with the right side of for any initial
value of :math:`y_0` requires that

.. math::

   P = R + \beta A'P A -\beta^2 A'P   B (  Q +  \beta   B' P
       B)^{-1}   B' P A. \EQN olrp14

 Equation is the algebraic matrix Riccati equation associated with the
optimal linear regulator for the system :math:`A,   B, Q,   R`.

This appendix generalizes some calculations from chapter for solving
systems of linear difference equations. Returning to system , let
:math:`L =L^* \beta^{-.5}` and transform the system to

.. math::

   L \left[ \matrix{ y_{t+1}^*  \cr
                   \mu_{t+1}^* \cr} \right] =
         N  \left[ \matrix{ y_{t}^*  \cr
              \mu_t^* \cr} \right] ,            \EQN symplec2

 where :math:`y_t^* = \beta^{t/2} y_t,  \mu_t^* = \mu_t \beta^{t/2}`.
Now :math:`\lambda L - N` is a symplectic pencil, so that the
generalized eigenvalues of :math:`L, N` occur in reciprocal pairs: if
:math:`\lambda_i` is an eigenvalue, then so is :math:`\lambda_i^{-1}`.

We can use Evan Anderson’s Matlab program schurg.m to find a stabilizing
solution of system . The program computes the ordered real generalized
Schur decomposition of the matrix pencil. Thus, schurg.m computes
matrices :math:`\bar L, \bar N, V` such that :math:`\bar L` is upper
triangular, :math:`\bar N` is upper block triangular, and :math:`V` is
the matrix of right Schur vectors such that for some orthogonal matrix
:math:`W`, the following hold:

.. math::

   \eqalign{ W L V & =  \bar L \cr
            W N V & = \bar N. \cr} \EQN schur

 Let the stable eigenvalues (those less than :math:`1`) appear first.
Then the stabilizing solution is

.. math:: \mu_t^* = P y_t^* \EQN chisoln

 where

.. math:: P = V_{21}  V_{11}^{-1},

 :math:`V_{21}` is the lower left block of :math:`V`, and :math:`V_{11}`
is the upper left block.

If :math:`L` is nonsingular, we can represent the solution of the system
as

.. math::

   \left[ \matrix {y_{t+1}^* \cr \mu_{t+1}^* \cr} \right]
          = L^{-1} N \left[ \matrix{I \cr P \cr} \right] y_t^*. \EQN Zsoln

 The solution is to be initialized from . We can use the first half and
then the second half of the rows of this representation to deduce the
following recursive solutions for :math:`y_{t+1}^*` and
:math:`\mu_{t+1}^*`:

.. math::

   \eqalign{ y_{t+1}^* &  = A_o^{*} y_t^*  \cr
                \mu_{t+1}^* & =   \psi^* y_t^*.  \cr } \EQN solnprelim

 Now express this solution in terms of the original variables:

.. math::

   \eqalign{ y_{t+1} &  = A_o y_t  \cr
                \mu_{t+1} & =   \psi y_t, \cr } \EQN soln

 where :math:`A_o = A_o^{*}\beta^{-.5}, \psi =
\psi^* \beta^{-.5}`. We also have the representation

.. math:: \mu_t = P y_t .   \EQN chicontemp

 The matrix :math:`A_o = A -   B F`, where :math:`F` is the matrix for
the optimal decision rule.

The decision rule for the competitive fringe incorporates forecasts of
future prices from under :math:`m`. Thus, the representative competitive
firm uses equation to forecast future values of :math:`(Q_t, q_t)` in
order to forecast :math:`p_t`. The representative competitive firm’s
forecasts are generated from the :math:`j`\ th iterate of :

.. math::

   \left[\matrix{z_{t+j} \cr \mu_{x,t+j}\cr}\right]
      = m^j
        \left[\matrix{z_t \cr \mu_{x,t} \cr} \right] . \EQN oli12

The following calculation verifies that the representative firm
forecasts by iterating the law of motion associated with :math:`m`.
Write the Euler equation for :math:`i_t` in terms of a polynomial in the
lag operator :math:`L` and factor it:
:math:`(1 - (\beta^{-1} + (1+c^{-1}h))L + \beta^{-1} L^2) = -(\beta
\lambda)^{-1} L (1 - \beta \lambda L^{-1})(1-\lambda L)` where
:math:`\lambda \in (0,1)` and :math:`\lambda =1` when :math:`h =0`. By
taking the nonstochastic version of and solving an unstable root forward
and a stable root backward using the technique of Sargent (1979 or
1987a, chap. IX), we obtain

.. math::

   i_t  =  (\lambda-1)q_t +  c^{-1}   \sum_{j=1}^\infty
      ( \beta \lambda)^j p_{t+j}, \EQN oli4a

 or

.. math::

   i_t = (\lambda -1) q_t + c^{-1} \sum_{j=1}^\infty
     (  \beta \lambda)^j
        [(A_0-d) - A_1 (Q_{t+j} + q_{t+j}) + v_{t+j}] , \EQN oli4b

 This can be expressed as

.. math::

   i_t =(\lambda -1) q_t + c^{-1} e_p \beta \lambda m
       (I - \beta \lambda m)^{-1}
   \left[\matrix{z_t \cr \mu_{xt}\cr}
     \right]   \EQN oli4c

 where
:math:`e_p = \left[\matrix{ (A_0 -d ) & 1 & - A_1 & -A_1 & 0\cr}\right]`
is a vector that forms :math:`p_t -d` upon postmultiplication by
:math:`\left[\matrix{z_t \cr \mu_{xt}\cr}
  \right]  `. It can be verified that the solution procedure builds in
as an identity, so that agrees with\ 

.. math::

   i_t = - P_{22}^{-1} P_{21} z_t + P_{22}^{-1} \mu_{xt}.
      \EQN oli4d

Exercises
=========

 There is no uncertainty. For :math:`t \geq 0`, a monetary authority
sets the growth of the (log) of money according to

.. math:: m_{t+1} = m_t + u_t \leqno(1)

 subject to the initial condition :math:`m_0>0` given. The demand for
money is

.. math:: m_t - p_t = - \alpha (p_{t+1} - p_t), \alpha > 0,  \leqno(2)

 where :math:`p_t` is the log of the price level. Equation (2) can be
interpreted as the Euler equation of the holders of money.

 Briefly interpret how equation (2) makes the demand for real balances
vary inversely with the expected rate of inflation. Temporarily (only
for this part of the exercise) drop equation (1) and assume instead that
:math:`\{m_t\}` is a given sequence satisfying
:math:`\sum_{t=0}^\infty m_t^2 < + \infty`. Please solve the difference
equation (2) “forward” to express :math:`p_t` as a function of current
and future values of :math:`m_s`. Note how future values of :math:`m`
influence the current price level.

At time :math:`0`, a monetary authority chooses a possibly
history-dependent strategy for setting :math:`\{u_t\}_{t=0}^\infty`.
(The monetary authority commits to this strategy.) The monetary
authority orders sequences :math:`\{m_t, p_t\}_{t=0}^\infty` according
to

.. math::

   - \sum_{t=0}^\infty .95^t \left[  (p_t - \overline p)^2 +
       u_t^2 + .00001 m_t^2  \right]. \leqno(3)

 Assume that :math:`m_0=10, \alpha=5, \bar p=1`. Please briefly
interpret this problem as one where the monetary authority wants to
stabilize the price level, subject to costs of adjusting the money
supply and some implementability constraints. (We include the term
:math:`.00001m_t^2` for purely technical reasons that you need not
discuss.)

 Please write and run a Matlab program to find the optimal sequence
:math:`\{u_t\}_{t=0}^\infty`. Display the optimal decision rule for
:math:`u_t` as a function of :math:`u_{t-1},  m_t, m_{t-1}`. Compute the
optimal :math:`\{m_t, p_t\}_t` sequence for :math:`t=0, \ldots,  10`.

 The optimal :math:`\{m_t\}` sequence must satisfy
:math:` \sum_{t=0}^\infty (.95)^t m_t^2 < +\infty`. You are free to
apply the Matlab program olrp.m.

 A representative consumer has quadratic utility functional

.. math:: \sum_{t=0}^\infty \beta^t \left\{ -.5 (b -c_t)^2 \right\} \leqno(1)

 where :math:`\beta \in (0,1)`, :math:`b = 30`, and :math:`c_t` is time
:math:`t` consumption. The consumer faces a sequence of budget
constraints

.. math:: c_t + a_{t+1} = (1+r)a_t + y_t - \tau_t \leqno(2)

 where :math:`a_t ` is the household’s holdings of an asset at the
beginning of :math:`t`, :math:`r >0` is a constant net interest rate
satisfying :math:`\beta (1+r) <1`, and :math:`y_t` is the consumer’s
endowment at :math:`t`. The consumer’s plan for :math:`(c_t, a_{t+1})`
has to obey the boundary condition
:math:`\sum_{t=0}^\infty \beta^t a_t^2 < + \infty`. Assume that
:math:`y_0, a_0` are given initial conditions and that :math:`y_t` obeys

.. math:: y_t = \rho y_{t-1}, \quad t \geq 1,  \leqno(3)

 where :math:`|\rho| <1`. Assume that :math:`a_0=0`, :math:`y_0=3`, and
:math:`\rho=.9`.

At time :math:`0`, a planner commits to a plan for taxes
:math:`\{\tau_t\}_{t=0}^\infty`. The planner designs the plan to
maximize

.. math::

   \sum_{t=0}^\infty \beta^t
   \left\{ -.5 (c_t-b)^2 -   \tau_t^2\right\}  \leqno(4)

 over :math:`\{c_t, \tau_t\}_{t=0}^\infty` subject to the
implementability constraints (2) for :math:`t\geq 0` and

.. math:: \lambda_t =  \beta (1+r) \lambda_{t+1} \leqno(5)

 for :math:`t\geq 0`, where :math:`\lambda_t \equiv (b-c_t)`.

 Argue that (5) is the Euler equation for a consumer who maximizes (1)
subject to (2), taking :math:`\{\tau_t\}` as a given sequence. Formulate
the planner’s problem as a Stackelberg problem. For
:math:`\beta=.95, b=30, \beta(1+r)=.95`, formulate an artificial optimal
linear regulator problem and use it to solve the Stackelberg problem.
Give a recursive representation of the Stackelberg plan for
:math:`\tau_t`.


Markov perfect equilibrium
==========================

This lecture applies linear-quadratic dynamic programming to a dynamic model of duopoly.

We use this as a vehicle to introduce the concept of a *Markov perfect equilibrium*


Duopoly model
--------------

A market has two firms.

Each firm recognizes that its output decision will affect the aggregate output and therefore influence the market price.

The one-period return function of firm :math:`i` is

.. math::
  R_{it} = p_t y_{it} - .5 d (y_{i t+1} - y_{it})^2
  :label: game1

There is an inverse demand curve

.. math::
  p_t = A_0 - A_1 (y_{1t} +  y_{2t}).
  :label: game2

Substituting the inverse demand curve into equation :eq:`game2` lets us express the return as

.. math::
   R_{it} = A_0 y_{it} - A_1 y_{it}^2 - A_1 y_{it}y_{-i,t} - .5 d (y_{it+1} - y_{it})^2 ,
   :label: game3

where :math:`y_{-i,t}` denotes the output of the firm other than :math:`i`.

Firm :math:`i` chooses a decision rule that sets :math:`y_{it+1}` as a function of :math:`(y_{it}, y_{-i,t})` and that maximizes

.. math::
  \sum_{t=0}^\infty \beta^t R_{it} .

Temporarily assume that the maximizing decision rule is :math:`y_{it+1}  = f_i(y_{it}, y_{-i,t})`.

Given the function :math:`f_{-i}`, the Bellman equation of firm :math:`i` is

.. math::
    v_i(y_{it}, y_{-i,t}) = \max_{y_{it+1}} \left\{R_{it} + \beta v_i(y_{it+1}, y_{-i,t+1}) \right\}
    :label: game4

where the maximization is subject to the perceived decision rule of the other firm

.. math::
  y_{-i,t+1} = f_{-i}(y_{-i,t}, y_{it}).
  :label: game5

Note the cross-reference between the two problems for :math:`i=1,2`.

We now advance the following

**Definition**  A *Markov perfect equilibrium* is a pair of value functions :math:`v_i` and a pair of policy functions :math:`f_i` for :math:`i=1,2` such that

     * Given :math:`f_{-i}`,\ :math:`v_i` satisfies the Bellman equation :eq:`game5`;

     * The policy function :math:`f_i` attains the right side of  Bellman equation :eq:`game5`.

The adjective "Markov" denotes that the equilibrium decision rules depend on the current values of the state variables :math:`y_{it}` only, not other parts of their histories.

"Perfect" means 'complete', i.e., that the equilibrium is constructed by backward induction and therefore builds in optimizing behavior for each firm for all possible future states, including many that will not be realized when we iterate forward on the pair of equilibrium strategies :math:`f_i`.

Computation
-----------

If it exists, a Markov perfect equilibrium can be computed by iterating to convergence on the pair of Bellman equations .

In particular, let :math:`v_i^j,f_i^j` be the value function and policy function for firm :math:`i` at the :math:`j`\ th iteration.

Imagine constructing the iterates

.. math::
    v_i^{j+1}(y_{it}, y_{-i,t}) = \max_{y_{i,t+1}} \left\{R_{it} + \beta v_i^{j}(y_{it+1}, y_{-i,t+1}) \right\}
    :label: game6

where the maximization is subject to

.. math::
  y_{-i,t+1} = f^j_{-i}(y_{-i,t}, y_{it}).
  :label: game7

In general, these iterations are difficult.

But they simplify for the case in which the return function is quadratic and the transition laws are linear.

Linear Markov perfect equilibria
================================

The optimal linear regulator can be used to compute a Markov perfect equilibrium of our duopoly model.

The model is an example of a *dynamic game*.

A dynamic game consists of these objects:

     * (a) a list of players;

     * (b) a list of dates and actions available to each player at each date; and

     * (c) payoffs for each player expressed as functions of the actions taken by all players.

The optimal linear regulator is a good tool for formulating and solving dynamic games.

The standard equilibrium concept — subgame perfection — in these games requires that each player's strategy be computed by backward induction.

This leads to an interrelated pair of Bellman equations.

In linear quadratic dynamic games, these "stacked Bellman equations" become "stacked Riccati equations" with a tractable mathematical structure.

We now consider the following two-player, linear quadratic *dynamic game*.

An :math:`(n \times 1)` state vector :math:`x_t` evolves according to a transition equation

.. math::
  x_{t+1} = A_t x_t + B_{1t} u_{1t} + B_{2t} u_{2t}
  :label: orig-0

where :math:`u_{jt}` is a :math:`(k_j \times 1)` vector of controls of player :math:`j`.

We start with a finite horizon formulation, where :math:`t_0` is the initial date and :math:`t_1` is the terminal date for the common horizon of the two players.

Player :math:`1` maximizes

.. math::
   - \sum_{t=t_0}^{t_1 - 1}  \left( x_t^T R_1 x_t + u_{1t}^T Q_1 u_{1t} + u_{2t}^T S_1 u_{2t}\right)
   :label: orig-1

where :math:`R_1` and :math:`S_1` are positive semidefinite and :math:`Q_1` is positive definite.

Player 2 maximizes

.. math::
   - \sum_{t=t_0}^{t_1 - 1} \left( x_t^T R_2 x_t + u_{2t}^T Q_2 u_{2t} + u_{1t}^T S_2 u_{1t} \right)
   :label: orig-2

where :math:`R_2` and :math:`S_2` are positive semidefinite and :math:`Q_2` is positive definite.

We formulate a Markov perfect equilibrium as follows.

Player :math:`j` employs linear decision rules

.. math::
  u_{jt} = - F_{jt}  x_t, \ \ t = t_0, \ldots, t_1 - 1

where :math:`F_{jt}` is a :math:`(k_j \times n)` matrix.

Assume that player :math:`i` knows :math:`\{F_{-i,t}; t = t_0, \ldots, t_1 - 1 \}`.

Then player 1's problem is to maximize expression subject to the known law of motion *and* the known control law :math:`u_{2t} = - F_{2t} x_t` of player 2.

Symmetrically, player 2's problem is to maximize expression subject to equation and :math:`u_{1t} = - F_{1t} x_t`.

A Markov perfect equilibrium is a pair of sequences :math:`\{F_{1t}, F_{2t};\, t = t_0, t_0 + 1 , \ldots, t_1 - 1 \}` such that

    * :math:`\{F_{1t}\}` solves player 1's problem, given :math:`\{F_{2t}\}`, and

    * :math:`\{F_{2t}\}` solves player 2's problem, given :math:`\{F_{1t}\}`.

We have restricted each player's strategy to depend only on :math:`x_t`, and not on the *history* :math:`h_t =\{(x_s, u_{1s}, u_{2s}), s = t_0, \ldots, t\}`.

This restriction on strategy spaces accounts for the adjective "Markov" in the phrase "Markov perfect equilibrium."

Player 1's problem is to maximize

.. math::
   - \sum_{t=t_0}^{t_1 - 1}\Bigl\{ x_t^T (R_1 + F_{2t}^T S_1 F_{2t}) x_t + u_{1t}^T Q_1 u_{1t} \Bigr\}

subject to

.. math::
  x_{t+1} = (A_t- B_{2t} F_{2t}) x_t + B_{1t} u_{1t}.

This is an optimal linear regulator problem, and it can be solved by working backward.

Evidently, player 2's problem is also an optimal linear regulator problem.

The policy rule that solves player 1's problem is

.. math::
    F_{1t} = ( B_{1t}^T P_{1t+1} B_{1t} + Q_1)^{-1}  B_{1t}^T P_{1t+1} (A_t - B_{2t} F_{2t})
    :label: orig-3

.. math::
  t = t_0, t_0 + 1 , \ldots, t_1 - 1

where :math:`P_{1t}` is the solution of the following matrix Riccati difference equation with terminal condition :math:`P_{1t_{1}} = 0`: \

.. math::
    P_{1t} = & (A_t - B_{2t} F_{2t})^T P_{1t+1} (A_t - B_{2t} F_{2t}) + (R_1 +  F_{2t}^T S_1 F_{2t}) \\
     & \; - (A_t   - B_{2t} F_{2t})^T P_{1t+1} B_{1t} (B_{1t}^T P_{1t+1} B_{1t} + Q_1)^{-1} B_{1t}^T P_{1t+1} (A_t - B_{2t} F_{2t})
    :label: orig-4

.. NOTE: I changed the formatting here a little bit

The policy that solves player 2's problem is

.. math::
   F_{2t} = (B_{2t}^T P_{2t+1} B_{2t} + Q_2)^{-1} B_{2t}^T P_{2t+1} (A_t - B_{1t} F_{1t})
   :label: orig-5

where :math:`P_{2t}` solves the following matrix Riccati difference equation, with terminal condition :math:`P_{2t_1} = 0`:

.. math::
   \eqalign {P_{2t} &= (A_t - B_{1t} F_{1t})^T P_{2t+1} (A_t - B_{1t} F_{1t}) + (R_2 + F_{1t}^T S_2 F_{1t}) \cr &- (A_t - B_{1t} F_{1t})^T P_{2t+1} B_{2t} \cr & (B_{2t}^T P_{2t+1} B_{2t} + Q_2)^{-1} B_{2t}^T P_{2t+1} (A_t - B_{1t} F_{1t}).\cr}
   :label: orig-6

The equilibrium sequences :math:`\{F_{1t}, F_{2t}; t = t_0, t_0 + 1 , \ldots, t_1 - 1\}` can be calculated from the pair of coupled Riccati difference equations and
:eq:`orig-3` and :eq:`orig-5`.

In particular, we use equations :eq:`orig-3`, :eq:`orig-4`, :eq:`orig-5`, and :eq:`orig-6` to "work backward" from time :math:`t_1 - 1`.

Notice that given :math:`P_{1t+1}` and :math:`P_{2t+1}`, equations :eq:`orig-3` and :eq:`orig-5` are a system of :math:`(k_2 \times n) + (k_1
\times n)` *linear* equations in the :math:`(k_2 \times n) + (k_1 \times n)` unknowns in the matrices :math:`F_{1t}` and :math:`F_{2t}`.

Notice how :math:`j`\ 's control law :math:`F_{jt}` is a function of :math:`\{F_{is}, s \geq t, i \neq j \}`.

Thus, agent :math:`i`\ 's choice of :math:`\{F_{it}; t = t_0, \ldots, t_1 - 1\}` influences agent :math:`j`\ 's choice of control laws.

However, in the Markov perfect equilibrium of this game, each agent is assumed to ignore the influence that his choice exerts on the other agent's choice.

We often want to compute the solutions of such games for infinite horizons, in the hope that the decision rules :math:`F_{it}` settle down to be time invariant as :math:`t_1 \rightarrow +\infty`.

In practice, we usually fix :math:`t_1` and compute the equilibrium of an infinite horizon game by driving :math:`t_0 \rightarrow - \infty`.

Judd followed that procedure in the following example.

An example
----------

This section describes the Markov perfect equilibrium of an infinite horizon linear quadratic game proposed by Kenneth Judd (1990).

The equilibrium is computed by iterating to convergence on the pair of Riccati equations defined by the choice problems of two firms.

Each firm solves a linear quadratic optimization problem, taking as given and known the sequence of linear decision rules used by the other player.

The firms set prices and quantities of two goods interrelated through their demand curves. There is no uncertainty. Relevant variables are defined as follows:

:math:`I_{it}` = inventories of firm :math:`i` at beginning of :math:`t`.

:math:`q_{it}` = production of firm :math:`i` during period :math:`t`.

:math:`p_{it}` = price charged by firm :math:`i` during period :math:`t`.

:math:`S_{it}` = sales made by firm :math:`i` during period :math:`t`.

:math:`E_{it}` = costs of production of firm :math:`i` during period :math:`t`.

:math:`C_{it}` = costs of carrying inventories for firm :math:`i` during :math:`t`. The firms' cost functions are

:math:`C_{it} = c_{i1} + c_{i2} I_{it} + .5 c_{i3} I_{it}^2`

:math:`E_{it} = e_{i1} + e_{i2}q_{it} + .5 e_{i3} q_{it}^2` where :math:`e_{ij},c_{ij}` are positive scalars.

Inventories obey the laws of motion

.. math::
  I_{i,t+1} = (1 - \delta)  I_{it} + q_{it} - S_{it}

Demand is governed by the linear schedule

.. math::
  S_t = d p_{it} + B

where :math:`S_t = \left[\matrix{S_{1t} & S_{2t}\cr}\right]'`, :math:`d` is a :math:`(2\times 2)` negative definite matrix, and :math:`B` is a vector of constants.

Firm :math:`i` maximizes the undiscounted sum

.. math::
   \lim_{T \to \infty}\ {1 \over T}\   \sum^T_{t=0}\   \left( p_{it} S_{it} - E_{it} - C_{it} \right)

by choosing a decision rule for price and quantity of the form

.. math::
  u_{it} = -F_i  x_t

where :math:`u_{it} =\left[ \matrix{p_{it} & q_{it}\cr}\right]'`, and the state is :math:`x_t=\left[\matrix{I_{1t} & I_{2t}\cr}\right]`.

Below we show a Python function `nnash` that computes a Markov perfect equilibrium of the linear quadratic dynamic game in which player :math:`i` maximizes

.. math::
   - \sum_{t=0}^\infty \{ x_t' r_i x_t + 2 x_t' w_i u_{it} +u_{it}' q_i u_{it} + u_{jt}' s_i u_{jt} + 2 u_{jt}' m_i u_{it} \}

subject to the law of motion

.. math::
  x_{t+1} = a x_t + b_1 u_{1t}+b_2 u_{2t}

and a control law :math:`u_{jt}= -f_j x_t` for the other player; here variables have the following dimensions:

* :math:`a` is :math:`n \times n`
* :math:`b_1` is :math:`n \times k_1`
* :math:`b_2` is :math:`n \times k_2`
* :math:`r_1` is :math:`n\times n`
* :math:`r_2` is :math:`n \times n`
* :math:`q_1` is :math:`k_1 \times k_1`
* :math:`q_2` is :math:`k_2 \times k_2`
* :math:`s_1` is :math:`k_2 \times k_2`
* :math:`s_2` is :math:`k_1 \times k_1`
* :math:`w_1` is :math:`n \times k_1`
* :math:`w_2` is :math:`n \times k_2`
* :math:`m_1` is :math:`k_2 \times k_1`
* :math:`m_2` is :math:`k_1 \times k_2`

.. NOTE: I put these into a list. I was having a hard time reading them otherwise

The equilibrium of Judd’s model can be computed by filling in the matrices appropriately. A Python tutorial :download:`markov_perf_judd.py </../../python_programs/markov_perf_judd.py>`. uses `nnash` to compute the equilibrium.

.. literalinclude:: /../../pyTM/util/lq.py
   :pyobject: nnash


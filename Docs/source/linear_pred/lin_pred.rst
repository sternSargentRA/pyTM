.. _Lin_pred:

*********************************************
Linear State Space Models of Time Series
*********************************************


.. epigraph::

    "We may regard the present state of the universe as the effect of its past and the cause of its future" -- Marquis de Laplace


Overview
============

This lecture introduces the linear state space dynamic system

Easy to use and carries a powerful theory of prediction

A workhorse with many applications

* representing dynamics of many higher-order linear systems

* predicting the position of a system :math:`j` steps into the future

* predicting a geometric sum of future values of a variable like

    * non financial income

    * dividends on a stock

    * the money supply

    * a government deficit or surplus

    * etc., etc., :math:`\ldots`

* key ingredient of useful models

    * Friedman's permanent income model of consumption smoothing

    * Barro's model of smoothing total tax collections

    * Rational expectations version of Cagan's model of hyperinflation

    * Sargent and Wallace's "unpleasant monetarist arithmetic"

    * etc., etc., :math:`\ldots`


A Linear State Space Model
===============================

Objects in play

* An :math:`n \times 1` vector :math:`x_t` denoting the *state* at time :math:`t, \ t \geq 0`

* An :math:`n \times 1` vector :math:`x_0` denoting the initial state vector at :math:`t=0`

* An :math:`m \times 1` vector of i.i.d. random variables :math:`\epsilon_{t+1} \sim {\cal N}(0,I)`

* A :math:`k \times 1` vector of *observations* :math:`y_t` at time :math:`t, \ t \geq 0`

* An :math:`n \times n` matrix :math:`A`  called a *transition matrix*

* An :math:`n \times m` matrix :math:`C`  called a *volatility matrix*

* A :math:`k \times n` matrix :math:`G`

Here is the linear state-space system

.. math::
        x_{t+1} & =  A x_t + C \epsilon_{t+1}   \\
        y_t &  =  G x_t \\
        x_0 & \sim {\cal N}(\mu_0, \Sigma_0)
        :label: st_space_rep


Martingale difference shocks
=============================

The :math:`\epsilon_{t+1}` process serves as a vector of *shocks*.

Often, as above,  these are assumed to be a sequence of standardized normal vectors.

But we can equally well work with the assumption that :math:`\{\epsilon_{t+1}\}` is a *martingale difference sequence*, meaning that it satisfies

.. math::
       E [\epsilon_{t+1} | x_t, x_{t-1}, \ldots ] = 0

This is a weaker condition than that :math:`\epsilon` is vector of i.i.d. random variables satisfying :math:`\epsilon_{t+1} \sim {\cal N}(0,I)`

Examples
===========

These examples illustrate the wise dictum  *finding the state is an art*

By appropriately choosing the definitions of  :math:`A, C, G, x_t, y_t`, a variety of models for :math:`\{y_t\}_{t=0}^\infty` can be captured

Second-order difference equation
================================
Let :math:`\{y_t\}_t` be a deterministic sequence that satifies

.. math::
    y_{t+1} =  \alpha + \rho_1 y_t + \rho_2 y_{t-1} , \quad t \geq 0
    :label: st_ex_1

subject to given values of :math:`y_{-1}, y_{-2}`  These are called `initial conditions`

To map :eq:`st_ex_1` into our state space system :eq:`st_space_rep`, we set

.. math::
    x_t= \left[
    \begin{array}{c} 1 \\ y_t \\ y_{t-1} \end{array}
    \right]
    \qquad
    A = \left[\begin{array}{cc} \alpha & 0 & 0 \\
                              0 & \rho_1 & \rho_2  \\
                              0 & 1 & 0 \end{array} \right]
    \qquad
    C= \left[ \begin{array}{c} 0 \\ 0 \\ 0 \end{array}\right]
    \qquad
    G = \left[ \begin{array}{c} 0 & 1 & 0 \end{array}\right]





Univariate Autoregressive Processes
=====================================

We can use :eq:`st_space_rep` to represent the model

.. math::
   y_{t+1} = \alpha_1 y_{t} + \alpha_2 y_{t-1} + \alpha_3 y_{t-2} + \alpha_4  y_{t-3} + \epsilon_{t+1}
   :label: eq_ar_rep

where :math:`w_t` is a martingale difference sequence.  We set :math:`n = 4, x_t = [y_t \
y_{t-1} \  y_{t-2} \  y_{t-3} ]^\prime` and

.. math::
   A = \left[ \begin{array}{cc} \alpha_1 & \alpha_2 & \alpha_3 &
   \alpha_4 \cr 1 & 0 & 0 & 0 \cr 0 & 1 & 0 & 0 \cr 0 & 0 & 1 & 0 \end{array}
   \right]
   \qquad
   C = \left[ \begin{array}{cc} 1 \cr 0 \cr 0 \cr 0 \end{array} \right]
   \qquad
    G = \left[ \begin{array}{c} 1 & 0  & 0 & 0 \end{array}\right]

The matrix :math:`A` has the form of the *companion matrix* to the vector
:math:`[\alpha_1 \  \alpha_2 \ \alpha_3 \ \alpha_4]`.


Vector Autoregressions
========================

Let :math:`y_t` be a :math:`k \times 1`
vector, :math:`\alpha_j` a :math:`k \times k` matrix, and :math:`w_t` a :math:`k \times 1` martingale
difference sequence.  Then :eq:`eq_ar_rep` is termed a *vector autoregression*.
To map this into :eq:`st_space_rep`, we set :math:`n = k \cdot 4`, and

.. math::
   A = \left[ \begin{array}{cc} \alpha_1 & \alpha_2 & \alpha_3 & \alpha_4 \cr
   I & 0        & 0        & 0        \cr
   0 & I        & 0        & 0        \cr
   0 & 0        & I        & 0       \end{array}\right],
   \qquad
   C = \left[ \begin{array}{c} I \cr 0 \cr 0 \cr 0 \end{array} \right]

where :math:`I` is the :math:`k \times k` identity matrix.

Deterministic Seasonals
=========================

We can use :eq:`st_space_rep` to represent :math:`y_t = y_{t-4}`.    Let :math:`n=4`,

.. math::
    x_t = \left[\begin{array}{c} y_t & y_{t-1} & y_{t-2} & y_{t-3}\end{array}\right]^\prime,
    \qquad
     x_0 = \left[\begin{array}{c} 0 & 0 & 0 & 1\end{array}\right]^\prime

.. math::
    A = \left[ \begin{array}{cc} 0 & 0 & 0 & 1 \cr
    1 & 0 & 0 & 0 \cr
    0 & 1 & 0 & 0 \cr
    0 & 0 & 1 & 0  \end{array} \right] ,
    \qquad
    C =  \left[ \begin{array}{cc}  0 \cr 0 \cr 0 \cr 0 \end{array} \right]

Here the :math:`A` matrix has four distinct eigenvalues and the absolute
values of each of these eigenvalues is one.  Two eigenvalues are real :math:`(1,-1)`
and two  are imaginary :math:`(i,-i)`,  and so have period four.  [#foot1]_ The
resulting sequence :math:`\{x_t : t=1,2,\ldots\}` oscillates deterministically
with period four.   It can be used to model deterministic seasonals in
quarterly time series.


Indeterministic Seasonal
===========================
We want to use :eq:`st_space_rep` to represent :math:`y_t = \alpha_4 y_{t-4} + w_t`
where :math:`w_t` is an iid Gaussian sequence   sequence and :math:`| \alpha_4 | \leq 1`.
We define :math:`x_t` as in the previous example and

.. math::
   A = \left[ \begin{array}{cc} 0 & 0 & 0 & \alpha_4 \cr 1 & 0 & 0 & 0 \cr
   0 & 1 & 0 & 0 \cr 0 & 0 & 1 & 0 \end{array} \right]
   \qquad
   C = \left[ \begin{array}{cc}   1 \cr 0 \cr 0 \cr 0 \end{array} \right]

With these definitions, :eq:`st_space_rep` represents what we want. :math:`\{y_t\}` displays an
*indeterministic* seasonal, i.e., recurrent,
but aperiodic, seasonal fluctuations.

.. [#foot1]  For example, note that :math:`i = \exp\left(\pi/2 \right) + i \sin \left(\pi/2\right)`, so  the period associated with :math:`i`  is :math:`{\frac{2 \pi}{\frac{\pi}{2}}} = 4`.

Polynomial Time Trends
=======================

Let :math:`n=2, x_0 = [0 \ 1]^\prime`, and

.. math::
   A = \left[ \begin{array}{cc} 1 & 1  \cr 0 & 1   \end{array} \right],
   \qquad
   C = \left[ \begin{array}{cc} 0 \cr 0 \end{array} \right].


Then

.. math::
   A^t = \left[ \begin{array}{cc} 1 & t  \cr 0 & 1  \end{array} \right]

Hence :math:`x_t = \left[\begin{array}{cc}  t &1 \end{array}\right]^\prime`, so that the first component of :math:`x_t` is a linear
time trend and the second component is a constant.

It is also possible to use the state-space system :eq:`st_space_rep` to represent polynomial trends of any order.
For instance, let :math:`n=3,C=0,x_0 = \left[\begin{array}{cc}0 &0 &1\end{array}\right]^\prime`, and

.. math::
   A = \left[ \begin{array}{cc} 1 & 1 & 0  \cr 0 & 1 & 1  \cr 0 & 0 & 1 \end{array} \right] .

It follows that

.. math::
   A^t = \left[ \begin{array}{cc} 1 & t & t(t-1)/2 \cr 0 & 1 & t \cr 0 & 0 & 1 \end{array}\right]

Then :math:`x_t^\prime = \left[\begin{array}{cc} t(t-1)/2 &t & 1\end{array}\right]`, so that :math:`x_t` contains  linear and
quadratic time trends.

Martingale with Drift
======================

Following Hansen and Sargent XXXXX [add reference], we modify the linear time trend example and set :math:`C` nonzero.  Suppose
that :math:`N` is one and :math:`C^\prime = [1 \ 0]`.  Since :math:`A = \left[ \begin{array}{cc} 1
& 1 \cr 0 & 1 \end{array}\right]` and :math:`A^t = \left[ \begin{array} {cc} 1 & t \cr 0
& 1 \end{array} \right]`, it follows that

.. math::
   A^\tau C = \left[ \begin{array} {cc} 1 \cr 0 \end{array} \right]
   :label: eqob24

Substituting into the moving-average representation :eq:`eqob5`, we obtain

.. math::
    x_{1t} = \sum_{\tau=0}^{t-1} \epsilon_{t-\tau} + \left[\begin{array}{cc} 1 & t \end{array}\right] x_0

where :math:`x_{1t}` is the first entry of :math:`x_t`.  The first term on the right is a cumulated sum of martingale differences,
and is called a *martingale*, while the second term is a translated linear function of time.



Processes with a constant state component
=========================================

Let :math:`A, C` satisfy

.. math::

     A & = \left[ \begin{array}{cc} A_{11} & A_{12} \cr 0 & 1 \end{array} \right] \\
     C & = \left[ \begin{array}{cc} C_{11} \cr 0 \end{array} \right]


where :math:`A_{11}` is an :math:`(n-1) \times (n-1)` matrix with eigenvalues that have
moduli strictly less than one and :math:`A_{12}` is an :math:`(n-1) \times 1`
column vector.

Conformably, let

.. math::

    x_t = \left[ \begin{array}{cc} x_{1t} \cr x_{2t} \end{array} \right]

where :math:`x_{1t}` is :math:`n-1 \times 1`.

It follows  that

.. math::
     x_{1t+1} & = A_{11}x_{1t} + A_{12}x_{2t} + C_{1}\epsilon_{t+1} \\
     x_{2t+1} & = x_{2t}
     :label: eqpartionA

Evidently, :math:`x_{1t} = x_{10}` for all :math:`t \geq 0`.
We choose to set :math:`x_{20} = 1` so that :math:`x_{2t} = 1` for
all :math:`t \geq 0`.


Let :math:`\mu_{1t} = Ex_{1t}`.   Taking unconditional expectations on both sides of
:eq:`eqpartionA` gives

.. math::
     \mu_{1,t+1} = A_{11} \mu_{1,t} + A_{12},
     :label: eqob29

a difference equation that is to be solved subject to an initial condition :math:`\mu_{1,0}` for :math:`x_{1,0}`


Evidently,

.. math::
      \mu_t \equiv E x_t = \left[\begin{array}{cc} \mu_{1,t} \cr 1 \end{array}\right]



Unconditional  covariance matrices
===================================

Define the *unconditional covariance matrix* of :math:`x_t` for :math:`t \geq 0` as

.. math::
    \Sigma_t = E (x_t - \mu_t) (x_t - \mu_t)'

where again the mathematical expectation is to be thought of as an average across sample paths (that we
can think of as being generated by computer simulations)

Equations :eq:`st_space_rep` and :eq:`eqmulaw` imply that

.. math::
    (x_{t+1} - \mu_{t+1}) = A (x_t - \mu_t) + C \epsilon_{t+1}
    :label: eqxlawmu

Equation :eq:`eqxlawmu` implies

.. math::
    \Sigma_{t+1}  = A \Sigma_t A' + C C',
    :label: eqsigmalaw

a difference equation that is to be solved subject to  a initial condition for  :math:`\Sigma_0` associated with the known initial distribution for :math:`x_0`


Autocovariance functions
=========================

Define the *autocovariance function* :math:`\Sigma_{t+j, j}` for :math:`j \geq 0, t \geq 0`
as

.. math::
    \Sigma_{t+j, t} = E (x_{t+j} - \mu_{t+j})(x_t - \mu_t)
    :label: eqnautodeff

Elementary calculations show that

.. math::
    \Sigma_{t+j,t} = A^j \Sigma_t
    :label: eqnautocov

Noticed that :math:`\Sigma_{t+j,t}` in general depends on both :math:`j`, the gap between the two dates, and :math:`t`, the earlier date.



Covariance stationary processes
================================


**Definition:**

A  process :math:`\{x_t\}` is said to be *covariance stationary* if

    * :math:`E x_t = \mu \ \forall t \geq 0`

    * :math:`\Sigma_t = \Sigma_0 \ \forall t \geq 0`

    * :math:`\Sigma_{t+j,t}` depends on the time gap :math:`j` but not on time :math:`t`

Put loosely, for a covariance stationary process, :math:`x_0, A, C`  assume values that imply that all first and second
unconditional moments of :math:`\{x_t : t=1,2,\ldots\}` are constant over time.

Constructing a covariance  stationary process
==============================================

Return to the process :eq:`eqpartionA`

Let  :math:`\bar \mu_1`  be the stationary value of
:math:`\mu_{1t}` and substitute :math:`\bar \mu_1` for :math:`\mu_{1t}`  and :math:`\mu_{1,t+1}` in :eq:`eqob29` and
solve  for :math:`\bar \mu_1` to get

.. math::
    \bar \mu_1 = (I-A_{11})^{-1} A_{12}

Therefore, if

.. math::
   Ex_{10} = (I-A_{11})^{-1} A_{12}

then

.. math::
    E x_{1,t} = E x_{1,0} = \bar \mu_{1}

It follows that the stationary value of :math:`\mu_t` is

.. math::
    E x_t = \left[\begin{array}{cc} \bar \mu_1 \cr 1 \end{array}\right] \equiv \bar \mu


The stationary values of :math:`\Sigma_t` and :math:`\Sigma_{t+j,t}` satisfy

.. math::
    \Sigma_\infty = A \Sigma_\infty A' + C C' \\
    \Sigma_{t+j,j} = A^j \Sigma_\infty
    :label: eqnSigmainf

Notice that :math:`\Sigma_\infty` does not depend on :math:`t` and that :math:`\Sigma_{t+j,t}` depends on the time gap :math:`j` but not on calendar time :math:`t`

.. note::

   If the eigenvalues of :math:`A_{11}` are
   less than unity in modulus, then (1) starting from any initial value of
   :math:`\mu_{1,0}`, :math:`\mu_{1t}`  converges to the stationary value :math:`(I-A_{11})^{-1} A_{12}`; and (2) iterations on :eq:`eqsigmalaw` converge
   to the fixed point of the *discrete Lyapunov equation* in
   the first line of :eq:`eqnSigmainf`

**Setting initial conditions to assure  covariance stationarity**

If :math:`x_0 \sim {\cal N}(\bar \mu, \Sigma_\infty)` and if the eigenvalues of  :math:`A_{11}` are strictly less than unity,
then the :math:`\{x_t\}` process is covariance stationary.





Unconditional means as ensemble averages
========================================

By an *ensemble average* we mean the average across an (infinite) population of sample paths *at a point in time*

Think of simlulating :eq:`st_space_rep` :math:`I`  times, thereby generating sample
paths :math:`x_{t}^i` for :math:`i=1, \ldots, I`

A law of large numbers assures us that

.. math::

    \bar x_t = \frac{1}{I} \sum_{i=1}^I x_t^i \approx \mu_t

where :math:`\mu_t \equiv E x_t` is to be thought of as an average *across (an infinite number of) sample paths*

By *population average* we mean the average across such an infinite number of sample paths


:math:`\mu_t` is called the *unconditional mean*  of  :math:`x_t, t \geq 0`



The population average of :math:`\epsilon_{t+1}` (again, the average across sample paths) is zero.


Unconditional covariance matrices as ensemble averages
=======================================================

Again, think of simlulating :eq:`st_space_rep` :math:`I`  times, thereby generating sample
paths :math:`x_{t}^i` for :math:`i=1, \ldots, I`

Another application of a  law of large numbers assures us that

.. math::

    {\rm Cov}_t = \frac{1}{I} \sum_{i=1}^I (x_t^i - \bar x_t) (x_t^i - \bar x_t) \approx \Sigma_t

where :math:`\Sigma_t = E (x_t - \mu_t)(x_t- \mu_t)'` is to be thought of as an average *across (an infinite number of) sample paths*

:math:`\Sigma_t` is called the *unconditional covariance*  of  :math:`x_t, t \geq 0`

Averages over time
===================

Think of taking a single realization :math:`\{x_t\}` of the state-space system and forming the sequence of averages and cross-averages

.. math::
    \bar x_t &= \frac{1}{t} \sum_{j=1}^t x_t \\
    R_t & = \frac{1}{t} \sum_{j=1}^t x_t x_t'

It is sometimes convenient to represent these sample moments recursively:

.. math::
    \bar x_t & =  \bar x_{t-1} + \frac{1}{t} (x_t - \bar x_{t-1} )\\
    R_t & = R_{t-1} + \frac{1}{t} \bigl( x_t x_t' - R_{t-1}\bigr)

As :math:`t \rightarrow +\infty`, we would like the sample moments :math:`\bar x_t` and :math:`R_t` to converge to something interpretable in terms
of our basic state-space representation.

To get this desideratum, we require something called *erodicity*

Ergodicity
===========

Averages across simulations are interesting theoretically, but in real life situations all we typically observe is a *single* realization
:math:`\{x_t, y_t\}_{t=0^T}`

What can we say about averages *over time*?

Suppose that :math:`\{x_t\}_{t=0}^\infty` is a *covariance stationary* process.

Then a law of large numbers implies that

.. math::

      \lim_{T \rightarrow \infty} \frac{1}{T} \sum_{t=0}^T x_t  & = \mu \\
      \lim_{T \rightarrow \infty} \frac{1}{T} \sum_{t=0}^T (x_t -\mu) (x_t - \mu)' & = \Sigma_\infty \\
      \lim_{T \rightarrow \infty} \frac{1}{T} \sum_{t=0}^T (x_{t+j} -\mu) (x_t - \mu)' & = A^j \Sigma_\infty

A stochastic process in which averages across time converge to averages across realizations is said to be *ergodic*

If our linear state space  system :eq:`st_space_rep` is covariance stationary, then it is ergodic.






Prediction Theory
==================

The optimal forecast of :math:`x_{t+1}` given information known at time :math:`t`, namely, :math:`x_t` is

.. math::
   E(x_{t+1} | x_t) = Ax_t
   :label: eqob2

and the one-step-ahead forecast error is

.. math::
   x_{t+1} - E(x_{t+1} \mid x_t) = C\epsilon_{t+1}
   :label: eqob3

The covariance matrix of :math:`x_{t+1}` conditioned on :math:`x_t` is

.. math::
   E (x_{t+1} - E ( x_{t+1} | x_t) ) (x_{t+1} - E ( x_{t+1} | x_t))^\prime = CC^\prime
   :label: eqob4

Moving average representation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A nonrecursive expression for :math:`x_t` as a function of
:math:`x_0, \epsilon_1, \epsilon_2, \ldots,  \epsilon_t` can be found by using :eq:`st_space_rep` repeatedly to obtain

.. math::
   x_t & = Ax_{t-1} + C\epsilon_t \\
       & = A^2 x_{t-2} + AC\epsilon_{t-1} + C\epsilon_t \\
       & = \cdots \\
       & = \left[\sum_{\tau=0}^{t-1} A^\tau C\epsilon_{t-\tau} \right] + A^t x_0
   :label: eqob5

Representation :eq:`eqob5` is a  *moving-average* representation.

It expresses :math:`\{x_t : t=1,2,\ldots\}`
as a linear function of current and past values of the  process
:math:`\{\epsilon_t: t=1,2,\ldots\}` and an initial condition :math:`x_0`.

By computing (population) averages across sample paths, we see that equation :eq:`eqob5`
implies that

.. math::
    E x_{t} | x_0 = A^t x_0

:math:`E_0 x_t \equiv E x_t | x_0` is called a *conditional mean* of :math:`x_t`

To approximate :math:`E_t x_t`, think of simulating many paths starting from the *same* given
value of :math:`x_0`, then averaging across the various :math:`x_t`'s



Forecasting formulas -- conditional means
-----------------------------------------


More generally, we'd like to compute


* :math:`j`-step ahead forecast of :math:`x`: :math:`E_t x_{t+j} \equiv E [x_{t+j} | x_t] = E [x_{t+j} | x_t, x_{t-1}, \ldots, x_0 ]`

* :math:`j`-step ahead forecast of :math:`y`: :math:`E_t y_{t+j} \equiv E [y_{t+j} | x_t] = E [y_{t+j} | x_t, x_{t-1}, \ldots, x_0  ]`


Here are the pertinent formulas


* :math:`j`-step ahead forecast of :math:`x`: :math:`E_t x_{t+j} \equiv E [x_{t+j} | x_t] = E [x_{t+j} | x_t, x_{t-1}, \ldots , x_0 ]`

.. math::
    E_t x_{t+j} = A^j x_t

* :math:`j`-step ahead forecast of :math:`y`: :math:`E_t y_{t+j} \equiv E [y_{t+j} | x_t] = E [y_{t+j} | x_t, x_{t-1}, \ldots , x_0 ]`

.. math::
    E_t y_{t+j} = G A^j x_t


Covariance of Prediction Errors
================================


It is useful to obtain the covariance matrix of the vector of  :math:`j`-step-ahead prediction
errors

.. math::
   x_{t+j} - E_t x_{t+j} = \sum^{j-1}_{s=0} A^s C \epsilon_{t-s+j}.
   :label: eqob8

Evidently,

.. math::
     V_j \equiv E_t (x_{t+j} - E_t x_{t+j}) (x_{t+j} - E_t x_{t+j})^\prime =   \sum^{j-1}_{k=0} A^k C C^\prime A^{k^\prime}
   :label: eqob9a

:math:`V_j` defined in :eq:`eqob9a` can be calculated recursively via

.. math::
   V_1 &= CC^\prime \\
   V_j &= CC^\prime + A V_{j-1} A^\prime, \quad j \geq 2
   :label: eqob9b

For :math:`j \geq 1`,  :math:`V_j` is the *conditional covariance matrix* of the errors in forecasting
:math:`x_{t+j}` on the basis of time :math:`t` information :math:`x_t`

Under particular conditions,  :math:`V_j` converges to

.. math::
    V_\infty = CC' + A V_\infty A'
    :label: eqob10

Equation :eq:`eqob10` is an example of a *discrete Lyapunov* equation in the covariance matrix :math:`V_\infty`

A sufficient condition for :math:`V_j` to converge is that the eigenvalues of :math:`A` be strictly less than one in modulus.

Weaker sufficient conditions for convergence  associate eigenvalues equaling or exceeding one in modulus with elements of :math:`C` that
equal :math:`0`




Forecasts of geometric sums
============================

In several contexts, we want to
compute forecasts of  geometric sums of future random variables governed by the linear state-space system :eq:`st_space_rep`

We want the following objects


*  Forecast of a geometric sum of future :math:`x`'s, or :math:`E_t \left[\sum_{j=0}^\infty \beta^j x_{t+j} | x_t \right]`

*  Forecast of a geometric sum of future :math:`y`'s, or :math:`E_t \left[\sum_{j=0}^\infty \beta^j y_{t+j} | x_t \right]`

These objects are important components of some famous and  interesting dynamic models.

    * For example, if :math:`\{y_t\}` is a stream of dividends, then :math:`E_t \left[\sum_{j=0}^\infty \beta^j y_{t+j} | x_t \right]` is a model of a stock price

    * Or if :math:`\{y_t\}` is  the money supply, then :math:`E_t \left[\sum_{j=0}^\infty \beta^j y_{t+j} | x_t \right]` is a  model of the price level

Formulas
========

Fortunately, it is easy to use a little matrix algebra to compute these objects

.. note::
   Useful fact: Suppose that the eigenvalues of :math:`A` are all bounded in modulus by :math:`\frac{1}{\beta}`.
   Then :math:`I + \beta A + \beta^2 A + \cdots = \left[I - \beta A \right]^{-1}`
   The assumption about the eigenvalues of :math:`A` assure that the series on the left converges.

Here are our formulas:



* Forecast of a geometric sum of future :math:`x`'s

.. math::
    E_t \left[\sum_{j=0}^\infty \beta^j x_{t+j} | x_t\right] = [I + \beta A + \beta^2 A^2 + \cdots \ ] x_t = [I - \beta A]^{-1} x_t

* Forecast of a geometric sum of future :math:`y`'s

.. math::
    E_t \left[\sum_{j=0}^\infty \beta^j y_{t+j} | x_t\right] = G [I + \beta A + \beta^2 A^2 + \cdots \ ] x_t = G[I - \beta A]^{-1} x_t


Things to do to complete the module
====================================

* Use an updated version of the python program signaprocessingtutorial_anmol.py to construct simulations to teach various lessons

    * Use the control system tools easily to create companion matrices.  This is illustrated in Anmol's program, but much more can be done.  Use it to generate all of the examples above and more.

    * For a given stochastic difference equation (e.g., the simple ar 1 in Anmol's program), compute averages and standard deviations across sample paths and compare them with population analogues

    * Use the simulations  to illustrate ergodicity -- give some examples where averages across time equal averages across simulations, and some finite T examples where they don't.  Emphasize the role of the initial distribution for :math:`x_0` in determining whether averages over times and averages across simulations are equal.

    * Create a teaser example of a nonstationary process that is one of Lars  Hansen's additive or multiplicative processes.  Show tranformation to make outcome stationary and ergodic.

* Create a concise but informative list of examples to simulate.  Create this list with an eye to doing somethings later with the Kalman filter with these same examples

* Create some examples forecasting  geometric sums. Define and describe the *resolvent operator*

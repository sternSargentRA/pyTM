.. _Lin_pred:

******************************************
Simple linear prediction theory
******************************************


.. epigraph::

    "We may regard the present state of the universe as the effect of its past and the cause of its future" -- Marquis de Laplace


Overview
============

This lecture introduces a linear state space system

Easy to use and embodies a powerful theory of prediction

A workhorse with many applications 

* representing dynamics of many higher-order systems

* predicting the position of a system :math:`j` steps into the future 

* predicting a geometric sum of future values of a variable like 

    * non financial income
    
    * dividends on a stock
      
    * the money supply
    
    * a government deficit or surplus
    
    * etc., etc., :math:`\ldots`
    
* key ingredient of important models 

    * Friedman's permanent income model of consumption smoothing

    * Barro's model of smoothing total tax collections
    
    * Rational expectations versions of Cagan's model of hyperinflation
    
    * Sargent and Wallace's `unpleasant monetarist arithmetic'
    
    * etc., etc., :math:`\ldots`
    
A Linear State Space Model
===============================

Objects in play are

* An :math:`n \times 1` vector :math:`x_t` denoting the *state* at time :math:`t`

* An :math:`m \times 1` vector of i.i.d. random variables :math:`\epsilon_{t+1} \sim {\cal N}(0,I)`

* A :math:`k \times 1` vector of *observations* :math:`y_t` at time :math:`t`

* An :math:`n \times n` matrix :math:`A` often called a *transition matrix*

* A :math:`n \times m` matrix :math:`C` sometimes called a *volatility matrix*

* A :math:`k \times n` matrix :math:`G`

Here is the linear state-space system

.. math::
        x_{t+1} & =  A x_t + C \epsilon_{t+1}   \\
        y_t &  =  G x_t 
        :label: st_space_rep
 
Convenient extension
=====================

We can equally well work with the assumption that :math:`\{\epsilon_{t+1}\}` is a *martingale difference sequence* meaning that it satisfies

.. math::
       E [\epsilon_{t+1} | x_t, x_{t-1}, \ldots ] = 0     
       
This is a weaker condition than that :math:`\epsilon` is vector of i.i.d. random variables satisfying :math:`\epsilon_{t+1} \sim {\cal N}(0,I)`
      
Examples
===========
      
Second-order difference equation
================================
.. math::
    y_{t+1} =  \alpha + \rho_1 y_t + \rho_2 y_{t-1} 
    :label: st_ex_1
    
To map :eq:`st_ex_1` into our state space system :eq:`st_space_rep`, we set

.. math::
    x_t= \left[
    \begin{array}{c} 1 \\ y_t \\ y_{t-1} \end{array}
    \right]
    \qquad    
    A = \left[\begin{array}{cc} \alpha & 0 & 0 \\ 
                              1 & 0 & 0  \\
                              0 & 1 & 0 \end{array} \right]
    \qquad
    C= \left[ \begin{array}{c} 0 \\ 0 \\ 0 \end{array}\right]
    \qquad
    G = \left[ \begin{array}{c} 0 & 1 & 0 \end{array}\right]


Experiment with note
^^^^^^^^^^^^^^^^^^^^^
.. note::

   This is a good idea
    
    
Univariate Autoregressive Processes
=====================================

We can use :eq:`st_space_rep` to represent the model

.. math:: 
   y_t = \alpha_1 y_{t-1} + \alpha_2 y_{t-2} + \alpha_3 y_{t-3} + \alpha_4  y_{t-4} + w_t 
   :label: eq_ar_rep
   
where :math:`w_t` is a martingale difference sequence.  We set :math:`n = 4, x_t = [y_t \
y_{t-1} \  y_{t-2} \  y_{t-3} ]^\prime` and

.. math::
   A = \left[ \begin{array}{cc} \alpha_1 & \alpha_2 & \alpha_3 &
   \alpha_4 \cr 1 & 0 & 0 & 0 \cr 0 & 1 & 0 & 0 \cr 0 & 0 & 1 & 0 \end{array}
   \right]  
   \qquad 
   C = \left[ \begin{array}{cc} 1 \cr 0 \cr 0 \cr 0 \end{array} \right]
   
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
``indeterministic'' seasonal, i.e., recurrent,
but aperiodic, seasonal fluctuations.


.. [#foot1]  For example, note that :math:`i = \exp\left(\pi/2 \right) + i \sin \left(\pi/2\right)`, so  the period associated
with :math:`i`  is :math:`{\frac{2 \pi}{\frac{\pi}{2}}} = 4`.
  
  
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
   
Hence :math:`x_t = \left[\begin{array}{cc}  t &1 \end{array}\right]^\prime`, so that the first component of $x_t$ is a linear
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


Prediction Theory
==================

The optimal forecast of :math:`x_{t+1}` given current information is

.. math::
   E(x_{t+1} | x_t) = Ax_t 
   :label: eqob2
and the one-step-ahead forecast error is

.. math::
   x_{t+1} - E(x_{t+1} \mid J_t) = C\epsilon_{t+1} 
   :label: eqob3 

The covariance matrix of :math:`x_{t+1}` conditioned on :math:`x_t` is 

.. math::
   E (x_{t+1} - E ( x_{t+1} | J_t) ) (x_{t+1} - E ( x_{t+1} | J_t))^\prime = CC^\prime 
   :label: eqob4 

A nonrecursive expression for :math:`x_t` as a function of
:math:`x_0, \epsilon_1, \epsilon_2, \ldots,  \epsilon_t` can be found by using :eq:`st_space_rep` repeatedly to obtain

.. math::  
   x_t & = Ax_{t-1} + C\epsilon_t \\
       & = A^2 x_{t-2} + AC\epsilon_{t-1} + C\epsilon_t \\
       & = \left[\sum_{\tau=0}^{t-1} A^\tau C\epsilon_{t-\tau} \right] + A^t x_0 
   :label: eqob5

Representation :eq:`eqob5` is a  *moving-average* representation.
It expresses :math:`\{x_t : t=1,2,\ldots\}` 
as a linear function of current and past values of the  process
:math:`\{w_t: t=1,2,\ldots\}` and an initial condition :math:`x_0`.

Covariance of Prediction Errors
================================


It is useful to obtain the covariance matrix of the :math:`j`-step-ahead prediction
error 

.. math::
   x_{t+j} - E_t x_{t+j} = \sum^{j-1}_{s=0} A^s C \epsilon_{t-s+j}. 
   :label: eqob8 
Evidently,

.. math:: 
   E_t (x_{t+j} - E_t x_{t+j}) (x_{t+j} - E_t x_{t+j})^\prime =   \sum^{j-1}_{k=0} A^k C C^\prime A^{k^\prime} \equiv V_j 
   :label: eqob9a 
   
Note that :math:`V_j` defined in :eq:`eqob9a` can be calculated recursively via

.. math:: 
   V_1 &= CC^\prime \\
   V_j &= CC^\prime + A V_{j-1} A^\prime, \quad j \geq 2 
   :label: eqob9b 
   
For :math:`j \geq 1`,  :math:`V_j` is the conditional covariance matrix of the errors in forecasting
:math:`x_{t+j}` on the basis of time :math:`t` information :math:`x_t` 

A steady-state covariance matrix satisfies

.. math::
    V_\infty = CC' + A V_\infty A' 
    :label: eqob10
    
Equation :eq:`eqob10` is an example of a *discrete Lyapunov* equation in the covariance matrix :math:`v_\infty`




     
Some things we'd like to compute
================================

Here are some things that we want to compute

* :math:`j`-step ahead forecast of :math:`x`: :math:`E_t x_{t+j} \equiv E [x_{t+j} | x_t] = E [x_{t+j} | x_t, x_{t-1}, \ldots \ ]`

* :math:`j`-step ahead forecast of :math:`y`: :math:`E_t y_{t+j} \equiv E [y_{t+j} | x_t] = E [y_{t+j} | x_t, x_{t-1}, \ldots  \ ]`

*  Forecast of a geometric sum of future :math:`x`'s, or :math:`E_t \left[\sum_{j=0}^\infty \beta^j x_{t+j} | x_t \right]`

*  Forecast of a geometric sum of future :math:`y`'s, or :math:`E_t \left[\sum_{j=0}^\infty \beta^j y_{t+j} | x_t \right]`

We want to compute these and other objects because they are important components of some interesting dynamic models.

    * For example, if :math:`\{y_t\}` is a stream of dividends, then :math:`E_t \left[\sum_{j=0}^\infty \beta^j y_{t+j} | x_t \right]` is a model of a stock price

    * Or if :math:`\{y_t\}` is a the money supply, then :math:`E_t \left[\sum_{j=0}^\infty \beta^j y_{t+j} | x_t \right]` could be a model of the price level

Formulas for things we'd like to compute
==========================================
Fortunately, it is easy to use a little matrix algebra to compute these objects

.. note::
   Useful fact: Suppose that the eigenvalues of :math:`A` are all bounded in modulus by :math:`\frac{1}{\beta}`.  Then :math:`I + \beta A + \beta^2 A + \ldots = \left[I - \beta A \right]^{-1}`
   The assumption about the eigenvalues of :math:`A` assure that the series on the left converges.  

Here are our formulas:



* :math:`j`-step ahead forecast of :math:`x`: :math:`E_t x_{t+j} \equiv E [x_{t+j} | x_t] = E [x_{t+j} | x_t, x_{t-1}, \ldots \ ]`

.. math:: 
    E_t x_{t+j} = A^j x_t

* :math:`j`-step ahead forecast of :math:`y`: :math:`E_t y_{t+j} \equiv E [y_{t+j} | x_t] = E [y_{t+j} | x_t, x_{t-1}, \ldots \ ]`

.. math:: 
    E_t y_{t+j} = G A^j x_t

* Forecast of a geometric sum of future :math:`x`'s   
    
.. math::
    E_t \left[\sum_{j=0}^\infty \beta^j x_{t+j} | x_t\right] = [I + \beta A + \beta^2 A^2 + \cdots \ ] x_t = [I - \beta A]^{-1} x_t 
    
* Forecast of a geometric sum of future :math:`y`'s   
    
.. math::
    E_t \left[\sum_{j=0}^\infty \beta^j y_{t+j} | x_t\right] = G [I + \beta A + \beta^2 A^2 + \cdots \ ] x_t = G[I - \beta A]^{-1} x_t    
                                 
   

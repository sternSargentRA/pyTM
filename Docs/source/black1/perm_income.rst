.. _LQmodel:

The LQ permanent income model
======================================

This lecture describes the infinite-horizon linear-quadratic savings problem

Its  solution is a rational expectations version of the famous permanent income model of Friedman (1956)

Hall (1978) cast Friedman' model within the linear-quadratic setting

We use the model as a vehicle for illustrating

   * impulse response functions
   
   * alternative formulations of the *state* of a dynamic system
   
   * the idea of *cointegration*
   
   * the idea that changes in consumption are useful as predictors of movements in income 


The savings problem
---------------------
   

A consumer has preferences over consumption streams that are ordered by the utility functional

.. math::
  E_0 \sum_{t=0}^\infty \beta^t u(c_t)
  :label: sprob1

where 

    *  :math:`E_t` is the mathematical expectation conditioned on the consumer's time :math:`t` information
    
    *  :math:`c_t` is time :math:`t` consumption
    
    *  :math:`u(c)` is a strictly concave one-period utility function
    
    *  :math:`\beta \in (0,1)` is a discount factor 

The consumer maximizes :eq:`sprob1` by choosing a consumption, borrowing plan :math:`\{c_t, b_{t+1}\}_{t=0}^\infty` subject to the sequence of budget constraints

.. math::
  c_t + b_t = R^{-1} b_{t+1}  + y_t
  :label: sprob2

where 

     *  :math:`y_t` is an exogenous stationary endowment process
    
     *  :math:`R` is a constant gross risk-free interest rate
     
     *  :math:`b_t` is one-period risk-free debt maturing at :math:`t`
     
     *  :math:`b_0` is a given initial condition. 


.. note::
    For the remainder of this lecture, we shall follow Friedman XXXXX and Hall XXXX and assume that :math:`R^{-1} = \beta`. 
    
    
We shall  assume that the endowment process has the state-space representation

.. math::
    z_{t+1} & = A_{22} z_t + C_2 w_{t+1} \\
                  y_t & = U_y  z_t
    :label: sprob15ab


where

   *  :math:`w_{t+1}` is an i.i.d. process with mean zero and identity contemporaneous covariance matrix
   
   *  :math:`A_{22}` is a stable matrix, its eigenvalues being strictly below unity in modulus
   
   *  :math:`U_y` is a selection vector that pins down :math:`y` with a particular linear combination of the :math:`z_t`.

We impose the following condition on the consumption, borrowing plan:

.. math::
  E_0 \sum_{t=0}^\infty \beta^t b_t^2 < +\infty
  :label: sprob3

Condition :eq:`sprob3` suffices to rule out *Ponzi schemes*

The *state* vector confronting the household at :math:`t` is :math:`\left[\matrix{b_t & z_t\cr}\right]'`

   *  :math:`b_t` is the household's one-period debt falling due at the beginning oferiod :math:`t` 
   
   *  :math:`z_t` contains all variables useful for forecasting the household's future endowment

We impose condition :eq:`sprob3` to rule out an always-borrow scheme that would allow the household to enjoy unbounded or bliss consumption  forever.

First-order conditions for maximizing :eq:`sprob1` subject to :eq:`sprob2` are 

.. math::
  E_t u'(c_{t+1}) = u'(c_t) , \ \ \forall t \geq 0
  :label: sprob4

  
Quadratic preferences
----------------------

For the rest of this lecture we assume the quadratic utility function :math:`u(c_t) =  -.5 (c_t - \gamma)^2`, where :math:`\gamma` is a bliss level of consumption. 

Along with this quadratic utility specification, we allow consumption :math:`c_t` to be negative. 

.. note::
    One way to solve the consumer's problem is to apply *dynamic programming*  as in lecture XXXXX.  We do this later. But first we use an alternative approach that is revealing and shows the work that dynamic programming does for us automatically


First-order conditions :eq:`sprob4` imply [#f2]_

.. math::
  E_t c_{t+1} = c_t
  :label: sprob5

To deduce the optimal decision rule, we want to solve the system of difference equations formed by :eq:`sprob2` and :eq:`sprob5` subject to the boundary condition :eq:`sprob3`. 

To accomplish this, solve :eq:`sprob2` forward and impose :math:`\lim_{T\rightarrow +\infty} \beta^T b_{T+1} =0` to get

.. math::
  b_t = \sum_{j=0}^\infty \beta^j (y_{t+j} - c_{t+j})
  :label: sprob6

Imposing :math:`\lim_{T\rightarrow +\infty} \beta^T b_{T+1} =0` suffices to impose :eq:`sprob3` on the debt path. 

Take conditional expectations on both sides of :eq:`sprob6` and use  the *law of iterated expectations* to deduce

.. math::
   b_t = \sum_{j=0}^\infty \beta^j E_t y_{t+j} - {1 \over 1-\beta} c_t
   :label: sprob7

or

.. math::
   c_t = (1-\beta) \left[ \sum_{j=0}^\infty \beta^j E_t y_{t+j} - b_t\right]
   :label: sprob8

If we define the *net rate of interest* :math:`r` by :math:`\beta =\frac{1}{1+r}`, we can also express this equation as

.. math::
   c_t = {r \over 1+r}
   \left[ \sum_{j=0}^\infty \beta^j E_t y_{t+j} - b_t\right]
   :label: sprob9

Equation :eq:`sprob8` or :eq:`sprob9` asserts that  consumption  equals economic *income*

   * *financial wealth* equals :math:`b_t`
   
   * *non-financial* wealth equals :math:`\sum_{j=0}^\infty \beta^j E_t y_{t+j}`
   
   * A *marginal propensity to consume out of wealth* equals the  interest factor :math:`\frac{r}{1+r}`
   
   * *economic income* equals  a constant marginal propensity to consume  times the sum of nonfinancial wealth and financial wealth 

Notice that :eq:`sprob9` represents :math:`c_t` as a function of the *state* :math:`[b_t, z_t]` confronting the household.

Here :math:`z_t` contains all information useful for forecasting the household's endowment process.

Another enlightening representation
------------------------------------

We can regard :math:`z_t, b_t` as the time :math:`t` *state*

   *  :math:`z_t` is an *exogenous* component 
   
   *  :math:`b_t` is an *endogenous* component 

A linear state-space system governing consumption can be represented as

.. math::
  z_{t+1} & = A_{22} z_t + C_2 w_{t+1} \\
  b_{t+1} & = b_t + U_y [ (I -\beta A_{22})^{-1} (A_{22} - I) ] z_t \\
  y_t & = U_y z_t \\
  c_t & = (1-\beta) [ U_y(I-\beta A_{22})^{-1} z_t - b_t ]

Another way to understand the solution is to show that *after* the optimal decision rule has been obtained, there is a point of view that allows us to regard the state as being :math:`c_t` together with :math:`z_t` and to regard :math:`b_t` as an outcome. 

Following Hall (1978), this is a sharp way to summarize the implication of the LQ permanent income theory. 

To represent the solution for :math:`b_t`, substitute :eq:`sprob8` into :eq:`sprob2` and after
rearranging obtain

.. math::
   b_{t+1} = b_t +\left({\beta^{-1} -1}\right) \sum_{j=0}^\infty \beta^j E_t y_{t+j} - \beta^{-1} y_t.
   :label: sprob10

Next, shift :eq:`sprob8` forward one period and eliminate :math:`b_{t+1}` by using :eq:`sprob2` to obtain

.. math::
   c_{t+1} = (1-\beta)\sum_{j=0}^\infty  E_{t+1} \beta^j y_{t+j+1} - (1-\beta)[\beta^{-1} (c_t + b_t - y_t)]

If we add and subtract :math:`\beta^{-1} (1-\beta) \sum_{j=0}^\infty \beta^j E_t y_{t+j}` from the right side of the preceding equation and rearrange, we obtain

.. math::
   c_{t+1} - c_t = (1-\beta) \sum_{j=0}^\infty \beta^j (E_{t+1} y_{t+j+1} - E_t y_{t+j+1} )
   :label: sprob11

The right side is the time :math:`t+1` *innovation to the expected present value* of the endowment process :math:`y`.

It is useful to express this innovation in terms of a moving average representation [#f4]_ for income :math:`y_t`.

Suppose that the endowment process has the moving average representation

.. math::
  y_{t+1} = d(L) w_{t+1}
  :label: sprob12

where

   *  :math:`w_{t+1}` is an i.i.d. vector process with :math:`E w_{t+1} =0` and contemporaneous covariance matrix :math:`E w_{t+1} w_{t+1}'=I`
   
   *  :math:`d(L) = \sum_{j=0}^\infty d_j L^j`, where :math:`L` is the lag operator
   
   *  at time :math:`t`,  the household has an information set [#f5]_ :math:`w^t = [w_t, w_{t-1}, \ldots ]`  

Then notice that

.. math::
   y_{t+j} - E_t y_{t+j} = d_0 w_{t+j} + d_1 w_{t+j-1} + \cdots + d_{j-1} w_{t+1}

It follows that

.. math::
   E_{t+1} y_{t+j} - E_t y_{t+j} = d_{j-1} w_{t+1}
   :label: sprob120

Using :eq:`sprob120` in :eq:`sprob11` gives

.. math::
  c_{t+1} - c_t = (1-\beta) d(\beta) w_{t+1}
  :label: sprob13

The object :math:`d(\beta)` is the *present value of the moving average coefficients* in the representation for the endowment process :math:`y_t`.

We conclude that we can represent the optimal decision rule for :math:`c_t, b_{t+1}` in the form of the two equations :eq:`sprob11` and :eq:`sprob7` that  we repeat here:

.. math::
   c_{t+1} = c_t + (1-\beta) \sum_{j=0}^\infty \beta^j (E_{t+1} y_{t+j+1} - E_t y_{t+j+1} )
   :label: sprob11aa

.. math::
   b_t  &= \sum_{j=0}^\infty \beta^j E_t y_{t+j} - {1 \over 1-\beta} c_t .
   :label: sprob7aa

Equation :eq:`sprob7aa` asserts that the household's debt due at :math:`t` equals the expected present value of its endowment minus the expected present value of its consumption stream. 

A high debt thus indicates a large expected present value of surpluses :math:`y_t - c_t`.

Recalling the form of the endowment process , we can compute

.. math::
  E_t \sum_{j=0}^\infty \beta^j z_{t+j} &= (I-\beta A_{22})^{-1} z_t \\
  E_{t+1} \sum_{j=0}^\infty \beta^j z_{t+j+1} & = (I -\beta A_{22})^{-1} z_{t+1} \\
  E_t \sum_{j=0}^\infty \beta^j z_{t+j+1} & = (I - \beta A_{22})^{-1} A_{22} z_t

Using  these formulas together with :eq:`sprob15ab` and substituting  into :eq:`sprob11aa` and :eq:`sprob7aa`  gives the following representation for the consumer's optimum decision rule:

.. math::
  c_{t+1} & = c_t + (1-\beta) U_y  (I-\beta A_{22})^{-1} C_2 w_{t+1} \\
  b_t & = U_y (I-\beta A_{22})^{-1} z_t - {1 \over 1-\beta} c_t \\
  y_t & = U_y z_t \\
  z_{t+1} & = A_{22} z_t + C_2 w_{t+1}
  :label: sprob16abcd

Representation :eq:`sprob16abcd` reveals several things about the optimal decision rule. 

    1. The *state* consists of the endogenous part :math:`c_t` and the exogenous part :math:`z_t`. These contain all of the relevant information for forecasting future :math:`c,y, b`.
    
    2. Financial assets :math:`b_t` have disappeared as a component of the state because they are properly encoded in :math:`c_t`. 
   
    3. According to :eq:`sprob16abcd`, consumption is a random walk with innovation :math:`(1-\beta) d(\beta)w_{t+1}` as implied also by :eq:`sprob13`.
    
    4. The random walk outcome confirms that the Euler equation :eq:`sprob5` is built into the solution. 
    
    5. That consumption is a random walk of course implies that it does not possess an asymptotic stationary distribution, at least so long as :math:`z_t` exhibits perpetual random fluctuations, as it will generally under :eq:`sprob15ab`. This feature is inherited partly from the assumption that :math:`\beta R =1`.
    
    6. The impulse response function of :math:`c_t` is a box: for all :math:`j\geq 1`, the response of :math:`c_{t+j}` to an increase in the innovation :math:`w_{t+1}` is :math:`(1-\beta) d(\beta) = (1-\beta) U_y (I -\beta A_{22})^{-1} C_2`. 
    
    7. Solution :eq:`sprob16abcd` reveals that the joint process :math:`c_t,b_t` possesses the property that Granger and Engle (1987) called *cointegration*. 
    
    
Cointegration
--------------

System :eq:`sprob16abcd` is a good example of a system from economic theory that nicely illustrates the idea of co-integration.

In particular, *both* :math:`c_t` and :math:`b_t` are non-stationary because they have unit roots (see representation :eq:`sprob10` for :math:`b_t`).

But there is a linear combination of :math:`c_t, b_t` that *is* asymptotically stationary provided that :math:`z_t` is asymptotically stationary.

From :eq:`sprob7aa`, a linear combination that is stationary is :math:`(1-\beta) b_t + c_t`.

Accordingly, Granger and Engle would call :math:`\left[\matrix{(1-\beta) & 1 \cr}\right]` a *cointegrating vector* that, when applied to the nonstationary vector process :math:`\left[ \matrix{b_t  & c_t \cr}\right]'`, yields a process that is asymptotically stationary. 

Equation :eq:`sprob7` can be arranged to take the form

.. math::
   (1-\beta) b_t + c_t = (1-\beta) E_t \sum_{j=0}^\infty \beta^j y_{t+j},
   :label: sprob77

Equation :eq:`sprob77`  asserts that the *cointegrating residual*  on the left side equals the conditional expectation of the geometric sum of future incomes on the right. [#f8]_

.. _sub_debt_dynamics:

Debt dynamics
-------------

If we subtract the equation for :math:`b_t` in equation :eq:`sprob16abcd` evaluated at time
:math:`t` that equation evaluated at time :math:`t+1`, we obtain

.. math::
  b_{t+1}- b_t = U_y (I-\beta A_{22})^{-1} (z_{t+1} - z_t) - {\frac{1}{1-\beta}}(c_{t+1} - c_t ) .

Substituting :math:`z_{t+1} - z_t = (A_{22} - I )z_t + C_2 w_{t+1}` and the equation for :math:`c_{t+1}` from :eq:`sprob16abcd` into the above equation and rearranging gives

.. math::
  b_{t+1} - b_t =U_y (I - \beta A_{22})^{-1} (A_{22} - I) z_t
  :label: debt_evolution


.. _sub_classic_consumption:

Two classic examples
--------------------

We illustrate formulas :eq:`sprob16abcd` with the following two examples. In both examples, the endowment follows the process :math:`y_t = z_{1t} + z_{2t}` where

.. math::
  \begin{bmatrix} z_{1 t+1} \\ z_{2t+1}\end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1\end{bmatrix}\begin{bmatrix}z_{1t} \\z_{2t} \end{bmatrix} + \begin{bmatrix} \sigma_1 & 0 \\ 0 & \sigma_2 \end{bmatrix} \begin{bmatrix}w_{1t+1} \\w_{2t+1} \end{bmatrix}

where :math:`w_{t+1}` is an i.i.d. :math:`2 \times 1` process distributed as :math:`{\cal N}(0,I)`. 

    *  Here :math:`z_{1t}` is a permanent component of :math:`y_t` while :math:`z_{2t}` is a purely transitory component.

**Example 1.** Assume that the consumer observes the state :math:`z_t` at time :math:`t`.

This implies that the consumer can construct :math:`w_{t+1}` from observations of :math:`z_{t+1}` and :math:`z_t`.

Application of formulas :eq:`sprob16abcd` implies that

.. math::
  c_{t+1} - c_t = \sigma_1 w_{1t+1} + (1-\beta) \sigma_2 w_{2t+1}
  :label: consexample1

Since :math:`1-\beta = {\frac{r}{1+r}}` where :math:`R = (1+r)`, formula :eq:`consexample1` shows how an increment :math:`\sigma_1 w_{1t+1}` to the permanent component of income :math:`z_{1t+1}` leads to a permanent one-for-one increase in consumption and no increase in savings :math:`-b_{t+1}`;

But the purely transitory component of income :math:`\sigma_2 w_{2t+1}` leads to a permanent increment in consumption by a fraction :math:`(1-\beta)` of transitory income, while the remaining fraction :math:`\beta` is saved, leading to a permanent increment in :math:`-b`. 

Application of formula :eq:`debt_evolution` to this example shows that

.. math::
  b_{t+1} - b_t = - z_{2t} = - \sigma_2 w_{2t}
  :label: consexample1a

which confirms that none of :math:`\sigma_1 w_{1t}` is saved, while all of :math:`\sigma_2 w_{2t}` is saved.

**Example 2.** Assume that the consumer observes :math:`y_t`, and its history up to :math:`t`, but not :math:`z_t` at time :math:`t`. 

Under this assumption, it is appropriate to use an *innovation representation* to form :math:`A_{22}, C_2, U_y` in formulas :eq:`sprob16abcd`.

In particular, from our study of example XXXXX with the *Kalman filter* XXXXXX,  the pertinent state space representation for :math:`y_t` is

.. math::
  \begin{bmatrix}y_{t+1} \\ a_{t+1} \end{bmatrix} &= \begin{bmatrix}1 & -(1 - K) \\ 0 & 0 \end{bmatrix} \begin{bmatrix}y_t \\ a_t \end{bmatrix} + \begin{bmatrix} 1 \\ 1\end{bmatrix}a_{t+1} \\
  y_t &= \begin{bmatrix}1 & 0 \end{bmatrix} \begin{bmatrix}y_t \\ a_t \end{bmatrix}

where :math:`K` is the Kalman gain and :math:`a_t = y_t - E [ y_t | y^{t-1}]`.

From lecture XXXX on the Kalman filter,  we know that :math:`K \in [0,1]` and that :math:`K` increases as :math:`\Bigl(\frac{\sigma_1^2}{\sigma_2^2}\Bigr)` increases, i.e., as the ratio of the variance of the permanent shock to the variance of the transitory shock to income increases. 

Applying formulas :eq:`sprob16abcd` implies

.. math::
  c_{t+1} - c_t = [1-\beta(1-K) ] a_{t+1}
  :label: consexample2

where the endowment process can now be represented in terms of the univariate innovation to :math:`y_t` as

.. math::
  y_{t+1} - y_t = a_{t+1} - (1-K) a_t.
  :label: incomemaar

Equation :eq:`incomemaar` indicates that the consumer regards a fraction :math:`K` of an innovation :math:`a_{t+1}` to :math:`y_{t+1}` as *permanent* and a fraction :math:`1-K` as purely transitory. 

The consumer permanently increases his consumption by the full amount of his estimate of the permanent part of :math:`a_{t+1}`, but by only :math:`(1-\beta)` times his estimate of the purely transitory part of :math:`a_{t+1}`. 

Therefore, in total he permanently increments his consumption by a fraction :math:`K + (1-\beta) (1-K) = 1 - \beta (1-K)` of :math:`a_{t+1}`. 

He saves the remaining fraction :math:`\beta (1-K)` of :math:`a_{t+1}`. 

According to equation :eq:`incomemaar`, the first difference of income is a first-order moving average.

Equation  :eq:`consexample2` asserts that the first difference of consumption is i.i.d. 

Application of formula to this example shows that

.. math::
  b_{t+1} - b_t = (K-1) a_t,
  :label: consexample1b

which indicates how the fraction :math:`K` of the innovation to :math:`y_t` that is regarded as permanent influences the fraction of the innovation that is saved.

Spreading consumption cross section
-----------------------------------

Starting from an arbitrary initial distribution for :math:`c_0` and say the asymptotic stationary distribution for :math:`z_0`, if we were to apply formulas for the unconditonal  means and variances XXXXX from lecture XXXXX, the common unit root affecting :math:`c_t, b_t` would cause the time :math:`t` variance of :math:`c_t` to grow linearly with :math:`t`. 

If we think of the initial distribution as describing the joint distribution of :math:`c_0, b_0` for a cross section of ex ante identical households born at time :math:`0`, then these formulas would describe the evolution of the cross-section for :math:`b_t, c_t` as the population of households ages. 

The distribution would spread out. [#f9]_

.. FIXME: the references to equations diff6 and ydiff2 are not defined because they come from RMT section 2.4


.. rubric:: Footnotes

.. [#f2] A linear marginal utility is essential for deriving :eq:`sprob5` from :eq:`sprob4`.  Suppose instead that we had imposed the following more standard assumptions on the utility function: :math:`u'(c) >0, u''(c)<0, u'''(c) > 0` and required that :math:`c \geq 0`.  The Euler equation remains :eq:`sprob4`. But the fact that :math:`u''' <0` implies via Jensen's inequality that :math:`E_t u'(c_{t+1}) >  u'(E_t c_{t+1})`.  This inequality together with :eq:`sprob4` implies that :math:`E_t c_{t+1} > c_t` (consumption is said to be a 'submartingale'), so that consumption stochastically diverges to :math:`+\infty`.  The consumer's savings also diverge to :math:`+\infty`.  
.. [#f4] Representation :eq:`sprob15ab` implies that :math:`d(L) = U_y (I - A_{22} L)^{-1} C_2`.
.. [#f5] A moving average representation for a process :math:`y_t` is said to be *it fundamental* if the linear space spanned by :math:`y^t` is equal to the linear space spanned by :math:`w^t`.  A time-invariant innovations representation, attained via the Kalman filter, is by construction fundamental.
.. [#f8] See Campbell and Shiller (1988) and  Lettau and Ludvigson (2001, 2004) for interesting applications of related ideas.
.. [#f9] See Deaton and Paxton (1994) and Storesletten, Telmer, and  Yaron (2004) for evidence that cross section distributions of consumption spread out with age.

.. NOTE: in #f2, #f3, #f5, #f6, #f7 I had to hardcode some names

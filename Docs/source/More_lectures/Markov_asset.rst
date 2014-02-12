Asset Pricing in a Markov Environment
=====================================

This lecture describes the famous Lucas asset pricing model

[Lucas1978]_

Lucas allowed a continuous state Markov process for the state

To simplify things, we study a special casein which the state is governed by a discrete state Markov chain

The finite state Markov setting emulates 

[MehraPrescott1985]_



The model tells  how the price of a "Lucas tree" is determined in a pure exchange economy 

The economy features

   *  a representative agent 
   
   *  time-separable preferences over a single good 
   
   *  The evolution of the consumption endowment is  described by a discrete state Markov chain
   
Key tools for studying the economy are

   * Bellman equations 

   * Formulas for predicting future values of functions of a Markov state
   
   * A formula for predicting the discounted sum of future values of a Markov state 

Reminders about prediction formulas for  Markov chains
-----------------------------------------------------------

Let :math:`P` be an :math:`n \times n` stochastic matrix with

.. math::
     P_{ij} = {\rm Prob} (x_{t+1} = e_j | x_t = e_i )
     
where :math:`e_i` is the :math:`i` th unit vector. 

We are said to be "in state :math:`i`" when :math:`x_t = e_i`

Let :math:`\bar y` be an :math:`n \times 1` vector with the interpretation that :math:`y_t = \bar y_i` if :math:`x_t = e_i`

Here are some useful prediction formulas:

.. math::
       E (y_{t+1} | x_t = e_i ) &  = \sum_j P_{ij} \bar y_j = (P \bar y)_i \cr
       E (y_{t+k} | x_t = e_i ) & = \sum_j P_{ij}^{(k)} \bar y_j = (P^k \bar y)_i\cr
           \vdots  \quad \quad  & \quad \quad \vdots \cr
       E \bigl[\sum_{j=0}^\infty \beta^j y_{t+j} | x_t = e_i \bigr] & = [(I - \beta P)^{-1} \bar y]_i \cr
       
where :math:`P_{ij}^{(k)}` is the :math:`ij` element of :math:`P^k` and

.. math::
      (I - \beta P)^{-1}  = I + \beta P + \beta^2 P^2 + \cdots
      
Premultiplication  by :math:`(I - \beta P)^{-1}` amounts to "applying the *resolvent operator*"      

      
Basic setup 
---------------------

    
There is a single *non storable* consumption good at each :math:`t \geq 0`

Lucas studied a pure exchange economy with a representative agent

*pure exchange* means that all endowments are exogenous

For Lucas, *representative agent* meant that either

    * There is a single consumer (sometimes also referred to as a household), or
    
    * When there is more than one consumer,  all consumers have *identical* endowments and preferences 

Either way, the assumption of a representative agent eradicates all motives and opportunities for trade

This makes it very easy to compute competitive equilibrium prices



Details
--------
      
   
A  representative consumer ranks consumption streams according to the utility functional

.. math::
     E_0 \sum_{t=0}^\infty \beta^t U (C_t)
     
where 

    * :math:`C_t` is consumption 
    
    * :math:`\beta \in (0,1)` is a fixed discount factor
    
    * :math:`U(C) = \frac{C^{1-\gamma}}{1-\gamma}` for :math:`\gamma > 0`, where :math:`\gamma` is the coefficient of relative risk aversion
    
In our version  of the model, we'll assume that the consumer's endowment of the consumption  good  follows the process

.. math:: Y_{t+1} = \lambda_{t+1} Y_t 

where :math:`\lambda_t` is governed by an :math:`n` state discrete Markov chain with transition matrix :math:`P`  

We assume that

    * :math:`\lambda_t = \bar \lambda_i` when the economy is in state :math:`i` (i.e., when :math:`x_t = e_i`)
    
    * :math:`{\rm Prob} (\lambda_{t+1} = \bar \lambda_j | \lambda_t = \bar \lambda_i) = P_{ij}`

Key Insights
^^^^^^^^^^^^^

Since it is a pure exchange economy, in any competitive equilibrium, prices must adjust so that the representative consumer is content to consume his or her endowment:

.. math::
   C_t = Y_t \quad \forall t \geq 0
    
It follows, that :math:`C_t`  obeys the same stochastic process as the endowment, so 

.. math:: 
   C_{t+1} = \lambda_{t+1} C_t 

Following Lucas, we can read competitive equilibrium prices of any state-contingent claim by evaluating marginal utilities at the endowment

For example, if at time :math:`t`, state :math:`lambda_t`  the consumer could trade a claim to  one unit of  date :math:`t+1`, state :math:`\lambda_{t+1}`
consumption at price :math:`Q(\lambda_{t+1},\lambda_t)`,
the price would have to be

.. math::
    Q(\lambda_{t+1},\lambda_t) = \beta \frac{U'(C_{t+1})}{U'(C_t)} {\rm Prob}(\lambda_{t+1} | \lambda_t )
    :label: Arrowprice
    
in order for him to be content to consume his endowment at each date and state

Here :math:`Q(\lambda_{t+1},\lambda_t)` is the price of a one-period-ahead *Arrow security*


      
Asset pricing with Markov geometric consumption growth
------------------------------------------------------------------

Take a Lucas asset pricing model 

We'll price several assets

   * A Lucas tree
   
   * A consol (a type of bond issued by the UK in the 19th century)
   
   * An infinite horizon call option on a consol



Pricing a "Lucas tree"
^^^^^^^^^^^^^^^^^^^^^^

A "Lucas tree" is a claim on the consumption  endowment.  

The "dividend'' on the Lucas tree is :math:`Y_t = C_t`

We'll  price an  "ex dividend" claim on a Lucas tree meaning that,
  
     *  the seller retains  this period's dividend
     
     *  the buyer pays :math:`p_t` today to purchase a claim on 
     
         * :math:`C_{t+1}` and
         
         * the right to sell the claim tomorrow at price :math:`p_{t+1}`
 
The price :math:`p_t`  of an ex dividend  Lucas tree satisfies

.. math::
    p_t &= \sum_{\lambda_{t+1}} \Bigl[ Q(\lambda_{t+1}|\lambda_t ) (C_{t+1} + p_{t+1} ) \Bigr] \cr
    p_t & = E_t \Bigl[ \beta \frac{U'(C_{t+1})}{U'(C_t)} ( C_{t+1} + p_{t+1} ) \Bigr]  \cr
    p_t    & = E_t \Bigl[  \beta \Bigl(\frac{ C_{t+1}}{C_t} \Bigr)^{-\gamma} [ Y_{t+1} + p_{t+1}] \Bigr]
   :label: Lucas1
        
Guess a pricing function  of the form 

.. math::
    p_t = v(\lambda_t) C_t   
    :label: guess1
    
If we substitute this guess into :eq:`Lucas1` and rearrange we obtain

.. math::
     v(\lambda_t) C_t & = E_t \Bigl[ \beta \lambda_{t+1}^{-\gamma} (C_{t+1} + C_{t+1} v(\lambda_{t+1}) )\Bigr] \cr
                      & = E_t \Bigl[ \beta \lambda_{t+1}^{-\gamma} \lambda_{t+1} (1 + v(\lambda_{t+1})) C_t \Bigr] 
                      
It follows that 

.. math:: 
     v(\lambda_t) = E_t \Bigl[ \beta \lambda^{1-\gamma} (1 + \lambda_{t+1}) \Bigr]
     
or

.. math::
     \bar v_i = \beta \sum_{j=1}^n P_{ij} \lambda_j^{1-\gamma} ( 1 + \bar v_j )
     :label: Lucas101
     
where 

.. math::
     \bar v_i = v(\bar \lambda_i)
     
Thus,  we can write :eq:`Lucas101` as

.. math:: 
    \bar v = \beta \tilde P {\bf 1} + \beta \tilde P \bar  v
   :label: resolvent1
   
where :math:`\bar v` is an :math:`n \times n` vector, :math:`{\bf 1}` is an :math:`n \times 1` vector of ones,  and

.. math::
    \tilde P_{ij} = P_{ij} \lambda_j^{1-\gamma}
    
Finally, we can use a von Neuman series (or apply a resolvent operator) to solve  :eq:`resolvent1`:

.. math::
   \bar v = \beta (I - \beta \tilde P)^{-1} \tilde P {\bf 1}
   :label: resolvent2
    
    
A risk-free consol
^^^^^^^^^^^^^^^^^^^

Consider the same pure exchange representative agent economy

A risk-free consol promises to pay a constant amount  :math:`\zeta> 0` each period

Recycling notation,  let :math:`p_t` now be the price of an  ex-coupon claim to the consol

An ex-coupon claim to the consol entitles the owner at the end of period :math:`t` to

   * :math:`\zeta` in period :math:`t+1`, plus
   
   * the right to sell the claim for :math:`p_{t+1}` next period

The price satisies

.. math::
    U'(C_t) p_t = \beta E_t \Bigl[ U'(C_{t+1}) \zeta + U'(C_{t+1}) p_{t+1} \Bigr]
    
Substituting :math:`U'(C) = C^{-\gamma}` into the above equation yields

.. math::
    C_t^{-\gamma} p_t & = \beta E_t \Bigl[ C_{t+1}^{-\gamma} (\zeta + p_{t+1}) \Bigr] = \beta C_t^{-\gamma} E_t \Bigl[ \lambda_{t+1}^{-\gamma} (\zeta + p_{t+1}) \Bigr] \cr
                      
It follows that

.. math:: 
     p_t  = \beta E_t \bigl[ \lambda_{t+1}^{-\gamma} (\zeta + p_{t+1} ) \bigr]
     :label: consolguess1
     
Now *guess* that the price takes the form 

.. math::
    p_t = p(\lambda_t) = \bar p_i \quad {\rm when} \lambda_t = \bar \lambda_i
   
Then :eq:`consolguess1` becomes

.. math::
   \bar  p_i = \beta \sum_j (P_{ij}\lambda^j) (\zeta + \bar p_j )
     
which can be expressed as

.. math::
    \bar p = \beta \check P \zeta {\bf 1} + \beta \check P) \bar p
  
or

.. math::
   \bar p = \beta (I - \beta \check P)^{-1} \check P \zeta {\bf 1}
   :label: consol_price
   
where

.. math::
    \check  P_{ij} = P_{ij} \lambda_j^{-\gamma}
    
and :math:`{\bf 1}` is again an :math:`n \times 1` vector of ones
    
Pricing an option to purchase the consol
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We now want to price an infinite horizon  option to purchase a consol at a price :math:`p_S`

This is termed a *call option*

It is said to have a *strike price* :math:`p_S`

The owner of the option is entitled to purchase the consol at the price :math:`p_S` at the beginning of any period, after the coupon has been paid to the previous owner of the bond
           
The economy  is identical with the one above

Let :math:`w(\lambda_t, p_S)` be the value of the option when the initial growth state is :math:`\lambda_t`

Recall that :math:`p(\lambda_t)` is the value of the consol when the initial growth state is :math:`\lambda_t`

The value of the option satisfies the equation

.. math::
    U'(C_t) w(\lambda_t, p_S) & = \max \Bigl[ \beta E_t U'(C_{t+1}) w(\lambda_{t+1}, p_S), U'(C_t) (\bar p(\lambda_t) - p_S) \Bigr] \cr
    C_t^{-\gamma} w(\bar \lambda_i, p_S) & = \max \Bigl[ \sum_{j=1}^n \beta P_{ij} \bar \lambda_j^{-\gamma} C_t^{-\gamma} w(\bar \lambda_j, p_S), C_t^{-\gamma} (\bar p(\lambda_j) - p_S) \Bigr]
    
or

.. math::
    w(\bar \lambda_i, p_S) = \max \bigl[ \beta \sum_{j=1}^n (P_{ij} \bar \lambda_j^{\gamma}) w (\bar \lambda_j, p_S), p(\bar \lambda_j) - p_S \bigr]
    :label: FEoption0
    
Let :math:`\hat P_{ij} = P_{ij} \lambda^{-\gamma}_j` and :math:`\bar w_i = w(\lambda_i, p_S)`

Express the preceding equation as the functional equation

.. math:: 
      \bar w_i = \max \bigl[ \beta \sum_{j=1}^n \hat P_{ij}\bar w_j, \bar p_j - p_S \bigr]
      :label: FEoption
      
To solve :eq:`FEoption` form, the operator

.. math::
    T(\bar w;p, p_S) = \max \bigl( \beta \hat P \bar w, \bar p - p_S {\bf 1} \bigr)
    
and iterate to convergence on :math:`T(w;\bar p, p_S)`


Finite-horizon options
^^^^^^^^^^^^^^^^^^^^^^^

Finite horizon options obey  functional equations closely related to :eq:`FEoption0`

Thus, for :math:`k=1, 2, \ldots`, let :math:`w(\bar \lambda_i, p_S;k)` be the value of a :math:`k`-period option

It obeys

.. math::
    w(\bar \lambda_i, p_S;k) = \max \bigl[ \beta \sum_{j=1}^n (P_{ij} \bar \lambda_j^{\gamma}) w (\bar \lambda_j, p_S;k-1), p(\bar \lambda_j) - p_S \bigr]
    
where :math:`w(\bar \lambda_i, p_S;0) \equiv 0`


We can express the preceding equation as the functional equation as

.. math:: 
      \bar w_i^{(k)} = \max \bigl[ \beta \sum_{j=1}^n \hat P_{ij}\bar w_j^{(k-1)}, \bar p_j - p_S \bigr]
      :label: FEoption

The risk-free interest rate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For this economy, a stochastic discount factor is

.. math::
    m_{t+1} = \beta \frac{C_{t+1}^{-\gamma}}{C_t^{-\gamma}} = \beta \lambda_{t+1}^{-\gamma}
    
It follows that the reciprocal :math:`R_t^{-1}` of the gross risk-free interest rate :math:`R_t` is

.. math::
   E_t m_{t+1} = \beta \sum_{j=1}^n P_{ij} \bar \lambda_j^\gamma = \beta P \bar \lambda^\gamma
   
   
Price of Arrow securities
^^^^^^^^^^^^^^^^^^^^^^^^^^

In our economy, the prices of Arrow securities described in equation :eq:`Arrowprice` are given by

.. math::
     Q_{ij} = \beta \bar \lambda_j^{-\gamma} P_{ij}
     
where :math:`Q_{ij}` is the price of one unit of consumption when next period's growth rate is :math:`\lambda_j` given that this period's growth rate is :math:`\lambda_i`
     
    
 
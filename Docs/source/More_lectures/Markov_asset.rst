Asset Pricing in a Markov Environment
=====================================

This lecture describes the famous Lucas asset pricing model*XXXXXX Econometrica 1978*

We study a special case of the model in which the state is governed by a discrete state Markov chain

(Lucas had studied a continuous state Markov process for the state)

The model tells  how the price of a "Lucas tree" is determined in a pure exchange economy 

The economy features

   *  a representative agent 
   
   *  time-separable preferences over a single good 
   
   *  The evolution of the consumption endowment is  described by a discrete state Markov chain
   
Our key tools in studying the economy are

   * Formulas for predicting future values of functions of a Markov state
   
   * A formula for predicting the discounted sum of future values of a Markov state 

Reminders about prediction formulas for  Markov chains
-----------------------------------------------------------

Let :math:`P` be an :math:`n \times n` stochastic matrix with

.. math::
     P_{ij} = {\rm Prob} (x_{t+1} = e_j | x_t = e_i )
     
where :math:`e_i` is the :math:`i` th unit vector.  

Let :math:`\bar y` be an :math:`n \times 1` vector with the interpretation that :math:`y_t = \bar y_i` if :math:`x_t = e_i`

Here are some useful prediction formulas:

.. math::
       E (y_{t+1} | x_t = e_i ) &  = \sum_j P_{ij} \bar y_j = (P \bar y)_i \cr
       E (y_{t+k} | x_t = e_i ) & = \sum_j P_{ij}^{(k)} \bar y_j = (P^k \bar y)_i\cr
           \vdots    & \vdots \cr
       E \bigl[\sum_{j=0}^\infty \beta^j y_{t+j} | x_t = e_i \bigr] & = [(I - \beta P)^{-1} \bar y]_i \cr
       
where :math:`P_{ij}^{(k)}` is the :math:`ij` element of :math:`P^k` and

.. math::
      (I - \beta P)^{-1}  = I + \beta P + \beta^2 P^2 + \cdots
      
      
Markov asset pricing with stochastic geometric consumption growth
------------------------------------------------------------------

Take a Lucas asset pricing model 

We'll price several assets

   * A Lucas tree
   
   * A risk-free consol (a type of bond issued by the UK in the 19th century)
   
   * An infinite horizon call option on a consol
   
A  representative consumer ranks consumption streams according to the utility functional

.. math::
     E_0 \sum_{t=0}^\infty \beta^t U (C_t)
     
where 

    * :math:`C_t` is aggregate consumption per capita
    
    * :math:`\beta \in (0,1)` is a fixed discount factor
    
    * :math:`U(C) = \frac{C^{1-\gamma}}{1-\gamma}` for :math:`\gamma > 0`
    
We assume that aggregate consumption per capital obeys

.. math:: C_{t+1} = \lambda_{t+1} C_t 

where :math:`\lambda_t` is governed by an :math:`n` state discrete Markov chain with transition matrix :math:`P`


Pricing a Lucas tree
^^^^^^^^^^^^^^^^^^^^^

A "Lucas tree" is a claim on the consumption  endowment.  

The "dividend'' is :math:`Y_t = C_t`

Let's price a Lucas tree "ex dividend,'' meaning that the seller retains and the buyer does not receive this period's dividend.
 
Let :math:`p_t` be the price of the Lucas tree, ex dividend

It satisfies

.. math::
    p_t & = E_t \Bigl[ \beta \frac{U'(C_{t+1})}{U'(C_t)} ( C_{t+1} + p_{t+1} ) \Bigr]  \cr
    p_t    & = E_t \Bigl[  \beta \Bigl(\frac{ C_{t+1}}{C_t} \Bigr)^{-\gamma} [ Y_{t+1} + p_{t+1}] \Bigr]
   :label: Lucas1
        
Guess a pricing function  of the form 

.. math::
    p_t = v(\lambda_t) C_t   
    :label: guess1
    
If we substitute this guess into :eq:`Lucas1` and rearrange we obtain

.. math::
     v(\lambda_t) C_t & = E_t \Bigl[ \beta \lambda_{t+1}^{-\gamma} (C_{t+1} + C_{t+1} \lambda_{t+1} )\Bigr] \cr
                      & = E_t \Bigl[ \beta \lambda_{t+1}^{-\gamma} \lambda_{t+1} (1 + v(\lambda_{t+1}) C_t \Bigr] 
                      
It follows that 

.. math:: 
     v(\lambda_t) = E_t \Bigl[ \beta \lambda^{1-\gamma} (1 + \lambda_{t+1}) \Bigr]
     
or

.. math::
     v(i) = \beta \sum_{j=1}^n P_{ij} \lambda_j^{1-\gamma} ( 1 + v(j) )
     
which we can write as

.. math:: 
    v = \beta \tilde P {\bf 1} + \beta \tilde P v
   :label: resolvent1
where :math:`v` is an :math:`n \times n` vector and

.. math::
    \tilde P_{ij} = P_{ij} \lambda_j^{1-\gamma}
    
Finally, we can use a von Neuman series to solve  :eq:`resolvent1`:

.. math::
    v = \beta (I - \beta \tilde P)^{-1} \tilde P {\bf 1}
    :label: resolvent2
    
    
A risk-free consol
^^^^^^^^^^^^^^^^^^^

Consider the same economy

A risk-free consol promises to pay a constant amount  :math:`\zeta> 0` each period

Recycling notation, let :math:`p_t` be the ex-coupon price of the consol

The price obeys the 

.. math::
    U'(C_t) p_t = \beta E_t \Bigl[ U'(C_{t+1}) \zeta + U'(C_{t+1}) p_{t+1} \Bigr]
    
Substituting :math:`U'(C) = C^{-\gamma}` into the above equation yields

.. math::
    C_t^{-\gamma} p_t & = \beta E_t \Bigl[ C_{t+1}^{-\gamma} (\zeta + p_{t+1}) \Bigr] \cr
                      &  = \beta C_t^{-\gamma} E_t \Bigl[ \lambda_{t+1}^{-\gamma} (\zeta + p_{t+1}) \Bigr] \cr
                      
It follows that

.. math:: 
     p_t  = \beta E_t \bigl[ \lambda_{t+1}^{-\gamma} (\zeta + p_{t+1} ) \bigr]
     
or

.. math::
   \bar  p_i = \beta \sum_j (P_{ij}\lambda^j) (\zeta + \bar p_j )
     
which can be expressed as

.. math::
    \bar p = \beta \check P \zeta {\bf 1} + \beta \check P \bar p
  
or

.. math::
   \bar p = \beta (I - \beta \check P)^{-1} \check P \zeta {\bf 1}
   :label: consol_price
   
where

.. math::
    \check  P_{ij} = P_{ij} \lambda_j^{-\gamma} 
    
Pricing a call option on the consol
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We now want to price an infinite horizon call option on the consol

The option has a *strike price* :math:`p_S`

This means that the owner of the option is entitled to purchase the consol at the price :math:`p_S` at the beginning of any period, after the coupon has been paid to the previous owner of the bond
           
The economy  is identical with the one above

Let :math:`w(\lambda_t, p_S)` be the value of the option when the initial growth state is :math:`\lambda_t`

Recall that :math:`p(\lambda_t)` is the value of the consol when the initial growth state is :math:`\lambda_t`

The value of the option satisfies the equation

.. math::
    U'(C_t) w(\lambda_t, p_S) & = \max \Bigl[ \beta E_t U'(C_{t+1}) w(\lambda_{t+1}, p_S), U'(C_t) (p(\lambda_t) - p_S) \Bigr] \cr
    C_t^{-\gamma} w(\lambda_i, p_S) & = \max \Bigl[ \beta P_{ij} \lambda^{-\gamma} C_t^{-\gamma} w(\lambda_j, p_S), C_t^{-\gamma} (p(\lambda_j) - p_S) \Bigr]
    
or

.. math::
    w(\lambda_i, p_S) = \max \bigl[ \beta \sum_{j=1}^n (P_{ij} \lambda_j^{\gamma}) w (\lambda_j, p_S), p(\lambda_j) - p_S \bigr]
    
Let :math:`\hat P_{ij} = P_{ij} \lambda^{-\gamma}_j`

Express the preceding equation as the functional equation

.. math:: 
      w_i = \max \bigl[ \beta \sum_{j=1}^n \hat P_{ij} w_j, p_j - p_S \bigr]
      :label: FEoption
      
To solve :eq:`FEoption` form, the operator

.. math::
    T(w;p, p_S) = \max \bigl( \beta \tilde P w, p - p_S {\bf 1} \bigr)
    
and iterate to convergence on :math:`T(w;p, p_S)`


The risk-free interest rate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For this economy, a stochastic discount factor is

.. math::
    m_{t+1} = \beta \frac{C_{t+1}^{-\gamma}}{C_t^{-\gamma}} = \beta \lambda_{t+1}^{-\gamma}
    
It follows that the reciprocal :math:`R_t^{-1}` of the gross risk-free interest rate :math:`R_t` is

.. math::

   E_t m_{t+1} = \beta \sum_{j=1}^n P_{ij} \lambda_j^\gamma = \beta P \lambda^\gamma
    
 
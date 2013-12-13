.. _ratexp1:

*********************************************
Rational Expectations Equilibrium
*********************************************


.. epigraph::

    "If you're so smart, why aren't you rich?``


Overview
============

This lecture introduces the concept of a *rational expectations equilibrium*


To illustrate the  rational expectations equilibrium concept, we describe a linear-quadratic version of a famous and important model
of Lucas and Prescott [XXXXX add reference] [XXXXX add footnote and reference to Sargent black book; also
cite Ljungqvist and Sargent chapter][#f1]_


Lucas and Prescott (1971) is one of the key papers that kicked off the *rational expectations revolution*

We will learn about how a represenative agent's problem differs from a planner's

We will also learn about the important "Big :math:`K`", "little :math:`k`" trick that is widely used in macroeconomics

Except that for us 

   * Instead of "Big :math:`K`" it will be "Big :math:`Y`"
   
   * and instead of "little :math:`k`" it will be "little :math:`y`"
   
We will learn about how a rational  expectations equilibrium can be characterized as a fixed point of a mapping (we'll call it `:math:{\cal M}` from a *perceived law of motion*
to an *actual law of motion*

Equality between the perceived and actual laws of motion captures in a nut shell what the rational expectations equilibrium concept is all about

A Model of a Competitive Equilibrium in the Presence of Adjustment Costs
==========================================================================



:math:`n` firms produce a homogeneous outputs that is sold in a competitive market.

Each firm faces adjustment costs.

We assume that there is no uncertainty


A firm's  profit function makes it want to forecast future values of  the aggregate of output decisions of other firms just like it

It wants to do this in order to choose its  own output optimally   

We assume that :math:`n` is a large number so that the output of any single firm has a negligible effect on aggregate output

That justifies firms  in treating their forecast of aggregate output as being unaffected by their own output decisions

.. [#f1]The model is a version of one analyzed by Lucas and Prescott (1971) and Sargent (1987a). The recursive competitive equilibrium concept was used by Lucas and Prescott (1971) and described further by Prescott and  Mehra (1980).


A firm's problem
^^^^^^^^^^^^^^^^^

Each of the :math:`n`   competitive firms sells  output :math:`y_t`

The firm chooses a production plan to maximize

.. math::
    \sum_{t=0}^\infty \beta^t R_t 
    :label: comp1 
    
where

.. math::
     R_t = p_t y_t - .5 d (y_{t+1} - y_t )^2, \ t \geq 0 
     :label: comp2 
     
Here 

   * :math:`y_0` is a  given initial condition.

   * :math:`\beta \in (0,1)` is a discount factor
   
   *  :math:`d >0` measures a cost of adjusting the rate of output.
   
The firm is a price taker.

The price :math:`p_t` lies on the inverse demand curve

.. math::
    p_t = A_0 - A_1 Y_t
    :label: comp3d 
    
where 

   * :math:`A_0 >0, A_1 > 0`
   
   * :math:`Y_t = n y_t` is the market-wide level of output
   
.. note:: 

   To state the firm's optimization problem completely requires that we specify laws of motion for all state variables, including ones like :math:`Y` that it cares about but does not control. 

   
   
The firm's beliefs about future prices and market-wide outputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The firm believes that market-wide output :math:`Y_t` follows the law of motion

.. math:: 
    Y_{t+1} = H_0 + H_1 Y_t \equiv H(Y_t) 
    :label: comp3 
    
where :math:`Y_0` is a known initial condition.

The *belief parameters* :math:`H_0, H_1` are   equilibrium objects

For now we proceed on faith and just take them  as given.


The firm observes :math:`Y_t` and :math:`y_t` at time :math:`t` when it chooses :math:`y_{t+1}`. 

The adjustment cost :math:`d(y_{t+1}-y_t)^2` gives the firm the incentive to forecast the market price

But since the market price is a function of market output :math:`Y_t` via the demand equation :eq:`comp3d`, that motivates the firm to forecast future :math:`Y`'s


Substituting equation :eq:`comp3d` into equation :eq:`comp2` gives
 
.. math::
     R_t = (A_0 - A_1 Y_t) y_t - .5 d (y_{t+1} - y_t )^2
     
The firm's incentive to forecast the market price translates into an incentive to forecast the level of market output :math:`Y`

A representative firm's Bellman equation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Let :math:`v(y,Y)` be the optimal value for a firm's problem when the initial state is :math:`(y_0, Y_0)  = (y,Y)`

The value function satisfies the Bellman equation

.. math::
      v(y,Y) = \max_{y'} \left\{ A_0 y - A_1 y Y - .5 d (y' - y)^2   + \beta v(y', Y')\right\}
      :label: comp4
   
where the prime  denotes a next period value and the maximization is subject to the perceived law of motion :math:`Y'=H(Y)`


The first-order necessary condition or *Euler equation* for choosing :math:`y'` is 

.. math::
    - d(y' - y) + \beta v_y(y',Y') =0
    :label: comp5
    
Noting that for this problem the control is :math:`y'` and applying the *Benveniste-Scheinkman formula* [XXXXX John we'll have to add a reference to this] gives

.. math::
    v_y(y,Y) = A_0 - A_1 Y + d(y' - y)
    
Substituting this equation into equation :eq:`comp5` gives

.. math::
    -d(y_{t+1} - y_t) + \beta [A_0 - A_1 Y_{t+1} + d(y_{t+2} - y_{t+1} )] =0
    :label: comp7  

    
Terminal condition
^^^^^^^^^^^^^^^^^^^
    
    * In the process of solving its Bellman equation, the firm sets  an output   path  that satisfies equation :eq:comp7, taking equation:eq:comp3 as given,  subject to the initial conditions for :math:`(y_0, Y_0)` as well as an extra terminal condition. 
    
    * The  terminal condition is :math:`\lim_{t \rightarrow \infty } \beta^t y_t v_y(y_{t}, Y_t) = 0`
    
    * This is called the transversality condition
    
    * It acts as a first-order necessary  condition  "at infinity"
    
    * The firm's decision rule solves the difference equation :eq:`comp7` subject to the given initial condition :math:`y_0` and the transversality condition
    
    * Solving  Bellman equation :eq:`comp4` by backward induction automatically imposes both the Euler equations :eq:`comp7` and the transversality condition
    

The Actual Law of motion for :math:`Y`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The  firm's optimal policy function is

.. math:: 
       y_{t+1} = h(y_t, Y_t)
       :label: comp9 
      
Recalling that :math:`Y_t = ny_t` implies that the *actual law of motion*  for market-wide output is 

.. math::
      Y_{t+1} = n h(Y_t/n, Y_t)
      :label: comp9a 
     
     
Mapping from Perceived to Actual Law of Motion
===============================================

When firms believe that the law of motion for market-wide  output is :eq:`comp3`, their optimizing behavior makes the actual law of motion equation be :eq:`comp9a`


Rational Expectations Equilibrium
==================================

Definition
^^^^^^^^^^^
 A *rational expectations equilibrium* or a  *recursive competitive equilibrium*  of the model with adjustment costs is a value function :math:`v(y, Y)`, an optimal policy function :math:`h(y, Y)`, and   a law of motion :math:`H(Y)` such that

   
    1.  Given :math:`H`, :math:`v(y,Y)` satisfies the firm's Bellman equation and :math:`h(y,Y)` is the firm's optimal policy function
    
    2.  The law of motion for market-wide output :math:`H` satisfies :math:`H(Y)= nh(Y/n,Y)`
    
Fixed point characterization
=============================

A recursive competitive equilibrium equates the actual and perceived laws of motion :eq:`comp3` and :eq:`comp9a`

The firm's optimum problem induces a mapping :math:`{\cal M}` from a perceived law of motion :math:`H` for market-wide output to an actual law of motion :math:`{\cal M}(H)`

The mapping :math:`\cal M` is summarized in equation :eq:`comp9a`

The :math:`H` component of a  rational expectations equilibrium is a fixed point of the operator :math:`{\cal M}`


Misbehavior of the :math:`cal M` operator
=========================================
The mapping :math:`{\cal M}` is not a contraction

There is no guarantee that direct iterations on :math:`{\cal M}` converge

    *  A literature that studies whether models populated  with agents who  learn can converge  to rational expectations equilibria features iterations 
       on a modification of the mapping :math:`\cal M}` that can be approximated as :math:`\gamma {\cal M} + (1-\gamma)I` where :math:`I` is the identity operator
       :math:`\gamma \in (0,1)` is a *relaxation parameter*
       
    *  See Marcet and Sargent (1989) and
       Evans and Honkapohja (2001) for statements and applications of this approach to establish conditions under which collections of adaptive agents who use least squares
       learning converge to a rational expectations equilibrium.  
       
Fortunately, there is  another  method that works in cases that  a rational expectations  equilibrium solves an associated planning problem. We turn to that method next.

    
A planning problem
====================
Our approach to computing an equilibrium is  to match the Euler equations of the market problem with those for a planning problem that can be 
posed as a single-agent dynamic programming problem.

The optimal quantities from  the planning problem are then rational expectations equilibrium quantities

The rational expectations equilibrium price is a  shadow price in the planning problem.

For convenience we set :math:`n=1`

We first compute a sum :math:`S_t` of  consumer and producer surplus at time :math:`t`

.. math::
      S_t = S(Y_t, Y_{t+1}) = \int_0^{Y_t} (A_0 - A_1 x) d \, x -.5 d (Y_{t+1} - Y_t)^2
      :label: comp10
      
The first term is the area under the demand curve

The second term is the social costs of changing output

The *planning problem* is to choose a production plan to maximize

.. math:: 
     \sum_{t=0}^\infty \beta^t S(Y_t, Y_{t+1})
     :label: comp11 
     
subject to an initial condition for :math:`Y_0`

Belman equation for planning problem
=====================================

The Bellman equation for the planning problem is

.. math:: 
      V(Y) = \max_{Y'}\left\{A_0  Y - {A_1 \over 2} Y^2 - .5 d (Y' - Y)^2 + \beta V(Y') \right\}
      :label: comp12 
      
The *Euler equation for the planning problem* is

.. math::
      - d(Y' - Y) + \beta V'(Y') = 0
      :label: comp14 
      
Applying the Benveniste-Scheinkman formula  gives

.. math::
       V'(Y) = A_0 - A_1 Y + d(Y' - Y) 
       :label: comp15 
       
Substituting this into equation :eq:`comp14` and rearranging gives

.. math::
       \beta A_0 + d Y_t - [\beta A_1 + d(1+ \beta)]Y_{t+1} + d \beta Y_{t+2} =0 
       :label: comp16 

       
The Key Insight
================

Return to equation :eq:`comp7` and set :math:`y_t = Y_t` for all :math:`t`. (Please remember that we have set :math:`n=1`. When :math:`n \neq 1`, we have to adjust some pieces of the argument for :math:`n`)

Notice that with :math:`y_t=Y_t`, equations :eq:`comp16` and :eq:`comp7` are identical

Thus, the Euler equation for the planning problem matches the second-order difference equation
that we derived by first finding the Euler equation of the representative firm and substituting into
it the expression :math:`Y_t = n y_t` that "makes the representative firm be representative"

Thus, if  it is appropriate to apply  the same terminal conditions for these two difference equations, which it is,
then we have verified that  a solution of the planning problem also is an equilibrium.

Setting :math:`y_t = Y_t` in equation :eq:`comp7` amounts to dropping equation :eq:`comp3` and instead
solving for the coefficients :math:`H_0, H_1` that make
:math:`y_t = Y_t` true and that jointly solve equations
:eq:`comp3` and :eq:`comp7`




It follows that for this example we can compute an equilibrium
by forming the optimal linear regulator problem corresponding
to the Bellman equation :eq:`comp12`. 

The optimal policy
function for the planning problem is the  law of motion :math:`Y'=H(Y)` that the representative firm faces within a rational
expectations equilibrium.

Lucas and Prescott (1971) used this  method to construct a rational expectations equlibrium

The method exploits a more general connection between equilibrium and Pareto optimality expressed in
the fundamental theorems of welfare economics. See Mas-Colell, Whinston, and Green (1995)
    


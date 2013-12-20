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


The Lucas and Prescott (1971) paper is one of a small number of papers that kicked off the *rational expectations revolution*

We'll follow Lucas and Prescott by employing a setting that is readily "Belmanized" (i.e., capable of being formulated in terms of dynamic programming problems)

Because we use  linear-quadratic-Gaussian setups for demand and costs, we can use  linear-quadratic dynamic programming 

We will learn about how a represenative agent's problem differs from a planner's and how a planning problem can be used to compute rational expectations quantities

We will also learn about the important "Big :math:`K`", "little :math:`k`" trick that is widely used in macroeconomics

Except that for us 

   * Instead of "Big :math:`K`" it will be "Big :math:`Y`"
   
   * and instead of "little :math:`k`" it will be "little :math:`y`"
   
We will learn about how a rational  expectations equilibrium can be characterized as a fixed point of a mapping  that we'll call :math:`{\cal M}` from a *perceived law of motion*
to an *actual law of motion*

Equality between a perceived and an actual law of motion for endogenous market-wide objects captures in a nut shell what the rational expectations equilibrium concept is all about

A Model of a Competitive Equilibrium in the Presence of Adjustment Costs
==========================================================================



:math:`n` firms produce a homogeneous good that is sold in a competitive market.

There is no uncertainty

The price :math:`p_t` of the single  good  lies on the inverse demand curve

.. math::
    p_t = A_0 - A_1 Y_t
    :label: comp3d 
    
where 

   * :math:`A_0 >0, A_1 > 0`
   
   * :math:`Y_t = n y_t` is the market-wide level of output

Each firm faces adjustment costs.

The presence of these adjustment costs in the  firm's  profit function makes it want to forecast future values of  the aggregate of output decisions of other firms just like it

It wants to do this in order to choose its  own output optimally   

We assume that :math:`n` is a large number so that the output of any single firm has a negligible effect on aggregate output

That justifies firms  in treating their forecast of aggregate output as being unaffected by their own output decisions

.. [#f1]The model is a version of one analyzed by Lucas and Prescott (1971) and Sargent (1987a). The recursive competitive equilibrium concept was used by Lucas and Prescott (1971) and described further by Prescott and  Mehra (1980).


.. note::
      We can get closer to Lucas and Prescott's formulation by adding uncertainty to the problem by assuming that the inverse demand function is :math:`p_t = A_0 - A_1 Y_t + u_t`, where :math:`u_{t+1} = \rho u_t + \sigma_u \epsilon_{t+1}`
      where :math:`|\rho| < ` and :math`epsilon_{t+1} \sim {\cal N}(0,1)` is an iid process.    We ask you to study the consequences of this change in problem XXXXX 

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
   
   * :math:`d >0` measures a cost of adjusting the rate of output.
   
The firm is a price taker.
   
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


Misbehavior of the :math:`{\cal M}` operator
=============================================
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

Return to equation :eq:`comp7` and set :math:`y_t = Y_t` for all :math:`t`.

(Please remember that we have set :math:`n=1`. When :math:`n \neq 1`, we have to adjust some pieces of the argument for :math:`n`)

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




Exercises
=============


Exercise 1
^^^^^^^^^^^

A competitive  firm seeks to maximize

.. math:: 
    \sum_{t=0}^\infty \beta^t R_t
    :label: ex1
    
where :math:`\beta \in (0,1)` and time :math:`t` revenue :math:`R_t` is

.. math::
    R_t = p_t y_t - .5 d (y_{t+1} - y_t)^2, \quad d > 0
    :label: ex2
    
where :math:`p_t` is the price of output and :math:`y_t` is the time :math:`t` output of the firm.  

The firm starts with a given initial level of output :math:`y_0`

The market  price lies on the market demand curve

.. math:: 
    p_t = A_0 - A_1 Y_t, \quad A_0, A_1 > 0
    :label: ex3
    
where :math:`Y_t` is the market level of output, which the firm takes as exogenous

The firm believes that :math:`Y_t` follows the law of motion

.. math::
      Y_{t+1} = H_0 + H_1 Y_{t}
      :label: ex4
      
with :math:`Y_0` as an initial condition.

    *  Formulate the Bellman equation for the firm's problem.

    *  Formulate the firm's problem as a discounted optimal linear regulator problem, being careful to describe all of the  objects needed. 
    
    *  What is the {\it state\/} for the firm's problem?

    *  Use the  program XXXXXX{\tt olrp.m}XXXXX to solve the firm's problem for the following parameter values: :math:`A_0= 100, A_1=.05, \beta = .95, d=10, H_0 = 95.5, H_1 = .95`
    
    *  Express the solution of the firm's problem in the form
    
       .. math::
              y_{t+1} = h_0 + h_1 y_t + h_2 Y_t
              :label: ex5
          
    * Give values for the :math: `h_j` s

    * If there were :math:`n` identical competitive firms all behaving according to  equation :eq:`ex5`, what would  equation :eq:`ex5`  imply for the {\it actual}
      law of motion of the form :eq:`ex4` for the market supply :math:`Y`?

      
      
      
Exercise 2
------------

Now assume that  the firm in problem 1 is ``representative''

Implement this idea  by setting :math:`n=1`

In equilibrium, we require that :math:`y_t = Y_t`, but we don't impose this condition at the stage that the firm is optimizing because we want to model  competitive behavior

Define a rational expectations equilibrium to be a pair of numbers :math:`H_0, H_1` such that if the representative firm solves   the problem ascribed to it in exercise 1,
then the firm's optimal behavior given by equation :eq:`	ex5` implies that :math:`y_t = Y_t \ \forall \ t \geq 0`


     *  Use the program that you wrote for exercise 1  to determine which if any  of the following pairs  :math:`(H_0, H_1)` is a rational expectations equilibrium:
                  
            *  (94.0888, .9211)
            
            *  (93.22, .9433)
            
            *  (95.08187459215024, .95245906270392)
            
            * (Answer: set (iii) which implies :math:`(h_0, h_1, h_2) = (95.0819, 1, -.0475)`

      * Describe an iterative algorithm that uses the program that you wrote for exercise 1 to compute a rational expectations equilibrium. 
        (You are not being asked actually to use the algorithm you are suggesting.)


      
Exercise 3
------------

A planner seeks to maximize the welfare criterion

.. math::
    \sum_{t=0}^\infty \beta^t S_t 
    
where :math:`S_t` is "consumer surplus plus producer surplus" defined to be

.. math::
     S_t = S(Y_t, Y_{t+1}) = \int_0^{Y_t} (A_0 - A_1 x) d   - .5 d (Y_{t+1} - Y_t)^2
     
Please 

     *  Formulate the planner's  Bellman equation.

     *  Formulate the planner's problem as an optimal linear regulator, and, for the same parameter values in exercise 1, solve it using the python program XXXXXX  olrp.m. 

     *  Represent the solution in the form :math:`Y_{t+1} = s_0 + s_1 Y_t`

     *  Compare your answer  in  the previous part  with your answer to the first part  of exercise 2
     

Exercise 4
------------

A monopolist faces the industry demand curve :eq:`ex3`  and  chooses :math:` Y_t` to maximize :math:` \sum_{t=0}^\infty \beta^t R_t` where

.. math::
      R_t = p_t Y_t - .5 d(Y_{t+1} - Y_t)^2

where :math:`Y_0` is given

     * Formulate the firm's Bellman equation
     
     * For the parameter values listed in exercise1, formulate and solve the firm's problem using the python program XXXXXXX olrp.m
     
     *  Compare your answer in part b with the answer you obtained to part b of exercise 3




Sherwin Rosen's model of the market for engineers
===================================================

A good example of a rational equilibrium is the equililbrium schooling  model used by Sherwin Rosen.

Rosen used versions of this model to study professional markets for engineers and for lawyers

These are models in which earlier researchers had posited cob web dynamics resting on ad hoc expectations errors to generate cycles in wages and new entrants

Rosen's model gets such cycles without imputing systematic expectations errors to the two workers and firms in his model

 
A household chooses a stream of amount of labor to send to a school that takes four periods to produce an educated worker.

Time is the main  input into the schooling technology.
    

Decentralized version of the model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


A firm and a representative household are price takers in a competitive market

A random shock hits the market, namely, 

.. math::
      \theta_{t+1}  = \rho \theta_t + \sigma_\theta \epsilon_{t+1} 
      :label: sherwin1999
      
where :math:`\theta_t` is a scalar technology shock and :math:`\epsilon_{t+1}` is an i.i.d. random process distributed as :math:`{\cal N}(0,1)`
 
A time-to-build technology describes how new entrants into school get transformed into educated labor through the input of time:

.. math::
      N_{t+1}  = \delta N_t + n_{t-3} 
      :label: sherwin2000

Here :math:`N_t` is the stock of educated labor at time :math:`t`, :math:`n_t` is the number of new entrants into school at time :math:`t`

:math:`\delta \in (0,1)` is one minus a depreciation rate 

Notice how :eq:`sherwin2000` incorporates a  four period time to build  stocks of labor

A representative firm's problem
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The firm faces a competitive wage process :math:`\{w_t\}_{t=0}^\infty$` as a price taker and chooses a contingency plan for :math:`\{N_t\}_{t=0}^\infty`  to maximize

.. math::
       E_0 \sum_{t=0}^\infty \beta^t \biggl\{ f_0 + (f_1 + \theta_t) N_t - {f_2 \over 2} N_t^2 - w_t N_t \biggr\}. 
       
       
The first-order condition for the firm's problem with respect to :math:`N_t` is

.. math::
       w_t = f_1 - f_2 N_t + \theta_t
       :label: sherwin2001
       
In the spirit of Rosen, we  regard equation :eq:`sherwin2001` as an inverse demand function for the stock of labor.





A representative household chooses a contingency plan for :math:`\{n_t, N_{t+4}\}_{t=0}^\infty` to maximize

.. math::
       E_0 \sum_{t=0}^\infty \beta^t \biggl\{ w_t N_t - {d \over 2} n_t^2 \biggr\} 
       :label: sherwin2004 
       
subject to :eq:`sherwin2000` and initial conditions in the form of given values for :math:`N_t` for :math:`t = 0, 1, 2, 3`.

To deduce  first order  conditions for the household' problem, it is helpful first to notice that :eq:`sherwin2000` implies that for :math:`j \geq 4`

.. math::
      N_{t+j} = \delta^{j-3} N_{t+1} + \delta^{j-4} n_t + \delta^{j-3} n_{t+1} + \ldots + \delta n_{t+j-5} + n_{t+j-4}
      :label: sherwin2002 
      
so that

.. math::
       {\partial \sum_{j=0}^\infty \beta^j w_{t+j} N_{t+j} \over \partial n_t } = \beta^4 \sum_{j=0}^\infty (\beta \delta)^j w_{t+j+4} 
       
It follows that the first-order conditions for maximizing :eq:`sherwin2004` subject to  :eq:`sherwin2000` are

.. math:: 
     n_t = d^{-1} E_t \beta^4 \sum_{j=0}^\infty (\beta \delta)^j w_{t+j+4}, \quad t \geq 0
     :label: sherwin2005 
     
We  regard equation :eq:`sherwin2005` as a supply curve for a flow of new entrants into the schooling technology.

It expresses the supply of new entrants into school :math:`n_t` as a linear function of the *expected present value of wages*


.. note::
    Rosen's approach was directly to posit the demand function :eq:`sherwin2001` and the supply function :eq:`sherwin2005` and to define an equilibrium that equates supply with demand
    
Definition
^^^^^^^^^^^

A *rational expectations equilibrium* of the Rosen schooling model  is a stochastic process :math:`\{w_t, N_t, n_t\}` such that 

    *  given the :math:`\{w_t\}` process, :math:`\{N_t, n_t\}` solves the household's problem, and
    
    *  given the :math:`\{w_t\}` process, :math:`\{N_t\}` solves the firms' problem.
    
.. note::
     Evidently, a rational expectations equilibrium can also be characterized as a :math:`\{w_t, N_t, n_t\}` process
     that equates the demand for labor (equation   :eq:`sherwin2001` to the supply   of  labor (equations :eq:`sherwin2002` and :eq:`sherwin2005`).
     
An indirect approach to computing a rational expectations equilibrium is to pose and solve a *planning problem* for :math:{N_t, n_t\}`, then to equate the wage :math:`w_t` to the shadow price of :math:`N_t`


Planning problem
^^^^^^^^^^^^^^^^^^


A planner chooses a contingency plan for new entrants :math:`n_t` to maximize

.. math::
       E_0 \sum_{t=0}^\infty \beta^t \biggl\{ f_0 + (f_1 + \theta_t) N_t - {f_2 \over 2} N_t^2 - {d \over 2} n_t^2 \biggr\} 
       
subject to the laws of motion

.. math::
     \theta_{t+1} & = \rho \theta_t + \sigma_\theta \epsilon_{t+1} \\
     N_{t+1} & = \delta N_t + n_{t-3} 
    
The planner confronts initial conditions :math:`\theta_0, N_0, n_{-1}, n_{-2}, n_{-3}` 

The planner's problem can be formulated as a stochastic discounted optimal linear regulator problem, i.e., a linear-quadratic dynamic programming problem

It  suffices to take

.. math:: 
      X_t = \left[\begin{array}{c}\theta_t \\ N_{t+3} \end{array} \right]
     
as the state vector for the planner's problem.

A solution of the planner's problem is then a law of motion 

.. math:: 
      X_{t+1} = (A-BF)X_t + C \epsilon_{t+1}
      
and a decision rule

.. math:: 
      n_t = -F X_t
      
      
It is also possible to define the state for the planner's problem more profligately as

.. math:: 
      \tilde X_t = \left[\begin{array}{cc}  \theta & N_t & n_{t-1} & n_{t-2} & n_{t-3} \end{array}\right]
      
with associated decision rule 

.. math::
     n_t = -\tilde F \tilde X_t
     
and law of motion

.. math:: 
      \tilde X_{t+1} = (\tilde A - \tilde B \tilde F) \tilde X_t + \tilde C \epsilon_{t+1}
      :label: sherwin2009 
      
We can use this representation  to express  a shadow wage 

.. math:: 
      \tilde w_t = f_1 - f_2 N_t + \theta_t

as 

.. math:: 
      \tilde w_t = S_w \tilde X_t


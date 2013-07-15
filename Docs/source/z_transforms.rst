****************************
Introduction to Z-Transforms
****************************

In this module we will introduce the idea of a z-Transform.  For those of you who are familiar with Laplace transforms, the z-Transform can basically be seen as the discrete time equivalent of the Laplace transform.  The z-Transform will share many of the same properties as the Laplace transform.  For those of you who are not familiar with the Laplace transform then the information provided should be sufficient for your understanding.



The Z-Transform
===============

In the same fashion that it is possible to have both one and two-sided integral transforms the z-transform can also be one or two-sided.  However, for our purposes we will just consider the one-sided z-transform.

z-Transform (one sided)
	The z-transform of a sampled sequence :math:`x(kT)` or :math:`x(k)`, where :math:`k` represents non-negative integers and :math:`T` is hte sampling period, is defined by:
	:math:`X(z) = Z[x^*(t)] = Z[x(kT)] = Z[x(k)] = \sum_{k=0}^\infty x(kT)z^{-k} = \sum_{k=0}^\infty x(k) z^{-k}`, where the complex variable :math:`z` must be selected so that the summation converges.

Lets practice calculating the z-transform before we discuss how it can be used.

First Example
^^^^^^^^^^^^^

Consider the unit step function defined by:

.. math::

    u(k) = \begin{array}{cc} 1 & \text{if } k>0 \\ 0 & \text{else} \end{array}

We calculate the z-transform by using the definition.

.. math::

    X(z) = Z[x(k)] = \sum_{k=0}^\infty 1 z^{-k}

    \sum_{k=0}^\infty 1 z^{-k} = 1 + z^{-1} + z^{-2} + ... = \frac{1}{1 - z^{-1}}

    \frac{1}{1 - z^{-1}} = \frac{z}{z-1}

This z-transform is defined on :math:`|z|>1`.


Second Example
^^^^^^^^^^^^^

Consider the polynomial function defined by:

.. math::

    u(k) = \begin{array}{c} a^k & \text{if } k \geq 0 \\ 0 & \text{if } k < 0 \end{array}

We calculate the z-transform by using the definition.

.. math::

    X(z) = Z[x(k)] = \sum_{k=0}^\infty a^k z^{-k}

    = \sum_{k=0}^\infty (a^{-1} z)^{-k} = \frac{1}{1 - (a^{-1}z)^{-1}}

    \frac{1}{1 - (a^{-1}z)^{-1}} = \frac{z}{z-a}    

This z-transform is defined on :math:`|z|>a`.

On Your Own
^^^^^^^^^^^

Now try to calculate the z-transform of the function:

.. math::

    u(k) = \begin{array}{c} \sin( \omega k T) & \text{if } k \geq 0 \\ 0 & \text{if } k < 0 \end{array}

For what values of :math:`z` is it defined?

.. hint::

    Try writing it in terms of the definition of sin.  :math:`sin(x) = \frac{e^{ix} - e^{-ix}}{2i}`.


Simple Example of a Difference Equation
=======================================

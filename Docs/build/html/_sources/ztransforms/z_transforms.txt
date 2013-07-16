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

    u(k) = \begin{cases} 1 & \text{if } k>0 \\ 0 & \text{else} \end{cases}

We calculate the z-transform by using the definition.

.. math::

    X(z) = Z[x(k)] = \sum_{k=0}^\infty 1 z^{-k}

    \sum_{k=0}^\infty 1 z^{-k} = 1 + z^{-1} + z^{-2} + ... = \frac{1}{1 - z^{-1}}

    \frac{1}{1 - z^{-1}} = \frac{z}{z-1}

This z-transform is defined on :math:`|z|>1`.


Second Example
^^^^^^^^^^^^^^

Consider the polynomial function defined by:

.. math::

    u(k) = \begin{cases} a^k & \text{if } k \geq 0 \\ 0 & \text{if } k < 0 \end{cases}

We calculate the z-transform by using the definition.

.. math::

        X(z) = Z[x(k)] &= \sum_{k=0}^\infty a^k z^{-k} \\
        &= \sum_{k=0}^\infty (a^{-1} z)^{-k}\\
        &= \frac{1}{1 - (a^{-1}z)^{-1}} \\
        &= \frac{1}{1 - (a^{-1}z)^{-1}} \\
        &= \frac{z}{z-a}

This z-transform is defined on :math:`|z|>a`.

On Your Own
^^^^^^^^^^^

Now try to calculate the z-transform of the function:

.. math::

    u(k) = \begin{cases} \sin( \omega k T) & \text{if } k \geq 0 \\ 0 & \text{if } k < 0 \end{cases}

For what values of :math:`z` is it defined?

.. hint::

    Try writing it in terms of the definition of sin.  :math:`sin(x) = \frac{e^{ix} - e^{-ix}}{2i}`.



Simple Example of a Difference Equation
=======================================

As a simple example of a difference equation we will examine the backward rectangle approximation of an integral.  Let :math:`x(k)` be the value of the integral at point :math:`k` and similarly :math:`x(k-1)` is the value at point :math:`k-1` etc...  Let the value of the function at point :math:`k` be given as :math:`y(k)`.  Then the value of the backward rectangle approximation at point :math:`k` can be expressed as:

.. math::

    x_(k) = x(k-1) + T y(k-1)

This problem could be solved through backward substitution and obtaining the equation :math:`x(k) = x(0) + T \sum_{j=0}^{k-1} y(j)`, but this method will not solve all linear difference equations.  We will examine how z-transforms can be used to solve linear difference equations.
.. image:: images/backwardrect.png
    :scale: 15%

.. include:: properties.rst


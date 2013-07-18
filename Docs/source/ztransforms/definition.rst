The Z-Transform
===============

The z-transform is a transformation that moves us from the time domain to the frequency domain.  In the same fashion that it is possible to have both one and two-sided integral transforms, the z-transform can also be one or two-sided.  However, for our purposes we will just consider the one-sided z-transform.

z-Transform (one sided)
    The z-transform of a sampled sequence :math:`x(kT)` or :math:`x(k)`, where :math:`k` represents non-negative integers and :math:`T` is the sampling period, is defined by the following equation. Note that the complex variable :math:`z` must be selected so that the summation converges [#fdef1]_ :

    .. math::
        :label: eq_ZTdef

        X(z) = \mathcal{Z}[x^*(t)] = \mathcal{Z}[x(kT)] = \mathcal{Z}[x(k)] = \sum_{k=0}^\infty x(kT)z^{-k} = \sum_{k=0}^\infty x(k) z^{-k}

Lets practice calculating the z-transform before we discuss how it can be used.

First Example
^^^^^^^^^^^^^

Consider the unit step function defined by:

.. math::

    u(k) = \begin{cases} 1 & \text{if } k>0 \\ 0 & \text{else} \end{cases}

We calculate the z-transform by using the definition.

.. math::

    X(z) = \mathcal{Z}[x(k)] &= \sum_{k=0}^\infty 1 z^{-k} \\
    &= 1 + z^{-1} + z^{-2} + \dots \\
    &= \frac{1}{1 - z^{-1}} \\
    &= \frac{z}{z-1}

This z-transform is defined on :math:`|z|>1`.

Second Example
^^^^^^^^^^^^^^

Consider the polynomial function defined by:

.. math::

    u(k) = \begin{cases} a^k & \text{if } k \geq 0 \\ 0 & \text{if } k < 0 \end{cases}

We calculate the z-transform by using the definition.

.. math::

        X(z) = \mathcal{Z}[x(k)] &= \sum_{k=0}^\infty a^k z^{-k} \\
        &= \sum_{k=0}^\infty (a^{-1} z)^{-k}\\
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

    Try writing it in terms of the definition of sin.  :math:`\sin(x) = \frac{e^{ix} - e^{-ix}}{2i}`.

..  [#fdef1] Note that some people use \sum_{k=0}^\infty x(k) z^{k}`.  We will use the definition given, but if you were working with the other definition all of this material can be easily translated by converting all of the :math:`z`'s to :math:`\frac{1}{z}`.

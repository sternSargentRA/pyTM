The Z-Transform
===============

A *one-sided sequence* is a sequence :math:`\{x(k)\}, k= 0, 1, \ldots`

The subscript :math:`k` often denotes time 

The one-sided z-transform maps a *one-sided sequence* into a function of complex variable :math:`z`  

z-Transform (one sided)

    The z-transform of a sampled sequence  :math:`x(k)`, where :math:`k` represents non-negative integers is defined by the following equation. 

    .. math::
        :label: eq_ZTdef

        X(z) \equiv \mathcal{Z}[x(k)] \equiv \sum_{k=0}^\infty x(k) z^{-k}
        
The complex variable :math:`z` must take a value that makes  the sum converge [#fdef1]_ :

Before we discuss some of its uses, let's practice calculating some z-transforms 

First Example
^^^^^^^^^^^^^

Consider the unit step function 

.. math::

    u(k) = \begin{cases} 1 & \text{if } k>0 \\ 0 & \text{else} \end{cases}

Using the definition.

.. math::

    X(z) = \mathcal{Z}[u(k)] &= \sum_{k=0}^\infty 1 z^{-k} \\
    &= 1 + z^{-1} + z^{-2} + \dots \\
    &= \frac{1}{1 - z^{-1}} \\
    &= \frac{z}{z-1}

This z-transform is well defined on the domain :math:`|z|>1`.

Second Example
^^^^^^^^^^^^^^

Consider the sequence

.. math::

    x(k) = \begin{cases} a^k & \text{if } k \geq 0 \\ 0 & \text{if } k < 0 \end{cases}

Use the definition again

.. math::

        X(z) = \mathcal{Z}[x(k)] &= \sum_{k=0}^\infty a^k z^{-k} \\
        &= \sum_{k=0}^\infty (a^{-1} z)^{-k}\\
        &= \frac{1}{1 - (a^{-1}z)^{-1}} \\
        &= \frac{z}{z-a}

This z-transform is well defined on the domain :math:`|z|>a`.

On Your Own
^^^^^^^^^^^

Now try to calculate the z-transform of the sequence:

.. math::

    x(k) = \begin{cases} \sin( \omega k T) & \text{if } k \geq 0 \\ 0 & \text{if } k < 0 \end{cases}

For what domain of :math:`z` values is it defined?

.. hint::

    Try writing it in terms of the definition of sin.  :math:`\sin(x) = \frac{e^{ix} - e^{-ix}}{2i}`.

..  [#fdef1] Some people define the transform as :math:`\sum_{k=0}^\infty x(k) z^{k}`.  We will use our definition, but if you want to use the other one, all of this material can be easily translated by converting all of the :math:`z`'s to :math:`\frac{1}{z}`s.

Properties of the Z-Transform
=============================

The Z-transform has many useful properties. We will list some of theme (without proof) here. [#f1]_

.. csv-table::
    :header: "Property", "Definition"
    :widths: 30, 70
    :delim: ;
    :stub-columns: 1
    :name: Z-Transform Properties

    Linearity; :math:`a_1 x_1[n] + z_2 x_2[n] \rightarrow a_1 X_1(z) + a_2 X_2(z)`
    Time Expansion; :math:`x_{(k)}[n] = \begin{cases} x[r],  n=rk \\ 0,  n \ne rk\end{cases} \rightarrow X(z^k)`
    Time Shifting [#f2]_; :math:`x[n-k] \rightarrow z^{-k}X(z)`
    Scaling in z-domain; :math:`a^n x[n] \rightarrow X(a^{-1}z)`
    Time Reversal; :math:`x[-n] \rightarrow X(z^{-1})`
    Complex Conjugation; :math:`x^*[n] \rightarrow X^*(z^*)`
    Differentiation; :math:`n x[n] \rightarrow -z2 \frac{\partial X(z)}{\partial z}`
    Convolution; :math:`x_1[n] \ast x_2[n] \rightarrow X_1(z) X_2(z)`
    Cross-Correlation; :math:`r_{x_1, x_2} = x_1^*[-n] \ast x_2[n] \rightarrow R_{x_1, x_2}(z) = X_1^*(\frac{1}{z^*}) X_2(z)`
    Multiplication; :math:`x_1[n]x_2[n] \rightarrow \frac{1}{i 2 \pi} \oint X_1(v) X_2(\frac{z}{v})v^{-1} dv`

Linearity
^^^^^^^^^

.. math::

    a_1 x_1[n] + z_2 x_2[n] &\rightarrow a_1 X_1(z) + a_2 X_2(z)

Time Expansion
^^^^^^^^^^^^^^

.. math::

    x_{(k)}[n] = \begin{cases} x[r], & n=rk \\ 0, & n \ne rk\end{cases} &\rightarrow X(z^k)

Time Shifting [#f2]_
^^^^^^^^^^^^^^^^^^^^

.. math::

    x[n-k] &\rightarrow z^{-k}X(z)

Scaling in z-domain
^^^^^^^^^^^^^^^^^^^

.. math::

    a^n x[n] &\rightarrow X(a^{-1}z)

Time Reversal
^^^^^^^^^^^^^

.. math::

    x[-n] &\rightarrow X(z^{-1})

Complex Conjugation
^^^^^^^^^^^^^^^^^^^

.. math::

    x^*[n] &\rightarrow X^*(z^*)

Differentiation
^^^^^^^^^^^^^^^

.. math::

    n x[n] &\rightarrow -z2 \frac{\partial X(z)}{\partial z}

Convolution
^^^^^^^^^^^

.. math::

    x_1[n] \ast x_2[n] &\rightarrow X_1(z) X_2(z)

Cross-Correlation
^^^^^^^^^^^^^^^^^

.. math::

    r_{x_1, x_2} = x_1^*[-n] \ast x_2[n] &\rightarrow R_{x_1, x_2}(z) = X_1^*(\frac{1}{z^*}) X_2(z)

Multiplication
^^^^^^^^^^^^^^

.. math::

    x_1[n]x_2[n] &\rightarrow \frac{1}{i 2 \pi} \oint X_1(v) X_2(\frac{z}{v})v^{-1} dv

Theorems Associated with the Z-Transform
========================================

Parseval's Theorem
^^^^^^^^^^^^^^^^^^

.. math::

    \sum_{b=-\infty}^{\infty} x_1[n]x_2^*[n] = \frac{1}{i 2 \pi} \oint X_1(v) X_2^*(\frac{1}{v})v^{-1} dv

Initial Value Theorem
^^^^^^^^^^^^^^^^^^^^^

.. math::

    x[0] = \lim_{z \rightarrow \infty} X(z)

Final Value Theorem
^^^^^^^^^^^^^^^^^^^

.. math::

    x[\infty] = \lim_{z \rightarrow 1} (z-1) X(z)


.. [#f1] Many of these properties were found on this `Wikipedia Page <http://en.wikipedia.org/wiki/Z-transform>`_. There you can find proofs for most of them.

.. [#f2] This property is very important in many economic contexts, as will be seen later in this module.

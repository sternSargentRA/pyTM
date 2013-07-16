Properties of the Z-Transform
=============================

 (without proof) here. [#f1]_

.. csv-table::
    :header: "Property", "n - domain( :math:`x[n]` )", "Z - domain ( :math:`X(z)` )"
    :widths: 20, 30, 30
    :delim: ;
    :stub-columns: 1
    :name: Z-Transform Properties

    Linearity; :math:`a_1 x_1[n] + z_2 x_2[n]`; :math:`a_1 X_1(z) + a_2 X_2(z)`
    Time Expansion; :math:`x_{(k)}[n] = \begin{cases} x[r],  n=rk \\ 0,  n \ne rk\end{cases}`; :math:`X(z^k)`
    Time Shifting [#f2]_; :math:`x[n-k]`; :math:`z^{-k}X(z)`
    Scaling in z-domain; :math:`a^n x[n]`; :math:`X(a^{-1}z)`
    Time Reversal; :math:`x[-n]`; :math:`X(z^{-1})`
    Complex Conjugation; :math:`x^*[n]`; :math:`X^*(z^*)`
    Differentiation; :math:`n x[n]`; :math:`-z \frac{\partial X(z)}{\partial z}`
    Convolution; :math:`x_1[n] \ast x_2[n]`; :math:`X_1(z) X_2(z)`
    Cross-Correlation; :math:`r_{x_1, x_2} = x_1^*[-n] \ast x_2[n]`; :math:`R_{x_1, x_2}(z) = X_1^*(\frac{1}{z^*}) X_2(z)`
    Multiplication; :math:`x_1[n]x_2[n]`; :math:`\frac{1}{i 2 \pi} \oint X_1(v) X_2(\frac{z}{v})v^{-1} dv`

Theorems Associated with the Z-Transform
========================================

.. csv-table::
    :header: "Theorem", "Mathematical Representation"
    :widths: 30, 70
    :delim: ;
    :stub-columns: 1
    :name: Z-Transform Theorems

    Parseval's Theorem; :math:`\sum_{b=-\infty}^{\infty} x_1[n]x_2^*[n] = \frac{1}{i 2 \pi} \oint X_1(v) X_2^*(\frac{1}{v})v^{-1} dv`
    Initial Value Theorem; :math:`x[0] = \lim_{z \rightarrow \infty} X(z)`
    Final Value Theorem; :math:`x[\infty] = \lim_{z \rightarrow 1} (z-1) X(z)`


.. [#f1] Many of these properties were found on this `Wikipedia Page <http://en.wikipedia.org/wiki/Z-transform>`_. There you can find proofs for most of them.

.. [#f2] This property is very important in many economic contexts, as will be seen later in this module.
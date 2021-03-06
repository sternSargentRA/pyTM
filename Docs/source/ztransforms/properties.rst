Properties of the Z-Transform
=============================

Here are some useful properties of the Z-transform 

.. csv-table::
    :header: "Property", "n - domain( :math:`x[n]` )", "z - domain ( :math:`X(z)` )"
    :widths: 20, 30, 30
    :delim: ;
    :stub-columns: 1
    :name: Z-Transform Properties

    Linearity; :math:`a_1 x_1[n] + z_2 x_2[n]`; :math:`a_1 X_1(z) + a_2 X_2(z)`
    Time Expansion; :math:`x_{(k)}[n] = \begin{cases} x[r],  n=rk \\ 0,  n \ne rk\end{cases}`; :math:`X(z^k)`
    Time Shifting (backwards) [#fprop2]_ ; :math:`x[n-k]`; :math:`z^{-k}X(z)`
    Time Shifting (forwards); :math:`x[n+k]`; :math:`z^{k}X(z) - z^{k}x(0) - z^{k-1}x(1) - ... - z x(d-1)`
    Scaling in z-domain; :math:`a^n x[n]`; :math:`X(a^{-1}z)`
    Time Reversal; :math:`x[-n]`; :math:`X(z^{-1})`
    Complex Conjugation; :math:`x^*[n]`; :math:`X^*(z^*)`
    Differentiation; :math:`n x[n]`; :math:`-z \frac{d X(z)}{d z}`
    Convolution; :math:`x_1[n] \ast x_2[n]`; :math:`X_1(z) X_2(z)`
    Cross-Correlation; :math:`r_{x_1, x_2} = x_1^*[-n] \ast x_2[n]`; :math:`R_{x_1, x_2}(z) = X_1^*(\frac{1}{z^*}) X_2(z)`
    Multiplication; :math:`x_1[n]x_2[n]`; :math:`\frac{1}{i 2 \pi} \oint X_1(v) X_2(\frac{z}{v})v^{-1} dv`

Some Useful Theorems Associated with the Z-Transform
=====================================================

.. csv-table::
    :header: "Theorem", "Mathematical Representation"
    :widths: 30, 70
    :delim: ;
    :stub-columns: 1
    :name: Z-Transform Theorems

    Parseval's Theorem; :math:`\sum_{b=-\infty}^{\infty} x_1[n]x_2^*[n] = \frac{1}{i 2 \pi} \oint X_1(v) X_2^*(\frac{1}{v})v^{-1} dv`
    Initial Value Thm; :math:`x[0] = \lim_{z \rightarrow \infty} X(z)`
    Final Value Thm; :math:`x[\infty] = \lim_{z \rightarrow 1} (z-1) X(z)`

.. [#fprop1] Many of these properties are  on this `Wikipedia Page <http://en.wikipedia.org/wiki/Z-transform>`_, where  you can find proofs for most of them.

.. [#fprop2] This property is very important in many economic contexts, as we shall see soon.

The Inverse Z-Transform
=======================

Given a function :math:`X(z)`, we might want to find a sequence :math:`x(k)` of which it is the z-transform.  This is where the inverse z-transform comes in

**Inverse z-transform**
    The inverse z-transform is defined as:
.. math::
    x(k) = \mathcal{Z}^{-1}[X(z)] = \frac{1}{2 \pi i} \oint_C X(z) z^{k-1} \partial z 
    
The contour integral can be evaluated using the  Cauchy Residue Theorem, a result from complex analysis. 
    
The contour of integration  should enclose all singularities of :math:`X(z)`.

Fortunately, there are easier ways to calculate the inverse z-transform.  

One useful technique is to the (complex) function into a sum of functions in the table, then apply the corresponding inverse z-transforms to each component

Steps:

1.  Break up the function through a partial fraction expansion of :math:`G[z] = \frac{F[z]}{z}`. This helps us get needed constant terms.
2.  Multiply by :math:`z` to get back to :math:`F[z]`.
3.  Put each piece into a recognizable form.
4.  Transform each piece.

Here is an example of how this works

Example
^^^^^^^^^^^^^
Find the inverse z-transform of the function :math:`X[z] = \frac{8z - 19}{(z-2)(z-3)z}`. 

Apply the steps:

1. Use partial fraction expansion to get :math:`G[z] = \frac{X[z]}{z} = \frac{c_1}{(z-2)} + \frac{c_2}{(z-3)} + \frac{c_3}{z}`.
2. Calculate the constants :math:`c_1, c_2, c_3` and get :math:`G[z] = \frac{(-19/6)}{z} + \frac{(3/2)}{(z-2)} + \frac{(5/3)}{(z-3)}`.
3. Multiply by :math:`z` to get :math:`X[z] = \frac{-19}{6} + \frac{(3/2)z}{(z-2)} + \frac{(5/3)z}{(z-3)}`.
4. Read each piece off of the table to get the inverse z-transform of each piece to get :math:`x[k]`

.. math::

    \frac{-19}{6} \rightarrow \frac{-19}{6} \delta[k]

    \frac{(3/2)z}{(z-2)} \rightarrow \frac{3}{2} (2)^k u[k]

    \frac{(5/3)z}{(z-3)} \rightarrow \frac{5}{3} (3)^k u[k]

This gives  :math:`x[k] = \frac{-19}{6} \delta[k] + \left(\frac{3}{2} (2)^k + \frac{5}{3} (3)^k \right) u[k]`

Present Value Calculations
==========================

One natural application of Z-transforms to economics is in computing the present value (PV) of an infinite income stream. Let this stream be represented by a sequence of real numbers :math:`\{x_n\}_{n=0}^{\infty}` and let :math:`\beta \in (0, 1)` be a constant discount factor. The present value of this sequence is defined as

.. math::
    :label: eq_PVdef

    PV(\beta) = \sum_{n=0}^{\infty} \beta^n x_n

Notice how Equation :eq:`eq_PVdef` looks very much like the definition of the z-transform :eq:`eq_ZTdef` of :math:`x_n` in terms of :math:`\beta`, instead of :math:`z`. The only difference is that the exponent on :math:`\beta` here is :math:`+n` instead of the :math:`-n` from before. This two representations actually yield equivalent results, but do require substituting :math:`\beta` for :math:`\beta^{-1}` after applying the definition of the transform. This is best understood by example.

First PV Example
^^^^^^^^^^^^^^^^

Let the sequence of payoffs be :math:`x_n = A \psi^n`, where :math:`(A, \psi) \in \mathbb{R}`. We can use the z-transform to compute the present value of this sequence directly. We can look up the z-transform we are interested in from the table of transforms. Note that in doing this we take the z-transform in terms of the variable :math:`\beta` to conform to our definition of the present value :eq:`eq_PVdef`.

.. math::

    X(\beta) = \mathcal{Z}(\psi^n) = \frac{1}{1 - \psi \beta^{-1}}

The z-transforms contained in the table use the :math:`z^{-n}` representation, whereas we would like :math:`\beta^n`. To overcome this we simply substitute :math:`\beta` with :math:`\beta^{-1}` in our z-transform to obtain

.. math::

    X(\beta) =  \frac{1}{1 - \psi \beta}

We can now use the linearity property of the z-transform to include the :math:`A` from the definition of the sequence. The property states that

.. math::

    a_1 x_1[n] + z_2 x_2[n] =  a_1 X_1(z) + a_2 X_2(z)

In our situation we don't have a linear combination of sequences, but we do have a scalar multiple of the sequence. We see that the scalar just passes directly through the transform. Applying this to our sequence we obtain the final expression for the present value.

.. math::

    PV(\beta) = \frac{A}{1 - \psi \beta}


Second PV Example
^^^^^^^^^^^^^^^^^

Let the sequence of payoffs be :math:`x_n = n \lambda^n`. We want to use the z-transform to compute the present value of this sequence.

We can see from the table of properties that :math:`\mathcal{Z}(n x_n) = -z \frac{\partial X(z)}{\partial z}`. We can apply this property, as well as the z-transform of :math:`\lambda^n` to evaluate the present value (note that we compute this in terms of :math:`\beta` instead of :math:`z`).

.. math::

    X(\beta) = \mathcal{Z}(\lambda^n) = \frac{1}{1 - \lambda \beta^{-1}}

Now, because we used :math:`\beta^{-n}` when we looked up the z-transform from the table, we need to replace :math:`\beta \rightarrow \beta^{-1}`. Doing so yields the following expression:

.. math::

    X(\beta) = \frac{1}{1 - \lambda \beta}

We now apply the property from above and finish the calculation of the present value. Note that because we have made the substitution :math:`\beta \rightarrow \beta^{-1}`, the negative sign on the property disappears and the expression becomes :math:`\mathcal{Z}(n x_n) = z \frac{\partial X(z)}{\partial z}`

.. math::

    PV(\beta) &= \beta \left[ \frac{\partial X(\beta)}{\partial \beta} \right]\\
    &= \beta \left[ \frac{\partial}{\partial \beta } \left(\frac{1}{1 - \lambda \beta} \right) \right] \\
    &= \beta \left[ \frac{\lambda }{(1-\beta  \lambda )^2} \right] \\
    &= \frac{\lambda \beta }{(1-\beta  \lambda )^2}

Reminders for PV Calculations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When using the z-transform to compute do present value calculations it is important to keep a few things in mind:

- Make sure that you adjust :math:`X(z)` to be in terms of :math:`z^n` immediately after taking the transform. As shown in the two examples above, this is done by substituting :math:`z \rightarrow z^{-1}`. Note that if you compute the infinite sum directly, just use :math:`z^n` to begin with and don't worry about making substitutions.
- Carefully examine the transform, properties, and theorems tables to avoid computing the infinite sum in the transform definition directly. Often this will require a little bit of algebra on the initial sequence to get it in the form of an one or more entries in the table.

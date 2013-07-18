Present Value Calculations
==========================

One natural application of Z-transforms to economics is in computing the present value of an infinite income stream. Let this stream be represnted by a sequence of real numbers :math:`\{x_n\}_{n=0}^{\infty}` and let :math:`\beta \in (0, 1)` be a constant discount factor. The present value of this sequence is defined as

.. math::
    :label: eq_PVdef

    PV(\beta) = \sum_{n=0}^{\infty} \beta^n x_n

Notice how Equation :eq:`eq_PVdef` looks very much like the definition of the z-transform :eq:`eq_ZTdef` of :math:`x_n` in terms of :math:`\beta`, instead of :math:`z`.

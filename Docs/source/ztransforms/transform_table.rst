Transform Table
===============

For the table [#ftab]_ below we make use of the following definitions:

.. math::

    u[n] = \begin{cases} 1, & n \ge 0 \\ 0, & n < 0 \end{cases}

    \delta[n] = \begin{cases} 1, & n = 0 \\ 0, & n \ne 0 \end{cases}

.. csv-table::
    :header-rows: 1
    :delim: ;
    :name: Transform Table

    Signal, :math:`x[n]`; Z-transform, :math:`X(z)`; Condition (radius of convergence)
    :math:`\delta[n]`; 1; all "z"
    :math:`\delta[n-n_0]`; :math:`z^{-n_0}`; :math:`z \neq 0`
    :math:`u[n]`; :math:`\frac{1}{1-z^{-1} }`; :math:`|z| > 1`
    :math:`e^{-\alpha n} u[n]`; :math:`1 \over 1-e^{-\alpha  }z^{-1}`; :math:`|z| >  |e^{-\alpha}| \,`
    :math:`-u[-n-1]`;  :math:`\frac{1}{1 - z^{-1}}`;:math:`|z| < 1`
    :math:`n u[n]`; :math:`\frac{z^{-1}}{( 1-z^{-1} )^2}`; :math:`|z| > 1`
    :math:`- n u[-n-1] \,`; :math:`\frac{z^{-1} }{ (1 - z^{-1})^2 }`;:math:`|z| < 1`
    :math:`n^2 u[n]`; :math:`\frac{ z^{-1} (1 + z^{-1} )}{(1 - z^{-1})^3}`; :math:`|z| > 1\,`
    :math:`- n^2 u[-n - 1] \,`; :math:`\frac{ z^{-1} (1 + z^{-1} )}{(1 - z^{-1})^3}`; :math:`|z| < 1\,`
    :math:`n^3 u[n]`; :math:`\frac{z^{-1} (1 + 4 z^{-1} + z^{-2} )}{(1-z^{-1})^4}`; :math:`|z| > 1\,`
    :math:`- n^3 u[-n -1]`; :math:`\frac{z^{-1} (1 + 4 z^{-1} + z^{-2} )}{(1-z^{-1})^4}`; :math:`|z| < 1\,`
    :math:`a^n u[n]`;  :math:`\frac{1}{1-a z^{-1}}`;:math:`|z| > |a|`
    :math:`-a^n u[-n-1]`;  :math:`\frac{1}{1-a z^{-1}}`;:math:`|z| < |a|`
    :math:`n a^n u[n]`;  :math:`\frac{az^{-1} }{ (1-a z^{-1})^2 }`; :math:`|z| > |a|`
    :math:`-n a^n u[-n-1]`; :math:`\frac{az^{-1} }{ (1-a z^{-1})^2 }`;:math:`|z| < |a|`
    :math:`n^2 a^n u[n]`; :math:`\frac{a z^{-1} (1 + a z^{-1}) }{(1-a z^{-1})^3}`; :math:`|z| > |a|`
    :math:`- n^2 a^n u[-n -1]`; :math:`\frac{a z^{-1} (1 + a z^{-1}) }{(1-a z^{-1})^3}`; :math:`|z| < |a|`
    :math:`\cos(\omega_0 n) u[n]`; :math:`\frac{ 1-z^{-1} \cos(\omega_0)}{ 1-2z^{-1}\cos(\omega_0)+ z^{-2}}`;:math:`|z| >1`
    :math:`\sin(\omega_0 n) u[n]`; :math:`\frac{ z^{-1} \sin(\omega_0)}{ 1-2z^{-1}\cos(\omega_0)+ z^{-2} }`;:math:`|z| >1`
    :math:`a^n \cos(\omega_0 n) u[n]`; :math:`\frac{1-a z^{-1} \cos( \omega_0)}{1-2az^{-1}\cos(\omega_0)+ a^2 z^{-2}}`; :math:`|z|>|a|`
    :math:`a^n \sin(\omega_0 n) u[n]`; :math:`\frac{ az^{-1} \sin(\omega_0) }{ 1-2az^{-1}\cos(\omega_0)+ a^2 z^{-2} }`; :math:`|z|>|a|`

.. [#ftab] This table a modified form of a similar table found on the `Wikipedia Page <http://en.wikipedia.org/wiki/Z-transform>`_.

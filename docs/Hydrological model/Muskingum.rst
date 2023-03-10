*****
Muskingum
*****
Muskingum is a hydrologic-routing method which employs the equation of continuity to predict magnitude, volume and temporal patterns of flow as it translates downstream of a channel.

.. math::
    πΌβπ = \frac{ππ}{ππ‘}


.. image:: /img/muskingum1.png
    :width: 400pt

.. image:: /img/muskingum2.png
    :width: 400pt


Channel routing functions of inflow, outflow and storage where storage can be considered as two parts, prism & wedge storage.

.. math::
    π  = πΎβ[π₯βπΌ^{\m} +(1βπ₯)βπ^{\π}]


Where `k` is the travel time constant and `x` are weighting coefficient to determine the linearity of the water surface, and it ranges between 0 & 0.5, and `m` is an exponential constant varies from 0.6 for rectangle channel to 1.


For Muskingum version of the channel routing equation `m` equals one which made the relation between `S` and `I`, `Q`. Using coefficient `k` & `x` three weights can be calculated as follow:

.. math::

    C1 = \left(\frac{π₯π‘β2πΎπ}{2πΎ(1βπ)+π₯π‘}\right)\label{eq:C1}
    C2 = \left(\frac{π₯π‘+2πΎπ}{2πΎ(1βπ)+π₯π‘}\right)\label{eq:C2}
    C3 = \left(\frac{2πΎ(1-π)-π₯π‘}{2πΎ(1βπ)+π₯π‘}\right)\label{eq:C3}

To route the inflow hydrograph

.. math::
    Q = \left(C1 * I_{j+1} + C2 * I_{j} + C3 * Q_{j} }\right)\label{eq:Q}

Getting started
===============

Installation
------------

Install Aspendos from its repository root:

.. code-block:: console

   python -m pip install -e .

The package defines ``ASPENDOS_PATH`` for repository-local data and products.
The enclosed-mass routines are re-exported from Chalcedon; new lensing work
should use Chalcedon's maintained API directly.

Truncated-halo mass
-------------------

The compatibility function accepts a positive cutoff-to-scale-radius ratio and
returns the enclosed mass ratio:

.. code-block:: python

   import numpy as np
   from aspendos import retr_mcutfrommscl

   radius_ratio = np.logspace(-2, 2, 200)
   mass_ratio = retr_mcutfrommscl(radius_ratio)
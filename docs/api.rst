API reference
=============

Aspendos re-exports ``retr_mcutfrommscl(fracacutasca)`` and
``retr_mcut(defs, asca, acut, adislens, mdencrit)`` from Chalcedon for older
imports. The first returns the dimensionless enclosed-mass fraction for a
positive cutoff-to-scale-radius ratio. The second returns truncated halo mass
from profile and lensing-distance inputs. New code should import these
functions from Chalcedon.

The maintained `Chalcedon documentation <https://chalcedon.readthedocs.io/>`_
describes the canonical lensing API and its physical assumptions.
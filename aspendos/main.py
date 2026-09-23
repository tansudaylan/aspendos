import numpy as np


def retr_mcut(gdat, defs, asca, acut, adishost, mdencrit):
    """Return the truncated-lens mass from its physical scale factors."""

    mscl = defs * np.pi * adishost**2 * mdencrit * asca
    fracacutasca = acut / asca
    mcut = mscl * retr_mcutfrommscl(fracacutasca)
    
    return mcut


def retr_mcutfrommscl(fracacutasca):
    """Return the dimensionless truncation mass for a positive radius ratio."""

    radius_ratio = np.asarray(fracacutasca, dtype=float)
    if np.any(radius_ratio <= 0):
        raise ValueError("The cutoff-to-scale-radius ratio must be positive.")

    mcut = radius_ratio**2 / (radius_ratio**2 + 1.)**2 * (
        (radius_ratio**2 - 1.) * np.log(radius_ratio)
        + radius_ratio * np.pi
        - (radius_ratio**2 + 1.)
    )

    return mcut




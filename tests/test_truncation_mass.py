import numpy as np
import pytest

from aspendos import retr_mcutfrommscl


def test_truncation_mass_normalization_at_unit_ratio():
    """The analytic kernel has its exact expected value at equal radii."""

    assert retr_mcutfrommscl(1.0) == pytest.approx(np.pi / 4.0 - 0.5)


def test_truncation_mass_increases_with_radius_ratio():
    """Increasing the truncation radius increases enclosed dimensionless mass."""

    radius_ratio = np.logspace(-2.0, 2.0, 200)
    mass_ratio = retr_mcutfrommscl(radius_ratio)

    assert np.all(np.diff(mass_ratio) > 0)


@pytest.mark.parametrize("radius_ratio", [0.0, -1.0])
def test_truncation_mass_rejects_nonpositive_ratio(radius_ratio):
    """The logarithmic kernel is undefined for nonpositive radius ratios."""

    with pytest.raises(ValueError, match="positive"):
        retr_mcutfrommscl(radius_ratio)
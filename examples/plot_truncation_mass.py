#!/usr/bin/env python3
"""Plot the analytic truncated-lens mass kernel."""

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from aspendos import retr_mcutfrommscl


def main() -> None:
    """Generate the dimensionless truncation-mass figure."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--typefileplot", choices=("png", "pdf"), default="png")
    arguments = parser.parse_args()

    radius_ratio = np.logspace(-2.0, 2.0, 500)
    mass_ratio = retr_mcutfrommscl(radius_ratio)
    output_path = Path(__file__).with_name(f"truncation_mass.{arguments.typefileplot}")

    figure, axis = plt.subplots(figsize=(6.5, 4.0), facecolor="white")
    axis.plot(radius_ratio, mass_ratio, color="#007A6F", linewidth=2.0)
    axis.scatter([1.0], [retr_mcutfrommscl(1.0)], color="#A51417", s=35, zorder=3)
    axis.annotate(
        r"$a_{cut}=a_s$",
        xy=(1.0, retr_mcutfrommscl(1.0)),
        xytext=(1.6, 0.18),
        arrowprops={"arrowstyle": "->", "color": "black"},
    )
    axis.set_xscale("log")
    axis.set_yscale("log")
    axis.set_xlabel(r"Cutoff-to-scale-radius ratio $a_{cut}/a_s$")
    axis.set_ylabel(r"Truncation-mass ratio $M_{cut}/M_s$")
    axis.grid(False)
    figure.tight_layout()

    print(f"Writing to {output_path}...")
    figure.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(figure)


if __name__ == "__main__":
    main()
"""
A collection of functions for discretizing continuous data.
"""

import numpy as np
from numpy.typing import NDArray
from typing import Any

from uniplot.conversions import floatify


def discretize(x: Any, x_min: float, x_max: float, steps: int) -> int:
    """
    Returns a discretized integer.
    """
    pass


def discretize_array(x: NDArray, x_min: float, x_max: float, steps: int) -> NDArray:
    """
    Returns a NumPy array of discretized integer values. NaN values will return
    -1.

    Note that the integer values are not bound to the rande defined by `steps`.
    """
    pass


def compute_y_at_middle_of_row(
    height_index_from_top: int, y_min: float, y_max: float, height: int
) -> float:
    """
    Returns the y level at the middle of the specified bin.

    Typical use case is to display the right axis tick.
    """
    pass


def invert_discretize(i: int, minimum: float, maximum: float, nr_bins: int) -> float:
    """
    Returns the level at the middle of the specified bin.

    This is the inverse of `discretizer.discretize`.
    """
    pass


def invert_discretize_array(
    i: NDArray, minimum: float, maximum: float, nr_bins: int
) -> NDArray:
    """
    Returns the level at the middle of the specified bin.

    This is the inverse of `discretizer.discretize`.
    """
    pass

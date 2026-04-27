import numpy as np
from numpy.typing import NDArray
from typing import List

from uniplot.discretizer import discretize, discretize_array

LEFT_MARGIN_FOR_HORIZONTAL_AXIS = 1


class LabelSet:
    """
    This class represents a list of possible axis labels. It can render them to
    a string, or list of strings. It also provides metrics about the rendering
    result.
    """

    def __init__(
        self,
        labels: NDArray,
        x_min: float = 0.0,
        x_max: float = 1.0,
        available_space: int = 17,
        unit: str = "",
        log: bool = False,
        vertical_direction: bool = False,
    ):
        self.labels: NDArray = labels
        self.x_min = x_min
        self.x_max = x_max
        self.unit = unit
        self.log = log
        self.available_space = available_space
        self.vertical_direction = vertical_direction
        self._results_already_in_cache: bool = False
        self._rendered_result: List[str] = []
        self._render_does_overlap: bool = False
        self._spacing_is_regular: bool = True

    ###########
    # private #
    ###########

    def _post_process_init(self) -> None:
        """Post-process initialization hook for subclasses."""
        pass

    def _find_shortest_string_representation(self) -> List[str]:
        """
        This method will find the shortest numerical values for axis labels
        that are different from each other.
        """
        pass

    def _float_format(self, n: float, nr_digits: int) -> str:
        """
        Format a number to a specified precision.

        Ref.: https://docs.python.org/3.8/library/string.html#format-specification-mini-language
        """
        pass

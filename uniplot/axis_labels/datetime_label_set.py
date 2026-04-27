import re
import numpy as np
from numpy.typing import NDArray
from typing import List

from uniplot.axis_labels.label_set import LabelSet


class DatetimeLabelSet(LabelSet):
    """
    A label set for datetime values like timestamps.
    """

    def __init__(
        self,
        labels: NDArray,
        x_min: float,
        x_max: float,
        available_space: int = 17,
        unit: str = "",
        log: bool = False,
        vertical_direction: bool = False,
    ):
        super().__init__(
            labels, x_min, x_max, available_space, unit, log, vertical_direction
        )
        # For convenience, make sure we have the bounds also available as
        # datetime objects.
        self.x_min_as_dt = np.float64(self.x_min).astype("datetime64[s]")
        self.x_max_as_dt = np.float64(self.x_max).astype("datetime64[s]")

    ###########
    # private #
    ###########

    def _find_shortest_string_representation(self) -> List[str]:
        """
        This method will find the shortest strings for datetime labels that
        give enough information.
        """
        pass


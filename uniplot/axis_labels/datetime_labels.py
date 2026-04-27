import numpy as np
from numpy.typing import NDArray
from typing import Tuple, List, Dict, Optional, Final
from collections import defaultdict
from functools import lru_cache

from uniplot.axis_labels.datetime_label_set import DatetimeLabelSet
from uniplot.axis_labels.extended_talbot_labels import (
    _compute_preferred_number_of_labels,
    _compute_coverage_score,
    _compute_density_score,
)

DIGIT_TIME_UNITS: Final = ["Y", "M", "D", "h", "m", "s"]

# Preference-ordered list of "nice" numbers
Q_VALUES: Final[Dict[str, List]] = defaultdict(
    lambda: [1, 5, 2, 4, 3],
    {
        "M": [1, 4, 3, 2],
        "h": [1, 12, 6, 3, 2],
        "m": [1, 15, 10, 5, 2],
    },
)
# Weights to be able to combine the different scores
WEIGHTS: Final = np.array([0.4, 0.25, 0.3, 0.2])
# The "depth" of the search
MAX_SKIP_AMOUNT: Final = 12


@lru_cache(maxsize=512)
def datetime_labels(
    x_min: float,
    x_max: float,
    available_space: int,
    vertical_direction: bool = False,
    unit: str = "",
    log: bool = False,
    verbose: bool = False,
) -> Optional[DatetimeLabelSet]:
    """
    A simple way to get started with datetime labelling.
    """
    pass


###########
# private #
###########








def _compute_simplicity_score(q_values, i: int, j: int) -> float:
    """
    Simplicity score according, modified from Talbot.
    """
    pass



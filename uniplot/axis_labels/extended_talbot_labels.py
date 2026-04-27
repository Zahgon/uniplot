import numpy as np
from numpy.typing import NDArray
from typing import Optional, Final
from functools import lru_cache

from uniplot.axis_labels.label_set import LabelSet

# Preference-ordered list of "nice" numbers
Q_VALUES: Final = [1, 5, 2, 2.5, 4, 3]
# Weights to be able to combine the different scores
WEIGHTS: Final = np.array([0.4, 0.25, 0.3, 0.5])
# The "depth" of the search
MAX_SKIP_AMOUNT: Final = 9


@lru_cache(maxsize=512)
def extended_talbot_labels(
    x_min: float,
    x_max: float,
    available_space: int,
    vertical_direction: bool = False,
    unit: str = "",
    log: bool = False,
    verbose: bool = False,
) -> Optional[LabelSet]:
    """
    The following is based on the paper Talbot, J., Lin, S. & Hanrahan, P. An
    Extension of Wilkinsonâ€™s Algorithm for Positioning Tick Labels on Axes.
    IEEE T Vis Comput Gr 16, 1036â€“1043 (2010). We have further exteded the
    algorithm to account for the discrete nature of terminal output.
    """
    pass


###########
# private #
###########


def _compute_preferred_number_of_labels(
    available_space: int, vertical_direction: bool
) -> int:
    """
    Compute an estimate for the preferred number of labels.
    """
    pass


def _compute_simplicity_score(labels: NDArray, i: int, j: int) -> float:
    """
    Simplicity score according to Talbot.
    """
    pass


def _compute_coverage_score(labels: NDArray, x_min: float, x_max: float) -> float:
    """
    Coverage score according to Talbot.
    """
    pass


def _compute_density_score(labels: NDArray, preferred_nr: int) -> float:
    """
    Density score according to Talbot.
    """
    pass

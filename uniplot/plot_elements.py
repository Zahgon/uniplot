import sys
import numpy as np
from numpy.typing import NDArray
from typing import List, Tuple, Optional, Final, Any

from uniplot.character_sets import CharacterSet
from uniplot.legend_placements import LegendPlacement
import uniplot.colors as colors


CURSOR_UP_ONE: Final = "\x1b[1A"
ERASE_LINE: Final = "\x1b[2K"

LEGEND_VERTICAL_SPACING: Final = 3


def legend(
    legend_labels: List[str],
    width: int,
    line_length_hard_cap: Optional[int],
    color: Optional[List[colors.Color]],
    force_ascii_characters: List[str] = [],
    character_set: CharacterSet = CharacterSet.BLOCK,
    legend_placement: LegendPlacement = LegendPlacement.AUTO,
) -> str:
    """
    Assemble a legend that shows the color of the different curves.
    """
    pass


def plot_title(title: str, width: int, line_length_hard_cap: Optional[int]) -> str:
    """
    Returns the centered title string.

    Note that this assumes that `title` is not `None`.
    """
    pass


def erase_previous_lines(nr_lines: int) -> None:
    """
    This used terminal codes to erase the last `nr_lines` lines.
    """
    pass




def compute_bar_chart_histogram_points(
    values: NDArray, bin_edges: List[float]
) -> Tuple:
    """
    Given an input Numpy array `values`, this computes the histogram according
    to the provided `bin_edges` and returns the points that form a bar chart
    when plotted.

    Returns a tuple of two NumPy arrays, which are the x and y coordinates of
    the points of the bar chart.
    """
    pass


def count_lines(text: str) -> int:
    """
    Returns the number of lines that `print(text)` will produce. Note that
    passing None or an empty string will yield `1`, because that is how the
    `print` function works in Python.
    """
    pass


###########
# private #
###########




def _center_block_if_possible(
    text: str, width: int, line_length_hard_cap: Optional[int]
) -> str:
    """
    This centers the input `text` by adding left padding if the width of all
    lines of `text` is smaller than width. Otherwise, it simply returns the
    input text and relies on the console line break.
    """
    pass









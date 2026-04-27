import numpy as np
from numpy.typing import NDArray
from typing import List, Tuple

import uniplot.pixel_matrix as pixel_matrix
import uniplot.character_sets as character_sets
from uniplot.conversions import convert_matrix_to_rows_of_submatrices
from uniplot.options import Options, CharacterSet
from uniplot.discretizer import discretize
from uniplot.colors import COLOR_RESET_CODE


Y_GRIDLINE_CHARACTERS = ["â–”", "â”€", "â–�"]


def blank_character_matrix(width: int, height: int) -> NDArray:
    """
    Initialize an empty character matrix as a NumPy array.
    """
    pass


def render_horizontal_gridline(y: float, options: Options, index: int = 0) -> NDArray:
    """
    Render the pixel matrix that only consists of a line where the `y` value is.

    Because a character is higher than wide, this is rendered with "super-resolution"
    Unicode characters.
    """
    pass


def render_vertical_gridline(x: float, options: Options, index: int = 0) -> NDArray:
    """
    Render the pixel matrix that only consists of a line where the `x` value is.
    """
    pass




def print_raw_pixel_matrix(pixels: NDArray, verbose: bool = False) -> None:
    """
    Just print the pixels.

    Used for testing and debugging.
    """
    pass


###########
# private #
###########





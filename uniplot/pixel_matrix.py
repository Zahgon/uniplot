import numpy as np
from numpy.typing import NDArray
from typing import Optional, Final


BATCH_SIZE: Final = 10_000




def merge_on_top(
    low_layer: NDArray, high_layer: NDArray, width: int, height: int
) -> NDArray:
    """
    Put a pixel matrix on top of another, with an optional single solid line of
    "shadow", including diagonal fields.

    If activated, this shadow will ensure that later 2x2 squares exclusively
    belong to one particular line.

    TODO I stopped using this but still there is the unused shadow stuff,
    I would delete it as well as the tests
    """
    pass


###########
# private #
###########





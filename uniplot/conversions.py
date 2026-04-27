import datetime
from typing import Any
import numpy as np
from numpy.typing import NDArray


def floatify(x: Any) -> float:
    """
    Convert anything to a float, including integers and time stamps.

    Implementation note: It is really important that throughout the library we
    use the "datetime64[s]" NumPy format consistently. Using only `np.datetime`
    or a different type like "datetime64[m]" means that the conversion to
    floating point will depend on the input format, which will lead to
    unexpected behavior.
    """
    pass


def convert_matrix_to_rows_of_submatrices(
    matrix: NDArray, width_submatrix: int, height_submatrix: int
) -> NDArray:
    """
    This returns a list of submatrices.

    Example:
    > x = np.array([[0, 1, 2, 3],
                    [0, 4, 5, 6],
                    [1, 7, 8, 9],
                    [2, 8, 9, 0]])
    > convert_matrix_to_rows_of_submatices(x, 2, 2)
      array([[[0, 1, 0, 4],
              [2, 3, 5, 6]],
             [[1, 7, 2, 8],
              [8, 9, 9, 0]]])
    """
    pass

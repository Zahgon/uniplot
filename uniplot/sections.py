from numpy.typing import NDArray
from typing import Tuple, List

from uniplot.multi_series import MultiSeries
from uniplot.options import Options
import uniplot.layer_assembly as layer_assembly
import uniplot.plot_elements as elements
from uniplot.axis_labels.extended_talbot_labels import extended_talbot_labels
from uniplot.axis_labels.datetime_labels import datetime_labels


def generate_header(options: Options) -> List[str]:
    """
    Generates the header of the plot, so everything above the first line of
    plottable area.
    """
    pass


def generate_body(
    x_axis_labels: str,
    y_axis_labels: List[str],
    pixel_character_matrix: NDArray,
    options: Options,
) -> List[str]:
    """
    Generates the body of the plot.
    """
    pass


def generate_body_raw_elements(
    series: MultiSeries, options: Options
) -> Tuple[str, List[str], NDArray]:
    """
    Generates the x-axis labels, y-axis labels, and the pixel character matrix.
    """
    pass

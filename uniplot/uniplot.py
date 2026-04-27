from typing import List, Dict, Optional, Final, Any
from readchar import readkey, key

from uniplot.multi_series import MultiSeries
from uniplot.options import Options
from uniplot.param_initializer import validate_and_transform_options
import uniplot.sections as sections
import uniplot.plot_elements as elements


def plot(ys: Any, xs: Optional[Any] = None, **kwargs) -> None:
    """
    2D plot on the terminal.

    Parameters:

    - `ys` are the y coordinates of the points to plot. This parameter is
      mandatory and can either be a list or a list of lists, or the equivalent
      NumPy array.
    - `xs` are the x coordinates of the points to plot. This parameter is
      optional and can either be a `None` or of the same shape as `ys`.
    - Any additional keyword arguments are passed to the
      `uniplot.options.Options` class.
    """
    pass


class plot_gen:
    def __init__(self, return_string=False, **kwargs) -> None:
        self.default_arguments: Final[Dict] = kwargs
        self.last_nr_of_lines: int = 0
        self.return_string: Final[bool] = return_string
        self.series: MultiSeries = MultiSeries([])
        self.options: Options = Options()
        if "ys" in kwargs:
            self.series = MultiSeries(xs=kwargs.get("xs"), ys=kwargs.get("ys", []))
            if "xs" in kwargs:
                del kwargs["xs"]
            del kwargs["ys"]
            self.options = validate_and_transform_options(
                series=self.series, kwargs=kwargs
            )




def plot_to_string(ys: Any, xs: Optional[Any] = None, **kwargs) -> str:
    """
    Same as `plot`, but the return type is string. Ignores the `interactive`
    option.

    Can be used to integrate uniplot in other applications, or if the output is
    desired to be not stdout.
    """
    pass


#####################################
# Experimental features, see Readme #
#####################################


def histogram(
    xs: Any,
    bins: int = 20,
    bins_min: Optional[float] = None,
    bins_max: Optional[float] = None,
    **kwargs,
) -> None:
    """
    Plot a histogram to the terminal.

    Parameters:

    - `xs` are the values of the points to plot. This parameter is mandatory
      and can either be a list or a list of lists, or the equivalent NumPy
      array.
    - Any additional keyword arguments are passed to the
      `uniplot.options.Options` class.
    """
    pass


def histogram_to_string(
    xs: Any,
    bins: int = 20,
    bins_min: Optional[float] = None,
    bins_max: Optional[float] = None,
    **kwargs,
) -> str:
    """
    Same as `histogram`, but the return type is string. Ignores the `interactive`
    option.

    Can be used to integrate uniplot in other applications, or if the output is
    desired to be not stdout.
    """
    pass

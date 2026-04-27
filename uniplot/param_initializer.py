import numpy as np
from typing import Dict

from uniplot.multi_series import MultiSeries
from uniplot.options import Options, CharacterSet
from uniplot.conversions import floatify
from uniplot.colors import Color
from uniplot.color_themes import COLOR_THEMES
from uniplot.legend_placements import LegendPlacement

AUTO_WINDOW_ENLARGE_FACTOR = 0.001


def validate_and_transform_options(series: MultiSeries, kwargs: Dict = {}) -> Options:
    """
    This will check the keyword arguments passed to the `uniplot.plot`
    function, will transform them and will return them in form of an `Options`
    object.

    The idea is to cast arguments into the right format to be used by the rest
    of the library, and to be as tolerant as possible for ease of use of the
    library.

    As a result the somewhat hacky code below should at least be confined to
    this function, and not spread throughout uniplot.
    """
    pass


###########
# private #
###########



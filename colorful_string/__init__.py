"""Colorful text"""
from . import colors, utils
from .colors import *
from .utils import *

__all__ = colors.__all__ + utils.__all__ # type: ignore

__version__ = "0.1.1"

# Now you can do the usual stuff.

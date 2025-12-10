"""
Phoenix Nest MARS Communications Suite

Open-source HF digital communications tools for Military Auxiliary Radio System (MARS) operations.

Author: Alex Pennington (KY4OLB, formerly AAR4TE / NNN0VO)
License: MIT
"""

__version__ = "0.1.0"
__author__ = "Alex Pennington"
__email__ = "projects@organicengineer.com"

from mars_suite.core import SignalProcessor
from mars_suite.modem import Modem

__all__ = ["SignalProcessor", "Modem", "__version__"]

"""
A dataclass for holding the state of the application.

it needs fields for:

- tsot: TSOT
- tdon: TDON
- tcp: TCP
"""

from dataclasses import dataclass

from external_brain.tsot import TSOT as _TSOT
from external_brain.tcp import TCP as _TCP
from external_brain.tdon import TDON as _TDON


@dataclass
class ApplicationState:
    """
    A dataclass for holding the state of the application.

    it needs fields for:

    - tsot: TSOT
    - tcp: TCP
    - tdon: TDON
    """

    tsot: _TSOT
    tcp: _TCP
    tdon: _TDON

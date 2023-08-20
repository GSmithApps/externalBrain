"""

"""

from external_brain.tcp import tcp as _tcp
from external_brain.tdon import tdon as _tdon
from external_brain.tsot import tsot as _tsot

class ApplicationState:
    """
    Holds the state of the application.
    """

    tsot = _tsot
    tdon = _tdon
    tcp = _tcp

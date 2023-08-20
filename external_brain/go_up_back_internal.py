"""
"""

from external_brain.go_up_internal import go_up_internal as _go_up_internal
from external_brain.go_back_internal import go_back_internal as _go_back_internal

def go_up_back_internal(up_tags, back_tags, application_state):
    """

    Raises
    ------

    - TagsNotInTSOTException
    - KeyIsNotConvertibleToASetException
    """

    _go_up_internal(up_tags, application_state)
    _go_back_internal(back_tags, application_state)

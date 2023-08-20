"""

"""
from external_brain.return_tf_as_a_frozen_set import (
    return_tf_as_a_frozen_set as _return_tf_as_a_frozen_set,
)
from external_brain.tags_not_in_subset import (
    tags_not_in_tsot as _tags_not_in_tsot,
)

def go_back_internal(tags, application_state):
    """

    Raises
    ------

    - TagsNotInTSOTException
    - KeyIsNotConvertibleToASetException
    """
    tags = _return_tf_as_a_frozen_set(tags)

    _tags_not_in_tsot(tags, application_state)
    
    tags_not_in_tcp = tags.difference(application_state.tcp)

    if tags_not_in_tcp:
        print(f"{tags_not_in_tcp} is not in the current position.")
        return
    
    application_state.tcp = application_state.tcp.difference(tags)
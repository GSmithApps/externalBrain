"""

"""
from external_brain.return_tf_as_a_frozen_set import (
    return_tf_as_a_frozen_set as _return_tf_as_a_frozen_set,
)
from external_brain.tags_not_in_subset import (
    tags_not_in_tsot as _tags_not_in_tsot,
)


def go_up_internal(tags, application_state):
    """

    Raises
    ------

    - TagsNotInTSOTException
    - KeyIsNotConvertibleToASetException
    """

    tags = _return_tf_as_a_frozen_set(tags)

    _tags_not_in_tsot(tags, application_state)

    intersection = tags.intersection(application_state.tcp)

    if intersection:
        print(f"{intersection} is already in the set of tags.")
        return
    
    application_state.tcp = tags.union(application_state.tcp)

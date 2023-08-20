"""

"""

from external_brain.return_tf_as_a_frozen_set import (
    return_tf_as_a_frozen_set as _return_tf_as_a_frozen_set,
)
from external_brain.tags_not_in_subset import (
    tags_not_in_tsot as _tags_not_in_tsot,
)


def go_to_internal(tags, application_state):
    """
    Go to a set of tags.

    Each tag in the set must
    be in _tsot. If not, simply tell
    the user, but do nothing else.

    Raises
    ------

    - TagsNotInTSOTException
    - KeyIsNotConvertibleToASetException
    """

    tags = _return_tf_as_a_frozen_set(tags)

    _tags_not_in_tsot(tags, application_state)

    application_state.tcp = tags

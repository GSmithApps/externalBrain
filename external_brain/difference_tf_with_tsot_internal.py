"""

"""

from external_brain.return_tf_as_a_set import return_tf_as_a_set as _return_tf_as_a_set
def difference_tf_with_tsot_internal(tags, application_state):
    """
    Raises
    ------

    KeyIsNotConvertibleToASetException
    """
    application_state.tsot.difference_update(_return_tf_as_a_set(tags))
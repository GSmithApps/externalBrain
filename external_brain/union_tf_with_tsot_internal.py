from external_brain.return_tf_as_a_set import return_tf_as_a_set as _return_tf_as_a_set

def union_tf_with_tsot_internal(tags, application_state):
    """
    Take the union of _tsot with tags and set it back to _tsot.

    Raises
    ------

    KeyIsNotConvertibleToASetException
    """
    application_state.tsot.update(_return_tf_as_a_set(tags))

from external_brain.key_is_not_convertible_to_a_set_exception import KeyIsNotConvertibleToASetException as _KeyIsNotConvertibleToASetException

def return_tf_as_a_set(key: str | set | frozenset | dict) -> set:
    """
    Converts a key to a set.

    Has nothing to do with whether the key is relative or full.

    Raises
    ------

    KeyIsNotConvertibleToASetException
    """

    if isinstance(key, str):
        return set([key])

    elif isinstance(key, set):
        return key

    elif isinstance(key, frozenset):
        return set(key)

    elif key == {}:
        return set()

    else:
        raise _KeyIsNotConvertibleToASetException(
            f"{key} is not convertible to a set.  It"
            "needs to be a str, set, frozenset, or empty dict."
        )
    
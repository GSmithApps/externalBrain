"""

set_

"""

from external_brain.key_is_not_convertible_to_a_set_exception import (
    KeyIsNotConvertibleToASetException as _KeyIsNotConvertibleToASetException,
)


def return_tf_as_a_frozen_set(key: str | set | frozenset | dict) -> frozenset:
    """
    Converts a key to a frozen set.

    Has nothing to do with whether the key is relative or full.

    Raises
    ------

    - KeyIsNotConvertibleToASetException
    """

    if isinstance(key, str):
        return frozenset([key])

    elif isinstance(key, set):
        return frozenset(key)

    elif isinstance(key, frozenset):
        return key

    elif key == {}:
        return frozenset()

    else:
        raise _KeyIsNotConvertibleToASetException(
            f"{key} is not convertible to a set.  It"
            "needs to be a str, set, frozenset, or empty dict."
        )

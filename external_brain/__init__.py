"""
We want to be able to do the following:

# Set a node

# Add or remove sets of tags from the current set of tags

# Move

"""

from external_brain.application_state import ApplicationState as _ApplicationState
from external_brain.difference_tf_with_tsot_internal import (
    difference_tf_with_tsot_internal as _difference_tf_with_tsot_internal,
)
from external_brain.union_tf_with_tsot_internal import (
    union_tf_with_tsot_internal as _union_tf_with_tsot_internal,
)
from external_brain.set_value_internal import (
    set_value_internal as _set_value_internal,
)
from external_brain.go_to_internal import go_to_internal as _go_to_internal
from external_brain.go_up_internal import go_up_internal as _go_up_internal
from external_brain.go_back_internal import go_back_internal as _go_back_internal
from external_brain.go_up_back_internal import (
    go_up_back_internal as _go_up_back_internal,
)
from external_brain.print_output import print_output as _print_output
from external_brain.tags_not_in_tsot_exception import (
    TagsNotInTSOTException as _TagsNotInTSOTException,
)
from external_brain.add_empty_text import add_empty_text as _add_empty_text
from external_brain.key_is_not_convertible_to_a_set_exception import (
    KeyIsNotConvertibleToASetException as _KeyIsNotConvertibleToASetException,
)

def difference_tf_with_tsot(tags):
    """
    Take the difference of _tsot with tags and set it back to _tsot.
    """
    try:
        _difference_tf_with_tsot_internal(tags, _ApplicationState)
    except _KeyIsNotConvertibleToASetException as e:
        print(e)
    _print_output(_ApplicationState)
    return this_module


def union_tf_with_tsot(tags):
    """
    Take the union of _tsot with tags and set it back to _tsot.
    """
    try:
        _union_tf_with_tsot_internal(tags, _ApplicationState)
    except _KeyIsNotConvertibleToASetException as e:
        print(e)
    _print_output(_ApplicationState)


def set_value(value):
    """
    Set the node to value.
    """
    _set_value_internal(value, _ApplicationState)
    _print_output(_ApplicationState)


def go_to(tags):
    """
    Go to a set of tags.

    Each tag in the set must
    be in _tsot. If not, simply tell
    the user, but do nothing else.
    """

    try:
        _go_to_internal(tags, _ApplicationState)
        _add_empty_text(_ApplicationState)
    except _TagsNotInTSOTException as e:
        print(e)
    except _KeyIsNotConvertibleToASetException as e:
        print(e)
    _print_output(_ApplicationState)


def go_up(tags):
    """
    Add plus_tags to _tsot.
    """
    try:
        _go_up_internal(tags, _ApplicationState)
        _add_empty_text(_ApplicationState)
    except _TagsNotInTSOTException as e:
        print(e)
    except _KeyIsNotConvertibleToASetException as e:
        print(e)
        
    _print_output(_ApplicationState)


def go_back(tags):
    """
    Remove minus_tags from _tsot.

    """
    try:
        _go_back_internal(tags, _ApplicationState)
        _add_empty_text(_ApplicationState)
    except _TagsNotInTSOTException as e:
        print(e)
    except _KeyIsNotConvertibleToASetException as e:
        print(e)
    _print_output(_ApplicationState)


def go_up_back(up_tags, back_tags):
    """
    Add plus_tags to _tsot and remove minus_tags from _tsot.
    """
    try:
        _go_up_back_internal(up_tags, back_tags, _ApplicationState)
        _add_empty_text(_ApplicationState)
    except _TagsNotInTSOTException as e:
        print(e)
    except _KeyIsNotConvertibleToASetException as e:
        print(e)
    _print_output(_ApplicationState)


import sys
this_module = sys.modules[__name__]

# pickle the application state


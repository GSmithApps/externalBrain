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
from external_brain.tsot import TSOT as _TSOT
from external_brain.tcp import TCP as _TCP
from external_brain.tdon import TDON as _TDON

class ExternalBrain:

    def __init__(self):

        _tsot = _TSOT()
        _tcp = _TCP()
        _tdon = _TDON()
        _tdon[_tcp] = ""
        self._application_state = _ApplicationState(_tsot, _tcp, _tdon)

    def difference_tf_with_tsot(self, tags):
        """
        Take the difference of _tsot with tags and set it back to _tsot.
        """
        try:
            _difference_tf_with_tsot_internal(tags, self._application_state)
        except _KeyIsNotConvertibleToASetException as e:
            print(e)
        _print_output(self._application_state)


    def union_tf_with_tsot(self, tags):
        """
        Take the union of _tsot with tags and set it back to _tsot.
        """
        try:
            _union_tf_with_tsot_internal(tags, self._application_state)
        except _KeyIsNotConvertibleToASetException as e:
            print(e)
        _print_output(self._application_state)


    def set_value(self, value):
        """
        Set the node to value.
        """
        _set_value_internal(value, self._application_state)
        _print_output(self._application_state)


    def go_to(self, tags):
        """
        Go to a set of tags.

        Each tag in the set must
        be in _tsot. If not, simply tell
        the user, but do nothing else.
        """

        try:
            _go_to_internal(tags, self._application_state)
            _add_empty_text(self._application_state)
        except _TagsNotInTSOTException as e:
            print(e)
        except _KeyIsNotConvertibleToASetException as e:
            print(e)
        _print_output(self._application_state)


    def go_up(self, tags):
        """
        Add plus_tags to _tsot.
        """
        try:
            _go_up_internal(tags, self._application_state)
            _add_empty_text(self._application_state)
        except _TagsNotInTSOTException as e:
            print(e)
        except _KeyIsNotConvertibleToASetException as e:
            print(e)
            
        _print_output(self._application_state)


    def go_back(self, tags):
        """
        Remove minus_tags from _tsot.

        """
        try:
            _go_back_internal(tags, self._application_state)
            _add_empty_text(self._application_state)
        except _TagsNotInTSOTException as e:
            print(e)
        except _KeyIsNotConvertibleToASetException as e:
            print(e)
        _print_output(self._application_state)


    def go_up_back(self, up_tags, back_tags):
        """
        Add plus_tags to _tsot and remove minus_tags from _tsot.
        """
        try:
            _go_up_back_internal(up_tags, back_tags, self._application_state)
            _add_empty_text(self._application_state)
        except _TagsNotInTSOTException as e:
            print(e)
        except _KeyIsNotConvertibleToASetException as e:
            print(e)
        _print_output(self._application_state)



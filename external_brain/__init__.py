"""
Contains the class ``ExternalBrain``.
"""

import pickle
from pprint import pprint
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
from external_brain.append_value_internal import (
    append_value_internal as _append_value_internal,
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
    """
    
    
    Methods
    -------

    - Setting Values

      - ``set_value``
      - ``append_value``

    - Modifying the set of tags

      - ``remove_tags``
      - ``add_tags``

    - Movement

      - ``go_to``
      - ``go_up``
      - ``go_back``
      - ``go_up_back``

    - Inspection

      - ``tags``
      - ``keys``
      - ``nodes``
      - ``nodes_with_one``
      - ``nodes_with_all``

    Usage
    -----

    >>> eb = ExternalBrain()
    >>> eb.set_value("apple")
    """


    def __init__(self, delete_data_and_start_blank="no"):
        """
        Initialize the external brain.

        If ``delete_data_and_start_blank == "delete_data_and_start_blank"``, then delete the
        data and reset the external brain to a blank state. Otherwise,
        load the data from the file ``data.pkl``.

        """

        if delete_data_and_start_blank == "delete_data_and_start_blank":
            
            _tsot = _TSOT()
            _tcp = _TCP()
            _tdon = _TDON()
            _tdon[_tcp] = ""
            self._application_state = _ApplicationState(_tsot, _tcp, _tdon)

        else:

            with open("data.pkl", "rb") as f:

                self._application_state = pickle.load(f)

    # @@@@@@@@@@@@@@@@@@@@@
    # @@@ setting value @@@
    # @@@@@@@@@@@@@@@@@@@@@

    def set_value(self, value):
        """
        Set the node to value.
        """
        _set_value_internal(value, self._application_state)
        _print_output(self._application_state)
        return self
    
    def append_value(self, value):
        """
        Append value to the node.
        """
        _append_value_internal(value, self._application_state)
        _print_output(self._application_state)
        return self

    # @@@@@@@@@@@@@@@@@@@
    # @@@ modify tsot @@@
    # @@@@@@@@@@@@@@@@@@@

    def remove_tags(self, tags):
        """
        Take the difference of _tsot with tags and set it back to _tsot.
        """
        try:
            _difference_tf_with_tsot_internal(tags, self._application_state)
        except _KeyIsNotConvertibleToASetException as e:
            print(e)
        _print_output(self._application_state)
        return self


    def add_tags(self, tags):
        """
        Take the union of _tsot with tags and set it back to _tsot.
        """
        try:
            _union_tf_with_tsot_internal(tags, self._application_state)
        except _KeyIsNotConvertibleToASetException as e:
            print(e)
        _print_output(self._application_state)
        return self

    # @@@@@@@@@@@@@@@@@@@
    # @@@ movement @@@
    # @@@@@@@@@@@@@@@@@@@

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
        return self


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
        return self


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
        return self


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
        return self

    # @@@@@@@@@@@@@@@@@@@
    # @@@ inspection @@@
    # @@@@@@@@@@@@@@@@@@@

    def tags(self):
        """
        Return tsot.
        """
        pprint(self._application_state.tsot)
        _print_output(self._application_state)

    def keys(self):
        """
        Return the keys of tsot.
        """
        pprint(self._application_state.tdon.keys())
        _print_output(self._application_state)

    def nodes(self):
        """
        Return tdon.
        """
        pprint(self._application_state.tdon)
        _print_output(self._application_state)

    def nodes_with_one(self, tags):
        """
        Return tdon with at least one of tags.
        """
        raise NotImplementedError
    
    def nodes_with_all(self, tags):
        """
        Return tdon with all of tags.
        """
        raise NotImplementedError

    # @@@@@@@@@@@@@@@@@@@
    # @@@ utilities @@@
    # @@@@@@@@@@@@@@@@@@@

    def __repr__(self):
        return (
            "\n"
            f"{self._application_state.tcp}\n"
            f"{'=' * len(str(self._application_state.tcp))}\n"
            f"{self._application_state.tdon[self._application_state.tcp]}\n"
            "\n"
        )

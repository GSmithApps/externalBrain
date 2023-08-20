import pickle
import os

class _MainDictOfNodes(dict):
    """
    The list of nodes.
    """

class _Position(frozenset):
    """
    A frozen set of tags.
    """

    def __str__(self) -> str:

        if self == _Position():
            return ''
        else:
            return set.__str__(self)[1:-1]
        
    def __init__(self, arg = None) -> None:
        if arg:
            super().__init__(arg)
        else:
            super().__init__()
    
    def union(self, other):

        return _Position(self.union(other))

    def difference(self, other):

        return _Position(self.difference(other))

class ExternalBrain:
    """
    What do I want this to be able to do?

    I want most of these methods to be able to
    accept a relative tuple
    """

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # @@@@@ Main UI Methods @@@@@@@@@
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    def __init__(self) -> None:
        self._position = _Position()

        self._main_dict_of_nodes = _MainDictOfNodes()

        self._create_node_at_position_if_empty()

        print(str(self))

    def absolute(self, key):
        
        self._absolute(key)

        self._create_node_at_position_if_empty()

        print(str(self))

    def _absolute(self, key):
        
        self._position = ExternalBrain._convert_key_to_frozen_set(key)

    def advance(self, key):
    
        self._advance(key)

        self._create_node_at_position_if_empty()

        print(str(self))

    def _advance(self, key):
    
        self._position = self._position.union(
            ExternalBrain._convert_key_to_frozen_set(key)
        )

    def retreat(self, key):
    
        self._retreat(key)

        self._create_node_at_position_if_empty()

        print(str(self))

    def _retreat(self, key):
    
        self._position = self._position.difference(
            ExternalBrain._convert_key_to_frozen_set(key)
        )

    def twist(self, key, key_minus):
        
        self._advance(key)

        self._retreat(key_minus)

        self._create_node_at_position_if_empty()

        print(str(self))

    def _create_node_at_position_if_empty(self):

        self._main_dict_of_nodes.setdefault(self._position, '')


    # @@@@@@@@@@@@@@@@@@@@@@@@@@
    # @@@@@ Set Methods @@@@@@@@
    # @@@@@@@@@@@@@@@@@@@@@@@@@@

    def write(self, val):

        self._main_dict_of_nodes[self._position] = val

        print(str(self))

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # @@@@@ Output Methods @@@@@@@@@
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    def __str__(self) -> str:
        key = self._position
        val = self._main_dict_of_nodes[key]
        return (
            "\n" +
            f"{key}" +
            "\n" +
            f"{'=' * len(str(key))}" +
            "\n" +
            f"{val}" +
            "\n"
        )

    def __repr__(self):
        return str(self)

    @property
    def all_tags(self):
        return set().union(*[key for key in self._main_dict_of_nodes.keys()])
    
    def all_keys(self):
        print('')
        [print(x) for x in self._main_dict_of_nodes.keys()]
        print('')

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # @@@@@ Utility Methods @@@@@@@@@
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    @staticmethod
    def _convert_key_to_frozen_set(key: str | set | _Position | dict):
        """
        Converts a key to a frozen set.

        Has nothing to do with whether the key is relative or full.
        """

        if isinstance(key, str):
            return _Position([key])

        elif isinstance(key, set):
            return _Position(key)

        elif isinstance(key, _Position):
            return key

        elif key == {}:
            return _Position()

        else:
            raise ValueError('Bad key.')


b = ExternalBrain()
b.advance('hi')
print(b)

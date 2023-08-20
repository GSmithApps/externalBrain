

from external_brain.tags_not_in_tsot_exception import TagsNotInTSOTException as _TagsNotInTSOTException

def tags_not_in_tsot(tags, application_state):
    """
    Return a frozenset of tags that are not in tsot.

    Raises
    ------

    TagsNotInTSOTException
    """

    _tags_not_in_tsot = tags.difference(application_state.tsot)

    if _tags_not_in_tsot:
        raise _TagsNotInTSOTException(f"{_tags_not_in_tsot} is/are not in the set of tags.")

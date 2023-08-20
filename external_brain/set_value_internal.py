"""
I see no reason to do any data validation here.
"""

def set_value_internal(value, application_state):
    """
    Set the node to value.
    """
    application_state.tdon[application_state.tcp] = value
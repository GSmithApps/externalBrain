"""

"""

import pickle

def print_output(application_state):
    """
    
    """

    print("")
    print(application_state.tcp)
    print('=' * len(str(application_state.tcp)))
    print(application_state.tdon[application_state.tcp])
    print("")
    print("")
    with open("data.pkl", "wb") as f:
        pickle.dump(application_state, f)
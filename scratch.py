# %%

import external_brain as eb
import pickle

# # %%

# eb.union_tf_with_tsot({'a'})

# # %%

# # pickle the eb object's _ApplicationState
# with open("data.pkl", "wb") as f:
#     pickle.dump(eb._application_state, f)

# %%


# Load the pickled object from the file
with open("data.pkl", "rb") as f:
    # eb._ApplicationState = pickle.load(f)
    my_obj = pickle.load(f)


# %%
my_obj.tsot


# %%
eb._application_state = my_obj
# %%
eb.union_tf_with_tsot('b')
# %%
eb._application_state.tsot
# %%

# %%

# from external_brain import ExternalBrain
import pickle

# # %%

# eb = ExternalBrain()

# eb.union_tf_with_tsot({'a'})

# # %%

# # pickle the eb object's _ApplicationState
# with open("data.pkl", "wb") as f:
#     pickle.dump(eb, f)

# %%


# Load the pickled object from the file
with open("data.pkl", "rb") as f:
    # eb._ApplicationState = pickle.load(f)
    my_obj = pickle.load(f)


# %%
my_obj.application_state.tsot


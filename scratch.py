# %%

from external_brain import ExternalBrain


# %%

eb = ExternalBrain('pickle')
# %%
eb._application_state.tsot
# %%
eb._application_state.tcp
# %%
eb.union_tf_with_tsot('c').union_tf_with_tsot('s')
# %%
eb.go_to('b')
# %%

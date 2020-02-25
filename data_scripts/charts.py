#%%
import numpy as np
import pandas as pd

data = pd.read_csv('../raw_data/energy.csv', header=0, index_col=0)
df_energy = pd.DataFrame(data, columns=data.columns, index=data.index)

data = pd.read_csv("../raw_data/major_indexes.csv", header=0, index_col=0)
df_major_indexes = pd.DataFrame(data, columns=data.columns, index=data.index)

data = pd.read_csv("../raw_data/metals.csv", header=0, index_col=0)
df_metals = pd.DataFrame(data, columns=data.columns, index=data.index)

#%%
df_energy.plot.line(rot=90)

#%%
df_major_indexes.plot.line(rot=90)

#%%
df_metals.plot.line(rot=90)

#%%

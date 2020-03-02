#%%
import numpy as np
import pandas as pd

data = pd.read_csv('../raw_data/energy.csv', header=0, index_col=0)
df_energy = pd.DataFrame(data, columns=data.columns, index=data.index)

data = pd.read_csv("../raw_data/major_indexes.csv", header=0, index_col=0)
df_major_indexes = pd.DataFrame(data, columns=data.columns, index=data.index)

data = pd.read_csv("../raw_data/metals.csv", header=0, index_col=0)
df_metals = pd.DataFrame(data, columns=data.columns, index=data.index)

data = pd.read_csv("../raw_data/yieldcurve.csv", header=0, index_col=0)
df_yieldcurve = pd.DataFrame(data, columns=data.columns, index=data.index)

data = pd.read_csv("../raw_data/currency.csv", header=0, index_col=0)
df_currency = pd.DataFrame(data, columns=data.columns, index=data.index)

#%%
df_energy.plot.line(rot=90, title="Wind and Solar ETF's outperorm traditional energy indexes")
#wind and solar ETF's are based off of equities prices and
#not commodities prices, like for oil and natural gas ETF's
#%%
df_major_indexes.plot.line(rot=90, title="Africa hit hard over past 12 months - brief recovery in Brazil")

#%%
df_metals.plot.line(rot=90, title="Palladium rises rapidly over past 12 months in comparison to other industrials and reserve metals")

#%%
test = df_yieldcurve.iloc[[0, -1]]
test = test.transpose()
test.plot.line(table=True, title="Yield curve inversion and parallel shift")

#%%
df_yieldcurve['10 Yr'].plot.line(title="10 year yields fall, pressuring equities prices upwards")


# %%
df_currency['UUP'].plot.line(rot=90, title = "Dollar index strengthening, but at a much lower pace")

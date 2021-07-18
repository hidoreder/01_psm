#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%%
df = pd.read_csv('./sample.csv')
del df['ID']
df.head()

#%%
df.describe()

# %%
df.hist(bins=50)
plt.tight_layout()
plt.show()


#%%
LUP_curve = df.groupby('LUP').size()[::-1].cumsum()/len(df)*100
LAP_curve = df.groupby('LAP').size()[::-1].cumsum()/len(df)*100
HAP_curve = df.groupby('HAP').size().cumsum()/len(df)*100
HUP_curve = df.groupby('HUP').size().cumsum()/len(df)*100


# %%
fig, ax = plt.subplots()

ax.set_ylabel('%')
ax.set_xlabel('price')
ax.set_ylabel('Cumulative curve[%]')

plt.plot(LUP_curve, c='r')
plt.plot(LAP_curve, c='m')
plt.plot(HAP_curve, c='c')
plt.plot(HUP_curve, c='b')

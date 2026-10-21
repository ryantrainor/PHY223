import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def period(l):
    return 2 * 3.14 * np.sqrt(l / 9.8)

np.random.seed(6563)
err = 0.1
lengths = np.arange(0.05,0.95,0.05)
nlen = len(lengths)

data = pd.DataFrame()
data['length'] = lengths
for i in range(1,6):
    data[f't{i}'] = period(data.length) + np.random.normal(0,err,nlen)

data.to_csv('test-pendulum-data.csv',index=False, float_format="%.2f")

cols = data.columns
data['t_mean'] = data[cols[1:]].mean(axis=1)
data['t_sig'] = data[cols[1:]].std(axis=1)

fig,ax=plt.subplots()
ax.errorbar(data['length'],data['t_mean'],data['t_sig'],fmt='k.')
ax.set_xlabel('Pendulum Length (m)')
ax.set_ylabel('Pendulum Period (s)')
fig.tight_layout()
# fig.show()
plt.show()
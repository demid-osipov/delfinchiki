import pandas as pd
from scipy import stats

df = pd.read_csv('resistance.csv', sep = ';')

ds = df['resistance']
print(stats.kstest(ds, 'norm', (ds.mean(), ds.std())))

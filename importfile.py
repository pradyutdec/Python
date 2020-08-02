##
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')


filename = 'Test4.csv'

data = pd.read_csv(filename, index_col=0)

df = data.head(5)

df = df.set_index(["HOUR"])

sd = df.reindex(columns=['DIFF','DIFF1'])

db = sd.diff(axis=1)

db.plot(kind = 'bar')

plt.show()

print(sd)


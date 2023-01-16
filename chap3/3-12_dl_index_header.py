import pandas as pd

df = pd.read_csv('test.csv')

kokugo = df.sort_values('国語', ascending=False)

kokugo.to_csv('export3.csv', index=False, header=False)

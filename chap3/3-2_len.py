import pandas as pd

df = pd.read_csv('test.csv')

print('データの件数=', len(df))
print('項目名      =', df.columns.values)
print('インデクス  =', df.index.values)
import pandas as pd

df = pd.read_csv('test.csv')

print('C子のデータ\n', df.loc[2])

print('C子とD郎のデータ\n', df.loc[[2, 3]])

print("C子の国語データ\n", df.loc[2]['国語'])
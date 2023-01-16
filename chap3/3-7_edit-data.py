import pandas as pd

df = pd.read_csv('test.csv')

print('数学の最高点', df['数学'].max())
print('数学の最低点', df['数学'].min())
print('数学の平均点', df['数学'].mean())
print('数学の中央値', df['数学'].median())
print('数学の合計', df['数学'].sum())

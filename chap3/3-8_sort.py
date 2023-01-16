import pandas as pd

df = pd.read_csv('test.csv')

kokugo = df.sort_values('国語', ascending=False)
print('国語の点数が高い順番に並べ替え\n', kokugo)

suugaku = df.sort_values('数学')
print('数学の点数が低い順に並べ替え\n', suugaku)

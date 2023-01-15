import pandas as pd

df = pd.read_csv('test.csv')

df['美術'] = [68, 73, 82 , 77, 94, 96]
print('列データ(美術)を追加\n',df)

df .loc[6] = ["G恵",90, 92, 94, 96, 92,98]
print('行データ(G恵)を追加\n', df)


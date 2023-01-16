import pandas as pd

df = pd.read_csv('test.csv')

print('行と列を入れ替える\n', df.T)

print('pythonのリストデータ化\n', df.values)

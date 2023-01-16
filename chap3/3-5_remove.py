import pandas as pd

df = pd.read_csv('test.csv')

# axis=1 列を削除
print("名前の列を削除\n", df.drop('名前', axis=1))
# axis=0 行を削除
print('インデクス2の行を削除\n', df.drop(2, axis=0))

import pandas as pd

df = pd.read_csv("test.csv")

# 1행의 데이터를 표시한다.
print("C의 데이터\n", df.loc[2])

# 여러 행의 데이터를 표시한다.
print("C와 D의 데이터", df.loc[[2,3]])

# 지정한 행의 지정한 열 데이터를 표시한다.
print("C의 국어데이터\n", df.loc[2]["국어"])
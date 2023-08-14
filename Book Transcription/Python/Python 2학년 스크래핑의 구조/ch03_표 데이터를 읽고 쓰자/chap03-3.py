import pandas as pd

df = pd.read_csv("test.csv")

# 1열의 데이터를 표시한다.
print("국어의 열 데이터\n",df["국어"])

# 여러 열의 데이터를 표시한다.
print("국어와 수학의 열 데이터\n",df[["국어","수학"]])
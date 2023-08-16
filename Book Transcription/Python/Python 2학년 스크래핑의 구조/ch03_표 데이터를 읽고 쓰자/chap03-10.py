import pandas as pd

df = pd.read_csv("test.csv")

# 행과 열을 바꾼다.
print("행과 열을 바꾼다\n", df.T)

# 데이터를 리스트로 만든다.
print("Python의 리스트 데이터화\n", df.values)
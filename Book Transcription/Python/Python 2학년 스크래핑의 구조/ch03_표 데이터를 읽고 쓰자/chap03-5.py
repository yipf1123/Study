import pandas as pd

df = pd.read_csv("test.csv")

# 1열의 데이터를 추가한다.
df["미술"] =[68, 73, 82, 77, 94, 96]
print("열 데이터(미술)를 추가\n", df)

# 1행의 데이터를 추가한다.
df.loc[6] = ["G", 98, 92, 94, 96, 92, 98]
print("헹 데이터(G)를 추가 \n", df)
import pandas as pd

df = pd.read_csv("test.csv")

# <이름> 열을 삭제한다
print("<이름> 열을 삭제\n", df.drop("이름", axis=1))

# 인덱스가 2인 행을 삭제한다.
print("인덱스가 2인 행을 삭제\n", df.drop(2, axis=0))

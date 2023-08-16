import pandas as pd

df = pd.read_csv("test.csv")

# 정렬해 표시한다.
kor = df.sort_values("국어",ascending=False)
print("국어 점수가 높은 순으로 정렬\n",kor)
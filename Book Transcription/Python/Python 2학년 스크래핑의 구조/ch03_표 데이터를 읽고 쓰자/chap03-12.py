import pandas as pd

df = pd.read_csv("test.csv")

# 국어 점수가 높은 순으로 정렬한다.
kor = df.sort_values("국어", ascending=False)

# CSV 파일로 출력한다(인덱스 삭제).
kor.to_csv("export2.csv", index=False)
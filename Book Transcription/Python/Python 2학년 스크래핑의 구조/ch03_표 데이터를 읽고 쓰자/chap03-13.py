import pandas as pd

df = pd.read_csv("test.csv")

kor = df.sort_values("국어", ascending=False)

# CSV 파일로 출력한다(인덱스와 헤더 삭제)
kor.to_csv("export3.csv", index=False, header=False)

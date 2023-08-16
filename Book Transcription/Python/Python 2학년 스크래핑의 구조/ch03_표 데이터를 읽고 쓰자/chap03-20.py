import pandas as pd
import openpyxl

df = pd.read_csv("test.csv")

#  국어 점수가 높은 순으로 정렬한다.
kor = df.sort_values("국어", ascending=False)

# 엑셀 파일로 출력한다.
kor.to_excel("csv_to_excel1.xlsx")
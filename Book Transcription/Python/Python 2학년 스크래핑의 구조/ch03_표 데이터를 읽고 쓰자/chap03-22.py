import pandas as pd
import openpyxl

df = pd.read_csv("test.csv")

kor = df.sort_values("국어", ascending=False)

# 하나의 엑셀 파일에 여러 개의 시트를 출력한다.
with pd.ExcelWriter("csv_to_excel3.xlsx") as writer :
    df.to_excel(writer, index=False, sheet_name="원본데이터")
    kor.to_excel(writer, index=False, sheet_name="국어로 정렬")
import pandas as pd
import openpyxl

# 엑셀 파일을 읽어 들인다.
df = pd.read_excel("csv_to_excel3.xlsx")
print(df)
df = pd.read_excel("csv_to_excel3.xlsx", sheet_name="국어로 정렬")
print(df)
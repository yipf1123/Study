import pandas as pd

# CSV 파일을 읽어 들인다.
df = pd.read_csv("test.csv")

# 표 데이터 정보를 표시한다.
print("데이터 건수 = ", len(df))
print("항목명 = ", df.columns.values)
print("인덱스 = ", df.index.values)




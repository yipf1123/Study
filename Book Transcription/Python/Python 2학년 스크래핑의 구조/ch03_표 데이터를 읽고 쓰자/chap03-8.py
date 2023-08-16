import pandas as pd

df = pd.read_csv("test.csv")

# 집계(최댓값, 평균값, 중앙값, 합계값 등)를 해 표시한다.
print("수학의 최고점 =",df["수학"].max())
print("수학의 최저점 =",df["수학"].min())
print("수학의 평균점 =",df["수학"].mean())
print("수학의 중앙값 =",df["수학"].median())
print("수학의 점수 합계 =",df["수학"].sum())
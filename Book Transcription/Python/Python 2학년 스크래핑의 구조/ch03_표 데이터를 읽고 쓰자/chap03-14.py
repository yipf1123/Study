import pandas as pd
import matplotlib.pyplot as plt

# 그래프에서 한글이 깨지는 문제 해결하기
from matplotlib import font_manager, rc
font_location = r'C:\Users\les80\AppData\Local\Microsoft\Windows\Fonts\BMEULJIROTTF.ttf'
font_name = font_manager.FontProperties(fname=font_location).get_name()
rc('font', family=font_name)

df = pd.read_csv("test.csv")

# 파일을 읽어 들인다.
df.plot() # 꺾은선 그래프
plt.show()
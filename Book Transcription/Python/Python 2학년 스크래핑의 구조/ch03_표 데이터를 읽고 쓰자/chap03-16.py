import pandas as pd
import matplotlib.pyplot as plt
# 그래프에서 한글이 깨지는 문제 해결하기
from matplotlib import font_manager, rc
font_location = r'C:\Users\les80\AppData\Local\Microsoft\Windows\Fonts\BMEULJIROTTF.ttf'
font_name = font_manager.FontProperties(fname=font_location).get_name()
rc('font', family=font_name)

df = pd.read_csv("test.csv", index_col=0)

# 국어에 대한 막대 그래프를 만들어 표시한다.
df["국어"].T.plot.barh()
plt.legend(loc="lower left")
plt.show()

# 국어와 수학에 대한 막대 그래프를 만들어 표시한다.
df[["국어", "수학"]].plot.barh()
plt.legend(loc="lower left")
plt.show()

# C군에 대한 막대 그래프를 만들어 표시한다.
df.loc["C"].plot.barh()
plt.legend(loc="lower left")
plt.show()

# C군에 대한 원 그래프를 만들어 표시한다.
df.loc["C"].plot.pie(labeldistance=0.6)
plt.legend(loc="lower left")
plt.show()
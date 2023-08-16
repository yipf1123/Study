import pandas as pd
import matplotlib.pyplot as plt
# 그래프에서 한글이 깨지는 문제 해결하기
from matplotlib import font_manager, rc
font_location = r'C:\Users\les80\AppData\Local\Microsoft\Windows\Fonts\BMEULJIROTTF.ttf'
font_name = font_manager.FontProperties(fname=font_location).get_name()
rc('font', family=font_name)
df = pd.read_csv("test.csv", index_col=0)

# 막대 그래프를 만들어 표시한다.
df.plot.bar()
plt.legend(loc="lower right")
plt.show()

# 막대 그래프(수평)를 만들어 표시한다.
df.plot.barh()
plt.legend(loc="lower left")
plt.show()

# 누적 막대그래프를 만들어 표시한다.
df.plot.bar(stacked=True)
plt.legend(loc="lower right")
plt.show()

# 상자 수염그래프를 만들어 표시한다.
df.plot.box()
plt.show()

# 면적 그래프를 만들어 표시한다.
df.plot.area()
plt.legend(loc="lower right")
plt.show()
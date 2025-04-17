import matplotlib.pyplot as plt
from matplotlib import font_manager

# 设置字体路径（以 Windows 为例）
font_path = "/System/Library/Fonts/Hiragino Sans GB.ttc"  # 黑体
my_font = font_manager.FontProperties(fname=font_path)

plt.plot([1, 2, 3], [4, 5, 6])
plt.title('测试标题', fontproperties=my_font)
plt.xlabel('横坐标', fontproperties=my_font)
plt.ylabel('纵坐标', fontproperties=my_font)
plt.show()
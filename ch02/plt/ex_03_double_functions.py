import numpy as np
import matplotlib.pyplot as plt


"""
一个坐标上画两个函数图像


"""



x = np.linspace(-10, 10, 400) #从-10，10之间，选择400个点

y1 = np.sin(x)
y2 = np.cos(x)


plt.plot(x, y1, label ='sin(x)')
plt.plot(x, y2, label ='cos(x)', linestyle='--') #虚线画cos
plt.legend()  # 显示图例， 显示线条的说明标签，这样看图的人就知道每一条线代表什么意思了

plt.title('sin(x) 和 cos(x)')


plt.grid(True)
plt.show()


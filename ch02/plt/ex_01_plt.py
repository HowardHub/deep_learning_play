import matplotlib.pyplot as plt
import numpy as np


"""
plt画图步骤
1.创建x数据
2.定义函数，计算y
3.绘图
4.添加标签和标题（可选）
5.显示图像



设置颜色        plt.plot(x,y,color='red)
设置线型        linestyle='--'、 '-.'、 ':'
设置线款        linewidth=2
设置图例        plt.legend()
设置图像大小     plg.figure(figsize=(8,6))

"""

# 1.创建x数据
x = np.linspace(-10, 10, 400) #从-10到10，生成400个数据点


# 2.定义函数，计算y
y = np.sin(x)
# 3.绘图
plt.plot(x, y, color='green', linestyle='-.', linewidth=3)



# 4.添加标签和标题（可选）
plt.xlabel('x')
plt.ylabel('y')
plt.title('y=sin(x)')
# 5.显示图像
plt.grid(True)  # 添加网格
plt.show()







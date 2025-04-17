import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

'''
画两个自变量的函数图像


'''

# 创建数据点
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)

# 定义两个函数
Z1 = np.sin(np.sqrt(X**2 + Y**2))  # 第一个函数：f(x,y) = sin(sqrt(x^2 + y^2))
Z2 = (X**2 + Y**2) / 10  # 第二个函数：f(x,y) = (x^2 + y^2)/10

# 创建图形和子图
fig = plt.figure(figsize=(15, 6))

# 第一个3D子图
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
surf1 = ax1.plot_surface(X, Y, Z1, cmap=cm.coolwarm, linewidth=0, antialiased=True)
ax1.set_title('f(x,y) = sin(sqrt(x² + y²))')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
fig.colorbar(surf1, ax=ax1, shrink=0.5, aspect=5)

# 第二个3D子图
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
surf2 = ax2.plot_surface(X, Y, Z2, cmap=cm.viridis, linewidth=0, antialiased=True)
ax2.set_title('f(x,y) = (x² + y²)/10')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
fig.colorbar(surf2, ax=ax2, shrink=0.5, aspect=5)

# 调整布局
plt.tight_layout()

# 显示图形
plt.show()
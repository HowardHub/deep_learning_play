import numpy as np
from matplotlib import pyplot as plt




"""
求偏导数的时候牢记：“别的变量都是常数。”



"""

def function2(x):
    return x[0]**2 + x[1]**2

#构造网格
x = np.linspace(-5,5, 100)
y = np.linspace(-5,5, 100)
X, Y = np.meshgrid(x, y)

#计算Z
Z = function2([X, Y])

#绘制3D图像
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')


#标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()


#求x0=3，x1=4，关于x0的偏导数，此时x1看作常数
def function_tmp1(x0):
    return x0**2 + 4 * 2

#求x0=3，x1=4，关于x1的偏导数，此时x0看作常数
def function_tmp2(x1):
    return x1**2 + 3 * 2


def numerical_diff(f, x):
    h = 1e-5
    return (f(x + h) - f(x - h)) / 2 * h

#偏导数和单变量的导数一样，都是求某个地方的斜率。
# 不过，偏导数需要将多个变量中的某一个变量定为目标变量，并将其他变量固定为某个值。
print(numerical_diff(function_tmp1, 3))
print(numerical_diff(function_tmp2, 4))














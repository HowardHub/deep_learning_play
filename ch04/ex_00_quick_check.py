import matplotlib.pyplot as plt
import numpy as np

# 定义函数
def f(x):
    return 0.01 * x**2 + 0.1 * x

# 数据范围
x = np.linspace(0, 20, 400)
y = f(x)

# 交点
x0 = 10
y0 = 2

# 画图
plt.figure(figsize=(6, 4))
plt.plot(x, y, label='Function $f(x)$')

# 手动画“有限长度”的虚线：
# 水平虚线：从x=0到x=10，y=2
plt.plot([0, x0], [y0, y0], linestyle='--', color='gray')
# 垂直虚线：从y=0到y=2，x=10
plt.plot([x0, x0], [0, y0], linestyle='--', color='gray')

# 圆圈标记交点
plt.plot(x0, y0, 'o', color='gray')

# 坐标标注
plt.text(x0 + 0.5, y0 + 0.2, f'({x0}, {y0})', color='black')

# 其它设置
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.title('Dashed Lines to a Point (10, 2)')
plt.grid(True)
plt.xlim(0, 20)
plt.ylim(-1, 6)
plt.legend()
plt.show()
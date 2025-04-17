# coding: utf-8
import numpy as np
import matplotlib.pylab as plt


def numerical_diff(f, x):
    h = 1e-4 # 0.0001
    return (f(x+h) - f(x-h)) / (2*h)


def function_1(x):
    return 0.01*x**2 + 0.1*x 


def tangent_line(f, x):
    d = numerical_diff(f, x)
    print(d)
    y = f(x) - d*x
    return lambda t: d*t + y
     
x = np.arange(0.0, 20.0, 0.1)
y = function_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")

tf = tangent_line(function_1, 5)
y2 = tf(x)

# 手动画“有限长度”的虚线：
# 水平虚线：从x=0到x=10，y=2
plt.plot([0, x0], [y0, y0], linestyle='--', color='gray')
# 垂直虚线：从y=0到y=2，x=10
plt.plot([x0, x0], [0, y0], linestyle='--', color='gray')


plt.plot(x, y)
plt.plot(x, y2)
plt.show()
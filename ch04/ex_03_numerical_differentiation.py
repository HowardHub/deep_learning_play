import numpy as np
import matplotlib.pylab as plt




#数值微分:利用微小的差分求导数的过程称为数值微分(numerical differentiation)



"""
这种计算微分的两个缺点：
    1.因为想把尽可能小的值赋给h（可以话，想让h无限接近0）​，所以h使用了10e-50（有50个连续的0的“0.00 ... 1”​）这个微小值。
        但是，这样反而产生了舍入误差(rounding error)。所谓舍入误差，是指因省略小数的精细部分的数值（比如，小数点第8位以后的数值）
        而造成最终的计算结果上的误差。
    2.真的导数”对应函数在x处的斜率（称为切线）​，但上述实现中计算的导数对应的是(x+h)和x之间的斜率。
        因此，真的导数（真的切线）和上述实现中得到的导数的值在严格意义上并不一致。
"""
def numerical_diff(f, x):
    h = 10e-50
    return (f(x+h) - f(x)) / h



"""
改进版本：
    1.让h的值大一些，避免舍入误差
    2.以x为中心，计算它左右两边的差分，所以也称为中心差分（而(x+h)和x之间的差分称为前向差分）​。
"""
def numerical_diff(f, x):
    h = 1e-4 #0.0001
    return ((f(x+h) - f(x-h))) / (2*h)










def function_1(x):
    return 0.01*x**2 + 0.1*x


x = np.arange(0.0, 20, 1)
y = function_1(x)

plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, y)



# 绘制切线（例如在 x=5 处的切线）
a = 5  # 选择切点的x坐标
f_a = function_1(a)
df_a = numerical_diff(function_1, a)
tangent_line = df_a * (x - a) + f_a  # 切线方程
plt.plot(x, tangent_line, '--', label=f'Tangent at x={a}')  # 绘制切线

plt.legend()
plt.grid()


plt.show()


print(numerical_diff(function_1, 5))
print(numerical_diff(function_1, 10))





def function_2(x):
    return x[0]**2 + x[1]**2

#x0=3,x1=4时，关于x0的偏导数
def function_tmp1(x0):
    return x0*x0 + 4.0*2.0
print(numerical_diff(function_tmp1, 3.0))


#求x0=3,x1=4时，关于x1的偏导数
def function_tmp2(x1):
    return 3.0*2.0 + x1*x1
print(numerical_diff(function_tmp2, 4.0))
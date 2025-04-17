import numpy as np
import matplotlib.pylab as plt

import numpy as np
import matplotlib.pyplot as plt




def simple_function(x):
    return 0.01 * (x**2) + 0.1 * x

def function_numerical_differentiation(f, x):
    h = 1e-5
    return (f(x+h) - f(x-h)) / 2*h

#在x=5处的切线为：y = 0.2x - 0.25
def tangent5(x):
    return 0.2*x - 0.25


#在x=10处的切线为：y = 0.3x - 1
def tangent10(x):
    return 0.3*x - 1


#用y = m(x-xi) + yi来求(xi,yi)处的切线表达式
def tangent_line(f, x):
    d = function_numerical_differentiation(f, x)
    y = f(x) - d*x
    return lambda t: d*t + y


x = np.linspace(0,20,100)

y = simple_function(x)

tangent_5 = tangent5(x)
print(simple_function(5))

tangent_10 = tangent10(x)
print((simple_function(10)))
print(function_numerical_differentiation(10))


plt.plot(x, y, label='y=f(x)')

plt.plot(x, tangent_5, label='diff5', linestyle = '--')
plt.scatter(5, 0.75, color='green', zorder=5)
plt.text(5, 0.75, f' 切点 ({5}, {0.75:.2f})', verticalalignment='bottom')

#plt.plot(x, tangent_10, label='diff10', linestyle='-.')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()






plt.show()





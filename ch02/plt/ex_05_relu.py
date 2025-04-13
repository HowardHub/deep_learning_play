import matplotlib.pyplot as plt

import numpy as np




def relu(x):
    #x = np.array([1, 3, 2, 0])
    #index = np.argmax(x)  # 输出: 1（因为最大值是3，索引为1）
    return np.maximum(0, x) #对输入数组 x 逐元素计算与 0 的最大值

x = np.linspace(-1, 5, 1000)
y = relu(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('relu')
plt.title('y=relu(x)')

plt.legend()
plt.show()





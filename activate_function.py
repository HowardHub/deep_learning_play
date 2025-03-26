import numpy as np
import matplotlib.pylab as plt

"""神经网络，可以从数据中自主地学习参数"""







"""阶跃函数"""
def step_function_simple(x):
    if x <= 0:
        return 0
    else:
        return 1
    
# 支持numpy数组的函数阶跃函数
def step_function_middle(x):
    y = x > 0
    return y.astype(int)


# 简化版本
def step_function(x):
    return np.array(x > 0, dtype = int)


# 画出阶跃函数的图像
x = np.arange(-5.0, 5.0, 0.2)
y = step_function(x)

plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()




#sigmoid激活函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))



x = np.arange(-5.0, 5.0, 0.2)
y = sigmoid(x)

plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()



# relu激活函数
def relu(x):
    return np.maximum(0, x)



x = np.arange(-5.0, 5.0, 0.2)
y = relu(x)

plt.plot(x, y)
plt.ylim(-3, 5)
plt.show()







"""
分类问题是数据属于哪一个类别的问题。回归问题是根据某个输入预测一个（连续的）数值的问题。
一般而言，回归问题用恒等函数，分类问题用softmax函数
"""

# softmax函数的实现
def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c) #防止溢出
    # 为了防止sum_exp_a太大，从而造成溢出，把每一个元素减去数组中的最大值，让和在一个小范围呢i
    sum_exp_a = sum(exp_a)
    y = exp_a / sum_exp_a
    return y


a = np.array([1,2,3])
y = softmax(a)
print(y)
print(np.sum(y))






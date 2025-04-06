
import numpy as np


def identity_function(x):
    return x


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c) #防止溢出
    # 为了防止sum_exp_a太大，从而造成溢出，把每一个元素减去数组中的最大值，让和在一个小范围呢i
    sum_exp_a = sum(exp_a)
    y = exp_a / sum_exp_a
    return y








################### 损失函数
#均方误差函数
def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t) ** 2)



#假设正确解为2
t = [0,0,1,0,0,0,0,0,0,0]
# 例1：“2”的概率最高的情况（0.6）
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
# print(mean_squared_error(np.array(y), np.array(t)))
# 例2：“7”的概率最高的情况（0.6）
y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
# print(mean_squared_error(np.array(y), np.array(t)))


#交叉墒误差函数
def cross_entropy_error(y ,t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))


t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
# print(cross_entropy_error(np.array(y), np.array(t)))

y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
# print(cross_entropy_error(np.array(y), np.array(t)))


#y是神经网络的输出，t是监督数据，适用于one-hot形式
# def cross_entropy_error(y, t):
#     if y.ndim == 1:
#         t = t.reshape(1, t.size)
#         y = y.reshape(1, y.size)

#     batch_size = y.shape[0]
#     return -np.sum(t * np.log(y + 1e-7)) / batch_size


# #适用于t是标签的形式（像“4”，“7”这样的标签）
# def cross_entropy_error(y, t):
#     if y.ndim == 1:
#         t = t.reshape(1, t.size)
#         y = y.reshape(1, y.size)
    
#     batch_size = y.shape[0]
#     return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size


def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
        
    # 教師データがone-hot-vectorの場合、正解ラベルのインデックスに変換
    if t.size == y.size:
        t = t.argmax(axis=1)
             
    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size





def function_2(x):
    return x[0]**2 + x[1]**2






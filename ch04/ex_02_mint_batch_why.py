import sys, os
sys.path.append(os.pardir) # 为了导入父目录中的文件而进行的设定

import numpy as np
from dataset.mnist import load_mnist


#为何使用MiniBatch?
'''
1.MNIST数据集的训练数据有60000个，如果以全部数据为对象求损失函数的和，则计算过程需要花费较长的时间。
2.如果遇到大数据，数据量会有几百万、几千万之多，这种情况下以全部数据为对象计算损失函数是不现实的。
'''




'''
需求
编写从训练数据中随机选择指定个数的数据的代码，以进行mini-batch学习。
'''


#导入数据
(x_train, t_train),(x_test, t_est) = load_mnist(one_hot_label = True)

train_size = x_train.shape[0] #训练数据大小
batch_size = 100
batch_mask = np.random.choice(train_size, batch_size)
print(batch_mask)

#挑选训练数据
x_batch = x_train[batch_mask] #花式索引
t_batch = t_train[batch_mask] #花式索引


print(x_batch)
print(t_batch)





#mini-batch兼容版的均方误差损失函数(one-hot)
def mean_squared_error(y, t):
    if y.ndim == 1:
        y = y.reshape(1, y.size)
        t = t.reshape(1, t.size)
    batch_size = y.shape[0]
    return 0.5 * np.sum((y-t)**2) / batch_size




#mini-batch兼容版的交叉墒损失函数(one-hot)
def cross_entropy_error(y, t):
    #兼容单个数据
    if y.ndim == 1:
        y = y.reshape(1, y.size)
        t = t.reshape(1, t.size)
    batch_size = y.shape[0]
    delta = 1e-7
    #因为是求和的操作，所以不需要指定axis。对y求对数，然后把y和t相乘得到一个ndim,shape相同的数据，再对数组进行求和。
    return -np.sum(t * np.log(y + delta)) / batch_size #可以在脑海里复现这个计算过程。


#mini-batch兼容版的均方误差损失函数(标签数据，2，3)
def cross_entropy_error_not_one_hot(y,t):
    if y.ndim == 1:
        y = y.reshape(1, y.size)
        t = t.reshape(1, t.size)
    batch_size = y.shape[0]
    return -np.sum(y[np.arange(batch_size), t] + 1e-7) / batch_size




print('mini-batch兼容版的均方误差损失函数-测试')
y = np.array([0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]) #2
t = np.array([0, 0, 1, 0, 0, 0, 0, 0, 0, 0]) #2
m1 = mean_squared_error(y, t)
print(m1)


y = np.array([0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]) #7
t = np.array([0, 0, 1, 0, 0, 0, 0, 0, 0, 0]) #2
m2 = mean_squared_error(y, t)
print(m2)

print(f'两个数据分别计算时，均方误差平均值={(m1+m2)/2}')


y = np.array([[0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0],[0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]])
t = np.array([[0, 0, 1, 0, 0, 0, 0, 0, 0, 0],[0, 0, 1, 0, 0, 0, 0, 0, 0, 0]])
print(f'两个数据批处理均方误差={mean_squared_error(y, t)}')


print('mini-batch兼容版的交叉墒损失函数-测试')
y = np.array([0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]) #2
t = np.array([0, 0, 1, 0, 0, 0, 0, 0, 0, 0]) #2
m1 = cross_entropy_error(y, t)
print(m1)


y = np.array([0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]) #7
t = np.array([0, 0, 1, 0, 0, 0, 0, 0, 0, 0]) #2
m2 = cross_entropy_error(y, t)
print(m2)
print(f'两个数据分别计算时，交叉墒误差平均值={(m1+m2)/2}')


y = np.array([[0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0],[0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]])
t = np.array([[0, 0, 1, 0, 0, 0, 0, 0, 0, 0],[0, 0, 1, 0, 0, 0, 0, 0, 0, 0]])
print(f'两个数据批处理均方误差={cross_entropy_error(y, t)}')






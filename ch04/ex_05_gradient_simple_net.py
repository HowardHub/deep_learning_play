import sys, os
sys.path.append(os.pardir)

import numpy as np
from common.functions import softmax, cross_entropy_error
from common.gradient import numerical_gradient





#神经网络的梯度指损失函数关于权重参数的梯度




class simpleNet:
    def __init__(self):
        #形状为2×3的权重参数
        self.W = np.random.randn(2, 3) #用高斯分布进行初始化


    def predict(self, x):
        return np.dot(x, self.W)
    

    #参数x接收输入数据，t接收正确解标签
    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)
        return loss
    


#测试simpleNet
net = simpleNet()
print(net.W) #权重参数


x = np.array([0.6, 0.9])
p = net.predict(x)
print(p)
print(np.argmax(p)) #最大索引值


t = np.array([0, 0, 1]) #正确解标签
print(net.loss(x, t))



#求梯度
def f(W):
    return net.loss(x, t)

dW = numerical_gradient(f, net.W)
print(dW)



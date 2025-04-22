import sys, os
sys.path.append(os.pardir)

import numpy as np
from common.functions import *
from common.gradient import numerical_gradient


"""
学习算法的实现
前提：神经网络存在合适的权重和偏置，调整权重和偏置以便拟合训练数据的过程称为“学习”​。

步骤1（mini-batch）
    从训练数据中随机选择一部分数据，这部分数据称为mini-batch，目标是减少mini-batch的损失函数值。

步骤2（计算梯度）
    为了减少mini-batch的损失函数的值，需要求出各个权重参数的梯度。梯度表示损失函数的值减少最多的方向。

步骤3（更新参数）
    将权重参数沿着梯度方向进行微小更新

步骤4（重复）
    重复步骤1、步骤2、步骤3

"""

def sigmoid_grad(x):
    return (1.0 - sigmoid(x)) * sigmoid(x)


class TwoLayerNet:
    def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
        #初始化权重
        self.params = {}
        self.params['W1'] = weight_init_std * np.random.randn(input_size, hidden_size)
        self.params['b1'] = np.zeros(hidden_size)
        self.params['W2'] = weight_init_std * np.random.randn(hidden_size, output_size)
        self.params['b2'] = np.zeros(output_size)


    def predict(self, x):
        W1, W2 = self.params['W1'], self.params['W2']
        b1, b2 = self.params['b1'], self.params['b2']

        a1 = np.dot(x, W1) + b1
        z1 = sigmoid(a1)
        a2 = np.dot(z1, W2) + b2
        y = softmax(a2)
        
        return y

    #x:输入数据， t:监督数据
    def loss(self, x, t):
        y = self.predict(x)
        return cross_entropy_error(y, t)
    

    def accuracy(self, x, t):
        y = self.predict(x)
        y = np.argmax(y, axis=1)
        t = np.argmax(t, axis=1)

        accuracy = np.sum(y == t) / float(x.shape[0])
        return accuracy


    #x:输入数据， t:监督数据
    def numerical_gradient(self, x, t):
        loss_W = lambda W: self.loss(x, t) #计算损失

        grads = {}
        grads['W1'] = numerical_gradient(loss_W, self.params['W1'])
        grads['b1'] = numerical_gradient(loss_W, self.params['b1'])
        grads['W2'] = numerical_gradient(loss_W, self.params['W2'])
        grads['b2'] = numerical_gradient(loss_W, self.params['b2'])

        return grads


    def gradient(self, x, t):
        W1, W2 = self.params['W1'], self.params['W2']
        b1, b2 = self.params['b1'], self.params['b2']
        batch_num = x.shape[0]

        # --- 前向传播 ---
        a1 = np.dot(x, W1) + b1            # 隐藏层线性变换
        z1 = sigmoid(a1)                   # 激活
        a2 = np.dot(z1, W2) + b2           # 输出层线性变换
        y = softmax(a2)                    # Softmax

        # --- 反向传播 ---
        # 输出层误差
        dy = (y - t) / batch_num           # 对 cross_entropy_error 求导后的误差

        # W2, b2 的梯度
        grads = {}
        grads['W2'] = np.dot(z1.T, dy)
        grads['b2'] = np.sum(dy, axis=0)

        # 隐藏层误差
        dz1 = np.dot(dy, W2.T)
        da1 = dz1 * z1 * (1 - z1)          # sigmoid 的导数：σ'(a)=σ(a)(1−σ(a))

        # W1, b1 的梯度
        grads['W1'] = np.dot(x.T, da1)
        grads['b1'] = np.sum(da1, axis=0)

        return grads
 


if __name__ == '__main__':

    net = TwoLayerNet(input_size=784, hidden_size=100, output_size=10)
    #params变量中保存了该神经网络所需的全部参数
    # print(net.params['W1'].shape) # (784, 100)
    # print(net.params['b1'].shape) # (100,)
    # print(net.params['W2'].shape) # (100, 10)
    # print(net.params['b2'].shape) # (10,)

    # #推理处理的实现
    # x = np.random.rand(100, 784)
    # y = net.predict(x)

    #使用numerical_gradient()方法计算梯度后，梯度的信息将保存在grads变量中
    x = np.random.rand(100, 784) #伪输入数据（100个）
    t = np.random.rand(100, 10) #伪正确解标签（100个） 
    # print(t)
    grad = net.numerical_gradient(x, t) #计算梯度

    print('求梯度结束')
    print(grad['W1'].shape)
    print(grad['b1'].shape)
    print(grad['W2'].shape)
    print(grad['b2'].shape)
    




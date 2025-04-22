import sys, os
sys.path.append(os.pardir)

import numpy as np
from ex_03_relu import Relu
from ch05.ex_05_affine import Affine
from common.gradient import numerical_gradient
from collections import OrderedDict
from ch05.ex_06_softmax_with_loss import SoftmaxWithLoss



"""
神经网络的学习步骤
前提：神经网络中有合适的权重和偏置，调整权重和偏置以便拟合训练数据的过程称为学习

步骤1（mini-batch）
    从训练数据中随机选择一部分数据

步骤2（计算梯度）
    计算损失函数关于各个权重参数的梯度

步骤3（更新参数）
    将权重参数沿梯度方向进行微小的更新

步骤4（重复）
    重复步骤1、步骤2、步骤3


"""




class TwoLayerNet:
    """基于层的两层神经网络
    """


    def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
        """初始化方法

        Args:
            input_size (_type_): 输入层的神经元数
            hidden_size (_type_): 隐藏层的神经元数
            output_size (_type_): 输出层的神经元数
            weight_init_std (float, optional): 初始化权重时，高斯分布的规模. Defaults to 0.01.
        """


        #初始化权重
        self.params = {}
        self.params['W1'] = weight_init_std * np.random.randn(input_size, hidden_size)
        self.params['b1'] = np.zeros(hidden_size)
        self.params['W2'] = weight_init_std * np.random.randn(hidden_size, output_size)
        self.params['b2'] = np.zeros(output_size)

        #生成层
        #layers保存神经网络的层的有序字典型变量
        self.layers = OrderedDict()
        self.layers['Affine1'] = Affine(self.params['W1'], self.params['b1'])
        self.layers['Relu1'] = Relu()
        self.layers['Affine2'] = Affine(self.params['W2'], self.params['b2'])

        #最后一层，本例为SoftmaxWithLoss
        self.lastLayer = SoftmaxWithLoss()

    


    def predict(self, x):
        """进行识别（推理）

        Args:
            x (_type_): 图像数据

        Returns:
            _type_: _description_
        """
        for layer in self.layers.values():
            x = layer.forward(x)

        return x
    

    def loss(self, x, t):
        """计算损失函数的值

        Args:
            x (_type_): 图像数据
            t (_type_): 正确解标签

        Returns:
            _type_: _description_
        """
        y = self.predict(x)
        return self.lastLayer.forward(y ,t)
    


    def accuracy(self, x, t):
        """计算识别精度

        Args:
            x (_type_): _description_
            t (_type_): _description_

        Returns:
            _type_: _description_
        """
        y = self.predict(x)
        y = np.argmax(y, axis=1)
        if t.ndim != 1 : t = np.argmax(t, axis=1)
        accuracy = np.sum(y == t) / float(x.shape[0])
        return accuracy
    

    def numerical_gradient(self, x, t):
        """通过数值微分计算关于权重参数的梯度

        Args:
            x (_type_): _description_
            t (_type_): _description_

        Returns:
            _type_: _description_
        """

        losss_W = lambda W: self.loss(x, t)
        
        grad = {}
        grad['W1'] = numerical_gradient(losss_W, self.params['W1'])
        grad['b1'] = numerical_gradient(losss_W, self.params['b1'])
        grad['W2'] = numerical_gradient(losss_W, self.params['W2'])
        grad['b2'] = numerical_gradient(losss_W, self.params['b2'])

        return grad




    def gradient(self, x, t):
        """通过误差反向传播计算关于权重参数的梯度

        Args:
            x (_type_): _description_
            t (_type_): _description_

        Returns:
            _type_: _description_
        """

        #forward
        self.loss(x, t)

        #backward
        dout = 1
        dout = self.lastLayer.backward(dout)

        layers = list(self.layers.values())
        layers.reverse()
        for layer in layers:
            dout = layer.backward(dout)

        #设定
        grads = {}
        grads['W1'] = self.layers['Affine1'].dW
        grads['b1'] = self.layers['Affine1'].db
        grads['W2'] = self.layers['Affine2'].dW
        grads['b2'] = self.layers['Affine2'].db

        return grads
    





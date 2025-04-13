import numpy as np


"""
使用numpy实现一个神经网络，结构如下：
输入层（第0层）有2个神经元，
第1个隐藏层（第1层）有3个神经元，
第2个隐藏层（第2层）有2个神经元，
输出层（第3层）有2个神经元


输入.shape=(n,2)
W1.shape=(2,3)
W2.shape=(3,2)
W3.shape=(2,2)
输出.shape=(n,2)


tips:连接有几层，权重参数W，偏置参数b就有几个。这里是3层连接，所以W和b各有3个。
"""

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


class SimpleNetwork:

    def __init__(self):
        self.W1 = np.random.randn(2,3)
        self.b1 = np.random.randn(3)
        self.W2 = np.random.randn(3,2)
        self.b2 = np.random.randn(2)
        self.W3 = np.random.randn(2,2)
        self.b3 = np.random.randn(2)

    

    def forward(self, x):
        a1 = np.dot(x, self.W1) + self.b1
        z1 = sigmoid(a1)
        a2 = np.dot(z1, self.W2) + self.b2
        z2 = sigmoid(a2)
        a3 = np.dot(z2, self.W3) + self.b3
        z3 = sigmoid(a3)
        return z3


simpleNetWork = SimpleNetwork()
x = np.random.randn(2) #造1行数据
y = simpleNetWork.forward(x)
print(y) #输出10行结果


























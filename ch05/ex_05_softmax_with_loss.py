import sys, os
sys.path.append(os.pardir)


import numpy as np
from common.functions import softmax, cross_entropy_error


#softmax将输出归一化
#loss能够计算输出y和标签t的损失


#Softmax层将输入[a1,a2,a3,...]正规化，输出[y1,y2,y3,...]
#Cross Entropy Error层接收Softmax的输出[y1,y2,y3,...]和监督标签[t1,t2,t3,...]，从这些数据中输出损失L

class SoftmaxWithLoss:
    def __init__(self):
        self.loss = None #损失
        self.y = None #softmax的输出
        self.t = None #监督数据

    def forward(self, x, t):
        self.t = t
        self.y = softmax(x)
        self.loss = cross_entropy_error(self.y, self.t)
        return self.loss
    
    def backward(self, dout=1):
        batch_size = self.t.shape[0]
        dx = (self.y - self.t) / batch_size

        return dx



















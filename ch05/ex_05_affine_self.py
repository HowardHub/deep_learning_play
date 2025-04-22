import numpy as np


'''
这些实现都是根据公式来的，
y = X * W + b

梯度需要自己根据计算图推导。
dl/dX
dl/dW
dl/db

'''

class Affine:
    def __init__(self, W, b):
        self.W = W
        self.b = b
        self.X = None


    def forward(self, X):
        self.X = X
        return np.dot(X, self.W) + self.b
    




    def backward(self, dout):
        dx = np.dot(dout, self.W.T)
        dW = np.dot(self.X.T, dout)
        db = np.sum(dout, axis=0)
        return dW, db
    






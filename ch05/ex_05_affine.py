import numpy as np


'''
在神经网络的反向传播算法中，每一层需要完成两个主要任务：
    计算该层参数（权重W和偏置b）的梯度
    计算输入x相对于损失函数的梯度，以便传递给前一层




'''
# affine 仿射层,负责矩阵乘积， y = Wx + b
class Affine:
    def __init__(self, W, b):
        self.W = W
        self.b = b
        self.x = None

        #本层的梯度要保存起来
        self.dW = None
        self.db = None

        #保留输入的形状
        self.original_shape = None


    def forward(self, x):
        self.original_shape = x.shape
        #将输入的形状变为矩阵，第一个维度的shape（代表数据的个数）保持不变，其他的维度自动计算成第二个维度
        x = x.reshape(x.shape[0], -1)
        self.x = x
        out = np.dot(x, self.W) + self.b
        return out
    






    def backward(self, dout):
        #dout为上游传递过来的值
        dx = np.dot(dout, self.W.T)
        self.dW = np.dot(self.x.T, dout)
        #每个样本对应的输出都受到同一个偏置项 b 的影响
        #所以偏置的梯度是所有样本贡献的梯度之和
        #axis=0 表示沿着第一个维度（样本维度）求和
        self.db = np.sum(dout, axis=0)
        #dx 表示损失函数相对于输入x的梯度，这正是前一层需要的信息
        #返回dx是为了把梯度信息继续向前传递

        #把dx重新变了输入前的样子
        dx = dx.reshape(*self.original_shape)
        return dx
    




arr = np.array([[1,2], [3,4]])
db = np.sum(arr, axis=0)
print(db)

X = np.random.rand(2)
W = np.random.rand(2,3)
b = np.random.rand(3)

print(np.dot(X,W))






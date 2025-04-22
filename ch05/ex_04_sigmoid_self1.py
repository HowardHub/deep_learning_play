import numpy as np



class Sigmoid:


    def __init__(self):
        #保存输出，因为backward时要用到。
        self.out = None

    def forward(self, x):
        out = 1 / (1 + np.exp(-x))
        self.out = out
        return out
    
    #sigmoid的导函数是Df = y(1-y)，其中y是sigmoid的原函数
    def backward(self, dout):
        dx = dout * (self.out) * (1 - self.out)
        return dx
    

    
print('sigmoid层针对向量输入测试=========》')
arr = np.array([1, -6, 3, 0, 2, -3])
sigmoid = Sigmoid()
out = sigmoid.forward(arr)
print(f'sigmoid的foward输出是{out}')

dout = np.array([1, 0, -2, 0, 5, -3])
dout = sigmoid.backward(dout)
print(f'sigmoid的backward输出是{dout}')



print('\nsigmoid针对矩阵输入测试=========》')
arr = np.array([[10, 3, -5],
                [-8,  6, 2],
                [9,  2, 0],
                [7,  -5, 1]])

sigmoid = Sigmoid()
out = sigmoid.forward(arr)
print(f'sigmoid的foward输出是\n{out}')

dout = np.array([[-1, 3, 5],
                [8,  6, 2],
                [-9,  2, 0],
                [7,  5, -1]])
dout = sigmoid.backward(dout)
print(f'sigmoid的backward输出是\n{dout}')







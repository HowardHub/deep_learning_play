
import numpy as np

class Relu:
    def __init__(self):
        self.mask = None


    def forward(self, x):
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0
        return out
    

    def backward(self, dout):
        #针对dout>0的部分，原样输出；针对dout<=0的部分，强制为0
        dout[self.mask] = 0
        dx = dout
        return dx
    
print('relu针对向量输入测试=========》')
arr = np.array([1, -6, 3, 0, 2, -3])
relu = Relu()
out = relu.forward(arr)
print(f'relu的foward输出是{out}')

dout = np.array([1, 0, -2, 0, 5, -3])
dout = relu.backward(dout)
print(f'relu的backward输出是{dout}')





print('relu针对矩阵输入测试=========》')
arr = np.array([[10, 3, -5],
                [-8,  6, 2],
                [9,  2, 0],
                [7,  -5, 1]])

relu = Relu()
out = relu.forward(arr)
print(f'relu的foward输出是\n{out}')

dout = np.array([[-1, 3, 5],
                [8,  6, 2],
                [-9,  2, 0],
                [7,  5, -1]])
dout = relu.backward(dout)
print(f'relu的backward输出是\n{dout}')







import numpy as np



#在神经网络的层的实现中，一般假定forward()和backward()的参数是NumPy数组

class Relu:
    def __init__(self):
        #这个变量mask是由True/False构成的NumPy数组，
        #它会把正向传播时的输入x的元素中小于等于0的地方保存为True，其他地方（大于0的元素）保存为False
        self.mask = None


    def forward(self, x):
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0
        return out
    
        
    def backward(self, dout):
        dout[self.mask] = 0
        dx = dout
        return dx
    

    

x = np.array([[1.0, -5.0], [-2.0, 3.0]])
print(x)
mask = (x < 0)
print(mask)





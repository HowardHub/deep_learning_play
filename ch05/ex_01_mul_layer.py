import numpy as np


"""
层的实现中有两个共通的方法（接口）forward()和backward()。forward()对应正向传播，backward()对应反向传播

反向传播推导过程，就是沿着正向传播的路径反向地、逐步地运用链式法则，求解损失函数对每个参数的梯度。
通过计算图的方式，可以清晰而直观地理解梯度是如何一步步被计算和传播的。

"""

#反向传播：乘法层的实现

class MulLayer:
    def __init__(self):
        #定义两个变量，并赋值为None
        self.x = None
        self.y = None

    
    def forward(self, x, y):
        #前向传播时，把x,y初始化
        self.x = x
        self.y = y
        out = x * y
        return out


    def backward(self, dout):
        dx = dout * self.y #翻转x和y
        dy = dout * self.x 

        return dx, dy
    


apple = 100
apple_num = 2
tax = 1.1

#layer
mul_apple_layer = MulLayer()
mul_tax_layer = MulLayer()

#forward
apple_price = mul_apple_layer.forward(apple, apple_num)
price = mul_tax_layer.forward(apple_price, tax)
print(price)


#backward
dprice = 1
dapple_price, dtax = mul_tax_layer.backward(dprice)
dapple, dapple_num = mul_apple_layer.backward(dapple_price)
print(dapple, dapple_num, dtax)

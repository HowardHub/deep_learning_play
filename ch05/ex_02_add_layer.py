import numpy as np
from  ex_01_mul_layer import MulLayer

"""
加法层的实现
"""


class AddLayer:
    def __init__(self):
        pass

    def foward(self, x, y):
        return x + y
    

    def backward(self, dout):
        #dout为上游传递过来的值，将上游传递过来的导数，原封不动地传递给下游
        dx = dout * 1
        dy = dout *1
        return dx, dy
    

"""
首先，生成必要的层，以合适的顺序调用正向传播的forward()方法。
然后，用与正向传播相反的顺序调用反向传播的backward()方法，就可以求出想要的导数。



"""





apple = 100
apple_num = 2
orange = 150
orange_num = 3
tax = 1.1

#layer
mul_apple_layer = MulLayer()
mul_orange_layer = MulLayer()
add_apple_orange_layer = AddLayer()
mul_tax_layer = MulLayer()



#forward
apple_price = mul_apple_layer.forward(apple, apple_num)
orange_price = mul_orange_layer.forward(orange,orange_num)
all_price = add_apple_orange_layer.foward(apple_price, orange_price)
price = mul_tax_layer.forward(all_price, tax)
print(price )

#backward
dprice = 1
dall_price, dtax = mul_tax_layer.backward(dprice)
dapple_price, dornage_price = add_apple_orange_layer.backward(dall_price)
dorange, dornage_num = mul_orange_layer.backward(dornage_price)
dapple, dapple_num = mul_apple_layer.backward(dapple_price)






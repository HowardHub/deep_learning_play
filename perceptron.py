import numpy as np


"""感知机，实现门电路
   偏置的参数，用于控制神经元被激活的容易程度。
   权重的参数，用于控制各个信号的重要性。
   0, b + w1x1 + w2x2 <= 0
   1, b + w1x1 + w2x2 > 0

"""


"""与门电路"""
def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    y = x1 * w1 + x2 * w2
    if y <= theta:
        return 0
    else:
        return 1
    


print(AND(0,0))
print(AND(0,1))
print(AND(1,0))
print(AND(1,1))

"""与非门电路"""
def NAND(x1, x2):
    w1, w2, theta = -0.5, -0.5, -0.7
    y = x1 * w1 + x2 * w2
    if y <= theta:
        return 0
    else:
        return 1
    
print(NAND(0,0))
print(NAND(0,1))
print(NAND(1,0))
print(NAND(1,1))



"""或门电路"""
def OR(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.4
    y = w1 * x1 + w2 * x2
    if y <= theta:
        return 0
    else:
        return 1
    
print(OR(0,0))
print(OR(0,1))
print(OR(1,0))
print(OR(1,1))






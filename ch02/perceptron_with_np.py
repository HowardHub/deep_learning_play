import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else: 
        return 1
    

print('AND结果')
print(AND(0,0))
print(AND(0,1))
print(AND(1,0))
print(AND(1,1))


def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
    

print('NAND结果')
print(NAND(0,0))
print(NAND(0,1))
print(NAND(1,0))
print(NAND(1,1))



# 或门电路
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.4
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
    
print('OR结果')
print(OR(0,0))
print(OR(0,1))
print(OR(1,0))
print(OR(1,1))



# 异或门电路：将或门电路的输出和与非门电路的输出，作为与门电路的输入
# 从而得到异或门电路
def XOR(x1, x2):
    or_output = OR(x1, x2)
    nand_output = NAND(x1 ,x2)
    and_output = AND(or_output, nand_output)
    return and_output
print('异或的结果')
print(XOR(0,0))
print(XOR(0,1))
print(XOR(1,0))
print(XOR(1,1))